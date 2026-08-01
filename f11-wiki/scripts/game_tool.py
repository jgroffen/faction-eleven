#!/usr/bin/env python3
"""Author game-development notes in an LLM Wiki — a living game design document.

Standard library only. Scaffolds and maintains eight source-exempt note types — `game-mechanic`,
`lore`, `quest`, `level`, `item`, `character`, `faction`, `location` — wiring the links between
them, keeping the managed rollup blocks current, then running the core `wiki_tool.py` gate. The
skills supply the content; this tool keeps the notes, links and rollups consistent.

It's built to sit alongside the `software-development` plugin: a `game-mechanic` can link to the
`feature`(s) that implement it. Those cross-plugin links are validated only when
software-development is installed; otherwise they're accepted with a warning.

Commands:
  new-mechanic --name N [--state S] [--category C] [--feature SD-SLUG]... [--related SLUG]...
               [--summary S] [--replace]
                      Create/update a mechanic. --state: concept, prototyped, tuned, shipped, cut.
  new-lore --title T [--canon C] [--era E] [--character SLUG]... [--faction SLUG]...
           [--location SLUG]... [--summary S] [--replace]
                      Create/update a lore note. --canon: proposed, canon, retconned, non-canon.
  new-quest --title T [--status S] [--type T] [--giver CHAR] [--location LOC] [--mechanic SLUG]...
            [--reward ITEM]... [--prereq QUEST]... [--summary S] [--replace]
                      Create/update a quest. --status: design, blockout, scripted, shipped, cut.
  new-level --title T [--status S] [--location LOC] [--mechanic SLUG]... [--quest SLUG]...
            [--enemy CHAR]... [--summary S] [--replace]
                      Create/update a level. --status: design, blockout, art, polished, shipped, cut.
  new-item --name N [--type T] [--rarity R] [--cost C] [--mechanic SLUG]... [--source S]
           [--summary S] [--replace]
                      Create/update an item.
  new-character --name N [--role R] [--faction FAC] [--home LOC] [--summary S] [--replace]
                      Create/update a character.
  new-faction --name N [--homeland LOC] [--ally FAC]... [--enemy FAC]... [--summary S] [--replace]
                      Create/update a faction.
  new-location --name N [--parent LOC] [--faction FAC] [--summary S] [--replace]
                      Create/update a location.
  set-status --note SLUG --status VALUE
                      Move a note along its lifecycle, validating against that type's vocabulary
                      (game-mechanic.state / quest.quest_status / level.level_status /
                      lore.canon).
  list-notes [--query Q] [--tag TAG]
                      List notes from Wiki/catalog.jsonl — their slugs are what you pass to the
                      link flags above.
  refresh             Rebuild every managed rollup block from the notes' frontmatter.
  status              Design rollup: mechanics/quests/levels by lifecycle, lore by canon, and the
                      catalog counts.

All `new-*` commands are idempotent on title/name: re-run to update in place, preserving prose in
unmanaged sections. List arguments merge; pass --replace to overwrite them.

All eight types are source-exempt. Ground the world in itself with `[[wikilinks]]`; do not invent
characters, places or systems that aren't authored.
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:  # shared helpers from the core template (scripts/wiki_notes.py)
    from wiki_notes import (
        die, emit_frontmatter, existing_created, rel, replace_block, run_gate, slug, today)
except ImportError:
    print("error: this vault's core is missing scripts/wiki_notes.py. Update it from "
          "llm-wiki-core (re-copy template/. into the vault), then re-run.", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
WIKI_TOOL = ROOT / "scripts" / "wiki_tool.py"
CATALOG = ROOT / "Wiki" / "catalog.jsonl"

# --------------------------------------------------------------------------- #
# The eight note types this plugin registers (mirrors plugin/manifest.json)
# --------------------------------------------------------------------------- #
TYPES = {
    "game-mechanic": {"folder": "Wiki/GameMechanics", "status_field": "state"},
    "lore":          {"folder": "Wiki/Lore",          "status_field": "canon"},
    "quest":         {"folder": "Wiki/Quests",        "status_field": "quest_status"},
    "level":         {"folder": "Wiki/Levels",        "status_field": "level_status"},
    "item":          {"folder": "Wiki/Items"},
    "character":     {"folder": "Wiki/Characters"},
    "faction":       {"folder": "Wiki/Factions"},
    "location":      {"folder": "Wiki/Locations"},
}

MECHANIC_STATES = ["concept", "prototyped", "tuned", "shipped", "cut"]
QUEST_STATUSES = ["design", "blockout", "scripted", "shipped", "cut"]
LEVEL_STATUSES = ["design", "blockout", "art", "polished", "shipped", "cut"]
CANON_STATES = ["proposed", "canon", "retconned", "non-canon"]

VOCAB = {"game-mechanic": MECHANIC_STATES, "quest": QUEST_STATUSES,
         "level": LEVEL_STATUSES, "lore": CANON_STATES}

# The software-development plugin's feature folder — for cross-plugin game-mechanic links.
SD_FEATURES = "Wiki/Features"

# Managed rollup regions the tool owns inside note bodies (prefix `gd:`).
USED_IN_START, USED_IN_END = "<!-- gd:used-in:start -->", "<!-- gd:used-in:end -->"
QUESTS_START, QUESTS_END = "<!-- gd:quests:start -->", "<!-- gd:quests:end -->"
MEMBERS_START, MEMBERS_END = "<!-- gd:members:start -->", "<!-- gd:members:end -->"
SET_HERE_START, SET_HERE_END = "<!-- gd:set-here:start -->", "<!-- gd:set-here:end -->"


def require_plugin():
    if not WIKI_TOOL.exists():
        die("this folder is not an LLM Wiki (no scripts/wiki_tool.py). "
            "Set up an llm-wiki first, then install this plugin into it.")
    if not (ROOT / TYPES["game-mechanic"]["folder"]).is_dir():
        die("the game-development plugin is not installed (no Wiki/GameMechanics/). "
            "Install this plugin into the vault first: plugins/install-plugins.py")


# --------------------------------------------------------------------------- #
# Note read/write (full frontmatter, including list fields)
# --------------------------------------------------------------------------- #
def _unquote(value):
    v = value.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return v


def split_note(path):
    """Return (frontmatter dict incl. lists, body text) for an existing note."""
    text = Path(path).read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    close = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if close is None:
        return {}, text
    fm, key = {}, None
    for line in lines[1:close]:
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if m:
            key, raw = m.group(1), m.group(2).strip()
            # A bare `key:` or `key: []` opens a list; anything else is a scalar.
            fm[key] = [] if raw in ("", "[]") else _unquote(raw)
        elif key is not None and line.strip().startswith("- "):
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(_unquote(line.strip()[2:]))
    return fm, "\n".join(lines[close + 1:]).lstrip("\n")


def write_full(path, fm, body):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(emit_frontmatter(fm) + "\n\n" + body.strip() + "\n", encoding="utf-8")


def note_path(tag, note_slug):
    return ROOT / TYPES[tag]["folder"] / f"{note_slug}.md"


def load_notes(tag):
    """Yield (slug, frontmatter, body) for every note of a type (skipping folder indexes)."""
    folder = ROOT / TYPES[tag]["folder"]
    if not folder.is_dir():
        return
    for path in sorted(folder.glob("*.md")):
        if path.stem == "index":
            continue
        fm, body = split_note(path)
        yield path.stem, fm, body


def all_slugs(tag):
    return [s for s, _fm, _body in load_notes(tag)]


def find_note(note_slug):
    """Locate a note by slug across the plugin's types. Returns (tag, path) or dies."""
    s = slug(note_slug)
    for tag in TYPES:
        if note_path(tag, s).exists():
            return tag, note_path(tag, s)
    die(f"no game-development note '{s}' in this vault. "
        "List what exists with: python3 scripts/game_tool.py list-notes")


def require_slugs(values, tag, flag):
    """Validate that each referenced slug exists, so notes can't cite an unauthored part of the
    world. Returns the normalized slugs."""
    out = []
    for value in values or []:
        s = slug(value)
        if not note_path(tag, s).exists():
            existing = ", ".join(all_slugs(tag)) or "(none yet)"
            die(f"{flag} '{s}': no {tag} note by that name. Existing {tag}s: {existing}\n"
                f"Create it first, or fix the slug — don't reference something that isn't there.")
        out.append(s)
    return out


def require_external(values, folder, plugin, flag):
    """Validate slugs against another plugin's folder, but only if that plugin is installed.

    Cross-plugin links (game-mechanic -> software-development feature) should never hard-fail this
    plugin: if `folder` is absent the other plugin isn't installed, so we accept the links with a
    warning rather than dying."""
    out = [slug(v) for v in values or []]
    if not out:
        return out
    target = ROOT / folder
    if not target.is_dir():
        print(f"  note: {plugin} is not installed — keeping {flag} link(s) unverified: "
              f"{', '.join(out)}", file=sys.stderr)
        return out
    for s in out:
        if not (target / f"{s}.md").exists():
            existing = ", ".join(sorted(p.stem for p in target.glob("*.md")
                                        if p.stem != "index")) or "(none yet)"
            die(f"{flag} '{s}': no {plugin} note by that name. Existing: {existing}\n"
                "Create it in that plugin first, or fix the slug.")
    return out


def merge_list(existing, incoming, replace):
    """Union (order-preserving) unless --replace was passed."""
    if replace:
        return list(dict.fromkeys(incoming))
    return list(dict.fromkeys(list(existing or []) + list(incoming or [])))


def choice(value, allowed, flag):
    if value is None:
        return None
    v = str(value).strip().lower()
    if v not in allowed:
        die(f"{flag} '{value}' is not one of: {', '.join(allowed)}")
    return v


# --------------------------------------------------------------------------- #
# Body helpers
# --------------------------------------------------------------------------- #
def set_meta_line(body, prefix, line):
    """Replace the first body line starting with `prefix`, or insert it after the title."""
    lines = body.split("\n")
    for i, existing in enumerate(lines):
        if existing.startswith(prefix):
            lines[i] = line
            return "\n".join(lines)
    for i, existing in enumerate(lines):
        if existing.startswith("# "):
            lines[i + 1:i + 1] = ["", line]
            return "\n".join(lines)
    return line + "\n\n" + body


def set_section(body, header, content):
    """Replace the text under `## header` (up to the next `## `), appending the section if new."""
    if not content:
        return body
    pattern = re.compile(r"(^## " + re.escape(header) + r"[ \t]*$)(.*?)(?=^## |\Z)",
                         re.M | re.S)
    if pattern.search(body):
        return pattern.sub(lambda m: m.group(1) + "\n\n" + content.strip() + "\n\n", body)
    return body.rstrip() + f"\n\n## {header}\n\n{content.strip()}\n"


def set_lead(body, text):
    """Replace the lead paragraph — the prose between the `# Title` and the next block."""
    if not text:
        return body
    lines = body.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if start is None:
        return text.strip() + "\n\n" + body
    i = start + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    end = i
    while end < len(lines) and lines[end].strip() \
            and not lines[end].startswith(("#", "**", "<!--", "- ")):
        end += 1
    lines[i:end] = [text.strip()]
    return "\n".join(lines)


def template_body(tag, title):
    """Start a new note from the vault's `_templates/<tag>-note.md`, so the notes this tool
    writes match the templates a human would use (and any tailoring done to them)."""
    path = ROOT / "_templates" / f"{tag}-note.md"
    if path.exists():
        _fm, body = split_note(path)
        return re.sub(r"^# .*$", f"# {title}", body, count=1, flags=re.M)
    return f"# {title}\n"


def optlink(slug_value, label=None):
    """A `**Label:** [[slug]]` fragment, or empty when the slug is blank."""
    return f"[[{slug_value}]]" if slug_value else "—"


# --------------------------------------------------------------------------- #
# Note creation / update
# --------------------------------------------------------------------------- #
def upsert(tag, title, fields, sections, meta_lines, lead=None):
    """Create or update a note of `tag` titled `title`.

    A new note starts from the vault's template; sections the caller doesn't supply keep the
    template's guidance prose, which is the skill's cue to fill them in. Managed rollup blocks
    already live in the templates, so they don't need re-inserting here — `refresh_all` fills them.
    """
    note_slug = slug(title)
    path = note_path(tag, note_slug)
    exists = path.exists()
    fm, body = split_note(path) if exists else ({}, template_body(tag, title))

    core = {
        "tags": [tag],
        "topics": fm.get("topics", []),
        "status": fm.get("status", "seed"),
        "created": existing_created(path) or today(),
        "updated": today(),
        "sources": [],
        "source_count": 0,
        "aliases": fm.get("aliases", []),
    }
    merged = {**fm, **core, **fields}
    ordered = {k: merged[k] for k in core if k in merged}
    ordered.update({k: v for k, v in merged.items() if k not in ordered})

    body = set_lead(body, lead)
    for prefix, line in meta_lines:
        body = set_meta_line(body, prefix, line)
    for header, content in sections.items():
        body = set_section(body, header, content)

    write_full(path, ordered, body)
    print(f"  {'updated' if exists else 'created'} {rel(path)}")
    return note_slug


# --------------------------------------------------------------------------- #
# Commands: new-*
# --------------------------------------------------------------------------- #
def cmd_new_mechanic(args):
    require_plugin()
    path = note_path("game-mechanic", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    state = choice(args.state, MECHANIC_STATES, "--state") or fm.get("state") or "concept"
    category = args.category if args.category is not None else fm.get("category", "")
    features = merge_list(fm.get("features"),
                          require_external(args.feature, SD_FEATURES, "software-development",
                                           "--feature"), args.replace)
    related = merge_list(fm.get("related_mechanics"),
                         require_slugs(args.related, "game-mechanic", "--related"), args.replace)

    impl = ("**Implemented by:** " + ", ".join(f"[[{f}]]" for f in features)) if features \
        else "**Implemented by:** _(software-development feature slugs, when that plugin is installed)_"
    upsert("game-mechanic", args.name,
           fields={"state": state, "category": category, "features": features,
                   "related_mechanics": related},
           sections={"Related": "\n".join(f"- [[{r}]]" for r in related) or None},
           lead=args.summary,
           meta_lines=[("**State:**", f"**State:** {state}"
                        + (f" · **Category:** {category}" if category else "")),
                       ("**Implemented by:**", impl)])
    return refresh_all()


def cmd_new_lore(args):
    require_plugin()
    path = note_path("lore", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    canon = choice(args.canon, CANON_STATES, "--canon") or fm.get("canon") or "proposed"
    era = args.era if args.era is not None else fm.get("era", "")
    characters = merge_list(fm.get("characters"),
                            require_slugs(args.character, "character", "--character"), args.replace)
    factions = merge_list(fm.get("factions"),
                          require_slugs(args.faction, "faction", "--faction"), args.replace)
    locations = merge_list(fm.get("locations"),
                           require_slugs(args.location, "location", "--location"), args.replace)

    ties = "\n".join(f"- [[{s}]]" for s in characters + factions + locations) or None
    upsert("lore", args.title,
           fields={"canon": canon, "era": era, "characters": characters,
                   "factions": factions, "locations": locations},
           sections={"Ties": ties},
           lead=args.summary,
           meta_lines=[("**Canon:**", f"**Canon:** {canon}"
                        + (f" · **Era:** {era}" if era else ""))])
    return refresh_all()


def cmd_new_quest(args):
    require_plugin()
    path = note_path("quest", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    status = choice(args.status, QUEST_STATUSES, "--status") or fm.get("quest_status") or "design"
    qtype = args.type if args.type is not None else fm.get("quest_type", "side")
    giver = require_slugs([args.giver], "character", "--giver")[0] if args.giver \
        else fm.get("giver", "")
    location = require_slugs([args.location], "location", "--location")[0] if args.location \
        else fm.get("location", "")
    mechanics = merge_list(fm.get("mechanics"),
                           require_slugs(args.mechanic, "game-mechanic", "--mechanic"), args.replace)
    rewards = merge_list(fm.get("rewards"),
                         require_slugs(args.reward, "item", "--reward"), args.replace)
    prereqs = merge_list(fm.get("prerequisites"),
                         require_slugs(args.prereq, "quest", "--prereq"), args.replace)

    upsert("quest", args.title,
           fields={"quest_status": status, "quest_type": qtype, "giver": giver,
                   "location": location, "mechanics": mechanics, "rewards": rewards,
                   "prerequisites": prereqs},
           sections={"Rewards": "\n".join(f"- [[{r}]]" for r in rewards) or None,
                     "Prerequisites": "\n".join(f"- [[{p}]]" for p in prereqs) or None},
           lead=args.summary,
           meta_lines=[("**Status:**", f"**Status:** {status} · **Type:** {qtype}"
                        + f" · **Giver:** {optlink(giver)} · **Location:** {optlink(location)}")])
    return refresh_all()


def cmd_new_level(args):
    require_plugin()
    path = note_path("level", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    status = choice(args.status, LEVEL_STATUSES, "--status") or fm.get("level_status") or "design"
    location = require_slugs([args.location], "location", "--location")[0] if args.location \
        else fm.get("location", "")
    mechanics = merge_list(fm.get("mechanics"),
                           require_slugs(args.mechanic, "game-mechanic", "--mechanic"), args.replace)
    quests = merge_list(fm.get("quests"),
                        require_slugs(args.quest, "quest", "--quest"), args.replace)
    enemies = merge_list(fm.get("enemies"),
                         require_slugs(args.enemy, "character", "--enemy"), args.replace)

    upsert("level", args.title,
           fields={"level_status": status, "location": location, "mechanics": mechanics,
                   "quests": quests, "enemies": enemies},
           sections={"Encounters": "\n".join(f"- [[{e}]]" for e in enemies) or None},
           lead=args.summary,
           meta_lines=[("**Status:**", f"**Status:** {status} · **Location:** {optlink(location)}")])
    return refresh_all()


def cmd_new_item(args):
    require_plugin()
    path = note_path("item", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    itype = args.type if args.type is not None else fm.get("item_type", "")
    rarity = args.rarity if args.rarity is not None else fm.get("rarity", "common")
    cost = args.cost if args.cost is not None else fm.get("cost", "")
    source = args.source if args.source is not None else fm.get("source", "")
    mechanics = merge_list(fm.get("mechanics"),
                           require_slugs(args.mechanic, "game-mechanic", "--mechanic"), args.replace)

    upsert("item", args.name,
           fields={"item_type": itype, "rarity": rarity, "cost": cost, "source": source,
                   "mechanics": mechanics},
           sections={"Related": "\n".join(f"- [[{m}]]" for m in mechanics) or None},
           lead=args.summary,
           meta_lines=[("**Type:**", f"**Type:** {itype or '—'} · **Rarity:** {rarity}"
                        + (f" · **Cost:** {cost}" if cost else ""))])
    return refresh_all()


def cmd_new_character(args):
    require_plugin()
    path = note_path("character", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    role = args.role if args.role is not None else fm.get("role", "npc")
    faction = require_slugs([args.faction], "faction", "--faction")[0] if args.faction \
        else fm.get("faction", "")
    home = require_slugs([args.home], "location", "--home")[0] if args.home \
        else fm.get("home", "")

    upsert("character", args.name,
           fields={"role": role, "faction": faction, "home": home},
           sections={},
           lead=args.summary,
           meta_lines=[("**Role:**", f"**Role:** {role} · **Faction:** {optlink(faction)}"
                        + f" · **Home:** {optlink(home)}")])
    return refresh_all()


def cmd_new_faction(args):
    require_plugin()
    path = note_path("faction", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    homeland = require_slugs([args.homeland], "location", "--homeland")[0] if args.homeland \
        else fm.get("homeland", "")
    allies = merge_list(fm.get("allies"),
                        require_slugs(args.ally, "faction", "--ally"), args.replace)
    enemies = merge_list(fm.get("enemies"),
                         require_slugs(args.enemy, "faction", "--enemy"), args.replace)

    standing = None
    if allies or enemies:
        standing = ""
        if allies:
            standing += "- Allies: " + ", ".join(f"[[{a}]]" for a in allies) + "\n"
        if enemies:
            standing += "- Enemies: " + ", ".join(f"[[{e}]]" for e in enemies)
    upsert("faction", args.name,
           fields={"homeland": homeland, "allies": allies, "enemies": enemies},
           sections={"Standing": standing},
           lead=args.summary,
           meta_lines=[("**Homeland:**", f"**Homeland:** {optlink(homeland)}")])
    return refresh_all()


def cmd_new_location(args):
    require_plugin()
    path = note_path("location", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    parent = require_slugs([args.parent], "location", "--parent")[0] if args.parent \
        else fm.get("parent", "")
    controlling = require_slugs([args.faction], "faction", "--faction")[0] if args.faction \
        else fm.get("controlling_faction", "")

    upsert("location", args.name,
           fields={"parent": parent, "controlling_faction": controlling},
           sections={},
           lead=args.summary,
           meta_lines=[("**Part of:**", f"**Part of:** {optlink(parent)}"
                        + f" · **Controlled by:** {optlink(controlling)}")])
    return refresh_all()


# --------------------------------------------------------------------------- #
# Commands: set-status / list-notes / refresh / status
# --------------------------------------------------------------------------- #
STATUS_LABEL = {"game-mechanic": "**State:**", "lore": "**Canon:**",
                "quest": "**Status:**", "level": "**Status:**"}


def cmd_set_status(args):
    require_plugin()
    tag, path = find_note(args.note)
    field = TYPES[tag].get("status_field")
    if not field:
        die(f"'{slug(args.note)}' is a {tag} note, which has no lifecycle status. "
            "Only game-mechanic, quest, level and lore notes do.")
    value = choice(args.status, VOCAB[tag], "--status")
    fm, body = split_note(path)
    fm[field] = value
    fm["updated"] = today()
    label = STATUS_LABEL[tag]
    line = f"{label} {value}"
    if tag == "quest":
        line += f" · **Type:** {fm.get('quest_type', 'side')}" \
                f" · **Giver:** {optlink(fm.get('giver', ''))}" \
                f" · **Location:** {optlink(fm.get('location', ''))}"
    elif tag == "level":
        line += f" · **Location:** {optlink(fm.get('location', ''))}"
    elif tag == "game-mechanic" and fm.get("category"):
        line += f" · **Category:** {fm['category']}"
    elif tag == "lore" and fm.get("era"):
        line += f" · **Era:** {fm['era']}"
    body = set_meta_line(body, label, line)
    write_full(path, fm, body)
    print(f"  {rel(path)}: {field} -> {value}")
    return refresh_all()


def cmd_list_notes(args):
    require_plugin()
    if not CATALOG.exists():
        die(f"{rel(CATALOG)} not found. Build it first: python3 scripts/wiki_tool.py build")
    q = (args.query or "").lower()
    shown = 0
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except ValueError:
            continue
        tag, title, path = entry.get("tag", ""), entry.get("title", ""), entry.get("path", "")
        if args.tag and tag != args.tag:
            continue
        if q and q not in title.lower() and q not in path.lower():
            continue
        print(f"{Path(path).stem}\t[{tag}]\t{title}")
        shown += 1
    if shown == 0:
        print("(no matching notes)", file=sys.stderr)
    return 0


def title_of(tag, s):
    path = note_path(tag, s)
    if not path.exists():
        return s
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return s


def refresh_all(quiet=False, gate=True):
    """Regenerate every managed rollup block from the notes' frontmatter."""
    mechanics = {s: fm for s, fm, _b in load_notes("game-mechanic")}
    quests = {s: fm for s, fm, _b in load_notes("quest")}
    levels = {s: fm for s, fm, _b in load_notes("level")}
    items = {s: fm for s, fm, _b in load_notes("item")}
    characters = list(all_slugs("character"))
    factions = list(all_slugs("faction"))
    locations = list(all_slugs("location"))

    # --- game-mechanic: everything that references it ---
    for mech, fm, body in load_notes("game-mechanic"):
        used = []
        used += [f"- [[{s}|{title_of('quest', s)}]] · quest"
                 for s in sorted(quests) if mech in (quests[s].get("mechanics") or [])]
        used += [f"- [[{s}|{title_of('level', s)}]] · level"
                 for s in sorted(levels) if mech in (levels[s].get("mechanics") or [])]
        used += [f"- [[{s}|{title_of('item', s)}]] · item"
                 for s in sorted(items) if mech in (items[s].get("mechanics") or [])]
        body = replace_block(body, USED_IN_START, USED_IN_END, "\n".join(used))
        write_full(note_path("game-mechanic", mech), fm, body)

    # --- character: the quests they give ---
    for char, fm, body in load_notes("character"):
        gq = sorted(s for s in quests if quests[s].get("giver") == char)
        body = replace_block(body, QUESTS_START, QUESTS_END, "\n".join(
            f"- [[{s}|{title_of('quest', s)}]] · {quests[s].get('quest_status', 'design')}"
            for s in gq))
        write_full(note_path("character", char), fm, body)

    # --- faction: their members ---
    char_fm = {s: fm for s, fm, _b in load_notes("character")}
    for fac, fm, body in load_notes("faction"):
        members = sorted(s for s in char_fm if char_fm[s].get("faction") == fac)
        body = replace_block(body, MEMBERS_START, MEMBERS_END, "\n".join(
            f"- [[{s}|{title_of('character', s)}]] · {char_fm[s].get('role', 'npc')}"
            for s in members))
        write_full(note_path("faction", fac), fm, body)

    # --- location: the quests and levels set here ---
    for loc, fm, body in load_notes("location"):
        here = [f"- [[{s}|{title_of('quest', s)}]] · quest"
                for s in sorted(quests) if quests[s].get("location") == loc]
        here += [f"- [[{s}|{title_of('level', s)}]] · level"
                 for s in sorted(levels) if levels[s].get("location") == loc]
        body = replace_block(body, SET_HERE_START, SET_HERE_END, "\n".join(here))
        write_full(note_path("location", loc), fm, body)

    if not quiet:
        print(f"  refreshed {len(mechanics)} mechanic(s), {len(quests)} quest(s), "
              f"{len(levels)} level(s), {len(items)} item(s), {len(characters)} character(s), "
              f"{len(factions)} faction(s), {len(locations)} location(s)")
    return run_gate() if gate else 0


def cmd_refresh(args):
    require_plugin()
    return refresh_all()


def cmd_status(args):
    require_plugin()
    mechanics = {s: fm for s, fm, _b in load_notes("game-mechanic")}
    quests = {s: fm for s, fm, _b in load_notes("quest")}
    levels = {s: fm for s, fm, _b in load_notes("level")}
    lore = {s: fm for s, fm, _b in load_notes("lore")}

    def rollup(name, notes, field, vocab):
        print(name)
        for value in vocab:
            members = sorted(s for s, f in notes.items() if f.get(field) == value)
            if members:
                print(f"  {value:<11} {len(members):>3}  {', '.join(members)}")
        if not notes:
            print("  (none)")
        print()

    rollup("Mechanics", mechanics, "state", MECHANIC_STATES)
    rollup("Quests", quests, "quest_status", QUEST_STATUSES)
    rollup("Levels", levels, "level_status", LEVEL_STATUSES)
    rollup("Lore", lore, "canon", CANON_STATES)

    print(f"World: {len(all_slugs('character'))} character(s), {len(all_slugs('faction'))} "
          f"faction(s), {len(all_slugs('location'))} location(s), {len(all_slugs('item'))} item(s)")

    orphan_q = [s for s, f in quests.items() if not f.get("location")]
    if orphan_q:
        print(f"Quests with no location: {', '.join(sorted(orphan_q))}")
    proposed = [s for s, f in lore.items() if f.get("canon") == "proposed"]
    if proposed:
        print(f"Lore still proposed (not yet canon): {', '.join(sorted(proposed))}")
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser():
    parser = argparse.ArgumentParser(
        description="Author game-development notes in an LLM Wiki.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def with_replace(p):
        p.add_argument("--replace", action="store_true",
                       help="replace list fields instead of merging with what's there")
        return p

    nm = with_replace(sub.add_parser("new-mechanic", help="create/update a mechanic note"))
    nm.add_argument("--name", required=True)
    nm.add_argument("--state", choices=MECHANIC_STATES)
    nm.add_argument("--category")
    nm.add_argument("--feature", action="append", default=[],
                    help="software-development feature slug that implements it (repeatable)")
    nm.add_argument("--related", action="append", default=[],
                    help="slug of a related mechanic (repeatable)")
    nm.add_argument("--summary", help="one-paragraph description of the rule")
    nm.set_defaults(func=cmd_new_mechanic)

    nl = with_replace(sub.add_parser("new-lore", help="create/update a lore note"))
    nl.add_argument("--title", required=True)
    nl.add_argument("--canon", choices=CANON_STATES)
    nl.add_argument("--era")
    nl.add_argument("--character", action="append", default=[])
    nl.add_argument("--faction", action="append", default=[])
    nl.add_argument("--location", action="append", default=[])
    nl.add_argument("--summary")
    nl.set_defaults(func=cmd_new_lore)

    nq = with_replace(sub.add_parser("new-quest", help="create/update a quest note"))
    nq.add_argument("--title", required=True)
    nq.add_argument("--status", choices=QUEST_STATUSES)
    nq.add_argument("--type", help="quest type (main / side / faction / tutorial / …)")
    nq.add_argument("--giver", help="slug of the character who gives it")
    nq.add_argument("--location", help="slug of the location it plays out in")
    nq.add_argument("--mechanic", action="append", default=[])
    nq.add_argument("--reward", action="append", default=[], help="slug of an item it grants")
    nq.add_argument("--prereq", action="append", default=[], help="slug of a prerequisite quest")
    nq.add_argument("--summary")
    nq.set_defaults(func=cmd_new_quest)

    nv = with_replace(sub.add_parser("new-level", help="create/update a level note"))
    nv.add_argument("--title", required=True)
    nv.add_argument("--status", choices=LEVEL_STATUSES)
    nv.add_argument("--location")
    nv.add_argument("--mechanic", action="append", default=[])
    nv.add_argument("--quest", action="append", default=[])
    nv.add_argument("--enemy", action="append", default=[], help="slug of a character fought here")
    nv.add_argument("--summary")
    nv.set_defaults(func=cmd_new_level)

    ni = with_replace(sub.add_parser("new-item", help="create/update an item note"))
    ni.add_argument("--name", required=True)
    ni.add_argument("--type", help="item type (weapon / consumable / key / material / …)")
    ni.add_argument("--rarity")
    ni.add_argument("--cost")
    ni.add_argument("--mechanic", action="append", default=[])
    ni.add_argument("--source", help="where the player gets it")
    ni.add_argument("--summary")
    ni.set_defaults(func=cmd_new_item)

    nch = with_replace(sub.add_parser("new-character", help="create/update a character note"))
    nch.add_argument("--name", required=True)
    nch.add_argument("--role", help="protagonist / npc / enemy / boss / merchant / …")
    nch.add_argument("--faction", help="slug of their faction")
    nch.add_argument("--home", help="slug of their home location")
    nch.add_argument("--summary")
    nch.set_defaults(func=cmd_new_character)

    nfa = with_replace(sub.add_parser("new-faction", help="create/update a faction note"))
    nfa.add_argument("--name", required=True)
    nfa.add_argument("--homeland", help="slug of their home location")
    nfa.add_argument("--ally", action="append", default=[], help="slug of an allied faction")
    nfa.add_argument("--enemy", action="append", default=[], help="slug of an enemy faction")
    nfa.add_argument("--summary")
    nfa.set_defaults(func=cmd_new_faction)

    nlo = with_replace(sub.add_parser("new-location", help="create/update a location note"))
    nlo.add_argument("--name", required=True)
    nlo.add_argument("--parent", help="slug of the containing location")
    nlo.add_argument("--faction", help="slug of the controlling faction")
    nlo.add_argument("--summary")
    nlo.set_defaults(func=cmd_new_location)

    ss = sub.add_parser("set-status", help="move a note along its lifecycle")
    ss.add_argument("--note", required=True,
                    help="slug of a game-mechanic, quest, level or lore note")
    ss.add_argument("--status", required=True)
    ss.set_defaults(func=cmd_set_status)

    ln = sub.add_parser("list-notes", help="list notes from the catalog (slugs to link with)")
    ln.add_argument("--query")
    ln.add_argument("--tag")
    ln.set_defaults(func=cmd_list_notes)

    rf = sub.add_parser("refresh", help="rebuild every managed rollup block")
    rf.set_defaults(func=cmd_refresh)

    st = sub.add_parser("status", help="design rollup")
    st.set_defaults(func=cmd_status)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

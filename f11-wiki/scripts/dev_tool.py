#!/usr/bin/env python3
"""Author software-development notes in an LLM Wiki, grounded in a real codebase.

Standard library only. Scaffolds and maintains six source-exempt note types — `component`,
`feature`, `decision`, `change`, `pattern`, `convention` — wiring the links
(change -> feature -> component), keeping counts and managed blocks current, then running the
core `wiki_tool.py` gate. The skills supply the content; this tool keeps the notes consistent.

Commands:
  new-component --name N [--kind K] [--repo R] [--path P]... [--depends-on SLUG]...
                [--summary S] [--replace]
                      Create/update a component note. --kind is one of service, library,
                      module, ui, datastore, job, tool.
  new-feature --title T [--state S] [--component SLUG]... [--decision SLUG]... [--summary S]
              [--replace]
                      Create/update a feature note. --state is proposed, building, shipped or
                      deprecated.
  new-change --title T --feature SLUG [--component SLUG]... [--decision SLUG]... [--path P]...
             [--status S] [--summary S] [--replace]
                      Create/update a change note. --status is discussing, planned,
                      in-progress, done or abandoned.
  new-decision --title T [--status S] [--feature SLUG] [--component SLUG]... [--supersedes SLUG]
               [--context C] [--options O] [--decision D] [--consequences Q] [--summary S]
               [--replace]
                      Create/update a decision (ADR). --status is proposed, accepted, rejected
                      or superseded. --supersedes flips the older decision to `superseded` and
                      cross-links both; never rewrite an accepted decision in place.
  new-pattern --title T [--component SLUG]... [--path P]... [--convention SLUG]...
              [--problem P] [--solution S] [--summary S] [--replace]
                      Create/update a pattern note.
  new-convention --title T [--scope S] [--enforcement E] [--rule R] [--rationale R]
                 [--summary S]
                      Create/update a convention note. --enforcement is lint, test, review or
                      manual.
  set-status --note SLUG --status VALUE
                      Move a note along its lifecycle, validating against that type's
                      vocabulary (feature.state / change.change_status /
                      decision.decision_status).
  list-notes [--query Q] [--tag TAG]
                      List notes from Wiki/catalog.jsonl — their slugs are what you pass to
                      --component / --feature / --decision.
  refresh             Rebuild every managed block and count from the notes' frontmatter.
  status [--feature SLUG]
                      Project rollup: features by state, open changes, undecided decisions.

All `new-*` commands are idempotent on title: re-run with the same title to update the note in
place, preserving the prose you've written in unmanaged sections. List arguments merge with
what's already there; pass --replace to overwrite them instead.

Notes are grounded two ways, not by Raw sources (all six types are source-exempt): repo-relative
code paths (`paths:` frontmatter and the `**Code:**` line) and `**Based on:** [[...]]` wikilinks
to other notes. Do not invent components, paths or behaviour that aren't in the repository.
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
          "llm-wiki-setup (re-copy template/. into the vault), then re-run.", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
WIKI_TOOL = ROOT / "scripts" / "wiki_tool.py"
CATALOG = ROOT / "Wiki" / "catalog.jsonl"

# --------------------------------------------------------------------------- #
# The six note types this plugin registers (mirrors plugin/manifest.json)
# --------------------------------------------------------------------------- #
TYPES = {
    "component":  {"folder": "Wiki/Components"},
    "feature":    {"folder": "Wiki/Features",  "status_field": "state"},
    "decision":   {"folder": "Wiki/Decisions", "status_field": "decision_status"},
    "change":     {"folder": "Wiki/Changes",   "status_field": "change_status"},
    "pattern":    {"folder": "Wiki/Patterns"},
    "convention": {"folder": "Wiki/Conventions"},
}

COMPONENT_KINDS = ["service", "library", "module", "ui", "datastore", "job", "tool"]
FEATURE_STATES = ["proposed", "building", "shipped", "deprecated"]
CHANGE_STATUSES = ["discussing", "planned", "in-progress", "done", "abandoned"]
DECISION_STATUSES = ["proposed", "accepted", "rejected", "superseded"]
ENFORCEMENTS = ["lint", "test", "review", "manual"]

VOCAB = {"feature": FEATURE_STATES, "change": CHANGE_STATUSES, "decision": DECISION_STATUSES}

# Managed regions the tool owns inside note bodies.
FEATURES_START, FEATURES_END = "<!-- sd:features:start -->", "<!-- sd:features:end -->"
CHANGES_START, CHANGES_END = "<!-- sd:changes:start -->", "<!-- sd:changes:end -->"
DECISIONS_START, DECISIONS_END = "<!-- sd:decisions:start -->", "<!-- sd:decisions:end -->"


def require_plugin():
    if not WIKI_TOOL.exists():
        die("this folder is not an LLM Wiki (no scripts/wiki_tool.py). "
            "Set up an llm-wiki first, then run the devwiki-init skill.")
    if not (ROOT / TYPES["component"]["folder"]).is_dir():
        die("the software-development plugin is not installed (no Wiki/Components/). "
            "Run the devwiki-init skill in this vault first.")


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
    die(f"no software-development note '{s}' in this vault. "
        "List what exists with: python3 scripts/dev_tool.py list-notes")


def require_slugs(values, tag, flag):
    """Validate that each referenced slug exists, so notes can't cite invented components."""
    out = []
    for value in values or []:
        s = slug(value)
        if not note_path(tag, s).exists():
            existing = ", ".join(all_slugs(tag)) or "(none yet)"
            die(f"{flag} '{s}': no {tag} note by that name. Existing {tag}s: {existing}\n"
                f"Create it first, or fix the slug — don't reference something that isn't there.")
        out.append(s)
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


def link_list(slugs, label=None):
    return ", ".join(f"[[{s}]]" for s in slugs) if slugs else (label or "")


def code_line(paths):
    return "**Code:** " + (", ".join(f"`{p}`" for p in paths) if paths else "_(none recorded)_")


def based_on_line(slugs):
    return "**Based on:** " + (link_list(slugs) if slugs else "_(nothing yet)_")


# --------------------------------------------------------------------------- #
# Note creation / update
# --------------------------------------------------------------------------- #
def upsert(tag, title, fields, sections, meta_lines, lead=None, blocks=()):
    """Create or update a note of `tag` titled `title`.

    fields      — frontmatter to set (lists already merged by the caller)
    sections    — {header: content} prose sections to (re)write, skipping falsy values
    meta_lines  — [(prefix, line)] single-line body facts kept in sync (e.g. `**Status:** ...`)
    lead        — replaces the note's opening paragraph
    blocks      — managed regions to ensure exist, as (header, start, end)

    A new note starts from the vault's note template; sections the caller doesn't supply keep
    the template's guidance prose, which is the skill's cue to fill them in.
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
    # Keep the core keys first, then this type's own fields, for a readable, stable order.
    ordered = {k: merged[k] for k in core if k in merged}
    ordered.update({k: v for k, v in merged.items() if k not in ordered})

    body = set_lead(body, lead)
    for prefix, line in meta_lines:
        body = set_meta_line(body, prefix, line)
    for header, content in sections.items():
        body = set_section(body, header, content)
    for header, start, end in blocks:
        if start not in body:
            body = body.rstrip() + f"\n\n## {header}\n\n{start}\n{end}\n"

    write_full(path, ordered, body)
    print(f"  {'updated' if exists else 'created'} {rel(path)}")
    return note_slug


# --------------------------------------------------------------------------- #
# Commands: new-*
# --------------------------------------------------------------------------- #
def cmd_new_component(args):
    require_plugin()
    path = note_path("component", slug(args.name))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    kind = choice(args.kind, COMPONENT_KINDS, "--kind") or fm.get("kind") or "module"
    paths = merge_list(fm.get("paths"), args.path, args.replace)
    depends = merge_list(fm.get("depends_on"),
                         require_slugs(args.depends_on, "component", "--depends-on"),
                         args.replace)
    repo = args.repo if args.repo is not None else fm.get("repo", "")

    upsert("component", args.name,
           fields={"repo": repo, "kind": kind, "paths": paths, "depends_on": depends,
                   "feature_count": int(fm.get("feature_count") or 0),
                   "change_count": int(fm.get("change_count") or 0)},
           sections={"Depends On": "\n".join(f"- [[{d}]]" for d in depends) or None},
           lead=args.summary,
           meta_lines=[("**Kind:**", f"**Kind:** {kind}" + (f" · **Repo:** {repo}" if repo else "")),
                       ("**Code:**", code_line(paths))],
           blocks=[("Features", FEATURES_START, FEATURES_END),
                   ("Changes", CHANGES_START, CHANGES_END)])
    return refresh_all()


def cmd_new_feature(args):
    require_plugin()
    path = note_path("feature", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    state = choice(args.state, FEATURE_STATES, "--state") or fm.get("state") or "proposed"
    components = merge_list(fm.get("components"),
                            require_slugs(args.component, "component", "--component"),
                            args.replace)
    decisions = merge_list(fm.get("decisions"),
                           require_slugs(args.decision, "decision", "--decision"), args.replace)

    upsert("feature", args.title,
           fields={"state": state, "components": components, "decisions": decisions,
                   "change_count": int(fm.get("change_count") or 0)},
           sections={"Components": "\n".join(f"- [[{c}]]" for c in components) or None},
           lead=args.summary,
           meta_lines=[("**State:**", f"**State:** {state}")],
           blocks=[("Decisions", DECISIONS_START, DECISIONS_END),
                   ("Changes", CHANGES_START, CHANGES_END)])
    return refresh_all()


def cmd_new_change(args):
    require_plugin()
    path = note_path("change", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    feature = require_slugs([args.feature], "feature", "--feature")[0]
    status = choice(args.status, CHANGE_STATUSES, "--status") or fm.get("change_status") \
        or "discussing"
    components = merge_list(fm.get("components"),
                            require_slugs(args.component, "component", "--component"),
                            args.replace)
    decisions = merge_list(fm.get("decisions"),
                           require_slugs(args.decision, "decision", "--decision"), args.replace)
    paths = merge_list(fm.get("paths"), args.path, args.replace)

    upsert("change", args.title,
           fields={"change_status": status, "feature": feature, "components": components,
                   "decisions": decisions, "paths": paths},
           sections={"Impact": "\n".join(f"- [[{c}]]" for c in components) or None},
           lead=args.summary,
           meta_lines=[("**Status:**", f"**Status:** {status} · **Feature:** [[{feature}]]"),
                       ("**Code:**", code_line(paths)),
                       ("**Based on:**", based_on_line(components + decisions))])
    return refresh_all()


def cmd_new_decision(args):
    require_plugin()
    path = note_path("decision", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    status = choice(args.status, DECISION_STATUSES, "--status") or fm.get("decision_status") \
        or "proposed"
    components = merge_list(fm.get("components"),
                            require_slugs(args.component, "component", "--component"),
                            args.replace)
    feature = require_slugs([args.feature], "feature", "--feature")[0] if args.feature \
        else fm.get("feature", "")
    supersedes = require_slugs([args.supersedes], "decision", "--supersedes")[0] \
        if args.supersedes else fm.get("supersedes", "")
    decided = fm.get("decided", "")
    if status == "accepted" and not decided:
        decided = today()

    note_slug = upsert(
        "decision", args.title,
        fields={"decision_status": status, "decided": decided, "components": components,
                "feature": feature, "supersedes": supersedes,
                "superseded_by": fm.get("superseded_by", "")},
        sections={"Context": args.context, "Options Considered": args.options,
                  "Decision": args.decision, "Consequences": args.consequences},
        lead=args.summary,
        meta_lines=[("**Status:**", f"**Status:** {status}"
                     + (f" · **Decided:** {decided}" if decided else "")),
                    ("**Based on:**", based_on_line(components))])

    if supersedes and supersedes != note_slug:
        mark_superseded(supersedes, note_slug)
    return refresh_all()


def mark_superseded(old_slug, new_slug):
    """Flip a superseded decision and cross-link it, so history stays intact."""
    path = note_path("decision", old_slug)
    fm, body = split_note(path)
    fm["decision_status"] = "superseded"
    fm["superseded_by"] = new_slug
    fm["updated"] = today()
    body = set_meta_line(body, "**Status:**",
                         f"**Status:** superseded by [[{new_slug}]]"
                         + (f" · **Decided:** {fm['decided']}" if fm.get("decided") else ""))
    write_full(path, fm, body)
    print(f"  superseded {rel(path)} (now points at {new_slug})")


def cmd_new_pattern(args):
    require_plugin()
    path = note_path("pattern", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    components = merge_list(fm.get("components"),
                            require_slugs(args.component, "component", "--component"),
                            args.replace)
    conventions = merge_list(fm.get("related_conventions"),
                             require_slugs(args.convention, "convention", "--convention"),
                             args.replace)
    paths = merge_list(fm.get("paths"), args.path, args.replace)

    upsert("pattern", args.title,
           fields={"components": components, "paths": paths,
                   "related_conventions": conventions},
           sections={"Problem": args.problem, "Solution": args.solution,
                     "Related": "\n".join(f"- [[{c}]]" for c in conventions) or None},
           lead=args.summary,
           meta_lines=[("**Code:**", code_line(paths)),
                       ("**Based on:**", based_on_line(components))])
    return refresh_all()


def cmd_new_convention(args):
    require_plugin()
    path = note_path("convention", slug(args.title))
    fm, _ = split_note(path) if path.exists() else ({}, "")
    enforcement = choice(args.enforcement, ENFORCEMENTS, "--enforcement") \
        or fm.get("enforcement") or "review"
    scope = args.scope or fm.get("scope") or "repo-wide"
    if scope != "repo-wide" and not note_path("component", slug(scope)).exists():
        die(f"--scope '{scope}' is neither 'repo-wide' nor an existing component slug. "
            f"Components: {', '.join(all_slugs('component')) or '(none yet)'}")

    upsert("convention", args.title,
           fields={"scope": scope, "enforcement": enforcement},
           sections={"Rule": args.rule, "Rationale": args.rationale},
           lead=args.summary,
           meta_lines=[("**Scope:**", f"**Scope:** {scope} · **Enforced by:** {enforcement}")])
    return refresh_all()


# --------------------------------------------------------------------------- #
# Commands: set-status / list-notes / refresh / status
# --------------------------------------------------------------------------- #
def cmd_set_status(args):
    require_plugin()
    tag, path = find_note(args.note)
    field = TYPES[tag].get("status_field")
    if not field:
        die(f"'{slug(args.note)}' is a {tag} note, which has no lifecycle status. "
            "Only feature, change and decision notes do.")
    value = choice(args.status, VOCAB[tag], "--status")
    fm, body = split_note(path)
    fm[field] = value
    fm["updated"] = today()
    if tag == "decision" and value == "accepted" and not fm.get("decided"):
        fm["decided"] = today()
    label = {"feature": "**State:**"}.get(tag, "**Status:**")
    line = f"{label} {value}"
    if tag == "change" and fm.get("feature"):
        line += f" · **Feature:** [[{fm['feature']}]]"
    if tag == "decision" and fm.get("decided"):
        line += f" · **Decided:** {fm['decided']}"
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


def refresh_all(quiet=False, gate=True):
    """Regenerate every managed block and count from the notes' frontmatter."""
    features = {s: fm for s, fm, _b in load_notes("feature")}
    changes = {s: fm for s, fm, _b in load_notes("change")}
    decisions = {s: fm for s, fm, _b in load_notes("decision")}

    def title_of(tag, s):
        path = note_path(tag, s)
        if not path.exists():
            return s
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return s

    # --- components: the features and changes that touch them ---
    for comp, fm, body in load_notes("component"):
        feats = sorted(s for s, f in features.items() if comp in (f.get("components") or []))
        chgs = sorted(s for s, c in changes.items() if comp in (c.get("components") or []))
        body = replace_block(body, FEATURES_START, FEATURES_END, "\n".join(
            f"- [[{s}|{title_of('feature', s)}]] · {features[s].get('state', 'proposed')}"
            for s in feats))
        body = replace_block(body, CHANGES_START, CHANGES_END, "\n".join(
            f"- [[{s}|{title_of('change', s)}]] · "
            f"{changes[s].get('change_status', 'discussing')}" for s in chgs))
        fm["feature_count"] = len(feats)
        fm["change_count"] = len(chgs)
        fm["updated"] = fm.get("updated") or today()
        write_full(note_path("component", comp), fm, body)

    # --- features: their changes and the decisions that shaped them ---
    for feat, fm, body in load_notes("feature"):
        chgs = sorted(s for s, c in changes.items() if c.get("feature") == feat)
        decs = sorted(set(
            [s for s, d in decisions.items() if d.get("feature") == feat]
            + [s for s in (fm.get("decisions") or []) if s in decisions]))
        body = replace_block(body, CHANGES_START, CHANGES_END, "\n".join(
            f"- [[{s}|{title_of('change', s)}]] · "
            f"{changes[s].get('change_status', 'discussing')}" for s in chgs))
        body = replace_block(body, DECISIONS_START, DECISIONS_END, "\n".join(
            f"- [[{s}|{title_of('decision', s)}]] · "
            f"{decisions[s].get('decision_status', 'proposed')}" for s in decs))
        fm["change_count"] = len(chgs)
        fm["decisions"] = decs
        write_full(note_path("feature", feat), fm, body)

    if not quiet:
        print(f"  refreshed {len(list(load_notes('component')))} component(s), "
              f"{len(features)} feature(s), {len(changes)} change(s), "
              f"{len(decisions)} decision(s)")
    return run_gate() if gate else 0


def cmd_refresh(args):
    require_plugin()
    return refresh_all()


def cmd_status(args):
    require_plugin()
    features = {s: fm for s, fm, _b in load_notes("feature")}
    changes = {s: fm for s, fm, _b in load_notes("change")}
    decisions = {s: fm for s, fm, _b in load_notes("decision")}

    if args.feature:
        feat = require_slugs([args.feature], "feature", "--feature")[0]
        features = {feat: features[feat]}
        changes = {s: c for s, c in changes.items() if c.get("feature") == feat}
        decisions = {s: d for s, d in decisions.items()
                     if d.get("feature") == feat or s in (features[feat].get("decisions") or [])}

    print(f"Components: {len(all_slugs('component'))} · Patterns: {len(all_slugs('pattern'))} "
          f"· Conventions: {len(all_slugs('convention'))}\n")

    print("Features")
    for state in FEATURE_STATES:
        members = sorted(s for s, f in features.items() if f.get("state") == state)
        if members:
            print(f"  {state:<11} {len(members):>3}  {', '.join(members)}")
    if not features:
        print("  (none)")

    print("\nChanges")
    for st in CHANGE_STATUSES:
        members = sorted(s for s, c in changes.items() if c.get("change_status") == st)
        if members:
            print(f"  {st:<11} {len(members):>3}  {', '.join(members)}")
    if not changes:
        print("  (none)")

    print("\nDecisions")
    for st in DECISION_STATUSES:
        members = sorted(s for s, d in decisions.items() if d.get("decision_status") == st)
        if members:
            print(f"  {st:<11} {len(members):>3}  {', '.join(members)}")
    if not decisions:
        print("  (none)")

    open_decisions = [s for s, d in decisions.items() if d.get("decision_status") == "proposed"]
    if open_decisions:
        print(f"\nStill undecided: {', '.join(sorted(open_decisions))}")
    orphans = [s for s, c in changes.items() if not c.get("feature")]
    if orphans:
        print(f"Changes with no feature: {', '.join(sorted(orphans))}")
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser():
    parser = argparse.ArgumentParser(
        description="Author software-development notes in an LLM Wiki.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def with_replace(p):
        p.add_argument("--replace", action="store_true",
                       help="replace list fields instead of merging with what's there")
        return p

    nc = with_replace(sub.add_parser("new-component", help="create/update a component note"))
    nc.add_argument("--name", required=True)
    nc.add_argument("--kind", choices=COMPONENT_KINDS)
    nc.add_argument("--repo")
    nc.add_argument("--path", action="append", default=[],
                    help="repo-relative path (repeatable); must exist in the repository")
    nc.add_argument("--depends-on", action="append", default=[],
                    help="slug of a component this depends on (repeatable)")
    nc.add_argument("--summary", help="one-paragraph responsibility")
    nc.set_defaults(func=cmd_new_component)

    nf = with_replace(sub.add_parser("new-feature", help="create/update a feature note"))
    nf.add_argument("--title", required=True)
    nf.add_argument("--state", choices=FEATURE_STATES)
    nf.add_argument("--component", action="append", default=[])
    nf.add_argument("--decision", action="append", default=[])
    nf.add_argument("--summary", help="one-paragraph intent")
    nf.set_defaults(func=cmd_new_feature)

    ng = with_replace(sub.add_parser("new-change", help="create/update a change note"))
    ng.add_argument("--title", required=True)
    ng.add_argument("--feature", required=True, help="slug of the parent feature note")
    ng.add_argument("--component", action="append", default=[])
    ng.add_argument("--decision", action="append", default=[])
    ng.add_argument("--path", action="append", default=[])
    ng.add_argument("--status", choices=CHANGE_STATUSES)
    ng.add_argument("--summary", help="one-paragraph motivation")
    ng.set_defaults(func=cmd_new_change)

    nd = with_replace(sub.add_parser("new-decision", help="create/update a decision (ADR)"))
    nd.add_argument("--title", required=True, help="state it as a choice made")
    nd.add_argument("--status", choices=DECISION_STATUSES)
    nd.add_argument("--feature")
    nd.add_argument("--component", action="append", default=[])
    nd.add_argument("--supersedes", help="slug of the decision this replaces")
    nd.add_argument("--context")
    nd.add_argument("--options")
    nd.add_argument("--decision", dest="decision")
    nd.add_argument("--consequences")
    nd.add_argument("--summary", help="the decision in one sentence (the note's lead)")
    nd.set_defaults(func=cmd_new_decision)

    np_ = with_replace(sub.add_parser("new-pattern", help="create/update a pattern note"))
    np_.add_argument("--title", required=True)
    np_.add_argument("--component", action="append", default=[])
    np_.add_argument("--path", action="append", default=[])
    np_.add_argument("--convention", action="append", default=[])
    np_.add_argument("--problem")
    np_.add_argument("--solution")
    np_.add_argument("--summary")
    np_.set_defaults(func=cmd_new_pattern)

    nv = with_replace(sub.add_parser("new-convention", help="create/update a convention note"))
    nv.add_argument("--title", required=True)
    nv.add_argument("--scope", help="'repo-wide' or a component slug")
    nv.add_argument("--enforcement", choices=ENFORCEMENTS)
    nv.add_argument("--rule")
    nv.add_argument("--rationale")
    nv.add_argument("--summary")
    nv.set_defaults(func=cmd_new_convention)

    ss = sub.add_parser("set-status", help="move a note along its lifecycle")
    ss.add_argument("--note", required=True, help="slug of a feature, change or decision note")
    ss.add_argument("--status", required=True)
    ss.set_defaults(func=cmd_set_status)

    ln = sub.add_parser("list-notes", help="list notes from the catalog (slugs to link with)")
    ln.add_argument("--query")
    ln.add_argument("--tag")
    ln.set_defaults(func=cmd_list_notes)

    rf = sub.add_parser("refresh", help="rebuild every managed block and count")
    rf.set_defaults(func=cmd_refresh)

    st = sub.add_parser("status", help="project rollup")
    st.add_argument("--feature", help="limit the rollup to one feature")
    st.set_defaults(func=cmd_status)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

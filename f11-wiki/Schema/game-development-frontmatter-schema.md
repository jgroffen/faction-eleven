# Game Development Frontmatter Schema

The `game-development` plugin adds eight note types on top of the core LLM Wiki types
(`topic`, `concept`, `entity`, `log`), and is designed to sit **alongside** the
`software-development` plugin: game-development describes what the game *is* (design, content,
world); software-development describes how it's *built* (engineering). A `game-mechanic` links to the
`feature` notes that implement it, so the two compose without overlapping.

All core lint rules still apply: exactly one tag, ISO `created`/`updated`, `source_count ==
len(sources)`. All eight types are **source-exempt** (`requires_source: false`): their content is
design intent and in-world canon, not `Raw/Sources/` clippings, so they pass lint with
`sources: []` and `source_count: 0`.

## Grounding

Instead of `sources:`, notes carry their provenance as **`[[wikilinks]]`** to the other notes
they draw on (which also surface as Obsidian backlinks). Mechanics additionally link to the
`software-development` `feature`(s) that implement them. `scripts/game_tool.py` refuses to link a
`character`, `faction`, `location`, `quest`, `game-mechanic` or `item` that doesn't exist, so notes
can't cite parts of the world that were never authored. Cross-plugin links to
software-development `feature`s are validated only when that plugin is installed; otherwise they're
accepted with a warning.

## Link topology (a graph, not a tree)

```
quest ────▶ giver(character), location, mechanics, rewards(item), prerequisites(quest)
level ────▶ location, mechanics, quests, enemies(character)
character ▶ faction, home(location)
faction ──▶ homeland(location), allies/enemies(faction)
location ─▶ parent(location), controlling_faction
item ─────▶ mechanics
lore ─────▶ characters, factions, locations
mechanic ─▶ features   (cross-plugin → software-development)
```

## Managed blocks

`game_tool.py` owns these reverse-index regions; edit the prose around them freely, not inside.
Run `python3 scripts/game_tool.py refresh` to regenerate them all.

| Note type | Block | Contents |
|-----------|-------|----------|
| `game-mechanic` | `## Used In` | quests, levels and items that reference this mechanic |
| `character` | `## Quests` | quests this character gives |
| `faction` | `## Members` | characters whose `faction` is this |
| `location` | `## Set Here` | quests and levels whose `location` is this |

## Lifecycle vocabularies

Four types carry a lifecycle status, moved with `game_tool.py set-status`:

| Type | Field | Values |
|------|-------|--------|
| `game-mechanic` | `state` | `concept` → `prototyped` → `tuned` → `shipped` (or `cut`) |
| `quest` | `quest_status` | `design` → `blockout` → `scripted` → `shipped` (or `cut`) |
| `level` | `level_status` | `design` → `blockout` → `art` → `polished` → `shipped` (or `cut`) |
| `lore` | `canon` | `proposed`, `canon`, `retconned`, `non-canon` |

The four catalog types (`item`, `character`, `faction`, `location`) have no lifecycle.

## `game-mechanic` notes (`Wiki/GameMechanics/`, no source required)

A rule or system the player engages with (combat, crafting, movement, an economy).

| Field | Meaning |
|-------|---------|
| `tags` | `[mechanic]` |
| `state` | see the lifecycle table |
| `category` | free-text grouping (combat / economy / movement / progression / …) |
| `features` | slugs of `software-development` `feature` notes that implement it (cross-plugin) |
| `related_mechanics` | slugs of other mechanics it interacts with |

The body names how it works, the intended feeling, and the tuning knobs. A mechanic without a
stated "why it's fun" isn't ready.

## `lore` notes (`Wiki/Lore/`, no source required)

A piece of worldbuilding, told as in-world truth.

| Field | Meaning |
|-------|---------|
| `tags` | `[lore]` |
| `canon` | see the lifecycle table — `proposed` until the team commits it |
| `era` | free-text timeline label |
| `characters` / `factions` / `locations` | slugs it involves |

`canon` is deliberately honest: `retconned` lore is kept, not deleted, so contradictions stay
findable.

## `quest` notes (`Wiki/Quests/`, no source required)

A structured objective, mission, or story beat.

| Field | Meaning |
|-------|---------|
| `tags` | `[quest]` |
| `quest_status` | see the lifecycle table |
| `quest_type` | free-text (main / side / faction / tutorial / …) |
| `giver` | slug of the `character` who gives it |
| `location` | slug of the `location` it plays out in |
| `mechanics` | slugs of the mechanics it uses |
| `rewards` | slugs of the `item`s it grants |
| `prerequisites` | slugs of `quest`s that must come first |

`prerequisites` also guard against spoilers: a quest should never reference the outcome of one
that lists it as a prerequisite.

## `level` notes (`Wiki/Levels/`, no source required)

A designed space, area, or encounter.

| Field | Meaning |
|-------|---------|
| `tags` | `[level]` |
| `level_status` | see the lifecycle table |
| `location` | slug of the `location` it realises |
| `mechanics` | slugs of the mechanics it introduces or tests |
| `quests` | slugs of `quest`s set here |
| `enemies` | slugs of `character`s the player fights here |

## `item` notes (`Wiki/Items/`, no source required)

An item, piece of equipment, collectible, or resource.

| Field | Meaning |
|-------|---------|
| `tags` | `[item]` |
| `item_type` | free-text (weapon / consumable / key / material / …) |
| `rarity` | free-text (common / rare / legendary / …) |
| `cost` | free-text price or acquisition cost |
| `mechanics` | slugs of the mechanics it plugs into |
| `source` | free-text — where the player gets it |

## `character` notes (`Wiki/Characters/`, no source required)

A character, NPC, or boss.

| Field | Meaning |
|-------|---------|
| `tags` | `[character]` |
| `role` | free-text (protagonist / npc / enemy / boss / merchant / …) |
| `faction` | slug of the `faction` they belong to |
| `home` | slug of their home `location` |

## `faction` notes (`Wiki/Factions/`, no source required)

A group or organisation the world is made of.

| Field | Meaning |
|-------|---------|
| `tags` | `[faction]` |
| `homeland` | slug of the `location` they're based in |
| `allies` / `enemies` | slugs of other factions |

## `location` notes (`Wiki/Locations/`, no source required)

A place in the world. Locations nest via `parent`, so a city can sit inside a region.

| Field | Meaning |
|-------|---------|
| `tags` | `[location]` |
| `parent` | slug of the containing `location` |
| `controlling_faction` | slug of the `faction` that holds it |

## Relationship to core `entity`

The core `entity` type still exists for real-world or out-of-world things (the studio, a
middleware vendor, a real place a level is modelled on). Use `character`/`faction`/`location` for
things *inside the fiction*, and `entity` for things outside it.

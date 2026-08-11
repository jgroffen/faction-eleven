# Faction Eleven Frontmatter Schema

Project-local note types for Faction Eleven, registered by `Schema/plugins/faction-eleven.json`.
These sit alongside the `game-development` and `software-development` plugins and are specific to
this game's chaptered release ([[chapter-based-release]]).

## `chapter` notes (`Wiki/Chapters/`, no source required)

One note per released chapter. Chapters are the unit content is **balanced** against: which
factions appear, in what form, carrying which story beats, and how much has to be built.

| Field | Meaning |
|-------|---------|
| `tags` | `[chapter]` |
| `chapter_number` | integer, 1-based |
| `chapter_status` | `outline` → `design` → `building` → `shipped` (or `cut`) |
| `lead_faction` | slug of the `faction` carrying main plot progression |
| `factions` | slugs of every faction appearing, in any form |
| `quests` | slugs of the `quest` notes set in this chapter |

`game_tool.py` does not manage chapter notes — it belongs to the game-development plugin and does
not know this type exists. Chapter rollups are therefore maintained by hand, with one aid:

## The `chapter:` field on quests

`quest` notes carry an extra `chapter:` field naming the chapter they belong to. It is not part of
the game-development schema — lint tolerates unknown fields — and it exists so the mapping can be
recovered from the quests themselves:

```bash
grep -l "^chapter: chapter-02" Wiki/Quests/*.md
```

Keep it in sync with the chapter note's `quests` list.

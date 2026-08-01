---
name: gdd-worldbuild
description: This skill should be used when the user asks to "build the world", "add a location/faction/character", "create the setting", "write some lore", "populate the world", or "add an item" in a vault with the game-development plugin. It interviews the user about the setting and creates grounded location, faction, character, item and lore notes, wired together.
---

# Game Development: Build the world

Turn a game's setting into `location`, `faction`, `character`, `item` and `lore` notes — the
world that quests, levels and mechanics all hang off. Run this **first** after installing the
plugin, and again whenever the world grows.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `game-development`). If not, install it — see the repo's plugins/README.md.
- You know the game's setting, or the user is ready to invent it with you.

## Steps

1. **Load the prompt template** from the vault's `_prompts/worldbuilding.md`. Follow it.
2. **Check what exists:** `python3 scripts/game_tool.py list-notes --tag location` (and
   `--tag faction`, `--tag character`). Update existing notes rather than duplicating.
3. **Interview** the setting the way a player discovers it — the place, the powers, the people,
   the history, the stuff — only as deep as the game needs.
4. **Create notes in dependency order** (the tool rejects a link to something that doesn't exist
   yet): locations → factions → characters → items → lore.
   ```bash
   python3 scripts/game_tool.py new-location  --name "Thornvale" --parent the-frostmarch
   python3 scripts/game_tool.py new-faction   --name "The Ashen Circle" --homeland thornvale
   python3 scripts/game_tool.py new-character --name "Vess" --role npc \
       --faction the-ashen-circle --home thornvale
   python3 scripts/game_tool.py new-lore      --title "The Long Winter" --canon canon \
       --faction the-ashen-circle --location thornvale
   ```
5. **Fill the prose** in each note (`## The Place`, `## Identity`, `## Character`, `## The
   Story`). The tool maintains the rollups — a faction's `## Members`, a location's `## Set Here`.

## Guardrails

- **Author before you link.** Create a faction before naming it in a character's `--faction`.
- Keep in-fiction things as `character`/`faction`/`location`. A real place a level is *modelled
  on*, or the studio itself, is a core `entity`.
- **Canon is a commitment.** Leave lore `proposed` until the team has agreed it; mark overturned
  lore `retconned`, never delete it.
- Give every faction a want and every character a home — otherwise ask whether the note is needed
  yet. A tight world beats a sprawling thin one.
- **Stop at the world.** Quests and levels come from **gdd-quest** / **gdd-level**; a worldbuild
  pass that also invents the whole quest line produces filler.

## Done when

`python3 scripts/game_tool.py status` shows the world populated, the gate passed, and the user
agrees the setting hangs together. Then point them at **gdd-mechanic**, **gdd-quest** or
**gdd-level**.

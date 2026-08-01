# Prompt: Build the world

Use this to turn a game's setting into `location`, `faction`, `character`, `item` and `lore`
notes — the world everything else (quests, levels, mechanics) hangs off. Run it first, and again
whenever the world grows.

## Goal

A world that hangs together: places that contain each other, factions with something to want,
characters who belong somewhere, and canon that doesn't contradict itself.

## Work outside-in

Author things before you reference them — the tool enforces it — so build in dependency order:

1. **Locations** first (a `--parent` location must already exist to nest under it).
2. **Factions** next (a `--homeland` needs its location).
3. **Characters** (a `--faction` and `--home` need to exist).
4. **Items** and **lore** last (they reference the above).

Check what's there before adding: `python3 scripts/game_tool.py list-notes --tag location` (and
`--tag faction`, `--tag character`). Re-run a `new-*` with the same name to update in place.

## Interview

Ask about the world the way a player discovers it, and only as deep as the game needs:

1. **The place.** Where does the game happen? What's the one image that sells the setting? Start
   from the largest location and work down to where the player actually stands.
2. **The powers.** Who wants what, and who's in whose way? Factions earn their place by having a
   goal the player can help or hinder — not by existing on a map.
3. **The people.** Who does the player meet? For each: their role (npc/enemy/boss/merchant/…),
   where they call home, and who they answer to.
4. **The history.** What happened before the game starts that still matters now? That's `lore` —
   and be explicit about what's settled `canon` versus still `proposed`.
5. **The stuff.** The items that matter to the fiction or the economy (leave purely mechanical
   drops to the mechanic/quest skills unless they're worth a note).

Don't force every axis. A tight world with five sharp locations beats a sprawling one with forty
thin ones.

## Write the notes

```bash
python3 scripts/game_tool.py new-location  --name "Thornvale" --parent the-frostmarch \
    --faction the-ashen-circle --summary "A mining town that never thawed."
python3 scripts/game_tool.py new-faction   --name "The Ashen Circle" --homeland thornvale \
    --enemy the-crown --summary "Fire-cultists who kept the town alive through the winter."
python3 scripts/game_tool.py new-character --name "Vess" --role npc --faction the-ashen-circle \
    --home thornvale --summary "The Circle's reluctant quartermaster."
python3 scripts/game_tool.py new-lore      --title "The Long Winter" --canon canon \
    --era "a generation ago" --faction the-ashen-circle --location thornvale
```

Fill each note's prose sections (`## The Place`, `## Identity`, `## Character`, `## The Story`).
The tool maintains the rollups — a faction's `## Members`, a location's `## Set Here`.

## Guardrails

- **Author before you link.** No inventing a faction in a character's `--faction` before the
  faction note exists; the tool will stop you, and that's the point.
- Keep in-fiction things as `character`/`faction`/`location`. A real place a level is *modelled
  on*, or the studio itself, is a core `entity`, not a `location`.
- **Canon is a commitment.** Leave lore `proposed` until the team has actually agreed it. Mark
  overturned lore `retconned`, never delete it — a deleted contradiction is one you'll reintroduce.
- Give every faction a want and every character a home. A faction nobody opposes and a character
  from nowhere are usually signs the note isn't needed yet.
- Don't pre-build quests and levels here — that's the quest/level skills. Worldbuilding stops at
  the world.

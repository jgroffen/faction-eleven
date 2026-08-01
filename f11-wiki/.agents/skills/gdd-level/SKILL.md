---
name: gdd-level
description: This skill should be used when the user asks to "design a level", "lay out an area", "block out a zone", "design an encounter", or "add a dungeon/map" in a vault with the game-development plugin. It interviews the user about the space and its flow, wires the level to its location/mechanics/quests/enemies, and creates a grounded level note.
---

# Game Development: Design a level

Turn a place in the world into a `level` note — a designed space with a fantasy, a flow, the
mechanics it tests, the quests set in it, and the enemies the player meets.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `game-development`). If not, install it — see the repo's plugins/README.md.
- The `location` this level realises exists (**gdd-worldbuild** it if not), along with the
  mechanics, quests and characters it references.

## Steps

1. **Load the prompt template** from the vault's `_prompts/level-design.md`.
2. **Ground it:** `list-notes --tag location` (which place it realises), `--tag game-mechanic`,
   `--tag quest`, `--tag character` (enemies). Create anything missing first.
3. **Interview** for the fantasy (the feeling, the memorable image), the flow (path, pacing,
   where it opens and pinches), the mechanics it teaches or tests, the encounters, and the
   production risks.
4. **Create it:**
   ```bash
   python3 scripts/game_tool.py new-level --title "The Ashen Hall" --location thornvale \
       --mechanic ember-crafting --quest light-the-braziers --enemy frost-revenant \
       --status blockout \
       --summary "A collapsed foundry the player relights brazier by brazier."
   ```
   Fill `## Fantasy`, `## Flow`, and `## Notes`. `## Encounters` / `## Set Here` track the linked
   enemies and quests.

## Guardrails

- **Location vs level:** the `location` is the *fictional place*; the `level` is the *designed
  space* the player traverses. One location can hold several levels. Keep them as separate notes
  and link with `--location`.
- **Author before you link** — location, mechanics, quests and enemies must already exist.
- Give the level a focus: a level that introduces five mechanics teaches none of them.
- Enemies are `character` notes with a combat `role`; author a boss as a character first, then
  list it as `--enemy`.
- Move `--status` along as it's built (`blockout` → `art` → `polished` → `shipped`).

## Done when

The gate passed, the level names its fantasy and flow, and it's wired to its location, mechanics,
quests and enemies.

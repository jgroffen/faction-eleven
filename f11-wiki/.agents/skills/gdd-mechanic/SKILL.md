---
name: gdd-mechanic
description: This skill should be used when the user asks to "design a mechanic", "add a game mechanic", "how should X work", "design the combat/crafting/movement system", or "spec out a gameplay system" in a vault with the game-development plugin. It interviews the user about the rule and the feeling it's for, creates a grounded mechanic note, and links it to the software-development feature that implements it when that plugin is present.
---

# Game Development: Design a mechanic

Turn "the game should let you X" into a `game-mechanic` note a team could prototype from — the rule,
the feeling it's for, and the knobs that tune it.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `game-development`). If not, install it — see the repo's plugins/README.md.
- If the **software-development** plugin is also installed, you can link the mechanic to the
  `feature` that implements it — check `python3 scripts/dev_tool.py list-notes --tag feature`.

## Steps

1. **Load the prompt template** from the vault's `_prompts/mechanic-design.md`.
2. **Ground it:** `python3 scripts/game_tool.py list-notes --tag game-mechanic` — avoid duplicating or
   overlapping an existing mechanic (link it as `--related` instead).
3. **Interview** for the verb (what the player does), the feeling and the decision it asks, the
   rules, the tuning knobs, and the mechanics it interacts with.
4. **Create it:**
   ```bash
   python3 scripts/game_tool.py new-mechanic --name "Ember Crafting" --state prototyped \
       --category economy --feature crafting-system --related fuel-management \
       --summary "Spend gathered embers to forge single-use tools at any brazier."
   ```
   Fill `## How It Works`, `## Why It's Fun`, and `## Tuning`. The `## Used In` block fills itself
   from the quests, levels and items that reference the mechanic.

## Guardrails

- **Design, not implementation.** *What the player experiences* is the mechanic; *how the code
  does it* is a software-development `feature`/`component`, linked with `--feature`. Keep them
  separate.
- **Name the feeling.** A mechanic note without `## Why It's Fun` is a spec, not a design.
- One mechanic per note — "combat" is a category; "parry", "stagger", "execute" are mechanics.
- Don't over-tune on paper: list the knobs, leave the values for playtests, and only move
  `--state` to `tuned` once they've actually been tuned.
- `--feature` links validate only if software-development is installed; otherwise they're kept as
  unverified references. Don't invent feature slugs to look finished.

## Done when

The gate passed, the mechanic note names its feeling and its knobs, and — if software-development
is installed — it's linked to the feature(s) that will build it.

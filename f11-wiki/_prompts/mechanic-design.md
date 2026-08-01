# Prompt: Design a mechanic

Use this to turn "the game should let you X" into a `game-mechanic` note a team could prototype from —
and, when software-development is installed, to link it to the `feature` that will implement it.

## Goal

A mechanic note that states the rule, names the feeling it's for, and lists the knobs that tune
it. If you can't say why it's fun, it isn't ready.

## Ground it first

- `python3 scripts/game_tool.py list-notes --tag game-mechanic` — does this already exist, or overlap
  with one that does? Prefer updating, or linking as `--related`, over a near-duplicate.
- If the software-development plugin is installed, check for the `feature`(s) that would build it
  (`python3 scripts/dev_tool.py list-notes --tag feature`) so you can wire `--feature`.

## Interview

1. **The verb.** What does the player *do*, moment to moment? State it as an action, not a system
   name ("hold to charge, release to leap", not "the traversal system").
2. **The feeling.** What should it feel like, and what decision does it ask of the player? A
   mechanic with no interesting choice is a chore.
3. **The rules.** Inputs, outputs, costs, cooldowns, failure. Enough that someone could build a
   greybox from the note.
4. **The knobs.** Which numbers tune it, and what each trades off? These go in `## Tuning` and are
   what playtests will move.
5. **The web.** Which other mechanics does it interact with (combos, tensions)? Link them with
   `--related`.
6. **The state.** Is this `concept`, `prototyped`, `tuned`, or `shipped`? Be honest — `concept`
   is where most live, and that's fine.

## Write it

```bash
python3 scripts/game_tool.py new-mechanic --name "Ember Crafting" --state prototyped \
    --category economy --feature crafting-system --related fuel-management \
    --summary "Spend gathered embers to forge single-use tools at any brazier."
```

Fill `## How It Works`, `## Why It's Fun`, and `## Tuning`. The `## Used In` block fills itself
from the quests, levels and items that reference the mechanic.

## Guardrails

- **Design, not implementation.** *What the player experiences* is the mechanic; *how the code
  does it* is a software-development `feature`/`component`. Keep the mechanic note about the former
  and link the latter with `--feature`.
- Name the feeling. A mechanic note without `## Why It's Fun` is a spec, not a design.
- Don't over-tune on paper. List the knobs; leave the values for playtests to find, and update
  `--state` to `tuned` only once they actually have been.
- `--feature` links are validated only if software-development is installed; without it they're
  kept as unverified references (the tool says so). Don't invent feature slugs to look complete.
- One mechanic per note. "Combat" is not a mechanic; "parry", "stagger" and "execute" are.

# Prompt: Design a level

Use this to turn a place in the world into a `level` note — a designed space with a fantasy, a
flow, the mechanics it tests, the quests set in it, and the enemies the player meets.

## Goal

A level note a designer could greybox from: what it feels like, how the player moves through it,
and what they encounter.

## Ground it in the world

A level realises a `location` and pulls in existing pieces. Before writing:

- `python3 scripts/game_tool.py list-notes --tag location` — which place does this level realise?
  (Author it in worldbuilding first if it doesn't exist.)
- `--tag game-mechanic` — which systems does the level introduce or test?
- `--tag quest` — which quests play out here?
- `--tag character` — which characters/enemies appear?

## The difference between a location and a level

A `location` is the *fictional place* ("Thornvale, a frozen mining town"). A `level` is the
*designed space* the player traverses ("The Ashen Hall — the approach, the collapsed shaft, the
brazier chamber"). One location can hold several levels; a level names its location with
`--location`.

## Interview

1. **The fantasy.** What does being here make the player feel, and what's the one image they'll
   remember?
2. **The flow.** The path through it — the beats, the pacing, where it opens up and where it
   pinches. Where does the player catch their breath, and where does it spike?
3. **The mechanics.** What does this level teach or test? A good level has a focus, not a
   checklist.
4. **The encounters.** Who and what the player meets — enemies (`--enemy`), and the quests
   (`--quest`) that unfold here.
5. **The production reality.** What's expensive or risky to build? Note it now.

## Write it

```bash
python3 scripts/game_tool.py new-level --title "The Ashen Hall" --location thornvale \
    --mechanic ember-crafting --quest light-the-braziers --enemy frost-revenant \
    --status blockout \
    --summary "A collapsed foundry the player relights brazier by brazier, pushing back the cold."
```

Fill `## Fantasy`, `## Flow`, and `## Notes`. The `## Encounters` and `## Set Here` sections
track the linked enemies and quests.

## Guardrails

- **Author before you link** — location, mechanics, quests and enemies must already exist.
- Keep the fiction (`location`) and the design (`level`) as separate notes; link, don't merge.
- Give the level a focus. A level that introduces five mechanics teaches none of them.
- Move `--status` along as it's built (`blockout` → `art` → `polished` → `shipped`) so the design
  rollup is truthful.
- Enemies are `character` notes with a combat `role`; author a boss as a character first, then
  list it as an `--enemy` here.

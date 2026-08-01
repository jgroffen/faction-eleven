# Prompt: Design a quest

Use this to turn a story idea into a `quest` note — wired to its giver, its place, the mechanics
it leans on, its rewards, and the quests that must come first.

## Goal

A quest with a hook, clear objectives, and honest prerequisites — and one that doesn't spoil, or
get spoiled by, the quests around it.

## Ground it in the world

A quest links to things that must already exist. Before writing:

- `python3 scripts/game_tool.py list-notes --tag character` — who could give it?
- `--tag location` — where does it happen?
- `--tag game-mechanic` — what does it ask the player to do?
- `--tag item` — what does it reward? (Author the reward item first if it's new.)
- `--tag quest` — what has to happen before this?

If a needed piece doesn't exist, create it (worldbuilding for people/places/items, the mechanic
skill for systems) rather than referencing a slug that isn't there.

## Interview

1. **The hook.** How does it start, and why does the player care in the first ten seconds?
2. **The shape.** What does the player actually do — the objectives, in order? Keep them things a
   player can see they've done.
3. **The place and the giver.** Where does it play out, and who sets it off?
4. **The mechanics.** Which systems does it exercise or teach? A quest is a good place to introduce
   a mechanic — note that intent.
5. **The reward.** What's it worth, and why is that worth the effort?
6. **The order.** What must come first (`--prereq`)? And crucially: **does anything the player
   already did spoil this, or does this spoil anything later?**

## Write it

```bash
python3 scripts/game_tool.py new-quest --title "Light the Braziers" --type main \
    --giver vess --location thornvale --mechanic ember-crafting --reward cinder-key \
    --prereq reach-thornvale --status design \
    --summary "Vess needs the town's braziers relit before nightfall — the player's first taste of ember crafting."
```

Fill `## Hook`, `## Objectives`, and `## Notes` (branching, failure states). The `## Rewards` and
`## Prerequisites` sections track the linked items and quests.

## Keep the sequence spoiler-safe

Quests are played in an order constrained by `prerequisites`. The invariant: **nothing in a quest
may reveal the outcome of a quest that lists it as a prerequisite, and a quest may assume anything
its prerequisites established.** When you add a `--prereq`, read both quests and check:

- Does this quest's hook or objectives give away a twist the prerequisite is building to?
- Does the reward or a character's line here presume knowledge the player only gets *later*?

Fix by rewording, resequencing (change which is the prerequisite), or splitting the reveal. The
tool records the dependency; keeping the writing clean is the design work.

## Guardrails

- **Author before you link** — the tool rejects a giver, location, mechanic, reward or prereq that
  doesn't exist.
- A quest is content (one thing to do). The *system* that powers a class of quests is a `game-mechanic`
  or a software-development `feature`, not a quest.
- Objectives should be observable. "Understand the Circle's motives" isn't an objective; "read
  Vess's three letters" is.
- Don't leave a quest `design` once it's built — move `--status` along (`blockout` → `scripted` →
  `shipped`) so `status` reflects reality.

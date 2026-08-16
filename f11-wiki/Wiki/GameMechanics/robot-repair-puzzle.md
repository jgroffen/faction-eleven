---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-12
updated: 2026-08-12
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
  - Raw/Sources/factions-retro-readme.md
source_count: 2
aliases:
  - Repairing Deranged Robots
  - Diagnosis
state: concept
category: progression
features: []
related_mechanics:
  - autofix-skill-tree
  - minibot-command
---

# Robot Repair

The [[robots]]' core activity and the source of [[autofix]]'s progression: find a broken robot,
work out what it needs, supply the modules and components, and bring it back. **A parts puzzle
with varied outcomes.**

**State:** concept · **Category:** progression

**Implemented by:** _(no feature notes yet)_

## How It Works

**Diagnosis first, and diagnosis is itself a skill.**

- Autofix **always knows whether a robot can be repaired or not**.
- He **does not know how** until his **diagnostic skills** are upgraded ([[autofix-skill-tree]],
  Upgrades branch — including **scanning range**).
- Once he can diagnose a malfunctioning or fully disabled robot, **he knows exactly what parts the
  repair needs** — specific **modules** and **components**, which must then be fabricated.

So the loop is: *can this be fixed?* → *what does it need?* → *can I make that yet?*

### Outcomes

| Outcome | Result |
|---------|--------|
| **Repairable, and repaired** | **Data Fragments**, **lore**, **quests**, and **unblocked paths** that open more exploration |
| **Not repairable** | the robot can be **scrapped** for materials |
| **Not repairable *yet*** | **some of these block progress** until the tree has grown |

That third row is the design's cleverest part. A robot you cannot yet fix is a **locked door with a
diagnosis attached** — the player knows precisely which upgrade they lack, because Autofix told
them. It is Metroid gating where the gate explains itself, and it converts frustration into a
shopping list.

### Aggressive robots

Some robots have **gone mad or become aggressive**. These are handled by the specialist minibots —
Shield-bot, Suppressor-bot, EMP-bot — which **disable rather than destroy**, so Autofix can then
repair them ([[minibot-command]]).

## Why It's Fun

Not yet defined. What the design does is unusual and worth protecting: **the enemies are
the rewards.** There is no reason to destroy a robot when robots are the scarce thing, so combat
resolves into recruitment, and every hostile encounter is a resource you have not unlocked yet.

## Tuning

No values yet. The load-bearing ratio is **how many repairs are gated on unbuilt skills** — too
many and the realm is a wall, too few and diagnosis is decoration.

## Story Weight

Repairs carry the faction's exposition twice over. Lore and quests arrive attached to the robots you
save — and the **Data Fragments** they yield are literally recovered history, the raw material
[[autofix]] researches to rediscover lost technology ([[autofix-skill-tree]]). Mending a robot and
reading its memory are the same act. So
the more of his people Autofix restores, the more of his own history he recovers — which is the
same shape as [[mifix]]'s corrupted memory on the other side of the gate, and the same shape as the
game's whole mystery.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[autofix-skill-tree]] — what repairs pay for, and what gates them.
- [[minibot-command]] — the non-lethal toolkit that makes hostile robots repairable.
- [[robots]] — the people being put back together.

## Open

- Whether a robot can be **scrapped by choice** when it could have been repaired — a moral knob the
  design has not touched, and a sharp one given [[no-machine-repairs-itself]].
- Whether Data Fragments are generic or **specific to the robot they came from**, which would make
  particular robots worth hunting for particular unlocks.
- What "kinds of damage" the Repair branch distinguishes.

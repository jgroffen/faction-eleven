---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-08
updated: 2026-08-08
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Robots Game Style
state: concept
category: progression
features: []
related_mechanics:
  - exploration-core-loop
  - faction-genre-mechanics
---

# Robots — Incremental Exploration

The [[robots]] faction's game style, **replacing** the prototype's Civ / Defender of the Crown
region-control design. It is an **exploration platformer with incremental growth**: the player
collects parts and other currencies, repairs robots, and unlocks exploration through an
**incrementally unlocked skill tree** — needing wall-crawling, for example, to reach some areas.

**State:** concept · **Category:** progression

**Implemented by:** _(no feature notes yet)_

## How It Works

**Exploration is the spine.** [[realm-02]] is explored as a platformer on the shared
[[exploration-core-loop]] shell; everything else feeds it or gates it. The faction's systems split
into three, each with its own note:

| System | What it is |
|--------|-----------|
| [[robot-repair-puzzle]] | find broken robots, diagnose them, fabricate what they need, bring them back. The source of **skill points, lore, quests and unblocked paths**. |
| [[autofix-skill-tree]] | one tree, five branches — Scrapping, Upgrades, Fabrication, Repair, Robotics — fed by skill points, refining **scrap → construction materials → modules and components**. |
| [[minibot-command]] | build minibots and command them within range. The **comms ladder** turns them from followers, to tools, to an automated workforce. |

The incremental curve is the interaction of the three: repairing robots buys the tree, the tree
builds the minibots, the minibots collect the scrap and disable the hostile robots, which makes
more repairs possible.

**And the whole realm is sealed.** Every gate from [[realm-02]] is shut
([[sealed-interplane-gates]]), so all of this growth happens inside a closed box — until a stranger
cracks a gate ([[the-cracked-gate]]).

## Why It's Fun

Not yet stated by the author. Structurally, the appeal it's reaching for is the incremental
genre's core pleasure — a curve that always climbs — welded to exploration's, which is that the
world gets bigger when *you* do.

## Tuning

No values yet. The knob that will matter most is the **rate the tree unlocks relative to the map's
gates**: too fast and the world is never closed, too slow and the player is looking at a wall
they cannot climb with nothing to do about it.

## Open

- Where **wall-crawling** and the other movement gates sit — presumably the Upgrades branch's
  *movement* line, but that is not stated.
- How **[[faction-currencies]]**' "Parts" relates to **scrap**, **construction materials**,
  **modules** and **components**. The prototype's single currency has been replaced by a chain and
  the note needs reconciling.
- What survives of the prototype's region-control map ([[nested-map-navigation]] levels 2–3).

## Chapter One

This is the **main plot progression of chapter one** ([[chapter-based-release]]), so it is the
first genre to be built after the shell — and the one the game will be judged on first.

## Used In

<!-- gd:used-in:start -->
- [[the-first-signal|The First Signal]] · quest
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shell it builds on.
- [[faction-genre-mechanics]] — the per-faction genre layer this is an instance of.
- [[faction-unique-features]] — the robots' contribution to the final game mode, still unnamed;
  repair is the obvious candidate.

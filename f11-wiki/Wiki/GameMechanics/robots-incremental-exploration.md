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

Three loops, each feeding the next:

1. **Explore** — platforming through the ruins of [[realm-02]], on the shared
   [[exploration-core-loop]] shell.
2. **Collect and repair** — gather **Parts** and other currencies; repair robots. Repaired robots
   are the growth curve: [[autofix]] is the only working Autofix, and repairing is the one thing
   it can do that nothing else in its realm can.
3. **Unlock** — spend growth on a **skill tree**, unlocked incrementally. Skills are not only
   power; they are **keys**. Wall-crawling opens walls. The tree gates the map.

So the incremental layer and the exploration layer are the same layer: numbers going up is how
doors open. This is Metroid-style ability gating with an incremental economy driving it, rather
than set-piece ability pickups.

Not yet established:

- What the currencies beyond **Parts** are, and whether they gate different branches of the tree.
- Whether repaired robots are *automation* — bots that gather while you explore, the classic
  incremental engine — or purely narrative allies. The fiction points hard at the first: Autofix
  can build **mini-fix bots**, and a bot that repairs bots is an idle-game production chain by
  definition. **Unconfirmed.**
- Whether the skill tree belongs to Autofix or to the faction.
- What survives of the prototype's region-control map ([[nested-map-navigation]] levels 2–3).

## Why It's Fun

Not yet stated by the author. Structurally, the appeal it's reaching for is the incremental
genre's core pleasure — a curve that always climbs — welded to exploration's, which is that the
world gets bigger when *you* do.

## Tuning

No values yet. The knob that will matter most is the **rate the tree unlocks relative to the map's
gates**: too fast and the world is never closed, too slow and the player is looking at a wall
they cannot climb with nothing to do about it.

## Chapter One

This is the **main plot progression of chapter one** ([[chapter-based-release]]), so it is the
first genre to be built after the shell — and the one the game will be judged on first.

## Used In

<!-- gd:used-in:start -->
- [[the-shrine-bot-awakens|The Shrine Bot Awakens]] · quest
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shell it builds on.
- [[faction-genre-mechanics]] — the per-faction genre layer this is an instance of.
- [[faction-unique-features]] — the robots' contribution to the final game mode, still unnamed;
  repair is the obvious candidate.

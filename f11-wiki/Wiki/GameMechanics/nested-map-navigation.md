---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-08
updated: 2026-08-08
sources:
  - Raw/Sources/factions-retro-readme.md
source_count: 1
aliases: []
state: concept
category: navigation
features: []
related_mechanics:
  - exploration-core-loop
---

# Nested Map Navigation

Navigation is a **six-level zoom**, from the faction select screen down to a single encounter.
Selecting a faction zooms into a world map for that faction, *if appropriate* — not every faction
needs every level.

**State:** concept · **Category:** navigation

**Implemented by:** _(no feature notes yet)_

## How It Works

| Level | Map |
|-------|-----|
| 1 | Faction |
| 2 | World |
| 3 | Region |
| 4 | Fast-travel |
| 5 | Location |
| 6 | Encounter |

The "if appropriate" qualifier matters: it is the seam that lets ten different genres share one
navigation shell. A 4X faction lives high in the stack; a stealth platformer lives low.

The [[robots]] story is the clearest worked example — it **swaps between location exploration and
region control views**, starting in location exploration, and the world map opens up only after a
location is cleared.

A more radical version exists: the faction select screen as a **z-axis of circular world maps**,
which would make for interesting speedrun routing.
Unresolved.

## Why It's Fun

Not yet defined.

## Tuning

No values yet.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — what happens at the bottom of the zoom.
- [[protagonist-swapping-and-story-gating]] — level 1 is where swapping happens; the prototype
  notes say returning to the select screen depends on the faction, with some requiring waypoints
  or camping.

**Unconfirmed** — carried over from the earlier prototype.

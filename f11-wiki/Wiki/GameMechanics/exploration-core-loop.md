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
  - Common Gameplay Style
state: concept
category: exploration
features: []
related_mechanics:
  - faction-genre-mechanics
---

# Exploration Core Loop

The gameplay style common to all ten faction stories: **a combination of platforming and top-down
exploration**, in an open world.

**This is the shell, not the whole game.** Settled 2026-08-08: the exploration loop is the layer
every faction shares, and a faction's own genre is built *on top of* it. Some realms have
additional mechanics, but those mechanics **build on the shell** rather than replacing it. That is
what makes a 4X faction and a stealth-platformer faction the same game.

**State:** concept · **Category:** exploration

**Implemented by:** _(no feature notes yet — no code exists as of 2026-08-08)_

## How It Works

- The game is **open-world exploration** at its base.
- The presentation and movement are **mostly platforming or top-down**, shared across factions.
- Every faction's genre extends this rather than standing beside it. A faction may add mechanics;
  it may not opt out of the shell.

This makes the shell **the first thing to build** and the only system built once and used ten
times — which for a solo project ([[project-scope-and-constraints]]) is the difference between ten
games and one.

**Two presentations, chosen per faction** (settled 2026-08-08). Platforming and top-down are not
blended; they are both available in the shell, and a faction's game style picks one:

| Presentation | Factions |
|--------------|----------|
| **Platforming** | [[robots]] ([[robots-incremental-exploration]]), [[institute-of-eight]] ([[ninja-rhythm-platforming]]), [[green-skins]] ([[gargoyle-stone-metroidvania]]) |
| **Top-down** | [[celestials]] ([[celestials-hero-tower-defence]]), [[pirates]], and probably [[the-damned]] — the author's expectation, not yet settled |

A faction may use both: the [[celestials]] fight top-down but **explore in platforming sections
between battles**. So the split is per *activity*, not strictly per faction.

**One platformer, three factions** (settled 2026-08-14). The [[gargoyle]] uses **the same
platforming engine as the [[ninja]]**, with a different move set and no rhythm layer — which makes
a character, mechanically, **a list of abilities** over a shared controller. With the [[robots]]
platforming too, that is three of the ten factions running one build. It is the largest scope lever
in the project, and the Gargoyle is its first test.

Which realm's rules apply when a protagonist travels is settled separately, by
[[realm-governs-game-style]]: the realm's, not the traveller's.

Still not established: what the moment-to-moment verbs are beyond moving through space.

## Why It's Fun

Not yet stated by the author in terms of feeling. What the shell is *for* is now clear, though:
it is the continuity between ten otherwise unrelated games, so that swapping protagonist
([[protagonist-swapping-and-story-gating]]) is a change of world rather than a change of product.

## Tuning

No values yet.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[faction-genre-mechanics]] — the per-faction genre systems layered on top of this shared base.
- [[faction-eleven-premise]] — the game this loop sits inside.

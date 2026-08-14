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
  - Per-Faction Mechanics
  - Genre Per Faction
state: concept
category: structure
features: []
related_mechanics:
  - exploration-core-loop
---

# Faction Genre Mechanics

Each of the ten playable factions has **unique gameplay mechanics** layered on the shared
[[exploration-core-loop]]. The examples the author gives are **incremental**, **tower defence**,
**RPG**, and **platform-focused** — that is, each faction's story plays as a different *genre*,
not merely as a different loadout or stat spread.

**State:** concept · **Category:** structure

**Implemented by:** _(no feature notes yet — no code exists as of 2026-08-08)_

## How It Works

- All ten factions share the platforming/top-down open-world exploration base.
- On top of that base, each faction contributes a distinct genre of mechanics. The author named
  incremental, tower defence, RPG and platform-focused as examples.
- **The shared style is a shell** (confirmed 2026-08-08). Faction genres build on
  [[exploration-core-loop]] rather than replacing it; a realm may add mechanics but may not opt
  out of the shell. This is what reconciles "a mostly platform or top-down exploration game" with
  genre labels like 4X and bullet-hell.
**The genre assignments are in flux.** The author confirmed on 2026-08-08 that "the genre list has
moved" since the prototype notes, that **[[robots]] has changed for certain**, and that some —
[[fey-folk]] among them — are not locked down. A **heavy per-faction review of game style and
mechanics** is outstanding.

The prototype assignments, recorded as the last written state and **not as current design**:

| Faction | Prototype game type |
|---------|--------------------|
| [[robots]] | ~~Civ / Defender of the Crown~~ → **now [[robots-incremental-exploration]]** (settled 2026-08-08) |
| [[institute-of-eight]] | ~~Rogue-like / Isaac~~ → **now [[ninja-rhythm-platforming]]** (settled 2026-08-08); the prototype's "audio game cues" turn out to be a rhythm layer |
| [[celestials]] | Tower Defence / FTL → **now [[celestials-hero-tower-defence]]**, top-down with a directly-controlled hero unit (settled 2026-08-08) |
| [[mystics]] | Iso explorer / Diablo |
| [[fey-folk]] | Bullet-hell / 1941 — **not locked down** |
| [[pirates]] | 4X |
| [[werebeasts]] | RPG |
| [[the-damned]] | Puzzle / point-and-click |
| [[green-skins]] | ~~Stealth platformer~~ → **now [[gargoyle-stone-metroidvania]]** (settled 2026-08-14); the same platforming engine as the Ninja's, no rhythm layer, Metroid-structured |
| [[aliens]] | Choplifter / Metroid-like |

**Resolved 2026-08-08:** the unexplained "incremental" genre was the [[robots]]' new style. Its
Civ/Defender slot is gone.

**Resolved 2026-08-14 — a genre belongs to a realm, not to a protagonist.** See
[[realm-governs-game-style]]. When a protagonist travels, they play the host realm's genre: the
[[ninja]] plays a Metroid in [[realm-09]], and both he and the [[gargoyle]] play
[[celestials-hero-tower-defence]] in [[chapter-03]]. This is the rule that turns ten one-shot
genre systems into systems that get **played more than once** — the direct mitigation for the scope
risk recorded below.

Also unresolved: how deep each genre goes — whether a faction's genre governs its whole story or
surfaces in particular sequences.

## Why It's Fun

Stated intent, inferred from the premise rather than asserted by the author: playing ten stories
as ten protagonists is only worth doing if the ten play differently, and genre is the strongest
available axis of difference. The author has not yet stated the intended feeling in their own
words — flagged for a later round.

## Tuning

No values yet.

## Scope Risk

This mechanic is also the project's largest scope commitment: ten genre systems, built by one
developer (see [[project-scope-and-constraints]]). Recorded here so the risk is attached to the
design that creates it rather than discovered later.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shared base these genres vary on top of.
- [[faction-eleven-premise]] — the ten-stories structure this serves.

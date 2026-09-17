---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-08
updated: 2026-09-15
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
[[exploration-core-loop]] — that is, each faction's story plays as a different *genre*, not merely
as a different loadout or stat spread. **Incremental**, **tower defence**, **RPG** and
**platform-focused** are the illustrative examples.

**State:** concept · **Category:** structure

**Implemented by:** _(no feature notes yet — no code exists)_

## How It Works

- All ten factions share the platforming/top-down open-world exploration base.
- On top of that base, each faction contributes a distinct genre of mechanics.
- **The shared style is a shell.** Faction genres build on [[exploration-core-loop]] rather than
  replacing it; a realm may add mechanics but may not opt out of the shell. This is what reconciles
  "a mostly platform or top-down exploration game" with genre labels like 4X and bullet-hell.
- **A genre belongs to a realm, not to a protagonist** ([[realm-governs-game-style]]). When a
  protagonist travels, they play the host realm's genre: the [[ninja-kazuma]] plays a Metroid in
  [[realm-07]], and both he and the [[gargoyle-granite]] play [[celestials-hero-tower-defence]] in
  [[chapter-03]]. This turns ten one-shot genre systems into systems that get **played more than
  once**, and is the direct mitigation for the scope risk below.
- **The fiction supplies the reason.** A genre is a realm's [[the-setting-statement|Setting
  Statement]] — the rules the engine reads for that world — so a visitor plays the host genre because
  the host statement is the only one in force. The visiting character's own code does not switch off;
  it **self-corrects** what it meets into home terms, which is where cross-realm imbalance comes from
  and why carrying a capability across is a balancing problem by construction.

## Game Style By Faction

Six are settled, and the Pirates' is stated but not filled in. The rest carry an inherited genre from the earlier prototype which is
**unconfirmed** — the genre list has moved since then, and a per-faction review of game style and
mechanics is outstanding.

| Faction | Game style | Status |
|---------|-----------|--------|
| [[institute-of-eight]] | [[ninja-rhythm-platforming]] | settled |
| [[robots]] | [[robots-incremental-exploration]] | settled |
| [[celestials]] | [[celestials-hero-tower-defence]] | settled |
| [[green-skins]] | [[gargoyle-stone-metroidvania]] | settled |
| [[mystics]] | Iso explorer / Diablo | **unconfirmed** — and they lead [[chapter-03]] |
| [[fey-folk]] | Bullet-hell / 1941 | **unconfirmed**, explicitly not locked down |
| [[pirates]] | [[pirates-open-exploration]] — open exploration with freedom as a built-in mechanic | **partly settled** — the style is stated, its content is not; the prototype's 4X label stands alongside, unconfirmed |
| [[werebeasts]] | RPG | **unconfirmed** |
| [[the-damned]] | [[damned-undead-kingdom-rts]] — with [[wraith-memory-puzzle]] as a recruitment minigame | settled |
| [[aliens]] | Choplifter / Metroid-like | **unconfirmed** |

Do not build against the unconfirmed rows. See [[faction-design-status]].

Also unresolved: how deep each genre goes — whether a faction's genre governs its whole story or
surfaces in particular sequences.

## Why It's Fun

Not yet defined. What the structure is reaching for: playing ten stories as ten protagonists is
only worth doing if the ten play differently, and genre is the strongest available axis of
difference. **Inference, not established.**

## Tuning

No values yet.

## Scope Risk

This mechanic is the project's largest scope commitment: ten genre systems, built by one developer
(see [[project-scope-and-constraints]]).

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shared base these genres vary on top of.
- [[faction-eleven-premise]] — the ten-stories structure this serves.

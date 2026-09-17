---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-09-15
updated: 2026-09-17
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Wraith Game Style
  - The Wraith Mini-Game
  - Wraith Recruitment Minigame
state: concept
category: puzzle
features: []
related_mechanics:
  - damned-undead-kingdom-rts
  - exploration-core-loop
  - faction-genre-mechanics
  - wraith-object-reading
---

# Wraith — Memory Puzzle

**A recruitment minigame inside [[damned-undead-kingdom-rts]]**, the Damned's game: a **puzzle
game** in which you wake up as a [[wraiths|wraith]] and have to **work out who you were when alive
and why you have not moved on.** The RTS plays it on a map that requires a wraith; the wraith is
[[wraith-delahaye]], and she is the one recruitment that does not take. The prototype's "puzzle /
point-and-click" label is the one inherited genre that survives as stated — for this minigame.

**State:** concept · **Category:** puzzle

**Implemented by:** _(no feature notes yet — no code exists)_

## How It Works

**Two exits, by the rules.** A wraith either works out who it was and why it stayed, **resolves the
unfinished business and releases its spirit** — or **joins the ranks of the Damned**, which is the
recruitment the RTS is playing for ([[wraiths]]).

**Two play spaces.** The story is played in [[realm-08]], the Damned's realm and the RTS's world
map, and in [[the-wraith-s-mansion]] — a mansion that is a representation of the Wraith's mind and
memories. The realm is the world; the mansion is the protagonist. How the player moves between the
two is not stated.

**The goal is a person, not a place.** The Wraith was a **Pirate — a First Mate** named
**Delahaye** — and does not know it ([[pirates]]). **Her name is one of the memories**: she starts
without it and learns it through play. She is the Specialist of two factions on purpose: it gives
her a clear gameplay style, and a **party role** for any game that calls for party mechanics.
Progress is measured in memories unlocked, and the memories are the answer to the question the
whole story asks.

**The answer is a war.** What her gameplay uncovers is her **unresolved goal from life: rescuing
the Pirates from the invading [[institute-of-eight]]** ([[the-pirate-institute-war]]). She died
fighting in a pirate armada, shortly before the gates were sealed, and the Damned took her body home
with many others ([[the-linking-of-the-realms]]) — so the last memories the puzzle returns are a
detailed picture of the time just before the sealing ([[the-long-disconnection]]). The puzzle's
reward is not only a self but a witness.

**Delahaye takes neither exit.** Her business **cannot be resolved** — the invasion ended a thousand
years ago — and she is **not recruited: her power of will breaks her out of the game.** The player
cannot fail this: "will" is [[pirates-open-exploration|freedom]], a mechanic built into Pirate
characters, and the Damned's recruitment cannot translate it. **The break-out freezes the RTS.**
From there the player **moves her around the frozen world map, searching its locations with this
minigame's mechanics** ([[wraith-object-reading]] and the memory puzzle) for a way to [[realm-06]]
([[damned-undead-kingdom-rts]]).

**Unlocking memories changes the protagonist's body.** As memories return the Wraith becomes **less
ghost-like and more like a real person.** The power curve is legibility: the player is not
collecting abilities but a self, and can see how much of it she has by looking at her.
What "less ghost-like" does mechanically — whether a more solid Wraith can touch, be seen, or be
hurt by things a ghost cannot — is not defined.

**The verb that drives it is [[wraith-object-reading]]:** touch an object, know its history and the
emotional connections tied to it. A puzzle game about recovering a life, played by a character who
can read the past out of things, is the one mechanic explaining the other.

**It is bound to one place.** The Wraith has a **single spawn point** — a grave she must return to
([[death-and-return]]). A protagonist who cannot roam freely suits a puzzle game, where the space is
dense rather than wide — and the break-out is what turns that dense space into the whole map.

## Why It's Fun

Not yet defined. What the design reaches for: a puzzle game whose reward for solving is
**identity**. Every memory found is both a puzzle piece and a step out of the grave, and the
protagonist's own appearance keeps score — and the piece the RTS player wanted turns out to want
something else.

## Tuning

No values yet. The knob to expect is **how much the Wraith is told versus works out** — a memory
handed over is exposition; a memory the player assembles from objects is a puzzle.

## Open

- What the puzzles are — point-and-click, environmental, inventory, something else.
- **When the break-out triggers** — a memory threshold, or a scripted beat once the minigame has
  run its course. It cannot fail; what it waits for is not stated.
- Whether the other recruitment minigames in the RTS share this style, or only this one is a
  wraith's ([[damned-undead-kingdom-rts]]).
- How the mansion relates to the realm: entered from a place in realm-08, or a separate mode.
- What "less ghost-like" changes in play, and whether the break-out is where it peaks.
- Whether the single spawn point still binds her once she is loose on the world map.
- Where in the game's chapters the Damned's story lands ([[chapter-based-release]]).

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[damned-undead-kingdom-rts]] — the game this is a minigame of.
- [[exploration-core-loop]] — the shell; this is its puzzle presentation.
- [[wraiths]] — what the player wakes up as, and the two exits.
- [[pirates-open-exploration]] — the freedom that is her third way out.
- [[the-pirate-institute-war]] — what the memories add up to.
- [[wraith-object-reading]] — the Wraith's verb, and the game's evidence channel.
- [[faction-genre-mechanics]] — the per-faction genre layer this is an instance of.
- [[realm-governs-game-style]] — the decision that makes this style apply to visitors too.

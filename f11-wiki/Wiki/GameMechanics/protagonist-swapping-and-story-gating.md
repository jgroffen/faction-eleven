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
  - Story Gating
  - Protagonist Swapping
state: concept
category: structure
features: []
related_mechanics:
  - faction-genre-mechanics
---

# Protagonist Swapping And Story Gating

The player **swaps between faction protagonists** to progress each story. The ten stories run on
an **overlapping timeline**, and a faction's story can become **blocked** for story reasons while
it waits on an event in another faction's story — which is what pushes the player to go and play
somebody else.

Crucially: **the flow of time between factions is story-driven and does not have to be
consistent.**

**State:** concept · **Category:** structure

**Implemented by:** _(no feature notes yet)_

## How It Works

- The player picks a protagonist and plays their story forward.
- Progress in a story can hit a **story block**: it cannot advance until a specific event happens
  in another faction's story.
- The player clears the block by switching to that other faction and playing to that event.
- Time is **not** conserved across stories. Faction A's afternoon may span Faction B's decade.
  Consistency is not required — story need wins.

That last point is a deliberate licence and worth preserving as written. It means the design does
not owe the player a coherent global clock, only a coherent *causal order* of the events that
gate each other.

Not yet established:

- Whether a block is **legible** — does the player learn *which* faction to go play, or must they
  hunt?
- Whether the ten stories form a **dependency graph** authored up front, and whether it admits
  more than one valid completion order.
- What happens if the player simply refuses to switch.
- Whether swapping is free at any time, or requires reaching a waypoint or camp. (The prototype
  notes say returning to the select screen "is only possible based on how that game works" —
  some factions require waypoints or camping, others allow it any time.)

## Worked Example

The first concrete instance, from chapter one: [[the-first-signal]]. [[autofix]] earns
remote communication with their auto-fix bots in the [[robots]]' story; that signal wakes the
mini-fix bot sitting in [[ninja]]'s family shrine in [[realm-01]]. An event in one faction's story
lands in another's.

Note the shape it suggests for gating in general: the trigger is an **ability the player earned**,
not a cut-scene they watched, and the payoff arrives in a story they were not playing at the time.

**Conditions compose, and they cross chapters.** [[the-second-signal]] fires only when three
things are true: the guarded gate is cracked (Ninja, chapter one), Quantum Comms is unlocked
(Autofix, chapter one) and the Templar has activated his signals (chapter two). So a gate is not
one flag but a **conjunction of flags owned by different protagonists**, potentially set in
different releases. Anything implementing this needs to treat conditions as a set, not a chain.

## Why It's Fun

Not yet defined. What is structurally true: blocking is what converts ten parallel
stories into one story, because it forces the player to experience them as **causally
interleaved** rather than as ten things played in sequence.

## Tuning

No values yet. The knob that matters is **block density** — too few and the stories never braid,
too many and the player is thrown between genres before any one of them clicks.

## Used In

<!-- gd:used-in:start -->
- [[the-calling-of-ancient-allies|The Calling Of Ancient Allies]] · quest
- [[the-convergence-at-the-monastery|The Convergence At The Monastery]] · quest
- [[the-first-signal|The First Signal]] · quest
- [[the-second-signal|The Second Signal]] · quest
<!-- gd:used-in:end -->

## Related

- [[faction-genre-mechanics]] — swapping protagonists also means swapping genre, which makes the
  cost of a swap much higher here than in a normal multi-protagonist game.
- [[faction-reputation]] — reputation bars merge as storylines merge.

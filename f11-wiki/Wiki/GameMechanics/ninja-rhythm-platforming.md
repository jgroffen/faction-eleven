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
  - Institute of Eight Game Style
  - Ninja Game Style
state: concept
category: platforming
features: []
related_mechanics:
  - exploration-core-loop
  - faction-genre-mechanics
---

# Ninja — Rhythm Platforming

The [[institute-of-eight]]'s game style, **replacing** the prototype's rogue-like / Isaac label. It
is a **skill-based platformer in the mould of Super Meat Boy**, with a **rhythm layer**: the music
of each section carries beats that hint at the player's inputs.

**State:** concept · **Category:** platforming

**Implemented by:** _(no feature notes yet)_

## How It Works

**The platformer:**

- **Long, difficult levels**, broken into **short sections between respawn points**.
- Sections are **fast to retry**, with **fast respawns**.
- Progress comes from **pattern learning**, not from resources or randomisation.
- It should be **fast action** throughout.

**The rhythm layer:**

- Each short section has **music whose beats are hints to the player's inputs**, in the manner of
  **Bit.Trip Beat**.
- When the Ninja **jumps or attacks it makes a sound**. Timed well, that sound **lines up with the
  music**.

So the music is not accompaniment; it is the tutorial, playing continuously. The player who reads
the beat is told what to do before they need to do it, and their own actions answer it. Dying and
retrying a short section means hearing the phrase again — which is why fast respawn and rhythm fit
together rather than merely coexisting.

**Training sessions** teach the player about **timing**, and teach **new moves needed to progress**.
They are the faction's structural answer to teaching: not a tooltip, a dojo.

One trained move is load-bearing for the whole game: the Ninja progresses to the boss battle with a
**newly trained skill** — undetermined — and it is that fight which **cracks the guarded gate**
([[the-cracked-gate]]). Deciding which skill is therefore not a local decision; it is the hinge of
chapter one.

## The Rhythm Stays Home

When the Ninja crosses into [[realm-09]] in [[chapter-02]] he plays that realm's genre instead ([[realm-governs-game-style]]), and **the rhythm layer does not travel with
him**. It belongs to the [[institute-of-eight]] — their music, their training, their dojo.

What travels is the *acquisition model*. He still learns by training: in realm-09 he finds a
**challenge room**, [[mifix]] and the Ninja talk, and he **learns the new skill by practising it in
the room**. So the Institute's identity survives the genre swap even though its soundtrack does
not — and the challenge rooms are where this note's hard, section-based platforming lives on inside
a Metroid. See [[gargoyle-stone-metroidvania]].

Not yet established:

- Whether mistimed input is **penalised** or merely unrewarded. (Punishing it makes this a rhythm
  game; leaving it as a hint keeps it a platformer with a rhythmic conscience. Beats are described as
  *hints*, which points to the second.)
- How the music behaves across a retry: restart the phrase, or run continuously?
- Whether the rhythm layer persists into the boss fight or is a level-only device.

## Why It's Fun

Not yet defined. What the design is clearly reaching for: the Super Meat
Boy pleasure of a hard thing becoming easy through repetition, with the music making the repetition
*legible* — you do not just learn the pattern, you hear it.

## Tuning

No values yet. The critical knob is **section length**: short enough that a retry costs nothing,
long enough that a musical phrase completes.

## Tension To Resolve

[[death-and-return]] gives the Ninja a **generational death mechanic** — a cut-scene in which their
child grows up, is trained, and replaces them. That was written for a game where death is rare.
This is a game where **death is constant and respawn is instant**. The two cannot both be literal.
Flagged, not resolved.

## Used In

<!-- gd:used-in:start -->
- [[the-cracking-of-the-gate|The Cracking Of The Gate]] · quest
- [[the-second-signal|The Second Signal]] · quest
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shell it builds on.
- [[faction-genre-mechanics]] — the per-faction genre layer this is an instance of.
- [[robots-incremental-exploration]] — chapter one's other genre; both are skill-gated
  platformers, which is a useful economy of engineering.

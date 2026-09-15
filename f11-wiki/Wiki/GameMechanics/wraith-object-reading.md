---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-09-15
updated: 2026-09-15
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Touch Reading
  - "The Wraith's Touch"
state: concept
category: narrative
features: []
related_mechanics:
  - continuity-glitches
  - wraith-memory-puzzle
---

# Wraith — Object Reading

The [[wraith-delahaye]] can **touch an object and know its history** — and the **deep, emotional
connections** tied to it. It is the verb the [[wraith-memory-puzzle]] runs on, and it is also one of
the channels by which the reality of the four gods reaches the player.

**State:** concept · **Category:** narrative

**Implemented by:** _(no feature notes yet — no code exists)_

## How It Works

**Touch, and know.** An object gives up where it has been and what it meant to the people who held
it. In the memory puzzle this is how the Wraith recovers a life she does not remember: the objects
remember for her.

**Sometimes the object gives up the wrong layer.** The reading can return **under-the-hood game
information — code comments, commit messages** — instead of, or as well as, the object's in-world
history. This is real dev-layer text, the same kind [[the-ancient-language]] decodes to, delivered
raw rather than as a cipher.

**Two visual states tell the player which layer they got:**

| The reading returns | What the Wraith does |
|---|---|
| The object's history and emotional ties | **Head glows.** |
| Source code, comments, commit messages | **Flickers**, and the **eyes flash ASCII symbols.** |

The flicker is the power **glitching**. Read against [[the-setting-statement]], this is
self-correction failing in the bug manifestation: the Wraith's code has reached data no realm's
statement can represent, and the translation half-succeeds. **Inference, not established** — the
source says only that the flicker represents the power glitching.

**The channel is the player's, not the Wraith's.** She is **not self-aware when she glitches** — at
first she does not know anything has happened. Awareness that she is *receiving information* comes
slowly, and what she does with it is what every character does with glitch information: fit it into
game logic, most often as **messages from the gods** ([[the-setting-statement]]). So she can hold a
commit message in her head and never know what it is; no character in any realm can become aware they
are in a game ([[the-revelation-schedule]]). The player is handed dev-layer text and a character
visibly failing to hold it — both are evidence, and neither is an explanation.

## Why It's Fun

Not yet defined. What the design reaches for: the same button gives the player two different kinds
of truth, and the character's body tells them which one they are looking at before they have read a
word. The ASCII in the eyes is the leakage kind of glitch ([[continuity-glitches]]) placed on the
protagonist's own face.

## Tuning

No values yet. The knobs to expect:

- **Rate** — how often a reading returns dev-layer text. Every such reading spends deniability the
  way a strong-tier glitch does, so it is rationed, not free.
- **Which objects** — whether dev-layer readings attach to particular objects (a foreign object, an
  artifact of the four) or fire at random.

## Open

- Whether the ability is the Wraith's alone or something the Damned's undead share.
- Whether it relates to the liches' access to the engine ([[the-lich-experiment]]) — the Wraith is of
  the same faction, and the liches are the only other characters in the world who see the code layer.
- Whether the Wraith can read objects from other realms, and what that returns.
- How fast her awareness that the glitches carry information grows, and what marks each step.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[wraith-memory-puzzle]] — the game style this verb drives.
- [[continuity-glitches]] — the glitch this makes visible on the protagonist.
- [[the-ancient-language]] · [[the-four-developers]] — the other channels to the dev layer.

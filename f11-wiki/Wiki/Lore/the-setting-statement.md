---
tags:
  - lore
topics: []
status: seed
created: 2026-09-12
updated: 2026-09-12
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Game Setting
  - The Game Setting
  - Self-Correction
canon: proposed
era: "the shape of the engine, not an event in it"
characters:
  - tezcatlipoca-the-black
  - autofix
  - mifix
  - odie
factions: []
locations: []
---

# The Setting Statement

**Nobody in the world knows they are in a game.** Not one inhabitant of any realm, and — this is the
part that matters — **not one of the ten player-controlled protagonists either.** Every character's
code is permanently engaged in the same task: explaining whatever it encounters through the reality
of its home realm.

**Canon:** proposed · **Era:** the shape of the engine, not an event in it

## One Engine, Ten Statements

[[tezcatlipoca-the-black]] built one engine, and all ten games run on it ([[the-four-developers]]).
What makes them ten different games rather than one is a single piece of configuration each: a
**Setting Statement**, which declares that game's realm and the rules that hold in it.

The Setting Statement is what a realm *is*, from the engine's side. It is why
[[the-multiverse-of-realms]] is ten worlds with ten moods and ten art styles instead of ten regions
of one place, and it is the layer underneath [[realm-governs-game-style]] — the realm's mechanics
apply to whoever is standing in it because the realm's mechanics **are** the statement the engine is
reading.

Every character is written against exactly one of them. A character has no concept of there being a
second.

## Self-Correction

**A character's code cannot represent content from another game. It can only translate it.**

While the ten worlds were separate this cost nothing: nothing from another statement ever arrived, so
nothing ever needed translating. [[the-linking-of-the-realms]] ended that. A character who crosses
into another realm now meets content authored against a Setting Statement that is not theirs — and
their code does the only thing it is able to do. It **self-corrects** the foreign content into the
terms of its home realm, and presents the result as ordinary reality.

This is not deception and it is not confusion. It is the most fundamental fact about how anyone in
this world perceives anything. A machine that walks into a realm of magic does not see magic; it sees
whatever its own statement has available to mean that. It is completely certain about what it saw.

**It is also why nobody can simply be told.** The revelation that the world is software has no
surface to land on: a character receiving that claim runs it through the same translation as
everything else and gets back something their realm can hold.

## What It Breaks

Two failure modes, and the design lives in both.

**Imbalance.** A character leveraging content and rules from another game is operating outside
anything their own statement was balanced against. The translation gives them something usable; it
does not give anything the numbers to be fair. Every cross-realm capability in the game is a
balancing problem by construction rather than by oversight.

**Glitches.** Where the translation cannot close, the engine fails, and it fails in four distinct
ways ([[continuity-glitches]]):

| Manifestation | What has happened |
|---|---|
| **Hard-retcon** | The correction is forced through at the level of history rather than perception — the world simply is different now |
| **Bug** | The translation half-succeeds and leaves behaviour that belongs to neither statement |
| **Freeze** | The code cannot resolve the correction and stops, still running, going nowhere |
| **Crash** | It cannot resolve it and stops entirely |

These sit alongside the existing kind and tier axes rather than replacing them: the *kind* is what the
player sees, the *tier* is how loudly, and the manifestation is what actually went wrong underneath.
Freezes and crashes are the hardest thing in the design to keep on the right side of the deniability
rule, because they are what a real broken game does.

## The Two Exceptions

Two kinds of entity are **code-aware** — their behaviour is not confined to what their Setting
Statement can express. Both were built that way on purpose, and neither was built for this.

- **The fixbots.** Autofix and mini-fix bots repair by editing code, so they are code-aware
  underneath ([[a-heal-is-a-patch]]). It is what lets them see a retcon land, and it is what kills
  them: code-awareness makes a fixbot progressively unreliable the longer it runs once exposed to
  another realm, ending in a freeze or a crash. The [[robots]]' history no longer records this
  correctly ([[no-machine-repairs-itself]]).
- **The liches.** Backed by autonomous AI agents rather than deterministic code, with enough access to
  read both the engine and their own realm's Setting Statement — and they learned to bypass the
  engine's rules entirely ([[the-lich-experiment]]).

**Neither exception is a way out.** One degrades and dies of what it knows; the other went and hid.

## Ties

- [[the-four-developers]] — whose engine this is, and who wrote the ten statements.
- [[the-multiverse-of-realms]] — ten statements, seen from inside.
- [[realm-governs-game-style]] — the design rule this is the mechanism for.
- [[the-linking-of-the-realms]] — when foreign content first had to be translated.
- [[continuity-glitches]] — what the player finds when the translation fails.
- [[the-retcon-engine]] — the other system editing the world underneath its inhabitants.
- [[a-heal-is-a-patch]] · [[the-lich-experiment]] — the two exceptions.

## Player-Facing

**Never stated, and load-bearing on every screen.** The player is the only party in the arrangement
holding more than one Setting Statement at a time, which is what makes them able to notice anything at
all ([[protagonist-swapping-and-story-gating]]). Ten protagonists who each explain the multiverse
entirely in their own realm's terms, and one player accumulating all ten explanations, is the whole
detective structure.

The rule to protect: **a protagonist never gets closer to the truth than their statement allows.**
Characters can be puzzled, can be wrong, and can notice — but the moment one of them reasons their way
to *this is a game*, the game has no mystery left. That is why the characters who genuinely know
([[the-lich-experiment]]) present it as eldritch lore, and why the ones who can see it
([[autofix]], [[mifix]], [[odie]]) cannot interpret what they see.

## Open

- Whether the term is ever encountered in-world — as a phrase in [[the-ancient-language]], or from
  the liches, who can read one.
- Whether self-correction is ever shown *happening* to the player — the same object rendered two ways
  in two realms is the most direct demonstration available, and also the loudest.
- How imbalance is handled mechanically when a protagonist carries a capability across, which
  [[realm-governs-game-style]] leaves unresolved.

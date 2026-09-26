---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-09-26
updated: 2026-09-26
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Mystics Game Style
  - "The Conjurer's Game"
state: concept
category: progression
features: []
related_mechanics:
  - exploration-core-loop
  - faction-genre-mechanics
  - autofix-skill-tree
---

# Mystics — Isometric Action RPG

The [[mystics]]' game style: an **isometric action RPG** in **simple 2D** — Vampire Survivors rather
than Diablo 3, no 3D engine. The player takes [[conjurer-voisin]] out of a village, down into caves,
kills monsters for **Reagents**, and spends those Reagents on everything they will ever own.

**State:** concept · **Category:** progression

**Implemented by:** _(no feature notes yet — no code exists)_

## Three Stats

| Stat | What it is |
|------|-----------|
| **Health** | ordinary. Running out means death, which the homunculi undo ([[death-and-return]]). |
| **Magic** | a **regenerating** pool. **Every action costs some.** This is the floor: the player is never unable to act. |
| **Reagents** | **consumed and never regenerated.** Currency, crafting material and the cost of magic, all in one number. |

**Every action spends Magic. Magical actions also spend a small amount of Reagents.** There are
basic actions — and possibly others — that cost no Reagents at all, which is what keeps a broke player
playing.

### The Basic Kit

- **Four simple wand attacks**, each a **different damage type**.
- **A simple heal spell.**
- **A dash spell.**
- **A summon homunculi spell.**

Four damage types from the first minute makes the Conjurer a *matching* character rather than a
damage-per-second one: the interesting decision in an ordinary fight is which attack, not whether to
attack.

## Reagents Are The Whole Economy

One currency, two things to spend it on:

- **Casting** — a small trickle per magical action.
- **Gear and skills** — both **considerably expensive**, and gear is **impactful** rather than
  incremental. Gear is a decision, not a drip.

**Monsters drop Reagents and nothing else.** There are no gear drops anywhere in the game. So the loot
loop is not "kill things until something good falls out" — it is "kill things to afford the good thing
you already know you want."

**All gear is crafted, and never by the player.** Every piece of Mystic gear was made by a Mystic out
of Reagents; **vendors and NPCs** do the crafting, which is why gear costs what it does — the price is
the Reagents that went into it. There is no crafting screen and no recipe list.

**Unique gear is the same craft by better hands.** The powerful artefacts in the world were made the
same way, by **high-level and often historically significant Mystics**, and are **held by powerful
NPCs or rumoured to be somewhere in the world**. They are not for sale, which makes them the only gear
the player has to go and *get* rather than afford.

## The End-Boss Is Optional

A Mystic's own story is to level up until strong enough to beat the realm's **end-boss** — which is
[[conjurer-voisin]]'s destiny until the wand goes off, and which is **not required to complete Faction
Eleven**. No realm's own game has to be finished; the main story runs through the alliance
([[the-stabilisation-of-the-realms]]). What the end-boss actually is has not been decided.

## The Pull Is The Price Curve

**Costs for skills and gear scale rapidly.** That scaling is the only thing pushing the player
deeper: the next skill or the next weapon costs enough that the caves they can already clear cannot
pay for it. Progression is therefore a straight economic ladder — earn, price out, go somewhere
harder.

This is the design's load-bearing tuning relationship and it is the one most likely to break. Too
steep and the game is a grind with a shop attached; too shallow and there is no reason to leave the
first cave.

## The Skill Tree

**Borrowed in shape from [[autofix-skill-tree]]**, not in economy: branches that each buy a *kind* of
play rather than a stat line.

**One root, three branches — and only the third differs.** Every Mystic shares the **root** and the
**first two branches**. The **third branch is unique to the faction class**: the six
[[the-six-classes|Mystic classes]] are Oracle, Summoner, Battle Mage, Illusionist, Witch Doctor and
Conjurer, and [[conjurer-voisin]] can only ever take the Conjurer's.

| Branch | What it holds |
|---|---|
| **Spells** | common attacks and abilities |
| **Body** | magic pool, health pool, basic healing, damage resistances, movement speed — and more to be added |
| **Class** | the faction class's own, and the only one that differs between Mystics |

**Contents beyond that are deliberately unspecified** until the Mystics' gameplay is closer to
implementation.

So two thirds of any Mystic's progression is shared and the last third is who they are — which is what
makes the character-creation screen's refusal to let the player be anything but a Conjurer a
*mechanical* loss and not only a narrative one ([[the-ordinary-day-of-the-conjurer]]).

- **Skills have a level requirement** — levelling gates what is *available*.
- **Skills are bought with Reagents** — there is no skill-point currency. The same pool that pays for
  gear and casting pays for progression.

**It has no `ACCESS DENIED`.** That is the [[robots]]' device and belongs to their realm only
([[autofix-skill-tree]]).

## The Homunculi Are Three Mechanics

She lives with many of them, and every one of their uses is taught in the first hour:

- **Death:** the standby pool below.
- **Fast travel:** she de-constitutes into a homunculus, which carries her back to town. **Within
  [[realm-04]] only** — a homunculus cannot cross an interplane gate, so leaving the realm needs a gate
  like anyone else.
- **Dialogue:** [[the-ancient-relic]] speaks to her *through* them — an object with no mouth borrowing
  several ([[the-ordinary-day-of-the-conjurer]]).

### The Standby Pool Is The Death Mechanic

She keeps homunculi **on standby**. The pool starts at **one** and the summon-homunculi skills raise the
cap toward **six**.

- **On death, a standby homunculus comes and restores her where she fell.** No walk home, no lost
  progress — one homunculus spent.
- **On the last one**, that homunculus instead **collects her gear and returns to the cottage**, and she
  is reconstituted there.
- **Once reconstituted, the standby pool replenishes automatically.**

So the pool is *how many times she can die without losing the run*, and running it out costs her the
trip rather than the game. It is also the only death mechanic in the ten factions that the player can
**buy more of** ([[death-and-return]]).

Because the pool does not refill in the field, it is what makes [[celestial-tower]] a real cost: every
homunculus caught in there is one fewer standing between her and the walk home.

**And in one place they are the whole game.** Sneaking through [[celestial-tower]], the player **plays
the homunculi** rather than Voisin: send one ahead, and if it is caught it is **destroyed** and another
can be sent. A stealth section with no stealth system — the tension is attrition of a resource the
player has plenty of and can visibly run down, and the verbs are ones they already own.

## Why It's Fun

Not yet defined. What the structure reaches for: a single scarce number that every decision competes
for. Casting costs the same thing as shopping, so a fight won cheaply is a fight that paid for
itself, and the player is doing arithmetic about magic the whole time they are casting it.

## Presentation

**Isometric, 2D, simple.** A third presentation alongside the shell's platforming and top-down
([[exploration-core-loop]], [[the-shell-carries-more-than-two-presentations]]).

## Abroad

Voisin keeps her level and her progression when she travels, and everything she earns abroad comes home
with her — but **her gameplay becomes the host realm's** and **Reagent harvesting does not work outside
[[realm-04]]** ([[cross-realm-power-and-progression]]). That last rule is why
[[the-graceful-servants]] have to bring werebeasts home to harvest them.

## Tuning

No values yet. The numbers that matter:

- **Reagent yield per monster** against **skill and gear price scaling** — the ladder.
- **Reagent cost per cast** — small enough to ignore in the moment, large enough to notice over a
  cave.
- **Magic regeneration** — the floor that stops a broke player being stuck.

## The Exploit Inside It

Reagent yield scales with how **magical** a creature is, which makes the whole economy gameable by
anyone who can reach a realm full of magical creatures. That is not a bug in this note; it is
[[the-harvesting-of-the-werebeasts]], and it is the Mystics' story.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Open

- What the tree's branches are besides the six class branches — whether there is a shared trunk and
  what is on it.
- What "basic actions" are, and whether a Conjurer has a meaningful Reagent-free kit or only a
  fallback.
- **What is on the two shared branches**, and what the Conjurer's own branch does.
- Whether the basic **summon homunculi** spell and the tree's summon-homunculi skills are the same
  thing — one raises the standby cap, and what the in-field spell does alongside automatic
  replenishment is not settled.
- Which of the basic kit costs Reagents and which is Magic-only.
- **What the underground is made of.** Caves, caverns and dungeons are all in the material, and ruins
  or castles may join them; no progression structure among them is settled.
- Whether the realm has dungeons distinct from caves — the faction's older material says towers,
  castles, cottages, dungeons and an underworld, and only the caves are designed.

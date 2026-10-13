---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-10-13
updated: 2026-10-13
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Fey Folk Game Style
  - "The Phoenix's Game"
  - Ley Cleansing
state: concept
category: progression
features: []
related_mechanics:
  - mystics-isometric-action-rpg
  - werebeast-pack-hunt
  - faction-genre-mechanics
---

# Fey Folk — Ley Cleansing

The [[fey-folk]]' game style: **cleansing corruption, not fighting.** The player is a **Fey Beast**,
a powerful mythical guardian of the Fey Folk, whose **mere presence** cleanses the world of the Fell
Folk and their corrupting influence, **Fell Power** ([[the-fey-and-the-fell]]). You don't fight so much
as run around isometric maps clearing corruption.

**State:** concept · **Category:** progression

**Implemented by:** _(no feature notes yet — no code exists)_

**It is built on the Mystics' game.** Isometric view and movement come from
[[mystics-isometric-action-rpg]], the same base [[werebeast-pack-hunt]] uses — three realms on one
engine. It runs in **real time**, and **there is no combat mechanic.**

## Structure

| Unit | What it is |
|------|-----------|
| **Zone** | six of them, each with a different Fell Folk leader — a **Fell Beast** |
| **Map** | several per zone; each has a **Ley Knot** to free |
| **Fell Beast Lair** | the zone's final map, unlocked once every other map is cleared and the zone's Ley Knots are Fey Rings |

## How A Map Is Won

1. **Run to where the Fell Folk are spreading corruption.** Your presence chases them off.
2. **Chasing them off draws the Fey Folk**, who follow and spread **Fey Power**, pushing back the Fell
   Power.
3. **Ley Lines cross at Ley Knots.** Every Knot starts corrupted as a **Hag Ring**.
4. **Clear the Hag Ring and occupy it** to free the Ley Knot. The Fey Folk come and fortify it into a
   **Fey Ring**, which wins the map.

**The Ley Lines are the paths the Fey Beast follows** to progress through a map.

## Health And Magic

| Meter | Goes down | Comes back |
|-------|-----------|-----------|
| **Health** | Fell Folk attacks | slowly, standing near Fey Folk |
| **Magic** | spent clearing corruption | on uncorrupted Ley Lines |

**The game is that balance:** spend Magic pushing into corruption while the Fell Folk wear Health
down, then go back to the area you control to recover.

## The Lair

Every Ley Line in the zone leads to the lair, **built on top of a Prime Knot** that the Fell Beast has
corrupted. To beat it the player co-ordinates the whole zone:

- **Keep the Ley Lines clear and flowing with Fey Power.** That flow burns away the corruption and
  destroys the Fell Beast's defences, while the Fell Beast and his Fell Folk minions defend.
- **Clear the corruption from the Prime Knot**, feed it with Magic, and **stand on it** once the Ley
  Lines have fully powered it. That destroys the Fell Beast.

## Losing

Neither way is permanent.

- **Pushed back:** if corruption spreads along the Ley Line all the way back to the map's start, the
  Fey Beast is pushed back and starts the map again.
- **Out of health:** the Fey Beast "dies" and restarts from the character-selection screen, and **can
  still pick the same Fey Beast** ([[death-and-return]]).

## Character Selection

**Any Fey Beast, any time.** The six are the faction's six classes ([[the-six-classes]]). Play is much
the same with each, but each has different **base stats** — movement speed, max Health and Magic, and
Health and Magic regeneration — and **one passive and one active skill.**

| Fey Beast | Class | Active | Passive |
|-----------|-------|--------|---------|
| Stag Lord | Commander | — | — |
| Ent | Front Liner | — | — |
| **[[phoenix-ember\|Phoenix]]** | Heavy Weapons | **Cleansing Fire** | **Rebirth** |
| Moon Hound | Infiltrator | — | — |
| Unicorn | Medic | — | — |
| Hippogriff | Specialist | — | — |

**Any Fey Beast can clear any zone.** The six Fell Beasts mirror the six Fey Beasts only in theme.

**The Phoenix is the exception that matters.** Cleansing Fire can fight back, and Rebirth survives a
death. The story turns on both ([[the-beheading-of-the-fey-beasts]]).

## Why It's Fun

It's deliberately simple: a push-and-recover rhythm over a map you slowly turn from corrupted to
fortified, with the Fey Folk as a tide you lead rather than units you command. That simplicity is
also the setup. A game with no combat is defenceless against something that came to fight.

## Abroad

**[[realm-05]] is mostly a place to pass through between realms and a stage for story events.**
Visiting champions aren't played through the cleansing loop as Fey Beasts. **Werebeasts there have to
cope with real-time combat**: the pause in their own game ([[werebeast-pack-hunt]]) stays at home
([[realm-governs-game-style]]).

## When It Can Be Played

**Zones 1 and 2 open in [[chapter-06]].** Clearing zone 2 ends with the Fey Folk reporting that zone
3's Fell Beast has **gone quiet**. That is the first hint, and the gate. **Zone 3 onward opens in
[[chapter-08]]**, so the empty lair and the ambush are always played there.

## Tuning

No values yet.

## Used In

- [[fey-folk]] · [[phoenix-ember]] — the faction and its protagonist.
- [[the-beheading-of-the-fey-beasts]] — the story the game is built to carry.
- [[chapter-08]].

## Open

- The other five Fey Beasts' skills and every base stat. Left for a later session.
- What Crystals buy ([[faction-currencies]]).
- How zone 3's dead Fell Beast and the Fey Folk's confusion are presented in play.


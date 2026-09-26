---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-09-27
updated: 2026-09-27
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Travelling Protagonists
  - Power Level Abroad
state: concept
category: structure
features: []
related_mechanics:
  - faction-genre-mechanics
  - exploration-core-loop
  - protagonist-swapping-and-story-gating
---

# Cross-Realm Power And Progression

What happens to a protagonist's numbers when they leave home. **A genre belongs to a realm, not to a
protagonist** ([[realm-governs-game-style]]) — so a traveller plays the host realm's game, and this is
the rule for what they bring with them.

**State:** concept · **Category:** structure

**Implemented by:** _(no feature notes yet — no code exists)_

## The Rule

**Four parts, and they apply to every protagonist, not only the [[mystics]]:**

1. **Gameplay changes to suit the realm.** The verbs are the host realm's.
2. **Power level abroad roughly matches level at home.** A traveller is about as strong, relative to
   the host realm's content, as they were in their own.
3. **Progression abroad translates back.** Levels and advancement earned in a foreign realm are not
   lost when the protagonist goes home.
4. **Realm-bound abilities do not travel.** A capability that depends on the home realm's rules stops
   working outside it.

## The Worked Case

**[[conjurer-voisin]] cannot harvest outside [[realm-04]].** Reagent yield is a Mystic-realm rule, so
the moment she leaves, magical creatures stop paying out — and **that is why
[[the-graceful-servants]] bring werebeasts home instead of harvesting them in [[realm-09]]**
([[the-harvesting-of-the-werebeasts]]). A game rule, applied consistently, produced the shape of an
atrocity: the incursions have to be **captures**, and there have to be **wagons**
([[the-werebeast-caverns]]).

Her **homunculus fast travel** is the same case — it works inside realm-04 and cannot cross an
interplane gate.

## Why It's Fun

Not yet defined. What it protects: a player who has invested twenty hours in one protagonist does not
get handed a weakling in the next realm, and time spent abroad is not time stolen from the story they
care about. Without part 3 especially, every cross-realm chapter would be a tax.

## Tuning

No values yet. Part 2 is the hard one — "roughly matches" has to be computed between two genres whose
power curves have nothing in common, and there are ten of them.

## Scope Risk

**Acknowledged as a development challenge.** Ten genres times nine foreign realms is a mapping problem
with no obvious general solution, and it sits underneath [[faction-genre-mechanics]], which is already
the project's largest scope commitment ([[project-scope-and-constraints]]).

## Fiction

The fiction already explains it. A character's code can only represent what its own
[[the-setting-statement|Setting Statement]] allows, so a traveller **self-corrects** the foreign realm
into home terms rather than perceiving it — which is exactly why the verbs change, why some abilities
stop, and why carrying a capability across is a balancing problem by construction
([[continuity-glitches]]).

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Open

- How part 2 is actually computed, per realm pair.
- Whether gear travels, and what a Mystic does for equipment in a realm with no Mystic vendors.
- Whether currencies convert, or each realm's currency is simply inert elsewhere.
- Which other realm-bound abilities exist, now that harvesting has established the category.

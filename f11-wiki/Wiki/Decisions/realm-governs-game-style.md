---
tags:
  - decision
topics: []
status: seed
created: 2026-08-14
updated: 2026-08-14
sources: []
source_count: 0
aliases:
  - Realm Mechanics Apply To Visitors
decision_status: accepted
decided: 2026-08-14
components: []
feature: ""
supersedes: ""
superseded_by: ""
---

# Realm Governs Game Style

**A faction's game style belongs to its realm, not to its protagonist.** Whoever is playing, the
mechanics of the realm they are standing in apply.

**Status:** accepted · **Decided:** 2026-08-14

**Based on:** [[faction-genre-mechanics]] · [[exploration-core-loop]] ·
[[gargoyle-stone-metroidvania]]

## Context

[[faction-genre-mechanics]] gives each of the ten factions its own genre on top of the shared
[[exploration-core-loop]]. That was written while each protagonist was still at home. From
[[chapter-02]] the protagonists start **travelling**, and the question the design had never answered
became urgent: when the [[ninja]] walks into [[realm-09]], does he bring
[[ninja-rhythm-platforming]] with him, or does he play the Green Skins' game?

The trigger was the Gargoyle's style being settled as a Metroid. The author's answer also disposed
of a competing proposal — squad/party mechanics for the Gargoyle — on the grounds that it does not
suit the realm.

## Options Considered

- **Style follows the character.** Each protagonist carries their own genre everywhere. Preserves
  each faction's identity, but means every realm must be built to support every genre that might
  walk into it, and a shared scene would need two genres running at once.
- **Style follows the realm.** *(Chosen.)* The realm's mechanics apply to whoever is in it.
- **Style follows the story beat.** Chosen per scene by authorial preference. Maximum flexibility,
  no rule — and therefore no way to plan content.

## Decision

**The realm's mechanics apply when gameplay is in that realm.** Concretely:

- The [[ninja]] **swaps to the Metroid style in [[realm-09]]** — ability-gated progression, and no
  rhythm layer, which stays home in [[realm-01]].
- In [[chapter-03]], [[ninja]] and [[gargoyle]] move on to the Celestials' realm and **both swap to
  [[celestials-hero-tower-defence]]** — top-down tower defence with hero units.

Each protagonist keeps their **own way of acquiring** power inside the host genre, which is how
character survives the swap: in realm-09 the Gargoyle finds **lore fragments** while the Ninja finds
**challenge rooms** and trains with [[mifix]].

## Consequences

**Good:**

- **Genres become reusable content, not one-shot systems.** The largest scope risk in the project
  ([[faction-genre-mechanics]]: ten genres, one developer) is that each genre is built once and
  played once. This rule makes every genre earn its build cost repeatedly — realm-09's Metroid map
  is played by two protagonists, and the Celestials' tower defence is replayed with new heroes.
- It gives a mechanical shape to convergence. Meeting another faction is not just a story event; it
  **changes what game you are playing**, which is the premise made playable.
- The prototype's "later allies become hero units" idea now has a general rule behind it.

**Costs:**

- **Every protagonist needs a kit in every genre they visit.** The Ninja needs a Metroid ability
  ladder *and*, in chapter three, a role on a tower-defence field. That is new design work per
  visitor per realm, and it grows as the stories converge.
- Characters risk **flattening into skins** if the host genre dominates. The
  acquisition-model rule above is the counterweight, and it will need watching.
- **Progression does not obviously travel.** What happens to the Ninja's realm-09 abilities when he
  reaches [[realm-03]] — carried, converted, or dropped — is **unresolved**.

## Notes

Party/squad mechanics were considered for the [[gargoyle]] and **rejected as unsuited to the
realm**, not as a bad idea: the author has reserved them for a different faction. Do not re-propose
them for the Green Skins.

---
tags:
  - decision
topics: []
status: seed
created: 2026-09-26
updated: 2026-09-26
sources: []
source_count: 0
aliases: []
decision_status: accepted
decided: 2026-09-26
components: []
feature: ""
supersedes: ""
superseded_by: ""
---

# The Shell Carries More Than Two Presentations

A faction's game style decides its presentation; the shell supplies however many presentations the
ten styles need, kept to the minimum and reused wherever possible.

**Status:** accepted · **Decided:** 2026-09-26

**Based on:** [[exploration-core-loop]] · [[project-scope-and-constraints]]

## Context

The shared exploration shell was described as offering exactly two presentations, platforming and
top-down, with every faction picking one. The [[mystics]]' style is an isometric action RPG, which is
neither.

## Options Considered

Force isometric into top-down and leave the count at two. Let the count grow with what the styles
actually need. Build one fully general renderer covering every case up front.

## Decision

**Let the count grow.** Engine reuse is the goal, not a constraint that overrides a faction's game
style; the number of presentations is held to the minimum needed and shared across factions wherever
it can be. The Mystics' isometric view is **simple 2D** — Vampire Survivors, not Diablo 3.

## Consequences

Each presentation is real build, so the shell is a smaller scope defence than a fixed count would be;
what keeps it affordable is reuse across factions. Staying in 2D caps the cost, and no faction's style
so far needs 3D — worth testing deliberately against each remaining style.

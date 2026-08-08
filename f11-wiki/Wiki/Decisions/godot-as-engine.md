---
tags:
  - "decision"
topics: []
status: seed
created: 2026-08-08
updated: 2026-08-08
sources:
  - "Raw/Sources/interviews/faction-eleven-lore-and-design.md"
source_count: 1
aliases: []
decision_status: accepted
decided: "2026-08-08"
components: []
feature: ""
supersedes: ""
superseded_by: ""
---

# Build Faction Eleven In Godot

Faction Eleven will be built in **Godot**.

**Status:** accepted · **Decided:** 2026-08-08 (recorded; the author reports the choice was
already settled before this interview)

**Based on:** [[project-scope-and-constraints]]

## Context

Faction Eleven is a solo hobby project with commercial intent and no existing code
([[project-scope-and-constraints]]). The engine has to carry a 2D open world with both platforming
and top-down presentation ([[exploration-core-loop]]) and ten distinct genre systems
([[faction-genre-mechanics]]) — an unusually wide spread of mechanical requirements for one
codebase.

## Options Considered

Not recorded. The author stated the choice as already made — "tech decided as godot based" — and
the alternatives weighed, if any, were not captured in this interview. Worth backfilling if the
decision is ever revisited.

## Decision

Godot.

## Consequences

Not yet stated by the author. What Godot makes easy and hard for this specific game — the 2D
toolchain, the platform/top-down split, ten heterogeneous systems in one project, and the
commercial shipping path — has not been recorded and should be filled in before the first
architecture decisions depend on it.

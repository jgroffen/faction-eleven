---
tags:
  - "topic"
topics: []
status: seed
created: 2026-08-08
updated: 2026-08-08
sources:
  - "Raw/Sources/interviews/faction-eleven-lore-and-design.md"
source_count: 1
aliases: []
---

# Project Scope And Constraints

Faction Eleven is a **solo hobby computer game development project** with a **shippable
commercial game** as its goal. The engine is decided — Godot, see [[godot-as-engine]]. As of
2026-08-08 there is **no prior code**; the material that exists is lore held in the author's head,
which this wiki exists to capture.

## Overview

The constraints that shape every other decision in the wiki:

- **One developer.** Every system built is built once, by one person, with no parallelism.
- **Commercial intent.** This is not a design exercise — scope decisions have to survive contact
  with actually shipping. Trade-offs belong in `Wiki/Decisions/`.
- **Godot.** See [[godot-as-engine]].
- **Design-ahead-of-code.** The design exists in far more detail than the implementation, which
  is empty. The wiki currently leads the codebase rather than describing it.

The standing tension: [[faction-genre-mechanics]] commits a solo developer to ten distinct genre
systems. That is the project's defining scope risk and is unresolved as of this note.

## Concepts

- [[faction-genre-mechanics]] — the design commitment that carries the scope risk.

## Entities

- [[godot-as-engine]] — the engine decision.

## Sources

- `Raw/Sources/interviews/faction-eleven-lore-and-design.md`

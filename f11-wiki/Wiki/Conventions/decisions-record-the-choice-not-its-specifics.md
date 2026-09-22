---
tags:
  - convention
topics: []
status: seed
created: 2026-09-22
updated: 2026-09-22
sources: []
source_count: 0
aliases: []
scope: repo-wide
enforcement: review
---

# Decisions record the choice, not its specifics

Write a decision note as the choice and its reasoning; link to the notes that hold the details.

**Scope:** repo-wide · **Enforced by:** review

## Rule

A decision note states the choice made, its context, the options weighed and the consequences. Implementation specifics that could change — which quests sit in which chapter, faction rosters, numbers, names — live in the notes that own them (chapter, quest, mechanic) and are linked, not restated. An example may appear only when labelled as an example.

## Rationale

A decision's worth is recording what was chosen and why; specifics drift with every rewrite and turn the record stale or, worse, authoritative by accident.

## Examples

- ✅ [[spread-the-chapters-so-parallel-stories-converge]] — says chapters are spread and why;
  which quests landed where is in [[chapter-02]], [[chapter-03]] and [[chapter-04]].
- ✅ [[chapter-based-release]] — release in chapters, several arcs per chapter, eight to ten;
  chapter composition pointed at the chapter notes.
- ❌ A decision note listing each chapter's lead faction, quests and status — stale the first time a
  boundary moves, and a second copy of what the chapter notes already say.

## Exceptions

A worked example is fine when the heading says it is one. Superseded decisions keep whatever they
said — the rule applies to writing new ones, not rewriting old ones.

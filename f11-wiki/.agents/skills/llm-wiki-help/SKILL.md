---
name: llm-wiki-help
description: Ask which wiki skill fits your situation. A router over this vault's skills.
disable-model-invocation: true
---

# LLM Wiki: Help

You do not remember every skill this vault has, so ask.

## First, see what is actually installed

```bash
python3 scripts/wiki_tool.py plugins    # note types, and which plugin added them
python3 scripts/wiki_tool.py skills     # every skill in this vault
```

Plugins bring their own skills, so the list below is the **core** set — describe what the vault
really has, not this file.

## The core flows

Everything the core does is one question: **where is the knowledge right now, and where does it
need to go?**

| Where it is | Skill |
|---|---|
| In a document — a clipping, a page, a transcript | **llm-wiki-ingest** — drop it in `Raw/Sources/`, compile it into linked notes |
| In the user's head | **grill-into-wiki** — interview it out, transcript as the source |
| In someone else's head | **llm-wiki-questionnaire** — a document they fill in, answers as the source |
| Nobody has it yet | **llm-wiki-research** — background agent, primary sources, cited |
| Already in the wiki, and someone is asking | **llm-wiki-query** — catalog first, Raw only if needed |

And the upkeep:

| Situation | Skill |
|---|---|
| A term is fuzzy, overloaded, or duplicated across two notes | **llm-wiki-glossary** |
| An answer went over the user's head | **llm-wiki-plainly** — re-pitch it in the wiki's own words |
| `lint` / `source-lint` is failing | **llm-wiki-lint** |
| About to commit | **llm-wiki-maintain** — the full gate |
| Running out of context, or forking to another session | **llm-wiki-handover** |
| Picking a session back up | **llm-wiki-handover** (resume branch) — or `handover list` |
| Learning the vault's subject over weeks | **llm-wiki-teach** |

**llm-wiki-grilling** sits underneath rather than beside: it is the interview loop
`grill-into-wiki` and `llm-wiki-teach` both drive — rounds of questions, the wiki's own facts
looked up rather than asked. Reach for it directly when you want the grilling without anything
being written down.

## Two things worth knowing

**Grill before you build.** The most expensive failure is a wiki full of notes that record the
wrong thing precisely. `grill-into-wiki` is cheap; re-cutting fifty notes is not.

**A handover is one of five moves at a phase boundary**, and often the wrong one — continue,
`/clear`, handover, subagent, `/compact`, in that order. The tree, and the step that comes before
it (land the knowledge as notes first), are in
`.agents/skills/llm-wiki-handover/PHASE-BOUNDARIES.md`.

## Answering

Ask what the user is trying to do, if it is not already clear, then name **one** skill and say
why. A list of five is the problem this skill exists to solve.

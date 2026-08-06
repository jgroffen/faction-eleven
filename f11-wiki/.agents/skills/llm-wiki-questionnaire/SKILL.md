---
name: llm-wiki-questionnaire
description: Write a questionnaire for someone else to fill in, landing their answers in the wiki as a source.
disable-model-invocation: true
---

# LLM Wiki: Questionnaire

The inverse of `grill-into-wiki`. There, the knowledge is in the user's head and an interview gets
it out. Here it is in **somebody else's** — a colleague, a domain expert, a supplier — and the
user cannot answer for them.

The output is a questionnaire the user sends. What comes back is evidence, so it goes where all
evidence goes: `Raw/Sources/interviews/`, cited, compiled into notes like any other source.

## Grill the send, not the subject

Interview the user only about the **send**, which they can always answer. The subject is precisely
what they do not know — that is why the questionnaire exists.

Two exchanges, then write:

1. **Who is it going to?** The recipient's role, expertise, and relationship to the user. This
   fixes the tone and how much context the document must carry. Done when you know what this
   person knows that the user does not.

2. **What do you need back?** The specific decisions or facts the user cannot resolve alone. Done
   when you have a concrete list of what they must walk away able to decide.

Aim every question at the gap between those two answers.

## Where it lives

Write it straight into the wiki as an unprocessed source:
`Raw/Sources/interviews/<topic-slug>-questionnaire.md`, from `_templates/source-note.md`:

```yaml
Title: "Questionnaire: export retention policy"
Reference: "Questionnaire sent to the platform lead, 2026-08-06 — awaiting reply"
ContentType: ["questionnaire"]
Created: 2026-08-06
Processed: false
tags: ["source"]
```

`Processed: false` is doing real work here. `source-lint` demands coverage only of sources marked
processed, so an unanswered questionnaire passes the gate while `source-scan` lists it as
`uncovered` — which is exactly the status it has: sent, waiting.

Run `source-scan --update --accept-covered` so the manifest records it, then hand the user the
path.

## When the answers come back

Paste each answer under its question, in the recipient's own words. Then:

- Update `Reference` to the completed citation — `"Questionnaire completed by the platform lead,
  2026-08-14"`.
- Compile it into notes with **llm-wiki-ingest**, citing this file.
- Set `Processed: true` once at least one note covers it, and run the gate.

An answer that contradicts an existing note is the valuable one — resolve it the way
**llm-wiki-grilling** describes: the world changed, or the note was wrong.

## Document structure

Frame it as a **discovery questionnaire**: the user lacks context, the recipient holds it. Order
questions most-important-first — async means you may get only one pass — and group them under
`###` headings by theme once there are more than a handful.

```markdown
## Content

**Purpose:** why this questionnaire exists and the decision riding on it.

**From:** <the user> — **To:** <the recipient> — **How your answers will be used:** compiled into
our internal wiki, cited to you.

### Context

One paragraph orienting a recipient who was not in the user's head. Enough to answer well.

### How to answer

Deadline and rough effort. Partial answers and "I don't know" are useful — flag anything you are
unsure of rather than skipping it.

### <Theme heading>

#### What retention does the export bucket have today?

_Why this matters: it decides whether we archive before deleting._

>

### Anything else?

Anything we did not ask that we should know?
```

Every question is **one idea** — never compound — with an empty `>` answer stub directly beneath.
Add the `_Why this matters_` line only where a question could be misread or invite a throwaway
answer.

## Done when

The file exists, every item from step 2 is covered by a question, `source-lint` passes, and the
user has the path to send.

---
name: llm-wiki-teach
description: Teach the user a topic over multiple sessions, from what the wiki already knows.
disable-model-invocation: true
---

# LLM Wiki: Teach

Teach the user a topic over multiple sessions, grounded in the wiki's own notes.

This is **stateful**: the wiki holds the material, and `learning` notes hold what the user knows.
A teaching workspace elsewhere has to build both from nothing. Here the material already exists —
so most of the work is choosing what to teach next, not authoring it.

## What lives where

| | |
|---|---|
| **The material** | The wiki's compiled notes. They are already the compressed essence — do not re-author them as lesson handouts. |
| **The evidence** | `Raw/Sources/`, already tracked and linted. This is the reading list. |
| **The mission** | One `learning` note, `kind: mission` — *why* the user wants this. |
| **What they know** | `learning` notes, `kind: record` — one per non-obvious thing established. |
| **How they like to learn** | One `learning` note, `kind: preferences`. |

Lessons themselves are **not saved**. They happen in conversation, from the notes. A lesson worth
keeping is a sign the wiki is missing a note — write the note.

## Steps

1. **Find the mission.** `search-catalog --query "mission <topic>"`, or list `Wiki/Learning/`.
   If there is none, **that is the first session**: run **llm-wiki-grilling** to find out why
   they want this and what it is for — usually a round or two is enough. Without it, lessons
   drift into the abstract and you have no basis for choosing what comes next. Write it as a
   `learning` note, `kind: mission`, from `_templates/learning-note.md`.

2. **Read the learning records.** They are the floor: what is known, what was corrected, what
   they said they already knew.

3. **Pick the next thing** — the most mission-relevant thing just beyond what the records show
   they know. Challenged *just enough*: too easy and nothing sticks, too hard and working memory
   goes to keeping up instead of understanding.

4. **Check the wiki covers it:**
   ```bash
   python3 scripts/wiki_tool.py search-catalog --query "the concept"
   ```
   **A gap stops the lesson.** Fill it first — **llm-wiki-research**
   for facts nobody has, **grill-into-wiki** when the user turns out to know it after all. Then
   teach from the note. This is the whole reason to teach from a wiki: the lesson is as
   trustworthy as the notes behind it, and both improve together.

5. **Teach it small.** One tangible win per lesson, from the note, with its `sources` offered as
   the primary reading. Cite the notes as you go — `[[links]]` the user can open afterwards.

6. **Make them retrieve it.** Explaining is not learning; recall is. Ask them to state it back,
   apply it to a case you invent, or predict what happens in a scenario the note covers. If the
   `llm-quiz` plugin is installed, hand assessment to **llm-quiz-take** — its questions are
   already grounded in these notes. Otherwise ask directly.

7. **Write a learning record when something is established** — and only then. From
   `_templates/learning-note.md`, `kind: record`, one to three sentences, linked to the notes it
   covers. Then:
   ```bash
   python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint
   ```

## Fluency is not retention

Following along in the moment feels like mastery and is not. Retention is built by **effortful
recall**: make them retrieve rather than re-read, revisit earlier material in later sessions, and
mix related topics rather than drilling one to exhaustion. For *acquiring* knowledge difficulty
is the enemy; for *retaining* it, difficulty is the tool.

## Guardrails

- **Write a record for evidence.** Wait until they demonstrate it — material you presented is not
  material they learned, and records written for coverage inflate until every later lesson is
  pitched too high.
- **Supersede.** When an understanding turns out to be wrong, keep the old record with
  `status: superseded`, link the new one, and say what changed. Corrected misconceptions are the
  highest-value records — they predict where the user will stumble next.
- **Teach from the note in front of you.** If it is in neither the wiki nor a source, step 4
  applies: fill the gap first.
- Missions change as people learn. Confirm with the user, update the mission note, and record the
  shift.
- One record per established insight, or none. It is a record, not a session journal.

## Done when

The user has had a lesson tied to their mission, retrieved it under their own steam, and anything
newly established is a `learning` note that passes `lint`.

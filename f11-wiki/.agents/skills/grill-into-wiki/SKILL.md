---
name: grill-into-wiki
description: A relentless interview that lands what you know in the wiki as grounded, linked notes.
disable-model-invocation: true
---

# Grill Into Wiki

Most of what belongs in a wiki never arrives as a document — it is in the user's head. This is
how it gets out: interview the user, keep the transcript as evidence, and compile it into notes
that cite it.

## When to use

- The user wants a plan, design, or decision stress-tested **and recorded**.
- The wiki is thin on something the user knows well.
- The user types `/grill-into-wiki`.

## The transcript is the source

The wiki's hard rules say every compiled note links to a Raw source and no claim is asserted
without one. An interview does not weaken that — **it becomes the source**. The wiki then records
not just what is believed but who said it and when.

## Steps

1. **Find out what the wiki already knows:**
   ```bash
   python3 scripts/wiki_tool.py search-catalog --query "key terms"
   ```
   Open the most relevant notes. They set the floor for the interview.

2. **Run the interview** — use **llm-wiki-grilling**. A round of questions at a time, each with
   your recommended answer, facts looked up rather than asked.

3. **Open the transcript source as soon as the first round lands**, at
   `Raw/Sources/interviews/<topic-slug>.md`, from `_templates/source-note.md`:
   ```yaml
   Title: "Interview: export scheduling"
   Reference: "Interview with the maintainer, 2026-08-04"
   ContentType: ["interview"]
   Created: 2026-08-04
   Processed: false
   tags: ["source"]
   ```
   Record each resolved question and its answer under `## Content` **in the user's own words** —
   this is evidence, not prose. Append to it as the interview goes.

4. **Land each round before you ask the next.** The gap between rounds is the write point: append
   that round's questions and answers to the transcript, then write the notes for every branch it
   settled. The session may stop at any round, and an unwritten insight is a lost one — so a
   round's knowledge is on disk before the next round starts. It is also dead time while the user
   reads, and the natural place to write while a research agent is still out.

   Each note goes in the folder for its type (`Wiki/Concepts|Entities|Topics/`, or a plugin type
   like `decision` where one fits — run `plugins` to see what this vault has), with the transcript
   in `sources` and `source_count` matching.

5. **Mark the source processed** — `Processed: true` — once at least one note covers it.

6. **Run the gate:**
   ```bash
   python3 scripts/wiki_tool.py build
   python3 scripts/wiki_tool.py lint
   python3 scripts/wiki_tool.py source-scan --update --accept-covered
   python3 scripts/wiki_tool.py source-lint
   ```

7. **Log it** if the session meaningfully changed the wiki:
   ```bash
   python3 scripts/wiki_tool.py log --title "Interview: export scheduling" --details "<what changed>"
   ```

## Guardrails

- **Keep the transcript in the user's words.** It is evidence: their answers, verbatim enough to
  quote. The polish belongs in the compiled note.
- **Assert what the user actually said.** An interview grounds their claims, not yours — a gap
  you filled from your own knowledge is unsourced. Say so, or send it to **llm-wiki-research**.
- Where an answer contradicts an existing note, resolve it as **llm-wiki-grilling** describes —
  supersede or correct, and say which.
- When a term turns out to be fuzzy or overloaded, hand it to **llm-wiki-glossary**, which
  settles definitions against the notes.

## Done when

`lint` and `source-lint` pass, every resolved branch is either a note or an explicit deferral,
and the transcript shows as covered in `source-coverage`.

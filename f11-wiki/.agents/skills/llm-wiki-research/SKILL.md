---
name: llm-wiki-research
description: Investigate a question against primary sources and land the findings in the wiki as a cited Raw source plus compiled notes. Use when the user wants a topic researched, docs or API facts gathered, or when the wiki lacks the evidence to answer something.
---

# LLM Wiki: Research

The wiki refuses unsourced claims. This is how the source gets made when nobody in the room has
the answer.

## When to use

- The user asks for a topic to be researched or reading legwork delegated.
- **llm-wiki-grilling** or **llm-wiki-teach** hits something the user does not know either.
- `search-catalog` comes back empty on something the wiki ought to cover.

## Steps

1. **Confirm the gap is real:**
   ```bash
   python3 scripts/wiki_tool.py search-catalog --query "the question"
   ```
   If the wiki already covers it, this is a **llm-wiki-query**, not research.

2. **Spin up a background agent** so the user keeps working while it reads. Its brief:

   - Investigate against **primary sources** — official documentation, specifications,
     first-party APIs, the source code itself. Follow every claim back to the source that owns
     it, past any secondary write-up in between.
   - Note where sources **disagree** or where the answer is version-dependent. Both belong in the
     findings; neither should be smoothed over.

3. **Write the findings to `Raw/Sources/research/<question-slug>.md`** from
   `_templates/source-note.md`:
   ```yaml
   Title: "Research: Scryfall bulk data endpoints"
   Reference: "https://scryfall.com/docs/api/bulk-data"
   ContentType: ["research"]
   Created: 2026-08-04
   Processed: false
   tags: ["source"]
   ```
   **Every claim carries its URL inline.** `Reference` is the primary one; the rest sit beside
   the claims they support. A research source with claims and no links is worthless as evidence.

4. **Compile it** into focused Wiki notes — use **llm-wiki-ingest**. Set `Processed: true` once
   at least one note covers it.

5. **Run the gate:**
   ```bash
   python3 scripts/wiki_tool.py build
   python3 scripts/wiki_tool.py lint
   python3 scripts/wiki_tool.py source-scan --update --accept-covered
   python3 scripts/wiki_tool.py source-lint
   ```

## Guardrails

- **Write only what you opened.** A finding is something you read at its source; recall is a
  starting point for what to go and check.
- **Say what you could not establish.** A gap recorded honestly is more useful than a plausible
  guess, and the wiki will carry that guess for years.
- Prefer the dated, versioned source. Note when a source is old enough to distrust.
- Before merging research into an existing note, check whether it **contradicts** it. If it does,
  that is a correction to put to the user.

## Done when

`lint` and `source-lint` pass, every claim in the research source is traceable to a link, and the
compiled notes answer the original question.

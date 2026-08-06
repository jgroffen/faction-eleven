---
name: llm-wiki-plainly
description: That last message did not land — re-pitch it in plain English, in the wiki's own words.
disable-model-invocation: true
---

# LLM Wiki: Plainly

Stop. The last message did not land.

Re-pitch it: give enough context for it to make sense on its own, write in plain, direct English —
short sentences, one idea each, no jargon that has not been earned — and use **this wiki's
canonical terms** for anything it has a note about.

`[[Link]]` each of those terms on first use. A re-pitch in a wiki is worth more than a re-pitch
anywhere else, because the vocabulary is not just agreed — it is written down and readable. The
explanation doubles as a reading list.

Find the right terms before rewriting:

```bash
python3 scripts/wiki_tool.py search-catalog --query "the terms you used"
```

Where the wiki has a note, use its title and link it. Where it does not, say the thing in ordinary
words rather than inventing a term.

If the word that lost the user turns out to be genuinely fuzzy or overloaded — one word doing
several jobs, or two notes claiming it — that is **llm-wiki-glossary**, and the fix is to the
wiki, not to the sentence.

## Done when

The user says it landed.

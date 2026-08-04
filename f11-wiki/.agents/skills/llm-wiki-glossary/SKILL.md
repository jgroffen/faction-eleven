---
name: llm-wiki-glossary
description: Sharpen the wiki's shared language — challenge a fuzzy or overloaded term against the notes that define it, pick a canonical name, and fold duplicate notes together via aliases. Use when terminology is unclear, one word is doing several jobs, or two notes turn out to mean the same thing.
---

# LLM Wiki: Glossary

A wiki with two names for one thing is a wiki you cannot search. This skill keeps the vocabulary
sharp.

**The wiki is already the glossary** — no separate file. `concept` and `entity` notes *are* the
terms, and `aliases` is the synonym list. This skill maintains them.

## When to use

Reach for it the moment a term goes wobbly — mid-interview, mid-ingest, mid-answer. It is a
small, in-place correction, not a project.

- The user uses a term that conflicts with how a note defines it.
- One word is doing several jobs ("account" meaning the user, the org, and the billing record).
- Two notes turn out to be the same term under different names.

## The moves

### Challenge against the definition

When a term is used in a way the wiki does not define, say so immediately, with the note:

> `[[cancellation]]` defines this as the customer withdrawing before dispatch. You are using it
> for a failed payment. Same concept, or a second one that needs its own note?

### Sharpen the overloaded word

When one word covers several concepts, propose the split and name each part:

> "Account" is doing three jobs here — the login (`user`), the paying organisation
> (`customer`), and the ledger (`billing-account`). Which do you mean in this sentence?

Splitting a note is the fix: one term per note, always.

### Stress-test with a scenario

When the boundary between two terms is unclear, invent a concrete case that sits on it and make
the user rule. *"A customer with two orgs cancels one — does that end the account?"* Fuzzy
definitions survive abstraction and die on examples.

### Pick a canonical name, keep the others reachable

One note is the term. Everything else people call it goes in `aliases`, so `[[old-name]]` still
resolves and nobody's existing links break:

```yaml
aliases: ["cancellation request", "order withdrawal"]
```

Wording that should **not** be used goes in the body instead, so it stays visible but does not
become a link target:

```markdown
_Avoid: "refund" — that is the money movement, not the request. See [[refund]]._
```

### Merge, do not leave both

When two notes are the same term, fold the content into the better-named one, add the other's
title to its `aliases`, repoint the inbound `[[links]]`, and delete the duplicate. Two half-notes
are worse than either one alone.

## Guardrails

- **Change the definition, not the evidence.** Renaming or merging never drops a `sources` entry;
  the merged note carries the union, with `source_count` updated to match.
- **Only terms this wiki actually uses.** General vocabulary belongs in the reader's head, not in
  the wiki — a definition nobody looks up is context load.
- Keep definitions to a sentence or two: what the term **is**, not what it does.
- **Never invent a definition to settle an argument.** If neither the user nor the wiki can pin
  it down, that is **llm-wiki-research**.
- Fix it where you find it — do not defer terminology to a cleanup pass that never comes.

## After any change

```bash
python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint
```

A merge or rename changes the catalog, so `build` must run before the next `search-catalog`.

## Done when

One note per term, each with a one-line definition, its synonyms in `aliases`, and no dangling
`[[links]]` left by a merge.

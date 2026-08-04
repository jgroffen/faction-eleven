---
name: llm-wiki-grilling
description: Interview the user relentlessly about a plan, decision, or idea until every branch of the decision tree is resolved. Use when the user wants their thinking stress-tested, uses any "grill" trigger phrase, or when another skill needs to interview the user.
---

# LLM Wiki: Grilling

The interview loop. This skill is the **primitive** — `grill-into-wiki` and `llm-wiki-teach`
both drive it. On its own it writes nothing; it produces a shared understanding.

## The loop

Interview the user relentlessly about every aspect of this until you reach a shared
understanding. Walk down each branch of the decision tree, resolving dependencies between
decisions one at a time.

**Ask one question at a time**, and wait for the answer before continuing. Several questions at
once is bewildering, and the user will answer only the last one.

**Give your recommended answer with every question.** A question with no recommendation makes the
user do all the work. A recommendation they reject is still progress.

## Look it up before you ask it

The wiki is the environment of record. Before a question leaves your mouth, check whether the
wiki already answers it:

```bash
python3 scripts/wiki_tool.py search-catalog --query "key terms"
```

Open the notes it returns. **Facts** the wiki holds are not questions — state them back as
established and move on. **Decisions** are always the user's: put each one to them and wait.

This is the difference between grilling in a wiki and grilling anywhere else. The wiki should
make each session shorter than the last.

## Contradictions are the best questions

When an answer conflicts with an existing note, stop and surface it:

> `[[export-scheduling]]` says exports run on the shared job queue, but you just said they have
> their own worker. Which is true now — and did the other one change, or was the note wrong?

That fork matters: **the world changed** (write a new note, supersede the old) versus **the note
was wrong** (correct it). Never silently pick one.

## Guardrails

- Resolve dependencies in order. A question whose answer depends on an unresolved one wastes the
  user's turn — ask the blocker first.
- Push on the vague answer rather than accepting it. "It should be fast" is not resolved.
- Ask what the user is least comfortable with. That answer is usually the most valuable thing in
  the session.
- **Do not act on the outcome until the user confirms** you have reached a shared understanding.

## Done when

Every branch is resolved or explicitly deferred, and the user confirms the understanding is
shared. What happens to that understanding is the calling skill's job.

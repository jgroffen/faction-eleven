---
name: llm-wiki-grilling
description: Interview the user relentlessly about a plan, decision, or idea until every branch of the decision tree is resolved. Use when the user wants their thinking stress-tested, uses any "grill" trigger phrase, or when another skill needs to interview the user.
---

# LLM Wiki: Grilling

The interview loop. This skill is the **primitive** — `grill-into-wiki` and `llm-wiki-teach`
both drive it. On its own it writes nothing; it produces a shared understanding.

## The loop

Interview the user relentlessly until you reach a shared understanding. Map this as a **design
tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already
settled — the questions you can ask *now* without guessing at answers you have not heard yet. Ask
the whole frontier in one round, numbered, each with your recommended answer. Then wait for the
user's answers before the next round.

Format each question like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round of answers reshapes the tree — settled decisions push the frontier outward and unblock
questions that depended on them. Recompute the frontier and ask the next round. A question whose
answer depends on another question still open in this round belongs to a *later* round.

**Give your recommended answer with every question.** A question with no recommendation makes the
user do all the work. A recommendation they reject is still progress.

## Compute the frontier against the wiki

The wiki is the environment of record. Search it once for the whole round rather than once per
question:

```bash
python3 scripts/wiki_tool.py search-catalog --query "key terms"
```

Open the notes it returns. **Facts** the wiki holds are settled — state them back as established
and drop them from the round. **Decisions** are the user's: put each to them and wait.

This is the difference between grilling in a wiki and grilling anywhere else. The wiki should
make each session shorter than the last.

Finding facts is your job, never the user's, and the two kinds cost differently:

- **The catalog is cheap** — search it inline, as above, before every round.
- **A fact nobody has is expensive** — dispatch **llm-wiki-research** as a background agent and
  keep going. A running exploration is an unsettled prerequisite, so only the questions
  downstream of it wait for the report; ask the rest of the frontier now.

## Contradictions are the best questions

When an answer conflicts with an existing note, stop and surface it:

> `[[export-scheduling]]` says exports run on the shared job queue, but you just said they have
> their own worker. Which is true now — and did the other one change, or was the note wrong?

That fork matters: **the world changed** (write a new note, supersede the old) versus **the note
was wrong** (correct it). Put the fork to the user and let them pick.

## Guardrails

- Push on the vague answer rather than accepting it. "It should be fast" is not resolved.
- Ask what the user is least comfortable with. That answer is usually the most valuable thing in
  the session.
- **Act on the outcome once the user confirms** you have reached a shared understanding.

## Done when

The frontier is empty — every branch of the design tree visited or explicitly deferred, nothing
left silently assumed — and the user confirms the understanding is shared. What happens to that
understanding is the calling skill's job.

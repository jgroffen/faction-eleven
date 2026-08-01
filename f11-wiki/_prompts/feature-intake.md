# Prompt: Take in a feature

Use this to turn "we should build X" into a `feature` note that is specific enough to act on and
honest about what is still unknown.

## Goal

A feature note whose `## Acceptance` list someone else could check without asking you what you
meant.

## Ground it first

Before asking anything, look:

- `python3 scripts/dev_tool.py list-notes --query "<topic>"` — does a feature for this already
  exist? Prefer updating it to creating a near-duplicate.
- `python3 scripts/dev_tool.py list-notes --tag component` — which components will this touch?
  Read them, and read the code they point at.
- Look for `decision`, `pattern` and `convention` notes that already constrain this area. A
  feature that quietly contradicts an accepted decision is the expensive kind of mistake.

## Interview

Ask about intent before mechanism. Good questions, roughly in order:

1. **Who is this for, and what can't they do today?** Push back gently on solutions offered as
   problems ("we need a cache" → what's slow, for whom?).
2. **What does success look like from outside the system?** This becomes `## Behaviour`.
3. **What's explicitly out of scope?** Recording the boundary now saves an argument later.
4. **What are the edge cases that matter?** Empty states, concurrency, failure, permissions,
   scale, migration of existing data.
5. **How will we know it works?** Turn the answers into checkable acceptance statements.
6. **What's still undecided?** Anything architectural goes to the decision skill, not into a
   parenthetical.

Ask these a few at a time, not as a questionnaire. If the user gives a thorough brief up front,
skip to confirming what you inferred and asking only about the gaps.

## Propose before writing

Play back: the intent in one sentence, the components it touches, the acceptance list, and the
open questions. Get a correction pass. Then:

```bash
python3 scripts/dev_tool.py new-feature --title "<Title>" --state proposed \
    --component <slug> --component <slug> --summary "<one-line intent>"
```

Fill `## Intent`, `## Behaviour`, `## Acceptance` and `## Open Questions` in the note. Then
propose the first changes that would deliver it:

```bash
python3 scripts/dev_tool.py new-change --title "<first slice>" --feature <feature-slug> \
    --component <slug> --status discussing
```

## Guardrails

- **A feature is a capability, not a task.** If it reads like a unit of work, it's a `change`.
- Write acceptance statements as observable behaviour, not implementation ("a locked account
  can't sign in", not "add an `is_locked` column").
- Don't invent components. If the feature needs a part that doesn't exist yet, say so in
  `## Open Questions` and let the change or decision that creates it be explicit.
- Leave `state: proposed` until work actually starts. The states are for tracking reality, not
  optimism.
- If an open question is architectural, hand it to the decision skill now — features that carry
  unresolved architecture in a bullet list tend to get built twice.

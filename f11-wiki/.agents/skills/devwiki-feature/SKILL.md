---
name: devwiki-feature
description: This skill should be used when the user asks to "add a feature", "we should build X", "capture this feature in the wiki", "write up the requirements for X", or "what would it take to add X" in a vault with the software-development plugin. It interviews the user about intent, behaviour and acceptance, checks which components the feature touches, and creates a grounded `feature` note plus its first `change` notes.
---

# Software Development: Add a feature

Turn "we should build X" into a `feature` note specific enough to act on and honest about what's
still unknown.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `software-development`). If not, install it — see the repo's plugins/README.md.
- The codebase has been mapped into `component` notes (`dev_tool.py list-notes --tag component`).
  If there are none, run **devwiki-map** first — a feature that links to no components is a wish,
  not a plan.

## Steps

1. **Load the prompt template** from the vault's `_prompts/feature-intake.md`. Follow it to interview the user.
2. **Ground it before asking.** Search for an existing feature note
   (`python3 scripts/dev_tool.py list-notes --query "<topic>"`), read the component notes it would
   touch, and read the code behind them. Check for `decision`, `pattern` and `convention` notes
   that already constrain the area — a feature that quietly contradicts an accepted decision is
   the expensive kind of mistake.
3. **Interview for intent before mechanism** — who it's for and what they can't do today, what
   success looks like from outside the system, what's explicitly out of scope, the edge cases that
   matter, and how we'd know it works. Ask a few at a time, not as a questionnaire.
4. **Play it back** — the intent in one sentence, the components it touches, the acceptance list,
   the open questions — and take a correction pass.
5. **Create the note:**
   ```bash
   python3 scripts/dev_tool.py new-feature --title "Scheduled exports" --state proposed \
       --component scheduler --component api \
       --summary "Let admins export reports on a schedule rather than by hand."
   ```
   Then fill `## Intent`, `## Behaviour`, `## Acceptance` and `## Open Questions` in the note.
6. **Propose the first slices** as change notes, so the feature has a way in:
   ```bash
   python3 scripts/dev_tool.py new-change --title "Add export job runner" \
       --feature scheduled-exports --component scheduler --status discussing
   ```
   Hand off to **devwiki-change** to think any of them through properly.

## Guardrails

- **A feature is a capability, not a task.** If it reads like a unit of work, it's a `change`.
- Write acceptance statements as observable behaviour ("a locked account can't sign in"), not
  implementation ("add an `is_locked` column").
- Don't invent components. If the feature needs a part that doesn't exist yet, put that in
  `## Open Questions` and let the change or decision that creates it be explicit.
- Leave `state: proposed` until work actually starts — the states track reality, not optimism.
- If an open question is architectural, hand it to **devwiki-decision** now. Features carrying
  unresolved architecture in a bullet list tend to get built twice.
- Push back gently on solutions offered as problems ("we need a cache" → what's slow, for whom?).

## Done when

The gate passed, `Wiki/Features/<slug>.md` has a checkable acceptance list, and its managed
`## Changes` block lists the first slices. `python3 scripts/dev_tool.py status --feature <slug>`
gives the rollup.

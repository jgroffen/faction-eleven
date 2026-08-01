---
name: devwiki-change
description: This skill should be used when the user asks to "discuss a change", "let's think through changing X", "what would break if we did Y", "should we refactor X", "plan this change", or "write up this change in the wiki" in a vault with the software-development plugin. It scopes the change's blast radius in the real code, lays out options with trade-offs, and records the reasoning in a grounded `change` note.
---

# Software Development: Discuss a change

Think a change through *before* it's written, and leave the reasoning somewhere the next person
will find it.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `software-development`). If not, install it — see the repo's plugins/README.md.
- The components involved exist as notes. If not, run **devwiki-map** for that part of the repo
  first — the tool won't let a change cite a component that isn't there.
- A `feature` note to hang it on. If none fits, ask whether the feature note is simply missing
  (**devwiki-feature**), or whether this is maintenance under an existing one.

## Steps

1. **Load the prompt template** from the vault's `_prompts/change-discussion.md`.
2. **Scope it in the code, not in the abstract.** Read what the change touches and follow the
   callers — the surprise is almost never in the file you started in. Read the affected component
   notes, including their `## Notes` sections, where the sharp edges live. Collect the real paths
   as you go.
3. **Check what governs the area.** Look for `decision`, `pattern` and `convention` notes that
   apply. If the change contradicts one, that's the conversation to have first — either the change
   is wrong, or the decision needs superseding.
4. **Offer 2–3 genuine options**, each with what it costs and what it buys, and say which you'd
   pick and why. Include "do nothing" or "the smaller version" when they're live options; often
   they are. Where you're uncertain, say so and name what would resolve it.
5. **Be honest about risk** — what breaks if this is wrong, how you'd find out, whether it's
   reversible, what data has to migrate. Two risks you believe in beat six generic ones.
6. **Record it:**
   ```bash
   python3 scripts/dev_tool.py new-change --title "Add export job runner" \
       --feature scheduled-exports --component scheduler --status discussing \
       --path src/scheduler/jobs.py --summary "<one-paragraph motivation>"
   ```
   Fill `## Motivation`, `## Approach`, `## Impact`, `## Risks` and `## Discussion` — including
   the options you rejected and why.
7. **Keep the status truthful** as work progresses:
   ```bash
   python3 scripts/dev_tool.py set-status --note add-export-job-runner --status in-progress
   ```

## Guardrails

- Cite real paths. A change note naming files that don't exist is worse than an empty one.
- Describe the *shape* of the change, not a diff — diffs go stale, reasoning doesn't.
- `done` means merged, not "we agreed to do it".
- **Escalate architecture to a decision.** If the discussion turned on a choice with alternatives
  and a long half-life, extract it with **devwiki-decision** and link it from the change rather
  than burying it in prose. The test: would someone joining in a year need to know *why*, not just
  *what*?
- Don't let the note replace the conversation. Write it after the thinking, and keep it short
  enough that someone reads it.

## Done when

The gate passed, the change note names real components and paths, and the user is clear on which
option they're taking and what it risks.

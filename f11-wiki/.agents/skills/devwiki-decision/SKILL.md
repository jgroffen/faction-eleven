---
name: devwiki-decision
description: This skill should be used when the user asks to "make a decision", "record why we chose X", "write an ADR", "we need to decide between X and Y", "document this architecture decision", or "we're changing our mind about X" in a vault with the software-development plugin. It runs the ADR interview (context, options, decision, consequences), records a grounded `decision` note, and supersedes an earlier decision rather than rewriting it.
---

# Software Development: Make a decision

Record a choice that has alternatives and lasting consequences, so it stays legible to someone
reading it in two years who wasn't in the room.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `software-development`). If not, install it — see the repo's plugins/README.md.
- The components the decision constrains exist as notes (**devwiki-map** if not).
- Ideally, the `feature` or `change` that forced the question exists, so the ADR can be linked to
  the work.

## Steps

1. **Load the prompt template** from the vault's `_prompts/decision-record.md`.
2. **Check whether this has been decided before:**
   ```bash
   python3 scripts/dev_tool.py list-notes --tag decision
   ```
   If it has and the user is changing course, this is a **supersede**, not an edit.
3. **Interview** through the four sections:
   - **Context** — what's true about the system that made this a decision rather than an obvious
     call: constraints, deadlines, existing commitments, what can't change. Present tense of the
     decision, no hindsight.
   - **Options** — at least two, stated fairly. One real option and two strawmen fools nobody.
   - **Decision** — what was chosen and the factor that actually settled it.
   - **Consequences** — what it makes easy, what it makes hard, what's now foreclosed, and what
     would have to happen to revisit it.
   Ask directly: *what's the part of this you're least comfortable with?* That answer is usually
   the most valuable line in the note.
4. **Record it:**
   ```bash
   python3 scripts/dev_tool.py new-decision --title "Run exports on the existing job queue" \
       --feature scheduled-exports --component scheduler --status accepted \
       --context "..." --options "..." --decision "..." --consequences "..."
   ```
   Use `--status proposed` while it's still being weighed, then `set-status --note <slug>
   --status accepted` when it lands (the tool stamps `decided` with today's date).
5. **Link it from the work** — re-run `new-change`/`new-feature` with `--decision <slug>` so it
   shows up in the feature's managed `## Decisions` block.

## Superseding

**Never rewrite an accepted decision.** Its value is that it records what was believed at the
time. Write a new one instead:

```bash
python3 scripts/dev_tool.py new-decision --title "Move exports to a dedicated worker" \
    --supersedes run-exports-on-the-existing-job-queue --status accepted \
    --context "..." --options "..." --decision "..." --consequences "..."
```

The tool flips the old note to `superseded` and cross-links both. In the new note's `## Context`,
say **what changed** since the old decision — that delta is the whole point of the pair.

## Guardrails

- Title it as a choice made — "Store sessions in Redis", not "Session storage". Someone scanning
  `Wiki/Decisions/` should learn what was decided from the filenames alone.
- One decision per note. Two choices means two notes.
- No hindsight in `## Context`. If you know it only because of what happened after, it belongs in
  the superseding note.
- **Don't record non-decisions.** If there was only ever one option, it's documentation — put it
  in the component or convention note.
- Include the consequences you're not happy about. Those are the ones worth recording.
- Keep it short. An ADR nobody reads has failed regardless of its rigour.

## Done when

The gate passed, the decision reads as a choice with real alternatives, and it's linked from the
feature or change that motivated it. `python3 scripts/dev_tool.py status` shows nothing stuck at
`proposed` that the user thinks is settled.

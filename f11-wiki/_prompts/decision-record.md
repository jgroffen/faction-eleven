# Prompt: Record a decision (ADR)

Use this when a choice has alternatives and lasting consequences. The note's job is to make the
reasoning legible to someone reading it in two years, who will not have the conversation you just
had.

## Goal

An ADR whose `## Context` still makes sense after the code has moved on, and whose
`## Consequences` includes the ones you're not pleased about.

## Before writing

1. `python3 scripts/dev_tool.py list-notes --tag decision` — has this been decided before? If it
   has and you're changing course, this is a **supersede**, not an edit.
2. Read the components the decision constrains, and the `pattern`/`convention` notes near it.
3. Identify the feature or change that forced the question, so the ADR can be linked to it.

## The interview

**Context.** What's true about the system that made this a decision rather than an obvious call?
Capture the constraints — deadlines, team size, existing commitments, things that can't change.
Write it in the present tense of the decision, not with hindsight.

**Options.** At least two, each stated fairly. An ADR listing one real option and two strawmen
fools nobody and helps nobody. For each: what it is, what it costs, what it buys. Include the
status quo when it's viable.

**Decision.** What was chosen and the reasoning that settled it — the actual deciding factor, not
a summary of every consideration. If it came down to one constraint, say which.

**Consequences.** What this makes easy, what it makes hard, and what now must be true. Include:
- what the team is now committed to,
- what becomes harder or is foreclosed,
- what would have to happen to revisit this.

Ask the user directly: *what's the part of this you're least comfortable with?* That answer is
usually the most valuable line in the note.

## Write it

```bash
python3 scripts/dev_tool.py new-decision --title "<A choice, stated as a choice>" \
    --feature <slug> --component <slug> --status accepted \
    --context "..." --options "..." --decision "..." --consequences "..."
```

Title it as a decision made — "Store sessions in Redis", not "Session storage". Someone scanning
`Wiki/Decisions/` should learn what was decided from the filenames alone.

Use `--status proposed` while it's still being weighed, then:

```bash
python3 scripts/dev_tool.py set-status --note <slug> --status accepted
```

## Superseding

**Never rewrite an accepted decision.** Its value is that it records what was believed at the
time. When thinking changes, write a new one:

```bash
python3 scripts/dev_tool.py new-decision --title "<New choice>" --supersedes <old-slug> \
    --status accepted --context "..." --options "..." --decision "..." --consequences "..."
```

The tool flips the old note to `superseded` and cross-links both. In the new note's `## Context`,
say what changed since the old decision — that delta is the whole point.

## Guardrails

- One decision per note. If you're recording two choices, write two notes.
- No hindsight in `## Context`. If you know it only because of what happened after, it belongs in
  the superseding note.
- Don't record non-decisions. If there was only ever one option, it's documentation, not an ADR —
  put it in the component or convention note.
- Link it from the change or feature that motivated it, so it's findable from the work.
- Keep it short. An ADR nobody reads has failed regardless of its rigour.

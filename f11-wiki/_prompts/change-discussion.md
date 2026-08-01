# Prompt: Discuss a change

Use this to think through a change to the codebase *before* writing it — and to leave the
reasoning somewhere the next person will find it.

## Goal

A `change` note that states what's being changed, which components it disturbs, what could break,
and why this approach beat the alternatives.

## Scope it in the code, not in the abstract

Before offering an opinion:

1. Find the real blast radius. Read the code the change touches and follow the callers — the
   surprise in a change is almost never in the file you started in.
2. `python3 scripts/dev_tool.py list-notes --tag component` and read the notes for each component
   involved, including their `## Notes` sections (that's where the sharp edges live).
3. Check for `decision`, `pattern` and `convention` notes governing this area. If the change
   contradicts one, that's the conversation to have first — either the change is wrong, or the
   decision needs superseding.
4. Note the real paths as you go; they go in `--path` and the `**Code:**` line.

## Frame the options

Present **2–3 genuine options**, each with what it costs and what it buys. Say which you'd pick
and why — a menu with no recommendation pushes the work back onto the user.

Useful axes: blast radius, reversibility, migration burden, how it ages, whether it fits the
patterns already here. Include "do nothing" or "do the smaller version" when they're live options;
often they are.

Where you're uncertain, say so plainly and name what would resolve it.

## Surface the risk honestly

- What breaks if this is wrong, and how would you find out — a test, a metric, an error?
- Is there data to migrate, or a state the system passes through where both old and new must work?
- Can it be rolled back, or is it one-way?
- What's the smallest version that's still worth doing?

Don't list risks you don't believe in to look thorough. Two real ones beat six generic ones.

## Record it

```bash
python3 scripts/dev_tool.py new-change --title "<Title>" --feature <feature-slug> \
    --component <slug> --status discussing --path src/api/handlers.py
```

Fill `## Motivation`, `## Approach`, `## Impact`, `## Risks` and `## Discussion` — including the
options you rejected and why. Then move it along as reality does:

```bash
python3 scripts/dev_tool.py set-status --note <change-slug> --status planned
```

## When it's really a decision

If the discussion turned on an architectural choice — one with alternatives, consequences, and a
long half-life — extract it into a `decision` note and link it from the change. The test: would
someone joining in a year need to know *why*, not just *what*? Then it's a decision.

## Guardrails

- Cite real paths. A change note that names files that don't exist is worse than an empty one.
- Describe the shape of the change, not a diff — diffs go stale, reasoning doesn't.
- Keep `change_status` truthful; `done` means merged, not "we agreed to do it".
- If the change belongs to no feature, ask whether the feature note is simply missing.
- Don't let the note become a substitute for the conversation. Write it *after* the thinking, and
  keep it short enough that someone reads it.

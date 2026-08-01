# Prompt: Map a codebase into component notes

Use this to bootstrap a software-development wiki: read a real repository and turn it into
`component` notes the rest of the plugin can hang features, changes and decisions on.

## Goal

A small set of components that a new engineer would recognise as "the parts of this system" —
each with a real path, a clear responsibility, and honest dependencies.

## Read before you write

1. Start from the entry points: build files, `main`/`index`, route tables, CLI definitions,
   deployment manifests. They tell you what the system *is* before the folder tree does.
2. Read the top-level structure, then open enough of each candidate to state what it owns.
3. Look for existing documentation (`README`, `ARCHITECTURE`, `CLAUDE.md`, ADR folders) and treat
   it as a claim to verify against the code, not as truth.
4. Check the vault first — `python3 scripts/dev_tool.py list-notes --tag component` — so you
   update existing notes rather than duplicating them.

## Choosing the granularity

Aim for **5–15 components** on a first pass, however large the repo. The right size is the unit
people talk about in conversation: "the scheduler", "the web UI", "the billing service" — not
every file, and not the whole repo as one blob.

Split a candidate when it has two responsibilities that change for different reasons. Merge two
when nobody would ever touch one without the other.

A component is not always a directory. It can be a cross-cutting concern (auth, migrations) as
long as you can name the paths that implement it.

## Interview the user

Propose the breakdown **before** creating notes, as a list of one-liners:

> `scheduler` (job) — decides what runs when · `src/scheduler/`
> `api` (service) — public HTTP surface · `src/api/`

Ask about what the code can't tell you:
- Which of these are load-bearing versus incidental?
- Anything here that's deprecated, or being replaced?
- Any component you'd add that doesn't have obvious code yet?
- Which repo(s) are in scope, if more than one?

Adjust, then confirm before writing.

## Write the notes

```bash
python3 scripts/dev_tool.py new-component --name "Scheduler" --kind job \
    --repo myapp --path src/scheduler --depends-on datastore
```

Then fill each note's prose sections: `## Responsibility` (including what it deliberately does
*not* own), `## Interfaces` (how others talk to it), and `## Notes` (the things a newcomer learns
the hard way).

## Guardrails

- **Every path must exist.** Verify before you write it. No invented components.
- Record dependencies you can see in the code (imports, calls, schemas), not ones you assume.
- Don't editorialise about quality — a component note describes what is, not what you'd prefer.
- Leave `## Notes` empty rather than padding it.
- Stop at components. Features, changes and decisions come from the other skills; a mapping pass
  that also invents twenty features produces confident fiction.

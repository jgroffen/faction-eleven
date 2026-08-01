# Software Development Frontmatter Schema

The `software-development` plugin adds six note types on top of the core LLM Wiki types
(`topic`, `concept`, `entity`, `log`). All core lint rules still apply: exactly one tag, ISO
`created`/`updated`, `source_count == len(sources)`.

All six types are **source-exempt** (`requires_source: false`). Their content is derived from the
codebase and from discussion, not from `Raw/Sources/` clippings, so they pass lint with
`sources: []` and `source_count: 0`.

## Two kinds of grounding

Because there are no Raw sources, these notes carry their provenance two other ways:

- **Code grounding** — a `**Code:**` line in the body listing **repo-relative paths in
  backticks**, plus a `paths:` frontmatter list on the types that have one. This is what ties a
  note to the real repository. Every `component`, and any `change` or `pattern` that has landed,
  should name real paths.
- **Note grounding** — `**Based on:** [[...]]` wikilinks to other wiki notes the note draws on.
  These also produce Obsidian backlinks, so a component note shows every change, decision and
  pattern that references it.

**Do not invent code paths.** If a path does not exist in the repo, either find the real one or
leave it out and say so in the note.

## Link topology

```
change ──▶ feature ──▶ component
   │           │            ▲
   └─▶ decision ◀───────────┤
                pattern ────┤
             convention ────┘
```

A `change` belongs to a `feature` and touches `component`s. A `decision` is motivated by a change
or feature and constrains components. `pattern` and `convention` point at the components that
exemplify or are governed by them.

`scripts/dev_tool.py` scaffolds and maintains all six types and keeps the links, counts, and
managed blocks consistent — the skills supply the content.

## Managed blocks

The tool owns these regions; edit the prose around them freely, but not inside:

| Note type | Block | Markers |
|-----------|-------|---------|
| `component` | `## Features` | `<!-- sd:features:start -->` … `:end` |
| `component` | `## Changes` | `<!-- sd:changes:start -->` … `:end` |
| `feature` | `## Decisions` | `<!-- sd:decisions:start -->` … `:end` |
| `feature` | `## Changes` | `<!-- sd:changes:start -->` … `:end` |

Run `python3 scripts/dev_tool.py refresh` to regenerate them all from the notes' frontmatter.

## `component` notes (`Wiki/Components/`, no source required)

A service, module, package or subsystem — the anchor everything else links to.

| Field | Meaning |
|-------|---------|
| `tags` | `[component]` |
| `repo` | the repository it lives in (free text; useful in multi-repo wikis) |
| `kind` | one of `service`, `library`, `module`, `ui`, `datastore`, `job`, `tool` |
| `paths` | repo-relative paths that make up this component (dirs or files) |
| `depends_on` | slugs of other `component` notes it depends on |
| `feature_count` | features touching this component (maintained by the tool) |
| `change_count` | changes touching this component (maintained by the tool) |

## `feature` notes (`Wiki/Features/`, no source required)

A user-facing capability, usually spanning several components.

| Field | Meaning |
|-------|---------|
| `tags` | `[feature]` |
| `state` | `proposed` → `building` → `shipped`, or `deprecated` |
| `components` | slugs of the `component` notes it touches |
| `decisions` | slugs of `decision` notes that shaped it |
| `change_count` | changes under this feature (maintained by the tool) |

The body carries `## Intent`, `## Behaviour`, and `## Acceptance` (a checklist). Keep acceptance
statements checkable — that is what makes a feature note useful later.

## `decision` notes (`Wiki/Decisions/`, no source required)

An architecture decision record: context → options → decision → consequences.

| Field | Meaning |
|-------|---------|
| `tags` | `[decision]` |
| `decision_status` | `proposed`, `accepted`, `rejected`, or `superseded` |
| `decided` | ISO date the decision was made (set when it reaches `accepted`) |
| `components` | slugs of the components it constrains |
| `feature` | slug of the feature that motivated it, if any |
| `supersedes` | slug of the decision this one replaces |
| `superseded_by` | slug of the decision that replaced this one (written by the tool) |

**Decisions are immutable once accepted.** Do not rewrite an accepted decision when your thinking
changes — record a new one with `--supersedes`, which flips the old note to `superseded` and
cross-links both. The value of an ADR is that it preserves what was believed at the time.

## `change` notes (`Wiki/Changes/`, no source required)

A discrete change to the code: proposed, in flight, or done.

| Field | Meaning |
|-------|---------|
| `tags` | `[change]` |
| `change_status` | `discussing` → `planned` → `in-progress` → `done`, or `abandoned` |
| `feature` | slug of the parent `feature` note |
| `components` | slugs of the components it touches |
| `decisions` | slugs of `decision` notes it depends on or triggered |
| `paths` | repo-relative paths the change affects |

A change starts at `discussing` — a change note is a good place to think *before* the code exists,
not just a record of what was merged.

## `pattern` notes (`Wiki/Patterns/`, no source required)

A reusable approach **as this codebase actually does it** — not a textbook pattern.

| Field | Meaning |
|-------|---------|
| `tags` | `[pattern]` |
| `components` | slugs of components that exemplify it |
| `paths` | repo-relative paths to the exemplars |
| `related_conventions` | slugs of `convention` notes that codify part of it |

A pattern note earns its place by naming a real exemplar to copy and a `## When Not To Use It`.

## `convention` notes (`Wiki/Conventions/`, no source required)

A team standard: naming, structure, testing, review, style.

| Field | Meaning |
|-------|---------|
| `tags` | `[convention]` |
| `scope` | `repo-wide`, or the slug of the component it applies to |
| `enforcement` | `lint`, `test`, `review`, or `manual` — how compliance is actually checked |

`enforcement` is deliberately honest: a convention enforced only by `manual` is one people will
drift from, and recording that is the first step to automating it.

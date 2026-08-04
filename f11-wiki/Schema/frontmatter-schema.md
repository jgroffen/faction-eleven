# Frontmatter Schema

This file defines the required and optional frontmatter for notes in the LLM Wiki.

## Raw Source Notes (`Raw/Sources/`)

```yaml
---
Title: ""              # required, non-empty
Author: ""             # optional
Reference: ""          # required: URL or citation to the original
ContentType:
  - "markdown"         # list of content types
Created: YYYY-MM-DD     # required, ISO date
Processed: false        # required boolean; true once compiled into Wiki notes
tags:
  - "source"           # required; must include "source"
---
```

Notes:
- `Processed: true` asserts that the source has been compiled into one or more Wiki notes. `source-lint` fails if a processed source has no Wiki coverage.

Interview and research sources are ordinary Raw sources, kept in subfolders for legibility:

- `Raw/Sources/interviews/` — a grilling transcript. `Reference` is a citation, e.g.
  `"Interview with the maintainer, 2026-08-04"`; `ContentType: ["interview"]`.
- `Raw/Sources/research/` — findings gathered from primary sources. `Reference` is the primary
  URL, with the rest cited inline beside the claims they support; `ContentType: ["research"]`.

They are evidence like any other source, and notes compiled from them cite them normally.

## Compiled Wiki Notes (`Wiki/Topics|Concepts|Entities|Logs|Handovers|Learning/`)

```yaml
---
tags:
  - "concept"          # required; exactly one of: topic, concept, entity, log, handover, learning
topics: []             # list of topic slugs/links this note belongs to
status: seed           # seed | draft | stable
created: YYYY-MM-DD     # required, ISO date
updated: YYYY-MM-DD     # required, ISO date
sources: []            # list of paths under Raw/Sources/ this note is built from
source_count: 0        # required; must equal len(sources)
aliases: []            # optional alternate titles
---
```

Notes:
- `tags` must contain **exactly one** allowed tag value: `topic`, `concept`, `entity`, `log`, `handover`, or `learning`.
- `source_count` must equal the number of entries in `sources`.
- Each entry in `sources` should be a path to an existing file under `Raw/Sources/` (a bare filename like `example.md` is also accepted and resolved against `Raw/Sources/`).
- `log`, `handover`, and `learning` notes are exempt from requiring a source link: they record the Wiki's own history and the collaboration around it rather than compiling sources.

### Handover Notes (`Wiki/Handovers/`)

Session handovers add two fields. They are created by `wiki_tool.py handover new`, which stamps
both — see `command-reference.md`.

```yaml
status: open            # open | resumed | closed
expires: YYYY-MM-DD     # default 90 days out; push it out with `handover extend`
```

Handovers are **temporary by design**, and `handover prune` is what clears them out — but the two
ways a handover becomes spent are not the same. A **closed** one was deliberately finished with,
so `prune` deletes it. An **expired** one was never finished with; it simply aged out, and its
`## Not yet written down` section is the only copy of that content. So `prune` confirms each
expired handover individually, offering to extend it instead, and refuses to delete any of them
when it has no terminal to ask at. Anything in a handover worth keeping should already be a real
note.

### Learning Notes (`Wiki/Learning/`)

Learner state for the `llm-wiki-teach` skill.

```yaml
kind: record            # mission | record | preferences
status: active          # active | superseded
```

- `mission` — one per topic: why the user wants to learn it. Grounds every lesson.
- `record` — one per non-obvious thing established. Superseded, never deleted, when an
  understanding is corrected: set `status: superseded` and link the note that replaces it.
- `preferences` — how the user wants to be taught.

See `naming-conventions.md` for filenames and `lint-checklist.md` for the validation gate.

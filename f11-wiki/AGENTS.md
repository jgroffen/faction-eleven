# Agent Rules for This LLM Wiki

This repository is an **LLM Wiki**. Read these rules before making changes.

## The LLM Wiki Concept

An LLM Wiki separates **captured source material** from **compiled knowledge**.

- Raw sources preserve original context.
- Wiki notes turn useful claims into short, linked, reusable knowledge.
- The most useful workflow is to **search the compiled Wiki first**, and open Raw sources only when more evidence or detail is needed.

Source material is compiled into a number of Wiki notes, for example:

- one or more **topic** notes (`Wiki/Topics/`)
- one or more **concept** notes (`Wiki/Concepts/`)
- one or more **entity** notes (`Wiki/Entities/`)

**Log** notes (`Wiki/Logs/`) record meaningful changes to the Wiki and are normally created by deterministic tooling.

Every compiled Wiki note must link back to its Raw source(s) in `Raw/Sources/`. Do not rely on generated text alone — keep the transformation visible: a small Raw source should become focused Wiki notes.

## Hard Rules

1. **Treat `Raw/Sources/` as source material, not as compiled notes.** Never edit a Raw source to make it read like a finished Wiki note.
2. **Write reusable knowledge only under `Wiki/`.** Topics, concepts, and entities live here.
3. **Keep every compiled note linked to one or more Raw Sources.** Populate the `sources` list and keep `source_count` equal to its length.
4. **Search `Wiki/catalog.jsonl` before opening broad Raw context.** Use the query skill / `search-catalog` first. Only open Raw sources when the compiled note is insufficient or the user asks for source-level verification.
5. **Run `build`, `lint`, and source checks before commits** (see the Maintenance Gate below).
6. **Do not invent citations or create unsupported claims.** If a claim is not backed by a Raw source, do not assert it.

## Layout

| Path | Purpose |
|------|---------|
| `Raw/Sources/` | Original source notes (Markdown). Evidence. |
| `Raw/Files/` | Binary / large source files (git-ignored). |
| `Wiki/Topics/` | Broad topic notes. |
| `Wiki/Concepts/` | Focused concept notes. |
| `Wiki/Entities/` | People, orgs, things. |
| `Wiki/Logs/` | Change log notes. |
| `Wiki/catalog.jsonl` | Machine-readable catalog of compiled notes. |
| `Wiki/index.md` | Human index of the Wiki. |
| `Schema/` | Schema, conventions, lint rules, source manifest. |
| `_templates/` | Note templates. |
| `.agents/skills/` | Agent skills — the core wiki's, plus any a plugin installed. |
| `.claude/skills/` | Symlinks into `.agents/skills/` so Claude Code discovers them. Committed; rebuild with `wiki_tool.py skills --link`. |
| `scripts/` | Deterministic tooling. |

## Allowed Compiled Note Tags

Each compiled Wiki note uses exactly one allowed tag. The core tags are `topic`, `concept`,
`entity`, `log`. **Plugins may add more** (see below); run
`python3 scripts/wiki_tool.py plugins` to see every tag currently available in this vault.

## Extending the Wiki with Plugins

The wiki is extensible: a plugin registers additional note types (and their folders) by
dropping a manifest at `Schema/plugins/<name>.json`. `build`, `lint`, and `doctor` discover
plugins automatically — **do not edit `scripts/wiki_tool.py` to add a note type.** Each
plugin note type declares its `tag`, `folder`, and whether it `requires_source` (so derived
notes can be source-exempt like `log`). Tags and folders must be unique; conflicts fail the
gates with a `PLUGIN:` error. See `Schema/plugin-schema.md` for the manifest contract.

## Maintenance Gate

Before every meaningful commit:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

After ingesting sources, also run:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```

## Ingest Workflow

1. Put cleaned Markdown in `Raw/Sources/`.
2. Run `search-catalog` for likely related topics.
3. Open only the most relevant compiled Wiki notes.
4. Create or update focused notes in `Wiki/`.
5. Add Raw source links to `sources` and keep `source_count` accurate.
6. Run the build + lint + source-scan + source-lint commands above.
7. Add a log entry if the ingest meaningfully changed the Wiki.

See `Schema/` for frontmatter schema, naming conventions, the lint checklist, the command reference, and `Schema/workflow-examples.md` for worked examples.

## Software Development Plugin

This vault has the **software-development** plugin installed
(`Schema/plugins/software-development.json`). It turns the wiki into the knowledge base for a
**specific codebase** — what it's made of, what it does, and why it's built that way. It adds six
note types:

- **`component`** (`Wiki/Components/`) — a service, module, package or subsystem. The anchor
  everything else links to.
- **`feature`** (`Wiki/Features/`) — a user-facing capability, usually spanning several
  components.
- **`decision`** (`Wiki/Decisions/`) — an ADR: context → options → decision → consequences.
- **`change`** (`Wiki/Changes/`) — a discrete change to the code, from `discussing` to `done`.
- **`pattern`** (`Wiki/Patterns/`) — a reusable approach as this codebase actually does it.
- **`convention`** (`Wiki/Conventions/`) — a team standard and how it's enforced.

The topology is **change → feature → component**, with `decision` referenced by the change or
feature that motivated it, and `pattern`/`convention` pointing at the components they apply to.
All six types are source-exempt (no Raw source needed). See
`Schema/software-development-frontmatter-schema.md` for the fields.

### Ground every note in real code

These notes carry provenance two ways instead of `sources:`:

- **`**Code:**` lines and `paths:` frontmatter** — repo-relative paths, in backticks. This is what
  ties a note to the repository.
- **`**Based on:** [[...]]` wikilinks** — other wiki notes the note draws on, which surface as
  backlinks on those notes.

**Read the code before writing the note.** Do not invent components, paths, or behaviour that
aren't in the repo; if you can't find the real path, say so rather than guessing. A wiki that
describes a codebase that doesn't exist is worse than no wiki.

### Authoring

Notes are scaffolded and maintained by `scripts/dev_tool.py`, which writes them, wires the links,
keeps counts and managed blocks current, and runs the maintenance gate. Don't hand-author these
notes when the tool can do it consistently:

```bash
python3 scripts/dev_tool.py new-component --name "<Name>" --kind service \
    --repo <repo> --path src/api --path src/api/handlers.py
python3 scripts/dev_tool.py new-feature --title "<Title>" --state proposed \
    --component <slug> --summary "..."
python3 scripts/dev_tool.py new-change --title "<Title>" --feature <slug> \
    --component <slug> --status discussing --path src/api/handlers.py
python3 scripts/dev_tool.py new-decision --title "<Title>" --feature <slug> \
    --context "..." --options "..." --decision "..." --consequences "..." --status accepted
python3 scripts/dev_tool.py new-pattern --title "<Title>" --component <slug> --path <file>
python3 scripts/dev_tool.py new-convention --title "<Title>" --scope repo-wide --enforcement lint

python3 scripts/dev_tool.py set-status --note <slug> --status <value>   # move through a lifecycle
python3 scripts/dev_tool.py list-notes --query "auth" --tag component   # find slugs to link
python3 scripts/dev_tool.py refresh                                     # rebuild links + counts
python3 scripts/dev_tool.py status                                      # project rollup
```

All `new-*` commands are **idempotent on title** — re-run with the same title to update a note in
place, preserving the prose you've added to unmanaged sections.

### Lifecycles

- `feature.state`: `proposed` → `building` → `shipped` (or `deprecated`)
- `change.change_status`: `discussing` → `planned` → `in-progress` → `done` (or `abandoned`)
- `decision.decision_status`: `proposed` → `accepted` (or `rejected`), later `superseded`

**Accepted decisions are immutable.** When thinking changes, write a new decision with
`--supersedes <old-slug>` — the tool flips the old note to `superseded` and cross-links both.
Never rewrite history in an accepted ADR; its worth is that it records what was believed then.

### Where things belong

- A *capability* users can ask for → `feature`. A *unit of work* on the code → `change`.
- A choice with alternatives and lasting consequences → `decision`. If a change's discussion
  produced an architectural choice, extract it into a decision and link it, rather than leaving it
  buried in the change's prose.
- Something the codebase does repeatedly → `pattern`. A rule people must follow → `convention`.
- General industry knowledge that isn't about *this* codebase belongs in the core `concept` type,
  not `pattern`.

Reusable prompt templates live in `_prompts/` (`codebase-map.md`, `feature-intake.md`,
`change-discussion.md`, `decision-record.md`) — tailor them to this project.

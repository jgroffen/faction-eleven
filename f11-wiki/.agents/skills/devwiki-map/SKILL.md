---
name: devwiki-map
description: This skill should be used when the user asks to "map this codebase into the wiki", "document the architecture", "what are the components of this system", "add my repo to the dev wiki", or "bootstrap the software development wiki" in a vault with the software-development plugin. It reads a real repository, agrees a component breakdown with the user, and creates grounded `component` notes for it.
---

# Software Development: Map the codebase

Turn a real repository into `component` notes — the anchors that features, changes, decisions,
patterns and conventions all link to. Run this **first** after installing the plugin.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `software-development`). If not, install it — see the repo's plugins/README.md.
- You know where the codebase is. If the vault is not inside the repo, ask for its path — you
  must read the actual code, not describe it from memory or from its README alone.

## Steps

1. **Load the prompt template** from the vault's `_prompts/codebase-map.md`. Follow it.
2. **Read the repository.** Start from entry points (build files, `main`/`index`, route tables,
   CLI definitions, deployment manifests), then the top-level structure, then enough of each
   candidate component to state what it owns.
3. **Check what's already there:**
   ```bash
   python3 scripts/dev_tool.py list-notes --tag component
   ```
   Update existing notes rather than creating near-duplicates.
4. **Propose the breakdown** — 5–15 components, each a one-liner with its kind and real paths —
   and get the user's corrections before writing anything.
5. **Create the notes:**
   ```bash
   python3 scripts/dev_tool.py new-component --name "Scheduler" --kind job \
       --repo myapp --path src/scheduler --depends-on datastore \
       --summary "Decides what runs when, and hands work to the queue."
   ```
   Create components before the ones that depend on them — `--depends-on` requires the target to
   exist. Re-run with the same `--name` to update in place.
6. **Fill the prose** in each note: `## Responsibility` (including what it deliberately does
   *not* own), `## Interfaces` (how others talk to it), and `## Notes` (what a newcomer would
   otherwise learn the hard way).

## Guardrails

- **Every path must exist.** Verify before writing it. Never invent a component, a path, or a
  dependency — the tool validates slugs, but only you can validate the code.
- Right-size the breakdown: the unit people name in conversation ("the scheduler", "the web UI"),
  not every file, and not the whole repo as one note.
- Record dependencies you can see (imports, calls, schemas), not ones you assume.
- Describe what is, not what you'd prefer. A component note isn't a code review.
- **Stop at components.** Features, changes and decisions come from the other skills; a mapping
  pass that also invents twenty features produces confident fiction.
- Leave a section empty rather than padding it.

## Done when

`python3 scripts/dev_tool.py status` shows the components, the gate passed, and the user agrees
the breakdown matches how they think about the system. Then point them at **devwiki-feature**,
**devwiki-change**, or **devwiki-decision** as the work comes up.

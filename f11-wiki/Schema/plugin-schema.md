# Plugin Schema

The LLM Wiki ships four core note types — `topic`, `concept`, `entity`, `log`. **Plugins**
extend the wiki with additional note types (and the folders that hold them) without editing
`scripts/wiki_tool.py`. `build`, `lint`, and `doctor` discover plugins automatically.

## How a plugin registers

A plugin drops one JSON manifest into `Schema/plugins/<name>.json`. On every run,
`wiki_tool.py` reads all manifests in that folder and merges their note types with the core
set.

```json
{
  "name": "mtg-wiki",
  "version": "0.1.0",
  "note_types": [
    {"tag": "card",     "folder": "Wiki/Cards",     "requires_source": true},
    {"tag": "set",      "folder": "Wiki/Sets",      "requires_source": true},
    {"tag": "mechanic", "folder": "Wiki/Mechanics", "requires_source": false}
  ],
  "source_subdirs": ["Raw/Sources/cards", "Raw/Sources/sets"],
  "install": {
    "summary": "a Magic: The Gathering knowledge base, populated from Scryfall",
    "extra_dirs": ["Raw/Files/images"],
    "post_install": "mtg-wiki installed. Populate cards with: …",
    "post_update": "mtg-wiki updated. …"
  }
}
```

## Fields

| Field | Required | Meaning |
|-------|----------|---------|
| `name` | yes | Plugin name (defaults to the manifest filename). |
| `version` | no | Plugin version string, for display. |
| `note_types` | yes | List of note types this plugin adds. |
| `note_types[].tag` | yes | The single allowed tag for the note type. Must not collide with a core tag or another plugin's tag. |
| `note_types[].folder` | yes | Vault-relative folder holding these notes, e.g. `Wiki/Cards`. Must be unique across all note types. |
| `note_types[].requires_source` | no (default `true`) | Whether `lint` requires the note to link ≥1 Raw source. Set `false` for derived/cross-cutting notes (like the core `log` type). |
| `source_subdirs` | no | Raw source subfolders the plugin uses, e.g. `Raw/Sources/cards`. Created at install time; `iter_sources` already recurses all of `Raw/Sources/`. |
| `install` | no | Install metadata (below). Everything else the installer needs is derived from the payload layout. |
| `install.summary` | no | One line describing what the plugin turns a wiki into. Shown by the installer's plugin picker — the single source for this description. |
| `install.extra_dirs` | no | Folders to create beyond the note-type folders and `source_subdirs`, e.g. `Raw/Files/images`. |
| `install.post_install` / `install.post_update` | no | Closing message printed after a first install / a re-run. `post_update` falls back to `post_install`. |

## Payload layout

A plugin folder is `plugin/` (what gets copied into the vault) plus `skills/`. The installer
derives every copy from this layout, so adding a template or a schema doc needs no code change:

| In the plugin | Installed to |
|---------------|--------------|
| `plugin/manifest.json` | `Schema/plugins/<name>.json` |
| `plugin/Schema/*.md` | `Schema/` |
| `plugin/scripts/*.py` | `scripts/` |
| `plugin/_templates/*.md` | `_templates/` |
| `plugin/_prompts/*.md` | `_prompts/` (receipt-tracked: stock auto-updates, tailored is preserved) |
| `plugin/AGENTS-*.md` | appended once to the vault's `AGENTS.md` (its first heading is the marker) |
| `skills/<skill>/` | `.agents/skills/<skill>/`, then linked into `.claude/skills/` |

Folders created: every `note_types[].folder`, plus `source_subdirs`, plus `install.extra_dirs`.

## Skills belong to the vault

A plugin's skills are installed **into the vault**, never into a global skills directory — a
quiz-authoring or card-populating skill is meaningless in a project with no vault, or a vault
without that plugin. `.agents/skills/` is the canonical copy; `.claude/skills/` holds symlinks to
it because that is the only project location Claude Code reads. **Both are committed**, so a
cloned vault has working skills immediately. If the links are ever missing — a partial checkout,
or a platform where git didn't restore symlinks — `doctor` says so and
`wiki_tool.py skills --link` rebuilds them.

## Rules and behavior

- **Tags and folders must be unique.** A plugin that re-declares a core tag (`topic`,
  `concept`, `entity`, `log`) or collides with another plugin's tag/folder is rejected, and
  `build`/`lint`/`doctor` fail with a clear `PLUGIN:` error until fixed.
- A note type's `tag` participates in the same lint rules as core notes: each compiled note
  carries exactly one allowed tag, has valid `created`/`updated` dates, and keeps
  `source_count == len(sources)`. The only per-type difference is `requires_source`.
- Raw sources may live in subfolders (e.g. `Raw/Sources/cards/black-lotus.md`); the `sources`
  frontmatter list should reference them by path.
- Inspect what's installed with `python3 scripts/wiki_tool.py plugins`. That command also
  doubles as the **capability probe**: a plugin installer can run it to confirm the core is
  plugin-aware before installing.

## Shared plugin code (`scripts/wiki_plugin.py`, `scripts/wiki_notes.py`)

The core template ships two importable modules so plugins don't each reimplement common
capabilities:

- **`scripts/wiki_notes.py`** — note-authoring helpers a plugin's tool script imports as a
  sibling: `slug`, `today`, `rel`, `die`, `emit_frontmatter`/`_scalar`, `existing_created`,
  `write_note`, `read_frontmatter`/`read_title`/`read_section`, the surgical
  `set_frontmatter_fields`/`replace_block`/`update_managed`/`extract_managed_block` editors, and
  `run_gate()` (shells `build`/`lint`/`source-scan`/`source-lint`). Example:
  `from wiki_notes import slug, write_note, run_gate`.
- **`scripts/wiki_plugin.py`** — **`PluginInstaller`**, which performs the entire install from
  the manifest and payload layout below: verify the vault, copy the payload, sync `_prompts/`
  against a per-vault receipt (stock auto-updates, tailored is preserved), install skills and
  link them, create folders, append the AGENTS section, run the gate. Plugins ship **no
  installer code** — `plugins/install-plugins.py` constructs `PluginInstaller(plugin_dir)` and
  calls `run()`. It also exposes `link_skills(vault)` / `unlinked_skills(vault)`, which back
  `wiki_tool.py skills`.

Because these modules live in the vault (installed by the core template), a plugin **requires a
recent-enough core**: the installer capability-probes `scripts/wiki_plugin.py` and each tool
script guards its `wiki_notes` import — both tell the user to update the core (re-copy
`template/.`) if it's missing.

## Removing a plugin

Delete its manifest from `Schema/plugins/` (and, if desired, its folders/notes). The core
note types always remain.

# Command Reference

All tooling is in `scripts/` and uses only the Python standard library. Run from the repo root.

## `wiki_tool.py`

| Command | Mutates? | Description |
|---------|----------|-------------|
| `doctor` | no | Health check: folders, Python version, catalog, manifest, note counts. |
| `build` | yes | Generate `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder `index.md` files. |
| `lint` | no | Validate compiled Wiki note frontmatter, tags, sources, and `source_count`. |
| `source-scan` | no | List Raw sources and their coverage state. |
| `source-scan --update` | yes | Write `Schema/source-manifest.jsonl` from sources + computed coverage. |
| `source-scan --update --accept-covered` | yes | Update manifest, accepting current coverage state. |
| `source-lint` | no | Validate source frontmatter and coverage; fail if processed-but-uncovered. |
| `source-delta` | no | Show Raw sources not represented in the manifest (and stale manifest rows). |
| `source-coverage` | no | Show which Raw sources are covered by compiled Wiki notes. |
| `search-catalog --query "text"` | no | Search compiled notes through the catalog. |
| `log --title "t" --details "d"` | yes | Add a log note under `Wiki/Logs/`. |
| `handover new --title "t"` | yes | Create a session handover under `Wiki/Handovers/`, with the sections to fill in. `--expires-in DAYS` (default 90) sets the expiry; `--link SLUG` (repeatable) seeds the State section. |
| `handover list [--all]` | no | Open and expired handovers, newest first. `--all` includes closed ones. |
| `handover resume <slug>` | yes | Print the handover and mark it `resumed`. |
| `handover close <slug>` | yes | Mark a handover `closed`, so the next `prune` removes it. |
| `handover extend <slug> [--days N]` | yes | Push `expires` out to N days from today (default 90). |
| `handover prune [--dry-run]` | yes | Delete spent handovers. **Closed** ones go (one bulk confirm when interactive). **Expired** ones are confirmed *individually* — delete / extend 90 days / skip — and are **never deleted without a TTY**, since an expired handover was never finished with. `--dry-run` reports and changes nothing. |
| `plugins` | no | List installed plugins and the note types they add. |
| `skills` | no | List the vault's skills and whether each is discoverable by Claude Code. |
| `skills --link` | yes | Rebuild the `.claude/skills/` symlinks from `.agents/skills/`. They're committed, so this is only needed to repair them — or on a platform where git didn't restore symlinks. |
| `skills --link --no-repo-root` | yes | Opt out of the repo-root links. By default, a wiki nested in a project repo links into the *enclosing repo's* `.claude/skills/` as well, so its skills load when the client starts at the project root. No-op either way when the wiki is its own repo root. |
| `gate` | yes | Run the full maintenance gate in one command: `build`, `lint`, `source-lint`, `audit_public.py`. |
| `gate --staged-only` | yes | Same, but exits 0 immediately when nothing under the wiki is staged. This is what a nested wiki's commit gate uses so project commits aren't taxed. |

### Examples

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-scan
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
python3 scripts/wiki_tool.py source-delta
python3 scripts/wiki_tool.py source-coverage
python3 scripts/wiki_tool.py search-catalog --query "navigation"
python3 scripts/wiki_tool.py log --title "Ingest X" --details "Added concept notes from x.md"
python3 scripts/wiki_tool.py plugins
python3 scripts/wiki_tool.py handover new --title "Wire up the exporter" --link export-scheduling
python3 scripts/wiki_tool.py handover list
python3 scripts/wiki_tool.py handover resume wire-up-the-exporter
python3 scripts/wiki_tool.py handover extend wire-up-the-exporter --days 90
python3 scripts/wiki_tool.py handover prune --dry-run
```

Plugins extend the allowed note types via `Schema/plugins/*.json`; see
`Schema/plugin-schema.md`.

## `audit_public.py`

```bash
python3 scripts/audit_public.py
```

Fails on obvious secrets, private keys, machine-local absolute paths, and committed plugin/cache/workspace state.

## Git Hooks

```bash
bash scripts/install_hooks.sh
```

When the wiki **is** the repository, this points `core.hooksPath` at `.githooks/`; the
`pre-commit` hook then runs `wiki_tool.py gate`.

When the wiki is a **subfolder of a project repo**, it deliberately leaves `core.hooksPath`
alone — that setting is repo-wide and would displace the project's own hooks — and instead
prints the line to add to the project's pre-commit hook:

```bash
python3 <wiki>/scripts/wiki_tool.py gate --staged-only || exit 1
```

Pass `--force` to claim `core.hooksPath` for the wiki anyway.

## Maintenance Gate

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

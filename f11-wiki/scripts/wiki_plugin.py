#!/usr/bin/env python3
"""Shared install/lifecycle machinery for LLM Wiki plugins.

This module ships with the core wiki template (scripts/wiki_plugin.py). The plugin installer
imports it *from the target vault*, so the vault's own core governs how it is installed into.

A plugin is **data plus payload** — everything the installer needs comes from the plugin's
`plugin/manifest.json` and the layout of its folder, so plugins ship no installer code of
their own. `PluginInstaller.run()` performs the whole lifecycle:

  * verify the target is a plugin-aware LLM Wiki,
  * copy the code payload (manifest, schema, tool script, templates),
  * sync `_prompts/` templates against a per-vault receipt — auto-updating untouched (stock)
    prompts while preserving tailored ones (asking keep/update/diff in a terminal, else
    notifying),
  * install the plugin's skills into `.agents/skills/` and link them for AI clients,
  * create folders, append the AGENTS section once, and run the post-install gate.

See Schema/plugin-schema.md for the manifest contract and the payload layout.
"""

import difflib
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Where a vault keeps its skills, and where AI clients discover them. `.agents/skills/` is the
# canonical copy; `.claude/skills/` holds symlinks to it, because that is the only project
# location Claude Code reads. Both are committed, so a cloned vault has working skills with no
# setup step; `wiki_tool.py skills --link` rebuilds the links if they're missing.
SKILLS_DIR = Path(".agents") / "skills"
CLAUDE_SKILLS_DIR = Path(".claude") / "skills"


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


def link_skills(vault):
    """Mirror `.agents/skills/<name>/` into `.claude/skills/<name>` as relative symlinks.

    Claude Code discovers project skills only under `.claude/skills/`, and follows symlinks
    there. Creates missing links, repairs broken or mis-pointed ones, and prunes links whose
    target is gone. Never touches a real file or directory that isn't one of our symlinks.

    Returns (linked, repaired, pruned, skipped).
    """
    vault = Path(vault)
    src_root, dst_root = vault / SKILLS_DIR, vault / CLAUDE_SKILLS_DIR
    linked = repaired = pruned = skipped = 0
    if not src_root.is_dir():
        return (0, 0, 0, 0)

    names = sorted(p.name for p in src_root.iterdir() if (p / "SKILL.md").is_file())
    if names:
        dst_root.mkdir(parents=True, exist_ok=True)

    for name in names:
        link = dst_root / name
        # Relative so the vault stays portable when moved or cloned elsewhere.
        target = os.path.join("..", "..", str(SKILLS_DIR), name)
        if link.is_symlink():
            if os.readlink(str(link)) == target and link.exists():
                continue
            link.unlink()
            link.symlink_to(target)
            repaired += 1
        elif link.exists():
            print(f"  skipped .claude/skills/{name} (a real file/directory is in the way)")
            skipped += 1
        else:
            link.symlink_to(target)
            linked += 1

    # Drop links we own whose skill has been uninstalled.
    if dst_root.is_dir():
        for link in sorted(dst_root.iterdir()):
            if link.is_symlink() and not link.exists() and link.name not in names:
                link.unlink()
                pruned += 1

    return (linked, repaired, pruned, skipped)


def unlinked_skills(vault):
    """Return skills present in `.agents/skills/` with no working `.claude/skills/` entry."""
    vault = Path(vault)
    src_root = vault / SKILLS_DIR
    if not src_root.is_dir():
        return []
    missing = []
    for path in sorted(src_root.iterdir()):
        if (path / "SKILL.md").is_file():
            link = vault / CLAUDE_SKILLS_DIR / path.name
            if not link.exists():
                missing.append(path.name)
    return missing


class PluginInstaller:
    """Installs one plugin folder into a vault, driven entirely by its manifest.

    `plugin_dir` is the plugin's root (`plugins/<name>/`), holding `plugin/` (the payload
    copied into the vault) and, optionally, `skills/`. Nothing here is plugin-specific: the
    name, folders, payload files and closing message all come from `plugin/manifest.json`.
    """

    def __init__(self, plugin_dir):
        self.plugin_dir = Path(plugin_dir)
        self.payload = self.plugin_dir / "plugin"
        self.skills_src = self.plugin_dir / "skills"
        manifest_file = self.payload / "manifest.json"
        if not manifest_file.is_file():
            die(f"{self.plugin_dir} is not a plugin (no plugin/manifest.json)")
        try:
            self.manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        except ValueError as exc:
            die(f"{manifest_file}: cannot parse ({exc})")
        self.name = self.manifest.get("name") or self.plugin_dir.name
        self.install_meta = self.manifest.get("install", {})

    # --- Everything below is derived from the manifest / payload layout -------
    @property
    def manifest_name(self):
        return f"{self.name}.json"

    @property
    def summary(self):
        return self.install_meta.get("summary", "")

    @property
    def new_dirs(self):
        """Folders to create: the note types' folders, plus any declared extras."""
        dirs = [nt["folder"] for nt in self.manifest.get("note_types", []) if nt.get("folder")]
        dirs += list(self.manifest.get("source_subdirs", []))
        dirs += list(self.install_meta.get("extra_dirs", []))
        return dirs

    @property
    def agents_snippet(self):
        """The single AGENTS-*.md in the payload, appended to the vault's AGENTS.md."""
        found = sorted(self.payload.glob("AGENTS-*.md"))
        return found[0] if found else None

    @property
    def agents_marker(self):
        """The snippet's first heading — what we look for to avoid appending twice."""
        snippet = self.agents_snippet
        if not snippet:
            return ""
        for line in snippet.read_text(encoding="utf-8").splitlines():
            if line.startswith("#"):
                return line.strip()
        return ""

    def payload_copies(self, vault):
        """[(src, dst)] for the code payload. `_prompts/` is handled by sync_prompts()."""
        copies = [(self.payload / "manifest.json",
                   vault / "Schema" / "plugins" / self.manifest_name)]
        for sub, dest in (("Schema", "Schema"), ("scripts", "scripts"),
                          ("_templates", "_templates")):
            src_dir = self.payload / sub
            if src_dir.is_dir():
                for src in sorted(src_dir.iterdir()):
                    if src.is_file():
                        copies.append((src, vault / dest / src.name))
        return copies

    def post_install_message(self, updating):
        key = "post_update" if updating else "post_install"
        return self.install_meta.get(key) or self.install_meta.get("post_install", "")

    # --- Shared lifecycle ----------------------------------------------------
    def plugin_version(self):
        return self.manifest.get("version", "?")

    def verify_llm_wiki(self, vault):
        wiki_tool = vault / "scripts" / "wiki_tool.py"
        needed = [wiki_tool, vault / "Wiki", vault / "Raw" / "Sources", vault / "Schema"]
        missing = [p for p in needed if not p.exists()]
        if missing:
            die(f"{vault} is not an LLM Wiki (missing "
                f"{', '.join(str(m.relative_to(vault)) for m in missing)}). "
                "Run llm-wiki-core on this folder first.")
        probe = subprocess.run([sys.executable, str(wiki_tool), "plugins"],
                               capture_output=True, text=True)
        if probe.returncode != 0:
            die("this LLM Wiki core does not support plugins. Update it from llm-wiki-core "
                "(the core needs the `plugins` command and a plugin-aware wiki_tool.py).")

    def copy_payload(self, vault):
        for src, dst in self.payload_copies(vault):
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            print(f"  installed {dst.relative_to(vault)}")

    # --- Prompt sync (per-vault receipt) -------------------------------------
    @staticmethod
    def sha256_file(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    def receipt_path(self, vault):
        return vault / "Schema" / "plugins" / f"{self.name}.prompts.json"

    def read_receipt(self, vault):
        path = self.receipt_path(vault)
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8")).get("prompts", {})
        except (OSError, ValueError):
            return {}

    def write_receipt(self, vault, prompts):
        path = self.receipt_path(vault)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(
            {"plugin": self.name, "version": self.plugin_version(), "prompts": prompts},
            indent=2) + "\n", encoding="utf-8")

    @staticmethod
    def classify_prompt(dst_exists, vault_hash, shipped_hash, receipt_hash):
        """Decide what to do with one prompt. Pure — no I/O.

        Returns: install | up_to_date | update_stock | update_available | customized.
        """
        if not dst_exists:
            return "install"
        if vault_hash == shipped_hash:
            return "up_to_date"
        if receipt_hash is not None and vault_hash == receipt_hash:
            return "update_stock"       # untouched since install, but bundled moved on
        if shipped_hash != receipt_hash:
            return "update_available"   # tailored (or no receipt) AND a newer bundle exists
        return "customized"             # tailored, bundled unchanged since install

    @staticmethod
    def _prompt_resolve(name, dst, src):
        """Interactively resolve a tailored prompt with an available update. True = update."""
        while True:
            ans = input(f"  '_prompts/{name}' is customized; a newer bundled version exists. "
                        "[k]eep / [u]pdate / [d]iff? ").strip().lower()
            if ans in ("", "k", "keep"):
                return False
            if ans in ("u", "update"):
                return True
            if ans in ("d", "diff"):
                diff = difflib.unified_diff(
                    dst.read_text(encoding="utf-8").splitlines(),
                    src.read_text(encoding="utf-8").splitlines(),
                    fromfile=f"{name} (your copy)", tofile=f"{name} (bundled)", lineterm="")
                print("\n".join(diff) or "  (no textual difference)")

    def sync_prompts(self, vault, interactive, force_update, keep):
        src_dir = self.payload / "_prompts"
        if not src_dir.is_dir():
            return
        receipt = self.read_receipt(vault)
        counts = {"installed": 0, "updated": 0, "current": 0, "preserved": 0}
        pending = []

        for src in sorted(src_dir.glob("*.md")):
            name = src.name
            dst = vault / "_prompts" / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shipped_hash = self.sha256_file(src)
            receipt_hash = receipt.get(name, {}).get("hash")
            vault_hash = self.sha256_file(dst) if dst.exists() else None
            action = self.classify_prompt(dst.exists(), vault_hash, shipped_hash, receipt_hash)

            def install(tag):
                shutil.copyfile(src, dst)
                receipt[name] = {"hash": shipped_hash, "version": self.plugin_version()}
                print(f"  {tag} _prompts/{name}")

            if action == "install":
                install("installed"); counts["installed"] += 1
            elif action == "up_to_date":
                receipt[name] = {"hash": shipped_hash, "version": self.plugin_version()}
                counts["current"] += 1
            elif action == "update_stock":
                install("updated (stock)"); counts["updated"] += 1
            elif action == "customized":
                print(f"  preserved _prompts/{name} (customized)"); counts["preserved"] += 1
            else:  # update_available
                if force_update:
                    install("updated (--update-prompts)"); counts["updated"] += 1
                elif keep:
                    print(f"  preserved _prompts/{name} (customized; update available)")
                    counts["preserved"] += 1; pending.append(name)
                elif interactive and self._prompt_resolve(name, dst, src):
                    install("updated"); counts["updated"] += 1
                elif interactive:
                    print(f"  preserved _prompts/{name} (kept your version)")
                    counts["preserved"] += 1
                else:
                    print(f"  preserved _prompts/{name} (customized; update available)")
                    counts["preserved"] += 1; pending.append(name)

        self.write_receipt(vault, receipt)
        print(f"  prompts: {counts['installed']} installed, {counts['updated']} updated, "
              f"{counts['current']} up to date, {counts['preserved']} preserved")
        if pending:
            print(f"  note: {len(pending)} tailored prompt(s) have a newer bundled version "
                  f"({', '.join(pending)}). Re-run in a terminal to review (keep/update/diff), "
                  "or pass --update-prompts to overwrite.")

    def make_dirs(self, vault):
        for d in self.new_dirs:
            path = vault / d
            path.mkdir(parents=True, exist_ok=True)
            if not any(path.iterdir()):
                (path / ".gitkeep").touch()

    def install_skills(self, vault):
        """Copy the plugin's skills into the vault, then link them for AI clients.

        Skills live with the wiki they act on, not in a global skills directory: a quiz or
        card-populating skill is meaningless in a project that has no vault, or a vault
        without this plugin.
        """
        if not self.skills_src.is_dir():
            return
        names = sorted(p.name for p in self.skills_src.iterdir() if (p / "SKILL.md").is_file())
        for name in names:
            dst = vault / SKILLS_DIR / name
            if dst.exists():
                shutil.rmtree(dst)     # replace wholesale: skills are ours, not user-edited
            shutil.copytree(self.skills_src / name, dst)
            print(f"  installed {SKILLS_DIR}/{name}")
        if names:
            linked, repaired, _pruned, skipped = link_skills(vault)
            detail = f"{linked} linked, {repaired} repaired"
            if skipped:
                detail += f", {skipped} skipped"
            print(f"  skills: {len(names)} installed ({CLAUDE_SKILLS_DIR}: {detail})")

    def update_agents(self, vault):
        agents = vault / "AGENTS.md"
        if not self.agents_snippet:
            return
        snippet = Path(self.agents_snippet).read_text(encoding="utf-8").strip()
        if agents.exists():
            text = agents.read_text(encoding="utf-8")
            if self.agents_marker in text:
                print(f"  AGENTS.md already documents the {self.name} plugin (skipped)")
                return
            agents.write_text(text.rstrip() + "\n\n" + snippet + "\n", encoding="utf-8")
        else:
            agents.write_text(snippet + "\n", encoding="utf-8")
        print("  updated AGENTS.md")

    def run_gate(self, vault):
        wiki_tool = vault / "scripts" / "wiki_tool.py"
        for step in (["plugins"], ["doctor"], ["build"]):
            proc = subprocess.run([sys.executable, str(wiki_tool)] + step)
            if proc.returncode != 0:
                die(f"post-install check failed: wiki_tool.py {' '.join(step)}")

    def run(self, vault, update_prompts=False, keep_prompts=False):
        vault = Path(vault).resolve()
        if not vault.is_dir():
            die(f"{vault} is not a directory")
        updating = (vault / "Schema" / "plugins" / self.manifest_name).exists()
        verb = "Updating" if updating else "Installing"
        prep = "in" if updating else "into"
        print(f"{verb} {self.name} plugin {prep} {vault}")
        self.verify_llm_wiki(vault)
        self.copy_payload(vault)
        self.sync_prompts(vault, interactive=sys.stdin.isatty(),
                          force_update=update_prompts, keep=keep_prompts)
        self.install_skills(vault)
        self.make_dirs(vault)
        self.update_agents(vault)
        self.run_gate(vault)
        msg = self.post_install_message(updating)
        if msg:
            print("\n" + msg)
        return 0

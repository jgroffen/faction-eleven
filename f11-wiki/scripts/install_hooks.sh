#!/usr/bin/env bash
# Wire up the LLM Wiki pre-commit gate.
#
# If the wiki IS the repository, this points core.hooksPath at the wiki's .githooks/.
# If the wiki is a SUBFOLDER of a larger project repo, it leaves core.hooksPath alone — that
# setting is repo-wide, and claiming it would displace the project's own hooks. Instead it
# prints the one line to add to the project's pre-commit hook. Pass --force to claim it anyway.
set -euo pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FORCE="${1:-}"

if ! REPO="$(git -C "$VAULT" rev-parse --show-toplevel 2>/dev/null)"; then
  echo "error: $VAULT is not inside a git repository." >&2
  exit 1
fi

chmod +x "$VAULT/.githooks/pre-commit" 2>/dev/null || true

if [ "$VAULT" = "$REPO" ]; then
  git -C "$REPO" config core.hooksPath .githooks
  echo "Installed: core.hooksPath -> .githooks"
  echo "The pre-commit hook runs: build, lint, source-lint, audit_public."
  exit 0
fi

PREFIX="${VAULT#"$REPO"/}"          # vault path relative to the repo root

if [ "$FORCE" = "--force" ]; then
  git -C "$REPO" config core.hooksPath "$PREFIX/.githooks"
  echo "Installed: core.hooksPath -> $PREFIX/.githooks"
  echo "Note: core.hooksPath is repo-wide, so this now governs ALL commits in $REPO."
  exit 0
fi

cat <<EOF
This wiki is a subfolder of $REPO, so core.hooksPath was left alone — it is repo-wide, and
claiming it would displace the project's own hooks.

To run the wiki gate from the project's own pre-commit hook, add this line to it:

    python3 $PREFIX/scripts/wiki_tool.py gate --staged-only || exit 1

It exits immediately when a commit touches nothing under $PREFIX/, so ordinary code commits are
unaffected. To run the gate by hand at any time:

    python3 $PREFIX/scripts/wiki_tool.py gate

Re-run with --force if you do want the wiki to own core.hooksPath for the whole repo.
EOF

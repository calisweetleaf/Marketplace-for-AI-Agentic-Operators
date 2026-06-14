#!/usr/bin/env bash
# CTMv3 opencode adapter installer
#
# Usage:
#   bash install.sh            # project scope: installs to .opencode/ in $PWD
#   bash install.sh global     # global scope: installs to ~/.config/opencode/
#
# The adapter consists of:
#   - agent/ctmv3-architect.md      -> <target>/agents/
#   - command/ctmv3-status.md       -> <target>/commands/
#   - plugin/ctmv3.ts               -> <target>/plugins/
#
# Note: opencode uses 'agents/' and 'commands/' and 'plugins/' (plural) as the
# directory names under both .opencode/ and ~/.config/opencode/.
# See: https://opencode.ai/docs/agents, /docs/commands, /docs/plugins

set -euo pipefail

SCOPE="${1:-project}"

if [ "$SCOPE" = "global" ]; then
  TARGET="$HOME/.config/opencode"
else
  TARGET="$PWD/.opencode"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ---------------------------------------------------------------------------
# Helper: verify a source file exists, then copy it; exit clearly on failure
# ---------------------------------------------------------------------------
safe_cp() {
  local src="$1"
  local dest="$2"
  if [ ! -e "$src" ]; then
    echo "ERROR: source file not found: $src" >&2
    exit 1
  fi
  cp "$src" "$dest" || { echo "ERROR: failed to copy $src to $dest" >&2; exit 1; }
}

# ---------------------------------------------------------------------------
# Confirmation prompt for global-scope installs (writes into user home)
# ---------------------------------------------------------------------------
if [ "$SCOPE" = "global" ]; then
  echo "Installing CTMv3 opencode adapter to: $TARGET (scope: global)"
  printf "This will write files into %s. Continue? [y/N] " "$TARGET"
  read -r _confirm
  case "$_confirm" in
    [yY]|[yY][eE][sS]) ;;
    *)
      echo "Aborted - no files written."
      exit 0
      ;;
  esac
else
  echo "Installing CTMv3 opencode adapter to: $TARGET (scope: $SCOPE)"
fi

# Create target directories
mkdir -p "$TARGET/agents"   || { echo "ERROR: could not create $TARGET/agents" >&2; exit 1; }
mkdir -p "$TARGET/commands" || { echo "ERROR: could not create $TARGET/commands" >&2; exit 1; }
mkdir -p "$TARGET/plugins"  || { echo "ERROR: could not create $TARGET/plugins" >&2; exit 1; }

# Install agent
echo "  -> agents/ctmv3-architect.md"
safe_cp "$SCRIPT_DIR/agent/ctmv3-architect.md" "$TARGET/agents/"

# Install command surface
echo "  -> commands/ctmv3-status.md"
safe_cp "$SCRIPT_DIR/command/ctmv3-status.md" "$TARGET/commands/"

# Install plugin
echo "  -> plugins/ctmv3.ts"
safe_cp "$SCRIPT_DIR/plugin/ctmv3.ts" "$TARGET/plugins/"

echo ""
echo "Installation complete."
echo ""
echo "Verify opencode recognizes the adapter by running opencode and checking:"
echo "  - /ctmv3-status is available as a command"
echo "  - @ctmv3-architect is available as a subagent"
echo ""
echo "Verify Python engine is installed:"
if python3 -m ctmv3 version 2>/dev/null; then
  echo "  ctmv3 engine: OK"
else
  echo "  ctmv3 engine: NOT FOUND"
  echo "  Install the engine before using CTMv3 commands."
  echo "  See the sibling core/ directory in this plugin checkout for source."
fi

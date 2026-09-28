#!/usr/bin/env bash
# Run every check on a project root (default: the repository root).
#   checks/run.sh [root] [--baseline <previous report.json> | --first]   full run: page sampler (Node + Playwright) then every rule (Python)
#   SKIP_PAGE=1 checks/run.sh ...                                          reuse an existing out/checks/page.json
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "${1:-$HERE/..}" && pwd)"
shift || true
export NODE_PATH="${NODE_PATH:-$HERE/../node_modules:$(npm root -g 2>/dev/null || true)}"
if [ -z "${SKIP_PAGE:-}" ]; then
  if [ -f "$ROOT/out/page.json" ]; then
    node "$HERE/page/sampler.js" "$ROOT" || echo "page sampler failed: page rules will be MISSING"
  else
    echo "no out/page.json: page rules will be MISSING"
  fi
fi
python3 "$HERE/py/run.py" "$ROOT" "$@"

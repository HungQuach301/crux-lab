#!/usr/bin/env bash
# Crux factory: one command from episode.yaml to master + parts + Shorts + qc (toolkit/factory/build.py).
#   bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache]
set -euo pipefail
[ $# -ge 1 ] || { echo "usage: toolkit/build.sh <episode.yaml> [options]"; exit 2; }
exec python3 "$(dirname "$0")/factory/build.py" "$@"

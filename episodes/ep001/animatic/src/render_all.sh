#!/bin/bash
# Render scenes one after another (pass scene ids, default S01..S20); logs to ../work/logs/<S>.txt
# Needs THREE_DIR, NODE_PATH, PLAYWRIGHT_BROWSERS_PATH (see README "Dựng lại").
cd "$(dirname "$0")"
mkdir -p ../work/logs
S="$@"; [ -z "$S" ] && S=$(seq -f 'S%02g' 1 20)
for s in $S; do node render.js $s > ../work/logs/$s.txt 2>&1 || echo "FAILED $s" >> ../work/logs/failed.txt; done

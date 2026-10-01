#!/bin/bash
# Render clips, at most 2 Chromium processes in parallel (brief: <= 2 per direction).
#   THREE_DIR=<tmp>/node_modules/three/build src/run2.sh K1 K2 K3 ...
cd "$(dirname "$0")/.." && mkdir -p work
export NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules} PLAYWRIGHT_BROWSERS_PATH=${PLAYWRIGHT_BROWSERS_PATH:-/opt/pw-browsers}
printf '%s\n' "$@" | xargs -P 2 -I{} sh -c 'node src/render.js {} > work/log-{}.txt 2>&1; echo "{} exit $?"'

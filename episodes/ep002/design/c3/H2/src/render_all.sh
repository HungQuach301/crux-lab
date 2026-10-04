#!/bin/sh
# Render all H2 style frames, two Chromium processes at a time (brief: max 2 parallel renders per direction).
cd "$(dirname "$0")/.." || exit 1
export NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
( for k in K1 K5 K4 K7; do node src/render.js $k 2>&1 | tail -1; done ) > work/render-a.log 2>&1 &
( for k in K2 K3 K6; do node src/render.js $k 2>&1 | tail -1; done ) > work/render-b.log 2>&1 &
wait
node src/render.js THUMB --thumb

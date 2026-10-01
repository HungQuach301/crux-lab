#!/bin/bash
# Render scenes in up to 3 parallel queues (brief: at most 3 render processes); one line per finished scene to PROGRESS.md.
#   src/render_all.sh [S01 ...]   (default: all 13)
cd "$(dirname "$0")/.."
export NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
mkdir -p work/logs
S="$@"; [ -z "$S" ] && S="S07 S10 S09 S03 S08 S05 S04 S06 S02 S12 S01 S11 S13"
q=(); i=0; for s in $S; do q[$((i % 3))]+="$s "; i=$((i+1)); done
for k in 0 1 2; do
  ( for s in ${q[$k]}; do
      if node src/render.js $s > work/logs/$s.txt 2>&1; then echo "- $(date +%d/%m\ %H:%M) $s dựng xong: $(tail -1 work/logs/$s.txt | cut -c1-160)" >> PROGRESS.md
      else echo "- $(date +%d/%m\ %H:%M) $s LỖI dựng (work/logs/$s.txt)" >> PROGRESS.md; fi
    done ) &
done
wait

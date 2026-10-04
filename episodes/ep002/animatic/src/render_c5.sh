#!/bin/bash
# C5 final picture: 3 parallel queues (brief: at most 3 render processes); one line per finished scene to ../PROGRESS.md.
cd "$(dirname "$0")"
export NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules} PLAYWRIGHT_BROWSERS_PATH=${PLAYWRIGHT_BROWSERS_PATH:-/opt/pw-browsers}
L=../work/c5/logs; mkdir -p $L
S="$@"; [ -z "$S" ] && S="S10 S07 S09 S03 S08 S05 S04 S06 S02 S12 S01 S11 S13"
q=(); i=0; for s in $S; do q[$((i % 3))]+="$s "; i=$((i+1)); done
for k in 0 1 2; do ( for s in ${q[$k]}; do
  if node render_c5.js $s > $L/$s.txt 2>&1; then echo "- $(date +%d/%m\ %H:%M) C5 $s 1080p xong ($(tail -1 $L/$s.txt))" >> ../PROGRESS.md; else echo "- $(date +%d/%m\ %H:%M) C5 $s LỖI (work/c5/logs/$s.txt)" >> ../PROGRESS.md; fi
done ) & done; wait

#!/usr/bin/env bash
# A29 (K4.4): page.json của bộ lấy mẫu trang có cache theo đoạn so với --no-cache, cùng trang + cùng master.
#   bash checks-runs/K44/a29/run_a29.sh <ep> <tag> [--no-cache] [--clear]
# Ghi bản sao page.json vào $OUT/<ep>-<tag>.json, thời gian và số hit vào $OUT/<ep>-<tag>.log
set -euo pipefail
EP="$1"; TAG="$2"; shift 2
ROOT=/home/user/crux-lab; OUT="${A29_OUT:-$ROOT/../a29-out}"; mkdir -p "$OUT"
R="$ROOT/episodes/$EP"
NOC=""; for a in "$@"; do [ "$a" = "--no-cache" ] && NOC="--no-cache"; [ "$a" = "--clear" ] && rm -rf "$R/out/checks/cache/page-scenes"; done
export NODE_PATH="$(npm root -g)"
s=$(date +%s)
K_PROGRESS=1 node "${A29_CHECKS:-/home/user/k441/checks}/page/sampler.js" "$R" --jobs 4 $NOC > "$OUT/$EP-$TAG.stdout" 2> "$OUT/$EP-$TAG.log"
cp "$R/out/checks/page.json" "$OUT/$EP-$TAG.json"
echo "{\"ep\":\"$EP\",\"tag\":\"$TAG\",\"wall_s\":$(( $(date +%s) - s ))}" >> "$OUT/runs.jsonl"

#!/usr/bin/env bash
# Tập 3 · C5: checks đủ bộ trên bản sao khoá (git archive HEAD + file không commit: dữ liệu ghim, video, stem), LOCK tính lại phải trùng checks/LOCK.
#   bash episodes/ep003/design/c5/checks.sh <outdir> [--baseline <report.json> | --first]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../../../.." && pwd)"; OUT="$1"; shift
rm -rf "$OUT"; mkdir -p "$OUT"
git -C "$REPO" archive HEAD | tar -x -C "$OUT"
E=episodes/ep003
for f in data/TB3MS.csv data/CPIAUCNS.csv data/DTB3.csv data/DTB3_monthly.csv out/video.mp4; do cp "$REPO/$E/$f" "$OUT/$E/$f"; done
mkdir -p "$OUT/$E/out/audio/stems" "$OUT/$E/design/c3/work" && cp "$REPO/$E"/out/audio/stems/*.flac "$OUT/$E/out/audio/stems/" && cp "$REPO/$E/design/c3/work/data.js" "$OUT/$E/design/c3/work/"
L=$(cd "$OUT/checks" && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
[ "$L" = "$(cat "$OUT/checks/LOCK")" ] || { echo "LOCK mismatch $L"; exit 2; }
echo "LOCK $L ok"
# the page is served from the copy (same files as HEAD)
sed -i "s#http://127.0.0.1:8765/#http://127.0.0.1:8766/#" "$OUT/$E/out/page.json"
(cd "$OUT" && python3 -m http.server 8766 >/dev/null 2>&1 & echo $! > "$OUT/.srv")
sleep 1
bash "$OUT/checks/run.sh" "$OUT/$E" "$@" || true
kill "$(cat "$OUT/.srv")" || true

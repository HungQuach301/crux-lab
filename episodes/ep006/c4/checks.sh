#!/usr/bin/env bash
# Tập 6 · C4/C5: checks ĐỦ BỘ trên bản sao khoá (mẫu episodes/ep003/design/c5/checks.sh). Bản sao = git archive HEAD + thay đổi chưa commit của
# cây làm việc (tracked đã sửa + untracked không bị ignore) + file không commit mà luật cần (dữ liệu FRED ghim, video, stem, trang kiểm một-file,
# dữ liệu thế giới). LOCK tính lại trên checks/ của bản sao phải trùng checks/LOCK và contract.json lock. Trang kiểm mở bằng file:// (không máy chủ).
#   bash episodes/ep006/c4/checks.sh <outdir> [--first | --baseline <report.json>]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"; OUT="$1"; shift
E=episodes/ep006
rm -rf "$OUT"; mkdir -p "$OUT"
git -C "$REPO" archive HEAD | tar -x -C "$OUT"
( cd "$REPO" && { git diff --name-only HEAD; git ls-files --others --exclude-standard; } | sort -u | while read -r f; do
    if [ -e "$f" ]; then mkdir -p "$OUT/$(dirname "$f")"; cp -p "$f" "$OUT/$f"; else rm -f "$OUT/$f"; fi; done )
for f in data/raw data/normalized out/video.mp4 out/audio work/factory/page/index.html work/world-data work/factory/SH1.mp4 work/factory/SH2.mp4 work/factory/SH3.mp4 work/factory/page; do
  [ -e "$REPO/$E/$f" ] || continue; mkdir -p "$OUT/$E/$(dirname "$f")"; cp -rp "$REPO/$E/$f" "$OUT/$E/$f"; done
L=$(cd "$OUT/checks" && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
[ "$L" = "$(cat "$OUT/checks/LOCK")" ] || { echo "LOCK mismatch $L"; exit 2; }
python3 -c "import json,sys; c=json.load(open('$OUT/$E/contract.json')); sys.exit(0 if c['lock']=='$L' else 3)" || { echo "contract.json lock ≠ checks/LOCK"; exit 3; }
echo "LOCK $L ok (checks/LOCK = contract.json lock)"
bash "$OUT/checks/run.sh" "$OUT/$E" --contract "$OUT/$E/contract.json" "$@" || true

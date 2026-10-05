#!/usr/bin/env bash
# Mở phiên (Mốc B): kiểm công cụ + nhánh đúng lệnh. Không sửa gì.
#   bash toolkit/verify.sh <nhánh-lệnh-ghi>        ví dụ: bash toolkit/verify.sh ep004
# Thoát 0 khi mọi mục ĐẠT; 1 khi có mục TRƯỢT (in ra bảng). Nhánh do lệnh của chủ dự án/prompt ghi, không tự đặt.
set -u
WANT="${1:-}"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
fail=0; row() { printf '%-24s | %s | %s\n' "$1" "$2" "$3"; if [ "$2" = "TRƯỢT" ]; then fail=1; fi; return 0; }
have() { command -v "$1" >/dev/null 2>&1; }
echo "verify.sh — $(date -u +%FT%TZ) — $ROOT"
for c in git node python3 ffmpeg ffprobe; do have "$c" && row "$c" "ĐẠT" "$($c --version 2>&1 | head -1 | cut -c1-60)" || row "$c" "TRƯỢT" "không có"; done
NP="$(npm root -g 2>/dev/null)"; [ -d "$NP/playwright" ] && row "playwright (NODE_PATH)" "ĐẠT" "$NP" || row "playwright (NODE_PATH)" "TRƯỢT" "không thấy ở npm root -g"
[ -x /opt/pw-browsers/chromium ] || ls /opt/pw-browsers 2>/dev/null | grep -q chromium && row "chromium" "ĐẠT" "/opt/pw-browsers" || row "chromium" "TRƯỢT" "không thấy /opt/pw-browsers"
for m in numpy scipy requests yaml faster_whisper; do python3 -c "import $m" 2>/dev/null && row "py:$m" "ĐẠT" "" || row "py:$m" "TRƯỢT" "pip install"; done
# nhánh
CUR="$(git rev-parse --abbrev-ref HEAD)"
if [ -z "$WANT" ]; then row "nhánh" "TRƯỢT" "thiếu đối số: nhánh do lệnh ghi (đang ở $CUR)"
elif [ "$CUR" = "$WANT" ]; then row "nhánh" "ĐẠT" "$CUR"
else row "nhánh" "TRƯỢT" "đang ở $CUR, lệnh ghi $WANT (git checkout $WANT, hoặc git checkout -b $WANT origin/main nếu là nhánh mới)"; fi
git fetch -q origin main 2>/dev/null && { B=$(git rev-list --count HEAD..origin/main); [ "$B" = 0 ] && row "main mới nhất" "ĐẠT" "$(git rev-parse --short origin/main)" || row "main mới nhất" "TRƯỢT" "thiếu $B commit của origin/main (merge hoặc rebase theo lệnh)"; } || row "fetch origin" "TRƯỢT" "không fetch được"
[ -z "$(git status --porcelain)" ] && row "cây sạch" "ĐẠT" "" || row "cây sạch" "TRƯỢT" "có thay đổi chưa commit"
# khoá luật
L=$(cd checks && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
[ "$L" = "$(cat checks/LOCK)" ] && row "checks/LOCK" "ĐẠT" "${L:0:12}…" || row "checks/LOCK" "TRƯỢT" "LOCK không khớp nội dung checks/"
# đĩa
AV=$(df -Pm "$ROOT" | awk 'NR==2{print $4}'); [ "$AV" -ge 5000 ] && row "đĩa trống" "ĐẠT" "${AV} MB" || row "đĩa trống" "TRƯỢT" "${AV} MB < 5 GB"
exit $fail

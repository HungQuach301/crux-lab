#!/usr/bin/env bash
# Mở phiên (Mốc B): kiểm công cụ + nhánh đúng lệnh. Không sửa gì (trừ khi --install).
#   bash toolkit/verify.sh <nhánh-lệnh-ghi>        ví dụ: bash toolkit/verify.sh ep004
#   bash toolkit/verify.sh <nhánh> --install [episodes/epNNN]   F-15 (TONGKET Tập 7 p; cine-lab #66): cài đồ ngoài git của container mới —
#        three.js (`npm ci` ở world/vendor), PyAV ghim tương thích faster-whisper (thử nhận dạng thật, hỏng → av==14.2.0), và với tập:
#        dữ liệu (`data/fetch.py --verify`), nhạc nền `audio.music` (`music_cmd` trên timeline đã commit; chưa có timeline → `*/build_inputs.py
#        --timeline`). Mỗi mục một dòng bảng.
# Luôn có: MỘT lần nhận dạng thử (faster-whisper small.en trên một take giọng có trong repo) — import được chưa đủ (cine-lab #66).
# Thoát 0 khi mọi mục ĐẠT; 1 khi có mục TRƯỢT (in ra bảng). Nhánh do lệnh của chủ dự án/prompt ghi, không tự đặt.
set -uo pipefail   # F-15: pipefail ở mọi script cổng (test_factory_f15)
WANT="${1:-}"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
INSTALL=0; EP=""; [ "${2:-}" = "--install" ] && { INSTALL=1; EP="${3:-}"; }
fail=0; row() { printf '%-24s | %s | %s\n' "$1" "$2" "$3"; if [ "$2" = "TRƯỢT" ]; then fail=1; fi; return 0; }
have() { command -v "$1" >/dev/null 2>&1; }
echo "verify.sh — $(date -u +%FT%TZ) — $ROOT"
for c in git node python3 ffmpeg ffprobe; do have "$c" && row "$c" "ĐẠT" "$($c --version 2>&1 | head -1 | cut -c1-60)" || row "$c" "TRƯỢT" "không có"; done
NP="$(npm root -g 2>/dev/null)"; [ -d "$NP/playwright" ] && row "playwright (NODE_PATH)" "ĐẠT" "$NP" || row "playwright (NODE_PATH)" "TRƯỢT" "không thấy ở npm root -g"
{ [ -x /opt/pw-browsers/chromium ] || compgen -G '/opt/pw-browsers/chromium*' >/dev/null; } && row "chromium" "ĐẠT" "/opt/pw-browsers" || row "chromium" "TRƯỢT" "không thấy /opt/pw-browsers"
for m in numpy scipy requests yaml faster_whisper; do python3 -c "import $m" 2>/dev/null && row "py:$m" "ĐẠT" "" || row "py:$m" "TRƯỢT" "pip install"; done
# ---- F-15: đồ ngoài git (cài khi --install) + nhận dạng thử
V="toolkit/factory/world/vendor"
if [ ! -f "$V/node_modules/three/build/three.module.js" ] && [ $INSTALL = 1 ]; then (cd "$V" && npm ci --silent >/dev/null 2>&1); fi
[ -f "$V/node_modules/three/build/three.module.js" ] && row "three.js (vendor)" "ĐẠT" "$(node -p "require('./$V/node_modules/three/package.json').version" 2>/dev/null)" \
  || row "three.js (vendor)" "TRƯỢT" "cd $V && npm ci   (hoặc verify.sh <nhánh> --install)"
asr_try() {   # một lần nhận dạng thật: take giọng đầu tiên có trong repo, 12 s đầu; ĐẠT khi ≥ 70 % từ của văn bản take xuất hiện
  timeout 600 python3 - "$@" <<'PY' 2>&1 | tail -1
import glob, json, re, subprocess, sys, tempfile
takes = sorted(glob.glob('episodes/*/voice-takes/*.mp3'))
if not takes: print('SKIP không có take'); sys.exit(0)
mp3 = takes[-1]; meta = json.load(open(mp3[:-4] + '.json')); want = re.findall(r"[a-z]+", (meta.get('text') or '').lower())
wav = tempfile.mktemp(suffix='.wav'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-t', '12', '-i', mp3, wav], check=True)
from faster_whisper import WhisperModel
m = WhisperModel('small.en', device='cpu', compute_type='int8')
try:
    got = ' '.join(s.text for s in m.transcribe(wav)[0]).lower()   # đường của checks/py/common.py: tệp → av.open (lỗi PyAV lộ ở đây)
except TypeError as e:
    print('AV', e); sys.exit(4)
# take ghi số bằng chữ ("three hundred…"), ASR ra chữ số → đo chiều ASR → văn bản: từ chữ cái ≥ 3 ký tự của bản nhận dạng có trong văn bản take
heard = [w for w in re.findall(r"[a-z]+", got) if len(w) >= 3]
hit = sum(w in set(want) for w in heard) / max(1, len(heard))
print(f'{"OK" if hit >= 0.7 else "LOW"} {hit:.0%} "{got.strip()[:60]}"'); sys.exit(0 if hit >= 0.7 else 5)
PY
}
A=$(asr_try)
if echo "$A" | grep -q '^AV' && [ $INSTALL = 1 ]; then pip install -q 'av==14.2.0' >/dev/null 2>&1 && A=$(asr_try); fi
case "$A" in OK*|SKIP*) row "ASR thử (small.en)" "ĐẠT" "av $(python3 -c 'import av;print(av.__version__)' 2>/dev/null) · ${A:0:60}";;
  *) row "ASR thử (small.en)" "TRƯỢT" "${A:0:60} — PyAV ≠ faster-whisper: verify.sh <nhánh> --install (ghim av==14.2.0)";; esac
if [ -n "$EP" ]; then
  if [ -f "$EP/data/fetch.py" ]; then
    if out=$(timeout 300 python3 "$EP/data/fetch.py" --verify 2>&1); then row "dữ liệu tập (fetch)" "ĐẠT" "$EP/data"
    else row "dữ liệu tập (fetch)" "TRƯỢT" "$(echo "$out" | tail -1 | cut -c1-70)"; fi
  fi
  bed=$(python3 -c "import yaml,sys; a=(yaml.safe_load(open('$EP/episode.yaml')).get('audio') or {}); print(a.get('music') or '')" 2>/dev/null)
  if [ -n "$bed" ]; then
    if [ ! -f "$EP/$bed" ]; then
      # có out/factory/timeline.json (đã commit) → music_cmd của tập, không ghi tệp nào trong git; chưa có → */build_inputs.py --timeline
      bi=$(ls "$EP"/*/build_inputs.py 2>/dev/null | tail -1)
      if [ ! -f "$EP/out/factory/timeline.json" ] && [ -n "$bi" ]; then python3 "$bi" --timeline >/dev/null 2>&1
      else python3 - "$EP" <<'PY' >/dev/null 2>&1
import json, os, subprocess, sys, yaml
ep = sys.argv[1]; Y = yaml.safe_load(open(os.path.join(ep, 'episode.yaml'))); A = Y['audio']
tl = json.load(open(os.path.join(ep, 'out', 'factory', 'timeline.json')))
subprocess.run(A['music_cmd'].format(total=tl['total'], out=os.path.join(ep, A['music'])), shell=True, check=True)
PY
      fi
    fi
    [ -f "$EP/$bed" ] && row "nhạc nền tập" "ĐẠT" "$bed $(sha256sum "$EP/$bed" | cut -c1-12)…" || row "nhạc nền tập" "TRƯỢT" "$bed thiếu (build_inputs --timeline / music_cmd)"
  fi
fi
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

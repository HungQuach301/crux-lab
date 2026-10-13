#!/usr/bin/env bash
# F-15 (f) · clip thử footage 540p 8 s. Chạy từ gốc repo: bash toolkit/factory/f15/footage-trial/run.sh
#   1. ảnh: assets/loc.jpg nếu đã tải (`fetch.py <mục LoC> --loc …`, cần mạng cho www.loc.gov + tile.loc.gov); chưa có → ẢNH THAY THẾ = khung
#      thế giới 3D của chính cảnh này (tự dựng, không phải tư liệu), ghi rõ trên chú thích và trong REPORT
#   2. bản đồ: map.py (Census qua us-atlas + Natural Earth) → seg/map.json (+ giờ hiện)
#   3. render_shots.js 540 → out/footage-trial-540.mp4; 4. kiểm: hộp chữ ∩ hộp chủ thể = 0, nhãn hiện ≥ mốc từ và ≤ mốc + 0,2 s
set -euo pipefail
R="$(cd "$(dirname "$0")/../../../.." && pwd)"; cd "$R"
H=toolkit/factory/f15/footage-trial; A=$H/assets; S=$H/seg; mkdir -p $H/out
export NODE_PATH="$(npm root -g)"
python3 toolkit/factory/guard.py >/dev/null || { echo "còn build/render — chờ"; exit 3; }
if [ -f $A/loc.jpg ]; then
  python3 - "$S/plate.json" <<'PY'
import json, sys
json.dump({'src': '/toolkit/factory/f15/footage-trial/assets/loc.jpg', 'subject': [0.30, 0.18, 0.72, 0.80], 'zoom': [1.0, 1.12], 'anchor': [0.5, 0.40],
           't0': 1.0, 't1': 5.2, 'fade': [1.2, 1.0], 'caption': 'Archive photo', 'source': 'Photo: Library of Congress', 'key': 'plate-loc'},
          open(sys.argv[1], 'w'), indent=1)
PY
else
  rm -f $S/plate.json $S/map.json; mv $S/inputs.json $S/inputs.json.hold
  node toolkit/factory/world/render_shots.js $S 1080 $H/out/still.mp4 --stills 0.4 --stills-dir $A >/dev/null
  mv $S/inputs.json.hold $S/inputs.json; mv $A/seg-t0.40.png $A/standin.png
  python3 - "$S/plate.json" <<'PY'
import json, sys
# chủ thể = ngôi nhà + người (đo trên khung 1080 của ảnh thay thế: x 0,36–0,66, y 0,30–0,78)
json.dump({'src': '/toolkit/factory/f15/footage-trial/assets/standin.png', 'subject': [0.36, 0.30, 0.66, 0.78], 'zoom': [1.0, 1.18], 'anchor': [0.5, 0.40],
           't0': 1.0, 't1': 5.2, 'fade': [1.2, 1.0], 'caption': 'Stand-in frame (LoC photo pending)', 'source': 'Image: project render', 'key': 'plate-standin'},
          open(sys.argv[1], 'w'), indent=1)
PY
fi
python3 -I toolkit/footage/map.py --topo $A/us-atlas-3.0.1.tgz --attrs $A/ne_110m_admin_1_states_provinces.geojson --division "South Atlantic" \
  --context "East South Central" --box 640,190,1700,880 --out $S/map.json
python3 - "$S/map.json" <<'PY'
import json, sys
m = json.load(open(sys.argv[1])); m.update(t0=4.3, t1=7.4, fade=[1.0, 0.7]); json.dump(m, open(sys.argv[1], 'w'), separators=(',', ':'))
PY
rm -rf $H/out/cache
t0=$(date +%s)
node toolkit/factory/world/render_shots.js $S 540 $H/out/footage-trial-540.mp4 --workers 2 --cache $H/out/cache
echo "render: $(( $(date +%s) - t0 )) s"
python3 - $H <<'PY'
import json, subprocess, sys
H = sys.argv[1]; L = json.load(open(f'{H}/out/footage-trial-540.log.json')); W = {w['w'].strip(',.'): w['s'] for w in json.load(open(f'{H}/seg/words.json'))['words']}
hits = [(x['t'], b['k']) for x in L if 'plate' in x for b in x['plate']['boxes'] if b['hitsSubject']]
sides = sorted({x['plate']['side'] for x in L if 'plate' in x})
first = {}
for x in L:
    for lb in (x.get('map') or {}).get('labels', []):
        first.setdefault(lb['text'], x['t'])
want = {'South Atlantic': W['South'], 'Florida': W['Florida'], 'Maryland': W['Maryland']}
lag = {k: round(first.get(k, 99) - v, 3) for k, v in want.items()}
pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height,nb_frames,codec_name', '-of', 'json', f'{H}/out/footage-trial-540.mp4'],
                               capture_output=True, text=True).stdout)['streams'][0]
rep = {'video': pr, 'plate_frames_logged': sum('plate' in x for x in L), 'band_sides': sides, 'text_hits_subject': len(hits),
       'label_lag_s (log 0,1 s)': lag, 'labels_ok': all(0 <= v <= 0.2 for v in lag.values())}
json.dump(rep, open(f'{H}/out/check.json', 'w'), indent=1); print(json.dumps(rep, ensure_ascii=False))
sys.exit(0 if not hits and rep['labels_ok'] else 1)
PY

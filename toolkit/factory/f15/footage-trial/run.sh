#!/usr/bin/env bash
# F-15 (f) · clip thử footage 540p 8 s. Chạy từ gốc repo: bash toolkit/factory/f15/footage-trial/run.sh
#   1. ảnh: assets/loc.jpg = X-F15-3 (`fetch.py https://www.loc.gov/item/2015631813/ --loc --id X-F15-3 --tier 5 --license-name "No known restrictions (LoC)"
#      --dest toolkit/factory/f15/footage-trial/assets --out-name loc.jpg --credit …`); chưa có → ẢNH THAY THẾ = khung
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
# X-F15-3 (RIGHTS F6): LoC 2015631813, Carol M. Highsmith 2015-05-07, "No known restrictions on publication." — không người, không logo/nhãn hiệu
# (F2; ảnh đầu 2010630116 có logo ngân hàng → bỏ, REVIEWER 14/10). Chủ thể = dãy nhà, rà khung 14/10: x 0,12–0,95 · y 0,23–0,68 của ảnh 1840×1228;
# RIGHTS F4: tư liệu ghi năm + nguồn trên hình
json.dump({'src': '/toolkit/factory/f15/footage-trial/assets/loc.jpg', 'subject': [0.12, 0.23, 0.95, 0.68], 'zoom': [1.0, 1.12], 'anchor': [0.5, 0.40],
           't0': 1.0, 't1': 5.2, 'fade': [1.2, 1.0], 'caption': 'Bungalows, Huntington, West Virginia, 2015',
           'source': 'Photo: Carol M. Highsmith, Library of Congress', 'key': 'plate-loc'},
          open(sys.argv[1], 'w'), indent=1)
PY
else
  rm -f $S/plate.json $S/map.json; mv $S/inputs.json $S/inputs.json.hold
  node toolkit/factory/world/render_shots.js $S 1080 $H/out/still.mp4 --stills 0.4 --stills-dir $A --cache $H/out/cache >/dev/null
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
  --context "East South Central" --census-year 2017 --ne-version "$(cat $A/NE-VERSION 2>/dev/null || echo 5.2.0-pre)" --box 640,190,1700,880 --out $S/map.json
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
# chữ đè chữ: mọi cặp hộp chữ cùng hiện (độ hiện ≥ 0,5) giao nhau > 1 px (cine-lab #50: không để dòng này che dòng kia)
def inter(a, b):
    return min(a[2], b[2]) - max(a[0], b[0]) > 1 and min(a[3], b[3]) - max(a[1], b[1]) > 1
tt = [(x['t'], p['text'], q['text']) for x in L for i, p in enumerate(x['texts']) for q in x['texts'][i + 1:]
      if p['opacity'] >= 0.5 and q['opacity'] >= 0.5 and inter(p['box'], q['box'])]
lag = {k: round(first.get(k, 99) - v, 3) for k, v in want.items()}
pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height,nb_frames,codec_name', '-of', 'json', f'{H}/out/footage-trial-540.mp4'],
                               capture_output=True, text=True).stdout)['streams'][0]
rep = {'video': pr, 'plate_frames_logged': sum('plate' in x for x in L), 'band_sides': sides, 'text_hits_subject': len(hits),
       'label_lag_s (log 0,1 s)': lag, 'labels_ok': all(0 <= v <= 0.2 for v in lag.values()),
       'text_on_text_frames': len({t for t, *_ in tt}), 'text_on_text_pairs': sorted({f'{a} × {b}' for _, a, b in tt})}
json.dump(rep, open(f'{H}/out/check.json', 'w'), indent=1); print(json.dumps(rep, ensure_ascii=False))
sys.exit(0 if not hits and rep['labels_ok'] and not tt else 1)
PY

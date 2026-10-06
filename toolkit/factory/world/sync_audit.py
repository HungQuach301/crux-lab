"""Mốc V: kiểm đồng bộ trên SẢN PHẨM CUỐI.
  python3 toolkit/factory/world/sync_audit.py <video.mp4> <out.json> --spine <spine.json>   (từ moc-v/proto, Mốc V)
(1) Lời: ASR (faster-whisper small.en, word timestamps) trên bản trộn cuối → lệch so với alignment của take (spine.words).
(2) Hình: mỗi cue hình của spine (từ khoá) → khung đầu tiên trong [−0,4; +0,8] s có thay đổi điểm ảnh ≥ 35 % đỉnh cửa sổ; lệch = khung đó − từ khoá.
(3) Âm dữ liệu/sfx: mỗi sự kiện spine → đỉnh onset của bản trộn trong [−0,1; +0,2] s (nốt có thể dời vào khe lời ≤ 120 ms)."""
import json, os, re, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
video, out = sys.argv[1:3]
spine = json.load(open(sys.argv[sys.argv.index('--spine') + 1]))
from faster_whisper import WhisperModel
m = WhisperModel('small.en', device='cpu', compute_type='int8')
pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
segs, _ = m.transcribe(pcm, word_timestamps=True, language='en')
asr = [(re.sub(r'[^\w]', '', w.word).lower(), w.start) for s in segs for w in s.words]
ref = [(re.sub(r'[^\w]', '', w['w']).lower(), w['s']) for w in spine['words'] if not w['w'].startswith('[')]
d, j = [], 0
for word, t in ref:
    for k in range(j, min(j + 6, len(asr))):
        if asr[k][0] == word:
            d.append(asr[k][1] - t); j = k + 1; break
d = np.array(d)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', 'fps=30,scale=320:180,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320).astype(np.int16)
diff = np.r_[0, [np.abs(fr[i] - fr[i - 1]).mean() for i in range(1, len(fr))]]
VIS = spine.get('visual_cues') or ['b0.q', 'b1.blur', 'b2.draw0', 'b3.cap', 'b3.lbl', 'b4.grow', 'b4.less', 'b6.cross', 'b8.lbl', 'b9.fly', 'b10.past', 'b11.x']
LBL = spine.get('label_cues', {})            # cue → chữ trên hình: thời điểm hiện (opacity ≥ 0,5) đọc từ nhật ký trang (độ phân giải 0,1 s)
moves = spine.get('moves', [])
cues = {f"{b['id']}.{k}": t for b in spine['beats'] for k, t in b['cues'].items()}
plog = None
lp = video.replace('.mp4', '.log.json')
if os.path.exists(lp): plog = sorted(json.load(open(lp)), key=lambda l: l['t'])
vis, how = {}, {}
for name in VIS:
    t = cues[name]
    if name in LBL and plog:
        first = next((l['t'] for l in plog if l['t'] >= t - 1.0 and any(x['text'] == LBL[name] and x['opacity'] >= 0.5 for x in l['texts'])), None)
        vis[name] = round(first - t, 3) if first is not None else None; how[name] = 'label'; continue
    roi = None
    if plog:
        near = min(plog, key=lambda l: abs(l['t'] - t))
        roi = (near.get('roi') or {}).get(name)
    if roi:                                    # đo trong vùng của vật thể (hộp từ trang, thiết kế 1920×1080) trên video thật
        x0, y0, x1, y1 = [int(v * 320 / 1920) for v in roi[:1]] + [int(roi[1] * 180 / 1080)] + [int(roi[2] * 320 / 1920)] + [int(roi[3] * 180 / 1080)]
        x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(320, max(x1, x0 + 2)), min(180, max(y1, y0 + 2))
        dl = np.r_[0, [np.abs(fr[i, y0:y1, x0:x1] - fr[i - 1, y0:y1, x0:x1]).mean() for i in range(1, len(fr))]]
    else:
        dl = diff
    end = t + 0.8
    for m in moves:                          # không để động tác máy quay kế tiếp lẫn vào cửa sổ đo
        if t < m['t0'] < end: end = m['t0']
    base = float(np.median(dl[int((t - 0.7) * 30):int((t - 0.15) * 30)]))
    st = t - 0.3
    for m in moves:                          # … và không lấy đuôi động tác máy quay TRƯỚC đó làm "hình phản ứng"
        if st < m['t1'] <= t: st = m['t1'] + 1 / 30
    i0, i1 = int(st * 30), int(end * 30)
    seg = dl[i0:i1]
    if len(seg) == 0 or seg.max() - base < 0.08:
        vis[name] = None; how[name] = 'motion'; continue
    on = int(np.argmax(seg > base + 0.5 * (seg.max() - base)))
    vis[name] = round(i0 / 30 + on / 30 - t, 3); how[name] = 'motion-roi' if roi else 'motion'
res = {'video': video, 'asr_words_matched': int(len(d)), 'asr_words_ref': len(ref),
       'voice_offset_s': {'median': round(float(np.median(d)), 3), 'p90_abs': round(float(np.percentile(np.abs(d), 90)), 3)},
       'visual_peak_vs_keyword_s': vis, 'method': how,
       'visual_within_0.2s': f"{sum(v is not None and abs(v) <= 0.2 for v in vis.values())}/{len(vis)}",
       'visual_not_detected': [k for k, v in vis.items() if v is None]}
json.dump(res, open(out, 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'visual_peak_vs_keyword_s'}))

"""Clip nổi bật C4 (<= 2 phút) từ animatic/out/animatic-720p.mp4: cắt theo ranh câu (animatic/timing.json), mỗi đoạn
-0,4 s trước câu đầu / +0,8 s sau câu cuối, nối bằng mờ đen 0,25 s. PyAV (không ffmpeg). Ra: review-c4/c4-highlights.mp4 + .json."""
import json, os, fractions
import av, numpy as np
EP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = f'{EP}/animatic/out/animatic-720p.mp4'; OUT = f'{EP}/review-c4/c4-highlights.mp4'
T = json.load(open(f'{EP}/animatic/timing.json')); S = {s['n']: s for sc in T['scenes'] for s in sc['sentences']}
SEG = [  # (câu đầu, câu cuối, lý do)
    (4, 8, 'S01–S02: [softly] "She didn\'t take it", lá thư, câu hứa [curious]'),
    (49, 52, 'S10: khe dư nợ $1,133 [thoughtful], hoà vốn 24 → 30 [serious]'),
    (59, 61, 'S13: ngưỡng nửa điểm của Nora [warmly]'),
    (79, 80, 'S16: Walt, vì sao khoản nhỏ cần giảm nhiều hơn [serious]'),
    (88, 91, 'S18: thước ba mốc [matter-of-fact]'),
    (104, 105, 'S20: câu hỏi ở lại [softly]'),
]
FPS = 30; SR = 48000; FADE = 0.25
win = [(max(0, S[a]['start'] - 0.4), S[b]['end'] + 0.8, why) for a, b, why in SEG]
tot = sum(e - s for s, e, _ in win); assert tot <= 120, tot
inp = av.open(SRC); vs = inp.streams.video[0]; as_ = inp.streams.audio[0]
frames = []; audio = []
# lời nằm đúng thời điểm tuyệt đối trong animatic (assemble.py ghép copy) -> cắt thẳng từ file lời
_n = av.open(f'{EP}/review-c4/narration-v32.m4a'); _r = av.AudioResampler(format='flt', layout='mono', rate=SR)
NAR = np.concatenate([x.to_ndarray()[0] for f in _n.decode(audio=0) for x in _r.resample(f)]); _n.close()
res = av.AudioResampler(format='flt', layout='mono', rate=SR)
for s, e, _ in win:
    inp.seek(int(max(0, s - 2) / vs.time_base), stream=vs)
    seg = []
    for f in inp.decode(vs):
        t = float(f.pts * vs.time_base)
        if t < s - 1e-3: continue
        if t >= e: break
        seg.append(f.to_ndarray(format='rgb24'))
    n = len(seg); k = int(FADE * FPS)
    for i in range(n):
        g = min(1.0, (i + 1) / k, (n - i) / k); seg[i] = (seg[i] * g).astype(np.uint8)
    frames += seg
    L = int(round(n / FPS * SR)); i0 = int(round(s * SR)); a = NAR[i0:i0 + L]; a = np.pad(a, (0, L - len(a)))
    k = int(FADE * SR); r = np.linspace(0, 1, k); a[:k] *= r; a[-k:] *= r[::-1]; audio.append(a)
inp.close()
o = av.open(OUT, 'w'); v = o.add_stream('libx264', rate=FPS); v.width, v.height = frames[0].shape[1], frames[0].shape[0]
v.pix_fmt = 'yuv420p'; v.options = {'crf': '23'}
au = o.add_stream('aac', rate=SR); au.layout = 'mono'; au.bit_rate = 160000
for fr in frames:
    for p in v.encode(av.VideoFrame.from_ndarray(fr, format='rgb24')): o.mux(p)
for p in v.encode(None): o.mux(p)
A = np.concatenate(audio).astype(np.float32).reshape(1, -1)
for i in range(0, A.shape[1], 1024):
    fr = av.AudioFrame.from_ndarray(np.ascontiguousarray(A[:, i:i + 1024]), format='flt', layout='mono'); fr.sample_rate = SR
    for p in au.encode(fr): o.mux(p)
for p in au.encode(None): o.mux(p)
o.close()
json.dump({'source': 'animatic/out/animatic-720p.mp4', 'total_s': round(len(frames) / FPS, 2),
           'segments': [{'from': round(s, 2), 'to': round(e, 2), 'why': w} for s, e, w in win]},
          open(OUT.replace('.mp4', '.json'), 'w'), indent=1, ensure_ascii=False)
print(round(len(frames) / FPS, 2), 's', [(round(s, 1), round(e, 1)) for s, e, _ in win])

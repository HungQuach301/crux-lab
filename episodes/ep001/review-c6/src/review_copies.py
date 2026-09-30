"""C6: bản xem cho chủ dự án, cắt từ bản giao out/video.mp4 (1080p, CBR 24 Mb/s, quá lớn cho git).
  review-c6/c6-highlights.mp4 : clip nổi bật <= 3 phút (6 đoạn theo ranh câu animatic/timing.json, -0,4/+0,8 s, mờ 0,25 s), 1280x720 CRF 22, tiếng lấy
                                 từ out/audio/master.wav (bản mix cuối, stereo), cùng gốc thời gian.
  review-c6/ep001-full-720p.mp4: bản đầy đủ 1280x720 CRF 23 để xem qua link GitHub (bản giao 1080p giữ SHA-256 trong review-c6/c6-files.json).
PyAV + ffmpeg (apt). Ra thêm review-c6/c6-files.json."""
import hashlib, json, os, subprocess, sys
import av, numpy as np, soundfile as sf
EP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = f'{EP}/out/video.mp4'; MASTER = f'{EP}/out/audio/master.wav'; OUT = f'{EP}/review-c6'
T = json.load(open(f'{EP}/animatic/timing.json')); S = {s['n']: s for sc in T['scenes'] for s in sc['sentences']}
SEG = [(1, 8, 'S01–S02: cold open (cửa sổ đã khép, [softly]), lá thư, câu hứa [curious]'),
       (49, 52, 'S10: khe dư nợ $1,133 [thoughtful], hoà vốn 24 → 30 [serious]'),
       (59, 61, 'S13: ngưỡng nửa điểm của Nora [warmly]'),
       (78, 80, 'S16: Walt — vì sao khoản nhỏ cần giảm nhiều hơn [serious]'),
       (88, 96, 'S18: thước ba mốc (lời mới "For Walt, with…") [matter-of-fact], nhãn góc gốc tiền'),
       (103, 105, 'S20: câu hỏi ở lại [softly]')]
FPS, SR, FADE = 30, 48000, 0.25


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()


def highlights():
    win = [(max(0, S[a]['start'] - 0.4), S[b]['end'] + 0.8, w) for a, b, w in SEG]
    assert sum(e - s for s, e, _ in win) <= 180
    A, sr = sf.read(MASTER, dtype='float32', always_2d=True); assert sr == SR
    inp = av.open(SRC); vs = inp.streams.video[0]
    o = av.open(f'{OUT}/c6-highlights.mp4', 'w'); v = o.add_stream('libx264', rate=FPS); v.width, v.height = 1280, 720
    v.pix_fmt = 'yuv420p'; v.options = {'crf': '22', 'preset': 'medium'}
    au = o.add_stream('aac', rate=SR); au.layout = 'stereo'; au.bit_rate = 192000
    audio = []
    for s, e, _ in win:
        inp.seek(int(max(0, s - 2) / vs.time_base), stream=vs); frames = []
        for f in inp.decode(vs):
            t = float(f.pts * vs.time_base)
            if t < s - 1e-3: continue
            if t >= e: break
            frames.append(f.reformat(width=1280, height=720, format='rgb24').to_ndarray())
        n = len(frames); k = int(FADE * FPS)
        for i, fr in enumerate(frames):
            g = min(1.0, (i + 1) / k, (n - i) / k)
            for p in v.encode(av.VideoFrame.from_ndarray((fr * g).astype(np.uint8), format='rgb24')): o.mux(p)
        L = int(round(n / FPS * SR)); i0 = int(round(s * SR)); a = A[i0:i0 + L].copy(); a = np.pad(a, ((0, L - len(a)), (0, 0)))
        k = int(FADE * SR); r = np.linspace(0, 1, k)[:, None]; a[:k] *= r; a[-k:] *= r[::-1]; audio.append(a)
    for p in v.encode(None): o.mux(p)
    Aa = np.ascontiguousarray(np.concatenate(audio).T.astype(np.float32))
    for i in range(0, Aa.shape[1], 1024):
        fr = av.AudioFrame.from_ndarray(np.ascontiguousarray(Aa[:, i:i + 1024]), format='fltp', layout='stereo'); fr.sample_rate = SR
        for p in au.encode(fr): o.mux(p)
    for p in au.encode(None): o.mux(p)
    o.close(); inp.close()
    return [{'from': round(s, 2), 'to': round(e, 2), 'why': w} for s, e, w in win]


def full720():
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', SRC, '-vf', 'scale=1280:720', '-c:v', 'libx264', '-crf', '23', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', f'{OUT}/ep001-full-720p.mp4'], check=True)


if __name__ == '__main__':
    segs = highlights()
    if '--no-full' not in sys.argv: full720()
    files = {'source': 'out/video.mp4', 'sourceSha256': sha(SRC), 'sourceBytes': os.path.getsize(SRC), 'highlights': segs}
    for n in ['c6-highlights.mp4', 'ep001-full-720p.mp4']:
        p = f'{OUT}/{n}'
        if os.path.exists(p): files[n] = {'bytes': os.path.getsize(p), 'sha256': sha(p)}
    json.dump(files, open(f'{OUT}/c6-files.json', 'w'), indent=1, ensure_ascii=False); print(json.dumps(files, ensure_ascii=False)[:600])

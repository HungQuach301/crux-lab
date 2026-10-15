"""Tập 9 · nhạc nền cả tập = "Origami" — Scott Buckley (CC BY 4.0, RIGHTS M-BUCKLEY-ORIGAMI, D-014; chủ dự án G1 câu 3 b-Z), BIÊN TẬP theo hồi.
    python3 episodes/ep009/world/music/bed.py <seconds> <out.wav> --timeline episodes/ep009/out/factory/timeline.json
Ra nhạc khô (chưa trộn) + <out>.json (bpm, lưới phách, cue theo hồi, khoảng lặng, bản đồ căng) như bed.py Tập 8 — mức dưới lời và né 1–4 kHz do
toolkit/factory/music.py làm khi trộn. Tệp gốc: work/external/sb-Origami.mp3 (SHA-256 kiểm ở đây; lệch → dừng). Không sửa cao độ/nhịp bài.

Bản đồ đoạn của bài (năng lượng 4 s, đo 15/10): 0–20 dạo (thưa) · 20–68 dâng · 68–92 lắng (breakdown) · 92–164 dâng chính · 164–180 lắng · 180–189 kết.
Mỗi hồi một chuỗi đoạn của bài, nối ở ranh ô nhịp (152 bpm, 4 phách = 1,579 s) bằng crossfade 0,6 s (G-003: không cắt cứng):
  Q  cold open  S01 → hết lời S03   0–68 (dạo → dâng), nhường trước ident (F-12 phát ident A ở 3 s cuối đuôi S03)
  A1 hồi 1      S04 → MR1           68–92 lắng → 92–… (dâng ở số neo S04.3 là lặng, dâng lại sau)
  A2 hồi 2      MR1 → S14           20–68 → 92–164 (đi dọc phố)
  A2b hồi 2b    S14 → MR2           68–92 lắng (đống tụt) → 120–164 (đếm, sáng lại)
  A3 hồi 3      MR2 → S24           92–164
  O  kết        S24 → hết           164–189: điểm kết 180 s của bài rơi 0,8 s sau chữ cuối của tập
Lặng: MR1, MR2 [t − 0,6; t + 0,6]; ident [đuôi S03 − 3 s; hết S03]; 0,75 s TRƯỚC mỗi số neo (S04.3, S14.3, S15.2); nhả 0,2 s, vào lại 0,25 s.
Lần dựng ĐẦU (M2 animatic): giờ khô (prod/dry_takes.py); M3 dựng lại trên giờ lời thật — cùng mã."""
import hashlib, json, os, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(os.path.dirname(HERE)); ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
SRC = os.path.join(EP, 'work', 'external', 'sb-Origami.mp3')
SHA = '8b8edd81ee2110a62169b48e3233e1556c0f9de10003b21f41a28e5b4bcbfe14'
SR, BPM, XF = 48000, 152.0, 0.6
BAR = 4 * 60 / BPM
ANCHORS = ['S04.3', 'S14.3', 'S15.2']
ANCHOR_SIL, MR_HOLD, REL, RIN = 0.75, 0.6, 0.2, 0.25
PLAN = {'Q': [(0, 68)], 'A1': [(68, 92), (92, 164)], 'A2': [(20, 68), (92, 164), (20, 68)], 'A2b': [(68, 92), (120, 164), (92, 164)],
        'A3': [(92, 164), (20, 68)], 'O': [(164, 189)]}
TENSION = {'Q': 0.45, 'A1': 0.5, 'A2': 0.6, 'A2b': 0.7, 'A3': 0.55, 'O': 0.35}


def load():
    if hashlib.sha256(open(SRC, 'rb').read()).hexdigest() != SHA:
        raise SystemExit(f'{SRC}: SHA-256 khác RIGHTS M-BUCKLEY-ORIGAMI — dừng (tải lại từ trang bài)')
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', SRC, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).astype(np.float64)


def snap(t):
    return round(t / BAR) * BAR


def fill(x, ranges, dur, end_at=None):
    """Nối các đoạn [a, b) của bài (ranh ô nhịp, crossfade XF) tới đủ dur giây; end_at: giờ trong cụm mà đoạn cuối phải KẾT THÚC đúng (kết bài)."""
    out = np.zeros((int(dur * SR) + 1, 2)); t, segs, k = 0.0, [], 0
    if end_at is not None:   # kết: đặt đoạn cuối sao cho hết bài ở end_at
        a, b = ranges[-1]; t0 = end_at - (b - a); i0 = max(0, int(-t0 * SR)); s = x[int(a * SR) + i0:int(b * SR)]
        j = int(max(0, t0) * SR); n = min(len(s), len(out) - j); out[j:j + n] += s[:n]; segs.append([round(max(0, t0), 3), a + i0 / SR, b]); return out, segs
    while t < dur - 0.05:
        a, b = ranges[k % len(ranges)]; a, b = snap(a), snap(b); k += 1
        s = x[int(a * SR):int(b * SR)].copy(); f = int(XF * SR)
        s[:f] *= np.linspace(0, 1, f)[:, None] if t > 0 else 1; s[-f:] *= np.linspace(1, 0, f)[:, None]
        j = int(t * SR); n = min(len(s), len(out) - j); out[j:j + n] += s[:n]; segs.append([round(t, 3), a, b]); t += (b - a) - XF
    f = int(1.2 * SR); out[-f:] *= np.linspace(1, 0, f)[:, None]
    return out, segs


def gate(n, holes):
    g = np.ones(n)
    for a, b in holes:
        ia, ib = int(a * SR), int(b * SR); r0, r1 = int(REL * SR), int(RIN * SR)
        g[max(0, ia - r0):ia] = np.minimum(g[max(0, ia - r0):ia], 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, len(g[max(0, ia - r0):ia]))))
        g[ia:ib] = 0; g[ib:ib + r1] = np.minimum(g[ib:ib + r1], 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, len(g[ib:ib + r1]))))
    return g


def main():
    total, outp = float(sys.argv[1]), sys.argv[2]
    tl = json.load(open(sys.argv[sys.argv.index('--timeline') + 1]))
    import yaml
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    sc = {s['id']: s for s in tl['scenes']}; sent = {s['id']: s for s in tl['sentences']}
    end = lambda i: sc[i]['start'] + sc[i]['dur']
    last = max(s['end'] for s in tl['sentences'])
    mr = [m['t'] for m in Y.get('midrolls') or [] if m.get('t')] or [end('S06') - 0.7, end('S18') - 0.7]
    S03_last = max(s['end'] for s in tl['sentences'] if s['scene'] == 'S03')
    bounds = {'Q': (0.0, S03_last + 0.6), 'A1': (end('S03'), mr[0]), 'A2': (mr[0], sc['S14']['start']), 'A2b': (sc['S14']['start'], mr[1]),
              'A3': (mr[1], sc['S24']['start']), 'O': (sc['S24']['start'], total)}
    x = load(); bed = np.zeros((int(total * SR) + 1, 2)); cues = []
    for cue, (a, b) in bounds.items():
        seg, segs = fill(x, PLAN[cue], b - a + XF, end_at=(last + 0.8 - a + (189 - 180)) if cue == 'O' else None)
        j = int(a * SR); n = min(len(seg), len(bed) - j); bed[j:j + n] += seg[:n]
        cues.append({'id': cue, 't0': round(a, 3), 't1': round(b, 3), 'source': [[round(a + s[0], 3), round(s[1], 3), round(s[2], 3)] for s in segs]})
    holes = [[m - MR_HOLD, m + MR_HOLD] for m in mr] + [[S03_last + 0.6, end('S03')]]
    holes += [[sent[k]['start'] - ANCHOR_SIL - 0.05, sent[k]['start'] - 0.05] for k in ANCHORS if k in sent]
    bed *= gate(len(bed), holes)[:, None]
    pk = np.abs(bed).max(); bed *= 10 ** (-3 / 20) / max(pk, 1e-9)
    os.makedirs(os.path.dirname(os.path.abspath(outp)), exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'pcm_s16le', outp],
                   input=bed.astype(np.float32).tobytes(), check=True)
    kf = []
    for c in cues:
        kf += [{'t': c['t0'], 'v': TENSION[c['id']]}, {'t': c['t1'], 'v': TENSION[c['id']]}]
    beats = [round(i * 60 / BPM, 3) for i in range(int(total * BPM / 60))]
    json.dump({'bpm': BPM, 'beats': beats, 'accents': [], 'cues': cues, 'silences': [[round(a, 3), round(b, 3)] for a, b in holes],
               'tension': {'keyframes': kf}, 'source': {'file': 'work/external/sb-Origami.mp3', 'sha256': SHA, 'rights': 'M-BUCKLEY-ORIGAMI'}},
              open(outp + '.json', 'w'), indent=1)
    print(f'bed {total:.1f} s · {len(cues)} cue · {len(holes)} lặng · {outp}')


if __name__ == '__main__':
    main()

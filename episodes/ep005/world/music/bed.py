"""Tập 5 · F-3 — nhạc nền cả tập SINH BẰNG MÃ theo bản đồ căng (tension.py), style C (G-016 · chọn): ~114 BPM, D dorian (cold open →
Hồi 2) rồi F trưởng từ S15, ostinato pluck + bass móc + nhịp trầm mềm, cùng họ nhạc cụ với toolkit/factory/world/audio.py.
Ra nhạc KHÔ + reverb, chưa trộn: mức dưới lời (20 dB, A07) và mất dải 1–4 kHz (13 dB) do toolkit/factory/music.py làm khi mix.
  python3 episodes/ep005/world/music/bed.py <seconds> <out.wav> [--timeline out/factory/timeline.json]
  (episode.yaml → audio.music_cmd: "python3 episodes/ep005/world/music/bed.py {total} {out}")
Ra thêm <out>.json: lưới phách (cho toolkit/audio/d_music_selfsim.py), từng ô nhịp (khoá, hợp âm, mức căng, tầng), mốc MR1/chốt.

Biên độ nghe được (D-010 §5 "rộng hơn bản thử"): mức căng điều khiển CẢ số tầng (pad → bass → pluck → kick → shaker → chuông) LẪN
một đường gain liên tục (DB_SPAN dB giữa căng 0 và 1, làm mượt 1,5 s) — đo LUFS ngắn hạn của stem nhạc theo đoạn ở audition.py.
MR1: nhạc về 0 trong [MR1 − 0,6; MR1 + 0,6] s (≥ 1 s lặng), nhả cos 0,25 s trước (C5b; trước 0,6) (G-003: không cắt cứng), vào lại 0,3 s; lưới ô nhịp bắt
đầu lại đúng sau khoảng lặng (Hồi 2 vào ở phách mạnh). Lưới Hồi 2–outro co giãn ≤ 0,1 % để PHÁCH MẠNH rơi đúng đầu từ "removed" (S20.2):
ô trước là V (C), ô "removed" là I (F) — cadence chốt; sau đó chỉ còn pad + pluck thưa, tắt dần.
G-002 (không lộ vòng): hợp âm theo chuỗi Markov, cấm lặp lại bất kỳ chuỗi 4 hợp âm nào trong 24 ô gần nhất; mỗi ô một hình ostinato
(5 dáng giai điệu × 5 mặt nạ nhịp, không lặp hình của ô trước); tầng đổi theo mức căng.
"""
import json
import os
import sys

import numpy as np
from scipy.ndimage import uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
sys.dont_write_bytecode = True
import audio as WA  # noqa: E402  (nhạc cụ style C của nhà máy: pad, pluck, bass, thump, shaker, felt, bell, reverb)
import tension as TM  # noqa: E402

SR = WA.SR
BPM = 114.0
DB_SPAN = 1.0          # gain liên tục: căng 0 → −1 dB so với căng 1 (phần lớn biên độ do số tầng; đỉnh vẫn ≥ 15 dB dưới lời tại chỗ)
MR_HOLD, MR_REL, MR_IN = 0.6, 0.25, 0.3   # C5b vòng 2: nhả 0,6 → 0,25 s (checks T3: vào khoảng lặng 150–400 ms; đo 0,615 s)
hz = WA.hz
NOTE = {'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
CHORDS = {
    'F major': {'I': ('F', ''), 'V': ('C', ''), 'vi': ('D', 'm'), 'IV': ('Bb', ''), 'ii': ('G', 'm'), 'iii': ('A', 'm'), 'Iadd9': ('F', 'add9'),
                'IVmaj7': ('Bb', 'maj7')},
    'D dorian': {'i': ('D', 'm'), 'i7': ('D', 'm7'), 'IV': ('G', ''), 'IVadd9': ('G', 'add9'), 'VII': ('C', ''), 'III': ('F', ''), 'v': ('A', 'm'),
                 'ii': ('E', 'm')},
}
MARKOV = {   # cùng chuỗi đã duyệt của Tập 3 (mix_full.py); dorian: IV trưởng, không ♭VI buồn (G-016)
    'F major': {'I': ['IV', 'vi', 'V', 'ii', 'iii', 'IVmaj7'], 'Iadd9': ['vi', 'IV', 'ii'], 'IV': ['I', 'V', 'ii', 'Iadd9', 'vi'], 'IVmaj7': ['V', 'I', 'iii'],
                'V': ['I', 'vi', 'IV', 'Iadd9'], 'vi': ['IV', 'ii', 'V', 'IVmaj7'], 'ii': ['V', 'I', 'IV'], 'iii': ['vi', 'IV', 'ii']},
    'D dorian': {'i': ['IV', 'VII', 'III', 'IVadd9', 'v'], 'i7': ['IV', 'VII', 'ii'], 'IV': ['i', 'VII', 'i7', 'III', 'v'], 'IVadd9': ['i', 'VII', 'III'],
                 'VII': ['IV', 'i', 'III', 'i7'], 'III': ['IV', 'VII', 'i', 'ii'], 'v': ['IV', 'VII', 'i'], 'ii': ['IV', 'i7', 'v']},
}
TONIC = {'F major': 'I', 'D dorian': 'i'}
OST = [[0, 2, 3, 6, 8, 10, 11, 14], [0, 3, 6, 8, 9, 11, 14, 15], [0, 2, 3, 6, 8, 11, 12, 14], [0, 3, 4, 6, 8, 10, 12, 14], [0, 2, 3, 5, 6, 8, 11, 14]]
ACC16 = {0, 3, 6, 8, 11, 14}
SHAPES = ['up', 'down', 'updown', 'broken', 'pedal']
BELL_RHY = [[0, 6, 10], [2, 8, 12], [0, 4, 11], [3, 8, 14], [0, 10]]


def chord_pcs(key, name):
    root, q = CHORDS[key][name]
    r = NOTE[root]
    iv = {'m': [0, 3, 7], '': [0, 4, 7], 'm7': [0, 3, 7, 10], 'add9': [0, 4, 7, 14], 'maj7': [0, 4, 7, 11]}[q]
    return r, [r + i for i in iv]


def contour(shape, tones, k):
    m = len(tones)
    if shape == 'up': return tones[k % m]
    if shape == 'down': return tones[-1 - k % m]
    if shape == 'updown':
        c = k % (2 * m - 2); return tones[c if c < m else 2 * m - 2 - c]
    if shape == 'broken': return tones[[0, 2, 1, 3, 2, 4, 3, 1][k % 8] % m]
    return tones[0] if k % 2 == 0 else tones[1 + (k // 2) % (m - 1)]


def grid(M, total):
    """Ô nhịp: đoạn A [0, MR1 − hold), đoạn B [MR1 + hold, removed) co giãn cho phách mạnh trúng 'removed', đoạn C [removed, hết)."""
    bar0 = 4 * 60 / BPM
    a1, b0, land = M['mr1'] - MR_HOLD, M['mr1'] + MR_HOLD, M['landing']
    n = max(1, round((land - b0) / bar0))
    barB = (land - b0) / n
    bars = []
    t = 0.0
    while t < a1 - 0.25:
        bars.append({'t0': t, 't1': min(t + bar0, a1), 'len': bar0, 'sec': 'A'}); t += bar0
    for k in range(n):
        bars.append({'t0': b0 + k * barB, 't1': b0 + (k + 1) * barB, 'len': barB, 'sec': 'B'})
    t = land
    while t < total:
        bars.append({'t0': t, 't1': t + barB, 'len': barB, 'sec': 'C'}); t += barB
    return bars, 240 / barB


def harmony(bars, M):
    rng = np.random.default_rng(1005)
    seq = []
    for i, b in enumerate(bars):
        key = 'F major' if b['t0'] >= M['key_change'] - b['len'] / 2 else 'D dorian'
        b['key'] = key
        first = i == 0 or bars[i - 1]['sec'] != b['sec'] or bars[i - 1].get('key') != key
        if b['sec'] == 'C' and (i == 0 or bars[i - 1]['sec'] != 'C'):
            c = 'Iadd9'                                            # chốt: ô "removed" = I
        elif b['sec'] == 'B' and i + 1 < len(bars) and bars[i + 1]['sec'] == 'C':
            c = 'V'                                                # ô trước "removed" = V → cadence
        elif first:
            c = TONIC[key]
        else:
            prev = seq[-1]
            for attempt in range(200):
                opts = MARKOV[key][prev] if prev in MARKOV[key] else [TONIC[key]]
                c = opts[rng.integers(0, len(opts))]
                cand = seq + [c]
                if len(cand) >= 4 and attempt < 180:
                    hist = seq[-24:]
                    if any(hist[j:j + 4] == cand[-4:] for j in range(0, max(0, len(hist) - 3))):
                        continue
                if c == prev and attempt < 150:
                    continue
                break
        seq.append(c)
        b['chord'] = c
    return seq


def tension_fn(M):
    kf = [(k['t'], k['v']) for k in M['keyframes']]
    return lambda t: TM.curve(kf, t)


def render(total, M, seed=1005):
    rng = np.random.default_rng(seed)
    N = int(round(total * SR))
    dry = np.zeros((N, 2))
    bars, bpmB = grid(M, total)
    harmony(bars, M)
    ten_at = tension_fn(M)
    a1 = M['mr1'] - MR_HOLD
    land = M['landing']
    prev_vo, prev_fig = None, None
    for i, b in enumerate(bars):
        t0, L = b['t0'], b['len']
        stop = a1 if b['sec'] == 'A' else total + 2
        beat = L / 4
        ten = float(np.mean(ten_at(np.linspace(t0, t0 + L, 9))))
        b['ten'] = round(ten, 3)
        key, name = b['key'], b['chord']
        r, pcs = chord_pcs(key, name)
        pcl = [p % 12 for p in pcs]
        cands = []
        for inv in range(len(pcl)):
            order = pcl[inv:] + pcl[:inv]
            for low in range(50, 61):
                if low % 12 != order[0]: continue
                v = [low]
                for pc in order[1:]:
                    n_ = v[-1] + 1
                    while n_ % 12 != pc: n_ += 1
                    v.append(n_)
                if v[-1] <= 72: cands.append(v)
        vo = min(cands, key=lambda v: sum(min(abs(a - c) for c in prev_vo) for a in v) + 0.3 * rng.random()) if prev_vo else cands[0]
        prev_vo = vo
        layers = ['pad']
        landing_bar = b['sec'] == 'C' and (i == 0 or bars[i - 1]['sec'] != 'C')
        pdur = min(L + 0.6, stop - t0)
        WA.add(dry, t0, WA.pad(hz(vo), pdur, (0.05 + 0.20 * ten) * (1.6 if landing_bar else 1.0), 700 + 1800 * ten))
        broot = 36 + (r % 12) + (12 if (r % 12) < 2 else 0)
        # bass
        if ten < 0.3:
            for e in (0, 4):
                t = t0 + e * beat / 2
                if t < stop: WA.add(dry, t, WA.bass(hz(broot), 0.15, 0.9 * beat))
        else:
            layers.append('bass8')
            for e in range(8):
                t = t0 + e * beat / 2
                if t >= stop: break
                WA.add(dry, t, WA.bass(hz(broot + (12 if e % 2 else 0)), (0.2 if e % 2 == 0 else 0.11) * (0.4 + 0.6 * ten) * rng.uniform(0.92, 1.05),
                                       0.45 * beat))
        # nhịp trầm
        if b['sec'] != 'C':
            if ten >= 0.72: layers.append('kick4')
            elif ten >= 0.5: layers.append('kick2')
            for k in range(4):
                t = t0 + k * beat
                if t >= stop: break
                if ten >= 0.72 or (ten >= 0.5 and k % 2 == 0):
                    WA.add(dry, t, WA.thump((0.5 if k == 0 else 0.36) * (0.3 + 0.6 * ten) * rng.uniform(0.92, 1.05)))
            if ten >= 0.58:
                layers.append('shaker')
                steps = range(16) if ten >= 0.82 else range(2, 16, 4)
                for s in steps:
                    t = t0 + s * beat / 4
                    if t >= stop: break
                    WA.add(dry, t, WA.shaker((0.05 + 0.08 * ten) * (1.0 if s % 4 == 2 else 0.55)), 0.3 if s % 8 < 4 else -0.3)
        # ostinato pluck (luôn có nhịp — G-016: không chậm)
        tones = [n_ for n_ in range(57, 57 + 17) if n_ % 12 in pcl]
        for _ in range(20):
            shp, mk = SHAPES[rng.integers(0, len(SHAPES))], int(rng.integers(0, len(OST)))
            if (shp, mk) != prev_fig: break
        prev_fig = (shp, mk)
        hits = OST[mk] if ten >= 0.62 else (OST[mk][::2] if ten >= 0.3 or b['sec'] != 'C' else OST[mk][::4])
        layers.append('pluck' + ('8' if ten >= 0.62 else '4' if len(hits) == 4 else '2'))
        for j, h in enumerate(hits):
            t = t0 + h * beat / 4
            if t >= stop: break
            v = (0.16 if h in ACC16 else 0.1) * (0.45 + 0.6 * ten) * rng.uniform(0.88, 1.08)
            WA.add(dry, t, WA.pluck(hz(contour(shp, tones, j)), v, 1500 + 1500 * ten, 0.3), 0.22 if j % 2 else -0.22)
        # chuông đối âm ở đỉnh
        if ten >= 0.8 and b['sec'] != 'C':
            layers.append('bell')
            hi = [n_ for n_ in range(74, 88) if n_ % 12 in pcl]
            for j, s in enumerate(BELL_RHY[int(rng.integers(0, len(BELL_RHY)))]):
                t = t0 + s * beat / 4
                if t < stop: WA.add(dry, t, WA.lp1(WA.bell(hz(hi[int(rng.integers(0, len(hi)))]), 0.045 * ten, 1.6), 3200), 0.35 if j % 2 else -0.35)
        if landing_bar:   # chốt: I trưởng sáng — felt trầm + chuông rải
            layers.append('landing')
            WA.add(dry, t0, WA.felt(hz(41), 0.42, 1.8)); WA.add(dry, t0, WA.felt(hz(53), 0.22, 1.8), 0.1)
            for j, m in enumerate([77, 81, 84, 89]):
                WA.add(dry, t0 + j * beat / 2, WA.lp1(WA.bell(hz(m), 0.05, 2.4), 3000), -0.3 + 0.2 * j)
        if i > 0 and b['sec'] == 'B' and bars[i - 1]['sec'] == 'A':   # Hồi 2 vào lại ở phách mạnh
            WA.add(dry, t0, WA.felt(hz(38), 0.32)); layers.append('re-entry')
        b['layers'] = layers
    # điểm nhấn đúng từ (số then chốt) — riser 2 ô dẫn vào đỉnh S14.1
    for a, t in M['accents']:
        if a == TM.LANDING: continue
        root = 38 if t < M['key_change'] else 41
        WA.add(dry, t, WA.felt(hz(root), 0.34)); WA.add(dry, t, WA.felt(hz(root + 7), 0.16), 0.1)
    pk = dict(M['accents'])['S14.1:one']
    d = 2 * 4 * 60 / bpmB
    WA.add(dry, pk - d, WA.noise_sweep(d, 500, 4000, 0.05, att=d * 0.8))
    wet = WA.reverb(dry, 1.9, 0.24)[:N]
    # gain liên tục theo căng + cổng MR1 + vào/ra
    t = np.arange(0, N, 480) / SR
    ten_s = uniform_filter1d(ten_at(t), 150)                     # 1,5 s
    g = 10 ** (-DB_SPAN * (1 - ten_s) / 20)
    m = M['mr1']
    gate = np.where(t < m - MR_HOLD - MR_REL, 1.0,
                    np.where(t < m - MR_HOLD, 0.5 + 0.5 * np.cos(np.pi * (t - (m - MR_HOLD - MR_REL)) / MR_REL),
                             np.where(t < m + MR_HOLD, 0.0, np.clip((t - m - MR_HOLD) / MR_IN, 0, 1))))
    fade = np.clip(t / 0.8, 0, 1) * np.clip((total - t) / 1.5, 0, 1)
    env = np.interp(np.arange(N) / SR, t, g * gate * fade)
    mus = wet * env[:, None]
    mus = mus / max(1e-9, np.abs(mus).max()) * 0.5
    beats = []
    for b in bars:
        beats += [b['t0'] + k * b['len'] / 4 for k in range(4)]
    info = {'bpm': BPM, 'bpm_act2_outro': round(bpmB, 3), 'mr1': round(m, 3), 'mr1_silence': [round(m - MR_HOLD, 3), round(m + MR_HOLD, 3)],
            'landing': round(land, 3), 'key_change': round(M['key_change'], 3), 'db_span': DB_SPAN, 'beats': [round(x, 4) for x in beats],
            'bars': [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in b.items()} for b in bars]}
    return mus, info


def main():
    total, out = float(sys.argv[1]), sys.argv[2]
    tl = sys.argv[sys.argv.index('--timeline') + 1] if '--timeline' in sys.argv else None
    M = TM.build(tl)
    mus, info = render(total, M)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    import soundfile as sf
    sf.write(out, mus, SR, subtype='PCM_24')
    json.dump({**info, 'tension': M}, open(out + '.json', 'w'), indent=1, ensure_ascii=False)
    print('bed', out, total, 's ·', info['bpm'], '/', info['bpm_act2_outro'], 'BPM · MR1', info['mr1_silence'], '· landing', info['landing'])


if __name__ == '__main__':
    main()

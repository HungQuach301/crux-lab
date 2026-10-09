"""Tập 6 · F-3 + episode.md §5b — nhạc nền cả tập SINH BẰNG MÃ theo bản đồ căng (tension.py), style C (G-016), MỖI HỒI MỘT CUE, không lặp vòng.
Mẫu: episodes/ep005/world/music/bed.py (cùng họ nhạc cụ toolkit/factory/world/audio.py: pad, pluck, bass, thump, shaker, felt, bell, reverb).
  python3 episodes/ep006/world/music/bed.py <seconds> <out.wav> [--timeline episodes/ep006/out/factory/timeline.json]
  (episode.yaml → audio.music_cmd). Ra thêm <out>.json: lưới phách, ô nhịp (cue, khoá, hợp âm, căng, tầng), cue theo hồi, các khoảng lặng.
Ra nhạc KHÔ + reverb, chưa trộn: mức dưới lời (20 dB, A07) và né 1–4 kHz (13 dB) do toolkit/factory/music.py làm khi trộn.

Cue theo hồi (ô nhịp bắt đầu lại đúng ở đầu mỗi cue; mỗi cue một khoá + một bộ hình ostinato + một bộ tầng riêng; G-002 trong cue: không chuỗi 4 hợp
âm nào lặp trong 24 ô, mỗi ô một hình khác ô trước):
  Q  cold open  S01 → hết lời S03   D dorian, pluck thưa, chuông hỏi (câu hỏi của Ruth) — tắt trước ident (F-12 phát ident A ở 3 s cuối đuôi S03)
  A1 Hồi 1      S04 → MR1           C dorian (D dorian −2), pad + bass, pluck đi lên từng bậc (năm theo năm)
  A2 Hồi 2      MR1 → S24           E dorian (+2), nhịp trầm + shaker khi căng, chuông ở đỉnh "seventeen" (phát lại 715 quãng)
  A3 Hồi 3      S24 → S31           F trưởng, ba giọng pluck so le (ba người, cùng mức tăng)
  O  kết        S31 → hết           F trưởng, chỉ pad + pluck thưa; KHÚC ĐÓNG A (toolkit/factory/theme/close-A.wav) đặt sao cho điểm chạm (8,421 s)
                                    rơi 0,6 s sau chữ cuối của tập; music.post nâng +12 dB sau chữ cuối (close_lift_db)
Lặng: MR1 [t − 0,6; t + 0,6] (≥ 1 s); ident [đuôi S03 − 3 s; hết S03] (nhạc nền nhường ident); 0,8 s TRƯỚC mỗi số neo (tension.ANCHORS: đầu câu
S11.1, S14.1, S25.1 — trong đuôi lời của cảnh trước, không thêm giây vào tập); nhả cos 0,2 s, vào lại 0,25 s (G-003: không cắt cứng).
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
import audio as WA  # noqa: E402
import tension as TM  # noqa: E402

SR = WA.SR
BPM = 114.0
DB_SPAN = 1.0
MR_HOLD, REL, RIN = 0.6, 0.2, 0.25
ANCHOR_SIL = 0.75                      # lặng trước số neo (episode.md §5b: 0,7–0,9 s); đuôi S13 chỉ 1,0 s
CLOSE = 'toolkit/factory/theme/close-A.wav'
CLOSE_TOUCH, CLOSE_AFTER_LAST = 8.421, 0.6
hz = WA.hz
NOTE = {'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
CHORDS = {
    'F major': {'I': ('F', ''), 'V': ('C', ''), 'vi': ('D', 'm'), 'IV': ('Bb', ''), 'ii': ('G', 'm'), 'iii': ('A', 'm'), 'Iadd9': ('F', 'add9'),
                'IVmaj7': ('Bb', 'maj7')},
    'D dorian': {'i': ('D', 'm'), 'i7': ('D', 'm7'), 'IV': ('G', ''), 'IVadd9': ('G', 'add9'), 'VII': ('C', ''), 'III': ('F', ''), 'v': ('A', 'm'),
                 'ii': ('E', 'm')},
}
MARKOV = {
    'F major': {'I': ['IV', 'vi', 'V', 'ii', 'iii', 'IVmaj7'], 'Iadd9': ['vi', 'IV', 'ii'], 'IV': ['I', 'V', 'ii', 'Iadd9', 'vi'], 'IVmaj7': ['V', 'I', 'iii'],
                'V': ['I', 'vi', 'IV', 'Iadd9'], 'vi': ['IV', 'ii', 'V', 'IVmaj7'], 'ii': ['V', 'I', 'IV'], 'iii': ['vi', 'IV', 'ii']},
    'D dorian': {'i': ['IV', 'VII', 'III', 'IVadd9', 'v'], 'i7': ['IV', 'VII', 'ii'], 'IV': ['i', 'VII', 'i7', 'III', 'v'], 'IVadd9': ['i', 'VII', 'III'],
                 'VII': ['IV', 'i', 'III', 'i7'], 'III': ['IV', 'VII', 'i', 'ii'], 'v': ['IV', 'VII', 'i'], 'ii': ['IV', 'i7', 'v']},
}
TONIC = {'F major': 'I', 'D dorian': 'i'}
OST = [[0, 2, 3, 6, 8, 10, 11, 14], [0, 3, 6, 8, 9, 11, 14, 15], [0, 2, 3, 6, 8, 11, 12, 14], [0, 3, 4, 6, 8, 10, 12, 14], [0, 2, 3, 5, 6, 8, 11, 14],
       [0, 4, 6, 8, 10, 12, 14, 15], [0, 1, 4, 6, 8, 9, 12, 14], [0, 3, 5, 8, 10, 11, 13, 14]]
ACC16 = {0, 3, 6, 8, 11, 14}
BELL_RHY = [[0, 6, 10], [2, 8, 12], [0, 4, 11], [3, 8, 14], [0, 10]]
# cue: (khoá, dịch nửa cung, hình ostinato được dùng, dáng giai điệu, tầng được phép, hệ số nhịp trầm)
CUES = {
    'Q': ('D dorian', 0, [0, 2], ['up', 'pedal'], {'bell'}, 0.0),
    'A1': ('D dorian', -2, [1, 3, 5], ['up', 'broken', 'updown'], {'bass8'}, 0.6),
    'A2': ('D dorian', 2, [0, 4, 6, 7], ['broken', 'down', 'updown', 'up'], {'bass8', 'kick', 'shaker', 'bell'}, 1.0),
    'A3': ('F major', 0, [2, 3, 7], ['updown', 'up', 'pedal'], {'bass8', 'kick', 'bell'}, 0.8),
    'O': ('F major', 0, [0], ['pedal'], set(), 0.0),
}


def chord_pcs(key, name, tr):
    root, q = CHORDS[key][name]
    r = (NOTE[root] + tr) % 12
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


def sections(M):
    """[(cue, t0, t1)]: ô nhịp bắt đầu lại ở đầu mỗi cue."""
    s = M['scenes']
    last_s03 = s['S04'] - 0.0
    q_end = M['ident'][0]
    a1_0 = M['ident'][1] - 0.2
    a1_1 = M['mr1'] - MR_HOLD if M['mr1_break'] else s['S13'] - 0.4
    a2_0 = M['mr1'] + MR_HOLD if M['mr1_break'] else a1_1
    a3_0 = s['S24'] - 0.5
    o_0 = s['S31'] - 0.5
    return [('Q', 0.0, q_end), ('A1', a1_0, a1_1), ('A2', a2_0, a3_0), ('A3', a3_0, o_0), ('O', o_0, M['total'] + 2)], last_s03


def grid(M):
    bar = 4 * 60 / BPM
    secs, _ = sections(M)
    bars = []
    for cue, a, b in secs:
        n = max(1, round((b - a) / bar))
        L = (b - a) / n                                            # co giãn ≤ ½ ô để cue kết đúng mép (nhịp đổi < 4 %)
        for k in range(n):
            bars.append({'t0': a + k * L, 't1': a + (k + 1) * L, 'len': L, 'cue': cue})
    return bars


def harmony(bars):
    rng = np.random.default_rng(1006)
    seq = []
    for i, b in enumerate(bars):
        key = CUES[b['cue']][0]
        b['key'] = key
        first = i == 0 or bars[i - 1]['cue'] != b['cue']
        if first:
            c = TONIC[key]
        else:
            prev = seq[-1]
            hist = [x for x, bb in zip(seq, bars) if bb['cue'] == b['cue']][-24:]
            for attempt in range(200):
                opts = MARKOV[key].get(prev, [TONIC[key]])
                c = opts[rng.integers(0, len(opts))]
                cand = hist + [c]
                if len(cand) >= 4 and attempt < 180 and any(cand[j:j + 4] == cand[-4:] for j in range(0, max(0, len(cand) - 4))):
                    continue
                if c == prev and attempt < 150:
                    continue
                break
        seq.append(c)
        b['chord'] = c
    return seq


def render(total, M, seed=1006):
    rng = np.random.default_rng(seed)
    N = int(round(total * SR))
    dry = np.zeros((N, 2))
    bars = grid(M)
    harmony(bars)
    ten_at = lambda t: TM.curve([(k['t'], k['v']) for k in M['keyframes']], t)
    secs, _ = sections(M)
    end_of = {c: b for c, a, b in secs}
    prev_vo, prev_fig = None, None
    for i, b in enumerate(bars):
        t0, L, cue = b['t0'], b['len'], b['cue']
        key, tr, figs, shapes, allow, kick = CUES[cue]
        stop = end_of[cue]
        beat = L / 4
        ten = float(np.mean(ten_at(np.linspace(t0, t0 + L, 9))))
        b['ten'] = round(ten, 3)
        r, pcs = chord_pcs(key, b['chord'], tr)
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
        WA.add(dry, t0, WA.pad(hz(vo), min(L + 0.6, stop - t0), 0.05 + 0.20 * ten, 700 + 1800 * ten))
        broot = 36 + (r % 12) + (12 if (r % 12) < 2 else 0)
        if ten < 0.3 or 'bass8' not in allow:
            for e in (0, 4):
                t = t0 + e * beat / 2
                if t < stop: WA.add(dry, t, WA.bass(hz(broot), 0.15, 0.9 * beat))
        else:
            layers.append('bass8')
            for e in range(8):
                t = t0 + e * beat / 2
                if t >= stop: break
                WA.add(dry, t, WA.bass(hz(broot + (12 if e % 2 else 0)), (0.2 if e % 2 == 0 else 0.11) * (0.4 + 0.6 * ten) * rng.uniform(0.92, 1.05), 0.45 * beat))
        if 'kick' in allow and kick > 0:
            if ten >= 0.72: layers.append('kick4')
            elif ten >= 0.5: layers.append('kick2')
            for k in range(4):
                t = t0 + k * beat
                if t >= stop: break
                if ten >= 0.72 or (ten >= 0.5 and k % 2 == 0):
                    WA.add(dry, t, WA.thump(kick * (0.5 if k == 0 else 0.36) * (0.3 + 0.6 * ten) * rng.uniform(0.92, 1.05)))
        if 'shaker' in allow and ten >= 0.58:
            layers.append('shaker')
            for s in (range(16) if ten >= 0.8 else range(2, 16, 4)):
                t = t0 + s * beat / 4
                if t >= stop: break
                WA.add(dry, t, WA.shaker((0.05 + 0.08 * ten) * (1.0 if s % 4 == 2 else 0.55)), 0.3 if s % 8 < 4 else -0.3)
        tones = [n_ for n_ in range(57, 57 + 17) if n_ % 12 in pcl]
        for _ in range(20):
            shp, mk = shapes[int(rng.integers(0, len(shapes)))], figs[int(rng.integers(0, len(figs)))]
            if (shp, mk) != prev_fig: break
        prev_fig = (shp, mk)
        hits = OST[mk] if ten >= 0.62 else (OST[mk][::2] if ten >= 0.3 else OST[mk][::4])
        layers.append(f'pluck{len(hits)}')
        voices = 3 if cue == 'A3' else 1                                 # A3: ba giọng so le (ba người, cùng một mức tăng)
        for vce in range(voices):
            off = vce * beat / 3
            for j, h in enumerate(hits):
                t = t0 + h * beat / 4 + off
                if t >= stop: break
                v = (0.16 if h in ACC16 else 0.1) * (0.45 + 0.6 * ten) * rng.uniform(0.88, 1.08) / (1 + 0.6 * vce)
                WA.add(dry, t, WA.pluck(hz(contour(shp, tones, j) + (12 if vce == 1 else 0)), v, 1500 + 1500 * ten, 0.3), (0.22 if j % 2 else -0.22) * (1 - 2 * (vce == 2)))
        if 'bell' in allow and (ten >= 0.8 or cue == 'Q' and (i % 2 == 1)):
            layers.append('bell')
            hi = [n_ for n_ in range(74, 88) if n_ % 12 in pcl]
            for j, s in enumerate(BELL_RHY[int(rng.integers(0, len(BELL_RHY)))]):
                t = t0 + s * beat / 4
                if t < stop: WA.add(dry, t, WA.lp1(WA.bell(hz(hi[int(rng.integers(0, len(hi)))]), (0.045 if cue != 'Q' else 0.03) * max(ten, 0.5), 1.6), 3200), 0.35 if j % 2 else -0.35)
        if i > 0 and bars[i - 1]['cue'] != cue:                          # cue mới vào ở phách mạnh
            WA.add(dry, t0, WA.felt(hz(36 + r % 12), 0.3)); layers.append('cue-entry')
        b['layers'] = layers
    for a, t in M['accents']:
        WA.add(dry, t, WA.felt(hz(38), 0.34)); WA.add(dry, t, WA.felt(hz(45), 0.16), 0.1)
    wet = WA.reverb(dry, 1.9, 0.24)[:N]
    # gain liên tục theo căng + cổng lặng (MR1, ident, số neo) + vào/ra
    t = np.arange(0, N, 480) / SR
    g = 10 ** (-DB_SPAN * (1 - uniform_filter1d(ten_at(t), 150)) / 20)
    gate = np.ones_like(t)
    sil = []
    if M['mr1_break']:
        sil.append(('MR1', M['mr1'] - MR_HOLD, M['mr1'] + MR_HOLD))
    sil.append(('ident', M['ident'][0], M['ident'][1]))
    for a, ta in M['anchors']:
        sil.append((f'anchor {a}', ta - ANCHOR_SIL - 0.05, ta - 0.05))
    for _, a, b in sil:
        d = np.where(t < a, (a - t) / REL, np.where(t > b, (t - b) / RIN, 0.0))
        gate = np.minimum(gate, np.where(d >= 1, 1.0, 0.5 - 0.5 * np.cos(np.pi * np.clip(d, 0, 1))))
    fade = np.clip(t / 0.8, 0, 1)
    env = np.interp(np.arange(N) / SR, t, g * gate * fade)
    mus = wet * env[:, None]
    mus = mus / max(1e-9, np.abs(mus).max()) * 0.5
    # khúc đóng A: điểm chạm 0,6 s sau chữ cuối; nhạc của cue O nhường dần trong 1,5 s trước khi khúc đóng vào
    import soundfile as sf
    cl, csr = sf.read(os.path.join(ROOT, CLOSE), always_2d=True)
    assert csr == SR
    c0 = M['last_word'] + CLOSE_AFTER_LAST - CLOSE_TOUCH
    i0 = int(round(c0 * SR))
    pre = mus[max(0, i0 - 20 * SR):i0]
    lvl = np.sqrt(np.mean(pre ** 2) + 1e-12) / np.sqrt(np.mean(cl[:int(CLOSE_TOUCH * SR)] ** 2) + 1e-12)
    tt = np.arange(N) / SR
    mus *= np.clip((c0 + 1.5 - tt) / 1.5, 0, 1)[:, None] ** 2
    n = min(len(cl), N - i0)
    mus[i0:i0 + n] += cl[:n] * lvl
    tail = np.clip((total - tt) / 0.4, 0, 1)                             # 0,4 s cuối: tắt (khúc đóng dài hơn đuôi S32)
    mus *= tail[:, None]
    beats = [b['t0'] + k * b['len'] / 4 for b in bars for k in range(4)]
    cues = []
    for cue, a, b in secs:
        bb = [x for x in bars if x['cue'] == cue]
        cues.append({'t': round(a, 3), 'end': round(min(b, total), 3), 'function': {'Q': 'cold open', 'A1': 'act 1', 'A2': 'act 2 replay', 'A3': 'act 3 people',
                     'O': 'limits + outro'}[cue], 'cue': cue, 'key': CUES[cue][0] + (f' {CUES[cue][1]:+d}' if CUES[cue][1] else ''),
                     'tempo': round(240 / bb[0]['len'], 2) if bb else BPM, 'bars': len(bb)})
    cues.append({'t': round(c0, 3), 'end': round(total, 3), 'function': 'closing cue A (F-12)', 'cue': 'close-A', 'key': 'F major', 'tempo': 114.0,
                 'touch': round(c0 + CLOSE_TOUCH, 3)})
    info = {'bpm': BPM, 'mr1': round(M['mr1'], 3), 'mr1_silence': [round(M['mr1'] - MR_HOLD, 3), round(M['mr1'] + MR_HOLD, 3)] if M['mr1_break'] else None,
            'silences': [{'what': w, 't': round(a, 3), 'end': round(b, 3)} for w, a, b in sil], 'cues': cues, 'close': {'t0': round(c0, 3), 'touch': round(c0 + CLOSE_TOUCH, 3),
            'last_word': round(M['last_word'], 3), 'gain': round(float(lvl), 4)}, 'db_span': DB_SPAN, 'beats': [round(x, 4) for x in beats],
            'accents': [{'at': a, 't': round(t, 3)} for a, t in M['accents']],
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
    print('bed', out, total, 's · cues', [(c['cue'], c['t']) for c in info['cues']], '· silences', [(s['what'], s['t']) for s in info['silences']])


if __name__ == '__main__':
    main()

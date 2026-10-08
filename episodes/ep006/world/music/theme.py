"""Tập 6 · nhạc hiệu kênh (playbook/episode.md §5b) — SINH BẰNG MÃ (D-010 §5), không mẫu tải về, không tài sản bên thứ ba.
Một lần cho cả kênh: ident 3,0 s (IDENT_S, sau cold open) + một khúc đóng KHÁC (≈ 10,5 s, chạy dưới câu kết / thẻ cuối).
Cùng họ nhạc cụ style C của nhà máy (toolkit/factory/world/audio.py: pad, pluck, bass, thump, shaker, felt, bell, glide, reverb), F trưởng.

  python3 episodes/ep006/world/music/theme.py [out_dir]      (mặc định episodes/ep006/world/music/out)
Ra: ident-A.wav, ident-B.wav, close-A.wav, close-B.wav (48 kHz stereo float), theme.json (mốc "chạm", LUFS/TP đo bằng ffmpeg ebur128).

  A (khuyến nghị) "câu hỏi → lời giải": 114 BPM (style C, G-016·chọn), pad IV → Vsus4 → V → I; motif pluck 5 nốt đi lên
     C–D–F–G–A (câu hỏi), CHẠM ở phách 5 (2,105 s) = F add9: chuông + felt + bass F1 + nhịp trầm; đuôi tắt hẳn ở 2,96 s.
  B "dụng cụ đo ổn định": 132 BPM, không tiến hành hợp âm; tick lọc mềm 4,5–7 kHz (họ âm dữ liệu S2) đếm 16 phần, hai đường
     glide hội tụ từ Bb/C về quãng tám F (kim đồng hồ đo dừng ở số đọc), CHẠM ở 2,0 s = một cao độ F (đồng âm, không hợp âm).
  Khúc đóng (hợp A): 114 BPM, 4 ô xuyên suốt không lặp (vi7 → IVmaj7 → ii7 → Vsus4·V) rồi chạm I add9 ở 8,42 s, tắt ở 10,45 s;
     ô 4 nhắc motif của ident dạng giãn (nốt đen) và đáp xuống A5 (ident đáp C6) → cùng chất liệu, không phải bản lặp.
     --variant B (close-B.wav): ô 4 thay bằng glide hội tụ + tick của B, chạm đồng âm F.
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
sys.dont_write_bytecode = True
import audio as WA  # noqa: E402  (chỉ đọc/gọi: nhạc cụ style C của nhà máy)
from scipy import signal  # noqa: E402

SR = WA.SR
hz = WA.hz
IDENT_S = 3.0
TARGET_LUFS = -16.0      # mức đứng riêng của từng file (ident nằm giữa lời −14 LUFS; khúc đóng được nhà máy đặt lại −20 dB dưới lời)
CLOSE_LUFS = -18.0       # khúc đóng đứng riêng; trong tập nhà máy đặt lại 20 dB dưới lời (music.py)
TP_MAX = -1.5            # dBTP mỗi file (bản trộn tập: ≤ −1)


def buf(sec):
    return np.zeros((int(round(sec * SR)), 2))


def tick(vel, rng):
    """Tick lọc mềm 4,5–7 kHz (họ bảng âm S2 'minimal', G-005·chọn) — không bíp."""
    n = int(0.05 * SR); t = np.arange(n) / SR
    x = signal.sosfilt(signal.butter(2, [4500, 7000], 'band', fs=SR, output='sos'), rng.standard_normal(n))
    return x / (np.abs(x).max() + 1e-9) * WA.env_ar(t, 0.002, 0.012) * vel


def tail_window(x, t_fade0, t_end):
    """Đuôi tắt TRONG khung (G-003: không cắt cứng): nửa cos từ t_fade0 tới t_end, 0 sau đó."""
    n = len(x); t = np.arange(n) / SR
    w = np.where(t < t_fade0, 1.0, np.where(t >= t_end, 0.0, 0.5 + 0.5 * np.cos(np.pi * (t - t_fade0) / (t_end - t_fade0))))
    return x * w[:, None]


def touch(x, t, notes_bell, notes_felt, bass_m, vel=1.0, low=0.7):
    for m in notes_bell: WA.add(x, t, WA.bell(hz(m), 0.10 * vel, 1.4), pan=0.15)
    for k, m in enumerate(notes_felt): WA.add(x, t, WA.felt(hz(m), 0.16 * vel, 1.2), pan=(-0.25, 0.0, 0.25)[k % 3])
    WA.add(x, t, WA.bass(hz(bass_m), 0.42 * vel * low, 0.8))
    WA.add(x, t, WA.thump(0.75 * vel * low))


# ------------------------------------------------------------------ ident A — câu hỏi → lời giải (khuyến nghị)
def ident_a():
    b = 60 / 114.0; x = buf(IDENT_S); T = 4 * b                       # chạm ở phách 5 = 2,105 s
    WA.add(x, 0.0, WA.pad(hz([58, 62, 65, 69]), 2 * b + 0.3, 0.11, 900))          # Bbmaj7 (IV)
    WA.add(x, 2 * b, WA.pad(hz([60, 65, 67]), b + 0.2, 0.12, 1300))               # Csus4
    WA.add(x, 3 * b, WA.pad(hz([60, 64, 67]), b + 0.15, 0.13, 1600))              # C (V)
    WA.add(x, T, WA.pad(hz([53, 57, 60, 67]), 0.85, 0.16, 1500))                  # F add9 (I)
    for t, m in ((0.0, 34), (2 * b, 36)): WA.add(x, t, WA.bass(hz(m), 0.20, 1.6 * b))
    motif = [(1.0, 72), (1.5, 74), (2.0, 77), (3.0, 79), (3.5, 81)]                # C5 D5 F5 · G5 A5 → chạm
    for k, (bt, m) in enumerate(motif): WA.add(x, bt * b, WA.pluck(hz(m), 0.30 + 0.05 * k, 2300, 0.45), pan=0.2 * ((-1) ** k))
    rng = np.random.default_rng(6)
    for s in range(8, 16):                                                         # shaker dâng 16 phần trong phách 3–4
        WA.add(x, s * b / 4, WA.shaker(0.03 + 0.008 * (s - 8)), pan=0.3 if s % 2 else -0.3)
    WA.add(x, T - 0.55, WA.noise_sweep(0.55, 900, 6000, 0.035, 0.45))              # hơi thở vào điểm chạm
    touch(x, T, [77, 84], [65, 69, 72], 29)                                        # chuông F5+C6, felt F4 A4 C5, bass F1
    x = WA.reverb(x, rt60=1.1, wet=0.20)
    return tail_window(x, T + 0.45, 2.96), {'bpm': 114, 'touch_s': round(T, 3), 'beats_s': [round(k * b, 3) for k in range(5)],
                                            'motif_s': [round(bt * b, 3) for bt, _ in motif]}


# ------------------------------------------------------------------ ident B — dụng cụ đo ổn định
def ident_b():
    b = 60 / 132.0; t0 = 0.18; x = buf(IDENT_S); T = t0 + 4 * b                   # chạm 2,0 s
    rng = np.random.default_rng(16)
    for s in range(16):                                                            # tick đếm 16 phần, mạnh dần, nhấn mỗi phách
        WA.add(x, t0 + s * b / 4, tick((0.05 + 0.10 * s / 15) * (1.0 if s % 4 == 0 else 0.55), rng), pan=0.35 * np.sin(s * 0.9))
    for k in range(4): WA.add(x, t0 + k * b, WA.thump(0.22 + 0.06 * k))
    g0 = 0.25; L = T - g0 + 0.05                                                    # kim dừng: Bb3→F4 và C6→F5 hội tụ thành quãng tám
    WA.add(x, g0, WA.glide(58, 65, L, 0.07), pan=-0.3)
    WA.add(x, g0, WA.glide(84, 77, L, 0.045), pan=0.3)
    WA.add(x, g0, WA.pad(hz([53, 60]), L, 0.06, 700))                              # nền quãng năm trống F–C, không ba
    touch(x, T, [77], [53, 65], 29, vel=1.05, low=0.55)                                      # chạm đồng âm F: chuông F5, felt F3 F4, bass F1
    x = WA.reverb(x, rt60=0.9, wet=0.16)
    return tail_window(x, T + 0.5, 2.96), {'bpm': 132, 'touch_s': round(T, 3), 'beats_s': [round(t0 + k * b, 3) for k in range(5)]}


# ------------------------------------------------------------------ khúc đóng (hợp A; --variant B đổi ô 4)
CLOSE_BARS = [  # (hợp âm pad, gốc bass, nốt ostinato, mặt nạ 16 phần) — mỗi ô một dáng, không ô nào lặp
    ([62, 65, 69, 72], 38, [69, 72, 74, 76, 74, 72], [0, 3, 6, 8, 11, 14]),        # Dm7 (vi7)
    ([58, 62, 65, 69], 34, [70, 74, 77, 74, 69, 72], [0, 2, 6, 8, 10, 14]),        # Bbmaj7 (IVmaj7)
    ([55, 58, 62, 65], 31, [67, 70, 74, 77, 74, 70, 74], [0, 3, 4, 8, 11, 12, 14]),  # Gm7 (ii7)
]


def close(variant='A'):
    b = 60 / 114.0; bar = 4 * b; T = 4 * bar; total = 10.5; x = buf(total)
    rng = np.random.default_rng(1006)
    for i, (pc, br, ost, mask) in enumerate(CLOSE_BARS):
        t0 = i * bar
        WA.add(x, t0, WA.pad(hz(pc), bar + 0.5, 0.10 + 0.015 * i, 900 + 250 * i))
        for e in (0, 2, 3) if i else (0, 2):
            WA.add(x, t0 + e * b, WA.bass(hz(br), 0.17 * (1.0 if e == 0 else 0.7), 0.9 * b))
        for k, s in enumerate(mask):
            WA.add(x, t0 + s * b / 4, WA.pluck(hz(ost[k % len(ost)]), (0.20 if s % 4 == 0 else 0.13) * rng.uniform(0.92, 1.05), 1900, 0.4),
                   pan=0.25 * np.sin(k + i))
        if i >= 1:
            for k in range(4): WA.add(x, t0 + k * b, WA.thump(0.20 if k % 2 == 0 else 0.13))
        if i == 2:
            for s in range(2, 16, 4): WA.add(x, t0 + s * b / 4, WA.shaker(0.05), pan=0.3)
    t0 = 3 * bar
    if variant == 'A':                                                             # ô 4: Csus4 → C, motif ident giãn nốt đen
        WA.add(x, t0, WA.pad(hz([60, 65, 67, 72]), 2 * b + 0.3, 0.14, 1500))
        WA.add(x, t0 + 2 * b, WA.pad(hz([60, 64, 67, 72]), 2 * b + 0.2, 0.15, 1800))
        for e in range(8): WA.add(x, t0 + e * b / 2, WA.bass(hz(36 + (12 if e % 2 else 0)), 0.18 if e % 2 == 0 else 0.10, 0.45 * b))
        for k, m in enumerate([72, 74, 77, 79]): WA.add(x, t0 + k * b, WA.pluck(hz(m), 0.26 + 0.03 * k, 2200, 0.5), pan=0.2 * ((-1) ** k))
        for s in range(0, 16, 2): WA.add(x, t0 + s * b / 4, WA.shaker(0.035 + 0.003 * s), pan=0.3 if s % 4 else -0.3)
        for k in range(4): WA.add(x, t0 + k * b, WA.thump(0.24))
        WA.add(x, T - 0.6, WA.noise_sweep(0.6, 900, 6000, 0.03, 0.5))
        touch(x, T, [81, 77], [65, 69, 72, 79], 29, low=0.5)                               # chuông A5+F5, felt F4 A4 C5 G5 (add9)
        WA.add(x, T, WA.pad(hz([53, 57, 60, 67]), 2.0, 0.13, 1400))
    else:                                                                          # ô 4 kiểu B: glide hội tụ + tick, chạm đồng âm
        for s in range(16): WA.add(x, t0 + s * b / 4, tick((0.05 + 0.08 * s / 15) * (1.0 if s % 4 == 0 else 0.55), rng), pan=0.35 * np.sin(s))
        for k in range(4): WA.add(x, t0 + k * b, WA.thump(0.22))
        WA.add(x, t0, WA.glide(58, 65, bar + 0.05, 0.06), pan=-0.3)
        WA.add(x, t0, WA.glide(84, 77, bar + 0.05, 0.04), pan=0.3)
        WA.add(x, t0, WA.pad(hz([53, 60]), bar, 0.07, 800))
        touch(x, T, [77], [53, 65], 29, low=0.5)
        WA.add(x, T, WA.pad(hz([53, 60, 65]), 2.0, 0.11, 1100))
    x = WA.reverb(x, rt60=1.6, wet=0.22)
    return tail_window(x, T + 1.15, total - 0.05), {'bpm': 114, 'bar_s': round(bar, 3), 'touch_s': round(T, 3), 'len_s': total,
                                                    'chords': ['Dm7', 'Bbmaj7', 'Gm7', 'Csus4-C' if variant == 'A' else 'F5 glide', 'Fadd9' if variant == 'A' else 'F unison']}


# ------------------------------------------------------------------ mức + đo (ffmpeg ebur128)
def ebur(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
    s = r.stderr[r.stderr.rfind('Summary:'):]
    g = lambda k: float(re.search(k + r':\s+(-?[\d.]+|-inf)', s).group(1).replace('-inf', '-120'))
    return {'I_lufs': g('I'), 'tp_dbtp': g('Peak'), 'lra_lu': g('LRA')}


def limit(x, ceil_db):
    """Giới hạn đỉnh nhìn trước 5 ms, nhả 80 ms (chỉ đỉnh của điểm chạm; đuôi không đổi)."""
    from scipy.ndimage import maximum_filter1d, uniform_filter1d
    la = int(0.005 * SR); c = 10 ** (ceil_db / 20)
    env = maximum_filter1d(np.abs(x).max(1), 2 * la + 1)
    g = np.minimum(1.0, c / (env + 1e-12))
    g = np.minimum(g, uniform_filter1d(maximum_filter1d(1 - g, int(0.08 * SR)), la, mode='nearest') * -1 + 1)
    g = np.minimum(g, c / (np.abs(x).max(1) + 1e-12))
    return x * g[:, None], float(-20 * np.log10(g.min()))


def level(x, path, target=TARGET_LUFS):
    sf.write(path, x, SR, subtype='FLOAT')
    m = ebur(path)
    gdb, gr = target - m['I_lufs'], 0.0
    for _ in range(4):                                                             # mức đích, rồi giới hạn đỉnh tới trần TP, lặp cho khớp LUFS
        y, gr = limit(x * 10 ** (gdb / 20), TP_MAX - 0.6)
        sf.write(path, y, SR, subtype='FLOAT')
        m = ebur(path)
        if abs(m['I_lufs'] - target) < 0.15 and m['tp_dbtp'] <= TP_MAX: break
        gdb += target - m['I_lufs'] + min(0.0, TP_MAX - m['tp_dbtp'])
    m['gain_db'] = round(gdb, 2); m['limiter_max_gr_db'] = round(gr, 2)
    tailp = np.abs(sf.read(path)[0][-int(0.04 * SR):]).max()
    m['last40ms_peak_dbfs'] = float(round(20 * np.log10(tailp + 1e-12), 1))
    return m


def main(out):
    os.makedirs(out, exist_ok=True)
    rep = {'sr': SR, 'target_lufs': {'ident': TARGET_LUFS, 'close': CLOSE_LUFS}, 'tp_max_dbtp': TP_MAX, 'files': {}}
    for name, fn in (('ident-A', ident_a), ('ident-B', ident_b), ('close-A', lambda: close('A')), ('close-B', lambda: close('B'))):
        x, meta = fn()
        p = os.path.join(out, name + '.wav')
        meta.update(level(x, p, TARGET_LUFS if name.startswith('ident') else CLOSE_LUFS)); meta['dur_s'] = round(len(x) / SR, 3)
        rep['files'][name] = meta
        print(name, meta)
    json.dump(rep, open(os.path.join(out, 'theme.json'), 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out'))

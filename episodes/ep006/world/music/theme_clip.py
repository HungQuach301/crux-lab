"""Tập 6 · C3 — clip duyệt nhạc hiệu (có chuyển động + âm) → episodes/ep006/review-c3/music-ident.mp4 (960×540, 30 fps, H.264 + AAC).
  python3 episodes/ep006/world/music/theme.py && python3 episodes/ep006/world/music/theme_clip.py
Trình tự: [ident A 0–3 s] · lặng 3–4 · [ident B 4–7 s] · lặng 7–8 · [khúc đóng A 8–18,5 s dưới câu kết mẫu].
Câu kết mẫu = take có sẵn voice-takes/7ac4b74ef01702a7.mp3 12,58–18,76 s ("This is U.S. only, and it's history, not a forecast.
It doesn't say which check to choose.") — 0 ký tự ElevenLabs. Trộn bằng hàm của nhà máy toolkit/factory/music.py mix()
(nhạc 20 dB dưới lời theo cách đo A07, 1–4 kHz né 13 dB). Mức: khúc đóng + lời −14 LUFS (mức tập); ident giữ −16 LUFS như file.
Hình: thẻ ident của kênh như Tập 5 (C4 đoạn A: "CRUX" + "decision lab · US personal finance" trên nền #0E1116, hiện 0,3–0,8 s,
tắt ở 0,8–0,2 s trước hết) + chuyển động tối giản theo nhịp: A = gạch chân vẽ theo 5 nốt motif rồi khép ở điểm chạm;
B = thang 16 vạch sáng theo tick, kim dao động tắt dần về giữa ở điểm chạm. Nhãn nhỏ A / B / close ở góc trên trái.
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import music as MUSIC  # noqa: E402  (chỉ gọi: mức lời/nhạc của nhà máy)
import theme as TH  # noqa: E402

SR, FPS, W, H = 48000, 30, 960, 540
OUT = os.path.join(HERE, 'out')
WORK = os.path.join(OUT, 'clip-work')
DST = os.path.join(EP, 'review-c3', 'music-ident.mp4')
TAKE = os.path.join(EP, 'voice-takes', '7ac4b74ef01702a7.mp3')
V0, V1, V_AT = 12.58, 18.756, 1.0                     # đoạn take, chỗ đặt trong khúc đóng
SEG = [('A', 0.0, 3.0), (None, 3.0, 4.0), ('B', 4.0, 7.0), (None, 7.0, 8.0), ('close', 8.0, 18.5)]
TOTAL = 18.5
LIFT_DB = 12.0                                        # nhạc lên sau chữ cuối của câu kết
CAPS = [(12.656, 16.0, "This is U.S. only, and it's history, not a forecast."), (16.133, 18.72, "It doesn't say which check to choose.")]
BG, INK, MUTED, ACCENT, GRID = (14, 17, 22), (242, 244, 247), (154, 164, 178), (76, 141, 255), (42, 48, 59)
FONT = '/usr/share/fonts/opentype/inter/'
F_MARK = ImageFont.truetype(FONT + 'Inter-SemiBold.otf', 80)
F_TAG = ImageFont.truetype(FONT + 'Inter-Regular.otf', 32)
F_LAB = ImageFont.truetype(FONT + 'Inter-Medium.otf', 20)
F_CAP = ImageFont.truetype(FONT + 'Inter-Regular.otf', 28)


def sh(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def ease(t, a, b):
    u = np.clip((t - a) / max(b - a, 1e-6), 0, 1); return float(u * u * (3 - 2 * u))


def mix_rgb(c, a):
    return tuple(int(BG[i] + (c[i] - BG[i]) * a) for i in range(3))


# ------------------------------------------------------------------ âm
def audio(meta):
    os.makedirs(WORK, exist_ok=True)
    N = int(round(TOTAL * SR)); y = np.zeros((N, 2))
    put = lambda x, t: y.__setitem__(slice(int(round(t * SR)), int(round(t * SR)) + len(x)), x)
    put(sf.read(os.path.join(OUT, 'ident-A.wav'))[0], 0.0)
    put(sf.read(os.path.join(OUT, 'ident-B.wav'))[0], 4.0)
    # khúc đóng dưới câu kết: lời take → trộn bằng music.mix() của nhà máy
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(V0), '-to', str(V1), '-i', TAKE, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    v = np.frombuffer(raw, np.float32).astype(np.float64)
    v[:int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))
    close_len = SEG[-1][2] - SEG[-1][1]; vt = np.zeros(int(round(close_len * SR)))
    i0 = int(V_AT * SR); vt[i0:i0 + len(v)] = v[:len(vt) - i0]
    vp, cp = os.path.join(WORK, 'voice.wav'), os.path.join(WORK, 'close-mix.wav')
    sf.write(vp, np.stack([vt, vt], 1), SR, subtype='FLOAT')
    rep = MUSIC.mix(vp, os.path.join(OUT, 'close-A.wav'), close_len, cp, os.path.join(WORK, 'stems'))
    # đuôi lên sau chữ cuối (thẻ cuối không lời): nhạc giữ 20 dB dưới lời khi có lời, rồi +LIFT_DB trong 0,5 s → điểm chạm nghe rõ
    vs, ms = sf.read(os.path.join(WORK, 'stems', 'voice.flac'))[0], sf.read(os.path.join(WORK, 'stems', 'music.flac'))[0]
    tt = np.arange(len(ms)) / SR; vend = V_AT + CAPS[-1][1] - V0 + 0.15
    ms = ms * (10 ** (LIFT_DB * np.array([ease(x, vend, vend + 0.5) for x in tt[::48]]).repeat(48)[:len(ms)] / 20))[:, None]
    rep['a07_gap_db'] = round(MUSIC.a07_gap(vs, ms), 2)
    cm = vs + ms; sf.write(cp, cm, SR, subtype='FLOAT'); m = TH.ebur(cp)
    cm *= 10 ** ((-14.0 - m['I_lufs']) / 20)
    cm, _ = TH.limit(cm, -1.7)                                       # đỉnh của điểm chạm sau khi nhạc lên
    put(cm, 8.0)
    wav = os.path.join(WORK, 'clip.wav'); sf.write(wav, y, SR, subtype='FLOAT')
    m_all = TH.ebur(wav)
    if m_all['tp_dbtp'] > -1.0:
        y *= 10 ** ((-1.0 - m_all['tp_dbtp'] - 0.1) / 20); sf.write(wav, y, SR, subtype='FLOAT'); m_all = TH.ebur(wav)
    sf.write(cp, cm, SR, subtype='FLOAT')
    return wav, {'close_under_voice': {**TH.ebur(cp), 'a07_voice_over_music_db': rep['a07_gap_db'], 'lift_after_last_word_db': LIFT_DB, 'mid_duck_db': rep['mid_duck_db']}, 'clip': m_all}


# ------------------------------------------------------------------ hình
def text_c(d, xy, s, font, fill, anchor='mm', spacing=0):
    if not spacing: d.text(xy, s, font=font, fill=fill, anchor=anchor); return
    ws = [font.getlength(ch) for ch in s]; tot = sum(ws) + spacing * (len(s) - 1); x = xy[0] - tot / 2
    for ch, w in zip(s, ws): d.text((x, xy[1]), ch, font=font, fill=fill, anchor='lm'); x += w + spacing


def card(d, a, sp=6, glow=0.0):
    if a <= 0.01: return
    text_c(d, (W / 2, 268), 'CRUX', F_MARK, mix_rgb(INK, a * min(1, 0.92 + glow)), spacing=sp)
    text_c(d, (W / 2, 340), 'decision lab · US personal finance', F_TAG, mix_rgb(MUTED, a))


def frame_a(d, t, M):
    mk = ease(t, 0.3, 0.8) * (1 - ease(t, 2.2, 2.8))
    T = M['touch_s']; pulse = np.exp(-max(0, t - T) / 0.12) if t >= T else 0
    card(d, mk, sp=int(round(10 - 4 * ease(t, 0.3, T))), glow=0.08 * pulse)
    x0, x1, yl = W / 2 - 150, W / 2 + 150, 374
    pts = M['motif_s'] + [T]
    for k in range(len(pts)):   # gạch chân vẽ theo từng nốt motif; đoạn cuối = điểm chạm
        u = ease(t, pts[k], pts[k] + 0.09)
        if u <= 0: continue
        a0 = x0 + (x1 - x0) * k / len(pts); a1 = a0 + (x1 - x0) / len(pts) * u
        col = ACCENT if k == len(pts) - 1 else INK
        d.line([(a0, yl), (a1, yl)], fill=mix_rgb(col, mk), width=3 if k < len(pts) - 1 else 4)


def frame_b(d, t, M):
    mk = ease(t, 0.3, 0.8) * (1 - ease(t, 2.2, 2.8))
    card(d, mk)
    T, t0 = M['touch_s'], M['beats_s'][0]; st = (T - t0) / 16
    x0, x1, yl = W / 2 - 160, W / 2 + 160, 384
    for s in range(17):         # thang 16 vạch: sáng theo tick
        x = x0 + (x1 - x0) * s / 16; on = t >= t0 + s * st
        hgt = 12 if s % 4 == 0 else 7
        col = (ACCENT if s == 8 and t >= T else INK if on else GRID)
        d.line([(x, yl - hgt), (x, yl)], fill=mix_rgb(col, mk), width=2)
    if t >= 0.25:               # kim: dao động tắt dần, dừng ở giữa đúng điểm chạm (theo glide hội tụ)
        u = np.clip((t - 0.25) / (T - 0.25), 0, 1)
        off = 0 if t >= T else 150 * (1 - u) ** 1.6 * np.cos(2 * np.pi * 2.2 * u)
        x = W / 2 + off
        d.line([(x, yl - 26), (x, yl + 6)], fill=mix_rgb(ACCENT if t >= T else INK, mk), width=3)


def frame_close(d, t, M):
    T, bar = M['touch_s'], M['bar_s']; b = bar / 4
    for a_, b_, s in CAPS:      # phụ đề câu kết (theo alignment của take)
        c0, c1 = a_ - V0 + V_AT, b_ - V0 + V_AT
        al = ease(t, c0 - 0.1, c0 + 0.1) * (1 - ease(t, c1 + 0.15, c1 + 0.35))
        if al > 0.01: d.text((W / 2, 430), s, font=F_CAP, fill=mix_rgb(MUTED, al), anchor='mm')
    mk = ease(t, T - 0.15, T + 0.25) * (1 - ease(t, 10.1, 10.45))
    card(d, mk)
    x0, x1, yl = W / 2 - 150, W / 2 + 150, 374
    for k in range(5):          # ô 4: 4 nốt motif giãn (nốt đen) + chạm
        tk = 3 * bar + k * b if k < 4 else T
        u = ease(t, tk, tk + 0.12)
        if u <= 0: continue
        a0 = x0 + (x1 - x0) * k / 5; a1 = a0 + (x1 - x0) / 5 * u
        d.line([(a0, yl), (a1, yl)], fill=mix_rgb(ACCENT if k == 4 else INK, max(mk, 0.6 * (1 - ease(t, 10.1, 10.45)))), width=3)


def video(wav, meta, rep):
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-i', wav, '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-tune', 'animation',
                          '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', DST], stdin=subprocess.PIPE)
    for i in range(int(round(TOTAL * FPS))):
        t = i / FPS
        im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
        for lab, a, b in SEG:
            if lab and a <= t < b:
                lt = t - a
                d.text((24, 22), lab, font=F_LAB, fill=MUTED, anchor='lt')
                {'A': frame_a, 'B': frame_b, 'close': frame_close}[lab](d, lt, meta[{'A': 'ident-A', 'B': 'ident-B', 'close': 'close-A'}[lab]])
        p.stdin.write(im.tobytes())
    p.stdin.close(); assert p.wait() == 0


def main():
    meta = json.load(open(os.path.join(OUT, 'theme.json')))['files']
    wav, rep = audio(meta)
    video(wav, meta, rep)
    rep['clip_mp4'] = os.path.relpath(DST, ROOT)
    rep['timeline_s'] = {'ident-A': [0, 3], 'silence1': [3, 4], 'ident-B': [4, 7], 'silence2': [7, 8], 'close-A': [8, 18.5],
                         'touch_A': meta['ident-A']['touch_s'], 'touch_B': 4 + meta['ident-B']['touch_s'],
                         'close_voice': [8 + V_AT, round(8 + V_AT + CAPS[-1][1] - V0, 2)], 'touch_close': round(8 + meta['close-A']['touch_s'], 3)}
    json.dump(rep, open(os.path.join(OUT, 'clip-report.json'), 'w'), indent=1)
    print(json.dumps(rep, indent=1))


if __name__ == '__main__':
    main()

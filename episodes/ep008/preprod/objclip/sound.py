"""Âm cho clip vật thể thử (mỗi vật đổi trạng thái có tiếng riêng; nhạc không có — chỉ âm vật thể + nền phòng).
    python3 episodes/ep008/preprod/objclip/sound.py <clip> <giây> <ra.wav>"""
import json, os, sys, wave
import numpy as np

SR = 48000
HERE = os.path.dirname(os.path.abspath(__file__))
clip, secs, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
n = int(SR * secs)
y = np.zeros(n)
rng = np.random.default_rng(8)
t = np.arange(n) / SR
y += 0.004 * rng.standard_normal(n)                       # nền phòng rất nhỏ


def tone(t0, dur, f, amp, decay=6.0, harm=(1, 0.3, 0.1)):
    a, b = int(t0 * SR), min(n, int((t0 + dur) * SR))
    if a >= n: return
    tt = np.arange(b - a) / SR
    env = np.exp(-decay * tt) * np.minimum(1, tt / 0.004)
    y[a:b] += amp * env * sum(h * np.sin(2 * np.pi * f * (k + 1) * tt) for k, h in enumerate(harm))


def noise(t0, dur, amp, lp=0.15, decay=30.0):
    a, b = int(t0 * SR), min(n, int((t0 + dur) * SR))
    s = rng.standard_normal(b - a)
    for i in range(1, len(s)): s[i] = lp * s[i] + (1 - lp) * s[i - 1]
    tt = np.arange(b - a) / SR
    y[a:b] += amp * s * np.exp(-decay * tt)


d = json.load(open(os.path.join(HERE, 'data.json')))
if clip == 'street':
    ahead = d['ahead']['5']; N = len(ahead)
    for i in range(0, N, 4):                               # một hạt mỗi 4 nhà: sáng = chuông ấm cao dần, tối = trầm đục
        t0 = 1.0 + 4.0 * i / N
        if ahead[i]: tone(t0, 0.35, 520 + 380 * i / N, 0.05, decay=9)
        else: tone(t0, 0.4, 130, 0.07, decay=7, harm=(1, 0.05, 0.0))
    noise(5.0, 1.2, 0.05, lp=0.05, decay=2.5)              # lùi máy (whoosh mềm)
    for f in (262, 330, 392): tone(6.4, 0.6, f, 0.04, decay=2.0)   # chuyển chế độ đồ thị: hợp âm treo
elif clip == 'tag':
    for t0, up in ((2.0, False), (4.4, True)):
        noise(t0, 0.08, 0.25, lp=0.6, decay=60); tone(t0, 0.12, 900, 0.06, decay=40)   # thẻ lật (clack)
        for k in range(10):                                # cả phố đổi đèn: rơi xuống (4 %) / dâng lên (6 %)
            f = (400 + 60 * k) if up else (900 - 60 * k)
            tone(t0 + 0.3 + 0.08 * k, 0.3, f, 0.035, decay=10)
elif clip == 'box':
    for k in range(13):
        t0 = 0.6 + 0.45 * k + 0.35
        noise(t0, 0.1, 0.10, lp=0.25, decay=40); tone(t0, 0.25, 1800, 0.012, decay=25)   # bó tiền rơi vào hộp kính (bịch giấy + keng kính khẽ)
elif clip == 'fog':
    s = rng.standard_normal(n)
    for i in range(1, n): s[i] = 0.02 * s[i] + 0.98 * s[i - 1]
    y += 0.4 * s * np.clip(t / 6.5, 0, 1)                    # gió sương dâng dần khi tới mép
else:
    a, b = int(0.2 * SR), int(6.0 * SR)                    # đèn của Nina: tiếng ù ấm riêng, vào dần
    env = np.clip((t[a:b] - 0.2) / 0.7, 0, 1)
    y[a:b] += 0.02 * env * (np.sin(2 * np.pi * 110 * t[a:b]) + 0.4 * np.sin(2 * np.pi * 220 * t[a:b])) * (0.85 + 0.15 * np.sin(2 * np.pi * 0.33 * t[a:b]))
    for t0 in (1.6, 3.2, 4.8): tone(t0, 0.5, 330, 0.03, decay=5)   # vòng 2: không bước chân; mỗi lần đổi hướng nhìn một nốt mềm
y = np.clip(y / max(1e-9, np.abs(y).max()) * 0.5, -1, 1)
st = np.stack([y, y], 1)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype('<i2').tobytes())
print(out)

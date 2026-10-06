"""Mốc V · đoạn thử: tiếng ĐỦ LỚP từ trục xương sống (spine.json) — lời, nhạc theo căng–chùng, âm dữ liệu (bảng S2), hiệu ứng, room tone.
  python3 moc-v/proto/audio.py <out_dir> [--music code|<file.wav>] [--no-data] [--no-sfx]
Ra: <out_dir>/mix.wav (−14 LUFS, ≤ −1,5 dBTP) + stems/{voice,music,data,sfx,room}.wav + audio-report.json.

Luật áp (sổ gu):
  G-006 lời ưu tiên: nhạc dưới lời 20 dB (cách đo A07: RMS lúc có lời), mọi lớp phụ né lời (side-chain 8 dB) và mất dải 1–4 kHz khi có lời;
        không giải bằng tăng âm lượng.
  G-001/G-005·chọn: âm dữ liệu bảng S2 "minimal" (tick lọc mềm 4,5–7 kHz + nhịp trầm có cao độ), cao độ theo giá trị, gắn khoá nhạc;
        NGHE THẤY ĐƯỢC: nốt rơi vào khe giữa âm tiết (dời −60/+120 ms), mức đo trong khe lời ≥ −30 dB so với lời (báo cáo).
  G-003 vào khoảng lặng: nhạc nhả như đuôi reverb (τ 90 ms), room tone +6 dB làm sàn, trở lại trong 200 ms.
  G-016 nhạc sáng/năng động (114 BPM, D dorian → F trưởng lúc thả), DX-R1 theo bản đồ căng (tầng nhạc cụ theo mức căng).
"""
import json, os, subprocess, sys
import numpy as np
from scipy import signal
from scipy.io import wavfile
from scipy.ndimage import maximum_filter1d, uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.dont_write_bytecode = True
SR = 48000
rng = np.random.default_rng(20261006)
hz = lambda m: 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)
BPM = 114.0
BEAT = 60 / BPM


def load(p, ch=1):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    x = np.frombuffer(r.stdout, np.float32).astype(np.float64)
    return x if ch == 1 else x.reshape(-1, ch)


def write(p, x):
    y = np.clip(x, -1, 1)
    wavfile.write(p, SR, (y * 8388607).astype(np.int32) if False else y.astype(np.float32))


def add(buf, t, sig, pan=0.0, g=1.0):
    i0 = int(round(t * SR))
    if i0 >= len(buf) or i0 + len(sig) <= 0:
        return
    s0 = max(0, -i0); i0 = max(0, i0); n = min(len(sig) - s0, len(buf) - i0)
    a = (np.clip(pan, -1, 1) + 1) * np.pi / 4
    buf[i0:i0 + n, 0] += sig[s0:s0 + n] * np.cos(a) * g * np.sqrt(2)
    buf[i0:i0 + n, 1] += sig[s0:s0 + n] * np.sin(a) * g * np.sqrt(2)


def mixs(*xs):
    n = max(len(x) for x in xs); return sum(np.pad(x, (0, n - len(x))) for x in xs)


def lp1(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    return signal.lfilter([1 - a], [1, -a], x)


def env_ar(t, att, dec):
    return np.minimum(1, t / max(att, 1e-4)) * np.exp(-t / dec)


# ------------------------------------------------------------------ nhạc cụ (cùng họ âm sắc với nhạc style C Tập 1–4)
def pad(freqs, dur, vel, bright=1100):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for f in freqs:
        for det in (-0.0045, 0.0, 0.0052):
            x += 2 * ((f * (1 + det) * t + rng.uniform()) % 1.0) - 1
    x /= 3 * len(freqs)
    y = lp1(lp1(x, bright), bright)
    return y * np.minimum(1, t / 0.45) * np.minimum(1, np.maximum(0, dur - t) / 0.6) * vel


def pluck(f, vel, lp=1900, dur=0.4):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) + 0.15 * np.sin(6 * np.pi * f * t)
    return lp1(x * env_ar(t, 0.004, 0.13), lp) * vel


def bass(f, vel, dur):
    n = int(max(dur, 0.12) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.18 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.05)
    return x * env_ar(t, 0.006, 0.16) * np.minimum(1, np.maximum(0, n / SR - t) / 0.03) * vel


def thump(vel):
    n = int(0.3 * SR); t = np.arange(n) / SR
    f = 48 + 57 * np.exp(-t / 0.035)
    return lp1(np.sin(2 * np.pi * np.cumsum(f) / SR) * env_ar(t, 0.002, 0.11), 260) * vel


def shaker(vel):
    n = int(0.06 * SR); t = np.arange(n) / SR
    x = signal.sosfilt(signal.butter(2, [6000, 11000], 'band', fs=SR, output='sos'), rng.standard_normal(n))
    return x / (np.abs(x).max() + 1e-9) * env_ar(t, 0.003, 0.018) * vel


def felt(f, vel, dur=1.2):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.08)
    return lp1(x * env_ar(t, 0.003, 0.35), 1500) * vel


def bell(f, vel, dur=2.2):
    n = int(dur * SR); t = np.arange(n) / SR
    mod = 1.8 * np.exp(-t / 0.25) * np.sin(2 * np.pi * f * 3.5 * t)
    x = np.sin(2 * np.pi * f * t + mod) * env_ar(t, 0.002, 0.7) + 0.25 * np.sin(2 * np.pi * 2.01 * f * t) * env_ar(t, 0.002, 0.3)
    return x * vel


def noise_sweep(dur, f0, f1, vel, att=0.3):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n); y = np.zeros(n)
    fc = f0 * (f1 / f0) ** (t / dur)
    for i in range(0, n, 512):
        sos = signal.butter(2, [fc[i] * 0.7, min(fc[i] * 1.4, 20000)], 'band', fs=SR, output='sos')
        y[i:i + 512] = signal.sosfilt(sos, x[i:i + 512])
    e = np.minimum(1, t / att) * np.minimum(1, (dur - t) / 0.12)
    return y / (np.abs(y).max() + 1e-9) * e * vel


def glide(m0, m1, dur, vel):
    n = int(dur * SR); t = np.arange(n) / SR
    m = m0 + (m1 - m0) * (0.5 - 0.5 * np.cos(np.pi * t / dur))
    ph = 2 * np.pi * np.cumsum(hz(m)) / SR
    return (np.sin(ph) + 0.25 * np.sin(2 * ph)) * np.minimum(1, t / 0.08) * np.minimum(1, (dur - t) / 0.25) * vel


def reverb(x, rt60=1.9, wet=0.22):
    n = int(rt60 * SR); t = np.arange(n) / SR; e = np.exp(-6.9 * t / rt60); r = np.random.default_rng(7)
    L = r.standard_normal(n) * e; R = 0.8 * L + 0.6 * r.standard_normal(n) * e
    L[:int(0.012 * SR)] = 0; R[:int(0.017 * SR)] = 0
    lp = signal.butter(2, 5500, 'low', fs=SR, output='sos'); L, R = signal.sosfilt(lp, L), signal.sosfilt(lp, R)
    L /= np.sqrt(np.sum(L ** 2)); R /= np.sqrt(np.sum(R ** 2))
    N = len(x)
    return x + wet * np.stack([signal.oaconvolve(x[:, 0], L)[:N], signal.oaconvolve(x[:, 1], R)[:N]], 1)


# ------------------------------------------------------------------ nhạc theo bản đồ căng (DX-R1)
DOR = {'i7': (50, [0, 3, 7, 10]), 'IV': (55, [0, 4, 7, 10]), 'VII': (60, [0, 4, 7]), 'v7': (57, [0, 3, 7, 10]), 'III': (53, [0, 4, 7, 11])}
FMAJ = {'I': (53, [0, 4, 7, 14]), 'V': (60, [0, 4, 7]), 'vi': (50, [0, 3, 7]), 'IV': (58, [0, 4, 7, 11])}
OST = [[0, 2, 3, 6, 8, 10, 11, 14], [0, 3, 6, 8, 9, 11, 14, 15], [0, 2, 3, 6, 8, 11, 12, 14], [0, 3, 4, 6, 8, 10, 12, 14]]


def tension_at(spine, t):
    kf = spine['tension']
    return float(np.interp(t, [k[0] for k in kf], [k[1] for k in kf]))


def music_code(spine):
    """Tầng theo mức căng: pad luôn có; bass ≥ 0,35; pluck ≥ 0,45 (dày hơn ≥ 0,7); kick ≥ 0,55 (4 phách ≥ 0,75); shaker ≥ 0,6.
    Nhịp 114 BPM; đỉnh căng (b10 'past the cap') → cắt mọi tầng sau 'cap' với đuôi reverb (khoảng lặng ngắn, G-003),
    rồi b11 thả: F trưởng, pad + pluck thưa (sáng, G-016). Điểm nhấn felt rơi đúng sự kiện (vạch trần khoá, cắt vạch, qua trần)."""
    T = spine['total']; N = int(T * SR) + SR; dry = np.zeros((N, 2))
    cue = {b['id']: b['cues'] for b in spine['beats']}
    stop = cue['b10']['cap'] + 0.32
    rel0 = cue['b11']['x'] - 2.2  # thả bắt đầu ngay sau khoảng lặng
    bar = 4 * BEAT
    prog = ['i7', 'IV', 'i7', 'VII', 'i7', 'IV', 'v7', 'III']
    k = 0; t0 = 0.0
    while t0 < stop:
        ten = tension_at(spine, t0 + bar / 2)
        name = prog[k % len(prog)]; root, iv = DOR[name]
        fr = [hz(root + i) for i in iv]
        d = min(bar, stop - t0)
        add(dry, t0, pad(fr, d + 0.6, 0.08 + 0.2 * ten, 700 + 1400 * ten))   # tương phản căng–chùng rõ hơn (lượt đạo diễn)
        for e in range(8):
            t = t0 + e * BEAT / 2
            if t >= stop: break
            if ten >= 0.35:
                add(dry, t, bass(hz(root - 12 + (12 if e % 2 else 0)), (0.2 if e % 2 == 0 else 0.11) * (0.6 + 0.6 * ten), 0.45 * BEAT))
            if ten >= 0.6:
                add(dry, t + BEAT / 4, shaker(0.08 + 0.08 * ten), 0.3 if e % 2 else -0.3)
        for b in range(4):
            t = t0 + b * BEAT
            if t >= stop: break
            if ten >= 0.75 or (ten >= 0.55 and b % 2 == 0):
                add(dry, t, thump((0.5 if b == 0 else 0.36) * (0.6 + 0.5 * ten)))
        if ten >= 0.45:
            tones = [m for m in range(62, 62 + 17) if (m - root) % 12 in [i % 12 for i in iv]]
            hits = OST[k % len(OST)] if ten >= 0.7 else OST[k % len(OST)][::2]
            for j, h in enumerate(hits):
                t = t0 + h * BEAT / 4
                if t >= stop: break
                add(dry, t, pluck(hz(tones[(j * 2 + k) % len(tones)]), (0.15 if h in (0, 6, 8, 14) else 0.09) * (0.7 + 0.5 * ten)),
                    0.25 if j % 2 else -0.25)
        k += 1; t0 += bar
    # thả: F trưởng, thưa
    seq = ['I', 'IV', 'I', 'V']
    t0 = rel0 + 1.0; k = 0
    while t0 < T:
        root, iv = FMAJ[seq[k % 4]]
        add(dry, t0, pad([hz(root + i) for i in iv], bar + 0.6, 0.16, 1500))
        tones = [m for m in range(65, 65 + 15) if (m - root) % 12 in [i % 12 for i in iv]]
        for j, h in enumerate([0, 3, 6, 10, 12]):
            add(dry, t0 + h * BEAT / 4, pluck(hz(tones[(j + k) % len(tones)]), 0.08, 2600), 0.2 if j % 2 else -0.2)
        k += 1; t0 += bar
    # điểm nhấn đúng sự kiện
    for key, m, v in ((cue['b3']['cap'] + 0.35, 38, 0.45), (cue['b6']['cross'], 50, 0.4), (cue['b10']['past'] - 0.05, 38, 0.55)):
        add(dry, key, felt(hz(m), v)); add(dry, key, felt(hz(m + 7), v * 0.5), 0.1)
    wet = reverb(dry)
    # G-003: sau 'stop' chỉ còn đuôi reverb (τ 90 ms cho phần khô) — đã cắt nốt khô ở stop; đuôi reverb tự nhả
    tt = np.arange(N) / SR
    g = np.where(tt < stop, 1.0, np.exp(-(tt - stop) / 0.09) * 0 + 1.0)
    fade = np.clip(tt / 0.8, 0, 1) * np.clip((T - tt) / 1.5, 0, 1)
    return (wet * (g * fade)[:, None])[:int(T * SR)], {'stop': stop, 'release': rel0 + 1.0}


# ------------------------------------------------------------------ âm dữ liệu S2 + hiệu ứng
PENTA = {2, 5, 7, 9, 0}


def qpenta(m):
    m = int(round(m))
    for d in range(7):
        for c in (m - d, m + d):
            if c % 12 in PENTA: return c
    return m


def s2_tick(vel):
    n = int(0.03 * SR); t = np.arange(n) / SR
    x = signal.sosfilt(signal.butter(2, [4500, 7000], 'band', fs=SR, output='sos'), rng.standard_normal(n)) * np.exp(-t / 0.006)
    return x / (np.abs(x).max() + 1e-9) * 0.5 * vel


def s2_pulse(f, vel):
    n = int(0.45 * SR); t = np.arange(n) / SR
    fr = f * (1 + 0.25 * np.exp(-t / 0.02))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.14) * np.minimum(1, t / 0.004) * vel


def gap_shift(t, venv):
    """Dời nốt vào chỗ lời nhỏ nhất trong [−60, +120] ms (khe giữa âm tiết)."""
    i0 = int((t - 0.06) * 200); i1 = int((t + 0.12) * 200)
    i0 = max(0, i0); i1 = min(len(venv) - 1, i1)
    if i1 <= i0: return t
    j = i0 + int(np.argmin(venv[i0:i1 + 1]))
    return j / 200


def data_layer(spine, N, venv):
    out = np.zeros((N, 2)); shifts = []
    for e in spine['events']:
        if e['kind'] != 'data': continue
        t = gap_shift(e['t'], venv); shifts.append(round(t - e['t'], 3))
        m = qpenta(45 + 19 * e['v'])                         # cao độ theo giá trị: thấp → cao, khoá D (ngũ cung)
        v = 0.9 if e.get('over') else 0.65
        add(out, t, s2_pulse(hz(m), v), -0.2 + 0.4 * e['v'])
        add(out, t, s2_tick(0.55 * v), 0.3)
        if e.get('over'):                                   # vượt trần: thêm một bội âm sáng (cùng khoá) — nghe được phần "trên vạch"
            add(out, t, s2_pulse(hz(m + 24), 0.22), 0.2)
    return out, shifts


def sfx_layer(spine, N):
    out = np.zeros((N, 2))
    for e in spine['events']:
        k, t = e['kind'], e['t']
        if k == 'riser':
            d = e['to'] - t; add(out, t, mixs(noise_sweep(d, 400, 3500, 0.10, att=d * 0.8), glide(57, 62, d, 0.05)))
        elif k == 'whoosh_soft':
            add(out, t, noise_sweep(0.9, 2500, 500, 0.10, 0.2))
        elif k == 'tick':
            add(out, t, mixs(s2_tick(e['v']), 0.4 * s2_pulse(hz(qpenta(62 + 8 * e['v'])), e['v'] * 0.6)), rng.uniform(-0.6, 0.6))
        elif k == 'gather':
            add(out, t, pad([hz(62), hz(69), hz(74)], 1.6, 0.25, 1800))
        elif k == 'thud':
            add(out, t, mixs(felt(hz(31), 0.45), thump(0.4)))   # lượt đạo diễn: thud ngang lời → −6 dB
        elif k == 'drone_on':
            d = e['until'] - t; n = int(d * SR); tt = np.arange(n) / SR
            x = (np.sin(2 * np.pi * 73.4 * tt) + 0.3 * np.sin(2 * np.pi * 146.8 * tt)) * (1 + 0.15 * np.sin(2 * np.pi * 0.3 * tt))
            add(out, t, x * np.minimum(1, tt / 0.8) * np.minimum(1, (d - tt) / 0.8) * 0.024)
        elif k == 'slide_down':
            add(out, t, mixs(glide(74, 62, e['dur'], 0.12), noise_sweep(e['dur'], 3000, 700, 0.05, 0.4)))
        elif k == 'chime':
            add(out, t, bell(hz(81), 0.32), 0.15); add(out, t + 0.09, bell(hz(88), 0.18), -0.15)
        elif k == 'swish':
            d = e['to'] - t; add(out, t, mixs(noise_sweep(d, 900, 5000, 0.12, att=d * 0.7), glide(62, 74, d, 0.06)))
        elif k == 'impact':
            add(out, t, mixs(felt(hz(26), 0.32, 1.6), thump(0.32))); add(out, t, bell(hz(74), 0.06), 0.0)   # −10 dB, sau chữ 'cap'
        elif k == 'rise':
            add(out, t, glide(57, 69, e['dur'], 0.10))
    return out


def room_tone(N, venv, mus_env):
    """Sàn room tone (≈ −62 dBFS); +6 dB trong khoảng lặng (không lời, nhạc nhỏ) — G-003."""
    x = rng.standard_normal(N)
    b, a = signal.butter(1, 900, 'low', fs=SR)
    x = signal.lfilter(b, a, x); x = x / np.sqrt(np.mean(x ** 2)) * 10 ** (-62 / 20)
    quiet = ((venv < 1e-3) & (mus_env < 10 ** (-40 / 20))).astype(float)
    q = np.repeat(quiet, SR // 200)[:N]; q = np.pad(q, (0, N - len(q)))
    g = 10 ** (6 * uniform_filter1d(q, int(0.2 * SR)) / 20)
    return np.stack([x * g, np.roll(x, 2400) * g], 1)


def env200(x):
    m = np.abs(x if x.ndim == 1 else x.mean(1))
    k = SR // 200
    return maximum_filter1d(m[:len(m) // k * k].reshape(-1, k).max(1), 3)


def duck(layer, venv, depth_db=8.0, carve=True):
    """Side-chain theo lời + mất dải 1–4 kHz khi có lời (G-006)."""
    act = (venv > 10 ** (-38 / 20)).astype(float)
    a = np.repeat(uniform_filter1d(act, 10), SR // 200)[:len(layer)]
    a = np.pad(a, (0, len(layer) - len(a)))
    g = 10 ** (-depth_db * a / 20)
    y = layer * g[:, None]
    if carve:
        band = signal.sosfiltfilt(signal.butter(2, [1000, 4000], 'band', fs=SR, output='sos'), y, axis=0)
        y = y - band * a[:, None] * 0.9
    return y


def rms_active(x, venv):
    act = np.repeat((venv > 10 ** (-38 / 20)), SR // 200)[:len(x)]
    act = np.pad(act, (0, len(x) - len(act)))
    m = x if x.ndim == 1 else x.mean(1)
    return np.sqrt(np.mean(m[act.astype(bool)] ** 2) + 1e-12)


def lufs(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
    tail = r.stderr[r.stderr.rfind('Summary'):]
    I = float(tail.split('I:')[1].split('LUFS')[0]); P = float(tail.split('Peak:')[1].split('dBFS')[0])
    return I, P


def main():
    out = sys.argv[1]; os.makedirs(os.path.join(out, 'stems'), exist_ok=True)
    music_src = sys.argv[sys.argv.index('--music') + 1] if '--music' in sys.argv else 'code'
    spine = json.load(open(sys.argv[sys.argv.index('--spine') + 1] if '--spine' in sys.argv else os.path.join(HERE, 'spine.json')))
    T = spine['total']; N = int(T * SR)
    voice = np.zeros(N)
    for tk in spine['takes']:
        w = load(tk['wav']); i0 = int(tk['t'] * SR); n = min(len(w), N - i0); voice[i0:i0 + n] += w[:n]
    venv = env200(voice)
    rep = {'music': music_src}
    if music_src == 'code':
        mus, info = music_code(spine); rep.update(info)
    else:
        mus = load(music_src, 2)[:N]; mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
        # nhạc từ file (thư viện/AI): cũng khoảng lặng ngắn sau 'cap' (G-003): nhả τ 90 ms, lặng ~1,1 s, trở lại trong 200 ms
        cue = {bb['id']: bb['cues'] for bb in spine['beats']}; t_ = np.arange(N) / SR; c0 = cue['b10']['cap'] + 0.32
        g_ = np.where(t_ < c0, 1.0, np.where(t_ < c0 + 1.1, np.exp(-(t_ - c0) / 0.09), np.clip((t_ - c0 - 1.1) / 0.2, 0, 1)))
        mus = mus * g_[:, None]
    mus = mus[:N]
    data, shifts = data_layer(spine, N, venv) if '--no-data' not in sys.argv else (np.zeros((N, 2)), [])
    sfx = sfx_layer(spine, N) if '--no-sfx' not in sys.argv else np.zeros((N, 2))
    # mức: nhạc 20 dB dưới lời (RMS lúc có lời, A07); âm dữ liệu −16 dB, sfx −14 dB dưới lời TRƯỚC side-chain (mọi lớp cùng cách đo)
    vr = rms_active(voice, venv)
    def level(x, db):
        r = rms_active(x, venv) if np.any(x) else 1
        if r < 1e-9:
            r = np.sqrt(np.mean(x ** 2) + 1e-12)
        return x * (vr * 10 ** (-db / 20) / r)
    mus_d = duck(level(mus, 20.0), venv, 4.0, carve=True)
    data_d = duck(level(data, 18.0), venv, 8.0) if np.any(data) else data
    # sfx: chuẩn theo ĐỈNH (đỉnh sfx = đỉnh lời − 12 dB), không theo RMS cả lớp — để hạ một tiếng không kéo tiếng khác lên (lượt đạo diễn v2)
    sfx_d = duck(sfx * (np.abs(voice).max() * 10 ** (-12 / 20) / (np.abs(sfx).max() + 1e-12)), venv, 6.0) if np.any(sfx) else sfx
    room = room_tone(N, venv, env200(mus_d))
    v2 = np.stack([voice, voice], 1)
    mix = v2 + mus_d + data_d + sfx_d + room
    # đo nghe thấy được (G-001): mức đỉnh âm dữ liệu trong khe lời so với RMS lời
    rep['voice_over_music_db'] = round(20 * np.log10(vr / (rms_active(mus_d, venv) + 1e-12)), 2)
    gaps = np.repeat(venv < 10 ** (-38 / 20), SR // 200)[:N]; gaps = np.pad(gaps, (0, N - len(gaps))).astype(bool)
    if np.any(data_d):
        pk = env200(data_d)[:len(venv)]
        rep['data_in_gaps_db_vs_voice'] = round(20 * np.log10(np.percentile(pk[venv < 10 ** (-38 / 20)], 99) / vr + 1e-12), 1)
        rep['data_shift_ms'] = {'max': int(1000 * max(map(abs, shifts))), 'mean': int(1000 * np.mean(np.abs(shifts)))}
    # lớp phụ không được vọt đỉnh hơn lời: giới hạn mềm tổng lớp phụ ở 0,8 × đỉnh lời (lời không bị nén)
    side = mus_d + data_d + sfx_d
    lim = 0.8 * np.abs(voice).max()
    side = lim * np.tanh(side / lim)
    mix = v2 + side + room
    tmp = os.path.join(out, 'pre.wav'); write(tmp, mix * 0.5)
    # loudnorm 2 lượt như nhà máy (−14 LUFS, −1,5 dBTP)
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', tmp, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rfind('{'):])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
          f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', af, '-ar', str(SR), '-c:a', 'pcm_f32le', os.path.join(out, 'mix.wav')], check=True)
    os.remove(tmp)
    g = 10 ** ((-14.0 - float(m['input_i'])) / 20)
    I, P = lufs(os.path.join(out, 'mix.wav'))
    rep.update({'lufs': I, 'peak_dbfs': P})
    for name, x in (('voice', v2), ('music', mus_d), ('data', data_d), ('sfx', sfx_d), ('room', room)):
        write(os.path.join(out, 'stems', name + '.wav'), x * 0.5 * g)
    json.dump(rep, open(os.path.join(out, 'audio-report.json'), 'w'), indent=1)
    print(json.dumps(rep))


if __name__ == '__main__':
    main()

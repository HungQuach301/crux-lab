"""Episode 3 temporary full-episode music mix for the animatic (gate C4): voice.wav + music bed over the whole 570.000 s picture.

Copied from episodes/ep003/audio_src/mix_c3clip.py (the C3-approved clip: style C, 114 BPM, D dorian, same instruments / reverb / ducking /
levels / master chain), changed:
  TIMELINE: voice = animatic/work/voice.wav (48 kHz mono, whole narration; gain only, never stretched/shifted/edited), padded with silence to
            570.000 s = ceil(timing.total + 15); no voice fade-out. Music runs continuously to the end with a 3 s fade-out.
  KEY:      D dorian S01-S07; F major from the first bar at/after S08 start (timing.json scene S08); Markov chords, no repeated 4-bar window
            within 24 bars (engine rules kept; the engine switches key on the bar grid).
  SWELL:    +3 dB at every scene start in timing.json (same ramp shape as the clip's story-turn swell; t=0 scene skipped).
  OUTPUT:   animatic/work/mix.wav (PCM 24, 48k stereo), stems/{voice,music,sonify,sfx,whoosh,room}.wav (sonify/sfx/whoosh silent: unused),
            tempo-map.json, animatic/mix-report.json (incl. T2 self-similarity of the music stem).
  KEPT:     music 20 dB under voice (A07 method), 1-4 kHz ducked 13 dB, master -14 LUFS, TP <= -1.5 dBTP on every stem, seeds as the clip.
    python3 episodes/ep003/audio_src/mix_full.py
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
from scipy import signal
from scipy.ndimage import maximum_filter1d, minimum_filter1d, uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..'))
SCR = '/tmp/claude-0/-home-user-crux-lab/7feba40e-1932-5b7d-90df-5c7e79c0113c/scratchpad'
ANI = os.path.join(EP, 'animatic')
WORK = os.path.join(ANI, 'work')
SRC = os.path.join(WORK, 'voice.wav')
TIMING = json.load(open(os.path.join(ANI, 'timing.json')))
CLIP_S = float(np.ceil(TIMING['total'] + 15))
END_FADE_S = 3.0
SCENE_STARTS = [sc['start'] for sc in TIMING['scenes'] if sc['start'] > 0]
F_START = next(sc['start'] for sc in TIMING['scenes'] if sc['id'] == 'S08')
BPM_CLIP = 114.0
SWELL_DB = 3.0

SR = 48000


def _ffmpeg():
    if os.environ.get('FFMPEG'):
        return os.environ['FFMPEG']
    if shutil.which('ffmpeg'):
        return 'ffmpeg'
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FFMPEG = _ffmpeg()

RNG = np.random.default_rng(20261001)
NOTE = {'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
hz = lambda m: 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)
MASTER_LUFS = -14.0
TP_CEIL_DB = -1.5
VOICE_OVER_MUSIC_DB = 20.0      # A07 window 18-22 dB; Tập 1 level kept (G-016: "mức dưới lời giữ nguyên")
ROOM_DBFS = -66.0

def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def decode(path, ch=1):
    raw = subprocess.run([FFMPEG, '-v', 'error', '-i', path, '-map', '0:a:0', '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-'],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).astype(np.float64)


def write_wav(path, x, bits=24):
    import soundfile as sf
    sf.write(path, np.clip(x, -1, 1), SR, subtype='PCM_24' if bits == 24 else 'FLOAT')


def ebur128(x):
    with tempfile.TemporaryDirectory() as d:
        w = os.path.join(d, 'm.wav')
        write_wav(w, x, bits=32)
        o = subprocess.run([FFMPEG, '-nostats', '-v', 'info', '-i', w, '-af', 'ebur128=peak=true:framelog=quiet', '-f', 'null', '-'],
                           capture_output=True, text=True).stderr
    txt = o[o.rfind('Summary:'):]
    g = lambda k: float(re.search(k + r':\s+(-?[\d.inf]+)', txt).group(1))
    return {'I': g('I'), 'LRA': g('LRA'), 'TP': g('Peak')}


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def smooth_gate(target, att, rel, hop=48):
    n = len(target)
    blocks = target[: (n // hop) * hop].reshape(-1, hop).max(1)
    out = np.zeros(len(blocks))
    aa, ar = np.exp(-hop / (att * SR)), np.exp(-hop / (rel * SR))
    cur = 0.0
    for i, t in enumerate(blocks):
        c = aa if t > cur else ar
        cur = t + (cur - t) * c
        out[i] = cur
    g = np.repeat(out, hop)
    return np.concatenate([g, np.full(n - len(g), g[-1] if len(g) else 0.0)])


def bandpass(x, lo, hi, order=4):
    sos = signal.butter(order, [lo, hi], 'band', fs=SR, output='sos')
    return signal.sosfiltfilt(sos, x, axis=0)


SECTION = 'curious'
GAIN_DB = 0.0
BRIGHT = 900 * 1.25
KEY = 'D dorian'
VARIANT = 'default'


def tempo_grid(total):
    """Constant tempo, 4-beat bars from 0 until the clip is covered (the last bar may run past the end; the render is cut at the clip)."""
    beat = 60.0 / BPM_CLIP
    n = int(np.ceil(total / (4 * beat)))
    bars = [{'t0': k * 4 * beat, 't1': (k + 1) * 4 * beat, 'scene': 'S01', 'i': k, 'beats': 4, 'bpm': BPM_CLIP} for k in range(n)]
    beats = [k * beat for k in range(4 * n)]
    return beats, bars


CHORDS = {
    'F major': {'I': ('F', ''), 'V': ('C', ''), 'vi': ('D', 'm'), 'IV': ('Bb', ''), 'ii': ('G', 'm'), 'iii': ('A', 'm'), 'Iadd9': ('F', 'add9'), 'IVmaj7': ('Bb', 'maj7')},
    'D dorian': {'i': ('D', 'm'), 'i7': ('D', 'm7'), 'IV': ('G', ''), 'IVadd9': ('G', 'add9'), 'VII': ('C', ''), 'III': ('F', ''), 'v': ('A', 'm'), 'ii': ('E', 'm')},
}
MARKOV = {
    'F major': {'I': ['IV', 'vi', 'V', 'ii', 'iii', 'IVmaj7'], 'Iadd9': ['vi', 'IV', 'ii'], 'IV': ['I', 'V', 'ii', 'Iadd9', 'vi'], 'IVmaj7': ['V', 'I', 'iii'],
                'V': ['I', 'vi', 'IV', 'Iadd9'], 'vi': ['IV', 'ii', 'V', 'IVmaj7'], 'ii': ['V', 'I', 'IV'], 'iii': ['vi', 'IV', 'ii']},
    'D dorian': {'i': ['IV', 'VII', 'III', 'IVadd9', 'v'], 'i7': ['IV', 'VII', 'ii'], 'IV': ['i', 'VII', 'i7', 'III', 'v'], 'IVadd9': ['i', 'VII', 'III'],
                 'VII': ['IV', 'i', 'III', 'i7'], 'III': ['IV', 'VII', 'i', 'ii'], 'v': ['IV', 'VII', 'i'], 'ii': ['IV', 'i7', 'v']},
}
TONIC = {'F major': ['I', 'Iadd9', 'IV'], 'D dorian': ['i', 'i7', 'IV']}


def chord_pcs(root, q):
    r = NOTE[root]
    iv = {'m': [0, 3, 7], '': [0, 4, 7], 'm7': [0, 3, 7, 10], 'add9': [0, 4, 7, 14], 'maj7': [0, 4, 7, 11]}[q]
    return r, [(r + i) for i in iv]


def harmony(bars):
    rng = np.random.default_rng(7)
    seq = []
    for b in bars:
        key = 'F major' if b['t0'] >= F_START - 1e-6 else 'D dorian'
        for attempt in range(200):
            if b['i'] == 0:
                c = TONIC[key][rng.integers(0, len(TONIC[key]))] if seq else TONIC[key][0]
            else:
                prev = seq[-1][1] if seq and seq[-1][0] == key else TONIC[key][0]
                opts = MARKOV[key][prev]
                c = opts[rng.integers(0, len(opts))]
                if False:
                    # alt: among the Markov options, prefer the chord sharing the fewest tones with the last two (more harmonic contrast per bar)
                    pcs_ = lambda n: {p % 12 for p in chord_pcs(*CHORDS[key][n])[1]}
                    recent = set().union(*[pcs_(x[1]) for x in seq[-2:] if x[0] == key]) if seq else set()
                    sc_ = {o: len(pcs_(o) & recent) + rng.random() * 1.2 for o in opts}
                    c = min(opts, key=lambda o: sc_[o])
            cand = [s[1] for s in seq] + [c]
            if len(cand) >= 4:
                w = cand[-4:]
                hist = [s[1] for s in seq[-24:]]
                if any(hist[j:j + 4] == w for j in range(0, max(0, len(hist) - 3))):
                    continue
            if seq and seq[-1][1] == c and attempt < 150:
                continue
            break
        seq.append((key, c))
    return seq
# ================================================================== instruments (numpy synthesis, Tập 1)
def onepole_lp(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    return signal.lfilter([1 - a], [1, -a], x)


def pad(freqs, dur, vel, bright):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        for det in (-0.0045, 0.0, 0.0052):
            x += 2 * ((f * (1 + det) * t + RNG.uniform(0, 1)) % 1.0) - 1
    x /= 3 * len(freqs)
    cut = bright * (0.65 + 0.35 * np.minimum(1, t / max(0.5 * dur, 1e-3)))
    y = np.zeros(n)
    z1 = z2 = 0.0
    for i in range(0, n, 1024):
        a = np.exp(-2 * np.pi * cut[i] / SR)
        seg, zf = signal.lfilter([1 - a], [1, -a], x[i:i + 1024], zi=[z1])
        z1 = zf[0]
        seg2, zf2 = signal.lfilter([1 - a], [1, -a], seg, zi=[z2])
        z2 = zf2[0]
        y[i:i + 1024] = seg2
    env = np.minimum(1, t / 0.45) * np.minimum(1, np.maximum(0, dur - t) / 0.5)
    return y * env * vel


def pluck(f, dur=0.45, vel=1.0, lp=2200):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) + 0.15 * np.sin(6 * np.pi * f * t)
    env = np.minimum(1, t / 0.004) * np.exp(-t / 0.13)
    return onepole_lp(x * env, lp) * vel


def soft_bass(f, dur, vel):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.12 * np.sin(4 * np.pi * f * t)
    env = np.minimum(1, t / 0.06) * np.exp(-t / max(0.6, 0.5 * dur)) * np.minimum(1, np.maximum(0, dur - t) / 0.2)
    return x * env * vel


def felt(f, vel):
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.08)
    return onepole_lp(x * np.minimum(1, t / 0.003) * np.exp(-t / 0.28), 1500) * vel


def bass_pluck(f, dur, vel):
    n = int(max(dur, 0.12) * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.18 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.05)
    env = np.minimum(1, t / 0.006) * np.exp(-t / 0.16) * np.minimum(1, np.maximum(0, n / SR - t) / 0.03)
    return x * env * vel


def thump(vel):
    n = int(0.3 * SR)
    t = np.arange(n) / SR
    f = 48 + 57 * np.exp(-t / 0.035)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    return onepole_lp(x * np.minimum(1, t / 0.002) * np.exp(-t / 0.11), 260) * vel


def add(buf, t, sig, pan=0.0, g=1.0):
    i0 = int(round(t * SR))
    if i0 >= len(buf) or i0 + len(sig) <= 0:
        return
    s0 = max(0, -i0)
    i0 = max(0, i0)
    n = min(len(sig) - s0, len(buf) - i0)
    a = (np.clip(pan, -1, 1) + 1) * np.pi / 4
    buf[i0:i0 + n, 0] += sig[s0:s0 + n] * np.cos(a) * g * np.sqrt(2)
    buf[i0:i0 + n, 1] += sig[s0:s0 + n] * np.sin(a) * g * np.sqrt(2)


def reverb_ir(rt60=1.9, seed=7):
    n = int(rt60 * SR)
    t = np.arange(n) / SR
    env = np.exp(-6.9 * t / rt60)
    r = np.random.default_rng(seed)
    L = r.standard_normal(n) * env
    R = 0.8 * L + 0.6 * r.standard_normal(n) * env
    L[: int(0.012 * SR)] = 0
    R[: int(0.017 * SR)] = 0
    lp = signal.butter(2, 5500, 'low', fs=SR, output='sos')
    L, R = signal.sosfilt(lp, L), signal.sosfilt(lp, R)
    return L / np.sqrt(np.sum(L ** 2)), R / np.sqrt(np.sum(R ** 2))


# ================================================================== music: style C (Tap 1 render_music_styled, drive=True), D dorian
OST16 = [[0, 2, 3, 6, 8, 10, 11, 14], [0, 3, 6, 8, 9, 11, 14, 15], [0, 2, 3, 6, 8, 11, 12, 14], [0, 3, 4, 6, 8, 10, 12, 14],
         [0, 2, 3, 5, 6, 8, 11, 14]]
ACC16 = {0, 3, 6, 8, 11, 14}
SHAPES = ['up', 'down', 'updown', 'broken', 'pedal']


def _contour(shape, tones, k):
    m = len(tones)
    if shape == 'up':
        return tones[k % m]
    if shape == 'down':
        return tones[-1 - k % m]
    if shape == 'updown':
        c = k % (2 * m - 2)
        return tones[c if c < m else 2 * m - 2 - c]
    if shape == 'broken':
        return tones[[0, 2, 1, 3, 2, 4, 3, 1][k % 8] % m]
    return tones[0] if k % 2 == 0 else tones[1 + (k // 2) % (m - 1)]



def render_music(N, bars, seq):
    dry = np.zeros((N, 2), np.float32)
    rng = np.random.default_rng(11)
    prev_voicing = None
    prev_fig = None
    v_lo, v_hi, v_top = 50, 61, 72
    for bi, (b, (key, cname)) in enumerate(zip(bars, seq)):
        if b['t0'] >= N / SR:
            break
        sec = SECTION
        root, q = CHORDS[key][cname]
        r, pcs = chord_pcs(root, q)
        pcl = [p % 12 for p in pcs]
        cands = []
        for inv in range(len(pcl)):
            order = pcl[inv:] + pcl[:inv]
            for low in range(v_lo, v_hi):
                if low % 12 != order[0]:
                    continue
                v = [low]
                for pc in order[1:]:
                    n_ = v[-1] + 1
                    while n_ % 12 != pc:
                        n_ += 1
                    v.append(n_)
                if v[-1] <= v_top:
                    cands.append(v)
        vo = min(cands, key=lambda v: sum(min(abs(a - c) for c in prev_voicing) for a in v) + 0.3 * rng.random()) if prev_voicing else cands[0]
        dur = b['t1'] - b['t0']
        beat = 60.0 / b['bpm']
        pv = 0.2 * 0.8 * rng.uniform(0.92, 1.06)
        add(dry, b['t0'], pad(hz(vo), dur + 0.7, pv, BRIGHT), 0.0)
        lift = 1.0
        broot = 36 + (r % 12) + (12 if (r % 12) < 2 else 0)
        for e in range(2 * b['beats']):
            t = b['t0'] + e * beat / 2
            add(dry, t, bass_pluck(hz(broot + (12 if e % 2 else 0)), 0.45 * beat, (0.2 if e % 2 == 0 else 0.12) * lift * rng.uniform(0.9, 1.05)), 0.0)
        if b['i'] == 0:
            add(dry, b['t0'], felt(hz(48 + r % 12), 0.35), 0.0)
            add(dry, b['t0'], felt(hz(55 + r % 12), 0.18), 0.1)
        for k in range(b['beats']):
            t = b['t0'] + k * beat
            add(dry, t, thump((0.5 if k == 0 else 0.38) * lift * rng.uniform(0.9, 1.05)), 0.0)
        tones = [n_ for n_ in range(57, 57 + 17) if n_ % 12 in pcl]
        for _ in range(20):
            shp = SHAPES[rng.integers(0, len(SHAPES))]
            msk_i = int(rng.integers(0, len(OST16)))
            if (shp, msk_i) != prev_fig:
                break
        prev_fig = (shp, msk_i)
        for j, h in enumerate(OST16[msk_i]):
            t = b['t0'] + h * beat / 4
            f = hz(_contour(shp, tones, j))
            v = (0.17 if h in ACC16 else 0.1) * lift * rng.uniform(0.88, 1.08)
            add(dry, t, pluck(f, 0.2, v, lp=1700), 0.22 if j % 2 else -0.22)
    return dry


def music_dynamics(N):
    t = np.arange(0, N, 480) / SR
    g = np.full(len(t), GAIN_DB)
    # story-turn swell: +3 dB from 41.9 s (0.3 s ramp) to 42.2 s + 2.0 s, 0.3 s ramp down (Episode 2 gap-swell shape)
    for st in SCENE_STARTS:
        a, z = st - 0.3, st + 2.0
        g += SWELL_DB * np.clip(np.minimum((t - a) / 0.3, (z - t) / 0.3), 0, 1)
    g = uniform_filter1d(g, 30)
    g += 20 * np.log10(np.clip(t / 0.6, 1e-4, 1))
    g += 20 * np.log10(np.clip((N / SR - t) / END_FADE_S, 1e-4, 1))
    return np.interp(np.arange(N) / SR, t, 10 ** (g / 20))


# ================================================================== master (Tập 1)
def true_peak_gain(mix, ceil_db):
    N = len(mix)
    ceil = 10 ** (ceil_db / 20)
    pk = np.zeros(N, np.float32)
    CH, OV = SR * 20, 512
    for i0 in range(0, N, CH):
        a0, a1 = max(0, i0 - OV), min(N, i0 + CH + OV)
        up = signal.resample_poly(mix[a0:a1], 4, 1, axis=0)
        p_ = np.abs(up).max(1)
        p_ = p_[: (len(p_) // 4) * 4].reshape(-1, 4).max(1)
        n = min(CH, N - i0)
        pk[i0:i0 + n] = p_[i0 - a0:i0 - a0 + n]
    need = np.minimum(1, ceil / np.maximum(pk, 1e-9))
    la = int(0.005 * SR)
    gmin = minimum_filter1d(need, 2 * la + 1)
    hop = 48
    nb = N // hop
    blk = gmin[: nb * hop].reshape(nb, hop).min(1)
    out = np.empty(nb)
    a = np.exp(-hop / (0.08 * SR))
    cur = 1.0
    for i in range(nb):
        cur = min(blk[i], 1 - (1 - cur) * a)
        out[i] = cur
    g = np.interp(np.arange(N), np.arange(nb) * hop + hop / 2, out)
    g = np.minimum(uniform_filter1d(g, int(0.002 * SR)), gmin)
    return g


def a07_gap(v, m):
    w = int(0.1 * SR)
    k = min(len(v), len(m)) // w
    pv = (v[: k * w].mean(1) ** 2).reshape(k, w).mean(1)
    pm = (m[: k * w].mean(1) ** 2).reshape(k, w).mean(1)
    a = 10 * np.log10(pv + 1e-20) > -45
    return float(10 * np.log10(pv[a].mean()) - 10 * np.log10(pm[a].mean() + 1e-20))


def main():
    N = int(round(CLIP_S * SR))
    log('clip', CLIP_S, 's samples', N)
    beats, bars = tempo_grid(CLIP_S)
    seq = harmony(bars)
    v0 = decode(SRC)[:, 0]
    assert len(v0) <= N
    voice = np.zeros(N)
    voice[:len(v0)] = v0                                                       # gain only, padded with silence
    vr = np.sqrt(np.maximum(uniform_filter1d(voice ** 2, int(0.1 * SR)), 0))
    act = (20 * np.log10(vr + 1e-12) > -45).astype(float)
    la = int(0.08 * SR)
    gate_v_duck = smooth_gate(np.concatenate([act[la:], np.zeros(la)]), 0.04, 0.35)
    log('music: arrangement', len(bars), 'bars')
    dry = render_music(N, bars, seq)
    irL, irR = reverb_ir()
    wetL = signal.oaconvolve(dry[:, 0], irL)[:N]
    wetR = signal.oaconvolve(dry[:, 1], irR)[:N]
    music = (dry + 0.24 * np.stack([wetL, wetR], 1)).astype(np.float64)
    music *= music_dynamics(N)[:, None]
    duck_mid = 10 ** (-13 * gate_v_duck / 20)
    for ch in range(2):
        mid = bandpass(music[:, ch], 1000, 4000)
        music[:, ch] = music[:, ch] - mid + mid * duck_mid
    vt = act > 0
    pv = np.mean(voice[vt] ** 2)
    pm = np.mean(music[vt].mean(1) ** 2)
    music *= np.sqrt(pv / pm) * 10 ** (-VOICE_OVER_MUSIC_DB / 20)
    wn = RNG.standard_normal(N)
    pink = signal.lfilter([0.049922035, -0.095993537, 0.050612699, -0.004408786], [1, -2.494956002, 2.017265875, -0.522189400], wn)
    pink = onepole_lp(pink, 3500)
    pink = pink / np.sqrt(np.mean(pink ** 2))
    room = np.stack([pink, 0.85 * np.roll(pink, 480) + 0.15 * pink], 1)
    voice2 = np.stack([voice, voice], 1)
    stems = {'voice': voice2, 'music': music}
    I0 = ebur128(voice2 + music)['I']
    gain = 10 ** ((MASTER_LUFS - I0) / 20)
    for k in ('voice', 'music'):
        stems[k] *= gain
    stems['room'] = room * 10 ** (ROOM_DBFS / 20)
    mix = sum(stems.values())
    I1 = ebur128(mix)['I']
    g2 = 10 ** ((MASTER_LUFS - I1) / 20)
    mix *= g2
    gl = true_peak_gain(mix, TP_CEIL_DB) * g2
    for k in stems:
        stems[k] *= gl[:, None]
    master = sum(stems.values())
    m = ebur128(master)
    log('master', m)
    sd = os.path.join(WORK, 'stems')
    os.makedirs(sd, exist_ok=True)
    zero = np.zeros((N, 2))
    stems['sonify'] = zero; stems['sfx'] = zero; stems['whoosh'] = zero
    for k in ('voice', 'music', 'sonify', 'sfx', 'whoosh', 'room'):
        write_wav(os.path.join(sd, k + '.wav'), stems[k])
    write_wav(os.path.join(WORK, 'mix.wav'), master)
    bt = [round(b_, 4) for b_ in beats if b_ < CLIP_S]
    tm = {'bpm': BPM_CLIP, 'beats': bt, 'accents': [round(b_['t0'], 4) for b_ in bars if b_['t0'] < CLIP_S]}
    json.dump(tm, open(os.path.join(WORK, 'tempo-map.json'), 'w'))
    mx = ebur128(sf_roundtrip(os.path.join(WORK, 'mix.wav')))
    ss = subprocess.run([sys.executable, os.path.join(EP, '..', '..', 'toolkit', 'audio', 'd_music_selfsim.py'), os.path.join(sd, 'music.wav'),
                         os.path.join(WORK, 'tempo-map.json'), 'ep003-full-music'], capture_output=True, text=True)
    rep = {'engine': {'path': 'episodes/ep003/audio_src/mix_full.py', 'sha256': sha256(os.path.abspath(__file__))},
           'durationS': round(len(master) / SR, 3), 'sections': ['D dorian 0-%.3f s (S01-S07)' % F_START, 'F major %.3f-%.1f s (S08-end)' % (F_START, CLIP_S)],
           'swellsAt_s': SCENE_STARTS, 'seeds': {'RNG(pad,noise)': 20261001, 'harmony': 7, 'arrangement': 11, 'reverb_ir': 7},
           'bpm': BPM_CLIP, 'bars': len(bars), 'master_py': m, 'master_wav_roundtrip': mx, 'preGainLUFS': I0,
           'voiceOverMusicDb_A07': round(a07_gap(stems['voice'], stems['music']), 2),
           'limiterMinGainDb': round(float(20 * np.log10(gl.min() / g2)), 2),
           'T2_selfsim_exit': ss.returncode, 'T2_selfsim_stdout': ss.stdout, 'T2_selfsim_stderr': ss.stderr[-500:],
           'files': {n: {'sha256': sha256(p)} for n, p in [('mix.wav', os.path.join(WORK, 'mix.wav'))] + [(k + '.wav', os.path.join(sd, k + '.wav')) for k in ('voice', 'music', 'sonify', 'sfx', 'whoosh', 'room')] + [('tempo-map.json', os.path.join(WORK, 'tempo-map.json'))]},
           'stubbed': 'sonify/sfx/whoosh stems silent (unused)', 'chords': [c[1] for c in seq]}
    json.dump(rep, open(os.path.join(ANI, 'mix-report.json'), 'w'), indent=1)
    log('done', json.dumps({k: rep[k] for k in ('master_wav_roundtrip', 'voiceOverMusicDb_A07', 'limiterMinGainDb')}))
    print(ss.stdout)


def sf_roundtrip(p):
    import soundfile as sf
    x, sr = sf.read(p, dtype='float64')
    assert sr == SR
    return x


if __name__ == '__main__':
    main()

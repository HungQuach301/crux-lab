"""Data-sound palettes (sổ gu G-001, G-005, G-006): three candidate timbres for the sonification, one shared set of rules.

    python3 toolkit/audio/sonify_palettes.py <root> <palette> <out.wav> [--report r.json]
    palette: mallet | breath | minimal

Shared rules (the owner's G-006: the voice comes first, never solved by level):
  - pitch mapping unchanged: line -> pitch follows the slope at the drawing tip (rising = higher), dot -> pitch from its
    height on screen, bar -> pitch from its value on one fixed scale; every pitch snapped to the music's key
    (D minor pentatonic, the key of the m0 cue sheet / --key);
  - timing: a discrete note that would start while the voice is sounding moves to the quietest instant of the voice
    envelope within [-60 ms, +120 ms] (a gap between syllables); shifts are reported;
  - side-chain: the whole data-sound layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release);
  - band: while the voice is active the data sounds lose 1-4 kHz (the speech-intelligibility band) almost entirely;
  - level: every palette is matched to the same loudness (-16 dB under the voice's active RMS, before the side-chain):
    no palette wins by being louder.
Reads <root>/out/sonify-events.json and <root>/out/audio/stems/voice.flac.
"""
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from scipy import signal
from scipy.io import wavfile
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 48000
PENTA = {2, 5, 7, 9, 0}
hz = lambda m: 440.0 * 2 ** ((m - 69) / 12)
rng = np.random.default_rng(20260928)


def qpenta(m):
    m = int(round(m))
    for d in range(7):
        for c in (m - d, m + d):
            if c % 12 in PENTA:
                return c
    return m


def load_mono(p):
    with tempfile.TemporaryDirectory() as t:
        w = os.path.join(t, 'a.wav')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-c:a', 'pcm_f32le', w], check=True)
        return wavfile.read(w)[1].astype(np.float64)


def pan(x, p):
    a = (np.clip(p, -1, 1) + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], 1)


def add(buf, t, stereo):
    i0 = int(t * SR)
    if i0 < 0 or i0 >= len(buf):
        return
    n = min(len(stereo), len(buf) - i0)
    buf[i0:i0 + n] += stereo[:n]


# ------------------------------------------------------------------ instruments
def mallet(f, vel=1.0, dur=1.2):
    """Marimba-like bar: partials 1 : 3.93 : 9.2 with fast-decaying overtones, soft 3 ms attack."""
    n = int(dur * SR); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.45) + 0.35 * np.sin(2 * np.pi * 3.93 * f * t) * np.exp(-t / 0.10)
         + 0.08 * np.sin(2 * np.pi * 9.2 * f * t) * np.exp(-t / 0.035))
    att = np.minimum(1, t / 0.003) ** 2
    return x * att * vel


def swell(f, dur, vel=1.0, att=0.25, rel=0.45, breath=0.25):
    """Soft pad: detuned sine + triangle, slow attack, a little band-limited breath around the second partial."""
    n = int((dur + rel) * SR); t = np.arange(n) / SR
    tri = lambda ph: 2 / np.pi * np.arcsin(np.sin(ph))
    x = 0.5 * np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 1.003 * t) + 0.2 * tri(2 * np.pi * f * 0.997 * t)
    nz = signal.sosfilt(signal.butter(2, [1.7 * f, 2.3 * f], 'band', fs=SR, output='sos'), rng.standard_normal(n))
    x = x + breath * nz / (np.std(nz) + 1e-9) * 0.3
    env = np.minimum(1, t / att) * np.where(t < dur, 1, np.exp(-(t - dur) / (rel / 3)))
    return x * env * vel


def tick(vel=1.0):
    """Soft filtered tick: 6 ms noise burst, band 4.5-7 kHz (outside the speech band), gentle."""
    n = int(0.03 * SR); t = np.arange(n) / SR
    x = signal.sosfilt(signal.butter(2, [4500, 7000], 'band', fs=SR, output='sos'), rng.standard_normal(n)) * np.exp(-t / 0.006)
    return x / (np.abs(x).max() + 1e-9) * 0.5 * vel


def pulse(f, vel=1.0):
    """Low soft pulse (felt more than heard): sine with a short pitch drop, 140 ms decay."""
    n = int(0.45 * SR); t = np.arange(n) / SR
    fr = f * (1 + 0.25 * np.exp(-t / 0.02))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.14) * np.minimum(1, t / 0.004) * vel


# ------------------------------------------------------------------ events -> notes
def line_runs(ev, fps):
    runs = {}
    for l in ev['line']:
        runs.setdefault(l['id'], []).append(l)
    out = []
    for lid, ls in runs.items():
        ls.sort(key=lambda r: r['f'])
        cur = [ls[0]]
        for r in ls[1:]:
            if r['f'] - cur[-1]['f'] <= 8:
                cur.append(r)
            else:
                out.append(cur); cur = [r]
        out.append(cur)
    return [{'t0': r[0]['f'] / fps, 't1': (r[-1]['f'] + 1) / fps, 'tf': np.array([x['f'] for x in r]) / fps,
             'slope': np.array([x['slope'] for x in r]), 'x': np.array([x['x'] for x in r])} for r in out if len(r) >= 2]


def render(ev, N, palette, voice):
    fps = ev['fps']
    out = np.zeros((N, 2))
    notes = []  # (t_planned, kind, midi, pan, vel, extra)
    step = 60 / 84 / 2  # eighth notes at the music tempo
    for run in line_runs(ev, fps):
        base = {'mallet': 67, 'breath': 62, 'minimal': 43}[palette]
        span = {'mallet': 12, 'breath': 9, 'minimal': 7}[palette]
        if palette == 'breath':
            # one continuous swell per drawing run; the pitch glides with the slope (quantised steps, 150 ms glide)
            tt = np.arange(int((run['t1'] - run['t0']) * SR)) / SR + run['t0']
            mid = np.array([qpenta(base + span * np.tanh(1.2 * s)) for s in run['slope']], float)
            m = np.interp(tt, run['tf'], mid)
            m = uniform_filter1d(m, int(0.15 * SR))
            f = hz(m)
            ph = 2 * np.pi * np.cumsum(f) / SR
            speed = np.interp(tt, run['tf'][1:], np.abs(np.diff(run['x'])) / np.maximum(np.diff(run['tf']), 1e-3)) if len(run['tf']) > 1 else np.ones_like(tt)
            amp = 0.55 + 0.45 * np.clip(speed / (np.percentile(speed, 90) + 1e-9), 0, 1)  # swells with the change
            amp = uniform_filter1d(amp, int(0.2 * SR))
            n = len(tt); tn = np.arange(n) / SR
            env = np.minimum(1, tn / 0.3) * np.minimum(1, (n - np.arange(n)) / (0.45 * SR))
            x = (0.55 * np.sin(ph) + 0.3 * np.sin(ph * 1.003) + 0.15 * np.sin(2 * ph)) * amp * env
            nz = signal.sosfilt(signal.butter(2, [600, 1000], 'band', fs=SR, output='sos'), rng.standard_normal(n))
            x = x + 0.06 * nz / (np.std(nz) + 1e-9) * amp * env
            p = np.clip((np.interp(tt, run['tf'], run['x']) - 960) / 960, -0.7, 0.7)
            a = (p + 1) * np.pi / 4
            i0 = int(run['t0'] * SR); k = min(n, N - i0)
            out[i0:i0 + k, 0] += (x * np.cos(a))[:k]; out[i0:i0 + k, 1] += (x * np.sin(a))[:k]
            continue
        t = run['t0']
        while t < run['t1']:
            s = float(np.interp(t, run['tf'], run['slope']))
            px = float(np.interp(t, run['tf'], run['x']))
            notes.append([t, 'line', qpenta(base + span * np.tanh(1.2 * s)), np.clip((px - 960) / 960, -0.7, 0.7), 0.7, None])
            t += step
    for d in ev['dot']:
        base = {'mallet': 72, 'breath': 62, 'minimal': 38}[palette]
        notes.append([d['f'] / fps, 'dot', qpenta(base + 24 * (1 - np.clip(d['y'], 0, 1080) / 1080)), np.clip((d['x'] - 960) / 960, -0.7, 0.7), 1.0, None])
    for b in ev.get('bar', []):
        notes.append([b['f0'] / fps, 'bar', qpenta(67 + 12 * float(b.get('value') or 0)), np.clip((b['x'] - 960) / 960, -0.7, 0.7), 0.9, None])
    for k in ev.get('tick', []):
        notes.append([k['f'] / fps, 'tick', 0, np.clip((k['x'] - 960) / 960, -0.7, 0.7), 0.6, None])

    # move discrete notes into syllable gaps
    env = 20 * np.log10(np.sqrt(uniform_filter1d(voice ** 2, int(0.01 * SR))) + 1e-9)
    active = env > -40
    shifts = []
    for nt in notes:
        i = int(nt[0] * SR)
        if 0 <= i < N and active[i]:
            a, b = max(0, i - int(0.06 * SR)), min(N, i + int(0.12 * SR))
            j = a + int(np.argmin(env[a:b]))
            shifts.append(round((j - i) / SR * 1000, 1))
            nt[0] = j / SR
    for t, kind, m, p, vel, _ in notes:
        if palette == 'mallet':
            x = mallet(hz(m), vel) if kind != 'tick' else mallet(hz(84), 0.3, 0.3)
            if kind == 'dot':
                o = 0.35 * mallet(hz(m + 12), vel, 0.8)
                x[:len(o)] += o[:len(x)]
        elif palette == 'breath':
            x = swell(hz(m), 0.35 if kind != 'tick' else 0.05, vel, att=0.08, rel=0.7) if kind != 'line' else np.zeros(1)
            if kind == 'dot':
                o = 0.6 * swell(hz(m + 7), 0.35, vel, att=0.12, rel=0.7)
                k = min(len(x), len(o)); x[:k] += o[:k]
        else:
            if kind == 'line':
                x = 0.9 * pulse(hz(m), vel)
                tk = tick(0.35)
                x[:len(tk)] += tk
            elif kind == 'tick':
                x = tick(vel)
            else:
                x = pulse(hz(m), vel)
                tk = tick(0.8)
                x[:len(tk)] += tk
        add(out, t, pan(x, p))
    return out, {'notes': len(notes), 'shiftedIntoGaps': len(shifts), 'shiftMs': shifts}


def process(root, palette, out_wav, key='D minor'):
    ev = json.load(open(os.path.join(root, 'out', 'sonify-events.json')))
    voice = load_mono(os.path.join(root, 'out', 'audio', 'stems', 'voice.flac'))
    N = len(voice)
    son, rep = render(ev, N, palette, voice)
    # loudness match: active RMS 16 dB under the voice's active RMS
    va = voice[np.abs(voice) > 1e-4]
    sm = np.abs(son).max(1)
    sa = son[sm > 1e-5]
    target = np.sqrt(np.mean(va ** 2)) * 10 ** (-16 / 20)
    son *= target / (np.sqrt(np.mean(sa ** 2)) + 1e-12)
    # voice activity (10 ms RMS > -40 dBFS, held 60 ms), smoothed attack 20 ms / release 250 ms
    e = 20 * np.log10(np.sqrt(uniform_filter1d(voice ** 2, int(0.01 * SR))) + 1e-9)
    act = maximum_filter1d((e > -40).astype(float), int(0.06 * SR))
    g = np.zeros(N); cur = 0.0
    aa, ar = np.exp(-1 / (0.02 * SR)), np.exp(-1 / (0.25 * SR))
    hop = 48
    for i in range(0, N, hop):
        tgt = act[i]
        c = aa if tgt > cur else ar
        cur = tgt + (cur - tgt) * c ** hop
        g[i:i + hop] = cur
    duck = 10 ** (-8 * g / 20)
    sos = signal.butter(4, [1000, 4000], 'band', fs=SR, output='sos')
    for ch in range(2):
        mid = signal.sosfiltfilt(sos, son[:, ch])
        son[:, ch] = (son[:, ch] - mid + mid * (1 - 0.95 * g)) * duck
    wavfile.write(out_wav, SR, son.astype(np.float32))
    rep.update({'palette': palette, 'key': key, 'sidechainDb': -8, 'bandStop1to4kWhileVoice': 0.95, 'levelUnderVoiceDb': -16})
    return rep


if __name__ == '__main__':
    a = sys.argv[1:]
    r = process(a[0], a[1], a[2])
    if '--report' in a:
        json.dump(r, open(a[a.index('--report') + 1], 'w'), indent=1)
    print(json.dumps({k: v for k, v in r.items() if k != 'shiftMs'}))

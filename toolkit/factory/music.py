"""Crux factory music mix (Mốc B): voice + music bed at the level Tập 1–3 used (mix_full.py of Tập 3):
  - music level set so voice is VOICE_OVER_MUSIC dB (20) above music, power measured over voice-active 100 ms windows (A07 method);
  - 1–4 kHz of the music ducked 13 dB while the voice is active (gate 40 ms attack, 350 ms release, 80 ms look-ahead).
  mix(voice_wav, music_wav, total, out_wav, stems_dir) → {'a07_gap_db', 'mid_duck_db'}; loudness is done after, by build.py (loudnorm 2-pass).
"""
import os

import numpy as np
import soundfile as sf
from scipy import signal
from scipy.ndimage import uniform_filter1d

SR = 48000
VOICE_OVER_MUSIC_DB = 20.0
MID_DUCK_DB = 13.0


def load(p, n):
    x, sr = sf.read(p, always_2d=True)
    assert sr == SR, f'{p}: {sr} Hz'
    x = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, 1)
    out = np.zeros((n, 2))
    out[:min(n, len(x))] = x[:n]
    return out


def gate(act, att, rel, hop=48):
    a, r, g, y = np.exp(-hop / (att * SR)), np.exp(-hop / (rel * SR)), 0.0, []
    for v in act[::hop]:
        k = a if v > g else r
        g = k * g + (1 - k) * v
        y.append(g)
    return np.repeat(y, hop)[:len(act)]


def a07_gap(v, m):
    w = int(0.1 * SR)
    k = min(len(v), len(m)) // w
    pv = (v[:k * w].mean(1) ** 2).reshape(k, w).mean(1)
    pm = (m[:k * w].mean(1) ** 2).reshape(k, w).mean(1)
    a = 10 * np.log10(pv + 1e-20) > -45
    return float(10 * np.log10(pv[a].mean()) - 10 * np.log10(pm[a].mean() + 1e-20))


def mix(voice_wav, music_wav, total, out_wav, stems_dir):
    n = int(round(total * SR))
    voice, music = load(voice_wav, n), load(music_wav, n)
    vr = np.sqrt(np.maximum(uniform_filter1d(voice[:, 0] ** 2, int(0.1 * SR)), 0))
    act = (20 * np.log10(vr + 1e-12) > -45).astype(float)
    la = int(0.08 * SR)
    duck = 10 ** (-MID_DUCK_DB * gate(np.concatenate([act[la:], np.zeros(la)]), 0.04, 0.35) / 20)
    b, a = signal.butter(4, [1000, 4000], 'bandpass', fs=SR)
    for ch in range(2):
        mid = signal.filtfilt(b, a, music[:, ch])
        music[:, ch] = music[:, ch] - mid + mid * duck
    vt = act > 0
    music *= np.sqrt(np.mean(voice[vt] ** 2) / np.mean(music[vt].mean(1) ** 2)) * 10 ** (-VOICE_OVER_MUSIC_DB / 20)
    os.makedirs(stems_dir, exist_ok=True)
    sf.write(os.path.join(stems_dir, 'voice.flac'), voice, SR)
    sf.write(os.path.join(stems_dir, 'music.flac'), music, SR)
    out = voice + music
    sf.write(out_wav, out / max(1.0, np.abs(out).max() / 0.98), SR, subtype='PCM_24')
    return {'a07_gap_db': round(a07_gap(voice, music), 2), 'mid_duck_db': MID_DUCK_DB}

"""Blind palette test on the 10 s sample (owner feedback 2026-09-28, sổ gu G-005, G-006).

    python3 episodes/ep001/m0-sample/palettes.py

Three palettes (toolkit/audio/sonify_palettes.py) get blind names S1-S3 in a random order; the decoding is written to
episodes/ep001/review-m1/key.json only. Each version: the sample's voice, music, sfx, whoosh and room stems unchanged +
the new data-sound layer, mixed, mastered to -14 LUFS (true-peak safety -1.5 dBFS sample peak), muxed with the
sample's picture -> episodes/ep001/review-m1/sonify-S{n}.mp4 (< 20 MB). Measurements per blind name ->
review-m1/sonify-metrics.json (builder's own measures, not the checker).
"""
import json
import os
import random
import re
import subprocess
import sys

import numpy as np
from scipy import signal
from scipy.io import wavfile

R = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(R, '..')
REPO = os.path.join(EP, '..', '..')
sys.path.insert(0, os.path.join(REPO, 'toolkit', 'audio'))
import sonify_palettes as SP  # noqa: E402

SR = 48000
PICTURE = os.environ.get('M0_PICTURE') or os.path.join(R, 'work', 'picture.mp4')
REV = os.path.join(EP, 'review-m1')


def lufs(path):
    o = subprocess.run(['ffmpeg', '-nostats', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1])


def stereo(p):
    x = SP.load_mono(p)
    return np.stack([x, x], 1)


def main():
    work = os.path.join(R, 'work', 'palettes')
    os.makedirs(work, exist_ok=True); os.makedirs(REV, exist_ok=True)
    pals = ['mallet', 'breath', 'minimal']
    random.SystemRandom().shuffle(pals)
    key = {f'S{i + 1}': p for i, p in enumerate(pals)}
    stems = {}
    for k in ('voice', 'music', 'sfx', 'whoosh', 'room'):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(R, 'out', 'audio', 'stems', k + '.flac'), '-ar', str(SR), '-ac', '2', '-c:a', 'pcm_f32le',
                        os.path.join(work, k + '.wav')], check=True)
        stems[k] = wavfile.read(os.path.join(work, k + '.wav'))[1].astype(np.float64)
    N = len(stems['voice'])
    band = signal.butter(4, [1500, 8000], 'band', fs=SR, output='sos')
    sp14 = signal.butter(4, [1000, 4000], 'band', fs=SR, output='sos')
    vmono = stems['voice'].mean(1)
    ve = 20 * np.log10(np.sqrt(np.convolve(vmono ** 2, np.ones(480) / 480, 'same')) + 1e-9)
    ev = json.load(open(os.path.join(R, 'out', 'sonify-events.json')))
    metrics = {}
    for name, pal in key.items():
        sw = os.path.join(work, f'sonify-{name}.wav')
        rep = SP.process(R, pal, sw)
        son = wavfile.read(sw)[1].astype(np.float64)[:N]
        son = np.pad(son, ((0, N - len(son)), (0, 0)))
        mix = sum(stems[k] for k in stems) + son
        mw = os.path.join(work, f'mix-{name}.wav')
        wavfile.write(mw, SR, mix.astype(np.float32))
        gain = 10 ** ((-14.0 - lufs(mw)) / 20)
        mix *= gain
        pk = np.abs(mix).max()
        if pk > 10 ** (-1.5 / 20):
            mix *= 10 ** (-1.5 / 20) / pk
        wavfile.write(mw, SR, mix.astype(np.float32))
        # builder's measures: T1-style lift (1.5-8 kHz, 150 ms windows at each event cluster, every 0.5 s) and how much the
        # data layer puts into 1-4 kHz while the voice speaks (relative to the voice in that band)
        s_b = signal.sosfilt(band, (son * gain).mean(1)); r_b = signal.sosfilt(band, (mix - son * gain).mean(1))
        ts = sorted({round(l['f'] / 30, 2) for l in ev['line']} | {round(d['f'] / 30, 2) for d in ev['dot']})
        wins, t0 = [], ts[0]
        while t0 <= ts[-1]:
            a, b = int(t0 * SR), int((t0 + 0.15) * SR)
            ps, pr = np.mean(s_b[a:b] ** 2), np.mean(r_b[a:b] ** 2)
            wins.append(round(10 * np.log10((ps + pr) / pr), 2)); t0 += 0.5
        va = ve > -40
        s14 = signal.sosfilt(sp14, (son * gain).mean(1))[va]; v14 = signal.sosfilt(sp14, vmono * gain)[va]
        metrics[name] = {'liftDbPerWindow': wins, 'medianLiftDb': float(np.median(wins)),
                         'dataVsVoice1to4kWhileSpeakingDb': round(10 * np.log10(np.mean(s14 ** 2) / np.mean(v14 ** 2)), 1),
                         'dataVsVoiceFullBandDb': round(10 * np.log10(np.mean((son * gain).mean(1)[np.abs(son).max(1) > 1e-5] ** 2) / np.mean((vmono * gain)[np.abs(vmono) > 1e-4] ** 2)), 1),
                         'notes': rep['notes'], 'shiftedIntoGaps': rep['shiftedIntoGaps'], 'medianShiftMs': float(np.median(rep['shiftMs'])) if rep['shiftMs'] else 0.0}
        out = os.path.join(REV, f'sonify-{name}.mp4')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', PICTURE, '-i', mw, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-b:v', '4M',
                        '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
                        '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', out], check=True)
        metrics[name]['fileMB'] = round(os.path.getsize(out) / 1e6, 2)
    json.dump({'note': 'blind names; decoding in key.json (do not open before choosing)', 'key': key, 'order': 'random (SystemRandom)',
               'palettes': {'mallet': 'soft pitched mallet (marimba-like), tuned to the music key', 'breath': 'breath / soft pad that swells with the change',
                            'minimal': 'soft filtered tick + low pulse'}}, open(os.path.join(REV, 'key.json'), 'w'), indent=1)
    json.dump({'names': sorted(metrics), 'measures': metrics,
               'rules': 'all three: side-chain -8 dB under the voice, 1-4 kHz removed while the voice speaks, notes moved into syllable gaps (-60..+120 ms), '
                        'pitch mapping unchanged, loudness-matched at -16 dB under the voice (before the side-chain); no +10 dB'}, open(os.path.join(REV, 'sonify-metrics.json'), 'w'), indent=1)
    print(json.dumps({k: {kk: v[kk] for kk in ('medianLiftDb', 'dataVsVoice1to4kWhileSpeakingDb', 'dataVsVoiceFullBandDb', 'shiftedIntoGaps', 'fileMB')} for k, v in metrics.items()}, indent=1))


if __name__ == '__main__':
    main()

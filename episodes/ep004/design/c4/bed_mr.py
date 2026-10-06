"""Tập 4 · G2 (b) — nhạc nền như C5 (episodes/ep003/audio_src/factory_bed.py, style C) rồi hạ về 0 quanh mỗi mid-roll của
episode.yaml (lặng ≥ 1 s cho S14 / episode.md §9): 0 trong [t − 0,75; t + 0,75] s, vào/ra cos 0,4 s. Chỉ mix lại, không đổi nhạc.
  python3 episodes/ep004/design/c4/bed_mr.py <seconds> <out.wav>
"""
import os
import subprocess
import sys

import numpy as np
import soundfile as sf
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
HOLD, RAMP = 0.75, 0.4


def main():
    total, out = sys.argv[1], sys.argv[2]
    raw = out + '.raw.wav'
    subprocess.run([sys.executable, os.path.join(ROOT, 'episodes', 'ep003', 'audio_src', 'factory_bed.py'), total, raw], check=True)
    x, sr = sf.read(raw, always_2d=True)
    t = np.arange(len(x)) / sr
    g = np.ones(len(x))
    for m in yaml.safe_load(open(os.path.join(EP, 'episode.yaml'))).get('midrolls') or []:
        d = np.abs(t - float(m['t']))
        r = np.clip((d - HOLD) / RAMP, 0, 1)
        g = np.minimum(g, 0.5 - 0.5 * np.cos(np.pi * r))
    sf.write(out, x * g[:, None], sr, subtype='PCM_24')
    os.remove(raw)


if __name__ == '__main__':
    main()

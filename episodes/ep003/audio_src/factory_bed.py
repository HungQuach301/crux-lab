"""Tập 3 · nhạc nền cho demo nhà máy (S04): cùng engine nhạc đã duyệt của Tập 3 (mix_full.py: style C, 114 BPM, D dorian, cùng nhạc cụ,
reverb, seed), chỉ ra phần nhạc khô + reverb + fade, KHÔNG trộn: mức dưới lời và ducking do toolkit/factory/music.py làm.
  python3 episodes/ep003/audio_src/factory_bed.py <seconds> <out.wav>
"""
import os
import sys

import numpy as np
from scipy import signal

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mix_full as M  # noqa: E402


def main():
    total, out = float(sys.argv[1]), sys.argv[2]
    N = int(round(total * M.SR))
    _, bars = M.tempo_grid(total)
    dry = M.render_music(N, bars, M.harmony(bars))
    irL, irR = M.reverb_ir()
    music = dry + 0.24 * np.stack([signal.oaconvolve(dry[:, 0], irL)[:N], signal.oaconvolve(dry[:, 1], irR)[:N]], 1)
    t = np.arange(N) / M.SR
    music *= (np.clip(t / 0.6, 0, 1) * np.clip((total - t) / M.END_FADE_S, 0, 1))[:, None]
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    M.write_wav(out, music / max(1e-9, np.abs(music).max()) * 0.5)
    print('bed', out, total, 's')


if __name__ == '__main__':
    main()

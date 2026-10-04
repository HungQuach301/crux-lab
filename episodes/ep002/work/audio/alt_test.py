import sys, os, json, numpy as np
sys.path.insert(0, '/home/user/crux-lab/episodes/ep002/audio_src'); sys.path.insert(0, os.path.dirname(__file__))
sys.argv = ['x']
import mix as M, t2eval
from scipy import signal
tm = json.load(open(M.EV.TIMING)); tl = M.TL(float(tm['total_s']))
beats, bars, bpms = M.tempo_grid(tl)
voice, _ = M.build_voice(tl); gaps = tl.voice_gaps(voice)
gi = {(g['a'], g['b']): g for g in gaps}
sil = [gi[(a, b)] for a, b, _ in M.BEAT_SILENCES]
for v in [29, 31, 37]:
    M.VARIANT = 'alt'; M.ALT_SEED = v; seq = M.harmony(bars)
    dry = M.render_music(tl, bars, seq, sil, set())
    irL, irR = M.reverb_ir(); N = tl.N
    dry = dry + 0.24 * np.stack([signal.oaconvolve(dry[:, 0], irL)[:N], signal.oaconvolve(dry[:, 1], irR)[:N]], 1)
    print(v, t2eval.t2(dry.astype(np.float64), beats), flush=True)

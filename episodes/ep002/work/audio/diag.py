import sys, os, json, numpy as np
sys.path.insert(0, '/home/user/crux-lab/episodes/ep002/audio_src'); sys.path.insert(0, os.path.dirname(__file__))
sys.argv = ['x']
import mix as M, t2eval
from scipy import signal
sys.path.insert(0, '/tmp/claude-0/-home-user-crux-lab/ce118c19-8f87-59ac-a641-3486272a248d/scratchpad/A/ck/checks/py'); import r_sound as R
tm = json.load(open(M.EV.TIMING)); tl = M.TL(float(tm['total_s']))
beats, bars, bpms = M.tempo_grid(tl); seq = M.harmony(bars)
M.VARIANT = 'alt'; M.ALT_SEED = 29
dry = M.render_music(tl, bars, seq, [], set())
irL, irR = M.reverb_ir(); N = tl.N
dry = dry + 0.24 * np.stack([signal.oaconvolve(dry[:, 0], irL)[:N], signal.oaconvolve(dry[:, 1], irR)[:N]], 1)
x = signal.resample_poly(dry.mean(1), 1, 4)
ph = R.phrase_features(x, beats)
def sims(sl):
    out = []
    for i, p in enumerate(ph):
        if p is None: continue
        best = 0
        for L in R.LAGS:
            if i - L >= 0 and ph[i - L] is not None:
                a = np.concatenate([p[1][k*28:(k+1)*28][sl] for k in range(4)]); b = np.concatenate([ph[i-L][1][k*28:(k+1)*28][sl] for k in range(4)])
                best = max(best, a @ b / np.linalg.norm(a) / np.linalg.norm(b))
        out.append(best)
    return np.median(out)
print('chroma', sims(slice(0, 12)), 'onset', sims(slice(12, 28)))
c = ph[10][1][:12]; print('chroma/onset energy share', np.sum(ph[10][1][:12]**2), np.sum(ph[10][1][12:28]**2))

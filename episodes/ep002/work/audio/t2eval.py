import sys, json, numpy as np
from scipy import signal
sys.path.insert(0, '/tmp/claude-0/-home-user-crux-lab/ce118c19-8f87-59ac-a641-3486272a248d/scratchpad/A/ck/checks/py')
import r_sound as R
def t2(x48, beats):
    x = signal.resample_poly(x48.mean(1) if x48.ndim > 1 else x48, 1, 4).astype(np.float32)
    ph = R.phrase_features(x, beats)
    rows = []
    for i, p in enumerate(ph):
        if p is None: continue
        prev = [float(p[1] @ ph[i - L][1]) for L in R.LAGS if i - L >= 0 and ph[i - L] is not None]
        if prev: rows.append(max(prev))
    return 100 * sum(r >= R.SIM_NEAR for r in rows) / len(rows), float(np.median(rows))
if __name__ == '__main__':
    import soundfile as sf
    x, _ = sf.read(sys.argv[1]); b = json.load(open(sys.argv[2]))['beats']
    print(t2(x, b))

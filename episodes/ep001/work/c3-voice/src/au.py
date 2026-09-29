import av, numpy as np
def decode(path, sr=48000):
    c = av.open(path); rs = av.AudioResampler(format='flt', layout='mono', rate=sr); out=[]
    for f in c.decode(audio=0):
        for g in rs.resample(f): out.append(g.to_ndarray().reshape(-1))
    for g in rs.resample(None): out.append(g.to_ndarray().reshape(-1))
    c.close(); return sr, np.concatenate(out).astype(np.float64)
def speech_span(x, sr, thr=-45.0, win=0.02):
    w=int(win*sr); n=len(x)//w
    db=20*np.log10(np.sqrt((x[:n*w].reshape(n,w)**2).mean(axis=1)+1e-12)); on=np.where(db>thr)[0]
    return (on[0]*win,(on[-1]+1)*win) if len(on) else (0.0,len(x)/sr)
def f0_median(x, sr):
    # crude autocorrelation pitch on voiced 40ms frames
    w=int(0.04*sr); fs=[]
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]
        if np.sqrt((s**2).mean())<0.02: continue
        s=s-s.mean(); ac=np.correlate(s,s,'full')[w-1:]
        lo,hi=int(sr/400),int(sr/70); k=lo+np.argmax(ac[lo:hi])
        if ac[k]>0.4*ac[0]: fs.append(sr/k)
    return float(np.median(fs)) if fs else None

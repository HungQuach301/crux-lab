"""Tập 5 · C4 · số đo tiếng trên bản giao (out/video.mp4 + out/audio/stems), cùng cách đo với checks/ (không gọi checks/):
  MR1: khoảng lặng của master (RMS 50 ms / bước 10 ms ≤ −40 dBFS, như S14/A09) chứa giờ mid-roll; độ dài
  A07: lời − nhạc (cửa sổ 100 ms có lời, > −45 dBFS); A08: trung vị độ tụt dải 1–4 kHz của stem nhạc quanh đầu lời (Welch)
  loudness: ffmpeg ebur128 (I, true peak)
  python3 episodes/ep005/c4/audio_report.py → out/factory/audio-report.json"""
import json, os, re, subprocess
import numpy as np
import soundfile as sf
from scipy import signal
import yaml
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 48000


def dec(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).astype(float)


def stem(n):
    for ext in ('flac', 'wav'):
        p = os.path.join(EP, 'out', 'audio', 'stems', f'{n}.{ext}')
        if os.path.exists(p):
            x, sr = sf.read(p, always_2d=True); assert sr == SR; return x.mean(1)


def rms_db(x, win=0.05, hop=0.01):
    w, h = int(win * SR), int(hop * SR)
    n = 1 + (len(x) - w) // h
    idx = np.arange(w)[None, :] + h * np.arange(n)[:, None]
    return np.arange(n) * hop + win / 2, 10 * np.log10((x[idx] ** 2).mean(1) + 1e-20)


Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
mr = Y['midrolls'][0]['t']
m = dec(os.path.join(EP, 'out', 'video.mp4'))
t, db = rms_db(m)
q = db <= -40
i = int(round((mr - 0.025) / 0.01))
a = i
while a > 0 and q[a - 1]: a -= 1
b = i
while b < len(q) - 1 and q[b + 1]: b += 1
sil = [round(t[a] - 0.025, 3), round(t[b] + 0.025, 3)] if q[i] else None
v, mu = stem('voice'), stem('music')
n = min(len(v), len(mu)); w = int(0.1 * SR); k = n // w
pv = (v[:k * w] ** 2).reshape(k, w).mean(1); pm = (mu[:k * w] ** 2).reshape(k, w).mean(1)
act = 10 * np.log10(pv + 1e-20) > -45
a07 = float(10 * np.log10(pv[act].mean()) - 10 * np.log10(pm[act].mean() + 1e-20))
tt = (np.arange(k) + 0.5) * 0.1
ons = [float(tt[j] - 0.05) for j in range(6, k - 6) if act[j] and not act[j - 1] and not act[j - 6:j].any() and act[j:j + 6].all()]
def band(x, t0, t1, lo, hi):
    s = x[int(t0 * SR):int(t1 * SR)]; f, P = signal.welch(s, fs=SR, nperseg=2048); return 10 * np.log10(P[(f >= lo) & (f < hi)].sum() + 1e-20)
pres, rel = [], []
for o in ons:
    a1, b1 = band(mu, o - 0.6, o - 0.1, 1000, 4000), band(mu, o + 0.1, o + 0.6, 1000, 4000)
    if a1 < -90: continue
    a2, b2 = band(mu, o - 0.6, o - 0.1, 60, 500), band(mu, o + 0.1, o + 0.6, 60, 500)
    pres.append(a1 - b1); rel.append((a1 - b1) - (a2 - b2))
r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', os.path.join(EP, 'out', 'video.mp4'), '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
tail = r.stderr[r.stderr.rindex('Summary:'):]
rep = {'mr1_t': mr, 'mr1_silence': sil, 'mr1_silence_s': round(sil[1] - sil[0], 3) if sil else 0.0,
       'a07_voice_minus_music_db': round(a07, 2), 'a08_onsets': len(pres), 'a08_median_1_4k_drop_db': round(float(np.median(pres)), 2) if pres else None,
       'a08_median_band_excess_db': round(float(np.median(rel)), 2) if rel else None,
       'lufs_I': float(re.search(r'I:\s+(-?[\d.]+) LUFS', tail)[1]), 'true_peak_dbfs': float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', tail)[1]),
       'duration_s': round(len(m) / SR, 3)}
json.dump(rep, open(os.path.join(EP, 'out', 'factory', 'audio-report.json'), 'w'), indent=1)
print(json.dumps(rep))

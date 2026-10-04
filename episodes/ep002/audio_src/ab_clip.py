"""review-c6/music-ab.m4a: owner comparison of the default music and the alternative (--music alt), same mix otherwise.
Two excerpts, each played A (default, master.wav) then B (alt, master-alt.wav). Before each play: one soft beep = A, two beeps = B; 1.2 s gaps.
Excerpt 1 holds S02.2 "Leah" (the -8 dB bed dip under the word). Times are read from animatic/timing.json (re-run after a re-time).
    python3 episodes/ep002/audio_src/ab_clip.py
"""
import json, os, subprocess
import numpy as np
import soundfile as sf
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SR = 48000
tm = json.load(open(os.path.join(EP, 'animatic', 'timing.json')))
S = {x['id']: x for s in tm['scenes'] for x in s['sentences']}
leah = next(w for w in S['S02.2']['words'] if w['t'] == 'leah')['start']
ex = [(S['S02.2']['start'] - 1.0, 'S02.2 "Leah" (bed dip) and the federal limits'), (S['S07.5']['start'] - 0.5, 'S07.5 the two rides (data sounds, full drive)')]
L = 12.5
def beep(n):
    t = np.arange(int(0.12 * SR)) / SR
    b = 0.12 * np.sin(2 * np.pi * 880 * t) * np.sin(np.pi * t / 0.12)
    gap = np.zeros(int(0.12 * SR))
    return np.concatenate(sum([[b, gap] for _ in range(n)], []) + [np.zeros(int(0.3 * SR))])
def cut(path, t0):
    x, sr = sf.read(path, start=int(t0 * SR), stop=int((t0 + L) * SR)); assert sr == SR
    f = np.minimum(1, np.minimum(np.arange(len(x)) / (0.15 * SR), (len(x) - 1 - np.arange(len(x))) / (0.4 * SR)))[:, None]
    return x * f
parts, idx = [], []
for t0, what in ex:
    for lab, n, p in (('A', 1, 'master.wav'), ('B', 2, 'master-alt.wav')):
        bp = beep(n); parts.append(np.stack([bp, bp], 1))
        idx.append({'at': round(sum(len(q) for q in parts) / SR, 2), 'play': lab, 'from': round(t0, 2), 'to': round(t0 + L, 2), 'what': what})
        parts += [cut(os.path.join(EP, 'out', 'audio', p), t0), np.zeros((int(1.2 * SR), 2))]
y = np.concatenate(parts)
os.makedirs(os.path.join(EP, 'review-c6'), exist_ok=True)
w = os.path.join(EP, 'work', 'audio', 'ab.wav'); sf.write(w, y, SR, subtype='PCM_24')
out = os.path.join(EP, 'review-c6', 'music-ab.m4a')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', w, '-c:a', 'aac', '-b:a', '256k', out], check=True); os.remove(w)
json.dump({'_about': 'music-ab.m4a: A = default music (out/audio/master.wav), B = alternative (master-alt.wav); one beep before A, two before B.',
           'durationS': round(len(y) / SR, 2), 'leahAt': round(leah, 2), 'plays': idx}, open(os.path.join(EP, 'review-c6', 'music-ab.json'), 'w'), indent=1)
print(round(len(y) / SR, 2), 's', idx)

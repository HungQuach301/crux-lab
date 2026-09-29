"""Calibration roots for T1/L1 (K2). m0 = the builder's m0-sample (+10 dB data sounds) as delivered (stems) with the preview as master
(the 25 MB master is not committed). S1..S3 = the blind palettes: only the mixed mp4 exists, so the checker derives the data stem
as  mix/g − Σ(other m0 stems), g = least-squares gain of the other stems in the mix (the palettes changed only the data layer)."""
import json, os, shutil, subprocess, sys
import numpy as np, soundfile as sf
E = 'ep001/episodes/ep001/'
def dec(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-map', '0:a:0', '-f', 'f32le', '-ac', '2', '-ar', '48000', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
N = 480000
names = ['voice', 'music', 'sfx', 'whoosh', 'room']
st = {n: dec(E + f'm0-sample/out/audio/stems/{n}.flac')[:N] for n in names + ['sonify']}
rest = sum(st[n] for n in names)
bands = json.load(open('cal-bands.json'))
def root(name, video, son, gain):
    r = f'cal/{name}'
    shutil.rmtree(r, ignore_errors=True)
    os.makedirs(r + '/out/audio/stems', exist_ok=True)
    os.makedirs(r + '/out/checks', exist_ok=True)
    for f in ['script.json', 'sonify-events.json', 'timeline.json', 'claims.json']:
        shutil.copy(E + 'm0-sample/out/' + f, r + '/out/' + f)
    shutil.copy(E + 'm0-sample/out/checks/page.json', r + '/out/checks/page.json')
    shutil.copy(video, r + '/out/video.mp4')
    for n in names:
        sf.write(f'{r}/out/audio/stems/{n}.wav', (st[n] * gain).astype(np.float32), 48000, subtype='FLOAT')
    sf.write(f'{r}/out/audio/stems/sonify.wav', (son * gain).astype(np.float32), 48000, subtype='FLOAT')
    json.dump({'episode': 'ep001-calibration-' + name, 'sonification': {'stem': 'sonify', 'bandsHz': bands[name]}}, open(r + '/contract.json', 'w'), indent=1)
root('m0', E + 'm0-sample/work/preview.mp4', st['sonify'], 1.0)
for k in ['S1', 'S2', 'S3']:
    m = dec(E + f'review-m1/sonify-{k}.mp4')[:N]
    g = float(np.sum(m * rest) / np.sum(rest * rest))
    root(k, E + f'review-m1/sonify-{k}.mp4', m / g - rest, g)
    print(k, 'gain', round(g, 4))
if len(sys.argv) > 1:  # method check: derive the m0 data stem from the m0 preview the same way and compare with the delivered stem
    m = dec(E + 'm0-sample/work/preview.mp4')[:N]
    tot = rest + st['sonify']
    g = float(np.sum(m * rest) / np.sum(rest * rest))
    bands['m0d'] = bands['m0']
    root('m0d', E + 'm0-sample/work/preview.mp4', m / g - rest, g)
    print('m0d gain', g)

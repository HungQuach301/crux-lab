"""K4.4 · A33 trên dữ liệu thật Tập 4–7: A12 (tempo-map thật + transitions thật), A13 (takes.json + timeline thật + take thô thật),
R01 (tension-map.json thật). Stem của nhà máy (out/audio/stems/*) không có trong git: stem giọng TÁI DỰNG = mỗi take thô đặt ở đầu cảnh của nó
+ 0,3 s (nhà máy không kéo giãn take: 0 ký tự EL); stem nhạc = nhiễu −60 dBFS (A12 chỉ chứng minh không còn lỗi máy và đo 'accents on a cut').
  python3 checks-runs/K44/a33/a33_real.py <out.json>   (chạy với checks/py hiện hành; trước/sau = chạy trên hai mã)"""
import json, os, shutil, subprocess, sys, tempfile
import numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'checks', 'py'))
import common, run as runner  # noqa
from common import SR
RULES = {fn.rid: fn for fn in common.RULES}

def dec(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32)

out = {}
for ep in ['ep004', 'ep005', 'ep006', 'ep007']:
    E = os.path.join(REPO, 'episodes', ep); d = tempfile.mkdtemp(prefix=f'a33-{ep}-')
    os.makedirs(os.path.join(d, 'out', 'voice')); os.makedirs(os.path.join(d, 'out', 'audio', 'stems'))
    for rel in ['out/timeline.json', 'out/voice/takes.json', 'out/tempo-map.json', 'out/transitions.json', 'out/tension-map.json', 'contract.json']:
        if os.path.exists(os.path.join(E, rel)): shutil.copy(os.path.join(E, rel), os.path.join(d, rel))
    tl = json.load(open(os.path.join(E, 'out/timeline.json'))); sc = {s['id']: s for s in tl['scenes']}
    takes = json.load(open(os.path.join(E, 'out/voice/takes.json')))['takes']
    v = np.zeros(int((tl['total'] + 1) * SR), np.float32); placed = 0
    for tk in takes:
        if not tk.get('raw') or tk['id'] not in sc or not os.path.exists(os.path.join(E, tk['raw'])): continue
        os.makedirs(os.path.join(d, os.path.dirname(tk['raw'])), exist_ok=True); shutil.copy(os.path.join(E, tk['raw']), os.path.join(d, tk['raw']))
        x = dec(os.path.join(E, tk['raw'])); i = int((sc[tk['id']]['start'] + 0.3) * SR)
        end = int(sc[tk['id']].get('end', sc[tk['id']]['start'] + sc[tk['id']]['dur']) * SR)
        x = x[:max(0, end - i)]; v[i:i + len(x)] += x; placed += 1
    sf.write(os.path.join(d, 'out/audio/stems/voice.flac'), np.stack([v, v], 1), SR)
    m = (np.random.default_rng(0).standard_normal(len(v)) * 10 ** (-60 / 20)).astype(np.float32)
    sf.write(os.path.join(d, 'out/audio/stems/music.flac'), np.stack([m, m], 1), SR)
    for n in ('sfx', 'whoosh'): sf.write(os.path.join(d, f'out/audio/stems/{n}.flac'), np.zeros((len(v), 2), np.float32), SR)
    ctx = common.Ctx(d); res = {'takesPlaced': placed}
    for rid in ('A12', 'A13', 'R01'):
        r = common.safe(RULES[rid], ctx)
        res[rid] = {'status': r['status'], 'note': (r.get('note') or '')[:160], 'metrics': {mm['name']: mm['value'] for mm in r.get('metrics', [])}}
    out[ep] = res; shutil.rmtree(d, ignore_errors=True)
    print(ep, json.dumps(res)[:600], flush=True)
json.dump(out, open(sys.argv[1], 'w'), indent=1)

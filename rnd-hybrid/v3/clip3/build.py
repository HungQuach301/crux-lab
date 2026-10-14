"""R&D vòng 3: clip v3 (P3 — tranh in báo 1930, 2.5D; Today màu sạch), cùng lời/giọng/mốc với v2 (không gọi API giọng lần nữa).
Dựng bằng toolkit/factory/world/render_shots.js nguyên trạng: thư mục đoạn rnd-hybrid/v3/clip3/seg (P3 tranh in báo 1930 + Today màu sạch).
  python3 rnd-hybrid/v3/clip3/build.py --plan            → seg/spine.json, seg/timeline.json (mốc từ lời đã tăng nhịp)
  python3 rnd-hybrid/v3/clip3/build.py [--res 1080] [--workers 4]   → work/v2/clip-<res>.mp4 + clip/out/build-<res>.json
Giọng: một take ElevenLabs (voice_v2.py, 48,08 s ở speed 0.9) → atempo 1.06 (giữ cao độ) ≈ 45,4 s; mọi mốc chữ chia cùng hệ số.
"""
import hashlib, json, os, re, subprocess, sys, time
import numpy as np
from scipy.io import wavfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
SEG = os.path.join(HERE, 'seg'); WORK = os.path.join(ROOT, 'rnd-hybrid', 'work', 'v3clip3'); os.makedirs(WORK, exist_ok=True)
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
FPS, OFF, TAIL, TEMPO = 30, 0.3, 1.2, 1.06
RES = int(arg('--res', 1080)); WORKERS = int(arg('--workers', 4))
V = json.load(open(os.path.join(ROOT, 'rnd-hybrid', 'work', 'v2', 'voice.json')))   # take v2 (cache), 0 ký tự mới
WORDS = [{**x, 's': x['s'] / TEMPO, 'e': x['e'] / TEMPO} for x in V['words']]
SENT = {s['id']: {**s, 'start': s['start'] / TEMPO, 'end': s['end'] / TEMPO} for s in V['sentences']}
DUR = V['duration'] / TEMPO
TOTAL = round(round((DUR + OFF + TAIL) * FPS) / FPS, 4)


def w(sid, prefix, n=1, end=False):
    k = 0
    for x in WORDS:
        if x['sid'] == sid and re.sub(r'[^a-z0-9-]', '', x['w'].lower()).startswith(prefix.lower()):
            k += 1
            if k == n:
                return round((x['e'] if end else x['s']) + OFF, 3)
    raise SystemExit(f'anchor {sid}:{prefix} not found')


cut = lambda sid: round(SENT[sid]['start'] + OFF - 0.08, 3)
endof = lambda sid: round(SENT[sid]['end'] + OFF, 3)
fr = lambda t: round(round(t * FPS) / FPS, 4)   # ranh giới cảnh trùng khung

# ---- cảnh (ranh giới) — mỗi cảnh một câu hoặc nửa câu
B = [('A1', 0.0), ('A2', w('s01', 'looked')), ('B', cut('s02')), ('C', cut('s03')), ('D', cut('s04')), ('E', cut('s05')), ('F', w('s05', 'you')),
     ('G', cut('s06')), ('H', w('s06', 'new')), ('I', cut('s07')), ('J', endof('s07') - 0.9), ('K1', cut('s08')), ('K2', w('s08', 'congress')),
     ('L1', cut('s09')), ('L2', w('s09', 'up')), ('M', cut('s10')), ('N', cut('s11')), ('O', cut('s12')), ('P', cut('s13'))]
shots = [{'id': sid, 't0': fr(t), 't1': fr(B[i + 1][1]) if i + 1 < len(B) else TOTAL} for i, (sid, t) in enumerate(B)]
A = {  # mốc chữ dùng trong scene.js (giây toàn cục)
    'year1930': w('s01', 'nineteen'), 'home': w('s01', 'home'), 'half': w('s02', 'half'), 'three': w('s03', 'three'), 'five': w('s03', 'five'),
    'whole': w('s04', 'whole'), 'once': w('s04', 'once'), 'noloan': w('s05', 'no'), 'lose': w('s05', 'lose'), 'december': w('s06', 'december'),
    'closed': w('s06', 'closed'), 'depositors': w('s07', 'depositors'), 'congress': w('s08', 'congress'), 'fha': w('s08', 'fha'),
    'insured': w('s09', 'insured'), 'eighty': w('s09', 'eighty'), 'value': w('s09', 'value'), 'paid': w('s10', 'paid'), 'month': w('s10', 'month'),
    'twenty': w('s10', 'twenty'), 'nogiant': w('s11', 'no'), 'bill': w('s11', 'bill'), 'y1954': w('s12', 'nineteen'), 'thirty': w('s12', 'thirty'),
    'long': w('s13', 'long'), 'starts': w('s13', 'starts'),
}
ARCHIVAL = {'in': shots[[s['id'] for s in shots].index('I')]['t0'], 'out': shots[[s['id'] for s in shots].index('J')]['t0'] + 0.8}
assert ARCHIVAL['out'] - ARCHIVAL['in'] <= 6.0, 'RIGHTS §F3: ≤ 6 s liền'
os.makedirs(SEG, exist_ok=True)
json.dump({'note': 'R&D v2 clip: cảnh = ranh giới câu/nửa câu; mốc ở timeline.json', 'total': TOTAL, 'shots': shots, 'moves': []}, open(os.path.join(SEG, 'spine.json'), 'w'), indent=1)
json.dump({'fps': FPS, 'total': TOTAL, 'shots': shots, 'a': A, 'archival': ARCHIVAL}, open(os.path.join(SEG, 'timeline.json'), 'w'), indent=1)
json.dump(['rnd-hybrid/v3/style/figure1930.js', 'rnd-hybrid/v3/style/street2d.js', 'rnd-hybrid/cutout/rig.js', 'rnd-hybrid/v3/clip3/seg/timeline.json', 'rnd-hybrid/work/external/bank1931_crop.jpg'], open(os.path.join(SEG, 'inputs.json'), 'w'), indent=1)
durs = sorted(s['t1'] - s['t0'] for s in shots)
print(f'total {TOTAL} s, {len(shots)} shots, median {np.median(durs):.2f} s, min {durs[0]:.2f}, max {durs[-1]:.2f}, archival {ARCHIVAL}')
if '--plan' in sys.argv:
    raise SystemExit(0)

# ---- hình: render_shots (cache theo cảnh)
env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
pic = os.path.join(WORK, f'picture-{RES}.mp4'); T = time.time()
r = subprocess.run(['node', os.path.join(ROOT, 'toolkit/factory/world/render_shots.js'), os.path.relpath(SEG, ROOT), str(RES), pic, '--workers', str(WORKERS),
                    '--cache', os.path.join(WORK, 'cache', str(RES))], cwd=ROOT, env=env, capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:], r.stderr[-3000:]); raise SystemExit('render failed')
render_s = round(time.time() - T, 1); rr = json.load(open(pic + '.render.json'))

# ---- tiếng: giọng (atempo) + sột soạt giấy mỗi lần cắt + "pop" khi thẻ giấy hiện + nền hai hợp âm; loudnorm −14 LUFS
SR = 48000; n = int(TOTAL * SR)
vt = os.path.join(WORK, 'voice-tempo.wav')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', V['wav'], '-filter:a', f'atempo={TEMPO}', '-ar', str(SR), '-ac', '1', vt], check=True)
_, vo = wavfile.read(vt); vo = vo.astype(np.float32) / 32768.0
voice = np.zeros(n, np.float32); a = int(OFF * SR); voice[a:a + len(vo)] = vo[:n - a]
rng = np.random.default_rng(1401); sfx = np.zeros(n, np.float32)
def put(t, x, g):
    i = int(t * SR); j = min(n, i + len(x)); sfx[i:j] += g * x[:j - i]
for t in [A[k] for k in ('half', 'three', 'whole', 'closed', 'fha', 'eighty', 'twenty', 'bill', 'thirty')]:   # thẻ giấy bật lên
    L = int(0.09 * SR); env_ = np.exp(-np.linspace(0, 9, L)); x = rng.standard_normal(L) * env_
    x = np.convolve(x, np.ones(6) / 6, 'same'); x += 0.6 * np.sin(2 * np.pi * 900 * np.arange(L) / SR) * np.exp(-np.linspace(0, 30, L)); put(t, x, 0.09)
for s in shots[1:]:
    L = int(0.22 * SR); env_ = np.sin(np.linspace(0, np.pi, L)) ** 2; x = rng.standard_normal(L) * env_
    x = np.convolve(x, np.ones(24) / 24, 'same'); put(max(0, s['t0'] - 0.12), x, 0.08)
tt = np.arange(n) / SR; bed = np.zeros(n, np.float32); tK = shots[[s['id'] for s in shots].index('K1')]['t0']
for f, a0, a1 in [(110.0, 0, tK), (130.81, 0, tK), (164.81, 0, tK), (146.83, tK, TOTAL), (185.0, tK, TOTAL), (220.0, tK, TOTAL)]:
    m = (tt >= a0) & (tt < a1); bed[m] += np.sin(2 * np.pi * f * tt[m]) * 0.5 + 0.15 * np.sin(4 * np.pi * f * tt[m])
bed *= 0.012 * np.clip(tt / 1.0, 0, 1) * np.clip((TOTAL - tt) / 1.5, 0, 1)
raw = os.path.join(WORK, 'mix-raw.wav'); wavfile.write(raw, SR, (np.clip(voice + sfx + bed, -1, 1) * 32767).astype(np.int16))
out = os.path.join(WORK, f'clip-{RES}.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', pic, '-i', raw, '-filter:a', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], check=True)
rep = {'res': RES, 'fps': FPS, 'total_s': TOTAL, 'shots': len(shots), 'shot_durations': {s['id']: round(s['t1'] - s['t0'], 2) for s in shots},
       'median_shot_s': round(float(np.median(durs)), 2), 'min_shot_s': round(durs[0], 2), 'max_shot_s': round(durs[-1], 2),
       'archival_s': round(ARCHIVAL['out'] - ARCHIVAL['in'], 2), 'archival_share': round((ARCHIVAL['out'] - ARCHIVAL['in']) / TOTAL, 3),
       'render_wall_s': render_s, 'render': rr, 'voice_chars_this_take': V['chars'], 'tempo': TEMPO,
       'video': os.path.relpath(out, ROOT), 'sha256': hashlib.sha256(open(out, 'rb').read()).hexdigest()}
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
json.dump(rep, open(os.path.join(HERE, 'out', f'build-{RES}.json'), 'w'), indent=1); print(json.dumps(rep))

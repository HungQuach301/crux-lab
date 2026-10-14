"""R&D rnd-hybrid: 45 s test clip "before 1934: 5-year balloon → Great Depression → FHA / 30-year loan".
Paper-cutout characters (rnd-hybrid/cutout) + archival photo slots + one existing factory data template (bars, bignum), rendered by the
existing factory renderer (toolkit/factory/render.js + page.html, custom_symbols), 30 fps, deterministic.
  python3 rnd-hybrid/clip/make_clip.py [--workers 3] [--res 1080|540]
Outputs (rnd-hybrid/work/, not committed): job.json, seg/*.mp4, picture.mp4, mix.wav, clip.mp4; report → rnd-hybrid/clip/out/build.json
"""
import hashlib, json, os, re, subprocess, sys, time
import numpy as np
from scipy.io import wavfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(ROOT, 'rnd-hybrid', 'work'); os.makedirs(os.path.join(WORK, 'seg'), exist_ok=True)
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
FPS, OFF, TAIL = 30, 0.3, 2.0
RES = int(arg('--res', 1080)); WORKERS = int(arg('--workers', 3))
V = json.load(open(os.path.join(WORK, 'voice.json')))
WORDS = V['words']; SENT = {s['id']: s for s in V['sentences']}
TOTAL = round(V['duration'] + OFF + TAIL, 3)


def w(sid, prefix, n=1):
    """global time of the n-th word of sentence sid starting with prefix"""
    k = 0
    for x in WORDS:
        if x['sid'] == sid and re.sub(r'[^a-z0-9-]', '', x['w'].lower()).startswith(prefix.lower()):
            k += 1
            if k == n:
                return round(x['s'] + OFF, 3)
    raise SystemExit(f'anchor {sid}:{prefix} not found')


cut = lambda sid: round(SENT[sid]['start'] + OFF - 0.08, 3)
C = {'warn': '#F2B441', 'accent': '#4C8DFF', 'neg': '#E5484D', 'pos': '#3FBF7F', 'paper': '#EDE4CF', 'ink': '#0E1116'}

# ---- shots: (id, template, t0, t1, p) with p times in GLOBAL seconds; localised below
S = []
def shot(sid, tpl, t0, t1, p): S.append({'id': sid, 'template': tpl, 't0': t0, 't1': t1, 'p': p})

t0, t1 = 0.0, cut('s02')
shot('A-home1930', 'cutout', t0, t1, {'era': 1930, 'year': '1930', 'yearAt': w('s01', 'nineteen'), 'cam': [[0, [960, 540, 1.0]], [t1, [1010, 520, 1.07]]],
     'items': [{'kind': 'prop', 'id': 'house', 'x': 1240, 'y': 860, 's': 1.0, 'pop': False},
               {'kind': 'char', 'id': 'ruth', 'x': 560, 'y': 860, 's': 0.92, 'move': [[0, [150, 860]], [1.7, [560, 860]]], 'walk': [0, 1.7], 'expr': 'happy', 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 780, 'y': 860, 's': 0.95, 'move': [[0, [330, 860]], [1.8, [780, 860]]], 'walk': [0, 1.8], 'expr': 'happy', 'poses': [[w('s01', 'home'), 'wave']], 'pop': False},
               {'kind': 'sticker', 'text': 'NEW HOME', 'x': 1240, 'y': 330, 'rot': -6, 'at': w('s01', 'home'), 'bg': C['paper']}]})
t0, t1 = t1, cut('s03')
shot('B-down', 'cutout', t0, t1, {'era': 1930, 'year': '1930', 'cam': [[t0, [800, 560, 1.28]], [t1, [820, 540, 1.36]]],
     'items': [{'kind': 'char', 'id': 'walt', 'x': 700, 'y': 860, 's': 0.95, 'pose': 'hold', 'expr': 'worried', 'exprs': [[w('s02', 'big'), 'shocked']], 'pop': False},
               {'kind': 'coins', 'x': 860, 'y': 860, 'n': 12, 'cols': 4, 'every': 0.09, 'at': w('s02', 'needed'), 's': 1.1},
               {'kind': 'sticker', 'text': 'BIG DOWN PAYMENT', 'x': 1130, 'y': 420, 'rot': 4, 'at': w('s02', 'down'), 'size': 58}]})
t0, t1 = t1, cut('s04')
shot('C-lend', 'cutout', t0, t1, {'era': 1930, 'year': '1930', 'cam': [[t0, [960, 540, 1.0]], [t1, [1000, 540, 1.05]]],
     'items': [{'kind': 'prop', 'id': 'bank', 'x': 1380, 'y': 860, 's': 1.0, 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 520, 'y': 860, 's': 0.95, 'pose': 'stand', 'poses': [[w('s03', 'lent') + 0.6, 'hold']], 'expr': 'neutral', 'exprs': [[w('s03', 'rest'), 'happy']], 'pop': False},
               {'kind': 'prop', 'id': 'note', 'x': 1380, 'y': 700, 's': 0.6, 'at': w('s03', 'bank'), 'move': [[w('s03', 'lent'), [1380, 640]], [w('s03', 'rest'), [720, 700]]], 'rot': [[w('s03', 'lent'), 0], [w('s03', 'rest'), -8]],
                'stamp': {'text': '5 YEARS', 'at': w('s03', 'five'), 'rot': -8, 'dy': -120, 'size': 60, 'bg': C['warn']}}]})
t0, t1 = t1, cut('s05')
shot('D-interest', 'cutout', t0, t1, {'era': 1930, 'year': '1930', 'cam': [[t0, [960, 560, 1.12]], [t1, [930, 560, 1.18]]],
     'items': [{'kind': 'prop', 'id': 'bank', 'x': 1380, 'y': 860, 's': 1.0, 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 560, 'y': 860, 's': 0.95, 'pose': 'point', 'expr': 'neutral', 'pop': False},
               {'kind': 'coins', 'x': 1080, 'y': 860, 'n': 4, 'cols': 4, 'every': 0.45, 'at': w('s04', 'month')},
               {'kind': 'sticker', 'text': 'INTEREST ONLY', 'x': 960, 'y': 250, 'rot': -3, 'at': w('s04', 'only'), 'bg': C['paper']}]})
t0, t1 = t1, cut('s06')
shot('E-balloon', 'cutout', t0, t1, {'era': 1930, 'cam': [[t0, [900, 560, 1.05]], [t1, [900, 540, 1.12]]],
     'items': [{'kind': 'char', 'id': 'walt', 'x': 520, 'y': 860, 's': 0.95, 'pose': 'stand', 'poses': [[w('s05', 'due'), 'shock']], 'expr': 'neutral', 'exprs': [[w('s05', 'due'), 'shocked']], 'pop': False},
               {'kind': 'prop', 'id': 'note', 'x': 1240, 'y': 900, 's': 0.7, 'at': w('s05', 'whole') - 0.2, 'popDur': 0.5, 'rot': [[w('s05', 'whole'), 4], [w('s05', 'due'), -4]]},
               {'kind': 'sticker', 'text': 'ALL DUE AT ONCE', 'x': 1240, 'y': 300, 'rot': 5, 'at': w('s05', 'due'), 'bg': C['neg'], 'fg': '#FFFFFF', 'size': 66}]})
t0, t1 = t1, cut('s07')
shot('F-renew', 'cutout', t0, t1, {'era': 1930, 'cam': [[t0, [960, 540, 1.0]], [t1, [980, 540, 1.04]]],
     'items': [{'kind': 'prop', 'id': 'bank', 'x': 1380, 'y': 860, 's': 1.0, 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 600, 'y': 860, 's': 0.95, 'pose': 'stand', 'poses': [[w('s06', 'signed'), 'hold']], 'expr': 'worried', 'exprs': [[w('s06', 'new'), 'relieved']], 'pop': False},
               {'kind': 'prop', 'id': 'note', 'x': 1380, 'y': 640, 's': 0.55, 'at': w('s06', 'simply'), 'move': [[w('s06', 'simply'), [1380, 640]], [w('s06', 'new'), [820, 700]]],
                'stamp': {'text': 'RENEWED', 'at': w('s06', 'new'), 'rot': 6, 'dy': -110, 'size': 54, 'bg': C['pos']}}]})
t0, t1 = t1, cut('s08')
shot('G-archival-bank', 'archival', t0, t1, {'slot': 'bank1931', 'subject': 'Crowd outside a failed bank, New York', 'record': 'LoC cph.3c17261',
     'year': '1931', 'source': 'Source: Library of Congress (NYWT&S), 1931', 'caption': 'Archival photo'})
t0, t1 = t1, cut('s09')
shot('H-closed', 'cutout', t0, t1, {'era': 1930, 'cam': [[t0, [1060, 560, 1.0]], [t1, [1020, 560, 1.08]]],
     'items': [{'kind': 'prop', 'id': 'bank', 'x': 1500, 'y': 860, 's': 1.0, 'doors': [[w('s08', 'no'), 0], [w('s08', 'no') + 0.5, 1]], 'pop': False},
               {'kind': 'queue', 'x': 720, 'y': 880, 'n': 7, 'gap': 72, 'at': t0 - 1, 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 440, 'y': 880, 's': 0.95, 'pose': 'stand', 'poses': [[w('s08', 'due'), 'slump']], 'expr': 'worried', 'exprs': [[w('s08', 'due'), 'sad']], 'pop': False},
               {'kind': 'sticker', 'text': 'CLOSED', 'x': 1500, 'y': 640, 'rot': -10, 'at': w('s08', 'no') + 0.3, 'bg': C['neg'], 'fg': '#FFFFFF'},
               {'kind': 'sticker', 'text': 'DUE NOW', 'x': 860, 'y': 330, 'rot': 5, 'at': w('s08', 'due'), 'bg': C['warn']}]})
t0, t1 = t1, w('s09', 'around') - 0.1
shot('I-archival-fsa', 'archival', t0, t1, {'slot': 'fsa_auction', 'subject': 'Farm auction after foreclosure, Nebraska', 'record': 'LoC FSA/OWI (Rothstein, Kearney NE)',
     'year': '1936', 'source': 'Source: Library of Congress (FSA/OWI), 1936', 'caption': 'Archival photo'})
t0, t1 = t1, cut('s10')
shot('J-data-foreclosures', 'bignum', t0, t1, {'claim': 'foreclosures_per_day', 'at': w('s09', 'thousand') - t0, 'caption': 'homes foreclosed per day, 1933',
     'sub': 'Source: Wheelock (2008), Federal Reserve Bank of St. Louis', 'captionAt': w('s09', 'foreclosed') - t0, 'role': 'warn'})
t0, t1 = t1, w('s10', 'insured') - 0.1
shot('K-fha', 'cutout', t0, t1, {'era': 1930, 'year': '1934', 'yearAt': w('s10', 'nineteen'), 'cam': [[t0, [960, 540, 1.0]], [t1, [960, 520, 1.06]]],
     'items': [{'kind': 'char', 'id': 'ruth', 'x': 520, 'y': 860, 's': 0.92, 'pose': 'stand', 'poses': [[w('s10', 'federal'), 'point']], 'expr': 'worried', 'exprs': [[w('s10', 'federal'), 'happy']], 'pop': False},
               {'kind': 'char', 'id': 'walt', 'x': 330, 'y': 860, 's': 0.95, 'pose': 'slump', 'poses': [[w('s10', 'federal') + 0.3, 'stand']], 'expr': 'sad', 'exprs': [[w('s10', 'administration'), 'neutral']], 'pop': False},
               {'kind': 'sticker', 'text': 'FEDERAL HOUSING ADMINISTRATION', 'x': 1220, 'y': 470, 'rot': -3, 'at': w('s10', 'federal'), 'bg': C['accent'], 'fg': '#FFFFFF', 'size': 50},
               {'kind': 'sticker', 'text': 'FHA', 'x': 1220, 'y': 300, 'rot': 4, 'at': w('s10', 'federal') + 0.25, 'bg': C['paper'], 'size': 96}]})
t0, t1 = t1, cut('s11')
shot('L-newloan', 'cutout', t0, t1, {'era': 1930, 'year': '1934', 'cam': [[t0, [960, 540, 1.0]], [t1, [960, 540, 1.05]]],
     'items': [{'kind': 'prop', 'id': 'note', 'x': 620, 'y': 860, 's': 0.75, 'pop': False, 'alpha': 0.6, 'stamp': {'text': 'OLD: ALL DUE', 'at': t0, 'rot': -8, 'dy': -150, 'size': 50, 'bg': '#9AA4B2'}},
               {'kind': 'prop', 'id': 'note', 'x': 1300, 'y': 860, 's': 0.85, 'at': w('s10', 'different') - 0.15, 'label': 'FHA LOAN',
                'stamp': {'text': 'NEW', 'at': w('s10', 'different'), 'rot': 7, 'dy': -170, 'size': 70, 'bg': C['accent'], 'fg': '#FFFFFF'}}]})
t0, t1 = t1, cut('s12')
shot('M-monthly', 'cutout', t0, t1, {'era': 1930, 'year': '1934', 'cam': [[t0, [960, 540, 1.0]], [t1, [960, 520, 1.05]]],
     'items': [{'kind': 'build', 'x': 1240, 'y': 860, 's': 1.0, 'from': w('s11', 'paid'), 'to': t1 + 0.4, 'pop': False},
               {'kind': 'char', 'id': 'ruth', 'x': 520, 'y': 860, 's': 0.92, 'pose': 'stand', 'poses': [[w('s11', 'little'), 'cheer']], 'expr': 'happy', 'exprs': [[w('s11', 'little'), 'relieved']], 'pop': False},
               {'kind': 'coins', 'x': 760, 'y': 860, 'n': 6, 'cols': 6, 'every': 0.32, 'at': w('s11', 'paid'), 's': 0.9},
               {'kind': 'sticker', 'text': 'A LITTLE EVERY MONTH', 'x': 960, 'y': 230, 'rot': -2, 'at': w('s11', 'little'), 'bg': C['paper'], 'size': 56}]})
t0, t1 = t1, w('s13', 'those') - 0.1
shot('N-data-lump', 'bars', t0, t1, {'title': 'Due in one payment at the end ($5,000 loan)', 'at': 0.05, 'illustrative': True,
     'items': [{'label': 'Pre-1934 loan', 'claim': 'lump_balloon', 'role': 'warn', 'at': 0.1}, {'label': 'FHA-style loan', 'claim': 'lump_amortized', 'role': 'accent', 'at': w('s12', 'giant') - t0}]})
t0, t1 = t1, cut('s14')
shot('O-thirty', 'cutout', t0, t1, {'era': 'now', 'cam': [[t0, [960, 540, 1.0]], [t1, [960, 540, 1.04]]],
     'items': [{'kind': 'prop', 'id': 'note', 'x': 960, 'y': 940, 's': 1.15, 'pop': False, 'label': 'MORTGAGE', 'rot': [[t0, -3], [t1, 2]]},
               {'kind': 'sticker', 'text': '30 YEARS', 'x': 960, 'y': 330, 'rot': -5, 'at': w('s13', 'thirty'), 'bg': C['warn'], 'size': 90}]})
t0, t1 = t1, round(V['duration'] + OFF + 0.35, 3)
shot('P-today', 'cutout', t0, t1, {'era': 'now', 'year': 'TODAY', 'yearAt': t0, 'cam': [[t0, [960, 540, 1.0]], [t1, [1000, 530, 1.06]]],
     'items': [{'kind': 'prop', 'id': 'houseModern', 'x': 1280, 'y': 860, 's': 1.0, 'pop': False},
               {'kind': 'char', 'id': 'sam', 'x': 640, 'y': 860, 's': 0.95, 'move': [[t0, [300, 860]], [t0 + 1.4, [640, 860]]], 'walk': [t0, t0 + 1.4], 'pose': 'phone', 'expr': 'neutral', 'exprs': [[w('s14', 'standard'), 'happy']], 'pop': False},
               {'kind': 'sticker', 'text': '30-YEAR FIXED', 'x': 1280, 'y': 300, 'rot': 4, 'at': w('s14', 'standard'), 'bg': C['accent'], 'fg': '#FFFFFF', 'size': 64}]})
t0, t1 = t1, TOTAL
shot('Q-scoreboard', 'cutout', t0, t1, {'era': 'now', 'cam': [[t0, [960, 540, 1.0]], [t1, [960, 540, 1.03]]],
     'hud': [{'text': 'BEFORE 1934', 'x': 600, 'y': 250, 'rot': -2, 'at': t0, 'bg': '#9AA4B2', 'size': 56},
             {'text': 'TODAY', 'x': 1320, 'y': 250, 'rot': 2, 'at': t0 + 0.1, 'bg': C['accent'], 'fg': '#FFFFFF', 'size': 56},
             {'text': '5 years', 'x': 600, 'y': 450, 'at': t0 + 0.25, 'bg': C['paper'], 'size': 52},
             {'text': '30 years', 'x': 1320, 'y': 450, 'at': t0 + 0.35, 'bg': C['paper'], 'size': 52},
             {'text': 'interest only', 'x': 600, 'y': 610, 'at': t0 + 0.5, 'bg': C['paper'], 'size': 52},
             {'text': 'paid down monthly', 'x': 1320, 'y': 610, 'at': t0 + 0.6, 'bg': C['paper'], 'size': 52},
             {'text': 'all due at the end', 'x': 600, 'y': 770, 'at': t0 + 0.75, 'bg': C['neg'], 'fg': '#FFFFFF', 'size': 52},
             {'text': 'nothing left at the end', 'x': 1320, 'y': 770, 'at': t0 + 0.85, 'bg': C['pos'], 'size': 52}],
     'items': [{'kind': 'char', 'id': 'walt', 'x': 170, 'y': 960, 's': 0.7, 'expr': 'sad', 'pop': False}, {'kind': 'char', 'id': 'sam', 'x': 1760, 'y': 960, 's': 0.7, 'expr': 'happy', 'pop': False}]})


def localise(v, t0):
    """every time inside p is global → shot-local (keys [[t, v]], at/…At fields, walk spans)"""
    if isinstance(v, dict):
        o = {}
        for k, x in v.items():
            if k in ('at', 'yearAt', 'captionAt', 'from', 'to', 'out') and isinstance(x, (int, float)):
                o[k] = round(x - t0, 3)
            elif k == 'walk':
                o[k] = [round(x[0] - t0, 3), round(x[1] - t0, 3)]
            elif k in ('cam', 'move', 'rot', 'doors', 'poses', 'exprs') and isinstance(x, list):
                o[k] = [[round(a - t0, 3), localise(b, t0)] for a, b in x]
            else:
                o[k] = localise(x, t0)
        return o
    if isinstance(v, list):
        return [localise(x, t0) for x in v]
    return v


LOCAL_DATA_TPL = {'bars', 'bignum'}  # factory templates: their at-values are already shot-local
shots = []
for s in S:
    p = s['p'] if s['template'] in LOCAL_DATA_TPL else localise(s['p'], s['t0'])
    shots.append({**s, 'p': p})
claims = {
    'foreclosures_per_day': {'display': '≈1,000', 'value': 1000, 'historical': True,
                             'source': 'stlouisfed.org news release 2008-05-02 quoting D. Wheelock: "At its worst, in 1933, around 1,000 home loans were foreclosed every day."'},
    'lump_balloon': {'display': '$5,000', 'value': 5000, 'illustrative': True, 'source': 'code: interest-only 5-year loan, whole principal due at maturity'},
    'lump_amortized': {'display': '$0', 'value': 0, 'illustrative': True, 'source': 'code: fully amortizing loan, balance 0 at the last payment'},
}
tokens = {'color': {'bg': '#0E1116', 'surface': '#171B22', 'grid': '#2A303B', 'ink': '#F2F4F7', 'ink-muted': '#9AA4B2', 'accent': '#4C8DFF', 'warn': '#F2B441'}}
size = [1920, 1080] if RES == 1080 else [960, 540]
code = hashlib.sha256(b''.join(open(os.path.join(ROOT, f), 'rb').read() for f in ['rnd-hybrid/cutout/rig.js', 'rnd-hybrid/cutout/templates.js',
       'toolkit/factory/lib/engine.js', 'toolkit/factory/lib/templates.js', 'toolkit/factory/page.html', 'toolkit/factory/render.js'])).hexdigest()
segs = []
for s in shots:
    f0, f1 = round(s['t0'] * FPS), round(s['t1'] * FPS)
    local = {**s, 't0': 0.0, 't1': round((f1 - f0) / FPS, 4)}
    h = hashlib.sha256(json.dumps([local, RES, code, claims], sort_keys=True).encode()).hexdigest()[:16]
    segs.append({'id': s['id'], 'shot': s['id'], 'f0': 0, 'f1': f1 - f0, 'out': os.path.join(WORK, 'seg', f'{h}-{RES}.mp4'), 'local': local, 'g0': f0})
todo = [g for g in segs if not os.path.exists(g['out'])]
job = {'name': 'rnd-hybrid', 'orient': 'h', 'res': 1080 if RES == 1080 else 720, 'fps': FPS, 'fmt': 'jpeg', 'quality': 0.95,
       'encode': {'crf': 16, 'preset': 'fast'}, 'size': size, 'tokens': tokens, 'claims': claims, 'data': {}, 'floor': {'h': 40, 'v': 56},
       'counterweights': [], 'symbols': [{'id': 'cutout', 'url': '/rnd-hybrid/cutout/templates.js'}, {'id': 'archival', 'url': '/rnd-hybrid/cutout/templates.js'}],
       'shots': [g['local'] for g in todo], 'segments': [{k: g[k] for k in ('id', 'shot', 'f0', 'f1', 'out')} for g in todo]}
if RES != 1080:  # engine knows 1080 and 720 only; 540 = 720 render scaled at encode
    job['res'], job['size'] = 720, [1280, 720]
jp = os.path.join(WORK, 'job.json'); json.dump(job, open(jp, 'w'))
T = time.time()
if todo:
    env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
    r = subprocess.run(['node', os.path.join(ROOT, 'toolkit/factory/render.js'), jp, '--workers', str(WORKERS)], env=env, capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-4000:]); raise SystemExit('render failed')
render_s = round(time.time() - T, 1)
lst = os.path.join(WORK, 'seg', 'list.txt'); open(lst, 'w').write(''.join(f"file '{g['out']}'\n" for g in segs))
pic = os.path.join(WORK, f'picture-{RES}.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', pic], check=True)

# ---- audio: voice at OFF + paper sfx (sticker pops, cut swishes) + a quiet code-made bed; loudnorm −14 LUFS
SR = 48000; n = int(TOTAL * SR)
_, vo = wavfile.read(V['wav']); vo = vo.astype(np.float32) / 32768.0
voice = np.zeros(n, np.float32); a = int(OFF * SR); voice[a:a + len(vo)] = vo[:n - a]
rng = np.random.default_rng(1401); sfx = np.zeros(n, np.float32)
def put(t, x, g):
    i = int(t * SR); j = min(n, i + len(x)); sfx[i:j] += g * x[:j - i]
pop_t = []
for s in S:
    for it in (s['p'].get('items', []) + s['p'].get('hud', [])):
        if it.get('kind', 'sticker') == 'sticker' and 'text' in it: pop_t.append(it['at'])
        if it.get('stamp'): pop_t.append(it['stamp']['at'])
for t in pop_t:  # paper pop: short band-passed noise + a click
    L = int(0.09 * SR); env = np.exp(-np.linspace(0, 9, L)); x = rng.standard_normal(L) * env
    x = np.convolve(x, np.ones(6) / 6, 'same'); x += 0.6 * np.sin(2 * np.pi * 900 * np.arange(L) / SR) * np.exp(-np.linspace(0, 30, L)); put(t, x, 0.09)
for s in S[1:]:  # paper swish on each cut
    L = int(0.22 * SR); env = np.sin(np.linspace(0, np.pi, L)) ** 2; x = rng.standard_normal(L) * env
    x = np.convolve(x, np.ones(24) / 24, 'same'); put(max(0, s['t0'] - 0.12), x, 0.10)
tt = np.arange(n) / SR; bed = np.zeros(n, np.float32)  # two-chord pad, 1930s → today brighter after O
for k, (f, a0, a1) in enumerate([(110.0, 0, S[13]['t0']), (130.81, 0, S[13]['t0']), (164.81, 0, S[13]['t0']),
                                 (146.83, S[13]['t0'], TOTAL), (185.0, S[13]['t0'], TOTAL), (220.0, S[13]['t0'], TOTAL)]):
    m = (tt >= a0) & (tt < a1); bed[m] += np.sin(2 * np.pi * f * tt[m]) * 0.5 + 0.15 * np.sin(4 * np.pi * f * tt[m])
bed *= 0.012 * np.clip(tt / 1.0, 0, 1) * np.clip((TOTAL - tt) / 1.5, 0, 1)
mix = voice + sfx + bed
raw = os.path.join(WORK, 'mix-raw.wav'); wavfile.write(raw, SR, (np.clip(mix, -1, 1) * 32767).astype(np.int16))
out = os.path.join(WORK, f'clip-{RES}.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', pic, '-i', raw, '-filter:a', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], check=True)
durs = sorted(round(s['t1'] - s['t0'], 2) for s in S)
rep = {'res': RES, 'fps': FPS, 'total_s': TOTAL, 'shots': len(S), 'shot_durations': [round(s['t1'] - s['t0'], 2) for s in S],
       'median_shot_s': float(np.median(durs)), 'min_shot_s': durs[0], 'max_shot_s': durs[-1], 'render_s': render_s, 'rendered_segments': len(todo),
       'voice_chars': V['chars'], 'video': os.path.relpath(out, ROOT), 'sha256': hashlib.sha256(open(out, 'rb').read()).hexdigest(),
       'archival_slots': {s['p']['slot']: ('file' if os.path.exists(os.path.join(WORK, 'external', s['p']['slot'] + '.jpg')) else 'placeholder') for s in S if s['template'] == 'archival'}}
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
json.dump(rep, open(os.path.join(HERE, 'out', f'build-{RES}.json'), 'w'), indent=1); print(json.dumps(rep))

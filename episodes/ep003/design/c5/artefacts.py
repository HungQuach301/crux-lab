"""Tập 3 · C5: artefact hợp đồng (`checks/CONTRACT.md`) của bản cuối 1080p. Thay `animatic/artefacts.py` (C4); không đổi hình/tiếng, chỉ khai báo.
    python3 episodes/ep003/design/c5/artefacts.py            # khai báo (chạy được trước khi có video)
    python3 episodes/ep003/design/c5/artefacts.py --media    # + chép video cuối, stem (FLAC), tempo map, bản đồ căng (sau mux)
Ra (gốc tập): out/script.json, out/timeline.json, out/captions.srt (F09: dòng ≤ 42 ký tự, ≤ 2 dòng, cue 1–7 s, không chồng),
out/voice/takes.json, out/page.json (trang 1080p + window.CHECKS), out/camera.json (trang 2D: máy đứng yên), out/transitions.json,
out/cues.json, out/sfx-events.json, out/sonify-events.json, out/adbreaks.json, preprod/shotlist.json, out/rights.json, out/visual-assets.json,
contract.json (coverage, sonification, artefacts.M3, rights.generated)."""
import glob, json, os, re, shutil, subprocess, sys
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
A = f'{EP}/animatic'
sys.path.insert(0, f'{EP}/story')
import table_read as TR  # noqa: E402

J = lambda p: json.load(open(p))
def W(rel, o):
    p = f'{EP}/{rel}'; os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(o if isinstance(o, str) else json.dumps(o, indent=1, ensure_ascii=False))

tm = J(f'{A}/timing.json')
rows = {r['id']: r for r in TR.rows()}
TOTAL = float(int(-(-(tm['total'] + 15) // 1)))  # = ANIM.duration in scenes.js: ceil(total + 15)

# ---- script ----
sents = [{'id': s['id'], 'scene': s['scene'], 'text': s['text'], 'spoken': rows[s['id']]['tts'], 'start': s['start'], 'end': s['end']} for s in tm['sentences']]
W('out/script.json', {'sentences': sents})

# ---- timeline (acts and layouts as at C4) ----
ACT = {'S01': 'cold-open', 'S02': 'act1', 'S03': 'act1', 'S04': 'act2', 'S05': 'act2', 'S06': 'act2', 'S07': 'act3', 'S08': 'act3',
       'S09': 'method', 'S10': 'outro', 'S11': 'outro'}
LAY = {'S01': 'paths/dana', 'S02': 'card/bond', 'S03': 'paths/chain', 'S04': 'swarm/full', 'S05': 'swarm/eras', 'S06': 'dumbbell/eras',
       'S07': 'shadow/bars', 'S08': 'swarm/rate-scale', 'S09': 'card/method', 'S10': 'paths/dana', 'S11': 'card/end'}
scenes = []
for k, s in enumerate(tm['scenes']):
    end = tm['scenes'][k + 1]['start'] if k + 1 < len(tm['scenes']) else TOTAL
    scenes.append({'id': s['id'], 'act': ACT[s['id']], 'start': s['start'], 'dur': round(end - s['start'], 3), 'layout': LAY[s['id']],
                   'shot': 'wide', 'panels': [s['id']], 'chart': LAY[s['id']].split('/')[0], 'move': 0})
acts = []
for sc in scenes:
    if acts and acts[-1]['id'] == sc['act']:
        acts[-1]['end'] = round(sc['start'] + sc['dur'], 3)
    else:
        acts.append({'id': sc['act'], 'start': sc['start'], 'end': round(sc['start'] + sc['dur'], 3)})
W('out/timeline.json', {'fps': 30, 'total': TOTAL, 'acts': acts, 'scenes': scenes, 'turns': [{'t': s['start'], 'what': s['id']} for s in scenes[1:]]})

# ---- captions (F09): each sentence wrapped at ≤ 42 chars per line, ≤ 2 lines per cue, cue time ∝ characters inside the sentence's
# ASR span; cues shorter than 1 s take the gap to the next sentence, else merge with a neighbour; none longer than 7 s; no overlap ----
MAXL, MINC, MAXC = 42, 1.0, 7.0
def wrap(s):
    out, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > MAXL:
            out.append(cur); cur = w
        else:
            cur = f'{cur} {w}' if cur else w
    return out + ([cur] if cur else [])
def lines2(txt):  # balanced split of a cue text into ≤ 2 lines of ≤ 42 chars (None if impossible)
    if len(txt) <= MAXL: return [txt]
    ws = txt.split(); best = None
    for i in range(1, len(ws)):
        a, b = ' '.join(ws[:i]), ' '.join(ws[i:])
        if len(a) <= MAXL and len(b) <= MAXL and (best is None or abs(len(a) - len(b)) < abs(len(best[0]) - len(best[1]))): best = (a, b)
    return list(best) if best else None
cues = []
for s in sents:
    ls = wrap(s['text']); n = sum(len(x) for x in ls); dur = s['end'] - s['start']
    groups, i = [], 0
    while i < len(ls):  # two lines per cue while that cue stays ≤ 7 s
        if i + 1 < len(ls) and (len(ls[i]) + len(ls[i + 1])) / n * dur <= MAXC: groups.append(ls[i] + ' ' + ls[i + 1]); i += 2
        else: groups.append(ls[i]); i += 1
    t = s['start']
    for g in groups:
        d = (len(g) - g.count(' ') * 0 ) / max(1, sum(len(x) for x in groups)) * dur
        cues.append({'text': g, 't0': t, 't1': t + d, 'sid': s['id']}); t += d
for k, c in enumerate(cues):  # short cue: extend into the silence before the next cue
    nxt = cues[k + 1]['t0'] if k + 1 < len(cues) else TOTAL
    if c['t1'] - c['t0'] < MINC: c['t1'] = min(nxt, c['t0'] + MINC)
k = 0
while k < len(cues):  # still short: merge with the next (or previous) cue when the merged text fits 2 lines and 7 s
    c = cues[k]
    if c['t1'] - c['t0'] >= MINC - 1e-6: k += 1; continue
    for j in ([k + 1] if k + 1 < len(cues) else []) + ([k - 1] if k else []):
        a, b = (c, cues[j]) if j > k else (cues[j], c)
        txt = a['text'] + ' ' + b['text']
        if lines2(txt) and b['t1'] - a['t0'] <= MAXC:
            m = {'text': txt, 't0': a['t0'], 't1': b['t1'], 'sid': a['sid']}
            lo = min(j, k); cues[lo:lo + 2] = [m]; k = max(0, lo - 1); break
    else:
        k += 1
def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{int(h):02d}:{int(m):02d}:{s:06.3f}'.replace('.', ',')
with open(f'{EP}/out/captions.srt', 'w') as f:
    for i, c in enumerate(cues, 1):
        f.write(f"{i}\n{ts(c['t0'])} --> {ts(c['t1'])}\n" + '\n'.join(lines2(c['text']) or wrap(c['text'])) + '\n\n')
bad = [c for c in cues if not lines2(c['text']) or not (MINC - 1e-6 <= c['t1'] - c['t0'] <= MAXC + 1e-6)]
assert ' '.join(c['text'] for c in cues).split() == ' '.join(s['text'] for s in sents).split()

# ---- voice takes ----
rep = J(f'{A}/voice-report.json')
takes = [{'id': sc, 'raw': v.get('use') or v.get('take'), 'final': f'animatic/work/voice/{sc}.wav', 'model': TR.MODEL, 'voiceId': TR.VOICE, 'provider': 'elevenlabs'} for sc, v in rep['scenes'].items()]
W('out/voice/takes.json', {'takes': takes, 'voice': {'provider': 'elevenlabs', 'voiceId': TR.VOICE, 'model': TR.MODEL}})
W('out/page.json', {'url': 'http://127.0.0.1:8765/episodes/ep003/design/c3/page.html?k=ANIM&r=anim&res=1080', 'ready': 'window.READY'})

# ---- shots and cuts: the ANIM plan of design/c3/src/scenes.js (first shot of a scene starts at the scene start; later shots at their sentence) ----
start = {s['id']: s['start'] for s in tm['sentences']}
SHOTS = [('S01', 'S01.1', 'KEY1'), ('S01', 'S01.6', 'KEY2'), ('S02', 'S02.1', 'TITLE'), ('S02', 'S02.2', 'BOND'), ('S03', 'S03.1', 'KEY3'),
         ('S04', 'S04.1', 'KEY4'), ('S05', 'S05.5', 'KEY5'), ('S06', 'S06.1', 'ERAS'), ('S07', 'S07.1', 'KEY6'), ('S08', 'S08.1', 'KEY7'),
         ('S09', 'S09.1', 'METHOD'), ('S10', 'S10.1', 'KEY1'), ('S11', 'S11.1', 'END')]
sc0 = {s['id']: s['start'] for s in tm['scenes']}
first = {}
shot_t = []
for sc, sid, name in SHOTS:
    t = sc0[sc] if sc not in first else start[sid]
    first.setdefault(sc, t); shot_t.append((round(t, 3), sc, sid, name))
WHY = {'KEY2': 'the what-if rule needs its own timeline before any historical number', 'TITLE': 'title card opens the promise of the episode',
       'BOND': "the bond's rule is explained on its own bar and gate", 'KEY3': "the bill chain answers the bond's single promise",
       'KEY4': 'the replay starts: every start month drops in as one dot', 'KEY5': 'the 17 real-guarantee months are shown apart from the what-ifs',
       'ERAS': 'why eras differ: first-month rate against the 20-year average', 'KEY6': 'buying power: the doubled dollars against prices',
       'KEY7': 'the steady-rate line the roll must clear', 'METHOD': 'method card: what the replay leaves out',
       'END': 'end screen after the last line'}
cuts = []
for k in range(1, len(shot_t)):
    t, sc, sid, name = shot_t[k]
    prev = shot_t[k - 1][3]
    sem = name == 'KEY1' and prev != 'KEY1'
    cuts.append({'t': t, 'from': prev, 'to': name, 'type': 'cut', 'match': 'semantic' if sem else None, 'audio': None,
                 'reason': "back to Dana's two paths: the opening question returns for its answer" if sem else WHY[name]})
W('out/transitions.json', {'cuts': cuts})
W('preprod/shotlist.json', {'_about': 'C5: the shots of the ANIM plan (design/c3/src/scenes.js PLAN); 2D page, no camera move',
                            'shots': [{'id': f'{sc}-{name}', 'scene': sc, 'size': 'wide', 'move': 'none', 'moveReason': '2D chart page: the data moves, the frame stays still'} for _, sc, _, name in shot_t]})
W('out/camera.json', {'_about': '2D page without a camera: the frame is the whole page at every frame', 'frames': [{'t': round(i / 30, 4), 'x': 960, 'y': 540, 'zoom': 1} for i in range(int(TOTAL * 30))]})
W('out/sfx-events.json', {'events': [], '_about': 'no sound effects in this episode (sfx stem silent)'})
W('out/sonify-events.json', {'fps': 30, 'bar': [], 'line': [], 'dot': [], '_about': 'no data sonification in this episode (C3: style C music only; sonify stem silent)'})
W('out/adbreaks.json', {'breaks': [], '_about': 'no mid-roll breaks declared (a monetisation choice is the owner\'s, C6)'})
mr = J(f'{A}/mix-report.json')
f_start = sc0['S08']
W('out/cues.json', {'cues': [{'t': 0.0, 'end': round(f_start, 3), 'function': 'bed under the question and the replay', 'key': 'D dorian', 'tempo': 114, 'layer': 'music'},
                             {'t': round(f_start, 3), 'end': TOTAL, 'function': 'bed under the line to clear and the close', 'key': 'F major', 'tempo': 114, 'layer': 'music'}],
                    'silences': []})

# ---- description (F10): chapters m:ss from the scene starts ----
def mss(t): return f'{int(t // 60)}:{int(t % 60):02d}'
desc = re.sub(r'\{scene:(S\d\d)\}', lambda m: mss(sc0[m.group(1)]), open(f'{EP}/design/c5/description.md').read())
W('out/package/description.md', desc)

# ---- rights (F12) and visual assets (K3.1) ----
W('out/visual-assets.json', {'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter', 'paths': ['../../toolkit/render/fonts/inter-latin-*.woff2']}],
                             'generated': [{'glob': 'design/c3/work/data.js', 'generator': 'design/c3/build_data.py'}]})
EL_Q = ('(ii) if you access or use our Services through a paid subscription plan (such a user, a " Paid User "), you may use the Services for commercial purposes, '
        'but in either case, your access and use of the Services and any Output must still comply with the Prohibited Use Policy.')
OFL_Q = ('Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, '
         'redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions')
W('out/rights.json', {'assets': [
    {'name': 'voice: Eric (ElevenLabs premade, eleven_v3)', 'stems': ['voice'], 'visuals': [], 'kind': 'tts', 'origin': 'ElevenLabs text-to-speech (RIGHTS.md V-ERIC)',
     'licence': 'ElevenLabs Terms of Service, paid Creator plan', 'thirdParty': True, 'commercial': True, 'terms': {'quote': EL_Q, 'url': 'https://elevenlabs.io/terms-of-use'}},
    {'name': 'music and silent effect layers (style C, generated by code)', 'stems': ['music', 'sfx', 'whoosh', 'room', 'sonify'], 'visuals': [], 'kind': 'music',
     'origin': 'project code, no third-party samples (RIGHTS.md A-MUSIC)', 'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'audio_src/mix_full.py'},
    {'name': 'Inter typeface', 'stems': [], 'visuals': ['Inter'], 'kind': 'font', 'origin': '@fontsource/inter 5.3.0 (RIGHTS.md F-INTER)', 'licence': 'SIL Open Font License 1.1',
     'thirdParty': True, 'commercial': True, 'terms': {'quote': OFL_Q, 'url': 'https://unpkg.com/@fontsource/inter@5.3.0/LICENSE'}},
    {'name': 'charts and figures drawn by code', 'stems': [], 'visuals': [], 'kind': 'image', 'origin': 'design/c3/src (canvas 2D, no image files)', 'licence': 'own work',
     'thirdParty': False, 'commercial': True, 'generator': 'design/c3/src/scenes.js'}]})

# ---- contract fields ----
c = J(f'{EP}/contract.json')
model = J(f'{EP}/out/model.json')
c['coverage'] = [{'attribute': 'case', 'act': 'act2', 'values': [w['start'][:7] for w in model['windows']],
                  '_about': 'every start month of the replay (Jan 1934 to Sep 2006) is a dot of the KEY-4 swarm (S04-S05), the ones that missed double included'}]
c['sonification'] = {'stem': 'sonify', 'bandsHz': [[1500, 8000]], '_about': 'no data sonification in this episode (C3, style C music only): the sonify stem is silent'}
c['artefacts'] = {'M3': ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/timeline.json', 'out/script.json', 'out/claims.json',
                         'out/audio/stems/voice.flac', 'out/audio/stems/music.flac', 'out/audio/stems/sfx.flac', 'out/audio/stems/whoosh.flac', 'out/audio/stems/room.flac',
                         'out/audio/stems/sonify.flac', 'out/voice/takes.json', 'out/camera.json', 'out/sfx-events.json', 'out/sonify-events.json', 'out/tempo-map.json',
                         'out/transitions.json', 'out/cues.json', 'out/tension-map.json', 'out/tension-map.png', 'out/adbreaks.json', 'preprod/shotlist.json',
                         'design/tokens.json', 'out/package/thumb-1.png', 'out/package/thumb-2.png', 'out/package/thumb-3.png', 'out/page.json',
                         'out/rights.json', 'out/visual-assets.json']}
c.pop('todo', None)
W('contract.json', c)

if '--media' in sys.argv:
    os.makedirs(f'{EP}/out/audio/stems', exist_ok=True)
    shutil.copyfile(f'{EP}/work/c5/video.mp4', f'{EP}/out/video.mp4')
    for f in glob.glob(f'{A}/work/stems/*.wav'):
        n = os.path.basename(f)[:-4]
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', f, '-c:a', 'flac', f'{EP}/out/audio/stems/{n}.flac'], check=True)
    shutil.copyfile(f'{A}/work/tempo-map.json', f'{EP}/out/tempo-map.json')
    subprocess.run([sys.executable, f'{ROOT}/toolkit/audio/d_tension.py', EP], check=True)
print(len(sents), 'sentences;', len(cues), 'cues (bad', len(bad), ');', len(cuts), 'cuts; total', TOTAL)

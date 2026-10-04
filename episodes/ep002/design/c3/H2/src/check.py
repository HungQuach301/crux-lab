#!/usr/bin/env python3
"""H2 self-check summary from the render logs: every number token on screen is in a claim `display`
(episodes/ep002/out/claims.json); smallest text; D4 distances; D2 contrast. python3 src/check.py"""
import json, os, re
H2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = os.path.abspath(os.path.join(H2, '../../..'))
disp = {c['claimId']: c['display'] for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims']}
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
toks = {}
for k, d in disp.items():
    for t in NUM.findall(d): toks.setdefault(t, []).append(k)
rows = []
for F in ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7']:
    L = json.load(open(os.path.join(H2, f'render-log-{F}.json')))
    bad = [(e['s'], t) for e in L['texts'] for t in NUM.findall(e['s']) if t not in toks]
    cv = L['selfCheck']; S = L['summary']
    rows.append({'F': F, 'claims': L['claimsUsed'], 'strings': [e['s'] for e in L['texts']], 'numbersNotInClaims': bad,
                 'minFontPx1080': S['minFontPx1080'], 'minFontPx720': round(S['minFontPx1080'] * 2 / 3, 1),
                 'minDistTextGraphic720': S['minDistTextToGraphicPx720'], 'minDistTextText720': S['minDistTextToTextPx720'],
                 'minContrast': S['minContrast'], 'outOfSafe': S['outOfSafe'], 'filmSec': L['filmSeconds'], 'wallSec': L['wallSeconds'],
                 'secPerFilmSec': L['machineSecPerFilmSec']})
th = json.load(open(os.path.join(H2, 'thumb-concept.json')))
for r in rows: print(json.dumps(r, ensure_ascii=False))
print('thumb', json.dumps([(t['text'], t['fontPx']) for t in th['texts']]), json.dumps(th['selfCheck']))

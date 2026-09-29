#!/usr/bin/env python3
"""C4 animatic / C5 final-picture self-checks, from the render logs (C5: <ep>/work/c5/logs/Sxx.json, 1920x1080 render):
  1. every number token of every on-screen string is in a claim `display` (out/claims.json); claim IDs listed;
  2. no string left the safe area (engine rectangle, and C5: the checker's V03 rectangle 96..1824 x 54..1026, `outV03`); 3. smallest text >= 40 px at 1080p (owner's floor, C3 signature);
  4. every anchor declared for the scene in anchors.json was used by the scene, and every keyword was found;
  5. writes <ep>/work/c5/25/Sxx.png: the scene's hardest frame (most text) box-downscaled 1920x1080 -> 480x270 (25%),
     and work/c5/25/sheet-N.png contact sheets at native 480x270 for the read-back.
   python3 check.py [S01 ...]  -> ../check-report.json"""
import json, os, re, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); EP = os.path.dirname(AN); WK = os.path.join(EP, 'work', 'c5')
claims = json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']
NUM = re.compile(r'\d+(?:,\d{3})*(?:\.\d+)?')
tok = {}
for c in claims:
    for x in NUM.findall(c['display']):
        tok.setdefault(x, []).append(c['claimId'])
anch = json.load(open(os.path.join(AN, 'anchors.json')))['anchors']
scenes = sys.argv[1:] or [f'S{i:02d}' for i in range(1, 21)]
rep, ok = {}, True
os.makedirs(os.path.join(WK, '25'), exist_ok=True)
for S in scenes:
    lp = os.path.join(WK, 'logs', S + '.json')
    if not os.path.exists(lp):
        rep[S] = {'missing': True}; ok = False; continue
    lg = json.load(open(lp))
    bad = [(e['s'], x) for e in lg['texts'] for x in NUM.findall(e['s']) if x not in tok]
    out = [e['s'] for e in lg['texts'] if e['out'] or e.get('outV03')]
    minpx = min(e['px'] for e in lg['texts'])
    declared = [a['id'] for a in anch if a['scene'] == S]
    unused = sorted(set(declared) - set(lg['anchorsUsed']))
    im = Image.open(os.path.join(WK, 'hard', S + '-hard.png')).convert('RGB').resize((480, 270), Image.BOX)
    im.save(os.path.join(WK, '25', S + '.png'))
    rep[S] = {'claimsUsed': lg['claimsUsed'], 'strings': len(lg['texts']), 'sentenceCaptions': [e['s'] for e in lg['texts'] if e.get('sent')],
              'numbersNotInClaims': bad, 'outOfSafeArea': out, 'minTextPx1080': minpx, 'minCapPxAt25pct': round(minpx * 0.727 / 4, 1),
              'anchorsDeclared': len(declared), 'anchorsUnused': unused, 'keywordsMissing': lg['anchorsKeywordMissing'],
              'size': lg.get('size'), 'frames': lg['frames'], 'frames3d': lg['frames3d'], 'wallSeconds': lg['wallSeconds'], 'machineSecPerFilmSec': lg['machineSecPerFilmSec'], 'hardTime': lg['hardTime']}
    ok &= not bad and not out and minpx >= 40 and not unused and not lg['anchorsKeywordMissing']
    print(S, 'numbers-outside-claims', bad, 'out', out, 'minpx', minpx, 'unused anchors', unused)
# contact sheets, 4 per sheet (2x2 of native 480x270)
ims = [(S, os.path.join(WK, '25', S + '.png')) for S in scenes if os.path.exists(os.path.join(WK, '25', S + '.png'))]
for k in range(0, len(ims), 4):
    sh = Image.new('RGB', (960, 540), 'black')
    for j, (S, f) in enumerate(ims[k:k + 4]):
        sh.paste(Image.open(f), ((j % 2) * 480, (j // 2) * 270))
    sh.save(os.path.join(WK, '25', f'sheet-{k // 4 + 1}.png'))
json.dump(rep, open(os.path.join(AN, 'check-report.json'), 'w'), indent=1, ensure_ascii=False)
print('ALL OK' if ok else 'ISSUES')

#!/usr/bin/env python3
"""C3 final self-checks (run after render.js):
  1. every number token in every on-screen string appears in a claim `display` of out/claims.json (claim IDs listed);
  2. no on-screen string left the safe area (render.js flags texts whose box leaves [40, W-40] x [36, H-18]);
  3. smallest text tier >= 48 px (cap height 0.727 x 48 = 34.9 px at 1080p);
  4. writes work/<F>-25.png: the hardest frame (poster = last frame unless the scene says otherwise) box-downscaled 4x
     to 480x270 (what a phone shows at 25%), plus a 2x nearest-neighbour enlargement for viewing, for the human/AI read.
   python3 check.py SF1 SF2 ...
"""
import json, os, re, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIN = os.path.dirname(HERE)
EP = os.path.normpath(os.path.join(FIN, '..', '..', '..'))
claims = json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']
displays = {c['claimId']: c['display'] for c in claims}
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
all_tokens = {}
for cid, d in displays.items():
    for tok in NUM.findall(d):
        all_tokens.setdefault(tok, []).append(cid)

ok = True
report = {}
for F in sys.argv[1:]:
    log = json.load(open(os.path.join(FIN, f'render-log-{F}.json')))
    bad_nums, out, small = [], [], []
    for e in log['texts']:
        for tok in NUM.findall(e['s']):
            if tok not in all_tokens:
                bad_nums.append((e['s'], tok))
        if e['out']:
            out.append(e['s'])
        if e['px'] < 48:
            small.append(e['s'])
    im = Image.open(os.path.join(FIN, 'work', f'{F}-hard.png')).convert('RGB')
    q = im.reduce(4)  # box average 4x4 -> 480x270
    q.save(os.path.join(FIN, 'work', f'{F}-25.png'))
    q.resize((960, 540), Image.NEAREST).save(os.path.join(FIN, 'work', f'{F}-25-x2.png'))
    minpx = min(e['px'] for e in log['texts'])
    report[F] = {'claimsUsed': log['claimsUsed'], 'strings': len(log['texts']), 'numbersNotInClaims': bad_nums,
                 'outOfSafeArea': out, 'minTextPx': minpx, 'minCapPx1080': round(minpx * 0.727, 1),
                 'minCapPxAt25pct': round(minpx * 0.727 / 4, 1)}
    ok &= not bad_nums and not out and not small
    print(F, json.dumps(report[F], ensure_ascii=False))
json.dump(report, open(os.path.join(FIN, 'work', 'check-report.json'), 'w'), indent=1, ensure_ascii=False)
sys.exit(0 if ok else 1)

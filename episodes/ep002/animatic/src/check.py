#!/usr/bin/env python3
"""Tập 2 · C4 animatic machine checks (pattern: episodes/ep001/animatic/src/check.py), from the render logs work/logs/Sxx.json:
  1. claim IDs used per scene; every number token of every on-screen string is in a claim `display` (out/claims.json): 0 outside;
  2. 0 strings outside the safe area (tokens.json canvas.safe: x 96, top 64, bottom 40 px @1080);
  3. smallest text >= 40 px @1080 (G-014); 4. text contrast >= 4.5:1; 5. text -> graphic clearance >= 4 px @720
     (self-check on every 6th frame + every strip frame); 6. ILLUSTRATIVE badge present whenever a Leah-only number is on screen;
  7. anchors declared in anchors.json for the scene == anchors used by the scene; keywords not found (0 expected).
  Also: the S11 method card (words, reveal, time fully on screen vs >= 1 s per 3 words) and the 25% read-back images:
  work/25/Sxx.png = the scene's frame with the most text, box-downscaled 1280x720 -> 480x270 (= 1920x1080 at 25%);
  strips/S11-card-25pct.png = the full method card at 480x270.
   python3 src/check.py  -> animatic/check-report.json"""
import json, os, re, subprocess
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); EP = os.path.dirname(AN); WK = os.path.join(AN, 'work')
claims = json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']
NUM = re.compile(r'\d+(?:,\d{3})*(?:\.\d+)?')
tok = {}
for c in claims:
    for x in NUM.findall(c['display']): tok.setdefault(x, []).append(c['claimId'])
anch = json.load(open(os.path.join(AN, 'anchors.json')))['anchors']
tm = json.load(open(os.path.join(AN, 'timing.json')))
scenes = [s['id'] for s in tm['scenes']]
os.makedirs(os.path.join(WK, '25'), exist_ok=True)
rep, ok, tot = {}, True, {'numbersNotInClaims': 0, 'outOfSafeArea': 0, 'minTextPx1080': 999, 'minContrast': 99, 'minTextToGraphicPx720': 99, 'badgeMissingFrames': 0, 'anchorsUnused': 0, 'keywordsMissing': 0, 'wallSeconds': 0, 'filmSeconds': 0}
for S in scenes:
    lp = os.path.join(WK, 'logs', S + '.json')
    if not os.path.exists(lp): rep[S] = {'missing': True}; ok = False; continue
    lg = json.load(open(lp))
    bad = [(e['s'], x) for e in lg['texts'] for x in NUM.findall(e['s']) if x not in tok]
    nums = sorted({x for e in lg['texts'] for x in NUM.findall(e['s'])})
    out = [e['s'] for e in lg['texts'] if e['out']]
    sm = lg['summary']
    if sm['minFontPx1080'] is None: sm['minFontPx1080'] = 999   # no text in the scene
    declared = [a['id'] for a in anch if a['scene'] == S]
    unused = sorted(set(declared) - set(lg['anchorsUsed']))
    kwmiss = sorted(set(lg['anchorsKeywordMissing']) | {a['id'] for a in anch if a['scene'] == S and not a['keyword_found']})
    lowC = sorted({x['s'] for x in lg['selfCheck'] if x['contrastMin'] < 4.5})
    near = sorted({x['s'] for x in lg['selfCheck'] if x['dGraphicMin'] < 4})
    Image.open(os.path.join(WK, 'hard', S + '.png')).convert('RGB').resize((480, 270), Image.BOX).save(os.path.join(WK, '25', S + '.png'))
    rep[S] = {'dur': next(s['dur'] for s in tm['scenes'] if s['id'] == S), 'claimsUsed': lg['claimsUsed'], 'strings': len(lg['texts']), 'numberTokens': nums,
              'numbersNotInClaims': bad, 'outOfSafeArea': out, 'minTextPx1080': sm['minFontPx1080'], 'minCapPxAt25pct': round(sm['minFontPx1080'] * 0.727 / 4, 1) if sm['minFontPx1080'] < 999 else None,
              'minContrast': sm['minContrast'], 'lowContrast': lowC, 'minTextToGraphicPx720': sm['minDistTextToGraphicPx720'], 'textCloserThan4px': near,
              'minTextToTextPx720': sm['minDistTextToTextPx720'], 'badgeMissingFrames': sm['badgeMissing'], 'badgeMissingAt': lg.get('badgeMissing', []),
              'anchorsDeclared': len(declared), 'anchorsUsed': len(lg['anchorsUsed']), 'anchorsUnused': unused, 'keywordsMissing': kwmiss,
              'frames': lg['frames'], 'checkFrames': lg['checkFrames'], 'wallSeconds': lg['wallSeconds'], 'machineSecPerFilmSec': lg['machineSecPerFilmSec'], 'hardTime': lg['hardTime']}
    tot['numbersNotInClaims'] += len(bad); tot['outOfSafeArea'] += len(out); tot['minTextPx1080'] = min(tot['minTextPx1080'], sm['minFontPx1080'])
    tot['minContrast'] = min(tot['minContrast'], sm['minContrast']); tot['minTextToGraphicPx720'] = min(tot['minTextToGraphicPx720'], sm['minDistTextToGraphicPx720'])
    tot['badgeMissingFrames'] += sm['badgeMissing']; tot['anchorsUnused'] += len(unused); tot['keywordsMissing'] += len(kwmiss)
    tot['wallSeconds'] += lg['wallSeconds']; tot['filmSeconds'] += lg['filmSeconds']
    ok &= not bad and not out and sm['minFontPx1080'] >= 40 and not unused and not kwmiss and sm['minContrast'] >= 4.5 and sm['minDistTextToGraphicPx720'] >= 4 and not sm['badgeMissing']
    print(S, 'nums-outside', bad, 'out', out, 'minpx', sm['minFontPx1080'], 'contrast', sm['minContrast'], lowC, 'dGraphic', sm['minDistTextToGraphicPx720'], near, 'badge-missing', sm['badgeMissing'], 'unused', unused, 'kw', kwmiss)
# method card
card = json.load(open(os.path.join(HERE, 'method_card.json')))
WRD = lambda s: len([w for w in s.split() if re.search(r'[A-Za-z0-9]', w)])
words = WRD(''.join(p[0] for p in card['title'])) + sum(WRD(l['text']) for l in card['lines'])
s11 = next(s for s in tm['scenes'] if s['id'] == 'S11'); a11 = next(a for a in anch if a['id'] == 'card' and a['scene'] == 'S11')
full_at = a11['local_s'] + 0.3 + 0.3 * len(card['lines']) + 0.3          # last line fully in (s11.js: 0.3 s apart, 0.3 s fade)
shown = round(s11['dur'] - full_at, 2)
cardpng = os.path.join(WK, 'stills', 'S11-own-6.png')
if os.path.exists(cardpng): Image.open(cardpng).convert('RGB').resize((480, 270), Image.BOX).save(os.path.join(AN, 'strips', 'S11-card-25pct.png'))
mc = {'words': words, 'requiredSeconds': round(words / 3, 2), 'fullyShownSeconds': shown, 'sceneSeconds': s11['dur'], 'narrationSeconds': next(x['end'] - x['start'] for x in s11['sentences']),
      'pass': shown >= words / 3, 'textTierPx1080': {'title': 72, 'lines': 64}, 'capHeightPxAt25pct': {'title': round(72 * 0.727 / 4, 1), 'lines': round(64 * 0.727 / 4, 1)},
      'image25pct': 'strips/S11-card-25pct.png'}
ok &= mc['pass']
tot['filmSeconds'] = round(tot['filmSeconds'], 2); tot['wallSeconds'] = round(tot['wallSeconds'], 1)
report = {'_about': 'C4 animatic machine checks (src/check.py over work/logs). Px: font sizes at 1080p; distances at 720p. Self-check on every 6th frame and every strip frame.',
          'allOk': bool(ok), 'totals': tot, 'methodCard': mc, 'scenes': rep}
json.dump(report, open(os.path.join(AN, 'check-report.json'), 'w'), indent=1, ensure_ascii=False)
# 25% contact sheets (2x2 of native 480x270)
ims = [os.path.join(WK, '25', S + '.png') for S in scenes if os.path.exists(os.path.join(WK, '25', S + '.png'))]
for k in range(0, len(ims), 4):
    sh = Image.new('RGB', (960, 540), 'black')
    for j, f in enumerate(ims[k:k + 4]): sh.paste(Image.open(f), ((j % 2) * 480, (j // 2) * 270))
    sh.save(os.path.join(WK, '25', f'sheet-{k // 4 + 1}.png'))
print('method card', mc)
print('ALL OK' if ok else 'ISSUES', tot)

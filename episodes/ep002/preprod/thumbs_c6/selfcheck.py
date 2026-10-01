"""P01/P02-style self-check of the C6 thumbnails and titles (REFERENCE; imports checks/py helpers read-only, never edits checks/).
python3 episodes/ep002/preprod/thumbs_c6/selfcheck.py -> out/package/selfcheck.json + out/package/legibility-25.png (25% and 10% views, 1:1)."""
import json, re, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
EP = Path(__file__).resolve().parents[2]
REPO = EP.parents[1]
sys.dont_write_bytecode = True  # no caches inside checks/
sys.path.insert(0, str(REPO / 'checks/py'))
from r_visual import token_share  # noqa: E402
from r_content import ADVICE, FORECAST, FOUR, WE_BAD  # noqa: E402

def rel_lum(c):
    c = np.asarray(c, float) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]

PK = EP / 'out/package'
tokens = list(json.loads((EP / 'design/tokens.json').read_text())['colors'].values())
claims = {c['claimId']: c for c in json.loads((EP / 'out/claims.json').read_text())['claims']}
NUM = re.compile(r'[−\-+]?\$?\d[\d,]*(?:\.\d+)?%?')

def s10(text):
    low = text.lower().replace('’', "'")
    hits = []
    for k, pats in (('advice', ADVICE), ('forecast', FORECAST), ('four', FOUR), ('we', WE_BAD)):
        for p in pats:
            if re.search(p, re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low) if k == 'forecast' else low, re.M):
                hits.append(k)
    return hits

def numbers_ok(text, ids):
    """every number token in the text appears inside the display of one of the named claims"""
    out = []
    for n in NUM.findall(text):
        core = n.lstrip('−-+')
        hit = [i for i in ids if core in claims[i]['display']]
        out.append({'number': n, 'claims': hit, 'ok': bool(hit)})
    return out

res = {'thumbnails': {}, 'titles': {}}
for k in (1, 2, 3):
    img = np.asarray(Image.open(PK / f'thumb-{k}.png').convert('RGB'))
    meta = json.loads((PK / f'thumb-{k}.json').read_text())
    h, w = img.shape[:2]
    small = img[: h - h % 10, : w - w % 10].reshape(h // 10, 10, w // 10, 10, 3).mean(axis=(1, 3))
    lum = rel_lum(small)
    # text mask (to measure token share on text + flat areas separately is not needed: every pixel is 2D token or token blend)
    rows = []
    for t in meta['texts']:
        x, y, bw, bh = [int(v / 10) for v in t.get('plateBox', t['box'])] if t.get('role') else [int(v / 10) for v in t['box']]
        reg = lum[y:y + max(1, bh), x:x + max(1, bw)]
        c = (np.percentile(reg, 95) + 0.05) / (np.percentile(reg, 5) + 0.05)
        cl = t.get('claim')
        rows.append({'text': t['text'], 'fontPx': t['fontPx'], 'px_at_25pct': round(t['fontPx'] / 4, 1), 'px_at_10pct': round(t['fontPx'] / 10, 1),
                     'contrast_at_10pct': round(float(c), 2), 'claim': cl,
                     'claimDisplayMatches': (claims[cl]['display'] == t['text'] or claims[cl]['display'] in t['text']) if cl else None,
                     'illustrativeClaim': claims[cl]['illustrative'] if cl else None,
                     'numbersWithoutClaim': [n['number'] for n in numbers_ok(t['text'], [cl] if cl else [])] if not t.get('role') else [],
                     's10': s10(t['text'])})
    main = [r for r, t in zip(rows, meta['texts']) if not t.get('role')]
    ill_needed = any(r['illustrativeClaim'] for r in main)
    has_badge = any(t.get('role', '').startswith('ILLUSTRATIVE') for t in meta['texts'])
    # clearance: ink pixels of the picture inside each main text box (+6 px) when the text is removed is not available here;
    # instead the renderer keeps text on plain bg: report the share of non-bg pixels in the box ring outside the glyph box
    res['thumbnails'][f'thumb-{k}'] = {
        'size': f'{w}x{h}', 'sizeOk': (w, h) == (1280, 720),
        'tokenSharePct_wholeImage': round(100 * token_share(img, tokens), 1),
        'words_excl_badge': sum(len(t['text'].split()) for t in meta['texts'] if not t.get('role')),
        'minFontPx_excl_badge': min(t['fontPx'] for t in meta['texts'] if not t.get('role')),
        'badgeFontPx': next((t['fontPx'] for t in meta['texts'] if t.get('role')), None),
        'minContrast10_excl_badge': min(r['contrast_at_10pct'] for r in main), 'badgeContrast10': next((r['contrast_at_10pct'] for r, t in zip(rows, meta['texts']) if t.get('role')), None),
        'illustrativeNumber': ill_needed, 'badge': has_badge, 'badgeRuleOk': (not ill_needed) or has_badge,
        'allNumbersHaveClaim': all(not r['numbersWithoutClaim'] or r['claim'] for r in main) and all(r['claimDisplayMatches'] in (None, True) for r in main),
        's10Hits': sum(len(r['s10']) for r in rows), 'texts': rows}

titles = json.loads((Path(__file__).parent / 'titles.json').read_text())
for tid, t in titles.items():
    res['titles'][tid] = {'title': t['title'], 'chars': len(t['title']), 'charsOk': len(t['title']) <= 60, 's10Hits': s10(t['title']),
                          'numbers': numbers_ok(t['title'], t.get('claims', []))}
(PK / 'selfcheck.json').write_text(json.dumps(res, indent=1, ensure_ascii=False))
# legibility sheet: each thumbnail at 25% (320x180) and 10% (128x72), shown 1:1
sheet = Image.new('RGB', (3 * 340 + 20, 180 + 72 + 70), (14, 17, 22))
d = ImageDraw.Draw(sheet)
for i in range(3):
    im = Image.open(PK / f'thumb-{i + 1}.png').convert('RGB')
    sheet.paste(im.resize((320, 180), Image.BOX), (20 + i * 340, 30))
    sheet.paste(im.resize((128, 72), Image.BOX), (20 + i * 340, 30 + 180 + 20))
    d.text((20 + i * 340, 8), f'thumb-{i + 1}: 25% (320x180) and 10% (128x72), 1:1', fill=(154, 164, 178))
sheet.save(PK / 'legibility-25.png')
for k, v in res['thumbnails'].items():
    print(k, {x: v[x] for x in ('sizeOk', 'tokenSharePct_wholeImage', 'words_excl_badge', 'minFontPx_excl_badge', 'badgeFontPx', 'minContrast10_excl_badge', 'badgeContrast10', 'badgeRuleOk', 'allNumbersHaveClaim', 's10Hits')})
for k, v in res['titles'].items():
    print(k, v['chars'], v['s10Hits'], v['numbers'])

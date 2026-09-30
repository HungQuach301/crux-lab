"""P01-style self-check of the v2 thumbnails (reference only; does not touch checks/, imports its token_share).
python3 episodes/ep001/preprod/thumbs_v2/selfcheck.py -> out/package/v2/selfcheck.json + legibility-25.png (25% and 10% views)."""
import json, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
EP = Path(__file__).resolve().parents[2]
REPO = EP.parents[1]
sys.dont_write_bytecode = True  # do not write caches into checks/
sys.path.insert(0, str(REPO / 'checks/py'))
from r_visual import token_share  # noqa: E402

def rel_lum(c):
    c = np.asarray(c, float) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]

OUT = EP / 'out/package/v2'
tokens = list(json.loads((EP / 'design/tokens.json').read_text())['colors'].values())
claims = {c['claimId']: c for c in json.loads((EP / 'out/claims.json').read_text())['claims']}
res = {}
for k in 'HLW':
    img = np.asarray(Image.open(OUT / f'thumb-{k}.png').convert('RGB'))
    meta = json.loads((OUT / f'thumb-{k}.json').read_text())
    h, w = img.shape[:2]
    small = img.reshape(h // 10, 10, w // 10, 10, 3).mean(axis=(1, 3))
    lum = rel_lum(small)
    rows = []
    for t in meta['texts']:
        x, y, bw, bh = [int(v / 10) for v in t['box']]
        reg = lum[y:y + max(1, bh), x:x + max(1, bw)]
        c = (np.percentile(reg, 95) + 0.05) / (np.percentile(reg, 5) + 0.05)
        ok_claim = None
        if t.get('claim'):
            ok_claim = claims[t['claim']]['display'] in t['text']
        rows.append({'text': t['text'], 'fontPx': t['fontPx'], 'px_at_25pct': round(t['fontPx'] / 4, 1), 'contrast_at_10pct': round(float(c), 2),
                     'claim': t.get('claim'), 'claimDisplayMatches': ok_claim, 'illustrativeClaim': claims[t['claim']]['illustrative'] if t.get('claim') else None})
    words = sum(len(t['text'].split()) for t in meta['texts'] if t.get('role') is None)
    res[k] = {'size': f'{w}x{h}', 'tokenSharePct': round(100 * token_share(img, tokens), 1), 'words_excl_badge': words,
              'minFontPx': min(t['fontPx'] for t in meta['texts']), 'minFontPx_excl_badge': min(t['fontPx'] for t in meta['texts'] if not t.get('role')),
              'minContrast10': min(r['contrast_at_10pct'] for r in rows), 'badge': any(t.get('role') for t in meta['texts']), 'texts': rows}
(OUT / 'selfcheck.json').write_text(json.dumps(res, indent=1, ensure_ascii=False))
# legibility sheet: each thumb at 25% (320x180) and 10% (128x72), shown 1:1
sheet = Image.new('RGB', (3 * 340 + 20, 180 + 72 + 70), (14, 17, 22))
d = ImageDraw.Draw(sheet)
for i, k in enumerate('HLW'):
    im = Image.open(OUT / f'thumb-{k}.png').convert('RGB')
    sheet.paste(im.resize((320, 180), Image.BOX), (20 + i * 340, 30))
    sheet.paste(im.resize((128, 72), Image.BOX), (20 + i * 340, 30 + 180 + 20))
    d.text((20 + i * 340, 8), f'thumb-{k}: 25% (320x180) and 10% (128x72), 1:1', fill=(154, 164, 178))
sheet.save(OUT / 'legibility-25.png')
for k, v in res.items():
    print(k, {x: v[x] for x in ('tokenSharePct', 'words_excl_badge', 'minFontPx', 'minFontPx_excl_badge', 'minContrast10', 'badge')})

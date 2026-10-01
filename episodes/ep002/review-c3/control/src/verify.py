#!/usr/bin/env python3
"""Checks for the CONTROL strips. verify.py <grabDir> <origStripsDir> S01 ...
1) rebuild fidelity: S-all.png (in-page builder) and S-recomposed-all.png (the compose path used for the masked strip)
   vs the original strip: pixels differing by > 8/255 (and mean |diff| per frame);
2) mask coverage at 1280x720: every recorded text() box is a flat #171B22 block in S-k-final.png;
3) OCR (tesseract --psm 11, strip upscaled 3x): words with >= 3 letters/digits, masked strip vs original strip."""
import sys, os, json, shutil, subprocess
import numpy as np
from PIL import Image
G, ORIG, *SC = sys.argv[1:]
X = lambda i: 3 + (i % 3) * 640
Y = lambda i: 2 + (i // 3) * 363
for s in SC:
    o = np.asarray(Image.open(f'{ORIG}/{s}.png').convert('RGB'), dtype=int)
    fid = []
    for nm in ('all', 'recomposed-all'):
        a = np.asarray(Image.open(f'{G}/{s}-{nm}.png').convert('RGB'), dtype=int)
        d = np.abs(a - o).max(axis=2)
        fid.append(f"{nm}: px>8 {int((d > 8).sum())}, max mean/frame {max(float(d[Y(i):Y(i) + 358, X(i):X(i) + 636].mean()) for i in range(6)):.3f}")
    J = json.load(open(f'{G}/{s}.json'))
    bad = 0
    for f in J['frames']:
        m = np.asarray(Image.open(f"{G}/{s}-{f['k']}-final.png").convert('RGB'), dtype=int)
        for t in f['texts']:
            l, tp, r, b = [int(round(v)) for v in t['box']]
            l, tp, r, b = max(l, 0), max(tp, 0), min(r, 1280), min(b, 720)
            if r <= l or b <= tp: continue
            reg = m[tp:b, l:r]
            if not (reg == [0x17, 0x1B, 0x22]).all(): bad += 1
    def ocr(path):
        im = Image.open(path).convert('L'); im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
        p = f'{G}/_ocr.png'; im.save(p)
        txt = subprocess.run(['tesseract', p, '-', '--psm', '11'], capture_output=True, text=True).stdout
        os.remove(p)
        return [w for w in txt.split() if sum(ch.isalnum() for ch in w) >= 3]
    wm, wo = ocr(f'{G}/{s}-mask.png'), ocr(f'{ORIG}/{s}.png')
    print(f"{s} | {' ; '.join(fid)} | text boxes {sum(len(f['texts']) for f in J['frames'])}, not flat: {bad} | OCR words original {len(wo)}, masked {len(wm)} {wm}")

#!/usr/bin/env python3
"""Compose 3x2 numbered strips (same layout as episodes/ep001/animatic/strips/Sxx.png: 1920x728, bg #05070A,
frames 636x358 at x=3+640*c, y=2+363*r, yellow number badge 40x40 at frame-relative (590,312)).
The badge pixels are copied from the original strip (same position, same number), so the numbering is identical.
Usage: compose.py <framesDir> <origStripsDir> <outDir> S01 ...  -> outDir/S-all.png, S-mask.png, prints diff vs original."""
import sys, os
import numpy as np
from PIL import Image
FR, ORIG, OUT, *SC = sys.argv[1:]
X = lambda c: 3 + 640 * c
Y = lambda r: 2 + 363 * r
BW, BH, BX, BY = 636, 358, 590, 312   # frame size; badge offset in frame
BADGE = (BX - 2, BY - 2, BX + 42, BY + 42)  # badge + 2 px margin, frame-relative
os.makedirs(OUT, exist_ok=True)
for s in SC:
    orig = Image.open(os.path.join(ORIG, f'{s}.png')).convert('RGBA')
    for kind in ('all', 'mask'):
        im = Image.new('RGBA', (1920, 728), (5, 7, 10, 255))
        for k in range(6):
            c, r = k % 3, k // 3
            f = Image.open(os.path.join(FR, f'{s}-{k + 1}-{kind}.png')).convert('RGBA').resize((BW, BH), Image.LANCZOS)
            im.paste(f, (X(c), Y(r)))
            b = (X(c) + BADGE[0], Y(r) + BADGE[1], X(c) + BADGE[2], Y(r) + BADGE[3])
            im.paste(orig.crop(b), b[:2])
        im.save(os.path.join(OUT, f'{s}-{kind}.png'))
        if kind == 'all':
            a, o = np.asarray(im, dtype=int)[..., :3], np.asarray(orig, dtype=int)[..., :3]
            d = np.abs(a - o).max(axis=2)
            cells = [float(d[Y(k // 3):Y(k // 3) + BH, X(k % 3):X(k % 3) + BW].mean()) for k in range(6)]
            print(s, 'vs original: mean abs diff per frame', [round(x, 2) for x in cells], '| px >32:', int((d > 32).sum()))

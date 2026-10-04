#!/usr/bin/env python3
"""finish.py <grabDir> S01 ... : S-k-final.png = S-k-mask.png (text() boxes filled #171B22) + flat #171B22 blocks over 3D
texture text: pixels where S-k-mask.png and S-k-tex.png differ (the MASKTEX render, texture glyphs replaced by #FF00FF
blocks) are grouped (dilated 6 px, connected components) and each group's bounding box + 4 px is filled #171B22."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
G, *SC = sys.argv[1:]
for s in SC:
    out = []
    for k in range(1, 7):
        m = np.array(Image.open(f'{G}/{s}-{k}-mask.png').convert('RGBA'))
        t = np.asarray(Image.open(f'{G}/{s}-{k}-tex.png').convert('RGBA'))
        d = np.abs(m[..., :3].astype(int) - t[..., :3].astype(int)).max(axis=2) > 6
        lab, n = ndimage.label(ndimage.binary_dilation(d, iterations=6))
        boxes = []
        for sl in ndimage.find_objects(lab):
            y0, y1, x0, x1 = max(sl[0].start - 4 + 6, 0), min(sl[0].stop + 4 - 6, 720), max(sl[1].start - 4 + 6, 0), min(sl[1].stop + 4 - 6, 1280)
            if (y1 - y0) * (x1 - x0) < 30: continue  # sub-pixel speck: not a glyph
            m[y0:y1, x0:x1] = (0x17, 0x1B, 0x22, 255); boxes.append((x0, y0, x1, y1))
        Image.fromarray(m).save(f'{G}/{s}-{k}-final.png')
        out.append(len(boxes))
    print(s, '3D-texture text blocks per frame:', out)

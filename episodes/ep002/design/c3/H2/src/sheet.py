#!/usr/bin/env python3
"""Contact sheet of work stills for review: python3 src/sheet.py out.png file1.png file2.png ..."""
import sys
from PIL import Image
ims = [Image.open(f) for f in sys.argv[2:]]
W, H = 640, 360
out = Image.new('RGB', (W * 3, H * ((len(ims) + 2) // 3)))
for i, im in enumerate(ims): out.paste(im.convert('RGB').resize((W, H)), ((i % 3) * W, (i // 3) * H))
out.save(sys.argv[1])

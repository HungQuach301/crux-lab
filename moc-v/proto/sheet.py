"""Ghép ảnh tĩnh thành tờ xem nhanh: python3 sheet.py <dir> <out.png> [cols] [width]"""
import sys, os, re
from PIL import Image, ImageDraw, ImageFont
d, out = sys.argv[1], sys.argv[2]; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4; W = int(sys.argv[4]) if len(sys.argv) > 4 else 640
fs = sorted([f for f in os.listdir(d) if f.endswith('.png') or f.endswith('.jpg')], key=lambda f: float(re.findall(r't([\d.]+)\.', f)[-1]) if re.findall(r't([\d.]+)\.', f) else 0)
H = W * 9 // 16; rows = (len(fs) + cols - 1) // cols
sh = Image.new('RGB', (cols * W, rows * (H + 30)), (40, 40, 40)); dr = ImageDraw.Draw(sh)
font = ImageFont.truetype('/home/user/crux-lab/toolkit/render/fonts/Inter-SemiBold.ttf', 22) if os.path.exists('/home/user/crux-lab/toolkit/render/fonts/Inter-SemiBold.ttf') else None
for i, f in enumerate(fs):
    im = Image.open(os.path.join(d, f)).convert('RGB').resize((W, H)); x, y = (i % cols) * W, (i // cols) * (H + 30)
    sh.paste(im, (x, y + 30)); dr.text((x + 6, y + 4), f, fill=(255, 255, 0), font=font)
sh.save(out); print(out, sh.size)

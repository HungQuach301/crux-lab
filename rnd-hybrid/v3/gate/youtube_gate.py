"""R&D v3 · CỔNG MÁY "nén giả YouTube": khung 1080p → x264 1080p ~8 Mbps → giải mã → hạ 360p (bicubic) → đo vùng chữ/mặt.
   python3 rnd-hybrid/v3/gate/youtube_gate.py <png 1080p> <roi.json của khung> <tên> <thư mục ra>
Chỉ số mỗi vùng (trên ảnh 360p): Michelson = (Lsáng − Ltối)/(Lsáng + Ltối) sau ngưỡng Otsu trong vùng; cao vùng (px 360p).
Ngưỡng ĐẠT (ghi trước, chưa hiệu chuẩn — chẩn đoán): chữ Michelson ≥ 0,35 và cao ≥ 9 px; mặt Michelson ≥ 0,35 và cao ≥ 14 px."""
import json, subprocess, sys, os
import numpy as np
from PIL import Image
png, roi, name, out = sys.argv[1], json.loads(sys.argv[2]) if sys.argv[2].startswith('{') else json.load(open(sys.argv[2])), sys.argv[3], sys.argv[4]
os.makedirs(out, exist_ok=True)
mp4 = os.path.join(out, name + '-8M.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-t', '2', '-i', png, '-c:v', 'libx264', '-preset', 'medium', '-b:v', '8M', '-maxrate', '8M', '-bufsize', '16M',
                '-pix_fmt', 'yuv420p', '-r', '30', mp4], check=True)
p360 = os.path.join(out, name + '-360p.png')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '1.0', '-i', mp4, '-frames:v', '1', '-vf', 'scale=640:360:flags=bicubic', p360], check=True)
im = np.asarray(Image.open(p360).convert('RGB')).astype(np.float32) @ np.array([0.2126, 0.7152, 0.0722]); k = 360 / 1080
def otsu(v):
    h, e = np.histogram(v, 64, (0, 255)); c = (e[:-1] + e[1:]) / 2; best, th = -1, 128
    for i in range(1, 64):
        w0, w1 = h[:i].sum(), h[i:].sum()
        if w0 == 0 or w1 == 0: continue
        m0, m1 = (h[:i] * c[:i]).sum() / w0, (h[i:] * c[i:]).sum() / w1; s = w0 * w1 * (m0 - m1) ** 2
        if s > best: best, th = s, c[i]
    return th
res = {}
for key, (x0, y0, x1, y1) in roi.items():
    a, b, c, d = [int(round(v * k)) for v in (x0, y0, x1, y1)]; a, b = max(a, 0), max(b, 0); c, d = min(c, 639), min(d, 359)
    if c - a < 2 or d - b < 2: res[key] = {'skip': 'ngoài khung'}; continue
    v = im[b:d, a:c].ravel(); t = otsu(v); lo, hi = v[v < t].mean(), v[v >= t].mean(); mich = (hi - lo) / (hi + lo + 1e-6)
    hmin = 14 if key == 'FACE' else 9
    res[key] = {'box360': [a, b, c, d], 'h360': d - b, 'michelson': round(float(mich), 3), 'pass': bool(mich >= 0.35 and (d - b) >= hmin)}
    Image.open(p360).crop((max(a - 6, 0), max(b - 6, 0), min(c + 6, 640), min(d + 6, 360))).resize(((c - a + 12) * 4, (d - b + 12) * 4), Image.NEAREST).save(os.path.join(out, f'{name}-{key}-crop360x4.png'))
print(json.dumps({'frame': name, 'regions': res, 'pass': all(r.get('pass', True) for r in res.values())}))

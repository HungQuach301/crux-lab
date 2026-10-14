"""Độ sáng trung bình (luma Rec.709, 0–255) của các cảnh ĐÊM, lấy mẫu mỗi 0,5 s, trước (clip v2) / sau (clip v3) — sửa (c) của chủ dự án.
   python3 rnd-hybrid/v3/clip/luma.py <video> <timeline.json>  → in JSON: theo cảnh + trung bình; cảnh I (ảnh tư liệu) bỏ qua."""
import json, subprocess, sys
import numpy as np
video, tl = sys.argv[1], json.load(open(sys.argv[2]))
NIGHT = ['E', 'F', 'G', 'H', 'J']
out = {}
for s in tl['shots']:
    if s['id'] not in NIGHT: continue
    vals = []
    t = s['t0'] + 0.1
    while t < s['t1'] - 0.05:
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{t:.3f}', '-i', video, '-frames:v', '1', '-vf', 'scale=480:270', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True, check=True).stdout
        a = np.frombuffer(raw, np.uint8).reshape(270, 480, 3).astype(np.float32)
        vals.append(float((a @ np.array([0.2126, 0.7152, 0.0722])).mean())); t += 0.5
    out[s['id']] = round(float(np.mean(vals)), 1)
out['mean'] = round(float(np.mean(list(out.values()))), 1)
print(json.dumps(out))

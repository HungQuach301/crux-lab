"""Mốc V · kiểm một đoạn trên SẢN PHẨM CUỐI (không sửa checks/; tiêu chí C14 chép đúng checks/page/sampler.js).
  python3 toolkit/factory/world/verify_seg.py <thư mục đoạn> <video.mp4> <out.json>
Đọc <video>.log.json (nhật ký trang mỗi 0,1 s từ render_shots.js) + spine.json.
  rule1   : chữ loại number/compare chỉ khi chartW ≥ 0,95 (vi phạm do trang ghi)
  rule2   : máy quay đứng yên ± pad quanh mọi từ khoá (log.camMoving tại mẫu gần nhất)
  rule3   : mọi động tác có lý do + âm (spine.moves) và sự kiện âm tương ứng (spine.events)
  C14     : mỗi 0,2 s, chữ opacity ≥ 0,95 đứng yên (hộp dịch < 2 px so với mẫu trước): cỡ ≥ 28 px VÀ tương phản ≥ 3:1 giữa phân vị 95/5
            của độ chói trong hộp trên khung video thu 4× (trung bình hộp 4×4) — như checks/page/sampler.js. Video phải 1920×1080.
  cuts    : cắt cứng = > 45 % điểm ảnh (xám, > 25 mức) đổi giữa hai khung liên tiếp
  modes   : tỉ lệ thời lượng chế độ thế giới / đồ thị (chartW < 0,5 / ≥ 0,5)
  F2      : mật độ sfx (sự kiện/phút, tối đa trong 10 s, sfx đè lời, sfx che từ khoá — đo SNR trên <video>.audio/stems) + nhãn đè nhau /
            chữ bị đường cắt (sfx_labels.py; BACKLOG F-2). level BLOCK (sfx che từ khoá, nhãn/đường đè chữ ở trạng thái đọc) → build_seg dừng
"""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx_labels  # noqa: E402
seg, video, out = sys.argv[1:4]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
S = json.load(open(os.path.join(seg if os.path.isdir(seg) else os.path.join(ROOT, 'moc-v/seg', seg), 'spine.json')))
logs = json.load(open(video.replace('.mp4', '.log.json')))
logs.sort(key=lambda l: l['t'])
res = {'video': video}
# rule 1
v1 = [dict(v, t=l['t']) for l in logs for v in l.get('violations', [])]
res['rule1'] = {'violations': len(v1), 'examples': v1[:5]}
# rule 2
cues = [(t, f"{b['id']}.{k}") for b in S['beats'] for k, t in b['cues'].items()]
v2 = []
for t, name in cues:
    near = [l for l in logs if abs(l['t'] - t) <= S['pad']]
    if any(l.get('camMoving') for l in near): v2.append(name)
res['rule2'] = {'keywords': len(cues), 'camera_moving_at_keyword': v2}
# rule 3
kinds = {e['kind'] for e in S['events']}
res['rule3'] = {'moves': len(S['moves']), 'missing_reason_or_sound': [m for m in S['moves'] if not m.get('reason') or m.get('sound') not in kinds]}
# modes
cw = np.array([l['chartW'] for l in logs])
res['modes'] = {'world_share': round(float((cw < 0.5).mean()), 3), 'chart_share': round(float((cw >= 0.5).mean()), 3),
                'first_5s_world': bool(all(l['chartW'] < 0.05 for l in logs if l['t'] < 5))}
# F-2: mật độ sfx + nhãn đè nhau (nhật ký trang + spine.events + stem của audio.py nếu có)
f2 = sfx_labels.check(S, logs, video.replace('.mp4', '.audio'))
res['F2'] = {'summary': sfx_labels.summary(f2), **f2}
# video frames (gray for cuts; rgb every 0.2 s for C14)
w, h = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', video],
                               capture_output=True, text=True).stdout.strip().split(','))
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', 'scale=320:180,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
g = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320).astype(np.int16)
cut = [round(i / 30, 2) for i in range(1, len(g)) if (np.abs(g[i] - g[i - 1]) > 25).mean() > 0.45]
res['cuts'] = {'hard_cuts': cut}
if (w, h) == (1920, 1080):
    fr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', video], capture_output=True, text=True).stdout.strip()
    assert fr == '30/1', f'C14: cần video 30 fps (bước n = 6k), gặp {fr}'
    # khung 1080p lấy ĐÚNG chỉ số khung n = 6k (t = k/5; fps=5 lệch tới nửa khung — cùng lỗi gói đạo diễn cũ), đọc lần lượt từng khung (nạp cả video float64 → hết bộ nhớ ở đoạn 34 s); phép tính giữ nguyên
    by_k = {}
    for l in logs:
        k = round(l['t'] * 5)
        if abs(l['t'] * 5 - k) <= 0.01: by_k.setdefault(k, []).append(l)
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-vf', r'select=not(mod(n\,6))', '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    prev, bad, n, k, FB = {}, [], 0, 0, 1080 * 1920 * 3
    while True:
        buf = proc.stdout.read(FB)
        if len(buf) < FB: break
        if k in by_k:
            F = np.frombuffer(buf, np.uint8).reshape(1080, 1920, 3).astype(np.float64) / 255
            lin = np.where(F <= 0.03928, F / 12.92, ((F + 0.055) / 1.055) ** 2.4)
            L = 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]
            for l in by_k[k]:
                for tx in l['texts']:
                    key = tx['text'] + tx['kind']; box = tx['box']; p = prev.get(key); prev[key] = box
                    if tx['opacity'] < 0.95 or (p and max(abs(a - b) for a, b in zip(p, box)) >= 2): continue
                    x0, y0, x1, y1 = [int(v) for v in box]; x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(1920, x1), min(1080, y1)
                    q = L[(y0 // 4) * 4:(y1 // 4 + 1) * 4, (x0 // 4) * 4:(x1 // 4 + 1) * 4]
                    if q.size < 16: continue
                    hh, ww = q.shape[0] // 4, q.shape[1] // 4
                    d = q[:hh * 4, :ww * 4].reshape(hh, 4, ww, 4).mean(axis=(1, 3)).ravel()
                    d.sort(); c25 = (d[int(len(d) * 0.95)] + 0.05) / (d[int(len(d) * 0.05)] + 0.05)
                    n += 1
                    if tx['px'] < 28 or c25 < 3: bad.append({'t': l['t'], 'text': tx['text'], 'px': tx['px'], 'contrastAt25': round(float(c25), 2)})
        k += 1
    proc.wait()
    res['C14'] = {'samples': n, 'violations': len(bad), 'examples': bad[:8]}
else:
    res['C14'] = {'skipped': f'video {w}×{h}; C14 đo trên bản 1920×1080'}
json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: (v['summary'] if k == 'F2' else v if k not in ('rule1', 'C14') else {kk: vv for kk, vv in v.items() if kk != 'examples'}) for k, v in res.items()}, ensure_ascii=False))
for lv in ('block', 'warn'):
    for m in f2[lv]: print(f'F-2 {lv.upper()}: {m}')

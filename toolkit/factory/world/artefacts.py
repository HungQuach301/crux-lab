"""Nhà máy · ARTEFACT HỢP ĐỒNG từ đoạn thế giới 3D (checks/CONTRACT.md; F11): out/camera.json, out/sonify-events.json.

camera.json — {fps, frames:[{t, x, y, zoom}], mapping, …}: máy quay 2.5D mỗi khung của tập (CONTRACT: x, y = tâm khung trên mặt phẳng biểu đồ, px
  của trang; zoom = tỉ lệ, 1 = cả trang). Ánh xạ từ máy quay 3D thật của mỗi khung (render_shots.js → <đoạn>.cam.json: vị trí p, hướng nhìn d,
  fov dọc, aspect — sau mọi chỉnh của scene.js, kể cả nắp ống kính khi bay):
    mặt phẳng biểu đồ = z = 0 của thế giới (đồ thị nằm trên đó; thế giới đứng trên sàn quanh z ≈ 0);
    tâm khung = giao của tia nhìn giữa khung với z = 0: h = p + s·d, s = −p_z / d_z (tia không cắt mặt phẳng phía trước → s = S_FALLBACK);
    bề rộng nhìn thấy ở đó w = 2·s·tan(fov/2)·aspect (đơn vị thế giới); 1920 px trang = W0 đơn vị thế giới ở zoom 1;
    x = h_x·1920/W0 + 960, y = −h_y·1920/W0 + 540, zoom = W0 / w.
  Tốc độ máy (checks: |Δ(x, y)| / (1920/zoom) + |Δ ln zoom|, theo bề rộng khung mỗi giây) = |Δh| / w + |Δ ln w| — KHÔNG phụ thuộc W0.
  Khung ngoài đoạn thế giới (shot 2D) = máy đứng yên ở giữa trang {x 960, y 540, zoom 1}. Thiếu nhật ký máy của một đoạn → không ghi (không bịa).
sonify-events.json — {fps, bar:[], line:[], dot:[{f, id, y}]}: mỗi âm dữ liệu của đoạn (spine.events kind 'data') ở KHUNG nó thật sự vang
  (audio.py dời nốt vào khe lời: audio-report.json data_events.t_sound), y = giá trị chuẩn hoá v (cao độ); id = <đoạn>:<thứ tự>.
"""
import json
import math
import os

W0 = 20.0            # đơn vị thế giới trên 1920 px trang ở zoom 1 (chỉ đổi thang x, y, zoom; tốc độ máy không đổi)
S_FALLBACK = 10.0    # tia nhìn không cắt z = 0 phía trước: điểm nhìn cách máy 10 đơn vị


def map_frame(c):
    """Một khung máy quay 3D {p, d, fov, aspect} → {x, y, zoom} (2.5D của CONTRACT)."""
    p, d = c['p'], c['d']
    n = math.sqrt(sum(v * v for v in d)) or 1.0
    d = [v / n for v in d]
    s = -p[2] / d[2] if d[2] < -1e-6 else S_FALLBACK
    if s <= 0:
        s = S_FALLBACK
    h = [p[i] + s * d[i] for i in range(3)]
    w = 2 * s * math.tan(math.radians(c['fov']) / 2) * c.get('aspect', 16 / 9)
    k = 1920 / W0
    return {'x': round(h[0] * k + 960, 3), 'y': round(-h[1] * k + 540, 3), 'zoom': round(W0 / w, 6)}


def camera_json(total, fps, segs):
    """segs: [{id, f0, f1, cams: [{f (khung của đoạn), p, d, fov, aspect}]}] (f0/f1 = khung của tập). → dict camera.json hoặc None nếu thiếu khung."""
    n = round(total * fps)
    still = {'x': 960.0, 'y': 540.0, 'zoom': 1.0}
    fr = [dict(still) for _ in range(n)]
    cover = []
    for g in segs:
        by = {c['f']: c for c in g['cams'] if c.get('p')}
        miss = [f for f in range(g['f1'] - g['f0']) if f not in by]
        if miss:
            return None, {'segment': g['id'], 'missing_frames': len(miss)}
        for f in range(g['f1'] - g['f0']):
            if g['f0'] + f < n:
                fr[g['f0'] + f] = map_frame(by[f])
        cover.append({'id': g['id'], 'f0': g['f0'], 'f1': g['f1']})
    out = {'fps': fps, 'frames': [{'t': round(i / fps, 4), **x} for i, x in enumerate(fr)], 'world': cover,
           'mapping': f'3D → 2.5D: tâm = giao tia nhìn với z = 0, zoom = {W0:g} / bề rộng nhìn thấy ở đó (đơn vị thế giới); ngoài đoạn thế giới: đứng yên '
                      '(toolkit/factory/world/artefacts.py)'}
    return out, None


def sonify_json(fps, segs):
    """segs: [{id, t0 (giây của tập), events: [{t, t_sound?, v}]}] → sonify-events.json."""
    dots = []
    for g in segs:
        for i, e in enumerate(g['events']):
            t = g['t0'] + e.get('t_sound', e['t'])
            dots.append({'f': int(round(t * fps)), 'id': f"{g['id']}:{i}", 'y': e['v'], **({'over': True} if e.get('over') else {})})
    dots.sort(key=lambda d: d['f'])
    return {'fps': fps, 'bar': [], 'line': [], 'dot': dots,
            '_about': 'âm dữ liệu của đoạn thế giới (spine.events data), khung = lúc nốt vang sau khi dời vào khe lời (audio.py); toolkit/factory/world/artefacts.py'}


def segment_files(mp4):
    """Đường dẫn sản phẩm build_seg của một đoạn: nhật ký máy quay, báo cáo tiếng."""
    return {'cam': mp4[:-4] + '.cam.json', 'audio_report': os.path.join(mp4[:-4] + '.audio', 'audio-report.json')}


def write(out_dir, total, fps, segs):
    """segs: [{id, mp4, spine (dict), t0, f0, f1}] → ghi out/camera.json + out/sonify-events.json; trả báo cáo."""
    rep = {}
    cams = []
    for g in segs:
        F = segment_files(g['mp4'])
        cams.append({'id': g['id'], 'f0': g['f0'], 'f1': g['f1'], 'cams': json.load(open(F['cam'])) if os.path.exists(F['cam']) else []})
    cam, why = camera_json(total, fps, cams)
    if cam:
        json.dump(cam, open(os.path.join(out_dir, 'camera.json'), 'w'))
        rep['camera'] = {'frames': len(cam['frames']), 'world': [c['id'] for c in cam['world']]}
    else:
        rep['camera'] = {'written': False, **why}
    son = []
    for g in segs:
        F = segment_files(g['mp4'])
        ar = json.load(open(F['audio_report'])) if os.path.exists(F['audio_report']) else {}
        ev = ar.get('data_events')
        src = 'audio-report'
        if ev is None:   # đoạn dựng trước khi audio.py ghi data_events: giờ theo spine (chưa dời vào khe lời)
            ev, src = [{'t': e['t'], 'v': e['v'], **({'over': True} if e.get('over') else {})} for e in g['spine']['events'] if e['kind'] == 'data'], 'spine'
        son.append({'id': g['id'], 't0': g['t0'], 'events': ev, 'src': src})
    json.dump(sonify_json(fps, son), open(os.path.join(out_dir, 'sonify-events.json'), 'w'), indent=1)
    rep['sonify'] = {g['id']: {'events': len(g['events']), 'from': g['src']} for g in son}
    return rep

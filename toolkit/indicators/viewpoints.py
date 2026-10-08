"""Đa dạng khung nhìn (tổng kết Tập 5 §3.3.2) — CHỈ BÁO. Đo vị trí + hướng máy quay, KHÔNG đo độ sáng (cine-lab #71: thước xám gộp
mọi cảnh tối thành một khung).
  - camera: `out/camera.json` của tập (2.5D {x, y, zoom} của nhà máy, hoặc 3D {pos, target, fovDeg} của pipeline 2D cũ → quy về 2.5D
    cùng cách `world/artefacts.py`: tâm = điểm nhìn trên z = 0, zoom = 20 / bề rộng nhìn thấy). Mẫu 0,5 s; hai mẫu cùng khung nhìn khi
    tâm lệch < 10 % bề rộng nhìn thấy và |ln(zoom1/zoom2)| < 0,15 (gom kiểu "leader": mọi mẫu so với khung đại diện).
  - spine: tư thế máy đặt tên (`moves[].from/to`) của các đoạn thế giới; thời gian ở mỗi tư thế = giữa hai cú máy.
Báo: số khung nhìn, khung nhìn/phút, cụm lớn nhất (% thời lượng).
    python3 toolkit/indicators/viewpoints.py camera episodes/ep005/out/camera.json
    python3 toolkit/indicators/viewpoints.py spine <spine.json …>
"""
import json, math, sys

ASPECT = 16 / 9


def to25(f):
    if 'zoom' in f:
        return f['x'], f['y'], f['zoom']
    p, t = f['pos'], f['target']
    dist = math.dist(p, t) or 1e-6
    width = 2 * dist * math.tan(math.radians(f.get('fovDeg', 35)) / 2) * ASPECT
    return t[0], t[1], 20 / width


def camera(path, step=0.5):
    d = json.load(open(path))
    fr = d['frames']
    fps = d.get('fps', 30)
    k = max(1, int(round(step * fps)))
    S = [to25(f) for f in fr[::k]]
    leaders, count = [], []
    for x, y, z in S:
        w = 20 / z
        for i, (lx, ly, lz) in enumerate(leaders):
            if abs(x - lx) < 0.1 * w and abs(y - ly) < 0.1 * w and abs(math.log(z / lz)) < 0.15:
                count[i] += 1
                break
        else:
            leaders.append((x, y, z)); count.append(1)
    minutes = len(S) * step / 60
    return {'method': 'camera', 'views': len(leaders), 'per_min': round(len(leaders) / minutes, 2),
            'largest_share': round(max(count) / len(S), 3), 'minutes': round(minutes, 2)}


def spine(paths):
    held, total = {}, 0.0
    for p in paths:
        d = json.load(open(p))
        mv = sorted(d.get('moves', []), key=lambda m: m['t0'])
        T = d.get('total', 0.0)
        total += T
        cur, t = (mv[0]['from'] if mv else 'start'), 0.0
        for m in mv:
            held[cur] = held.get(cur, 0.0) + max(0.0, m['t0'] - t)
            cur, t = m['to'], m['t1']
        held[cur] = held.get(cur, 0.0) + max(0.0, T - t)
    names = {k for k in held}
    return {'method': 'spine', 'views': len(names), 'per_min': round(len(names) / (total / 60), 2),
            'largest_share': round(max(held.values()) / total, 3), 'minutes': round(total / 60, 2)}


if __name__ == '__main__':
    mode, args = sys.argv[1], sys.argv[2:]
    print(json.dumps(camera(args[0]) if mode == 'camera' else spine(args), ensure_ascii=False))

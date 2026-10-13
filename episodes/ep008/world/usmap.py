"""Tập 8 · bản đồ "US only" (footage duy nhất Tập 8, G1 câu 3): đường viền 48 bang liền kề từ Natural Earth admin-1 50m (phạm vi công cộng,
RIGHTS.md M-NE-ADM1, SHA-256 b92c3f70…), chiếu phẳng (lon, lat) → (x, z) trong hộp rộng 10 đơn vị, giản lược điểm (mỗi đỉnh cách ≥ 0,04).
    python3 episodes/ep008/world/usmap.py → episodes/ep008/world/usmap.json (tệp nguồn ở work/footage/, không commit)"""
import hashlib, json, math, os
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
src = os.path.join(EP, 'work', 'footage', 'ne_50m_admin_1.geojson')
assert hashlib.sha256(open(src, 'rb').read()).hexdigest().startswith('b92c3f709b691240'), 'SHA khác RIGHTS M-NE-ADM1'
gj = json.load(open(src))
LON0, LON1, LAT0, LAT1, W = -125.0, -66.5, 24.0, 49.5, 10.0
k = W / ((LON1 - LON0) * math.cos(math.radians(37)))
out = []
for ft in gj['features']:
    p = ft['properties']
    if p.get('iso_a2') != 'US' or p.get('name') in ('Alaska', 'Hawaii'): continue
    g = ft['geometry']
    for poly in (g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]):
        pts, last = [], None
        for lon, lat in poly[0]:
            x = (lon - (LON0 + LON1) / 2) * math.cos(math.radians(37)) * k; z = -(lat - (LAT0 + LAT1) / 2) * k
            if last is None or math.hypot(x - last[0], z - last[1]) >= 0.04: pts.append([round(x, 3), round(z, 3)]); last = (x, z)
        if len(pts) >= 4: out.append(pts)
json.dump({'source': 'Natural Earth admin-1 50m (public domain) · RIGHTS.md M-NE-ADM1', 'polys': out}, open(os.path.join(HERE, 'usmap.json'), 'w'))
print(len(out), 'polys', sum(len(p) for p in out), 'pts')

"""F-15 (f) · BỘ DỰNG BẢN ĐỒ theo ngôn ngữ hình kênh: ranh giới Census (us-atlas = cartographic boundary GENZ2017 của Census, TopoJSON) +
thuộc tính Natural Earth admin-1 (vùng/phân vùng Census, postal, FIPS) → đường đã chiếu trên mặt phẳng thiết kế 1920×1080 + điểm neo nhãn.

  python3 -I toolkit/footage/map.py --topo <us-atlas-3.0.1.tgz>[:package/states-10m.json] --attrs <ne_110m_admin_1_states_provinces.geojson>
          (--division "South Atlantic" [--context "East South Central,Middle Atlantic"] | --states FL,GA,…) [--values <csv postal,value>]
          [--box 700,150,1800,960] --out map.json
Tô theo dữ liệu: `--values` (số theo bang → 5 lớp phân vị, thang tuần tự của kênh) hoặc mặc định thuộc tính phân loại `region_sub`
(phân vùng Census): bang trong `--division` = lớp 'focus', bang ngữ cảnh = 'context'. Nhãn: điểm xa biên nhất của mảnh lớn nhất (không phải
trọng tâm — bang cong như FL/MD lệch ra biển); world/plate.js `drawMap` hiện nhãn ĐÚNG mốc từ (label_at của spine) và tô vùng dần từ mốc đó.
Chiếu Albers diện tích bằng nhau (USGS: φ1 29,5°, φ2 45,5°, φ0 23°, λ0 −96°), vừa khít `--box` giữ tỉ lệ. Ô OSM (tuỳ chọn, chưa dùng ở thử F-15):
`--osm-attrib` chỉ ghi dòng nguồn "© OpenStreetMap contributors" (ODbL) vào map.json — tải ô không nằm trong công cụ này (mạng chặn tile.openstreetmap.org).
"""
import argparse, csv, io, json, math, os, tarfile

PAL = {'focus': '#4C8DFF', 'context': '#2A303B', 'line': '#0E1116', 'seq': ['#22314F', '#2C4A80', '#3A68B5', '#4C8DFF', '#9CC0FF']}


def read_topo(spec):
    path, _, member = spec.partition(':')
    if path.endswith(('.tgz', '.tar.gz')):
        with tarfile.open(path, 'r:gz') as tf:
            return json.load(tf.extractfile(member or 'package/states-10m.json'))
    return json.load(open(path))


def topo_features(T, obj='states'):
    sc, tr = T['transform']['scale'], T['transform']['translate']
    arcs = []
    for a in T['arcs']:
        x = y = 0; pts = []
        for dx, dy in a:
            x += dx; y += dy; pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        arcs.append(pts)
    def ring(ix):
        out = []
        for i in ix:
            p = arcs[i] if i >= 0 else arcs[~i][::-1]
            out += p[1:] if out else p
        return out
    for g in T['objects'][obj]['geometries']:
        polys = [g['arcs']] if g['type'] == 'Polygon' else g['arcs'] if g['type'] == 'MultiPolygon' else []
        yield {'id': str(g.get('id')), 'name': (g.get('properties') or {}).get('name'), 'polys': [[ring(r) for r in poly] for poly in polys]}


def albers(lon, lat, lat1=29.5, lat2=45.5, lat0=23.0, lon0=-96.0):
    r = math.radians
    n = (math.sin(r(lat1)) + math.sin(r(lat2))) / 2
    C = math.cos(r(lat1)) ** 2 + 2 * n * math.sin(r(lat1))
    rho = lambda la: math.sqrt(C - 2 * n * math.sin(r(la))) / n
    th = n * r(lon - lon0)
    return rho(lat) * math.sin(th), -(rho(lat0) - rho(lat) * math.cos(th))   # y xuống dưới (toạ độ màn hình)


def area(R):
    return 0.5 * sum(R[i][0] * R[i - 1][1] - R[i - 1][0] * R[i][1] for i in range(len(R)))


def inside(p, R):
    x, y, c = p[0], p[1], False
    for i in range(len(R)):
        (x1, y1), (x2, y2) = R[i - 1], R[i]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1:
            c = not c
    return c


def seg_dist(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    t = max(0, min(1, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / (vx * vx + vy * vy + 1e-12)))
    return math.hypot(p[0] - a[0] - t * vx, p[1] - a[1] - t * vy)


def pole(R, n=36):
    """Điểm trong đa giác xa biên nhất (lưới thô rồi tinh): neo nhãn không rơi ra biển/ra ngoài bang cong."""
    xs, ys = [p[0] for p in R], [p[1] for p in R]
    best, bd = (sum(xs) / len(xs), sum(ys) / len(ys)), -1
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    for _ in range(3):
        for i in range(n + 1):
            for j in range(n + 1):
                p = (x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * j / n)
                if not inside(p, R):
                    continue
                d = min(seg_dist(p, R[k - 1], R[k]) for k in range(len(R)))
                if d > bd:
                    best, bd = p, d
        w, h = (x1 - x0) / n * 2, (y1 - y0) / n * 2
        x0, x1, y0, y1 = best[0] - w, best[0] + w, best[1] - h, best[1] + h
    return best, bd


def simplify(R, tol):
    out = [R[0]]
    for p in R[1:]:
        if math.hypot(p[0] - out[-1][0], p[1] - out[-1][1]) >= tol:
            out.append(p)
    return out if len(out) >= 3 else R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--topo', required=True); ap.add_argument('--attrs', required=True); ap.add_argument('--division'); ap.add_argument('--context', default='')
    ap.add_argument('--states', default=''); ap.add_argument('--values'); ap.add_argument('--box', default='700,150,1800,960'); ap.add_argument('--out', required=True)
    ap.add_argument('--osm-attrib', action='store_true')
    a = ap.parse_args()
    NE = {f['properties']['fips'][2:]: f['properties'] for f in json.load(open(a.attrs))['features'] if f['properties'].get('iso_a2') == 'US'}
    want_div = [d.strip() for d in ([a.division] if a.division else []) + a.context.split(',') if d.strip()]
    want_st = {s.strip().upper() for s in a.states.split(',') if s.strip()}
    vals = {r[0].upper(): float(r[1]) for r in csv.reader(open(a.values)) if r and r[0].upper() != 'POSTAL'} if a.values else {}
    feats = []
    for f in topo_features(read_topo(a.topo)):
        p = NE.get(f['id'].zfill(2))
        if not p:
            continue
        sub = p.get('region_sub')
        if want_st and p['postal'] not in want_st:
            continue
        if not want_st and sub not in want_div:
            continue
        rings = [[albers(lon, lat) for lon, lat in R] for poly in f['polys'] for R in poly[:1]]   # vành ngoài mỗi mảnh
        feats.append({'id': p['postal'], 'fips': f['id'], 'name': p['name'], 'division': sub, 'region': p.get('region'),
                      'cls': 'focus' if sub == a.division else 'context', 'value': vals.get(p['postal']), 'rings': rings})
    if not feats:
        raise SystemExit('map: không bang nào khớp')
    X = [x for f in feats for R in f['rings'] for x, _ in R]; Y = [y for f in feats for R in f['rings'] for _, y in R]
    bx = [float(v) for v in a.box.split(',')]
    k = min((bx[2] - bx[0]) / (max(X) - min(X)), (bx[3] - bx[1]) / (max(Y) - min(Y)))
    ox = bx[0] + ((bx[2] - bx[0]) - k * (max(X) - min(X))) / 2 - k * min(X)
    oy = bx[1] + ((bx[3] - bx[1]) - k * (max(Y) - min(Y))) / 2 - k * min(Y)
    if vals:   # 5 lớp phân vị → thang tuần tự của kênh
        vs = sorted(v for v in vals.values())
        cut = [vs[min(len(vs) - 1, int(len(vs) * q / 5))] for q in range(1, 5)]
    for f in feats:
        f['rings'] = [simplify([(round(ox + k * x, 1), round(oy + k * y, 1)) for x, y in R], 0.8) for R in f['rings']]
        big = max(f['rings'], key=lambda R: abs(area(R)))
        (lx, ly), d = pole(big)
        f['label'] = [round(lx, 1), round(ly, 1)]; f['label_room'] = round(d, 1); f['area_px'] = round(sum(abs(area(R)) for R in f['rings']))
        f['fill'] = PAL['seq'][sum(f['value'] > c for c in cut)] if vals and f['value'] is not None else PAL[f['cls']]
    focus = [f for f in feats if f['cls'] == 'focus']
    rep = {'_about': 'toolkit/footage/map.py (F-15): toạ độ thiết kế 1920×1080, Albers USGS', 'box': bx,
           'sources': ['Census Bureau cartographic state boundaries 2017 (GENZ2017) via us-atlas 3.0.1 (TopoJSON)',
                       'Natural Earth admin-1 states/provinces 1:110m (attributes: postal, region, region_sub)'] + (['© OpenStreetMap contributors (ODbL)'] if a.osm_attrib else []),
           'source_line': 'Map: U.S. Census Bureau; Natural Earth', 'division': a.division, 'features': feats,
           'focus_box': [min(x for f in focus for R in f['rings'] for x, _ in R), min(y for f in focus for R in f['rings'] for _, y in R),
                         max(x for f in focus for R in f['rings'] for x, _ in R), max(y for f in focus for R in f['rings'] for _, y in R)] if focus else None}
    json.dump(rep, open(a.out, 'w'), separators=(',', ':'), ensure_ascii=False)
    print(json.dumps({'features': len(feats), 'focus': [f['id'] for f in focus], 'bytes': os.path.getsize(a.out)}))


if __name__ == '__main__':
    main()

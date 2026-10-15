"""F-17 · LUẬT KHOÁ MÀU DỮ LIỆU của lớp cine (chạy trên <out>.cine.json của cine_check.js).
  python3 toolkit/factory/world/cine/cine_color.py <cine.json> [<report.json>]     → thoát 1 khi CHẶN
Mỗi mẫu t, mỗi màu dữ liệu (vật role series/bar/grid, mặt nạ co 2 px, ≥ 200 điểm ảnh): trung bình sRGB trước lớp (trang không lớp) và sau lớp.
  - ΔE2000 (CIEDE2000, D65, kL = kC = kH = 1) giữa trước/sau > DE_MAX → CHẶN
  - thứ tự độ sáng: cặp màu có |ΔL*| trước ≥ ORDER_MIN mà sau lớp đổi dấu với |ΔL*| sau ≥ ORDER_FLIP → CHẶN (vd v4 cảnh c: cột "hi" tối hơn
    cột vàng trước lớp, sáng hơn sau lớp)
DE_MAX = 5 ghi trước trong toolkit/factory/f17/INTENT.md (T4/T5). INTENT ghi "đảo thứ tự sáng → CHẶN" không kèm vùng chết; ORDER_MIN/ORDER_FLIP là ĐỊNH
NGHĨA THÊM khi viết luật (trước lần đo đầu, commit 4ccffcab): cặp gần bằng sáng (|ΔL*| < 1 trước) không có thứ tự để đảo, và đổi dấu < 0,5 L* sau lớp là
nhiễu lượng tử/hạt. Cặp đảo nhỏ hơn các mức này không bị chặn (REVIEWER F-17).
"""
import json, math, sys

DE_MAX, ORDER_MIN, ORDER_FLIP = 5.0, 1.0, 0.5


def srgb_to_lab(c):
    lin = [((v / 255 + 0.055) / 1.055) ** 2.4 if v / 255 > 0.04045 else v / 255 / 12.92 for v in c]
    X = 0.4124564 * lin[0] + 0.3575761 * lin[1] + 0.1804375 * lin[2]
    Y = 0.2126729 * lin[0] + 0.7151522 * lin[1] + 0.0721750 * lin[2]
    Z = 0.0193339 * lin[0] + 0.1191920 * lin[1] + 0.9503041 * lin[2]
    f = lambda t: t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116  # noqa: E731
    fx, fy, fz = f(X / 0.95047), f(Y / 1.0), f(Z / 1.08883)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def de2000(l1, l2):
    L1, a1, b1 = l1; L2, a2, b2 = l2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2); Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h = lambda a, b: 0.0 if a == 0 and b == 0 else math.degrees(math.atan2(b, a)) % 360  # noqa: E731
    h1p, h2p = h(a1p, b1), h(a2p, b2)
    dLp, dCp = L2 - L1, C2p - C1p
    if C1p * C2p == 0: dhp = 0.0
    elif abs(h2p - h1p) <= 180: dhp = h2p - h1p
    elif h2p - h1p > 180: dhp = h2p - h1p - 360
    else: dhp = h2p - h1p + 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0: hpm = h1p + h2p
    elif abs(h1p - h2p) <= 180: hpm = (h1p + h2p) / 2
    elif h1p + h2p < 360: hpm = (h1p + h2p + 360) / 2
    else: hpm = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hpm - 30)) + 0.24 * math.cos(math.radians(2 * hpm)) + 0.32 * math.cos(math.radians(3 * hpm + 6))
         - 0.20 * math.cos(math.radians(4 * hpm - 63)))
    dth = 30 * math.exp(-(((hpm - 275) / 25) ** 2))
    RC = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    SL = 1 + 0.015 * (Lpm - 50) ** 2 / math.sqrt(20 + (Lpm - 50) ** 2); SC = 1 + 0.045 * Cpm; SH = 1 + 0.015 * Cpm * T
    RT = -math.sin(math.radians(2 * dth)) * RC
    return math.sqrt((dLp / SL) ** 2 + (dCp / SC) ** 2 + (dHp / SH) ** 2 + RT * (dCp / SC) * (dHp / SH))


def judge(doc):
    block, rows, worst = [], [], 0.0
    for s in doc['samples']:
        g = [{**x, 'lab0': srgb_to_lab(x['base']), 'lab1': srgb_to_lab(x['cine'])} for x in s['data']]
        for x in g:
            de = de2000(x['lab0'], x['lab1']); worst = max(worst, de)
            rows.append({'t': s['t'], 'key': x['key'], 'n': x['n'], 'L0': round(x['lab0'][0], 2), 'L1': round(x['lab1'][0], 2), 'dE': round(de, 2)})
            if de > DE_MAX: block.append(f"t={s['t']} màu {x['key']}: ΔE2000 {de:.2f} > {DE_MAX}")
        for i in range(len(g)):
            for j in range(i + 1, len(g)):
                d0, d1 = g[i]['lab0'][0] - g[j]['lab0'][0], g[i]['lab1'][0] - g[j]['lab1'][0]
                if abs(d0) >= ORDER_MIN and abs(d1) >= ORDER_FLIP and (d0 > 0) != (d1 > 0):
                    block.append(f"t={s['t']} đảo thứ tự sáng {g[i]['key']} / {g[j]['key']}: L* {d0:+.1f} → {d1:+.1f}")
    n = sum(len(s['data']) for s in doc['samples'])
    return {'level': 'BLOCK' if block else ('PASS' if n else 'NO_DATA'), 'samples': len(doc['samples']), 'groups': n,
            'max_dE': round(worst, 2), 'block': block, 'rows': rows, 'thresholds': {'DE_MAX': DE_MAX, 'ORDER_MIN': ORDER_MIN, 'ORDER_FLIP': ORDER_FLIP}}


if __name__ == '__main__':
    doc = json.load(open(sys.argv[1])); r = judge(doc)
    if len(sys.argv) > 2: json.dump(r, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: r[k] for k in ('level', 'samples', 'groups', 'max_dE')}, ensure_ascii=False))
    for m in r['block'][:20]: print('CHẶN:', m)
    sys.exit(1 if r['level'] == 'BLOCK' else 0)

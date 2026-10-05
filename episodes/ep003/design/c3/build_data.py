"""Tập 3 · C3: dựng design/c3/work/data.js cho style frame (không commit work/).
Claim lấy từ numbers.md (bảng A, C): mỗi số trên hình đi qua CL(id) → display dựng từ giá trị + đơn vị ở đây.
Cửa sổ (roll, lockReal) từ out/model.json; trung bình TB3MS 240 tháng tính lại từ data/raw/TB3MS.csv.
    python3 episodes/ep003/design/c3/build_data.py
"""
import csv, json, os, re

EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
LONG = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def claims():
    out = {}
    for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
        m = re.match(r'^\| `([a-z0-9_]+)` \| ([^|]+) \| ([^|]+) \|', ln)
        if not m:
            continue
        cid, val, unit = m.group(1), m.group(2).strip(), m.group(3).strip()
        if re.match(r'^\d{4}-\d{2}-\d{2}$', val):
            y, mo = int(val[:4]), int(val[5:7])
            out[cid] = {'value': val, 'display': f'{MON[mo - 1]} {y}', 'long': f'{LONG[mo - 1]} {y}', 'year': str(y)}
        elif unit == 'multiple':
            out[cid] = {'value': float(val), 'display': f'×{val}'}
        elif unit.startswith('%'):
            out[cid] = {'value': float(val), 'display': f'{val}%'}
        elif re.match(r'^[\d.]+$', val):
            out[cid] = {'value': float(val), 'display': val}
    # bối cảnh (bảng B): chữ cố định, không số mới
    out['ctx_guarantee'] = {'display': '×2'}
    out['ctx_hypothetical'] = {'display': 'IF today\'s guarantee had existed'}
    out['ctx_ee_rate'] = {'display': '2.40%', 'issued': 'for bonds issued May to October 2026'}
    out['ctx_penalty'] = {'display': 'cashed before 5 years: 3 months of interest lost', 'years': '5', 'months': '3'}
    return out


def main():
    tb = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:]]
    idx = {d: i for i, (d, _) in enumerate(tb)}
    m = json.load(open(os.path.join(EP, 'out/model.json')))
    W = []
    for w in m['windows']:
        s = w['start'][:7]; i = idx[s]
        avg = sum(v for _, v in tb[i:i + 240]) / 240
        W.append({'s': s, 'roll': round(w['roll'], 5), 'real': None if w.get('lockReal') is None else round(w['lockReal'], 5),
                  'avg': round(avg, 4), 'r0': tb[i][1]})
    assert len(W) == 873
    cpi = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/CPIAUCNS.csv'))))[1:] if r[1]]
    C = claims()
    # tự kiểm: các số trên hình trùng mô hình
    above = sum(w['roll'] > 2 for w in W) / len(W) * 100
    assert f'{above:.1f}' == f"{C['share_tbills_above_double_pct']['value']:.1f}", above
    mean = sum(v for _, v in tb) / len(tb)
    assert f'{mean:.2f}' == f"{C['mean_tb3ms_all_pct']['value']:.2f}", mean
    rule = sum((w['avg'] > 1200 * (2 ** (1 / 240) - 1)) == (w['roll'] > 2) for w in W)
    assert rule == 873, rule
    tf = os.path.join(EP, 'animatic/timing.json')
    timing = json.load(open(tf)) if os.path.exists(tf) else None
    data = {'timing': timing, 'series': tb, 'cpi': [c for c in cpi if c[0] >= '1934-01'], 'windows': W, 'claims': C,
            'breakeven': 1200 * (2 ** (1 / 240) - 1)}
    os.makedirs(os.path.join(EP, 'design/c3/work'), exist_ok=True)
    open(os.path.join(EP, 'design/c3/work/data.js'), 'w').write('window.DATA = ' + json.dumps(data) + ';\n')
    print('data.js:', len(W), 'windows;', len(C), 'claims; above', round(above, 1), '; rule', rule, '/873')


if __name__ == '__main__':
    main()

"""Tập 4 — mô hình (đặc tả topics-r1/machine/tax-2/model.json → newKindNeeds; tên kind do phiên K quyết).
Viết lại từ đặc tả, không gọi calc.py của hồ sơ. Đọc episodes/ep004/data/*.csv (fetch.py), ghi out/model.json (chưa làm tròn
+ bản làm tròn theo đặc tả). Thêm cho tập (ngoài hồ sơ; định nghĩa ở gates/V0-defs.md): lãi và quý vượt giới hạn của một căn
nhà mua năm 2000 với giá P ∈ PRICES, theo từng chỉ số.
  python3 episodes/ep004/model/model.py"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
D = os.path.join(EP, 'data')
SERIES = {'los_angeles': 'ATNHPIUS31084Q', 'san_diego': 'ATNHPIUS41740Q', 'san_francisco': 'ATNHPIUS41884Q',
          'san_jose': 'ATNHPIUS41940Q', 'seattle': 'ATNHPIUS42644Q', 'boston': 'ATNHPIUS14454Q',
          'new_york': 'ATNHPIUS35614Q', 'miami': 'ATNHPIUS33124Q', 'denver': 'ATNHPIUS19740Q',
          'phoenix': 'ATNHPIUS38060Q', 'dallas': 'ATNHPIUS19124Q', 'chicago': 'ATNHPIUS16984Q'}
P = dict(buyYear=2000, saleQuarter='2026-04-01', exclusionJoint=500000, exclusionSingle=250000,
         cpiBaseMonth='1997-05-01', cpiNowMonth='2026-08-01', countCutoffs=[200000, 300000])
PRICES = [200000, 300000]  # giá mua 2000 minh hoạ (ILLUSTRATIVE) cho phần hành trình


def read(sid):
    rows = list(csv.reader(open(os.path.join(D, sid + '.csv'))))
    return [(r[0], float(r[1])) for r in rows[1:] if len(r) > 1 and r[1] not in ('', '.')]


def series_stats(sid):
    s = read(sid)
    assert s[-1][0] == P['saleQuarter'], (sid, s[-1])
    base = [v for d, v in s if d.startswith(str(P['buyYear']))]
    assert len(base) == 4, sid
    b = sum(base) / 4
    g = s[-1][1] / b
    assert g > 1
    st = {'growth': g, 'threshold_joint': P['exclusionJoint'] / (g - 1)}
    for price in PRICES:
        k = price // 1000
        st[f'gain_at_{k}k'] = price * (g - 1)
        cross = next((d for d, v in s if d > f"{P['buyYear']}-12-31" and price * (v / b - 1) > P['exclusionJoint']), None)
        st[f'cross_quarter_at_{k}k'] = cross
        # quý đầu tiên mà từ đó tới quý bán lãi luôn > giới hạn (khác cross khi lãi vượt rồi tụt lại dưới, ví dụ quanh 2006–2011)
        after = [(d, price * (v / b - 1) > P['exclusionJoint']) for d, v in s if d > f"{P['buyYear']}-12-31"]
        stay = None
        for d, above in after:
            if above and stay is None:
                stay = d
            elif not above:
                stay = None
        st[f'stay_quarter_at_{k}k'] = stay
    return st


def main():
    raw = {}
    for name, sid in SERIES.items():
        for k, v in series_stats(sid).items():
            raw[f'{k}_{name}'] = v
    us = series_stats('USSTHPI')
    for k, v in us.items():
        raw[f'{k}_us'] = v
    raw['threshold_single_us'] = P['exclusionSingle'] / (us['growth'] - 1)
    thr = {n: raw[f'threshold_joint_{n}'] for n in SERIES}
    raw['threshold_joint_min'] = min(thr.values()); raw['threshold_joint_max'] = max(thr.values())
    raw['threshold_joint_min_metro'] = min(thr, key=thr.get); raw['threshold_joint_max_metro'] = max(thr, key=thr.get)
    for c in P['countCutoffs']:
        raw[f'metros_threshold_under_{c // 1000}k'] = sum(1 for v in thr.values() if v < c)
        raw[f'metros_threshold_under_{c // 1000}k_names'] = sorted(n for n, v in thr.items() if v < c)   # K3.8: mọi mốc
    for price in PRICES:
        k = price // 1000
        raw[f'metros_crossed_at_{k}k'] = sum(1 for n in SERIES if raw[f'cross_quarter_at_{k}k_{n}'])
    cpi = dict(read('CPIAUCNS'))
    assert max(cpi) == P['cpiNowMonth']
    raw['cpi_base'] = cpi[P['cpiBaseMonth']]; raw['cpi_now'] = cpi[P['cpiNowMonth']]
    raw['excl_joint_1997_in_now'] = P['exclusionJoint'] * raw['cpi_now'] / raw['cpi_base']
    # bất biến (đặc tả)
    for n in list(SERIES) + ['us']:
        assert abs(raw[f'threshold_joint_{n}'] * (raw[f'growth_{n}'] - 1) - P['exclusionJoint']) < 1e-6
    assert abs(raw['threshold_single_us'] - raw['threshold_joint_us'] * P['exclusionSingle'] / P['exclusionJoint']) < 1e-6
    assert raw['metros_threshold_under_200k'] <= raw['metros_threshold_under_300k'] <= len(SERIES)

    def rnd(k, v):
        if isinstance(v, (str, list)) or v is None:
            return v
        if k.startswith('growth'):
            return round(v, 4)
        if k.startswith(('threshold', 'gain')):
            return round(v, -2)
        if k.startswith('excl_'):
            return round(v, -3)
        return v
    out = {'params': {**P, 'prices': PRICES}, 'raw': raw, 'rounded': {k: rnd(k, v) for k, v in raw.items()}}
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump(out, open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1)
    return out


if __name__ == '__main__':
    o = main()['rounded']
    print(json.dumps({k: v for k, v in o.items() if 'cross' in k or 'gain' in k or 'crossed' in k}, indent=0))

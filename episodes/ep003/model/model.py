"""Tập 3 — mô hình "khoá một bội số đã biết" so với "lăn lãi ngắn hạn", phát lại từ mọi tháng bắt đầu.

Viết theo đặc tả `topics-r1/machine/retire-4/model.json` → newKindNeeds (tên kind do phiên K quyết; nhãn làm việc
"lock-vs-roll-replay"). Một hàm `replay(params)` dùng cho cả retire-4 (Tập 3) và retire-3 (kiểm đặc tả dùng lại).

  python3 episodes/ep003/model/model.py            → out/model.json (unrounded) + in tóm tắt
  python3 episodes/ep003/model/model.py --retire3  → so với topics-r1/machine/retire-3/result.json
"""
import csv, json, math, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
RAW = os.path.join(EP, 'data', 'raw')


def month(d):
    """'YYYY-MM' or 'YYYY-MM-01' → 'YYYY-MM-01'."""
    if d is None:
        return None
    if len(d) == 7:
        return d + '-01'
    if len(d) == 10 and d.endswith('-01'):
        return d
    raise ValueError(f'not a month: {d}')


def add(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + m - 1 + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


def load(spec):
    out = {}
    with open(os.path.join(RAW, os.path.basename(spec['file']))) as f:
        for row in csv.DictReader(f):
            v = row[spec['valueColumn']]
            if v not in ('', '.'):
                out[month(row[spec['dateColumn']])] = float(v)
    return out


def share(n, d):
    return 100 * n / d if d else None


def replay(P):
    H = P['horizonMonths']
    R = load(P['roll'])
    p = P['roll']['periodMonths']
    assert H % p == 0
    lock = P['lock']
    L = load(lock) if 'file' in lock else None
    q = lock.get('periodMonths')
    defl = load(P['deflator']) if P.get('deflator') else None
    first = month(P.get('firstStart')) or min(R)
    last = month(P.get('lastStart'))
    windows = []
    s = first
    end_data = max(R)
    while s <= end_data:
        if last and s > last:
            break
        need = [add(s, k * p) for k in range(H // p)]
        if all(x in R for x in need) and (L is None or s in L):
            roll = 1.0
            for x in need:
                roll *= 1 + R[x] * p / 1200
            lk = lock['multiple'] if L is None else (1 + L[s] * q / 1200) ** (H / q)
            w = {'start': s, 'end': add(s, H - 1), 'roll': roll, 'lock': lk, 'lockVsRollPct': 100 * (lk / roll - 1)}
            if L is not None:
                w['rollRateAtStart'], w['lockRateAtStart'] = R[s], L[s]
            if defl is not None:
                e = add(s, H)
                if s in defl and e in defl:
                    w['lockReal'] = lk * defl[s] / defl[e]
                    w['rollReal'] = roll * defl[s] / defl[e]
            windows.append(w)
        s = add(s, 1)

    def stats(ws):
        n = len(ws)
        if not n:
            return {'nWindows': 0}
        lo = min(ws, key=lambda w: w['roll'])  # min() keeps the earliest on ties
        hi = max(ws, key=lambda w: (w['roll'], -ws.index(w)))
        return {'from': ws[0]['start'], 'to': ws[-1]['start'], 'nWindows': n,
                'shareRollAhead': share(sum(w['roll'] > w['lock'] for w in ws), n),
                'shareLockAhead': share(sum(w['lock'] > w['roll'] for w in ws), n),
                'medianRoll': statistics.median(w['roll'] for w in ws),
                'minRoll': lo['roll'], 'minRollStart': lo['start'], 'maxRoll': hi['roll'], 'maxRollStart': hi['start'],
                'medianLockVsRollPct': statistics.median(w['lockVsRollPct'] for w in ws),
                'minLockVsRollPct': min(w['lockVsRollPct'] for w in ws),
                'maxLockVsRollPct': max(w['lockVsRollPct'] for w in ws)}

    out = {'params': P, 'nWindows': len(windows), 'firstStart': windows[0]['start'], 'lastStart': windows[-1]['start'],
           **{k: v for k, v in stats(windows).items() if k not in ('from', 'to', 'nWindows')},
           'latest': {k: windows[-1][k] for k in ('start', 'end', 'roll', 'lock')},
           'rollRateLatest': {'month': end_data, 'value': R[end_data]}}
    if L is None:
        out['equivalentLockRate'] = 100 * (lock['multiple'] ** (12 / H) - 1)
    out['subsets'] = {}
    for name, (a, b) in (P.get('subsets') or {}).items():
        a, b = month(a), month(b)
        out['subsets'][name] = stats([w for w in windows if w['start'] >= a and (b is None or w['start'] <= b)])
    if P.get('startFilter', {}).get('type') == 'rollRateAboveLockRate':
        f = [w for w in windows if w['rollRateAtStart'] > w['lockRateAtStart']]
        runs, prev = [], None
        for w in f:
            if prev is None or add(prev, 1) != w['start']:
                runs.append([])
            runs[-1].append(w)
            prev = w['start']
        out['filtered'] = {**stats(f), 'runs': len(runs),
                           'lockMajorityRuns': sum(sum(w['lock'] > w['roll'] for w in r) > len(r) / 2 for r in runs)}
    if defl is not None:
        rw = [w for w in windows if 'lockReal' in w]
        worst = min(rw, key=lambda w: w['lockReal'])
        below = [w for w in rw if w['lockReal'] < 1]
        out['deflator'] = {'nRealWindows': len(rw), 'skippedStarts': [w['start'] for w in windows if 'lockReal' not in w],
                           'shareLockRealAtLeastOne': share(sum(w['lockReal'] >= 1 for w in rw), len(rw)),
                           'shareLockRealBelowOne': share(len(below), len(rw)),
                           'medianLockReal': statistics.median(w['lockReal'] for w in rw),
                           'minLockReal': worst['lockReal'], 'minLockRealStart': worst['start'],
                           'lastStartLockRealBelowOne': below[-1]['start'] if below else None}
    if P.get('nearBandPct') is not None:
        out['nearCount'] = sum(abs(w['roll'] / w['lock'] - 1) < P['nearBandPct'] / 100 for w in windows)
    out['windows'] = windows
    return out


RETIRE4 = {
    'roll': {'file': 'data/TB3MS.csv', 'dateColumn': 'observation_date', 'valueColumn': 'TB3MS', 'periodMonths': 1},
    'lock': {'multiple': 2.0}, 'horizonMonths': 240, 'firstStart': '1934-01', 'lastStart': None,
    'subsets': {'1934-1949': ['1934-01', '1949-12'], '1950-1989': ['1950-01', '1989-12'], 'since-1990': ['1990-01', None],
                'guarantee': ['2005-05', None]},
    'deflator': {'file': 'data/CPIAUCNS.csv', 'dateColumn': 'observation_date', 'valueColumn': 'CPIAUCNS'},
    'nearBandPct': 0.5,
}
RETIRE3 = {
    'roll': {'file': 'data/GS1.csv', 'dateColumn': 'observation_date', 'valueColumn': 'GS1', 'periodMonths': 12},
    'lock': {'file': 'data/GS5.csv', 'dateColumn': 'observation_date', 'valueColumn': 'GS5', 'periodMonths': 12},
    'horizonMonths': 60, 'firstStart': '1953-04', 'startFilter': {'type': 'rollRateAboveLockRate'},
}


def summary4(m):
    s, d = m['subsets'], m['deflator']
    return {
        'starts': m['nWindows'], 'first_start': m['firstStart'], 'last_start': m['lastStart'],
        'share_tbills_above_double_pct': round(m['shareRollAhead'], 1),
        'median_tbill_multiple_20y': round(m['medianRoll'], 3), 'min_tbill_multiple_20y': round(m['minRoll'], 3),
        'max_tbill_multiple_20y': round(m['maxRoll'], 3),
        'share_tbills_above_double_starts_since_1990_pct': round(s['since-1990']['shareRollAhead'], 1),
        'latest_tbill_multiple_20y': round(m['latest']['roll'], 3),
        'doubling_rate_pct_per_year': round(m['equivalentLockRate'], 2), 'real_windows': d['nRealWindows'],
        'share_double_beat_prices_pct': round(d['shareLockRealAtLeastOne'], 1),
        'median_real_value_double_pct': round(100 * d['medianLockReal'], 1),
        'tb3ms_latest_pct': m['rollRateLatest']['value'],
        'min_start': m['minRollStart'], 'max_start': m['maxRollStart'],
        'starts_with_guarantee': s['guarantee']['nWindows'],
        'share_above_double_guarantee_starts_pct': round(s['guarantee']['shareRollAhead'], 1),
        'min_multiple_guarantee_starts': round(s['guarantee']['minRoll'], 3),
        'max_multiple_guarantee_starts': round(s['guarantee']['maxRoll'], 3),
        'starts_1934_1949': s['1934-1949']['nWindows'],
        'share_above_double_1934_1949_pct': round(s['1934-1949']['shareRollAhead'], 1),
        'starts_1950_1989': s['1950-1989']['nWindows'],
        'share_above_double_1950_1989_pct': round(s['1950-1989']['shareRollAhead'], 1),
        'starts_since_1990': s['since-1990']['nWindows'],
        'share_double_lost_buying_power_pct': round(d['shareLockRealBelowOne'], 1),
        'last_lost_start': d['lastStartLockRealBelowOne'],
        'worst_real_value_double_pct': round(100 * d['minLockReal'], 1), 'worst_real_start': d['minLockRealStart'],
        'near_double_starts': m['nearCount'],
    }


def extra4(m):
    """Đại lượng thêm ở C2 (needs-claims NC-1, NC-2)."""
    import csv
    tb = load(RETIRE4['roll'])
    D = sorted(tb); ix = {d: i for i, d in enumerate(D)}
    be = 1200 * (2 ** (1 / 240) - 1)
    agree = sum((statistics.mean(tb[d] for d in D[ix[w['start']]:ix[w['start']] + 240]) > be) == (w['roll'] > 2) for w in m['windows'])
    return {'steady_breakeven_tb3ms_pct': round(be, 2), 'share_avg_rule_agrees_pct': round(100 * agree / len(m['windows']), 1)}


def summary3(m):
    f = m['filtered']
    return {'starts_all': m['nWindows'], 'first_start_year': int(m['firstStart'][:4]),
            'last_start_year': int(m['lastStart'][:4]), 'share_lock_ahead_all_pct': round(m['shareLockAhead'], 1),
            'starts_inverted': f['nWindows'], 'share_lock_ahead_inverted_pct': round(f['shareLockAhead'], 1),
            'inversion_episodes': f['runs'], 'episodes_lock_ahead_majority': f['lockMajorityRuns'],
            'median_lock_vs_roll_inverted_pct': round(f['medianLockVsRollPct'], 2),
            'best_lock_vs_roll_inverted_pct': round(f['maxLockVsRollPct'], 2),
            'worst_lock_vs_roll_inverted_pct': round(f['minLockVsRollPct'], 2)}


def compare(got, ref):
    bad = [(k, got[k], ref[k]) for k in got if k in ref and got[k] != ref[k]]
    print(f'{len([k for k in got if k in ref])} so, {len(bad)} lệch', *bad, sep='\n  ')
    return not bad


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(EP))
    if '--retire3' in sys.argv:
        ref = {n['id']: n['value'] for n in json.load(open(os.path.join(root, 'topics-r1/machine/retire-3/result.json')))['numbers']}
        sys.exit(0 if compare(summary3(replay(RETIRE3)), ref) else 1)
    m = replay(RETIRE4)
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump(m, open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1)
    ref = json.loads(os.popen(f'cd {root}/topics-r1/machine/retire-4 && python3 calc.py --quantities').read())
    ok = compare(summary4(m), ref)
    print('C2:', extra4(m))
    sys.exit(0 if ok else 1)

"""Tập 6 (Việc 0): mô hình viết lại từ ĐỊNH NGHĨA trong topics-r1/machine/retire-1/result.json (không gọi, không chép calc.py),
cộng các đại lượng mở rộng của tập (nhân vật dẫn đường, theo thập kỷ, ngưỡng, độ vững CPI-W / PCE). History, not a forecast.

Cửa sổ H năm: tháng bắt đầu s ≥ 1947-01, tháng kết e = s + 12H; chỉ giữ khi chỉ số có giá trị ở cả s và e (ô trống bỏ qua:
CPIAUCNS 2025-10 trống). P = I(e)/I(s). Khoản trả tăng 2 %/năm sau H lần tăng: 1,02^H. Giữ sức mua ⇔ 1,02^H ≥ P.
Sức mua (% của khoản đầu): khoản 2 % = 100·1,02^H/P; khoản đều = 100/P. Lạm phát năm hoá = 100(P^(1/H) − 1).
Đường theo năm k = 0..H của một cửa sổ: khoản 2 % = 1,02^k / (I(s+12k)/I(s)) (lần tăng ở mỗi tháng kỷ niệm), khoản đều = 1/(I(s+12k)/I(s)).
    python3 episodes/ep006/model/model.py   → episodes/ep006/out/model.json {params, raw, rounded}"""
import json, os, statistics

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS = {
    'index': {'file': 'data/raw/CPIAUCNS.csv', 'dateColumn': 'observation_date', 'valueColumn': 'CPIAUCNS'},
    'robust': {'cpiw': {'file': 'data/raw/CWUR0000SA0.csv', 'valueColumn': 'CWUR0000SA0'},
               'pce': {'file': 'data/raw/PCEPI.csv', 'valueColumn': 'PCEPI'}},
    'raise': 0.02, 'horizonsYears': [20, 25], 'mainYears': 20, 'firstStart': '1947-01-01',
    'guide': {'start': '2006-08-01', 'age': 65, 'note': 'ILLUSTRATIVE retiree: latest complete 20-year window'},
    'raiseGrid': [0.02, 0.025, 0.03, 0.035, 0.04],
    'decades': [1940, 1950, 1960, 1970, 1980, 1990, 2000],
    'shareBands': [90, 75],
}


def load(rel):
    out = {}
    for line in open(os.path.join(EP, rel)).read().strip().splitlines()[1:]:
        d, v = line.split(',')[:2]
        if v not in ('', '.'):
            out[d] = float(v)
    return out


def addm(d, n):
    k = int(d[:4]) * 12 + int(d[5:7]) - 1 + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


def windows(idx, H, first='1947-01-01'):
    return [(s, addm(s, 12 * H), idx[addm(s, 12 * H)] / idx[s]) for s in sorted(idx) if s >= first and addm(s, 12 * H) in idx]


def run():
    I = load(PARAMS['index']['file'])
    g = 1 + PARAMS['raise']
    raw = {}
    last = max(I)
    raw['index_first_month'] = min(m for m in I if m >= PARAMS['firstStart'])
    raw['index_last_month'] = last
    raw['index_blank_months'] = sorted(m for m in (addm('1947-01-01', k) for k in range(0, 12 * 80)) if m <= last and m not in I)
    raw['cpi_yoy_latest_pct'] = 100 * (I[last] / I[addm(last, -12)] - 1)
    for H in PARAMS['horizonsYears']:
        w = windows(I, H)
        kept = [x for x in w if g ** H >= x[2]]
        r2 = [100 * g ** H / x[2] for x in w]
        lv = [100 / x[2] for x in w]
        inf = [100 * (x[2] ** (1 / H) - 1) for x in w]
        raw[f'windows_{H}y'] = len(w)
        raw[f'first_start_{H}y'] = w[0][0]
        raw[f'last_start_{H}y'] = w[-1][0]
        raw[f'windows_2pct_kept_up_{H}y'] = len(kept)
        raw[f'share_2pct_kept_up_{H}y_pct'] = 100 * len(kept) / len(w)
        raw[f'median_inflation_{H}y_pct_per_year'] = statistics.median(inf)
        raw[f'min_inflation_{H}y_pct_per_year'] = min(inf)
        raw[f'max_inflation_{H}y_pct_per_year'] = max(inf)
        raw[f'median_real_value_2pct_payment_after_{H}y_pct'] = statistics.median(r2)
        raw[f'median_real_value_level_payment_after_{H}y_pct'] = statistics.median(lv)
        wi = min(range(len(w)), key=lambda i: (r2[i], w[i][0]))
        raw[f'worst_real_value_2pct_payment_after_{H}y_pct'] = r2[wi]
        raw[f'worst_real_value_level_payment_after_{H}y_pct'] = lv[wi]
        raw[f'worst_window_start_{H}y'] = w[wi][0]
        raw[f'worst_window_start_year_{H}y'] = int(w[wi][0][:4])
        bi = max(range(len(w)), key=lambda i: (r2[i], -int(w[i][0].replace('-', ''))))
        raw[f'best_real_value_2pct_payment_after_{H}y_pct'] = r2[bi]
        raw[f'best_window_start_{H}y'] = w[bi][0]
        if kept:
            raw[f'kept_up_first_start_{H}y'] = kept[0][0]
            raw[f'kept_up_last_start_{H}y'] = kept[-1][0]
        else:
            raw[f'kept_up_first_start_{H}y'] = raw[f'kept_up_last_start_{H}y'] = None
        for b in PARAMS['shareBands']:
            raw[f'share_2pct_at_least_{b}_after_{H}y_pct'] = 100 * sum(x >= b for x in r2) / len(w)
        if H == PARAMS['mainYears']:
            W20, R2, LV = w, r2, lv
    H = PARAMS['mainYears']
    # latest complete window (ends at the last index month, or the last start whose end exists)
    lw = W20[-1]
    raw['latest_start'], raw['latest_end'] = lw[0], lw[1]
    raw['latest_window_real_value_2pct_payment_pct'] = 100 * g ** H / lw[2]
    raw['latest_window_real_value_level_payment_pct'] = 100 / lw[2]
    raw['latest_window_inflation_pct_per_year'] = 100 * (lw[2] ** (1 / H) - 1)
    raw['latest_window_price_rise_pct'] = 100 * (lw[2] - 1)
    raw['two_pct_growth_20y_pct'] = 100 * (g ** H - 1)
    # rank of latest window among all 20-year windows (by 2% real value; 1 = best)
    raw['latest_window_rank_2pct'] = 1 + sum(x > raw['latest_window_real_value_2pct_payment_pct'] + 1e-12 for x in R2)
    # guide character: year-by-year path
    gs = PARAMS['guide']['start']
    path = []
    for k in range(H + 1):
        m = addm(gs, 12 * k)
        p = I[m] / I[gs]
        path.append({'year': k, 'month': m, 'age': PARAMS['guide']['age'] + k, 'price_ratio': p,
                     'real_2pct_pct': 100 * g ** k / p, 'real_level_pct': 100 / p})
    raw['guide_path'] = path
    raw['guide_start'] = gs
    raw['guide_end'] = path[-1]['month']
    raw['guide_real_2pct_end_pct'] = path[-1]['real_2pct_pct']
    raw['guide_real_level_end_pct'] = path[-1]['real_level_pct']
    raw['guide_years_2pct_at_or_above_100'] = sum(1 for r in path[1:] if r['real_2pct_pct'] >= 100)
    raw['guide_last_year_2pct_at_or_above_100'] = max((r['year'] for r in path if r['real_2pct_pct'] >= 100), default=0)
    raw['guide_min_2pct_pct'] = min(r['real_2pct_pct'] for r in path)
    raw['guide_min_2pct_year'] = min(path, key=lambda r: (r['real_2pct_pct'], r['year']))['year']
    raw['guide_last_year_level_at_or_above_90'] = max(r['year'] for r in path if r['real_level_pct'] >= 90)
    # year when the level check fell to the 2% check's 20-year median end value (median over windows of the first such year)
    tgt = raw['median_real_value_2pct_payment_after_20y_pct']
    yrs = []
    for s, e, P in W20:
        y = next((k for k in range(1, H + 1) if 100 / (I[addm(s, 12 * k)] / I[s]) <= tgt), None)
        yrs.append(y if y is not None else H + 1)
    raw['median_year_level_reaches_2pct_end_median'] = statistics.median(yrs)
    # guide: year the level check first fell to the guide's own 2%-check end value
    raw['guide_year_level_reaches_2pct_end'] = next(r['year'] for r in path if r['real_level_pct'] <= raw['guide_real_2pct_end_pct'])
    # counterweight Carl (ILLUSTRATIVE, worst 20-year window): anniversaries k=1..H where the 2% check bought less than at k−1
    ws = raw['worst_window_start_20y']
    wr = [100 * g ** k / (I[addm(ws, 12 * k)] / I[ws]) for k in range(H + 1)]
    raw['worst_window_years_2pct_fell_20y'] = sum(1 for k in range(1, H + 1) if wr[k] < wr[k - 1])
    # by start decade
    dec = {}
    for (s, e, P), r in zip(W20, R2):
        d = int(s[:4]) // 10 * 10
        dec.setdefault(d, []).append((r, g ** H >= P, 100 * (P ** (1 / H) - 1)))
    raw['by_decade'] = {str(d): {'n': len(v), 'kept': sum(k for _, k, _ in v), 'median_real_2pct_pct': statistics.median(r for r, _, _ in v),
                                 'min_real_2pct_pct': min(r for r, _, _ in v), 'max_real_2pct_pct': max(r for r, _, _ in v),
                                 'median_inflation_pct': statistics.median(i for _, _, i in v)} for d, v in sorted(dec.items())}
    # raise grid: share of 20-year windows a fixed raise r kept up with
    raw['raise_grid'] = {f'{r:.3f}': 100 * sum((1 + r) ** H >= P for _, _, P in W20) / len(W20) for r in PARAMS['raiseGrid']}
    infl = sorted(100 * (P ** (1 / H) - 1) for _, _, P in W20)
    raw['raise_needed_all_20y_pct'] = infl[-1]          # keeps up in every window (≥)
    raw['raise_needed_half_20y_pct'] = statistics.median(infl)
    # robustness on other indexes
    for k, spec in PARAMS['robust'].items():
        J = load(spec['file'])
        w = windows(J, H)
        r2 = [100 * g ** H / P for _, _, P in w]
        raw[f'robust_{k}_windows_20y'] = len(w)
        raw[f'robust_{k}_first_start'] = w[0][0]
        raw[f'robust_{k}_last_start'] = w[-1][0]
        raw[f'robust_{k}_kept_up_20y'] = sum(g ** H >= P for _, _, P in w)
        raw[f'robust_{k}_share_kept_up_20y_pct'] = 100 * raw[f'robust_{k}_kept_up_20y'] / len(w)
        raw[f'robust_{k}_median_real_2pct_pct'] = statistics.median(r2)
        raw[f'robust_{k}_median_inflation_pct'] = statistics.median(100 * (P ** (1 / H) - 1) for _, _, P in w)
        lw2 = w[-1]
        raw[f'robust_{k}_latest_real_2pct_pct'] = 100 * g ** H / lw2[2]
    # CPI-U windows restricted to the PCE start (like-for-like)
    wp = [x for x in W20 if x[0] >= raw['robust_pce_first_start']]
    raw['cpiu_from_pce_start_windows_20y'] = len(wp)
    raw['cpiu_from_pce_start_kept_up_20y'] = sum(g ** H >= P for _, _, P in wp)
    raw['cpiu_from_pce_start_median_real_2pct_pct'] = statistics.median(100 * g ** H / P for _, _, P in wp)
    raw['windows'] = [{'start': s, 'end': e, 'P': P, 'real_2pct_pct': r, 'real_level_pct': l} for (s, e, P), r, l in zip(W20, R2, LV)]
    return raw


def rounded(raw):
    out = {}
    for k, v in raw.items():
        if isinstance(v, float):
            out[k] = round(v, 2) if 'inflation' in k or 'raise_needed' in k or 'yoy' in k else round(v, 1)
        elif k in ('windows', 'guide_path'):
            continue
        else:
            out[k] = v
    return out


if __name__ == '__main__':
    raw = run()
    json.dump({'params': PARAMS, 'raw': raw, 'rounded': rounded(raw)}, open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1)
    r = rounded(raw)
    print(json.dumps({k: v for k, v in r.items() if k not in ('by_decade',)}, indent=0)[:6000])
    print(json.dumps(r['by_decade']))
    print([(p['year'], p['month'], round(p['real_2pct_pct'], 1), round(p['real_level_pct'], 1)) for p in raw['guide_path']])

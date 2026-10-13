"""Tập 8 (Việc 0): thuê vs mua, phát lại mọi tháng mua từ 1991 — viết lại từ định nghĩa hồ sơ topics-r2/machine/rent-buy-1 (card, model.json,
claim-risk), không gọi calc.py. Đọc data/raw/*.csv (fetch.py). Ghi out/model.json {params, quantities{id: {value, unit, definition}}, sweep}.

    python3 episodes/ep008/model/model.py

Hai người ILLUSTRATIVE cùng tháng s, cùng tiền. Mua: nhà $400,000 theo chỉ số FHFA quốc gia (HPIPONM226N), 20 % cọc + 3 % phí mua, vay 30 năm
ở trung bình tháng s của lãi PMMS tuần, chi phí sở hữu 2,5 %/năm × giá trị hiện tại (tính tháng), phí bán 6 %. Thuê: tiền thuê năm đầu =
y(s) × $400,000, y(s) = y_neo × (CPI tiền thuê(s)/HPI(s)) / (CPI tiền thuê(neo)/HPI(neo)), neo 2026-07; tăng theo CPI tiền thuê.
Mỗi tháng cả hai chi bằng nhau: chênh (chi người mua − tiền thuê) cộng vào quỹ người thuê (khởi đầu 23 % giá), quỹ không lãi (biến thể T-bill).
Lợi thế người mua = 0,94 × giá trị cuối − dư nợ − quỹ. Độ nhạy (MỚI ở tập): quét y_neo 3,0–7,0 % → tỉ lệ cửa sổ người mua hơn, ngưỡng lật 50 %.
Neo tỉ lệ công khai: Census HVS (giá thuê hỏi / giá bán hỏi của nhà trống) — xem numbers.md, chỉ dùng làm dải đối chiếu cho y_neo.
"""
import csv, datetime, json, os, statistics as st

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(EP, 'data', 'raw')
P, DOWN, CLOSE, OWN, SELL, N = 400000.0, 0.20, 0.03, 0.025, 0.06, 360
ANCHOR, FIRST, Y0 = '2026-07', '1991-01', 0.05
ERAS = {'1990s': ('1991-01', '1999-12'), '2002-2007': ('2002-01', '2007-12'), '2009-2016': ('2009-01', '2016-07')}
HVS = {'2025Q4': (1464, 363800), '2026Q1': (1579, 339100)}   # Census HVS press releases (giá thuê hỏi/tháng, giá bán hỏi) — numbers.md


def mo(m, k):
    y, x = int(m[:4]), int(m[5:7]) - 1 + k
    return '%04d-%02d' % (y + x // 12, x % 12 + 1)


def series(sid):
    d = {}
    for r in csv.DictReader(open(os.path.join(RAW, sid + '.csv'))):
        v = r[sid].strip()
        if v not in ('', '.'):
            d[r['observation_date'][:7]] = d.get(r['observation_date'][:7], []) + [float(v)]
    return d


def load():
    hpi = {k: v[0] for k, v in series('HPIPONM226N').items()}
    cpi = {k: v[0] for k, v in series('CUUR0000SEHA').items()}
    tb = {k: v[0] for k, v in series('TB3MS').items()}
    w = series('MORTGAGE30US')
    rate = {k: sum(v) / len(v) for k, v in w.items()}
    lastw = max(r['observation_date'] for r in csv.DictReader(open(os.path.join(RAW, 'MORTGAGE30US.csv'))) if r['MORTGAGE30US'].strip() not in ('', '.'))
    d = datetime.date.fromisoformat(lastw)
    rml = lastw[:7] if (d + datetime.timedelta(7)).month != d.month else mo(lastw[:7], -1)
    gap = '2025-10'
    if gap not in cpi:
        cpi[gap] = (cpi[mo(gap, -1)] * cpi[mo(gap, 1)]) ** 0.5
    return hpi, cpi, tb, rate, rml, lastw


def run(s, H, D, y0=Y0, tbills=False, fixed=False):
    hpi, cpi, tb, rate = D
    r = rate[s] / 1200
    loan = P * (1 - DOWN)
    pay = loan * r / (1 - (1 + r) ** -N)
    y = y0 if fixed else y0 * (cpi[s] / hpi[s]) / (cpi[ANCHOR] / hpi[ANCHOR])
    rent0 = y * P / 12
    pot, bal = P * (DOWN + CLOSE), loan
    for k in range(12 * H):
        m = mo(s, k)
        out = pay + OWN / 12 * P * hpi[m] / hpi[s]
        pot += out - rent0 * cpi[m] / cpi[s]
        if tbills:
            pot *= 1 + tb[m] / 1200
        bal = bal * (1 + r) - pay
    e = mo(s, 12 * H)
    eq = (1 - SELL) * P * hpi[e] / hpi[s] - bal
    return {'s': s, 'adv': eq - pot, 'eq': eq, 'pot': pot, 'rate': rate[s], 'y': y, 'm1buy': pay + OWN / 12 * P, 'm1rent': rent0,
            'dp': hpi[e] / hpi[s] - 1, 'dr': cpi[e] / cpi[s] - 1}


def starts(H, D, tbills=False):
    hpi, cpi, tb, rate = D
    s, out = FIRST, []
    while mo(s, 12 * H) in hpi:
        ms = [mo(s, k) for k in range(12 * H + 1)]
        if s in rate and all(m in hpi and m in cpi for m in ms) and (not tbills or all(m in tb for m in ms[:-1])):
            out.append(s)
        s = mo(s, 1)
    return out


def main():
    hpi, cpi, tb, rate, rml, lastw = load()
    D = (hpi, cpi, tb, rate)
    q = {}

    def put(k, v, unit, dfn):
        q[k] = {'value': v, 'unit': unit, 'definition': dfn}
    put('hpi_last', max(hpi), 'month', 'Last month of the FHFA index file.')
    put('cpi_last', max(cpi), 'month', 'Last month of the CPI rent file.')
    put('tb_last', max(tb), 'month', 'Last month of the T-bill file.')
    put('rate_last_week', lastw, 'date', 'Last weekly PMMS date.')
    put('rate_month_latest', rml, 'month', 'Latest complete month of weekly rates.')
    put('rate_latest', round(rate[rml], 2), '%', 'Mean weekly 30-year rate in rate_month_latest.')
    W = {}
    for H in (5, 10, 15):
        ss = starts(H, D)
        w = [run(s, H, D) for s in ss]
        W[H] = w
        a = [x['adv'] for x in w]
        b, z = max(w, key=lambda x: x['adv']), min(w, key=lambda x: x['adv'])
        h = '%dy' % H
        put('n_' + h, len(w), 'windows', '%d-year windows from %s' % (H, FIRST))
        put('first_' + h, ss[0], 'month', 'first start')
        put('last_' + h, ss[-1], 'month', 'last start')
        put('share_buyer_ahead_' + h, round(100 * sum(x > 0 for x in a) / len(a), 1), '%', 'share of windows with buyer advantage > 0')
        put('median_adv_' + h, round(st.median(a)), 'USD', 'median buyer advantage')
        put('best_start_' + h, b['s'], 'month', 'start with largest advantage')
        put('best_adv_' + h, round(b['adv']), 'USD', 'largest advantage')
        put('worst_start_' + h, z['s'], 'month', 'start with smallest advantage')
        put('worst_adv_' + h, round(z['adv']), 'USD', 'smallest advantage')
        put('n_renter_ahead_' + h, sum(x <= 0 for x in a), 'windows', 'windows with advantage <= 0')
    w10 = {x['s']: x for x in W[10]}
    for t in ('best', 'worst'):
        x = w10[q[t + '_start_10y']['value']]
        put(t + '_rate_10y', round(x['rate'], 2), '%', 'start-month rate')
        put(t + '_price_change_10y', round(100 * x['dp'], 1), '%', 'index change over the window')
        put(t + '_rent_change_10y', round(100 * x['dr'], 1), '%', 'CPI rent change over the window')
        put(t + '_equity_10y', round(x['eq']), 'USD', 'buyer net equity at the end')
        put(t + '_pot_10y', round(x['pot']), 'USD', 'renter pot at the end')
    for k, (a0, a1) in ERAS.items():
        a = [x['adv'] for s, x in w10.items() if a0 <= s <= a1]
        put('era_%s_n' % k, len(a), 'windows', 'era windows')
        put('era_%s_share' % k, round(100 * sum(v > 0 for v in a) / len(a), 1), '%', 'era share buyer ahead')
        put('era_%s_median' % k, round(st.median(a)), 'USD', 'era median advantage')
    neg = sorted(s for s, x in w10.items() if x['adv'] <= 0)
    put('renter_first_10y', neg[0], 'month', 'first renter-ahead start')
    put('renter_last_10y', neg[-1], 'month', 'last renter-ahead start')
    put('yield_median_10y', round(100 * st.median(x['y'] for x in W[10]), 2), '%', 'median starting rent/price')
    put('yield_max_renter_ahead_10y', round(100 * max(w10[s]['y'] for s in neg), 2), '%', 'highest starting rent/price where renter ahead')
    put('yield_min_10y', round(100 * min(x['y'] for x in W[10]), 2), '%', 'lowest starting rent/price')
    put('yield_max_10y', round(100 * max(x['y'] for x in W[10]), 2), '%', 'highest starting rent/price')
    put('yield_first_10y', round(100 * W[10][0]['y'], 2), '%', 'starting rent/price of the first window')
    put('yield_worst_10y', round(100 * w10[q['worst_start_10y']['value']]['y'], 2), '%', 'starting rent/price of the worst window')
    ratio = [(100 * x['m1rent'] / x['m1buy'], x['s']) for x in W[10]]
    put('rent_to_outlay_min_10y', round(min(ratio)[0], 1), '%', 'lowest month-1 rent / buyer outlay')
    put('rent_to_outlay_min_start_10y', min(ratio)[1], 'month', 'start of that minimum')
    # today: buyer month 1 at rate_latest, rent at Y0 (anchor month)
    r = rate[rml] / 1200
    pay = P * (1 - DOWN) * r / (1 - (1 + r) ** -N)
    put('today_buyer_month1', round(pay + OWN / 12 * P), 'USD/month', 'month-1 buyer outlay at rate_latest')
    put('today_rent_month1', round(Y0 * P / 12), 'USD/month', 'month-1 rent at the anchor yield')
    put('today_rent_to_outlay', round(100 * (Y0 * P / 12) / (pay + OWN / 12 * P), 1), '%', 'ratio')
    tbs = starts(10, D, tbills=True)
    put('n_tbills_10y', len(tbs), 'windows', 'windows with T-bill data')
    put('share_tbills_10y', round(100 * sum(run(s, 10, D, tbills=True)['adv'] > 0 for s in tbs) / len(tbs), 1), '%', 'pot earns T-bill')
    put('share_fixedyield_10y', round(100 * sum(run(s, 10, D, fixed=True)['adv'] > 0 for s in starts(10, D)) / len(W[10]), 1), '%', 'fixed 5% every start')
    # sweep (MỚI): share buyer ahead (10y) vs anchor yield
    sw = []
    for i in range(30, 71, 2):
        y0 = i / 1000
        a = [run(s, 10, D, y0=y0)['adv'] > 0 for s in starts(10, D)]
        sw.append({'anchorYieldPct': round(100 * y0, 1), 'shareBuyerAhead10y': round(100 * sum(a) / len(a), 1)})
    for y0 in (0.04, 0.06):
        a = [run(s, 10, D, y0=y0)['adv'] > 0 for s in starts(10, D)]
        put('share_yield%dpct_10y' % round(100 * y0), round(100 * sum(a) / len(a), 1), '%', 'anchor yield %.0f%%' % (100 * y0))
    lo, hi = 0.01, 0.05
    for _ in range(40):
        mid = (lo + hi) / 2
        a = [run(s, 10, D, y0=mid)['adv'] > 0 for s in starts(10, D)]
        lo, hi = (lo, mid) if sum(a) / len(a) > 0.5 else (mid, hi)
    put('flip_yield_10y', round(100 * hi, 2), '%', 'anchor yield at which buyer-ahead share falls to 50% (10y)')
    for k, (rent, price) in HVS.items():
        y0 = 12 * rent / price
        a = [run(s, 10, D, y0=y0)['adv'] > 0 for s in starts(10, D)]
        put('hvs_yield_%s' % k, round(100 * y0, 2), '%', 'Census HVS 12 x median asking rent / median asking sales price, %s' % k)
        put('share_hvs_%s_10y' % k, round(100 * sum(a) / len(a), 1), '%', 'share buyer ahead with that anchor')
    put('price', P, 'USD', 'ILLUSTRATIVE price')
    put('yield_anchor_pct', 100 * Y0, '%', 'anchor yield (assumption)')
    put('anchor_month', ANCHOR, 'month', 'anchor month')
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump({'params': {'price': P, 'down': DOWN, 'closing': CLOSE, 'ownerCost': OWN, 'sell': SELL, 'term': N, 'anchor': ANCHOR, 'anchorYield': Y0},
               'quantities': q, 'sweep': sw}, open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1)
    print(len(q), 'đại lượng'); print(json.dumps(sw)); print({k: q[k]['value'] for k in q if 'flip' in k or 'hvs' in k})


if __name__ == '__main__':
    main()

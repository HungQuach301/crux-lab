"""Tập 9 (Việc 0): "nếu người thuê đầu tư phần chênh lệch" — cùng hai người ILLUSTRATIVE và cùng con phố 307 tháng mua của Tập 8
(định nghĩa Tập 8 giữ nguyên: episodes/ep008/model/model.py trên nhánh ep008), chỉ đổi MỘT điều: quỹ người thuê đầu tư vào cổ phiếu Mỹ
(tổng lợi nhuận, cổ tức tái đầu tư) thay vì để tiền mặt. Đọc data/raw/*.csv (fetch.py). Ghi out/model.json {params, quantities, sweep}.

    python3 episodes/ep009/model/model.py

Mua (như Tập 8): nhà $400,000 theo FHFA quốc gia, 20 % cọc + 3 % phí mua, vay 30 năm ở trung bình tháng s của PMMS, chi phí sở hữu
2,5 %/năm × giá trị hiện tại, phí bán 6 %. Thuê: tiền thuê năm đầu = y(s) × giá, y(s) neo 5 % ở 2026-07 kéo lùi theo CPI tiền thuê / HPI.
Mỗi tháng cả hai chi bằng nhau; chênh (chi người mua − tiền thuê, có thể âm) vào quỹ người thuê. Quỹ:
  cash    — không lãi (Tập 8);
  stocks  — đầu tháng nộp chênh, cả tháng hưởng tổng lợi nhuận thị trường Mỹ (Mkt-RF + RF của Fama/French, trước phí và thuế);
  lump    — chỉ $92,000 ban đầu vào cổ phiếu; chênh hằng tháng không ai để dành (người trả ít hơn tháng đó tiêu phần dư) — "không đầu tư phần chênh";
  stocks_fee — như stocks, trừ phí 1 %/năm (độ nhạy chi phí/thuế, không phải mô hình thuế).
Lợi thế người mua = 0,94 × giá trị nhà cuối − dư nợ − quỹ (> 0: người mua hơn).
"""
import csv, datetime, json, os, statistics as st

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(EP, 'data', 'raw')
P, DOWN, CLOSE, OWN, SELL, N = 400000.0, 0.20, 0.03, 0.025, 0.06, 360
ANCHOR, FIRST, Y0 = '2026-07', '1991-01', 0.05
ERAS = {'1990s': ('1991-01', '1999-12'), '2002-2007': ('2002-01', '2007-12'), '2009-2016': ('2009-01', '2016-07')}
HVS = {'2025Q4': (1464, 363800), '2026Q1': (1579, 339100)}   # Census HVS (Tập 8 numbers.md, đã xác minh trên PDF gốc)
MODES = ('cash', 'stocks', 'lump', 'stocks_fee')


def mo(m, k):
    y, x = int(m[:4]), int(m[5:7]) - 1 + k
    return '%04d-%02d' % (y + x // 12, x % 12 + 1)


def series(sid):
    d = {}
    for r in csv.DictReader(open(os.path.join(RAW, sid + '.csv'))):
        v = r[sid].strip()
        if v not in ('', '.'):
            d.setdefault(r['observation_date'][:7], []).append(float(v))
    return d


def french():
    """Tổng lợi nhuận tháng (số thập phân) = (Mkt-RF + RF)/100; chỉ khối tháng đầu tệp (trước dòng 'Annual')."""
    out = {}
    for l in open(os.path.join(RAW, 'ff3_monthly.csv'), encoding='latin-1'):
        if 'Annual' in l:
            break
        c = [x.strip() for x in l.split(',')]
        if len(c) >= 5 and len(c[0]) == 6 and c[0].isdigit():
            out[c[0][:4] + '-' + c[0][4:]] = (float(c[1]) + float(c[4])) / 100
    return out


def load():
    hpi = {k: v[0] for k, v in series('HPIPONM226N').items()}
    cpi = {k: v[0] for k, v in series('CUUR0000SEHA').items()}
    w = series('MORTGAGE30US')
    rate = {k: sum(v) / len(v) for k, v in w.items()}
    if '2025-10' not in cpi:   # BLS không công bố 10/2025 → trung bình nhân hai tháng kề (như Tập 8)
        cpi['2025-10'] = (cpi['2025-09'] * cpi['2025-11']) ** 0.5
    return hpi, cpi, rate, french()


def run(s, H, D, mode='cash', y0=Y0):
    hpi, cpi, rate, stk = D
    r = rate[s] / 1200
    loan = P * (1 - DOWN)
    pay = loan * r / (1 - (1 + r) ** -N)
    y = y0 * (cpi[s] / hpi[s]) / (cpi[ANCHOR] / hpi[ANCHOR])
    rent0 = y * P / 12
    pot, bal, spent, low = P * (DOWN + CLOSE), loan, 0.0, P * (DOWN + CLOSE)
    for k in range(12 * H):
        m = mo(s, k)
        diff = pay + OWN / 12 * P * hpi[m] / hpi[s] - rent0 * cpi[m] / cpi[s]
        if mode == 'lump':
            spent += diff
        else:
            pot += diff
        if mode != 'cash':
            pot *= 1 + stk[m] - (0.01 / 12 if mode == 'stocks_fee' else 0)
        low = min(low, pot)
        bal = bal * (1 + r) - pay
    e = mo(s, 12 * H)
    eq = (1 - SELL) * P * hpi[e] / hpi[s] - bal
    return {'s': s, 'adv': eq - pot, 'eq': eq, 'pot': pot, 'spent': spent, 'low': low, 'rate': rate[s], 'y': y,
            'stk': 1.0 if mode == 'cash' else None, 'dp': hpi[e] / hpi[s] - 1}


def growth(s, H, stk):
    g = 1.0
    for k in range(12 * H):
        g *= 1 + stk[mo(s, k)]
    return g


def starts(H, D):
    hpi, cpi, rate, stk = D
    s, out = FIRST, []
    while mo(s, 12 * H) in hpi:
        ms = [mo(s, k) for k in range(12 * H + 1)]
        if s in rate and all(m in hpi and m in cpi for m in ms) and all(m in stk for m in ms[:-1]):
            out.append(s)
        s = mo(s, 1)
    return out


def share(w):
    return round(100 * sum(x['adv'] > 0 for x in w) / len(w), 1)


def main():
    D = load()
    hpi, cpi, rate, stk = D
    q = {}

    def put(k, v, unit, dfn):
        q[k] = {'value': v, 'unit': unit, 'definition': dfn}
    put('hpi_last', max(hpi), 'month', 'Last month of the FHFA index file.')
    put('stocks_last', max(stk), 'month', 'Last month of the Fama/French monthly file.')
    put('stocks_first_used', FIRST, 'month', 'First month of stock returns used.')
    W = {}
    for H in (5, 10, 15):
        ss = starts(H, D)
        h = '%dy' % H
        put('n_' + h, len(ss), 'windows', '%d-year windows from %s' % (H, FIRST))
        put('last_' + h, ss[-1], 'month', 'last start')
        for md in MODES:
            w = [run(s, H, D, md) for s in ss]
            W[(H, md)] = w
            a = [x['adv'] for x in w]
            b, z = max(w, key=lambda x: x['adv']), min(w, key=lambda x: x['adv'])
            t = '%s_%s' % (md, h)
            put('share_buyer_ahead_' + t, share(w), '%', 'share of windows with buyer advantage > 0, renter pot = %s' % md)
            put('n_renter_ahead_' + t, sum(x <= 0 for x in a), 'windows', 'windows with advantage <= 0, pot = %s' % md)
            put('median_adv_' + t, round(st.median(a)), 'USD', 'median buyer advantage, pot = %s' % md)
            put('best_start_' + t, b['s'], 'month', 'start with largest buyer advantage, pot = %s' % md)
            put('best_adv_' + t, round(b['adv']), 'USD', 'largest buyer advantage, pot = %s' % md)
            put('worst_start_' + t, z['s'], 'month', 'start with smallest buyer advantage (best for renter), pot = %s' % md)
            put('worst_adv_' + t, round(z['adv']), 'USD', 'smallest buyer advantage, pot = %s' % md)
    c10, s10, l10 = ({x['s']: x for x in W[(10, m)]} for m in ('cash', 'stocks', 'lump'))
    ss = list(s10)
    # đổi phe: cửa sổ người mua hơn khi tiền mặt nhưng người thuê hơn khi cổ phiếu, và ngược lại
    put('n_flip_to_renter_10y', sum(c10[s]['adv'] > 0 >= s10[s]['adv'] for s in ss), 'windows', 'buyer ahead with cash pot, renter ahead with stock pot')
    put('n_flip_to_buyer_10y', sum(c10[s]['adv'] <= 0 < s10[s]['adv'] for s in ss), 'windows', 'renter ahead with cash pot, buyer ahead with stock pot')
    for k, (a0, a1) in ERAS.items():
        for md, w in (('cash', c10), ('stocks', s10), ('lump', l10)):
            a = [x['adv'] for s, x in w.items() if a0 <= s <= a1]
            put('era_%s_n' % k, len(a), 'windows', 'era windows')
            put('era_%s_share_%s' % (k, md), round(100 * sum(v > 0 for v in a) / len(a), 1), '%', 'era share buyer ahead, pot = %s' % md)
            put('era_%s_median_%s' % (k, md), round(st.median(a)), 'USD', 'era median buyer advantage, pot = %s' % md)
    # thị trường cổ phiếu theo cửa sổ 10 năm (để nói "stocks more than doubled" v.v.)
    g = {s: growth(s, 10, stk) for s in ss}
    gb, gw = max(g, key=g.get), min(g, key=g.get)
    put('stocks_growth_median_10y', round(st.median(g.values()), 2), 'x', 'median 10-year growth of $1 in US stocks (total return), over start months')
    put('stocks_growth_best_start_10y', gb, 'month', 'start with the largest 10-year stock growth')
    put('stocks_growth_best_10y', round(g[gb], 2), 'x', 'largest 10-year growth of $1')
    put('stocks_growth_worst_start_10y', gw, 'month', 'start with the smallest 10-year stock growth')
    put('stocks_growth_worst_10y', round(g[gw], 2), 'x', 'smallest 10-year growth of $1')
    put('n_stocks_lost_10y', sum(v < 1 for v in g.values()), 'windows', '10-year windows where $1 in stocks ended below $1')
    house = {s: hpi[mo(s, 120)] / hpi[s] for s in ss}
    put('n_stocks_beat_house_10y', sum(g[s] > house[s] for s in ss), 'windows', 'windows where 10-year stock growth > house index growth')
    put('share_stocks_beat_house_10y', round(100 * sum(g[s] > house[s] for s in ss) / len(ss), 1), '%', 'share of windows, stocks grew more than house index')
    # Tập 8 nối: tháng tệ nhất của người mua (6/2006) và tốt nhất (4/2012) khi quỹ ở cổ phiếu
    for s0 in ('2006-06', '2012-04', '2000-01', '1991-01'):
        for md, w in (('cash', c10), ('stocks', s10), ('lump', l10)):
            put('adv_%s_%s_10y' % (s0, md), round(w[s0]['adv']), 'USD', 'buyer advantage for start %s, pot = %s' % (s0, md))
        put('pot_%s_stocks_10y' % s0, round(s10[s0]['pot']), 'USD', 'renter stock pot at the end, start %s' % s0)
        put('pot_%s_cash_10y' % s0, round(c10[s0]['pot']), 'USD', 'renter cash pot at the end, start %s' % s0)
        put('equity_%s_10y' % s0, round(s10[s0]['eq']), 'USD', 'buyer net equity at the end, start %s' % s0)
        put('stocks_growth_%s_10y' % s0, round(g[s0], 2), 'x', '10-year growth of $1 in stocks from %s' % s0)
    put('min_pot_stocks_10y', round(min(x['low'] for x in W[(10, 'stocks')])), 'USD', 'lowest month-end stock pot in any window')
    put('n_pot_below_start_stocks_10y', sum(x['low'] < P * (DOWN + CLOSE) for x in W[(10, 'stocks')]), 'windows', 'windows where the stock pot dipped below $92,000 at some month-end')
    put('lump_monthly_spent_median_10y', round(st.median(x['spent'] for x in W[(10, 'lump')])), 'USD', 'median total monthly gap spent (not saved) over 10 years, lump variant')
    # độ nhạy: tỉ lệ thuê/giá neo 3–7 % với quỹ cổ phiếu
    sw = []
    for i in range(30, 71, 2):
        y0 = i / 1000
        sw.append({'anchorYieldPct': round(100 * y0, 1),
                   'cash': share([run(s, 10, D, 'cash', y0) for s in ss]),
                   'stocks': share([run(s, 10, D, 'stocks', y0) for s in ss])})
    for k, (rent, price) in HVS.items():
        y0 = 12 * rent / price
        put('hvs_yield_%s' % k, round(100 * y0, 2), '%', 'Census HVS 12 x median asking rent / median asking sales price, %s' % k)
        put('share_hvs_%s_stocks_10y' % k, share([run(s, 10, D, 'stocks', y0) for s in ss]), '%', 'share buyer ahead, stock pot, that anchor')
    lo, hi = 0.02, 0.12
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if sum(run(s, 10, D, 'stocks', mid)['adv'] > 0 for s in ss) / len(ss) > 0.5 else (mid, hi)
    put('flip_yield_stocks_10y', round(100 * hi, 2), '%', 'anchor yield at which buyer-ahead share (stock pot) falls to 50% (10y)')
    for k, v in (('price', P), ('savings_usd', round(P * (DOWN + CLOSE))), ('down_usd', round(P * DOWN)), ('closing_usd', round(P * CLOSE))):
        put(k, v, 'USD', 'model parameter (as Episode 8)')
    put('down_pct', 20, '%', 'down payment share'); put('closing_pct', 3, '%', 'closing cost share'); put('sell_pct', 6, '%', 'selling cost share')
    put('owner_cost_pct', 2.5, '% a year', 'property tax 1.0 + insurance 0.5 + repairs 1.0 (Episode 8 assumption)')
    put('yield_anchor_pct', 5.0, '%', 'anchor yield (assumption, Episode 8)'); put('fee_pct', 1.0, '% a year', 'fee/tax-drag variant stocks_fee')
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump({'params': {'price': P, 'down': DOWN, 'closing': CLOSE, 'ownerCost': OWN, 'sell': SELL, 'term': N, 'anchor': ANCHOR,
                          'anchorYield': Y0, 'modes': MODES},
               'quantities': q, 'sweep': sw,
               'windows10y': [{'s': s, 'cash': round(c10[s]['adv']), 'stocks': round(s10[s]['adv']), 'lump': round(l10[s]['adv']),
                               'stockGrowth': round(g[s], 3), 'houseGrowth': round(house[s], 3)} for s in ss]},
              open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1)
    print(len(q), 'đại lượng')


if __name__ == '__main__':
    main()

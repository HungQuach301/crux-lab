"""tax-3: an investor 11 months into a $50,000 index position with a $10,000 gain: sell now (short-term, taxed at the
24% bracket rate) or wait about one month (21 trading days) for the 15% long-term rate. Over every 21-trading-day
window of the S&P 500 price index in the pinned file, how often did waiting leave less after federal tax?
Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
V, G = 50000.0, 10000.0   # position value and unrealized gain (viewer identity)
C = V - G                 # cost basis
LT = 0.15                 # long-term rate for a taxpayer whose taxable income is in the 22%/24% brackets
WAIT = 21                 # trading days (about one calendar month)

px = []
for row in list(csv.reader(open(os.path.join(D, 'SP500.csv'))))[1:]:
    if len(row) > 1 and row[1] not in ('', '.'):
        px.append((row[0], float(row[1])))
ratios = [px[i + WAIT][1] / px[i][1] for i in range(len(px) - WAIT)]


def after_tax_wait(x):
    v1 = V * x
    gain = v1 - C
    return v1 - LT * gain if gain > 0 else v1  # a loss is given no tax value (conservative)


def stats(st):
    now = V - st * G
    be = (now - LT * C) / ((1 - LT) * V)  # ratio at which waiting and selling now leave the same amount
    diffs = sorted(after_tax_wait(x) - now for x in ratios)
    n = len(diffs)
    return {
        'now': now, 'breakeven_drop_pct': (1 - be) * 100,
        'share_wait_worse_pct': 100 * sum(1 for d in diffs if d < 0) / n,
        'median_diff': diffs[n // 2] if n % 2 else (diffs[n // 2 - 1] + diffs[n // 2]) / 2,
        'p05_diff': diffs[int(0.05 * (n - 1))],
        'worst_diff': diffs[0], 'n': n,
    }


s24, s22 = stats(0.24), stats(0.22)
worst_i = min(range(len(ratios)), key=lambda i: ratios[i])
out = {
    'tax_saving_if_flat_usd_24': round((0.24 - LT) * G, 2),
    'after_tax_sell_now_usd_24': round(s24['now'], 2),
    'breakeven_drop_pct_24': round(s24['breakeven_drop_pct'], 3),
    'windows_n': s24['n'],
    'first_window_start': px[0][0],
    'last_window_start': px[len(ratios) - 1][0],
    'share_wait_worse_pct_24': round(s24['share_wait_worse_pct'], 2),
    'median_wait_minus_now_usd_24': round(s24['median_diff'], 2),
    'p05_wait_minus_now_usd_24': round(s24['p05_diff'], 2),
    'worst_wait_minus_now_usd_24': round(s24['worst_diff'], 2),
    'worst_window_start': px[worst_i][0],
    'worst_window_index_change_pct': round((ratios[worst_i] - 1) * 100, 2),
    'breakeven_drop_pct_22': round(s22['breakeven_drop_pct'], 3),
    'share_wait_worse_pct_22': round(s22['share_wait_worse_pct'], 2),
    'share_index_down_pct': round(100 * sum(1 for x in ratios if x < 1) / len(ratios), 2),
}
print(json.dumps(out))

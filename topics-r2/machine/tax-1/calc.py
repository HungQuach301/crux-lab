"""tax-1: 10-year TIPS held in a taxable account (24% federal bracket) vs inside an IRA (no annual tax), every purchase
month 2003-01 .. 2016-11, using the monthly 10-year TIPS real yield (FII10) and CPI-U NSA (CPIAUCNS) with the 3-month
indexation lag. Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os, statistics

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
T = 0.24          # federal bracket (viewer identity)
FLOOR = 0.125     # minimum TIPS coupon, percent


def series(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0][:7]] = float(row[1])
    return out


def add(m, k):
    y, mo = int(m[:4]), int(m[5:7]) - 1 + k
    return f'{y + mo // 12}-{mo % 12 + 1:02d}'


fii, cpi = series('FII10'), series('CPIAUCNS')
ref = lambda m: cpi[add(m, -3)]          # reference CPI for month m = CPI three months earlier

rows, skipped = [], []
m = '2003-01'
last_cpi = max(cpi)
while add(m, 117) <= last_cpi and m in fii:
    if any(add(m, 12 * k - 3) not in cpi for k in range(11)):   # October 2025 CPI was never published
        skipped.append(m)
        m = add(m, 1)
        continue
    y = fii[m] / 100
    w_tax, w_ira, infl = 1.0, 1.0, 1.0
    for k in range(10):
        f = ref(add(m, 12 * (k + 1))) / ref(add(m, 12 * k))
        g = (1 + y) * f
        w_tax *= 1 + (1 - T) * (g - 1)
        w_ira *= g
        infl *= f
    r_tax = (w_tax / infl) ** 0.1 - 1
    r_ira = (w_ira / infl) ** 0.1 - 1
    rows.append((m, y, r_tax, r_ira, w_tax / infl, w_ira / infl))
    m = add(m, 1)

gaps = [(r[3] - r[2]) * 100 for r in rows]
neg = [r for r in rows if r[2] < 0]
worst = min(rows, key=lambda r: r[2])
best = max(rows, key=lambda r: r[2])
neg_ira = [r for r in rows if r[3] < 0]

# calendar-year cash check: holder of $10,000 inflation-adjusted principal bought each January at that month's yield
years = [yr for yr in range(2003, 2026) if add(f'{yr + 1}-01', -3) in cpi and add(f'{yr}-01', -3) in cpi]
phantom = 0
for yr in years:
    c = max(fii[f'{yr}-01'], FLOOR) / 100
    a = ref(f'{yr + 1}-01') / ref(f'{yr}-01') - 1
    tax = T * 10000 * (c + a)
    if tax > 10000 * c:
        phantom += 1
a22 = ref('2023-01') / ref('2022-01') - 1
c22 = max(fii['2022-01'], FLOOR) / 100

out = {
    'windows': len(rows),
    'windows_skipped_missing_cpi': len(skipped),
    'first_purchase': rows[0][0],
    'last_purchase': rows[-1][0],
    'taxable_negative_real_count': len(neg),
    'taxable_negative_real_share_pct': round(100 * len(neg) / len(rows), 1),
    'ira_negative_real_count': len(neg_ira),
    'median_gap_pctpts': round(statistics.median(gaps), 2),
    'max_gap_pctpts': round(max(gaps), 2),
    'min_gap_pctpts': round(min(gaps), 2),
    'worst_taxable_real_pct': round(worst[2] * 100, 2),
    'worst_purchase_month': worst[0],
    'worst_ira_real_pct': round(worst[3] * 100, 2),
    'best_taxable_real_pct': round(best[2] * 100, 2),
    'best_purchase_month': best[0],
    'median_end_real_usd_taxable': round(10000 * statistics.median(r[4] for r in rows), 0),
    'median_end_real_usd_ira': round(10000 * statistics.median(r[5] for r in rows), 0),
    'inflation_accrual_2022_pct': round(a22 * 100, 2),
    'tax_2022_usd': round(T * 10000 * (c22 + a22), 2),
    'coupon_cash_2022_usd': round(10000 * c22, 2),
    'phantom_years': phantom,
    'phantom_years_total': len(years),
}
print(json.dumps(out))

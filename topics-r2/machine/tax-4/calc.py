"""tax-4: $7,500 of cash earning the 3-month T-bill rate (TB3MS, monthly) inside a Roth IRA (no tax) vs in a taxable
savings account (22% federal tax on each calendar year's interest, paid from the balance), measured in real terms with
CPI-U NSA (CPIAUCNS). Ten-year windows starting each January 1934 .. 2016, and single calendar years 1934 .. 2025.
Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os, statistics

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
P = 7500.0
T = 0.22


def series(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0][:7]] = float(row[1])
    return out


tb, cpi = series('TB3MS'), series('CPIAUCNS')


def year_growth(y):
    g = 1.0
    for mo in range(1, 13):
        g *= 1 + tb[f'{y}-{mo:02d}'] / 100 / 12
    return g


def window(y0):
    roth, taxable = P, P
    for y in range(y0, y0 + 10):
        g = year_growth(y)
        roth *= g
        taxable *= 1 + (1 - T) * (g - 1)
    defl = cpi[f'{y0}-01'] / cpi[f'{y0 + 10}-01']
    return roth * defl, taxable * defl


starts = list(range(1934, 2017))
w = {y: window(y) for y in starts}
roth_loss = [y for y in starts if w[y][0] < P]
tax_loss = [y for y in starts if w[y][1] < P]
diff = [w[y][0] - w[y][1] for y in starts]

years = list(range(1934, 2026))
beat_pre = beat_post = 0
for y in years:
    g = year_growth(y) - 1
    infl = cpi[f'{y}-12'] / cpi[f'{y - 1}-12'] - 1
    beat_pre += g > infl
    beat_post += (1 - T) * g > infl

out = {
    'windows': len(starts),
    'roth_real_loss_windows': len(roth_loss),
    'taxable_real_loss_windows': len(tax_loss),
    'roth_real_loss_share_pct': round(100 * len(roth_loss) / len(starts), 1),
    'taxable_real_loss_share_pct': round(100 * len(tax_loss) / len(starts), 1),
    'median_real_end_roth_usd': round(statistics.median(v[0] for v in w.values()), 2),
    'median_real_end_taxable_usd': round(statistics.median(v[1] for v in w.values()), 2),
    'median_diff_usd': round(statistics.median(diff), 2),
    'max_diff_usd': round(max(diff), 2),
    'max_diff_start': starts[diff.index(max(diff))],
    'latest_start': starts[-1],
    'latest_real_end_roth_usd': round(w[starts[-1]][0], 2),
    'latest_real_end_taxable_usd': round(w[starts[-1]][1], 2),
    'calendar_years': len(years),
    'years_beat_inflation_untaxed': beat_pre,
    'years_beat_inflation_after_tax': beat_post,
}
print(json.dumps(out))

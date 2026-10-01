"""tax-1: what a $3,000 federal refund built from over-withholding costs in forgone interest (or extra card interest),
tax years 2000-2025, using monthly 3-month T-bill yields, the national average savings rate and the average credit
card APR. Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
R = 3000.0  # refund (viewer identity)


def series(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0][:7]] = float(row[1])  # 'YYYY-MM' -> percent per year
    return out


def ffill(s, months):
    """value for each month = latest observation at or before that month (quarterly card series)"""
    keys = sorted(s)
    res = {}
    for m in months:
        prior = [k for k in keys if k <= m]
        res[m] = s[prior[-1]] if prior else None
    return res


def window(y):
    """months Feb of tax year y .. Feb of y+1, with the over-withheld balance outstanding during each month.
    R/12 is over-withheld at the end of each month Jan..Dec of y; the refund arrives March 1 of y+1."""
    out = []
    for k in range(1, 14):  # Feb y (k=1) ... Feb y+1 (k=13)
        mi = k + 1  # month index 2..14
        yy, mm = (y, mi) if mi <= 12 else (y + 1, mi - 12)
        bal = R * min(k, 12) / 12
        out.append((f'{yy}-{mm:02d}', bal))
    return out


def lost(y, rates):
    return sum(bal * rates[m] / 100 / 12 for m, bal in window(y))


tb = series('TB3MS')
cc_raw = series('TERMCBCCALLNS')
sv = series('SNDR')
years = list(range(2000, 2026))
all_months = sorted({m for y in years for m, _ in window(y)})
cc = ffill(cc_raw, all_months)

tb_by_year = {y: lost(y, tb) for y in years}
cc_by_year = {y: lost(y, cc) for y in years}
tb_max_year = max(tb_by_year, key=tb_by_year.get)
tb_min_year = min(tb_by_year, key=tb_by_year.get)

out = {
    'balance_months_per_dollar': round(sum(b for _, b in window(2025)) / R, 4),
    'tbill_2025_usd': round(tb_by_year[2025], 2),
    'savings_avg_2025_usd': round(lost(2025, sv), 2),
    'card_2025_usd': round(cc_by_year[2025], 2),
    'tbill_mean_2000_2025_usd': round(sum(tb_by_year.values()) / len(years), 2),
    'tbill_max_usd': round(tb_by_year[tb_max_year], 2),
    'tbill_max_year': tb_max_year,
    'tbill_min_usd': round(tb_by_year[tb_min_year], 2),
    'tbill_min_year': tb_min_year,
    'tbill_years_under_10usd': sum(1 for v in tb_by_year.values() if v < 10),
    'card_mean_2000_2025_usd': round(sum(cc_by_year.values()) / len(years), 2),
    'card_min_usd': round(min(cc_by_year.values()), 2),
    'card_max_usd': round(max(cc_by_year.values()), 2),
}
print(json.dumps(out))

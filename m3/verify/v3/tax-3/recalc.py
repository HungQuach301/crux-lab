import csv, json
def load(p):
    rows=list(csv.reader(open(p)))[1:]
    return [(d, float(v)) for d, v in rows if v not in ('', '.')]
cpi = load('data/CPIAUCSL.csv')
cpi = [r for r in cpi if r[0] <= '2026-08-01']
last12 = cpi[-12:]
assert last12[0][0] == '2025-09-01' and last12[-1][0] == '2026-08-01', (last12[0], last12[-1])
y09 = [v for d, v in cpi if d.startswith('2009-')]
assert len(y09) == 12
f = (sum(v for _, v in last12) / 12) / (sum(y09) / 12)
inc = load('data/MEHOINUSA646N.csv')
m09 = [v for d, v in inc if d.startswith('2009-')][0]
latest_d, mlat = inc[-1]
# Statute 25A(b)(1),(d)(1): max 2000 + 25% x 2000 = 2500; joint phase-out 160000 over 20000
def credit(magi):
    return 2500 * max(0, min(1, (180000 - magi) / 20000))
grown = round(160000 * mlat / m09)
out = {
 'cpi_factor_2009_to_last12': f,
 'start_160k_in_current_prices_usd': round(160000 * f),
 'end_180k_in_current_prices_usd': round(180000 * f),
 'max_credit_2500_in_current_prices_usd': round(2500 * f),
 'credit_for_that_couple_now_usd': credit(160000 * f),
 'couple_160k_2009_grown_with_median_income_usd': grown,
 'credit_for_median_growth_couple_now_usd': credit(grown),
 'start_as_multiple_of_median_income_2009': round(160000 / m09, 2),
 'start_as_multiple_of_median_income_latest': round(160000 / mlat, 2),
 'median_income_latest_year': int(latest_d[:4]),
}
print(json.dumps(out, indent=1))

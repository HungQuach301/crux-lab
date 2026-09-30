import csv, json, os, sys
IDS = ['cpi_factor_2009_to_last12','start_160k_in_current_prices_usd','end_180k_in_current_prices_usd',
 'max_credit_2500_in_current_prices_usd','credit_for_that_couple_now_usd','couple_160k_2009_grown_with_median_income_usd',
 'credit_for_median_growth_couple_now_usd','start_as_multiple_of_median_income_2009',
 'start_as_multiple_of_median_income_latest','median_income_latest_year']
if not (os.path.exists('data/CPIAUCSL.csv') and os.path.exists('data/MEHOINUSA646N.csv')):
    # FRED series could not be downloaded; every number depends on them
    print(json.dumps({i: None for i in IDS}, indent=1)); sys.exit(0)
def load(p):
    rows=list(csv.reader(open(p)))[1:]
    return [(d, float(v)) for d, v in rows if v not in ('', '.')]
cpi = load('data/CPIAUCSL.csv')
cpi = [r for r in cpi if r[0] <= '2026-08-01']
# Window pinned by the definition/assumption: the 12 calendar months Sep 2025-Aug 2026.
# FRED has no value for 2025-10 (blank row), so the mean is over the 11 available values.
last12 = [r for r in cpi if '2025-09-01' <= r[0] <= '2026-08-01']
assert len(last12) == 11 and last12[-1][0] == '2026-08-01'
y09 = [v for d, v in cpi if d.startswith('2009-')]
assert len(y09) == 12
f = (sum(v for _, v in last12) / len(last12)) / (sum(y09) / 12)
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

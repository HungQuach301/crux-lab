"""tax-3: the college tax credits' income phase-out ($160,000-$180,000 joint, $80,000-$90,000 single) and the $2,500 maximum
credit are fixed dollar amounts, the same since tax year 2009 for the American Opportunity credit. Reads data/ only."""
import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load(sid):
    rows = [r for r in csv.reader(open(os.path.join(D, sid + '.csv')))][1:]
    return {r[0]: float(r[1]) for r in rows if r[1] not in ('', '.')}

cpi = load('CPIAUCSL')
inc = load('MEHOINUSA646N')
avg2009 = sum(v for k, v in cpi.items() if k.startswith('2009-')) / 12
last12 = sum(cpi[k] for k in sorted(cpi)[-12:]) / 12
f = last12 / avg2009
m2009, m_last = inc['2009-01-01'], inc[sorted(inc)[-1]]
g = m_last / m2009

def aotc(magi_joint, full=2500.0):
    """American Opportunity credit for a joint return with full qualifying expenses ($4,000+)."""
    return full * max(0.0, min(1.0, (180000 - magi_joint) / 20000))

out = {
    'cpi_factor_2009_to_last12': round(f, 4),
    'start_160k_in_current_prices_usd': round(160000 * f, 0),
    'end_180k_in_current_prices_usd': round(180000 * f, 0),
    'max_credit_2500_in_current_prices_usd': round(2500 * f, 0),
    'credit_for_that_couple_now_usd': round(aotc(160000 * f), 2),
    'couple_160k_2009_grown_with_median_income_usd': round(160000 * g, 0),
    'credit_for_median_growth_couple_now_usd': round(aotc(160000 * g), 2),
    'start_as_multiple_of_median_income_2009': round(160000 / m2009, 2),
    'start_as_multiple_of_median_income_latest': round(160000 / m_last, 2),
    'median_income_latest_year': int(sorted(inc)[-1][:4]),
}
print(json.dumps(out))

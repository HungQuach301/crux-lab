"""tax-5: the home-sale gain exclusion ($250,000 single / $500,000 joint) has been a fixed dollar amount since 1997.
Gain today on a home bought at the national median new-home price in each past quarter, grown with a repeat-sales
home price index. Reads data/ only; prints {id: value}."""
import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load(sid):
    rows = [r for r in csv.reader(open(os.path.join(D, sid + '.csv')))][1:]
    return {r[0]: float(r[1]) for r in rows if r[1] not in ('', '.')}

msp, cs, cpi = load('MSPUS'), load('CSUSHPINSA'), load('CPIAUCSL')
cs_now_date = sorted(cs)[-1]
cs_now = cs[cs_now_date]

def q_months(qdate):
    y, m = int(qdate[:4]), int(qdate[5:7])
    return [f'{y}-{m + k:02d}-01' for k in range(3)]

gain = {}
for q, p in msp.items():
    ms = q_months(q)
    if all(m in cs for m in ms):
        c = sum(cs[m] for m in ms) / 3
        gain[q] = p * (cs_now / c - 1)

def last_quarter_over(x):
    over = [q for q, g in gain.items() if g > x]
    return max(over) if over else None

cpi1997 = sum(v for k, v in cpi.items() if k.startswith('1997-')) / 12
cpi_last12 = sum(cpi[k] for k in sorted(cpi)[-12:]) / 12
msp1997 = sum(v for k, v in msp.items() if k.startswith('1997-')) / 4
latest_q = sorted(msp)[-1]

out = {
    'last_purchase_year_gain_over_250k': int(last_quarter_over(250000)[:4]),
    'last_purchase_quarter_of_that_year': (int(last_quarter_over(250000)[5:7]) - 1) // 3 + 1,
    'quarters_gain_over_500k': sum(1 for g in gain.values() if g > 500000),
    'gain_median_bought_1997q3_usd': round(gain['1997-07-01'], 0),
    'gain_median_bought_2000q1_usd': round(gain['2000-01-01'], 0),
    'taxable_gain_single_bought_1997q3_usd': round(max(0, gain['1997-07-01'] - 250000), 0),
    'tax_at_15pct_single_bought_1997q3_usd': round(0.15 * max(0, gain['1997-07-01'] - 250000), 0),
    'quarters_gain_over_250k': sum(1 for g in gain.values() if g > 250000),
    'quarters_total': len(gain),
    'max_gain_any_quarter_usd': round(max(gain.values()), 0),
    'exclusion_250k_in_current_prices_usd': round(250000 * cpi_last12 / cpi1997, 0),
    'exclusion_to_median_price_1997': round(250000 / msp1997, 2),
    'exclusion_to_median_price_latest': round(250000 / msp[latest_q], 2),
}
print(json.dumps(out))

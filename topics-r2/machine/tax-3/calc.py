"""tax-3: the rental-loss allowance ($25,000, reduced by half of income above $100,000, gone at $150,000), unchanged since
its first tax year (1987), measured against prices (CPI-U NSA, annual average of published months) and median household
income (current dollars), 1987 vs 2025; and what it leaves a couple with $130,000 of income.
Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
START, END = 100000.0, 150000.0
CAP = 25000.0
INCOME = 130000.0   # couple (viewer identity)


def rows(name):
    return [(r[0], float(r[1])) for r in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]
            if len(r) > 1 and r[1] not in ('', '.')]


def cpi_avg(year):
    v = [x for d, x in rows('CPIAUCNS') if d.startswith(str(year))]
    return sum(v) / len(v), len(v)


def allowance(magi, start=START, cap=CAP):
    return max(0.0, cap - 0.5 * max(0.0, magi - start))


med = {d[:4]: x for d, x in rows('MEHOINUSA646N')}
c87, n87 = cpi_avg(1987)
c25, n25 = cpi_avg(2025)
k = c25 / c87
out = {
    'cpi_1987_avg': round(c87, 3),
    'cpi_2025_avg': round(c25, 3),
    'cpi_2025_months': n25,
    'price_factor_1987_2025': round(k, 4),
    'start_in_2025_dollars': round(START * k, -2),
    'end_in_2025_dollars': round(END * k, -2),
    'cap_in_2025_dollars': round(CAP * k, -2),
    'start_real_value_pct_of_1987': round(100 / k, 1),
    'median_1987': med['1987'],
    'median_2025': med['2025'],
    'start_over_median_1987': round(START / med['1987'], 2),
    'start_over_median_2025': round(START / med['2025'], 2),
    'end_over_median_2025': round(END / med['2025'], 2),
    'start_if_tracked_median_2025': round(START * med['2025'] / med['1987'], -2),
    'income_in_1987_dollars': round(INCOME / k, -2),
    'allowance_at_income': allowance(INCOME),
    'allowance_at_income_if_cpi_indexed': round(allowance(INCOME, START * k, CAP * k), -2),
}
print(json.dumps(out))

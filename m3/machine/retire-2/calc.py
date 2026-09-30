"""retire-2: purchasing power lost to the timing lag of Social Security cost-of-living increases. Reads data/ only."""
import csv, json
w = {r[0]: float(r[1]) for r in list(csv.reader(open('data/CWUR0000SA0.csv')))[1:] if r[1] not in ('', '.')}
def q3(y): return sum(w[f'{y}-{m:02d}-01'] for m in (7, 8, 9)) / 3
base, cola, last_comp = 1983, {}, {}
for y in range(1984, 2024):
    p = round((q3(y) / q3(base) - 1) * 100, 1)
    cola[y] = p if p > 0 else 0.0
    if p > 0: base = y
    last_comp[y] = base          # base quarter year in force for benefits paid in year y+1
def shortfall(Y):
    b = last_comp[Y - 1]
    return [1 - q3(b) / w[f'{Y}-{m:02d}-01'] for m in range(1, 13)]
years = range(1985, 2025)
tot = sum(sum(shortfall(Y)) for Y in years)
out = {
    'cola_2021_pct': cola[2021], 'cola_2022_pct': cola[2022],
    'shortfall_2022_avg_pct': round(sum(shortfall(2022)) / 12 * 100, 2),
    'shortfall_2022_months': round(sum(shortfall(2022)), 3),
    'shortfall_2021_2023_months': round(sum(sum(shortfall(Y)) for Y in (2021, 2022, 2023)), 3),
    'cumulative_1985_2024_months': round(tot, 2),
    'avg_annual_shortfall_1985_2024_pct': round(tot / (12 * len(years)) * 100, 2),
    'years_retirees_ahead_1985_2024': sum(1 for Y in years if sum(shortfall(Y)) < 0),
}
print(json.dumps(out))

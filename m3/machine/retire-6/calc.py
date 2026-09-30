"""retire-6: how unstable is the income from living only on the interest of 3-month Treasury bills. Reads data/ only."""
import csv, json
t = {r[0]: float(r[1]) for r in list(csv.reader(open('data/TB3MS.csv')))[1:] if r[1] not in ('', '.')}
ann = {}
for y in range(1934, 2026):
    v = [t.get(f'{y}-{m:02d}-01') for m in range(1, 13)]
    if all(x is not None for x in v): ann[y] = sum(v) / 12
elig = [y for y in ann if y + 2 in ann and y + 1 in ann]
halved = [y for y in elig if min(ann[y + 1], ann[y + 2]) < 0.5 * ann[y]]
out = {
    'yield_2007_pct': round(ann[2007], 3), 'yield_2009_pct': round(ann[2009], 3),
    'income_drop_2007_2009_pct': round((1 - ann[2009] / ann[2007]) * 100, 1),
    'yield_2019_pct': round(ann[2019], 3), 'yield_2021_pct': round(ann[2021], 3),
    'income_drop_2019_2021_pct': round((1 - ann[2021] / ann[2019]) * 100, 1),
    'years_below_quarter_point_2009_2015': sum(1 for y in range(2009, 2016) if ann[y] < 0.25),
    'years_below_quarter_point_all': sum(1 for y in ann if ann[y] < 0.25),
    'years_in_sample': len(ann),
    'eligible_start_years': len(elig),
    'years_income_halved_within_two': len(halved),
    'yield_2024_pct': round(ann[2024], 3),
}
print(json.dumps(out))

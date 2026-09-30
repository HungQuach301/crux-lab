import csv, json
from collections import defaultdict
vals = defaultdict(list)
with open("data/TB3MS.csv") as f:
    for row in csv.DictReader(f):
        v = row["TB3MS"].strip()
        if v in ("", "."):
            continue
        vals[int(row["observation_date"][:4])].append(float(v))
complete = {y: sum(v)/len(v) for y, v in vals.items() if len(v) == 12}
m = lambda y: complete[y]
out = {}
out["yield_2007_pct"] = m(2007)
out["yield_2009_pct"] = m(2009)
out["income_drop_2007_2009_pct"] = (1 - m(2009)/m(2007))*100
out["yield_2019_pct"] = m(2019)
out["yield_2021_pct"] = m(2021)
out["income_drop_2019_2021_pct"] = (1 - m(2021)/m(2019))*100
out["years_below_quarter_point_2009_2015"] = sum(1 for y in range(2009, 2016) if y in complete and m(y) < 0.25)
sample = [y for y in range(1934, 2026) if y in complete]
out["years_below_quarter_point_all"] = sum(1 for y in sample if m(y) < 0.25)
out["years_in_sample"] = len(sample)
elig = [y for y in range(1934, 2024) if all(z in complete for z in (y, y+1, y+2))]
out["eligible_start_years"] = len(elig)
out["years_income_halved_within_two"] = sum(1 for y in elig if min(m(y+1), m(y+2)) < 0.5*m(y))
out["yield_2024_pct"] = m(2024)
print(json.dumps(out, indent=1))

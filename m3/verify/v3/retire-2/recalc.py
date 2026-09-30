import csv, json
from decimal import Decimal, ROUND_HALF_UP

cpi = {}
with open("data/CWUR0000SA0.csv") as f:
    for row in csv.DictReader(f):
        v = row["CWUR0000SA0"].strip()
        if v and v != ".":
            y, m, _ = row["observation_date"].split("-")
            cpi[(int(y), int(m))] = float(v)

def Q3(y):
    return sum(cpi[(y, m)] for m in (7, 8, 9)) / 3.0

def round1(x):  # round half up to 0.1 (legal "nearest one-tenth")
    return float(Decimal(repr(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

# COLA chain
cola = {}
base = 1983
base_for_year = {}          # base in force after determination in year y
positive_years = [1983]
for y in range(1984, 2024):
    c = round1((Q3(y) / Q3(base) - 1) * 100)
    cola[y] = c
    if c > 0:
        base = y
        positive_years.append(y)

def base_for_payment(Y):
    return max(b for b in positive_years if b <= Y - 1)

def month_short(Y, m):
    return 1 - Q3(base_for_payment(Y)) / cpi[(Y, m)]

def year_sum(Y):
    return sum(month_short(Y, m) for m in range(1, 13))

s2022 = year_sum(2022)
cum = sum(year_sum(Y) for Y in range(1985, 2025))
out = {
    "cola_2021_pct": cola[2021],
    "cola_2022_pct": cola[2022],
    "shortfall_2022_avg_pct": s2022 / 12 * 100,
    "shortfall_2022_months": s2022,
    "shortfall_2021_2023_months": sum(year_sum(Y) for Y in (2021, 2022, 2023)),
    "cumulative_1985_2024_months": cum,
    "avg_annual_shortfall_1985_2024_pct": cum / 480 * 100,
    "years_retirees_ahead_1985_2024": sum(1 for Y in range(1985, 2025) if year_sum(Y) < 0),
}
print(json.dumps(out, indent=1))

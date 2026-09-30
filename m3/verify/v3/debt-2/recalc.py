import csv, json, statistics

def load(s):
    d = {}
    with open(f"data/{s}.csv") as f:
        r = csv.reader(f); next(r)
        for row in r:
            if len(row) < 2 or row[1].strip() in ("", "."):
                continue
            d[row[0]] = float(row[1])
    return d

def premium(r30, r15):
    i15 = r15 / 1200
    P = 100000 * i15 / (1 - (1 + i15) ** -180)
    int15 = 180 * P - 100000
    i30 = r30 / 1200
    bal, paid, n = 100000.0, 0.0, 0
    while True:
        n += 1
        due = bal * (1 + i30)
        if due <= P:          # final (partial) month pays remaining balance*(1+i30)
            paid += due
            break
        paid += P
        bal = due - P
        if n > 10000:
            raise RuntimeError("no payoff")
    return (paid - 100000) - int15, n

a, b = load("MORTGAGE30US"), load("MORTGAGE15US")
weeks = sorted(set(a) & set(b))
last = "2026-09-24"
r30, r15 = a[last], b[last]
prem, months = premium(r30, r15)
spreads = [a[w] - b[w] for w in weeks]
prems = [premium(a[w], b[w])[0] for w in weeks]
out = {
    "latest_r30": r30,
    "latest_r15": r15,
    "latest_spread": round(r30 - r15, 2),
    "latest_premium_per_100k": round(prem),
    "latest_months_to_payoff": months,
    "mean_spread_all_weeks": round(statistics.mean(spreads), 3),
    "median_premium_all_weeks": round(statistics.median(prems)),
    "share_weeks_spread_ge_050": round(100 * sum(1 for s in spreads if round(s * 100) >= 50) / len(weeks), 1),
    "n_weeks": len(weeks),
}
print(json.dumps(out, indent=1))

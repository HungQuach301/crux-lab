import csv, json, os
D = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(D, "data/TB3MS.csv"))))
obs = [(r["observation_date"], float(r["TB3MS"])) for r in rows
       if "2022-01-01" <= r["observation_date"] <= "2026-08-01" and r["TB3MS"] not in ("", ".")]
assert len(obs) == 56, len(obs)
bey = [100*365*(v/100)/(360-91*(v/100)) for _, v in obs]
n = len(obs)

def prepay():
    B = 0.0
    for _ in range(n): B = (B + 500) * (1 + 3.00/1200)
    return B
def tbill(t):
    A = 0.0
    for y in bey: A = (A + 500) * (1 + y*(1-t)/1200)
    return A

P = prepay()
res = {"n_months": n, "contributed": 500*n, "prepay_value": round(P)}
for t in (0, 22, 24, 32):
    A = tbill(t/100)
    res[f"tbill_value_tax{t}"] = round(A)
    res[f"gap_tax{t}"] = round(A - P)
res["avg_bey"] = round(sum(bey)/n, 2)
res["months_aftertax22_above_rate"] = sum(1 for y in bey if y*0.78 > 3.00)
run = 0
for y in reversed(bey):
    if y*0.78 < 3.00: run += 1
    else: break
res["recent_run_aftertax22_below_rate"] = run
res["months_pretax_below_rate"] = sum(1 for y in bey if y < 3.00)
lo, hi = 0.0, 0.9
for _ in range(60):
    mid = (lo+hi)/2
    if tbill(mid) > P: lo = mid
    else: hi = mid
res["breakeven_tax_rate"] = round(lo*100, 1)
res["last_tb3ms"] = obs[-1][1]
json.dump(res, open(os.path.join(D, "result.json"), "w"), indent=1)
print(json.dumps(res, indent=1)); print("unrounded P", P, "A0", tbill(0), "lo", lo)

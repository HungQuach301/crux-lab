import csv, json, statistics
from collections import defaultdict

def qkey(d):
    y, m = int(d[:4]), int(d[5:7])
    return y * 4 + (m - 1) // 3

hpi = {}
for row in csv.DictReader(open("data/USSTHPI.csv")):
    k = qkey(row["observation_date"])
    if qkey("1975-01-01") <= k <= qkey("2026-04-01"):
        hpi[k] = float(row["USSTHPI"])

acc = defaultdict(list)
for row in csv.DictReader(open("data/MORTGAGE30US.csv")):
    v = row["MORTGAGE30US"].strip()
    if v in ("", "."):
        continue
    acc[qkey(row["observation_date"])].append(float(v))
rate = {k: sum(v) / len(v) for k, v in acc.items()}

def f(r):
    i = r / 1200.0
    return i / (1 - (1 + i) ** -360)

def run(h, thr):
    pc, off = [], []
    for q0 in sorted(hpi):
        q1 = q0 + h
        if q1 not in hpi:
            continue
        if rate[q0] - rate[q1] >= thr - 1e-9:
            pc.append(hpi[q1] * f(rate[q1]) / (hpi[q0] * f(rate[q0])) - 1)
            relief = 1 - f(rate[q1]) / f(rate[q0])
            off.append((hpi[q1] / hpi[q0] - 1) / relief)
    return pc, off

out = {}
for tag, h, thr in [("4q_1pt", 4, 1.0), ("4q_halfpt", 4, 0.5), ("8q_1pt", 8, 1.0)]:
    pc, off = run(h, thr)
    out[f"n_windows_{tag}"] = len(pc)
    out[f"share_payment_fell_{tag}"] = round(100 * sum(x < 0 for x in pc) / len(pc), 1)
    out[f"median_payment_change_{tag}"] = round(100 * statistics.median(pc), 1)
    out[f"median_offset_share_{tag}"] = round(100 * statistics.median(off), 1)
print(json.dumps(out, indent=1))

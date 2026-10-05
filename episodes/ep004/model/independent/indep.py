import csv, json
D = "/home/user/crux-lab/episodes/ep004/data/"
S = dict(los_angeles="ATNHPIUS31084Q", san_diego="ATNHPIUS41740Q", san_francisco="ATNHPIUS41884Q",
         san_jose="ATNHPIUS41940Q", seattle="ATNHPIUS42644Q", boston="ATNHPIUS14454Q",
         new_york="ATNHPIUS35614Q", miami="ATNHPIUS33124Q", denver="ATNHPIUS19740Q",
         phoenix="ATNHPIUS38060Q", dallas="ATNHPIUS19124Q", chicago="ATNHPIUS16984Q")
METROS = list(S)
S["us"] = "USSTHPI"

def load(sid):
    rows = []
    with open(D + sid + ".csv", newline="") as f:
        for r in csv.DictReader(f):
            v = r[sid].strip()
            if v in ("", "."):
                continue
            rows.append((r["observation_date"], float(v)))
    return rows

out = {}
for k, sid in S.items():
    rows = load(sid)
    assert rows[-1][0] == "2026-04-01", (k, rows[-1])
    vals = dict(rows)
    q = ["2000-01-01", "2000-04-01", "2000-07-01", "2000-10-01"]
    assert all(d in vals for d in q), k
    base = sum(vals[d] for d in q) / 4
    g = vals["2026-04-01"] / base
    out[f"base_{k}"] = base
    out[f"growth_{k}"] = g
    out[f"threshold_joint_{k}"] = 500000 / (g - 1)
    post = [(d, v) for d, v in rows if d >= "2001-01-01"]
    for P, lab in ((200000, "200k"), (300000, "300k")):
        out[f"gain_at_{lab}_{k}"] = P * (g - 1)
        ok = [P * (v / base - 1) > 500000 for d, v in post]
        out[f"cross_quarter_at_{lab}_{k}"] = next((post[i][0] for i, b in enumerate(ok) if b), None)
        stay = None
        for i in range(len(post) - 1, -1, -1):
            if ok[i]:
                stay = post[i][0]
            else:
                break
        out[f"stay_quarter_at_{lab}_{k}"] = stay

out["threshold_single_us"] = 250000 / (out["growth_us"] - 1)
tj = {m: out[f"threshold_joint_{m}"] for m in METROS}
mn = min(tj, key=tj.get); mx = max(tj, key=tj.get)
out["threshold_joint_min"] = tj[mn]; out["threshold_joint_min_metro"] = mn
out["threshold_joint_max"] = tj[mx]; out["threshold_joint_max_metro"] = mx
out["metros_threshold_under_200k"] = sum(t < 200000 for t in tj.values())
out["metros_threshold_under_300k"] = sum(t < 300000 for t in tj.values())
out["metros_crossed_at_200k"] = sum(out[f"cross_quarter_at_200k_{m}"] is not None for m in METROS)
out["metros_crossed_at_300k"] = sum(out[f"cross_quarter_at_300k_{m}"] is not None for m in METROS)
cpi = dict(load("CPIAUCNS"))
assert load("CPIAUCNS")[-1][0] == "2026-08-01"
out["cpi_base"] = cpi["1997-05-01"]; out["cpi_now"] = cpi["2026-08-01"]
out["excl_joint_1997_in_now"] = 500000 * out["cpi_now"] / out["cpi_base"]
json.dump(out, open("independent.json", "w"), indent=1)
print(len(out))

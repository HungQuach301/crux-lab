import csv, json
IDS = ["OBMMIC30YFLVLE80FGE740", "OBMMIC30YFLVGT80FGE740", "OBMMIC30YFLVLE80FLT680"]
def load(sid):
    d = {}
    with open(f"data/{sid}.csv") as f:
        for row in csv.DictReader(f):
            try: d[row["observation_date"]] = float(row[sid])
            except (ValueError, TypeError): pass
    return d
s = {k: load(k) for k in IDS}
le, gt, lo = (s[k] for k in IDS)
dates = sorted(d for d in set(le) & set(gt) & set(lo) if "2017-01-03" <= d <= "2026-09-29")
ltv = [gt[d] - le[d] for d in dates]
cr = [lo[d] - le[d] for d in dates]
m_ltv = sum(ltv) / len(ltv); m_cr = sum(cr) / len(cr)
out = {
    "n_days": len(dates),
    "mean_ltv_gap": round(m_ltv, 3),
    "max_ltv_gap": round(max(ltv), 3),
    "mean_credit_gap": round(m_cr, 3),
    "credit_to_ltv_ratio": round(m_cr / m_ltv, 1),
    "share_days_credit_gap_gt_ltv_gap": round(100 * sum(c > l for c, l in zip(cr, ltv)) / len(dates), 1),
    "latest_le80_ge740": le.get("2026-09-29"),
    "latest_gt80_ge740": gt.get("2026-09-29"),
    "latest_le80_lt680": lo.get("2026-09-29"),
}
print(json.dumps(out, indent=1))

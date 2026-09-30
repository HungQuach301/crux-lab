"""debt-4: locked-rate gap from a small down payment (LTV>80 vs <=80) vs the gap from a lower credit score. Reads data/ only."""
import csv, json, statistics as st
def load(s):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
le, gt, lo = load('OBMMIC30YFLVLE80FGE740'), load('OBMMIC30YFLVGT80FGE740'), load('OBMMIC30YFLVLE80FLT680')
days = sorted(set(le) & set(gt) & set(lo))
ltv = [gt[d] - le[d] for d in days]
cred = [lo[d] - le[d] for d in days]
last = days[-1]
out = {
    'n_days': len(days),
    'mean_ltv_gap': round(st.mean(ltv), 3),
    'max_ltv_gap': round(max(ltv), 3),
    'mean_credit_gap': round(st.mean(cred), 3),
    'credit_to_ltv_ratio': round(st.mean(cred) / st.mean(ltv), 1),
    'share_days_credit_gap_gt_ltv_gap': round(100 * sum(c > l for c, l in zip(cred, ltv)) / len(days), 1),
    'latest_le80_ge740': le[last], 'latest_gt80_ge740': gt[last], 'latest_le80_lt680': lo[last],
}
print(json.dumps(out))

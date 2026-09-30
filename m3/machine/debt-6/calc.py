"""debt-6: VA locked rate vs the best conventional tier (FICO>=740, LTV<=80), and the payback time of the 1.25% VA fee. Reads data/ only."""
import csv, json, statistics as st
def load(s):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
va, cv = load('OBMMIVA30YF'), load('OBMMIC30YFLVLE80FGE740')
days = sorted(set(va) & set(cv))
reg = [d for d in days if d >= '2023-04-07']
out = {
    'n_days': len(days),
    'share_days_va_below_best_conv': round(100 * sum(round(va[d] * 1000) < round(cv[d] * 1000) for d in days) / len(days), 1),
    'n_days_since_20230407': len(reg),
    'share_days_va_below_since_20230407': round(100 * sum(round(va[d] * 1000) < round(cv[d] * 1000) for d in reg) / len(reg), 1),
    'mean_va_since_20230407': round(st.mean(va[d] for d in reg), 3),
    'mean_conv_since_20230407': round(st.mean(cv[d] for d in reg), 3),
}
out['mean_gap_since_20230407'] = round(st.mean(cv[d] - va[d] for d in reg), 3)

def pay(rate, L=100000.0):
    i = rate / 1200
    return L * i / (1 - (1 + i) ** -360)

rv, rc = st.mean(va[d] for d in reg), st.mean(cv[d] for d in reg)
fee = 0.0125 * 100000
pv, pc = pay(rv), pay(rc)
bv = bc = 100000.0
cum, be_net = 0.0, None
for m in range(1, 361):
    bv = bv * (1 + rv / 1200) - pv
    bc = bc * (1 + rc / 1200) - pc
    cum += pc - pv
    if be_net is None and cum + (bc - bv) >= fee:
        be_net = m
out['monthly_saving_per_100k'] = round(pc - pv, 2)
out['breakeven_months_payment_only'] = round(fee / (pc - pv), 1)
out['breakeven_months_net'] = be_net
# net position after 10 years: payment savings + lower balance - fee
bv = bc = 100000.0
for m in range(120):
    bv = bv * (1 + rv / 1200) - pv
    bc = bc * (1 + rc / 1200) - pc
out['net_gain_10y_per_100k'] = round(120 * (pc - pv) + (bc - bv) - fee)
print(json.dumps(out))

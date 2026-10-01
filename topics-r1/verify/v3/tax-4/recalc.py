import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [r for r in csv.DictReader(open(os.path.join(HERE, "data/AHETPI.csv"))) if r["AHETPI"] not in ("", ".")]
last = rows[-1]
ahe = float(last["AHETPI"]); ahe_date = last["observation_date"]

BR = [(12400, .10), (50400, .12), (105700, .22), (201775, .24), (256225, .32), (640600, .35), (float("inf"), .37)]
def T(x):
    x = max(0.0, x); tax = 0.0; lo = 0.0
    for hi, r in BR:
        if x > lo: tax += (min(x, hi) - lo) * r
        lo = hi
    return tax

SD = 16100; HRS = 400; FICA = 0.0765
reg = float(round(ahe))  # nearest whole dollar
ot = 1.5 * reg
B = reg * 2080
E = ot * HRS
prem = 0.5 * reg * HRS
D_ot = min(prem, 12500)

def inc_tax(E, D): return T(B + E - SD - D) - T(B - SD)
def take_home(E, D): return E - FICA * E - inc_tax(E, D)

payroll = round(FICA * E, 2)
ot_tax = round(inc_tax(E, D_ot), 2)
side_tax = round(inc_tax(E, 0), 2)
ot_th = round(E - payroll - ot_tax, 2)
side_th = round(E - payroll - side_tax, 2)

lo, hi = ot, 3 * ot
f = lambda R: take_home(R * HRS, 0) - ot_th
for _ in range(200):
    mid = (lo + hi) / 2
    if f(mid) < 0: lo = mid
    else: hi = mid
be = round((lo + hi) / 2, 2)

res = {
 "ahe_latest": ahe, "ahe_date": ahe_date, "regular_rate_usd": reg, "ot_rate_usd": ot,
 "extra_pay_usd": E, "ot_premium_deduction_usd": prem,
 "deductible_share_of_ot_pay_pct": round(100 * prem / E, 2),
 "ot_income_tax_on_extra_usd": ot_tax, "side_income_tax_on_extra_usd": side_tax,
 "payroll_tax_on_extra_usd": payroll, "ot_extra_take_home_usd": ot_th,
 "side_extra_take_home_usd": side_th, "ot_advantage_usd": round(ot_th - side_th, 2),
 "ot_total_tax_rate_on_extra_pct": round(100 * (1 - ot_th / E), 2),
 "side_total_tax_rate_on_extra_pct": round(100 * (1 - side_th / E), 2),
 "side_breakeven_rate_usd": be,
}
json.dump(res, open(os.path.join(HERE, "result.json"), "w"), indent=1)
print(json.dumps(res, indent=1))

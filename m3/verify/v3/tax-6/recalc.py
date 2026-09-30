import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load(sid):
    out = {}
    with open(os.path.join(D, sid + '.csv')) as f:
        r = csv.reader(f); next(r)
        for d, v in r:
            if v not in ('', '.'):
                out[d[:7]] = float(v)
    return out

def A(s, y):
    keys = [f"{y-1}-{m:02d}" for m in range(9, 13)] + [f"{y}-{m:02d}" for m in range(1, 9)]
    return sum(s[k] for k in keys) / 12

cpi, cc = load('CPIAUCNS'), load('SUUR0000SA0')
r_cpi16 = A(cpi, 2025) / A(cpi, 2016); r_cc16 = A(cc, 2025) / A(cc, 2016)
r_cpi17 = A(cpi, 2025) / A(cpi, 2017); r_cc17 = A(cc, 2025) / A(cc, 2017)
g16 = r_cpi16 / r_cc16 - 1
g17 = r_cpi17 / r_cc17 - 1

RATES = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
ACT = [24800, 100800, 211400, 403550, 512450, 768700]
HYP = [24800 * (1 + g16), 100800 * (1 + g16)] + [x * (1 + g17) for x in ACT[2:]]

def tax(T, lims):
    t, lo = 0.0, 0.0
    for rate, hi in zip(RATES, lims + [float('inf')]):
        if T > lo:
            t += rate * (min(T, hi) - lo)
        lo = hi
    return t

def extra(agi):
    T = max(agi - 32200, 0)
    return tax(T, ACT) - tax(T, HYP)

e200 = extra(200000)
res = {
    "cpiu_growth_2016_2025_pct": 100 * (r_cpi16 - 1),
    "ccpiu_growth_2016_2025_pct": 100 * (r_cc16 - 1),
    "gap_2016_base_pct": 100 * g16,
    "gap_2017_base_pct": 100 * g17,
    "gap_per_year_pp": 100 * ((1 + g16) ** (1 / 9) - 1),
    "top12_mfj_under_cpiu_usd": round(100800 * (1 + g16)),
    "extra_tax_mfj_agi100k_usd": extra(100000),
    "extra_tax_mfj_agi200k_usd": e200,
    "extra_tax_mfj_agi300k_usd": extra(300000),
    "eitc_max3_under_cpiu_usd": round(8231 * (1 + g16)),
    "eitc_max3_shortfall_usd": 8231 * g16,
    "eitc_shortfall_share_of_25k_earnings_pct": 100 * 8231 * g16 / 25000,
    "extra_tax_share_of_agi200k_pct": 100 * e200 / 200000,
}
print(json.dumps(res, indent=1))

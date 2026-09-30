"""tax-6: tax year 2026 amounts are indexed with the chained CPI (C-CPI-U) instead of CPI-U since 2018.
Gap between the two over the indexing windows, and its 2026 cost for a few households. Reads data/ only."""
import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load(sid):
    rows = [r for r in csv.reader(open(os.path.join(D, sid + '.csv')))][1:]
    return {r[0]: float(r[1]) for r in rows if r[1] not in ('', '.')}

U, C = load('CPIAUCNS'), load('SUUR0000SA0')

def cy(d, y):
    """statutory 'calendar year' index: mean of the 12 months Sep (y-1) .. Aug (y)"""
    ks = [f'{y - 1}-{m:02d}-01' for m in range(9, 13)] + [f'{y}-{m:02d}-01' for m in range(1, 9)]
    return sum(d[k] for k in ks) / 12

g16 = (cy(U, 2025) / cy(U, 2016)) / (cy(C, 2025) / cy(C, 2016)) - 1   # 10%/12% bracket amounts, EITC (pre-2017 bases)
g17 = (cy(U, 2025) / cy(U, 2017)) / (cy(C, 2025) / cy(C, 2017)) - 1   # thresholds of the 22%+ brackets (2017 base)

STD = 32200
ACT = [(24800, .10), (100800, .12), (211400, .22), (403550, .24), (512450, .32), (768700, .35), (float('inf'), .37)]
HYP = [(24800 * (1 + g16), .10), (100800 * (1 + g16), .12)] + [(t * (1 + g17), r) for t, r in ACT[2:]]

def tax(ti, sched):
    t, lo = 0.0, 0.0
    for hi, r in sched:
        if ti > lo:
            t += (min(ti, hi) - lo) * r
        lo = hi
    return t

def extra(agi):
    ti = max(0.0, agi - STD)
    return tax(ti, ACT) - tax(ti, HYP)

out = {
    'cpiu_growth_2016_2025_pct': round((cy(U, 2025) / cy(U, 2016) - 1) * 100, 2),
    'ccpiu_growth_2016_2025_pct': round((cy(C, 2025) / cy(C, 2016) - 1) * 100, 2),
    'gap_2016_base_pct': round(g16 * 100, 3),
    'gap_2017_base_pct': round(g17 * 100, 3),
    'gap_per_year_pp': round(((1 + g16) ** (1 / 9) - 1) * 100, 3),
    'top12_mfj_under_cpiu_usd': round(100800 * (1 + g16), 0),
    'extra_tax_mfj_agi100k_usd': round(extra(100000), 2),
    'extra_tax_mfj_agi200k_usd': round(extra(200000), 2),
    'extra_tax_mfj_agi300k_usd': round(extra(300000), 2),
    'eitc_max3_under_cpiu_usd': round(8231 * (1 + g16), 0),
    'eitc_max3_shortfall_usd': round(8231 * g16, 2),
    'eitc_shortfall_share_of_25k_earnings_pct': round(8231 * g16 / 25000 * 100, 3),
    'extra_tax_share_of_agi200k_pct': round(extra(200000) / 200000 * 100, 3),
}
print(json.dumps(out))

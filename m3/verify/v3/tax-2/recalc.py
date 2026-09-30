#!/usr/bin/env python3
"""Independent recomputation for tax-2 (reads ./data only, no network)."""
import csv, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- 2026 parameters (IR-2025-103, Rev. Proc. 2025-32, 26 USC 21/24/32/3101) ----
STD_DED = 32_200
BRACKETS = [(24_800, .10), (100_800, .12), (211_400, .22), (403_550, .24),
            (512_450, .32), (768_700, .35), (math.inf, .37)]
CARE_CAP = 6_000
DCAP = 7_500
CTC_PER = 2_200
CTC_REFUND_PER = 1_700
CTC_EARN_THRESH = 2_500
KIDS = 2
EIC_MAX = 7_316
EIC_EARN_AMT = 18_290
EIC_PHASE_START = 31_160
EIC_PHASE_RATE = 0.2106
PAYROLL = 0.062 + 0.0145


def ordinary_tax(ti):
    tax, lo = 0.0, 0.0
    for hi, r in BRACKETS:
        if ti > lo:
            tax += (min(ti, hi) - lo) * r
        lo = hi
    return tax


def care_rate(agi):
    over = max(0, agi - 15_000)
    p = max(35, 50 - math.ceil(over / 2_000))
    over2 = max(0, agi - 150_000)
    p = max(20, p - math.ceil(over2 / 4_000))
    return p / 100


def eic(earned, agi):
    phase_in = min(EIC_MAX, EIC_MAX / EIC_EARN_AMT * earned)
    return max(0.0, phase_in - EIC_PHASE_RATE * max(0, max(agi, earned) - EIC_PHASE_START))


def net_cost(W, fsa):
    wages = W - DCAP if fsa else W
    agi = earned = wages
    cap = max(0, CARE_CAP - DCAP) if fsa else CARE_CAP
    tax = ordinary_tax(max(0, agi - STD_DED))
    care = min(tax, care_rate(agi) * cap)
    tax -= care
    ctc_total = KIDS * CTC_PER
    ctc_nr = min(tax, ctc_total)
    tax -= ctc_nr
    unused = ctc_total - ctc_nr
    ctc_ref = min(unused, KIDS * CTC_REFUND_PER, 0.15 * max(0, earned - CTC_EARN_THRESH))
    income_tax = tax - ctc_ref - eic(earned, agi)
    return income_tax + PAYROLL * wages


def diff(W):
    """NetCost(FSA) - NetCost(credit); positive = credit path cheaper."""
    return net_cost(W, True) - net_cost(W, False)


def cpi_ratio():
    rows = []
    with open(os.path.join(HERE, "data", "CPIAUCSL.csv")) as f:
        r = csv.reader(f)
        next(r)
        for d, v in r:
            try:
                rows.append((d, float(v)))
            except ValueError:
                pass
    rows.sort()
    last12 = [v for d, v in rows if "2025-09-01" <= d <= "2026-08-01"]
    y2003 = [v for d, v in rows if d.startswith("2003-")]
    assert len(last12) == 12 and len(y2003) == 12, (len(last12), len(y2003))
    assert rows[-1][0] == "2026-08-01"
    return (sum(last12) / 12) / (sum(y2003) / 12)


def main():
    out = {}
    out["credit_2026_usd_at_100k"] = round(care_rate(100_000) * CARE_CAP, 2)
    out["fsa_saving_usd_at_100k_12pct"] = round(DCAP * (0.12 + PAYROLL), 2)
    out["advantage_credit_usd_at_100k"] = round(diff(100_000), 2)
    out["advantage_credit_usd_at_80k"] = round(diff(80_000), 2)
    out["advantage_fsa_usd_at_40k"] = round(-diff(40_000), 2)
    out["advantage_fsa_usd_at_180k"] = round(-diff(180_000), 2)
    grid = 500
    assert diff(100_000) > 0
    lo = 100_000
    while lo - grid >= 0 and diff(lo - grid) > 0:
        lo -= grid
    hi = 100_000
    while diff(hi + grid) > 0:
        hi += grid
    out["credit_wins_from_wages_usd"] = lo
    out["credit_wins_to_wages_usd"] = hi
    out["cap_6000_in_current_prices_usd"] = round(CARE_CAP * cpi_ratio())
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

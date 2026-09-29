"""Tests of the Episode 1 refinance model. Hand cases come from published sources, not from the model itself.

    python3 -m pytest episodes/ep001/model/test_refi.py -q
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refi  # noqa: E402


def test_payment_cfpb_ask_136():
    # CFPB, Ask CFPB #136 ("How points affect interest rates in different scenarios"), $180,000, 30 years:
    # 4.875% instead of 5% -> "Pay $14 less each month", for "$675 more in closing costs"
    # (the same case is level-1 evidence of crux-studio model M-002).
    s = refi.payment(180000, 5, 360) - refi.payment(180000, 4.875, 360)
    assert round(s) == 14
    assert refi.break_even_months(675, s) == math.ceil(675 / s)


def test_payment_closed_form_values():
    # $100,000 at 6% for 360 months: the standard amortisation table value $599.55
    assert abs(refi.payment(100000, 6, 360) - 599.55) < 0.005
    # 0% rate: straight division
    assert refi.payment(36000, 0, 360) == 100


def test_balance_after_full_term_is_zero_and_after_zero_is_principal():
    assert abs(refi.balance_after(250000, 7, 360, 360)) < 1e-6
    assert abs(refi.balance_after(250000, 7, 360, 0) - 250000) < 1e-9
    # after 12 payments on $100,000 at 6%: $98,771.99 (standard amortisation table)
    assert abs(refi.balance_after(100000, 6, 360, 12) - 98771.99) < 0.01


def test_break_even_rounds_up_and_never_when_no_savings():
    assert refi.break_even_months(1000, 100) == 10
    assert refi.break_even_months(1001, 100) == 11
    assert refi.break_even_months(1000, 0) is None
    assert refi.break_even_months(1000, -5) is None


def test_refi_same_rate_same_term_saves_nothing():
    r = refi.refi(300000, 6.5, 360, 6.5, 5000)
    assert abs(r['monthlySavings']) < 1e-9 and r['breakEvenMonths'] is None


def test_spread_for_break_even_is_monotone_in_cost():
    a = refi.spread_for_break_even(300000, 7, 3000, 36)
    b = refi.spread_for_break_even(300000, 7, 6000, 36)
    assert 0 < a < b
    # the returned spread really meets the target and a slightly smaller one does not
    assert refi.refi(300000, 7, 360, 7 - b, 6000)['breakEvenMonths'] <= 36
    assert refi.refi(300000, 7, 360, 7 - (b - 0.01), 6000)['breakEvenMonths'] > 36


def test_zigzag_finds_every_swing():
    series = [(str(i), v) for i, v in enumerate([8, 9, 10, 9.5, 8.8, 8.5, 9.0, 9.8, 10.2, 9.0, 8.9, 9.1])]
    eps = refi.drop_episodes(series, threshold=1.0)
    assert [(e['peak'], e['trough']) for e in eps] == [('2', '5'), ('8', '10')]


def test_history_cases_reach_only_spreads_the_episode_reached():
    series = [(f'2000-{i:02d}', v) for i, v in enumerate([8.0, 8.0, 7.6, 7.2, 7.0, 7.1, 8.2], start=1)]
    h = refi.history(series, 2.0, spreads=(0.5, 1.0, 1.5))
    assert len(h) == 1
    c = {x['spread']: x for x in h[0]['cases']}
    assert c[0.5]['reached'] and c[0.5]['refiMonth'] == '2000-04'  # 7.6 is only 0.4 under the 8.0 peak; 7.2 is the first >= 0.5
    assert c[1.0]['reached'] and c[1.0]['refiMonth'] == '2000-05'
    assert not c[1.5]['reached']


# ------------------------------------------------------------------ balance-counting break-even (main method)
def _brute(P, r0, k, r1, C):
    """Independent re-implementation by explicit month-by-month amortisation (no closed forms)."""
    def sched(P, r, n, months):
        i = r / 1200; pay = refi.payment(P, r, n); b = P; out = []
        for _ in range(months):
            b = b * (1 + i) - pay; out.append(b)
        return pay, out
    p_old, old = sched(P, r0, 360, 360)
    B = P if k == 0 else old[k - 1]
    p_new, new = sched(B, r1, 360, 360)
    for m in range(1, 360 - k + 1):
        if (p_old - p_new) * m + (old[k + m - 1] - new[m - 1]) >= C:
            return m
    return None


def test_balance_break_even_matches_month_by_month_schedule():
    for case in [(375000, 7.62, 35, 7.03, 5124), (115000, 7.62, 35, 6.62, 3900), (655000, 7.62, 35, 7.03, 5514), (1005000, 7.62, 0, 7.12, 5750), (300000, 16.33, 1, 14.26, 4800)]:
        assert refi.break_even_balance(*case) == _brute(*case), case


def test_balance_method_is_never_earlier_than_simple_when_the_term_resets_late():
    # a loan already 5 years old refinanced into a fresh 30 years: the new loan pays principal more slowly,
    # so counting the balance makes break-even later than cost / savings
    b = refi.both(375000, 7.62, 60, 6.62, 5124)
    assert b['withBalance'] >= b['simple']


def test_balance_method_same_rate_never_breaks_even():
    assert refi.break_even_balance(300000, 6.5, 24, 6.5, 5000) is None


def test_net_after_equals_zero_near_break_even():
    m = refi.break_even_balance(375000, 7.62, 35, 6.62, 5124)
    assert refi.net_after(375000, 7.62, 35, 6.62, 5124, m) >= 0 > refi.net_after(375000, 7.62, 35, 6.62, 5124, m - 1)


# ------------------------------------------------------------------ cold-open claim peak_since2000 (recomputed from the CSV, not from build.py)
def test_peak_since2000_recomputed_from_csv():
    import csv
    import json
    import pytest
    ep = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    p = os.path.join(ep, 'data', 'normalized', 'mortgage30_weekly.csv')
    if not os.path.exists(p):
        pytest.skip('FRED data not in the repo (public repo): run python3 episodes/ep001/data/fetch.py --verify first')
    w = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(p))]
    since2000 = [(d, v) for d, v in w if d >= '2000-01-01']
    oct23 = [(d, v) for d, v in since2000 if d.startswith('2023-10')]
    peak_d, peak_v = max(oct23, key=lambda x: x[1])
    assert (peak_d, peak_v) == ('2023-10-26', 7.79)
    before = [(d, v) for d, v in since2000 if d < peak_d]
    tie = [d for d, v in before if v >= peak_v][-1]
    above = [d for d, v in before if v > peak_v][-1]
    assert tie == '2000-11-10' and above == '2000-10-20'
    # no week between the tie week and the peak week reached the peak: the statement "highest since 2000" is true
    assert all(v < peak_v for d, v in since2000 if tie < d < peak_d)
    claims = {c['claimId']: c for c in json.load(open(os.path.join(ep, 'out', 'claims.json')))['claims']}
    c = claims['peak_since2000']
    assert c['value'] == 2000 and c['display'] == '2000' and c['date'] == tie and c['lastWeekAbove'] == above
    assert c['peakWeek'] == peak_d and c['peakValue'] == peak_v and not c['illustrative']


# ------------------------------------------------------------------ 2026 refinance-window claims (recomputed from the CSV, not from build.py)
def test_window2026_recomputed_from_csv():
    import csv
    import datetime
    import json
    import pytest
    ep = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    p = os.path.join(ep, 'data', 'normalized', 'mortgage30_weekly.csv')
    if not os.path.exists(p):
        pytest.skip('FRED data not in the repo (public repo): run python3 episodes/ep001/data/fetch.py --verify first')
    rows = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(p))]
    rate = dict(rows)
    claims = {c['claimId']: c for c in json.load(open(os.path.join(ep, 'out', 'claims.json')))['claims']}
    anchor = '2026-09-24'
    assert rows[-1] == (anchor, 7.03)
    # 1. low of 2026 (scan by hand, no min())
    best = None
    for d, v in rows:
        if d[:4] == '2026' and (best is None or v < best[1]):
            best = (d, v)
    assert best == ('2026-02-26', 5.98)
    assert claims['low2026']['value'] == 5.98 and claims['low2026']['date'] == '2026-02-26' and claims['low2026']['asOf'] == anchor
    assert claims['low2026_date']['display'] == 'February 26, 2026'
    # 2. walk back from the low to the last week at or below it
    i = [d for d, _ in rows].index('2026-02-26') - 1
    while rows[i][1] > 5.98:
        i -= 1
    assert rows[i] == ('2022-09-08', 5.89)
    assert claims['low2026_since']['value'] == '2022-09-08' and claims['low2026_since']['display'] == 'September 2022'
    gap_days = (datetime.date(2026, 2, 26) - datetime.date(2022, 9, 8)).days
    assert 3 * 365 < gap_days < 4 * 365  # "lowest in more than three years" holds
    # 3. week ending 2026-01-15 = 6.06%, lowest since the week ending 2022-09-15; not the 2026 low; no week dated 2026-01-12
    assert rate['2026-01-15'] == 6.06 and '2026-01-12' not in rate and datetime.date(2026, 1, 12).weekday() == 0
    j = [d for d, _ in rows].index('2026-01-15') - 1
    while rows[j][1] > 6.06:
        j -= 1
    assert rows[j] == ('2022-09-15', 6.02)
    assert claims['jan2026']['value'] == 6.06 and claims['jan2026_since']['value'] == '2022-09-15' and 6.06 > best[1]
    # 4. the median character (Nora) refinancing at the 2026 low: month-by-month amortisation, own payment formula
    r_old = sum(v for d, v in rows if d[:7] == '2023-10') / len([d for d in rate if d[:7] == '2023-10'])
    assert round(r_old, 2) == 7.62 and claims['cut_low2026']['value'] == round(7.62 - 5.98, 2) == 1.64
    k = (2026 - 2023) * 12 + (2 - 10)
    assert k == 28 == claims['k_low2026']['value']

    def pay(P, r, n=360):
        i_ = r / 1200
        return P * i_ * (1 + i_) ** n / ((1 + i_) ** n - 1)

    def sched(P, r, months):
        i_, p_, b, out = r / 1200, pay(P, r), P, []
        for _ in range(months):
            b = b * (1 + i_) - p_
            out.append(b)
        return out
    hm = next(r for r in csv.DictReader(open(os.path.join(ep, 'data', 'normalized', 'hmda_refi_costs.csv')))
              if r['year'] == '2025' and r['purpose'] == 'refinance (31)' and r['loanSize'] == 'all sizes')
    L, cost = float(hm['loan_p50_usd']), float(hm['cost_p50_usd'])  # the HMDA medians of loan_median / cost_median
    assert (L, cost) == (claims['loan_median']['value'], claims['cost_median']['value']) == (375000.0, 5123.53)
    old = sched(L, r_old, 360)
    B = old[k - 1]
    new = sched(B, 5.98, 360)
    s = pay(L, r_old) - pay(B, 5.98)
    assert abs(s - claims['sav_low2026_median']['value']) < 0.01 and claims['sav_low2026_median']['display'] == '$459'
    assert claims['be_simple_low2026_median']['value'] == math.ceil(cost / s) == 12
    be = next(m for m in range(1, 360 - k + 1) if s * m + old[k + m - 1] - new[m - 1] >= cost)
    assert claims['be_bal_low2026_median']['value'] == be == 11
    for c in ('k_low2026', 'sav_low2026_median', 'be_simple_low2026_median', 'be_bal_low2026_median'):
        assert claims[c]['illustrative'], c
    # 5. first week >= 7.00% since ...
    back = [d for d, v in rows if d < anchor and v >= 7.0]
    assert back[-1] == '2025-01-16' and rate['2025-01-16'] == 7.04
    assert all(v < 7.0 for d, v in rows if '2025-01-16' < d < anchor)
    assert claims['first7_since']['value'] == '2025-01-16' and claims['first7_since']['asOf'] == anchor
    # 6. rise since the 2026 low and the number of weeks
    weeks = sum(1 for d, _ in rows if '2026-02-26' < d <= anchor)
    assert weeks == 30 == claims['weeks_rise_since_low2026']['value'] == claims['rise_since_low2026']['weeks']
    assert claims['rise_since_low2026']['value'] == round(7.03 - 5.98, 2) == 1.05
    # 7. weeks of 2026 with a cut of at least 1.00 point from 7.62% (rate <= 6.62%)
    win = [d for d, v in rows if d[:4] == '2026' and round(7.62 - v, 2) >= 1.0]
    assert len(win) == 29 == claims['weeks_below_r_old_minus_1']['value']
    assert win[0] == '2026-01-08' and win[-1] == '2026-07-23' == claims['cut1_last_2026']['value']
    assert all(v > 6.62 for d, v in rows if d > '2026-07-23')

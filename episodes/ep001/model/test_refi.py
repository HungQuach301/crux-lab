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

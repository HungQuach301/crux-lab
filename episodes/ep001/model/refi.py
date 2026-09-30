"""Episode 1 model: when does a refinance pay back its closing costs?

    python3 episodes/ep001/model/refi.py          # writes episodes/ep001/out/model.json
    python3 -m pytest episodes/ep001/model/test_refi.py

Definitions (all nominal dollars, US only):
  payment(P, r, n)       level monthly payment of principal and interest, annual rate r (%), n months
  monthly savings s      payment(B, r_old, n_old) - payment(B, r_new, 360): the old loan's payment on its remaining
                         balance B and remaining term n_old, versus a new 30-year loan for the same balance
  break-even months      closing costs C / s, rounded up to a whole month (the month in which the saved payments first
                         reach C). Closing costs paid in cash, not rolled into the loan; no tax effect; no discounting
                         (the common "costs / monthly savings" presentation). s <= 0 -> never.
  balance check          the new 30-year loan amortises more slowly than the old one; `balance_gap(months)` reports how
                         much more principal is still owed on the new loan after m months, so the film can say what the
                         simple break-even leaves out.

History (every rate drop since 1971, FRED MORTGAGE30US weekly):
  - a "drop episode" is a zig-zag swing of the 30-year rate: from a peak the rate falls by >= 1.00 percentage point
    before rising 1.00 point above its low (monthly means, so single-week noise does not create episodes);
  - borrower: took a 30-year loan at the peak month's rate; the refinance happens in the first month the rate is at
    least `spread` points below it (spreads 0.50, 0.75, 1.00, 1.50, 2.00);
  - loan: $300,000 original balance (ILLUSTRATIVE scenario variable), balance at refinance from the old amortisation;
  - closing cost: HMDA median total loan costs as a share of the loan amount (percent) of the refinance year, applied
    to the balance (`cost_share_pct` may be a function year -> (share, illustrative)); HMDA has the field only from
    2018, so for earlier years a fixed share is applied and every such number is ILLUSTRATIVE;
  - reported per episode and spread: months to break even, and whether the rate fell by another full spread within
    that window (a second refinance would restart the clock).
"""
import csv
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')


def payment(principal, annual_rate_pct, months):
    r = annual_rate_pct / 1200.0
    if r == 0:
        return principal / months
    return principal * r / (1 - (1 + r) ** -months)


def balance_after(principal, annual_rate_pct, months, k):
    """Remaining balance after k payments."""
    r = annual_rate_pct / 1200.0
    p = payment(principal, annual_rate_pct, months)
    if r == 0:
        return principal - p * k
    return principal * (1 + r) ** k - p * ((1 + r) ** k - 1) / r


def break_even_months(closing_cost, monthly_savings):
    if monthly_savings <= 0:
        return None
    return math.ceil(closing_cost / monthly_savings - 1e-9)


def refi(balance, old_rate, old_months_left, new_rate, closing_cost, new_months=360):
    old_p = payment(balance, old_rate, old_months_left)
    new_p = payment(balance, new_rate, new_months)
    s = old_p - new_p
    return {'oldPayment': old_p, 'newPayment': new_p, 'monthlySavings': s, 'breakEvenMonths': break_even_months(closing_cost, s)}


def balance_gap(balance, old_rate, old_months_left, new_rate, months, new_months=360):
    return balance_after(balance, new_rate, new_months, months) - balance_after(balance, old_rate, old_months_left, months)


def spread_for_break_even(balance, old_rate, closing_cost, months_target, old_months_left=360, new_months=360):
    """Smallest rate cut (percentage points) whose break-even is <= months_target (bisection on the new rate)."""
    lo, hi = 0.0, old_rate
    for _ in range(80):
        mid = (lo + hi) / 2
        be = refi(balance, old_rate, old_months_left, old_rate - mid, closing_cost, new_months)['breakEvenMonths']
        if be is not None and be <= months_target:
            hi = mid
        else:
            lo = mid
    return hi


# ------------------------------------------------------------------ break-even counting what is still owed (main method)
def break_even_balance(principal, old_rate, months_paid, new_rate, closing_cost, new_months=360, old_months=360):
    """Month m after the refinance when
         (old payment - new payment) x m  +  (old loan's balance after k+m payments - new loan's balance after m)  >=  closing cost.
    The old loan is `principal` at `old_rate` over `old_months`, with `months_paid` (k) payments already made; the new loan
    refinances the remaining balance at `new_rate` over `new_months` (a fresh 30 years), closing costs paid in cash.
    The second term is negative when the new loan pays principal down more slowly (the term reset): what the simple
    division leaves out. Searched up to the old loan's last payment; None if never reached."""
    k = months_paid
    bal = balance_after(principal, old_rate, old_months, k)
    p_old = payment(principal, old_rate, old_months)
    p_new = payment(bal, new_rate, new_months)
    for m in range(1, old_months - k + 1):
        gap = balance_after(principal, old_rate, old_months, k + m) - balance_after(bal, new_rate, new_months, m)
        if (p_old - p_new) * m + gap >= closing_cost - 1e-9:
            return m
    return None


def net_after(principal, old_rate, months_paid, new_rate, closing_cost, months, new_months=360, old_months=360):
    """Position after `months` (e.g. selling the house then): savings + balance difference - closing cost (dollars)."""
    k = months_paid
    bal = balance_after(principal, old_rate, old_months, k)
    s = (payment(principal, old_rate, old_months) - payment(bal, new_rate, new_months)) * months
    gap = balance_after(principal, old_rate, old_months, k + months) - balance_after(bal, new_rate, new_months, months)
    return s + gap - closing_cost


def both(principal, old_rate, months_paid, new_rate, closing_cost):
    """Simple (cost / monthly savings) and balance-counting break-even for the same case."""
    bal = balance_after(principal, old_rate, 360, months_paid)
    simple = refi(bal, old_rate, 360 - months_paid, new_rate, closing_cost)
    return {'balance': bal, 'monthlySavings': simple['monthlySavings'], 'simple': simple['breakEvenMonths'],
            'withBalance': break_even_balance(principal, old_rate, months_paid, new_rate, closing_cost)}


def cut_for_break_even_balance(principal, old_rate, months_paid, cost_share_or_cost, months_target, cost_is_share=False):
    """Smallest rate cut (points) whose balance-counting break-even is <= months_target."""
    bal = balance_after(principal, old_rate, 360, months_paid)
    cost = bal * cost_share_or_cost / 100 if cost_is_share else cost_share_or_cost
    lo, hi = 0.0, old_rate
    for _ in range(60):
        mid = (lo + hi) / 2
        be = break_even_balance(principal, old_rate, months_paid, old_rate - mid, cost)
        if be is not None and be <= months_target:
            hi = mid
        else:
            lo = mid
    return hi


# ------------------------------------------------------------------ history
def monthly_means(weekly):
    acc = {}
    for d, v in weekly:
        acc.setdefault(d[:7], []).append(v)
    return [(m, sum(v) / len(v)) for m, v in sorted(acc.items())]


def zigzag(series, threshold=1.0):
    """Peaks and troughs of a (label, value) series: a swing counts when it reverses by >= threshold."""
    pts, direction = [], 0
    ext_i = 0
    for i, (_, v) in enumerate(series):
        e = series[ext_i][1]
        if direction >= 0:
            if v > e:
                ext_i = i
            elif e - v >= threshold:
                pts.append(('peak', ext_i)); direction = -1; ext_i = i
        if direction < 0:
            if v < series[ext_i][1]:
                ext_i = i
            elif v - series[ext_i][1] >= threshold:
                pts.append(('trough', ext_i)); direction = 1; ext_i = i
    pts.append(('peak' if direction >= 0 else 'trough', ext_i))
    return pts


def drop_episodes(monthly, threshold=1.0):
    z = zigzag(monthly, threshold)
    eps = []
    for (k1, i1), (k2, i2) in zip(z, z[1:]):
        if k1 == 'peak' and k2 == 'trough':
            eps.append({'peak': monthly[i1][0], 'peakRate': round(monthly[i1][1], 2), 'trough': monthly[i2][0], 'troughRate': round(monthly[i2][1], 2),
                        'drop': round(monthly[i1][1] - monthly[i2][1], 2), 'iPeak': i1, 'iTrough': i2})
    return eps


def history(monthly, cost_share_pct, loan=300_000.0, spreads=(0.5, 0.75, 1.0, 1.5, 2.0), threshold=1.0):
    out = []
    for ep in drop_episodes(monthly, threshold):
        r0 = monthly[ep['iPeak']][1]
        row = {k: v for k, v in ep.items() if not k.startswith('i')}
        row['cases'] = []
        for s in spreads:
            # first month inside this episode (peak .. trough) with the rate at least `s` points under the peak
            j = next((j for j in range(ep['iPeak'] + 1, ep['iTrough'] + 1) if monthly[j][1] <= r0 - s + 1e-9), None)
            if j is None:
                row['cases'].append({'spread': s, 'reached': False})
                continue
            k = j - ep['iPeak']  # months paid on the old loan
            bal = balance_after(loan, r0, 360, k)
            share, illus = cost_share_pct(int(monthly[j][0][:4])) if callable(cost_share_pct) else (cost_share_pct, True)
            cost = bal * share / 100
            res = refi(bal, r0, 360 - k, monthly[j][1], cost)
            be_simple = res['breakEvenMonths']
            be = break_even_balance(loan, r0, k, monthly[j][1], cost)  # main method: counts what is still owed
            nxt = None
            if be is not None:
                nxt = next((m for m in range(j + 1, min(len(monthly), j + be + 1)) if monthly[m][1] <= monthly[j][1] - s), None)
            row['cases'].append({'spread': s, 'reached': True, 'refiMonth': monthly[j][0], 'newRate': round(monthly[j][1], 2), 'monthsOnOldLoan': k,
                                 'balance': round(bal, 2), 'costSharePct': round(share, 4), 'costIllustrative': illus, 'closingCost': round(cost, 2), 'monthlySavings': round(res['monthlySavings'], 2),
                                 'breakEvenMonths': be, 'breakEvenSimple': be_simple, 'beforeBreakEvenAnotherDrop': monthly[nxt][0] if nxt is not None else None,
                                 'dataOnlyTo': monthly[-1][0], 'censored': be is not None and j + be >= len(monthly)})
        out.append(row)
    return out


def load_weekly():
    p = os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv')
    return [(r['date'], float(r['rate'])) for r in csv.DictReader(open(p))]


if __name__ == '__main__':
    import sys
    weekly = load_weekly()
    monthly = monthly_means(weekly)
    share = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
    h = history(monthly, share)
    print(json.dumps({'episodes': len(h)}, indent=1))
    for e in h:
        print(e['peak'], e['peakRate'], '->', e['trough'], e['troughRate'], [(c['spread'], c.get('breakEvenMonths')) for c in e['cases']])

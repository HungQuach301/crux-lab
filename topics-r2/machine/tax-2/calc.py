"""tax-2: a $1,000 emergency bill. Option A: the once-a-year $1,000 emergency withdrawal from a 401(k) (no 10% additional
tax, ordinary income tax due). Option B: put it on a credit card and repay in equal monthly payments. For every quarterly
observation of the average APR on card accounts assessed interest (TERMCBCCINTNS, Nov 1994 .. May 2026), find how many
months of repayment make the card interest exceed the federal tax on the withdrawal at 12% (and at 22%).
Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os, statistics

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
P = 1000.0   # bill = withdrawal (viewer identity)
TAX12, TAX22 = 0.12 * P, 0.22 * P


def series(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0][:7]] = float(row[1])
    return out


def interest(apr, n):
    """total interest on P repaid in n equal monthly payments, monthly rate apr/12"""
    i = apr / 100 / 12
    pmt = P * i / (1 - (1 + i) ** -n)
    return n * pmt - P


def months_to_exceed(apr, tax):
    n = 1
    while interest(apr, n) <= tax:
        n += 1
    return n


apr = series('TERMCBCCINTNS')
obs = sorted(apr)
m12 = {d: months_to_exceed(apr[d], TAX12) for d in obs}
m22 = {d: months_to_exceed(apr[d], TAX22) for d in obs}
last = obs[-1]
lo = min(obs, key=lambda d: apr[d])
hi = max(obs, key=lambda d: apr[d])
out = {
    'observations': len(obs),
    'first_obs': obs[0],
    'last_obs': last,
    'apr_last_pct': apr[last],
    'tax_12_usd': TAX12,
    'tax_22_usd': TAX22,
    'months_12_last': m12[last],
    'months_22_last': m22[last],
    'interest_12mo_last_usd': round(interest(apr[last], 12), 2),
    'interest_24mo_last_usd': round(interest(apr[last], 24), 2),
    'interest_6mo_last_usd': round(interest(apr[last], 6), 2),
    'apr_min_pct': apr[lo], 'apr_min_obs': lo, 'months_12_at_min': m12[lo],
    'apr_max_pct': apr[hi], 'apr_max_obs': hi, 'months_12_at_max': m12[hi],
    'months_12_median': statistics.median(m12.values()),
    'months_22_median': statistics.median(m22.values()),
    'months_12_min': min(m12.values()), 'months_12_max': max(m12.values()),
    'months_22_min': min(m22.values()), 'months_22_max': max(m22.values()),
}
print(json.dumps(out))

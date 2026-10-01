import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP

def r(x, nd=0):
    q = Decimal(1).scaleb(-nd)
    v = Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP)
    return int(v) if nd == 0 else float(v)

dates, tb = [], []
with open('TB3MS.csv') as f:
    for row in csv.DictReader(f):
        dates.append(row['observation_date'][:7]); tb.append(float(row['TB3MS']))
idx = {d: i for i, d in enumerate(dates)}
INDEX = tb[-1]           # 3.72
P, N, FIX = 50000.0, 120, 9.00
MARGIN = 7.50 - INDEX    # 3.78

def level(bal, rate, n):
    i = rate / 1200.0
    if i == 0: return bal / n
    return bal * i / (1 - (1 + i) ** -n)

def amort(rates):
    bal, tot, pay, prev, maxpay = P, 0.0, None, None, -1
    pays = []
    for k, rt in enumerate(rates):
        if pay is None or rt != prev:
            pay = level(bal, rt, N - k)
        prev = rt
        it = bal * rt / 1200.0
        tot += it
        bal = bal + it - pay
        pays.append(pay)
    return tot, max(pays), pays[0], bal

fixed_tot, fixed_pay, _, fixed_end = amort([FIX] * N)
starts = [d for d in dates if '1954-01' <= d <= '2016-09']
assert idx[starts[-1]] + N - 1 == len(tb) - 1

def path(s, margin, cap=None):
    i0 = idx[s]
    out = []
    for k in range(N):
        rt = margin + max(0.0, INDEX + tb[i0 + k] - tb[i0])
        if cap is not None: rt = min(cap, rt)
        out.append(rt)
    return out

def run(margin, cap=None):
    res = []
    for s in starts:
        rates = path(s, margin, cap)
        tot, mp, p0, end = amort(rates)
        res.append(dict(start=s, diff=tot - fixed_tot, maxRate=max(rates), maxPay=mp, p0=p0, end=end))
    return res

def summ(res, tag, unr):
    def share(sub):
        v = 100.0 * sum(1 for x in sub if x['diff'] > 0) / len(sub); return v
    early = [x for x in res if x['start'] <= '1980-12']; late = [x for x in res if x['start'] >= '1981-01']
    sa, se, sl = share(res), share(early), share(late)
    unr[tag] = dict(share_all=sa, share_1954_1980=se, share_1981_on=sl, n_all=len(res), n_early=len(early), n_late=len(late),
                    count_all=sum(1 for x in res if x['diff']>0), count_early=sum(1 for x in early if x['diff']>0), count_late=sum(1 for x in late if x['diff']>0))
    w = max(res, key=lambda x: x['diff']); b = min(res, key=lambda x: x['diff'])
    med = statistics.median([x['diff'] for x in res])
    unr[tag].update(median_unrounded=med, worst_unrounded=w['diff'], best_unrounded=b['diff'])
    return dict(share_costlier=r(sa,1), share_costlier_1954_1980=r(se,1), share_costlier_1981_on=r(sl,1),
                median_diff=r(med), worst_diff=r(w['diff']), worst_start=w['start'], best_diff=r(b['diff']), best_start=b['start'])

unr = {}
base = run(MARGIN)
bs = summ(base, 'base', unr)
core = dict(n_starts=len(starts), first_start=starts[0], last_start=starts[-1], fixed_total_interest=r(fixed_tot),
    share_variable_costlier=bs['share_costlier'], median_variable_minus_fixed=bs['median_diff'],
    worst_variable_minus_fixed=bs['worst_diff'], worst_start=bs['worst_start'], best_variable_minus_fixed=bs['best_diff'],
    best_start=bs['best_start'], max_variable_rate_any_window=r(max(x['maxRate'] for x in base), 2),
    max_variable_rate_start=max(base, key=lambda x: x['maxRate'])['start'],
    n_starts_1954_1980=unr['base']['n_early'], share_costlier_1954_1980=bs['share_costlier_1954_1980'],
    n_starts_1981_on=unr['base']['n_late'], share_costlier_1981_on=bs['share_costlier_1981_on'],
    index_today=INDEX, margin=r(MARGIN, 2))
unr['fixed_total_interest'] = fixed_tot
unr['max_variable_rate_any_window'] = max(x['maxRate'] for x in base)

mpw = max(base, key=lambda x: x['maxPay'])
sh = 100.0 * sum(1 for x in base if x['maxPay'] > fixed_pay) / len(base)
unr['share_windows_max_payment_above_fixed'] = sh
unr['fixed_payment'] = fixed_pay; unr['variable_first_payment'] = base[0]['p0']
unr['max_variable_payment_any_window'] = mpw['maxPay']
unr['median_window_max_payment'] = statistics.median([x['maxPay'] for x in base])
unr['windows_maxPay_rounded_cents_above_rounded_fixed'] = 100.0*sum(1 for x in base if r(x['maxPay'],2) > r(fixed_pay,2))/len(base)
payments = dict(fixed_payment=r(fixed_pay,2), variable_first_payment=r(base[0]['p0'],2),
    max_variable_payment_any_window=r(mpw['maxPay'],2), max_variable_payment_start=mpw['start'],
    median_window_max_payment=r(unr['median_window_max_payment'],2),
    share_windows_max_payment_above_fixed=r(sh,1))

gaps = {}
for g in [0.5,1.0,1.5,2.0,2.5,3.0]:
    gaps[f'{g:.1f}'] = summ(run(FIX - g - INDEX), f'gap_{g:.1f}', unr)
caps = {}
for c in [12,15,18]:
    caps[str(c)] = summ(run(MARGIN, float(c)), f'cap_{c}', unr)

windows = [dict(start=x['start'], diff=r(x['diff'],2), maxRate=r(x['maxRate'],4), maxPay=r(x['maxPay'],2)) for x in base]
unr['max_abs_end_balance_base'] = max(abs(x['end']) for x in base); unr['fixed_end_balance'] = fixed_end

interp = [
 "Months indexed k=0..119; month k uses rate_k with TB3MS[s+k]; s = start month row in CSV. Window for 2016-09 ends at 2026-08 (last row).",
 "Each month: interest = balance*rate_k/1200 (unrounded, no cent rounding of interest, payment or balance); balance <- balance + interest - payment.",
 "Payment: level annuity payment on current (start-of-month) balance at rate_k over remaining 120-k months; computed at k=0 and recomputed only when rate_k != rate_{k-1} (exact float compare). Mathematically identical to recomputing every month.",
 "Fixed loan uses the same engine at 9.00% constant (single level payment). Total interest = sum of monthly interest; no final-payment adjustment (end balance ~1e-9).",
 "index_today = last TB3MS value (2026-08) = 3.72; margin = 7.50 - 3.72 = 3.78; variable rate formula unrounded, using float arithmetic.",
 "Difference = total variable interest - total fixed interest; 'costlier' means Difference > 0 strictly.",
 "Median over 753 windows is the single middle value (odd count). Worst = max Difference, best = min Difference; ties: first (earliest) start month.",
 "max_variable_rate_any_window = max over all windows and all k of rate_k (base path).",
 "maxPay = max over k of the (unrounded) scheduled payment; share above fixed compares unrounded maxPay > unrounded fixed_payment (also reported with both rounded to cents in unrounded block).",
 "variable_first_payment = level payment of 50,000 at the window's rate_0 over 120 months (identical for all windows; reported from the first window).",
 "Gap grid: margin = 9.00 - g - 3.72; rate_k = margin + max(0, 3.72 + TB3MS[s+k] - TB3MS[s]); fixed unchanged.",
 "Cap grid: rate_k = min(c, base rate_k) with base margin 3.78; payment recomputed when the capped rate changes.",
 "Rounding: decimal ROUND_HALF_UP applied to repr of the float (not Python banker's rounding).",
 "Period splits: 1954-1980 = starts 1954-01..1980-12; 1981 on = 1981-01..2016-09; shares are % of each subgroup's start count.",
 "Windows series uses the base path (v0=7.50, no cap).",
]
json.dump(dict(core=core, payments=payments, gaps=gaps, caps=caps, windows=windows, unrounded=unr, interpretations=interp),
          open('recompute.json','w'), indent=1)
print(json.dumps(dict(core=core, payments=payments, gaps=gaps, caps=caps), indent=1))
print(json.dumps({k:v for k,v in unr.items()}, indent=1))

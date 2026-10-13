"""Tập 7 (Việc 0): 15 năm vs 30 năm trả trong 15 năm, khoản vay $320.000, phát lại mọi tuần PMMS có cả hai lãi (1991-08-30 → nay).
Đọc data/normalized/pmms_weekly.csv (fetch.py). Ghi out/model.json: {params, quantities{id: {value, unit, definition}}, series}.

    python3 episodes/ep007/model/model.py

Quy ước (giống hồ sơ topics-r2/machine/debt-1/calc.py): khoản trả đều = P*x/(1-(1+x)^-n), x = lãi/1200; chỉ gốc + lãi (không thuế nhà,
bảo hiểm, phí, điểm); làm tròn chỉ ở đầu ra. "Trả 30 năm trong 15 năm" = 180 khoản trả đều ở lãi 30 năm. Trả thêm theo năm (câu hỏi
khán giả 3): mỗi 12 tháng một lần 12 × khoản trả thêm, trả cùng khoản thứ 12, 24, … Lãi tính tháng trên dư nợ đầu tháng.
"""
import csv, json, math, os, statistics as st

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = 320000.0
LEO_WEEK = '2021-01-07'          # tuần lãi 30 năm thấp nhất từ 1991 (nhân vật đối trọng; model kiểm lại là min)
ERAS = [('1991-08-30', '1999-12-31'), ('2000-01-01', '2009-12-31'), ('2010-01-01', '2019-12-31'), ('2020-01-01', '2026-12-31')]
SRC = ('Data: Freddie Mac Primary Mortgage Market Survey via FRED (MORTGAGE30US, MORTGAGE15US; weekly averages, percent), paired weeks '
       'where both series have a value. Loan math on $320,000: level payment = P*x/(1-(1+x)^-n), x = rate/1200; principal and interest only.')


def pay(r, n, p=P):
    x = r / 1200
    return p * x / (1 - (1 + x) ** -n)


def months_to_payoff(r, payment, p=P):
    x = r / 1200
    return -math.log(1 - p * x / payment) / math.log(1 + x)


def simulate(r, base, monthly_extra=0.0, yearly_lump=0.0, p=P, cap=360):
    """Dư nợ tháng; trả base + monthly_extra mỗi tháng, thêm yearly_lump ở tháng 12, 24, …; trả về (số tháng, tổng lãi)."""
    x, bal, interest, m = r / 1200, p, 0.0, 0
    while bal > 1e-9 and m < cap:
        m += 1
        i = bal * x
        interest += i
        bal = bal + i - base - monthly_extra - (yearly_lump if m % 12 == 0 else 0.0)
    return m, interest


def main():
    rows = [(r['week'], float(r['rate30']), float(r['rate15'])) for r in csv.DictReader(open(os.path.join(EP, 'data/normalized/pmms_weekly.csv')))]
    weeks = [w for w, _, _ in rows]
    spread = [a - b for _, a, b in rows]
    extra_total = [(pay(a, 180) - pay(b, 180)) * 180 for _, a, b in rows]
    q = {}

    def put(k, v, unit, d):
        q[k] = {'value': v, 'unit': unit, 'definition': f'{SRC} {d}'}

    last, r30, r15 = rows[-1]
    p15, p30, p30_15 = pay(r15, 180), pay(r30, 360), pay(r30, 180)
    put('n_weeks', len(rows), 'weeks', 'Number of paired weeks.')
    put('first_week', weeks[0], 'date', 'First paired week.')
    put('last_week', last, 'date', 'Last paired week ("now" of the data).')
    put('r30_now', r30, 'percent', '30-year rate in the last paired week.')
    put('r15_now', r15, 'percent', '15-year rate in the last paired week.')
    put('spread_now', round(r30 - r15, 2), 'percentage points', '30-year minus 15-year rate in the last paired week.')
    put('pay15_now', round(p15, 2), 'dollars per month', 'Payment on a 15-year loan (n=180) at the last week 15-year rate.')
    put('pay30_now', round(p30, 2), 'dollars per month', 'Required payment on a 30-year loan (n=360) at the last week 30-year rate.')
    put('pay30on15_now', round(p30_15, 2), 'dollars per month', 'Payment that retires the 30-year loan in 15 years: n=180 at the last week 30-year rate.')
    put('extra_vs15_month_now', round(p30_15 - p15, 2), 'dollars per month', 'pay30on15_now minus pay15_now (unrounded inputs).')
    put('extra_vs15_total_now', round((p30_15 - p15) * 180), 'dollars', '(pay30on15_now - pay15_now) * 180, unrounded inputs: extra paid over 15 years for paying the 30-year loan on a 15-year schedule instead of taking the 15-year loan.')
    put('fallback_gap_now', round(p15 - p30, 2), 'dollars per month', 'pay15_now minus pay30_now: how much lower the 30-year required payment is than the 15-year payment.')
    put('extra_principal_needed_now', round(p30_15 - p30, 2), 'dollars per month', 'pay30on15_now minus pay30_now: extra principal each month on top of the 30-year required payment to finish in 180 months.')
    mp = months_to_payoff(r30, p15)
    put('months_at_pay15_now', round(mp, 1), 'months', 'Months to pay off the 30-year loan at the last week 30-year rate when paying exactly pay15_now each month (continuous formula).')
    put('months_late_at_pay15_now', round(mp - 180, 1), 'months', 'months_at_pay15_now minus 180.')
    put('interest_15_now', round(p15 * 180 - P), 'dollars', 'Total interest on the 15-year loan: pay15_now*180 - 320000.')
    put('interest_30on15_now', round(p30_15 * 180 - P), 'dollars', 'Total interest on the 30-year loan paid in 15 years: pay30on15_now*180 - 320000.')
    put('interest_30full_now', round(p30 * 360 - P), 'dollars', 'Total interest on the 30-year loan paid on its own 30-year schedule: pay30_now*360 - 320000.')

    # historia
    put('spread_mean', round(st.mean(spread), 2), 'percentage points', 'Mean weekly spread (30-year minus 15-year).')
    put('spread_min', round(min(spread), 2), 'percentage points', 'Smallest weekly spread.')
    put('spread_max', round(max(spread), 2), 'percentage points', 'Largest weekly spread.')
    put('share_spread_ge_050', round(sum(s >= 0.5 - 1e-9 for s in spread) / len(spread), 3), 'share of weeks', 'Share of paired weeks with spread >= 0.50 point.')
    put('extra_total_median', round(st.median(extra_total)), 'dollars', 'For every paired week: (n=180 payment at the 30-year rate - n=180 payment at the 15-year rate) * 180. Median over weeks.')
    i_min, i_max = extra_total.index(min(extra_total)), extra_total.index(max(extra_total))
    put('extra_total_min', round(extra_total[i_min]), 'dollars', 'Same weekly quantity as extra_total_median; minimum over weeks.')
    put('extra_total_min_week', weeks[i_min], 'date', 'Week of extra_total_min.')
    put('extra_total_max', round(extra_total[i_max]), 'dollars', 'Same weekly quantity as extra_total_median; maximum over weeks.')
    put('extra_total_max_week', weeks[i_max], 'date', 'Week of extra_total_max.')
    put('share_extra_ge_now', round(sum(e >= (p30_15 - p15) * 180 - 1e-9 for e in extra_total) / len(extra_total), 3), 'share of weeks',
        'Share of paired weeks whose extra_total is at least extra_vs15_total_now (unrounded).')

    # câu hỏi khán giả 1: mỗi đô la trả thêm trên khoản 30 năm "được lãi" đúng bằng lãi 30 năm (tiết kiệm lãi, trước thuế) → mốc so sánh
    r30s = [a for _, a, _ in rows]
    i_lo, i_hi = r30s.index(min(r30s)), r30s.index(max(r30s))
    put('bar_now', r30, 'percent per year', 'Return earned by each extra dollar of principal on the 30-year loan = the loan rate (interest no longer charged), before taxes: the last week 30-year rate.')
    put('r30_min', r30s[i_lo], 'percent', 'Lowest weekly 30-year rate over the paired weeks.')
    put('r30_min_week', weeks[i_lo], 'date', 'First week of r30_min.')
    put('r30_max', r30s[i_hi], 'percent', 'Highest weekly 30-year rate over the paired weeks.')
    put('r30_max_week', weeks[i_hi], 'date', 'First week of r30_max.')
    put('share_r30_ge_now', round(sum(a >= r30 - 1e-9 for a in r30s) / len(r30s), 3), 'share of weeks', 'Share of paired weeks with a 30-year rate at least r30_now.')

    # nhân vật đối trọng: tuần lãi thấp nhất
    leo = next(r for r in rows if r[0] == LEO_WEEK)
    assert leo[1] == r30s[i_lo], 'LEO_WEEK không phải tuần lãi 30 năm thấp nhất'
    lp15, lp30_15, lp30 = pay(leo[2], 180), pay(leo[1], 180), pay(leo[1], 360)
    put('leo_r30', leo[1], 'percent', f'30-year rate in the week {LEO_WEEK}.')
    put('leo_r15', leo[2], 'percent', f'15-year rate in the week {LEO_WEEK}.')
    put('leo_extra_vs15_total', round((lp30_15 - lp15) * 180), 'dollars', f'extra_total for the week {LEO_WEEK}.')
    put('leo_extra_vs15_month', round(lp30_15 - lp15, 2), 'dollars per month', f'(n=180 payment at the 30-year rate - n=180 payment at the 15-year rate) in the week {LEO_WEEK}.')
    put('leo_fallback_gap', round(lp15 - lp30, 2), 'dollars per month', f'15-year payment minus 30-year required payment in the week {LEO_WEEK}.')

    # thời kỳ
    eras = []
    for a, b in ERAS:
        idx = [k for k, w in enumerate(weeks) if a <= w <= b]
        e = {'from': weeks[idx[0]], 'to': weeks[idx[-1]], 'weeks': len(idx),
             'median_r30': round(st.median(r30s[k] for k in idx), 2), 'median_spread': round(st.median(spread[k] for k in idx), 2),
             'median_extra_total': round(st.median(extra_total[k] for k in idx))}
        eras.append(e)
        tag = a[:4]
        put(f'era{tag}_median_extra_total', e['median_extra_total'], 'dollars', f'Median weekly extra_total over paired weeks {e["from"]} to {e["to"]}.')
        put(f'era{tag}_median_r30', e['median_r30'], 'percent', f'Median weekly 30-year rate over paired weeks {e["from"]} to {e["to"]}.')
        put(f'era{tag}_median_spread', e['median_spread'], 'percentage points', f'Median weekly spread over paired weeks {e["from"]} to {e["to"]}.')

    # câu hỏi khán giả 3: trả thêm theo tháng vs một lần mỗi năm (cùng tổng mỗi năm), ở lãi 30 năm hiện tại
    extra = p30_15 - p30
    m_m, i_m = simulate(r30, p30, monthly_extra=extra)
    m_y, i_y = simulate(r30, p30, yearly_lump=12 * extra)
    put('monthly_extra_months', m_m, 'months', 'Monthly simulation at r30_now: required payment + extra_principal_needed_now every month; number of payments until the balance reaches zero.')
    put('monthly_extra_interest', round(i_m), 'dollars', 'Total interest in the monthly-extra simulation.')
    put('yearly_lump', round(12 * extra, 2), 'dollars', '12 * extra_principal_needed_now, paid once a year with payments 12, 24, ...')
    put('yearly_lump_months', m_y, 'months', 'Monthly simulation at r30_now: required payment every month + yearly_lump with payments 12, 24, ...; number of payments until the balance reaches zero.')
    put('yearly_lump_interest', round(i_y), 'dollars', 'Total interest in the yearly-lump simulation.')
    put('yearly_vs_monthly_interest', round(i_y - i_m), 'dollars', 'yearly_lump_interest minus monthly_extra_interest (unrounded).')

    out = {'model': 'ep007 15-year vs 30-year paid in 15 (weekly PMMS replay)', 'params': {'principal': P, 'termShort': 180, 'termLong': 360,
           'leoWeek': LEO_WEEK, 'eras': ERAS, 'data': 'data/normalized/pmms_weekly.csv'},
           'quantities': q, 'eras': eras,
           'series': {'weeks': weeks, 'r30': r30s, 'r15': [b for _, _, b in rows], 'extra_total': [round(e) for e in extra_total]}}
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump(out, open(os.path.join(EP, 'out/model.json'), 'w'), indent=1)
    for k, v in q.items():
        print(f'{k:32s} {v["value"]} {v["unit"]}')
    for e in eras:
        print(e)


if __name__ == '__main__':
    main()

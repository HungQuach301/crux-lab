"""Episode 1 pre-production build (M1b): model -> claims -> script (numbers filled from claims only) -> comparison table.

    python3 episodes/ep001/build.py

Writes out/model.json, out/claims.json, out/script-draft.json, script/script.md and review tables
(out/break-even-methods.csv/.md). Main break-even = counting what is still owed (model.refi.break_even_balance);
the simple division (cost / monthly saving) is shown next to it as the thesis of the episode.
Characters `median` / `small` / `large` (neutral IDs; the writer names them) are ILLUSTRATIVE: each borrowed in October 2023
at that month's average rate, has made the payments since (months to the date anchor), and refinances at the rate of the
date anchor = the latest MORTGAGE30US observation (PMMS week ending Thursday, stated as an explicit date; no relative dates).
Loan and closing cost = HMDA 2025 medians (rate-and-term refinances, first lien, 360 months) of: all sizes / under $150k /
conforming (HMDA flag C) loans of $600,000 to under $720,000, so the large loan is conforming both when borrowed in October
2023 (FHFA 2023 baseline $726,200) and today (2026 baseline $832,750): PMMS rates are conforming-loan rates
(data/cll.json, data/normalized/hmda_refi31_conforming.csv).
Pre-voice checks (DX-S7): new numbers per scene <= 2, sentence-length CV.
"""
import csv
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'model'))
import refi  # noqa: E402

FRED = {'id': 'fred-MORTGAGE30US', 'url': 'https://fred.stlouisfed.org/series/MORTGAGE30US'}
HMDA = {'id': 'hmda-lar', 'url': 'https://ffiec.cfpb.gov/data-browser/'}
OB = {'id': 'fred-OBMMIC30YF', 'url': 'https://fred.stlouisfed.org/series/OBMMIC30YF'}
WPM = 155.0
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
usd = lambda v: ('-' if v < 0 else '') + '${:,.0f}'.format(abs(v))
pct = lambda v, d=2: f'{v:.{d}f}%'
mname = lambda m: MONTHS[int(m[5:7]) - 1] + ' ' + m[:4]


def main():
    weekly = refi.load_weekly()
    monthly = refi.monthly_means(weekly)
    months = [m for m, _ in monthly]
    hm = list(csv.DictReader(open(os.path.join(HERE, 'data', 'normalized', 'hmda_refi_costs.csv'))))
    hm += list(csv.DictReader(open(os.path.join(HERE, 'data', 'normalized', 'hmda_refi31_conforming.csv'))))
    CLL = json.load(open(os.path.join(HERE, 'data', 'cll.json')))
    HS = json.load(open(os.path.join(HERE, 'data', 'hmda-sources.json')))
    fred_latest = next(f for f in json.load(open(os.path.join(HERE, 'data', 'sources.json')))['files'] if f['series'] == 'MORTGAGE30US')['latestObservation']
    H = lambda y, p, b, k: float(next(r for r in hm if r['year'] == str(y) and r['purpose'].startswith(p) and r['loanSize'] == b)[k])
    years = sorted({int(r['year']) for r in hm})
    Y, P31 = max(years), 'refinance (31)'
    last_week, r_today = weekly[-1]
    r_old = dict(monthly)['2023-10']
    k = months.index(last_week[:7]) - months.index('2023-10')  # payments made since October 2023
    peak = max(weekly, key=lambda x: x[1]); low = min(weekly, key=lambda x: x[1])
    assert fred_latest['date'] == last_week, (fred_latest, last_week)
    import datetime
    anchor = datetime.date.fromisoformat(last_week)
    anchor_txt = f"{MONTHS[anchor.month - 1]} {anchor.day}, {anchor.year}"  # e.g. September 24, 2026
    week_txt = f'PMMS week ending Thursday {anchor_txt}'
    LARGE = '$600k-<$720k, conforming (C)'
    CH = {'median': 'all sizes', 'small': 'under $150k', 'large': LARGE}
    ch = {}
    for n, band in CH.items():
        P, Cst = H(Y, P31, band, 'loan_p50_usd'), H(Y, P31, band, 'cost_p50_usd')
        b = refi.both(P, r_old, k, r_today, Cst)
        ch[n] = {'loan': P, 'cost': Cst, **b, 'net36': refi.net_after(P, r_old, k, r_today, Cst, 36), 'net84': refi.net_after(P, r_old, k, r_today, Cst, 84),
                 'cut36': refi.cut_for_break_even_balance(P, r_old, k, Cst, 36), 'cut84': refi.cut_for_break_even_balance(P, r_old, k, Cst, 84)}
    M = ch['median']
    cuts = {c: refi.both(M['loan'], r_old, k, r_old - c, M['cost']) for c in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0)}
    gap_at = refi.balance_after(M['balance'], r_today, 360, M['simple']) - refi.balance_after(M['loan'], r_old, 360, k + M['simple'])
    shares = {y: H(y, P31, 'all sizes', 'cost_p50_pct') for y in years}
    fixed = statistics.median(shares.values())
    hist = refi.history(monthly, lambda y: (shares[y], False) if y in shares else (fixed, True), spreads=(0.5, 1.0, 2.0))
    one = [(e, next(c for c in e['cases'] if c['spread'] == 1.0)) for e in hist]
    one = [(e, c) for e, c in one if c['reached']]
    bes = [c['breakEvenMonths'] for _, c in one if c['breakEvenMonths']]
    bess = [c['breakEvenSimple'] for _, c in one]
    further = [(e, c) for e, c in one if c['beforeBreakEvenAnotherDrop']]
    sh_small = {y: H(y, P31, 'under $150k', 'cost_p50_pct') for y in years}
    fx_small = statistics.median(sh_small.values())
    hist_dan = refi.history(monthly, lambda y: (sh_small[y], False) if y in sh_small else (fx_small, True), spreads=(1.0,))
    bes_dan = [c['breakEvenMonths'] for e in hist_dan for c in e['cases'] if c['reached'] and c['breakEvenMonths']]
    # the conforming upper band exists for HMDA 2025 only: one fixed share for every year, so every such number is ILLUSTRATIVE
    sh_large = H(Y, P31, LARGE, 'cost_p50_pct')
    hist_big = refi.history(monthly, lambda y: (sh_large, True), spreads=(1.0,))
    bes_big = [c['breakEvenMonths'] for e in hist_big for c in e['cases'] if c['reached'] and c['breakEvenMonths']]
    e81, c81 = next((e, c) for e, c in one if e['peak'].startswith('1981'))
    ex_e, ex_c = further[-1]
    ex_gap = months.index(ex_c['beforeBreakEvenAnotherDrop']) - months.index(ex_c['refiMonth'])
    e23, c23 = next((e, c) for e, c in one if e['peak'] == '2023-10')

    C = {}

    def claim(cid, value, display, formula, source, year=None, **kw):
        C[cid] = {'claimId': cid, 'value': value, 'display': display, 'formula': formula, 'source': source,
                  **({'dataYear': year} if isinstance(year, int) else {'dataYears': year} if year else {}),
                  'historical': bool(source) and kw.pop('historical', True), 'illustrative': kw.pop('illustrative', False),
                  **({'basis': 'nominal'} if display.startswith('$') or display.startswith('-$') else {}), 'callbacks': [], 'shownIn': [], 'spoken': [], **kw}

    ly = int(last_week[:4])
    IL = dict(illustrative=True)
    dtxt = lambda d: f"{MONTHS[int(d[5:7]) - 1]} {int(d[8:10])}, {d[:4]}"
    NAME = {'median': 'all sizes', 'small': 'under $150,000', 'large': '$600,000 to under $720,000, conforming (HMDA conforming_loan_limit = C)'}
    CLLS = {'id': 'fhfa-cll', 'url': CLL['2026']['url']}
    HMC = dict(HMDA, file='data/normalized/hmda_refi31_conforming.csv')
    # ---- date anchor and the rate world
    claim('anchor_date', last_week, anchor_txt, f'date of the latest MORTGAGE30US observation = {week_txt} (FRED: "{fred_latest["frequencyQuote"]}"; "{fred_latest["updatedQuote"]}"); every "today" number is as of this date', FRED, ly)
    claim('oct2023', 2023, 'October 2023', "month of the monthly peak that starts the latest drop episode (the characters' borrowing month: scenario)", FRED, 2023)
    claim('r_old', r_old, pct(r_old), 'monthly mean of the weekly MORTGAGE30US values dated in October 2023', FRED, 2023)
    claim('r_today', r_today, pct(r_today), f'MORTGAGE30US, {week_txt} ({last_week})', FRED, ly, asOf=last_week)
    claim('term30', 30, '30', 'loan term of the series and of the HMDA filter (loan_term = 360 months)', FRED, ly, historical=False)
    claim('seven', 7, '7', f'first digit of the MORTGAGE30US value for the {week_txt} ({pct(r_today)})', FRED, ly, asOf=last_week)
    claim('cut_today', round(r_old - r_today, 2), f'{r_old - r_today:.2f}', f'{pct(r_old)} (October 2023 monthly mean) - {pct(r_today)} ({week_txt})', FRED, [2023, ly], core=True, asOf=last_week)
    claim('k35', k, str(k), f'monthly payments counted from October 2023 to {MONTHS[anchor.month - 1]} {anchor.year} (month of the date anchor {anchor_txt}); scenario: each character has paid since borrowing', FRED, [2023, ly], **IL, asOf=last_week)
    for n, band in CH.items():
        c = ch[n]
        src, fl = (HMC, 'loan_purpose 31, first lien, 360 months, conforming_loan_limit = C, loan_amount 600,000-719,999 (10k-bin midpoints 605,000-715,000)') if n == 'large' else (HMDA, f'loan_purpose 31, first lien, 360 months, {band}')
        claim(f'loan_{n}', c['loan'], usd(c['loan']), f'median loan_amount, HMDA {Y}, {fl} (character {n}: ILLUSTRATIVE; binned amounts, so a bin midpoint)', src, Y, **IL)
        claim(f'cost_{n}', c['cost'], usd(c['cost']), f'median total_loan_costs, HMDA {Y}, {fl}', src, Y, **({'core': True, 'decisive': False} if n == 'median' else {}))
        claim(f'sav_{n}', c['monthlySavings'], usd(c['monthlySavings']), f"payment({usd(c['loan'])}, {r_old:.2f}%, 360) - payment(balance after {k} payments {usd(c['balance'])}, {r_today:.2f}% [{week_txt}], 360)", FRED, [2023, ly], model='refi.both', **IL, asOf=last_week)
        claim(f'be_simple_{n}', c['simple'], str(c['simple']), f"ceil(cost_{n} / sav_{n}) (the simple division), rate of {anchor_txt}", src, [2023, Y], model='refi.break_even_months', **IL, asOf=last_week)
        claim(f'be_bal_{n}', c['withBalance'], str(c['withBalance']), f'first month m with savings x m + (old balance - new balance) >= closing cost (counting what is still owed), rate of {anchor_txt}', src, [2023, Y],
              model='refi.break_even_balance', **IL, asOf=last_week, **({'core': True, 'decisive': True} if n == 'median' else {}))
        claim(f'net36_{n}', c['net36'], usd(abs(c['net36'])), f'net_after(36 months) = savings + balance difference - closing cost ({usd(c["net36"])}; sign shown by wording), rate of {anchor_txt}', src, [2023, Y], model='refi.net_after', **IL, asOf=last_week)
        claim(f'net84_{n}', c['net84'], usd(abs(c['net84'])), f'net_after(84 months) ({usd(c["net84"])}), rate of {anchor_txt}', src, [2023, Y], model='refi.net_after', **IL, asOf=last_week)
        claim(f'cut36_{n}', round(c['cut36'], 2), f"{c['cut36']:.2f}".rstrip('0').rstrip('.'), f'smallest rate cut below {pct(r_old)} with the balance-counting break-even <= 36 months (bisection); independent of the date anchor except through k = {k}', src, [2023, Y],
              model='refi.cut_for_break_even_balance', **IL, **({'decisive': True, 'core': True} if n == 'median' else {}))
    claim('gap24', gap_at, usd(gap_at), f"new balance - old balance after {M['simple']} months (median character), rate of {anchor_txt}", HMDA, [2023, Y], model='refi.balance_after', **IL, asOf=last_week)
    claim('hold36', 36, '36', 'payback target of the question (3 years): an assumption, not data', None, None, **IL, historical=False)
    claim('y3', 3, '3', 'holding scenario: sell after 3 years (36 months)', None, None, **IL, historical=False)
    claim('y7', 7, '7', 'holding scenario: sell after 7 years (84 months)', None, None, **IL, historical=False)
    for s, key in ((0.25, '025'), (0.5, '05'), (1.0, '10')):
        claim('s' + key, s, f'{s:g}', 'rate cut in percentage points (analysis grid)', None, None, historical=False)
    for s, key in ((0.25, '025'), (0.5, '05'), (1.0, '10')):
        claim(f'be_simple_{key}', cuts[s]['simple'], str(cuts[s]['simple']), f'simple division for the median character at a cut of {s:g} point(s) below {pct(r_old)}', HMDA, [2023, Y], model='refi.both', **IL)
        if cuts[s]['withBalance']:
            claim(f'be_bal_{key}', cuts[s]['withBalance'], str(cuts[s]['withBalance']), f'balance-counting break-even for the median character at a cut of {s:g} point(s) below {pct(r_old)}', HMDA, [2023, Y], model='refi.both', **IL)
        else:
            claim(f'be_bal_{key}', None, 'never', f'balance-counting break-even for the median character at a cut of {s:g} point(s): not reached before the old loan ends', HMDA, [2023, Y], model='refi.both', **IL)
    claim('y1971', 1971, '1971', 'first observation of MORTGAGE30US (week of 1971-04-02)', FRED, 1971)
    claim('y2025', Y, str(Y), 'latest HMDA data year used', HMDA, Y)
    claim('y2018', min(years), str(min(years)), 'first HMDA year with total_loan_costs', HMDA, min(years))
    claim('y2017', 2017, '2017', 'first year of OBMMIC30YF (2017-01-03)', OB, 2017)
    claim('n31', int(H(Y, P31, 'all sizes', 'n')), '{:,}'.format(int(H(Y, P31, 'all sizes', 'n'))), f'count, HMDA {Y}, loan_purpose 31, originated, first lien, 360 months, total_loan_costs > 0', HMDA, Y)
    claim('cost_p25', H(Y, P31, 'all sizes', 'cost_p25_usd'), usd(H(Y, P31, 'all sizes', 'cost_p25_usd')), '25th percentile, same population', HMDA, Y)
    claim('cost_p75', H(Y, P31, 'all sizes', 'cost_p75_usd'), usd(H(Y, P31, 'all sizes', 'cost_p75_usd')), '75th percentile, same population', HMDA, Y)
    claim('band150', 150000, '$150,000', 'loan-size band edge (analysis parameter)', None, None, role='axis', historical=False)
    claim('band750', 750000, '$750,000', 'loan-size band edge (analysis parameter; context band, not a character)', None, None, role='axis', historical=False)
    claim('band600', 600000, '$600,000', 'lower edge of the large character band (analysis parameter)', None, None, role='axis', historical=False)
    claim('band720', 720000, '$720,000', 'upper edge (exclusive) of the large character band: keeps the October 2023 loan under the 2023 baseline limit (analysis parameter)', None, None, role='axis', historical=False)
    for yy in ('2023', '2025', '2026'):
        claim(f'cll{yy}', CLL[yy]['value'], usd(CLL[yy]['value']), f'FHFA baseline conforming loan limit {yy}, one-unit property, most of the US ({CLL[yy]["how"]})', {'id': 'fhfa-cll', 'url': CLL[yy]['url']}, int(yy), historical=yy != '2026')
    claim('share_small', H(Y, P31, 'under $150k', 'cost_p50_pct'), pct(H(Y, P31, 'under $150k', 'cost_p50_pct'), 1), f'median total_loan_costs / loan_amount, HMDA {Y}, loan_purpose 31, loans under $150k', HMDA, Y)
    claim('share_median', H(Y, P31, 'all sizes', 'cost_p50_pct'), pct(H(Y, P31, 'all sizes', 'cost_p50_pct'), 1), f'median total_loan_costs / loan_amount, HMDA {Y}, loan_purpose 31, all sizes', HMDA, Y)
    claim('share_large', H(Y, P31, LARGE, 'cost_p50_pct'), pct(H(Y, P31, LARGE, 'cost_p50_pct'), 1), f'median total_loan_costs / loan_amount, HMDA {Y}, loan_purpose 31, conforming (C), $600,000 to under $720,000', HMC, Y)
    claim('n_large', int(H(Y, P31, LARGE, 'n')), '{:,}'.format(int(H(Y, P31, LARGE, 'n'))), f'count of loans in the large character band, HMDA {Y}', HMC, Y)
    claim('n_small', int(H(Y, P31, 'under $150k', 'n')), '{:,}'.format(int(H(Y, P31, 'under $150k', 'n'))), f'count of loans in the small character band, HMDA {Y}', HMDA, Y)
    claim('n_eps', len(hist), str(len(hist)), 'drop episodes: zig-zag swings of the monthly mean rate of >= 1.00 point', FRED, [1971, ly], model='refi.drop_episodes')
    claim('beh_min', min(bes), str(min(bes)), 'min balance-counting break-even over the episodes, refinance at a 1-point cut ($300,000 ILLUSTRATIVE loan)', FRED, [1971, ly], model='refi.history')
    claim('beh_max', max(bes), str(max(bes)), 'max of the same', FRED, [1971, ly], model='refi.history')
    claim('behs_min', min(bess), str(min(bess)), 'min simple-division break-even over the same cases', FRED, [1971, ly], model='refi.history')
    claim('behs_max', max(bess), str(max(bess)), 'max of the same', FRED, [1971, ly], model='refi.history')
    claim('n_further', len(further), str(len(further)), 'episodes where the rate fell another full point before the balance-counting break-even', FRED, [1971, ly], model='refi.history')
    claim('n_nofurther', len(one) - len(further), str(len(one) - len(further)), 'the other episodes', FRED, [1971, ly], model='refi.history')
    claim('ex_peak', int(ex_e['peak'][:4]), mname(ex_e['peak']), 'peak month of the example episode', FRED, int(ex_e['peak'][:4]))
    claim('ex_refi', int(ex_c['refiMonth'][:4]), mname(ex_c['refiMonth']), 'refinance month (first month 1 point under the peak)', FRED, int(ex_c['refiMonth'][:4]))
    claim('ex_be', ex_c['breakEvenMonths'], str(ex_c['breakEvenMonths']), 'balance-counting break-even of the example', FRED, int(ex_c['refiMonth'][:4]), model='refi.history', illustrative=bool(ex_c['costIllustrative']))
    claim('ex_gap', ex_gap, str(ex_gap), 'months from that refinance to the first month another full point lower', FRED, int(ex_c['refiMonth'][:4]), model='refi.history')
    claim('r23', int(c23['refiMonth'][:4]), mname(c23['refiMonth']), 'first month 1 point under the October 2023 peak', FRED, int(c23['refiMonth'][:4]))
    claim('be23', c23['breakEvenMonths'], str(c23['breakEvenMonths']), f"balance-counting break-even at that month, HMDA {c23['refiMonth'][:4]} cost share", HMDA, int(c23['refiMonth'][:4]), model='refi.history')
    claim('behd_min', min(bes_dan), str(min(bes_dan)), 'min balance-counting break-even over the episodes with the under-$150k cost share (small-character-like loans)', HMDA, [1971, ly], model='refi.history', illustrative=True)
    claim('behd_max', max(bes_dan), str(max(bes_dan)), 'max of the same', HMDA, [1971, ly], model='refi.history', illustrative=True)
    claim('behl_max', max(bes_big), str(max(bes_big)), f'max balance-counting break-even over the episodes with the large band cost share of {Y} ({pct(sh_large, 2)}) applied to every year', HMC, [1971, ly], model='refi.history', illustrative=True)
    claim('y1981', int(peak[0][:4]), peak[0][:4], f'year of the weekly maximum ({peak[0]})', FRED, int(peak[0][:4]))
    claim('m81', c81['monthsOnOldLoan'], str(c81['monthsOnOldLoan']), 'months from the 1981-10 monthly peak to the first month 1 point lower', FRED, 1981, model='refi.history')
    claim('be81', c81['breakEvenMonths'], str(c81['breakEvenMonths']), 'balance-counting break-even of that refinance (fixed pre-HMDA cost share)', FRED, 1981, model='refi.history', illustrative=True)
    claim('peak', peak[1], pct(peak[1]), f'max of MORTGAGE30US weekly (week ending {dtxt(peak[0])})', FRED, int(peak[0][:4]), date=peak[0])
    claim('low', low[1], pct(low[1]), f'min of MORTGAGE30US weekly (week ending {dtxt(low[0])})', FRED, int(low[0][:4]), date=low[0])
    # ---- context facts (sourced; the writer may use them)
    wk = dict(weekly)
    claim('low_date', low[0], dtxt(low[0]), 'week of the all-time weekly low of MORTGAGE30US', FRED, int(low[0][:4]))
    claim('rise_since_low', round(r_today - low[1], 2), f'{r_today - low[1]:.2f}', f'{pct(r_today)} ({anchor_txt}) - {pct(low[1])} ({dtxt(low[0])}), percentage points', FRED, [int(low[0][:4]), ly], asOf=last_week)
    p23 = max(((d, v) for d, v in weekly if d.startswith('2023')), key=lambda x: x[1])
    claim('peak2023', p23[1], pct(p23[1]), f'max weekly MORTGAGE30US in 2023 (week ending {dtxt(p23[0])})', FRED, 2023, date=p23[0])
    prev = max((d for d, v in weekly if d < p23[0] and v >= p23[1]), default=None)
    if prev:
        claim('peak2023_since', int(prev[:4]), prev[:4], f'last week before {p23[0]} with a weekly rate >= {pct(p23[1])} (week ending {dtxt(prev)}, {pct(wk[prev])}): "highest since {prev[:4]}"', FRED, int(prev[:4]), date=prev)
    prev_t = max((d for d, v in weekly if d < last_week and v >= r_today), default=None)
    claim('today_since', prev_t, dtxt(prev_t), f'last week before {anchor_txt} with a weekly rate >= {pct(r_today)} ({pct(wk[prev_t])})', FRED, int(prev_t[:4]), date=prev_t)
    ya = max(d for d, v in weekly if d <= (anchor - datetime.timedelta(days=364)).isoformat())
    claim('r_year_ago', wk[ya], pct(wk[ya]), f'MORTGAGE30US, week ending {dtxt(ya)} (52 weeks before the date anchor)', FRED, int(ya[:4]), date=ya)
    cx25, cx23 = HS['context'][f'conforming{Y}'], HS['context']['purchaseRates2023']
    claim('n31_conforming', cx25['n_31_flag']['C'], '{:,}'.format(cx25['n_31_flag']['C']), f'of the n31 loans, count with conforming_loan_limit = C (HMDA {Y})', HMDA, Y)
    claim('conv_share31', round(cx25['conventional_share_31_pct'], 1), pct(cx25['conventional_share_31_pct'], 0), f'share of the n31 loans with loan_type = 1 (conventional; the rest FHA/VA/USDA), HMDA {Y}', HMDA, Y)
    claim('rate31_p50', cx25['rate_31_p50'], pct(cx25['rate_31_p50']), f'median interest_rate of the n31 loans (new rate-and-term refinances originated in {Y})', HMDA, Y)
    claim('purch23_ge7', round(cx23['share_ge_7_pct'], 1), pct(cx23['share_ge_7_pct'], 0), 'share of 2023 home-purchase originations (first lien, 360 months, interest_rate reported) with interest_rate >= 7.00%', HMDA, 2023)
    claim('purch23_n_ge7', cx23['n_ge_7'], '{:,}'.format(cx23['n_ge_7']), 'count of the same loans at >= 7.00%', HMDA, 2023)
    claim('purch23_n', cx23['n_purchase_rate_valid'], '{:,}'.format(cx23['n_purchase_rate_valid']), '2023 home-purchase originations, first lien, 360 months, interest_rate reported', HMDA, 2023)

    # script
    lines, act = [], None
    tpl_all = open(os.path.join(HERE, 'script', 'script.tpl.md')).read()
    missing = sorted({i for i in re.findall(r'\{\{(\w+)\}\}', tpl_all) if i not in C})
    render = not missing  # a stale template (old claim IDs) is not rendered: script.md is left as it is
    for raw in (tpl_all.splitlines() if render else []):
        raw = raw.rstrip('\n')
        if act is None and not raw.startswith('@act'):
            continue
        if raw.startswith('@act'):
            act = raw.split()[1]; continue
        if not raw.strip() or raw.startswith('#') or '|' not in raw:
            continue
        scene, tpl = [x.strip() for x in raw.split('|', 1)]
        ids = re.findall(r'\{\{(\w+)\}\}', tpl)
        text = re.sub(r'\{\{(\w+)\}\}', lambda m: C[m.group(1)]['display'], tpl)
        sid = scene + '.1'
        lines.append({'id': sid, 'act': act, 'scene': scene, 'text': text, 'claims': ids})
        for cid in ids:
            C[cid]['spoken'].append({'sentence': sid})
            if scene not in C[cid]['shownIn']:
                C[cid]['shownIn'].append(scene)
    MEAN = {'cost_median': {'a1-median': 'the median character\'s bill is the national median', 'a3-median': 'a median: half paid more'},
            'be_bal_median': {'a3-today': 'what the cut of the anchor date means for the median character'},
            'cut_today': {}}
    for cid, m in MEAN.items():
        C[cid]['callbacks'] = [{'scene': s, 'meaning': v} for s, v in m.items() if s in C[cid]['shownIn']]
    words = [len(re.findall(r"[\w$%.,'-]+", l['text'])) for l in lines]
    seen, per_scene = set(), {}
    for l in lines:
        new = [c for c in l['claims'] if c not in seen and C[c].get('role') != 'axis']
        seen |= set(l['claims']); per_scene[l['scene']] = new
    report = {'sentences': len(lines), 'words': sum(words), 'estSpeechSeconds': round(sum(words) / WPM * 60, 1),
              'newNumbers': len([c for c in seen if C[c].get('role') != 'axis']), 'scenesOver2New': {s: n for s, n in per_scene.items() if len(n) > 2},
              'sentenceLengthCV': round(statistics.pstdev(words) / statistics.mean(words), 3) if words else None, 'claims': len(C), 'unusedClaims': [c for c in C if not C[c]['spoken']]}
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    json.dump({'claims': list(C.values())}, open(os.path.join(HERE, 'out', 'claims.json'), 'w'), indent=1)
    json.dump({'scenario': {'borrowed': '2023-10', 'oldRate': r_old, 'paymentsMade': k, 'todayWeek': last_week, 'todayRate': r_today},
               'characters': ch, 'medianByCut': cuts, 'dateAnchor': {'date': last_week, 'text': anchor_txt, 'meaning': week_txt, 'fred': fred_latest}, 'largeBand': LARGE, 'conformingLimits': CLL, 'gapAtSimpleBreakEven': gap_at, 'costSharesByYear': shares, 'fixedSharePre2018': fixed, 'history': hist},
              open(os.path.join(HERE, 'out', 'model.json'), 'w'), indent=1)
    if render:
        json.dump({'sentences': lines, 'check': report}, open(os.path.join(HERE, 'out', 'script-draft.json'), 'w'), indent=1)
    report['templateMissingClaims'] = missing
    report['scriptRendered'] = render
    for f_ in ([] if render else [0]):
        print('script/script.tpl.md uses claim IDs not in claims.json; script.md NOT regenerated:', missing[:12], '...' if len(missing) > 12 else '')
    with (open(os.path.join(HERE, 'script', 'script.md'), 'w') if render else open(os.devnull, 'w')) as f:
        f.write('# Episode 1 — script M1b (generated from script.tpl.md and out/claims.json; do not edit)\n')
        a = None
        for l in lines:
            if l['act'] != a:
                a = l['act']; f.write(f'\n## {a}\n\n')
            f.write(f"- `{l['scene']}` {l['text']}\n")
    # comparison table of the two methods
    rows = []
    for n in CH:
        c = ch[n]
        rows.append({'case': f'{n} ({anchor_txt}, cut {r_old - r_today:.2f} pt)', 'loan': usd(c['loan']), 'closingCost': usd(c['cost']), 'monthlySaving': usd(c['monthlySavings']),
                     'simpleMonths': c['simple'], 'withBalanceMonths': c['withBalance'] or 'never', 'net3y': usd(c['net36']), 'net7y': usd(c['net84']), 'cutFor36m': f"{c['cut36']:.2f}"})
    for s, b in cuts.items():
        rows.append({'case': f'median, cut {s:g} pt', 'loan': usd(M['loan']), 'closingCost': usd(M['cost']), 'monthlySaving': usd(b['monthlySavings']),
                     'simpleMonths': b['simple'], 'withBalanceMonths': b['withBalance'] or 'never', 'net3y': '', 'net7y': '', 'cutFor36m': ''})
    for e, c in one:
        rows.append({'case': f"history {e['peak']} -> refi {c['refiMonth']} (1 pt){' *' if c['costIllustrative'] else ''}", 'loan': '$300,000 (ILLUSTRATIVE)', 'closingCost': usd(c['closingCost']),
                     'monthlySaving': usd(c['monthlySavings']), 'simpleMonths': c['breakEvenSimple'], 'withBalanceMonths': c['breakEvenMonths'] or 'never', 'net3y': '', 'net7y': '', 'cutFor36m': ''})
    with open(os.path.join(HERE, 'out', 'break-even-methods.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()

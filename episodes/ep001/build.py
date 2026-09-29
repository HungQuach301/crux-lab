"""Episode 1 pre-production build (M1b): model -> claims -> script (numbers filled from claims only) -> comparison table.

    python3 episodes/ep001/build.py

Writes out/model.json, out/claims.json (spoken/shownIn/callbacks from out/script-draft.json = story/script.md) and review tables
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
        claim('s' + key, s, f'{s:g}', 'rate cut in percentage points (analysis grid; an analyst choice, not data)', None, None, historical=False, illustrative=True)
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
        claim(f'cll{yy}', CLL[yy]['value'], usd(CLL[yy]['value']), f'FHFA baseline conforming loan limit {yy}, one-unit property, most of the US ({CLL[yy]["how"]})', {'id': 'fhfa-cll', 'url': CLL[yy]['url']}, int(yy), historical=yy != '2026',
              ownerVerified=CLL[yy].get('verifiedBy') == 'project owner', **({'released': CLL[yy]['released']} if CLL[yy].get('released') else {}))
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
    # cold-open sentence (cold open A): "In October 2023, the average 30-year fixed mortgage rate in the US hit its highest level since 2000."
    # peak week of October 2023 vs every week since 2000-01-01; "since 2000" = no week after the last week of 2000 with a value >= the peak
    pk = max(((d, v) for d, v in weekly if d.startswith('2023-10')), key=lambda x: x[1])
    after = [(d, v) for d, v in weekly if d > pk[0]]
    assert pk == p23 and not any(v > pk[1] for d, v in after if d.startswith('2023')), (pk, p23)
    tie = max(d for d, v in weekly if d < pk[0] and v >= pk[1])            # last week before the peak at or above it
    above = max(d for d, v in weekly if d < pk[0] and v > pk[1])           # last week before the peak strictly above it
    first_after_tie = min(d for d, v in weekly if d > tie)
    mm = dict(monthly)
    tie_m = max(m for m, v in monthly if m < '2023-10' and v >= mm['2023-10'])
    assert tie[:4] == above[:4] == tie_m[:4] == '2000' and pk[1] == max(v for d, v in weekly if d > tie)
    claim('peak_since2000', int(tie[:4]), tie[:4],
          f'week ending {dtxt(pk[0])} = highest weekly MORTGAGE30US value of October 2023 ({pct(pk[1])}); the last earlier week with a value >= {pct(pk[1])} is the week ending '
          f'{dtxt(tie)} ({pct(wk[tie])}, equal), the last earlier week strictly above it is the week ending {dtxt(above)} ({pct(wk[above])}); no week from {dtxt(first_after_tie)} '
          f'to {dtxt(max(d for d in wk if d < pk[0]))} reached {pct(pk[1])}. "Highest since 2000" = the highest weekly value since the week ending {dtxt(tie)} '
          f'(tied with that week; above every week since {dtxt(first_after_tie)}). Monthly means agree: October 2023 ({pct(mm["2023-10"])}) is the highest monthly mean '
          f'since {mname(tie_m)} ({pct(mm[tie_m], 3)}). Search window: whole series from 2000-01-01.', FRED, [int(tie[:4]), 2023], date=tie,
          peakWeek=pk[0], peakValue=pk[1], lastWeekAtOrAbove=tie, lastWeekAbove=above, noWeekAtOrAboveFrom=first_after_tie, lastMonthAtOrAbove=tie_m,
          sentence='In October 2023, the average 30-year fixed mortgage rate in the US hit its highest level since 2000.',
          meaning=f'Freddie Mac PMMS weekly average (FRED MORTGAGE30US), week ending {dtxt(pk[0])}: {pct(pk[1])}, a level no week had reached since the week ending {dtxt(tie)}')
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
    # ---- spoken-word variants (each points to its parent claim; value = the parent's value)
    sw = ch['small']['cost'] / ch['small']['loan'] * 100
    claim('share_walt', round(sw, 3), f'about {sw:.1f}%', f"cost_small / loan_small = {usd(ch['small']['cost'])} / {usd(ch['small']['loan'])} (the small character's own bill as a share of the loan; differs from share_small = median of per-loan shares)", HMDA, Y, parent=['cost_small', 'loan_small'], **IL)
    def words(cid, parent, display, why):
        claim(cid, C[parent]['value'], display, f'spoken form of {parent} ({C[parent]["display"]}): {why}', C[parent]['source'], C[parent].get('dataYear', C[parent].get('dataYears')),
              parent=parent, spokenForm=True, illustrative=C[parent]['illustrative'], **({'asOf': C[parent]['asOf']} if C[parent].get('asOf') else {}))
    assert 450_000 <= C['n31']['value'] < 500_000
    words('n31_approx', 'n31', 'nearly half a million', '450,000 <= n31 < 500,000')
    assert 0.5 < C['cut_today']['value'] < 0.625
    words('cut_today_words', 'cut_today', 'just over half a point', '0.50 < cut_today < 0.625 (percentage points)')
    assert 0.29 <= C['cut36_large']['value'] <= 0.37
    words('cut36_large_words', 'cut36_large', 'about a third of a point', '|cut36_large - 1/3| <= 0.04 point')
    assert 29 <= C['purch23_ge7']['value'] < 31.5
    words('purch23_words', 'purch23_ge7', 'three in ten', 'purch23_ge7 rounds to 30% (share of 2023 home-purchase originations at >= 7.00%)')
    claim('ge7_threshold', 7.0, 'seven percent', 'threshold of purch23_ge7 (interest_rate >= 7.00): an analysis parameter chosen by us (round number; the anchor-date rate 7.03% is just above it), not a sourced figure', None, None, historical=False, role='parameter', illustrative=True)

    # the character each character-level claim belongs to (checks/CONTRACT.md claims.character = a key of the contract's characters)
    for cid, c in C.items():
        base = c['parent'] if isinstance(c.get('parent'), str) else cid
        n = base.rsplit('_', 1)[-1]
        # cost_<n> is left untagged: it is the real HMDA median of the band (not ILLUSTRATIVE), the other fields are the illustrative person's
        if n in CH and base.split('_')[0] in ('loan', 'sav', 'be', 'net36', 'net84', 'cut36'):
            c['character'] = n

    # script: the approved story/script.md (v2), converted by preprod/script_from_story.py into out/script-draft.json.
    # The old template script (script/script.tpl.md) is retired; build.py no longer writes any script file.
    dp = os.path.join(HERE, 'out', 'script-draft.json')
    lines = [r for r in json.load(open(dp))['sentences'] if r.get('claims')] if os.path.exists(dp) else []
    unknown = sorted({c for l in lines for c in l['claims'] if c not in C})
    assert not unknown, f'story/script.md uses claim IDs not in claims.json: {unknown}'
    for l in lines:
        for cid in l['claims']:
            if l['kind'] == 'line':
                C[cid]['spoken'].append({'sentence': l['id']})
            if l['scene'] not in C[cid]['shownIn']:
                C[cid]['shownIn'].append(l['scene'])
    # callbacks: a number that comes back in a later scene, and what it means there (script v2)
    MEAN = {'cost_median': {'S10': 'the bill from the letter, now said: the real 2025 median', 'S23': 'Nora\'s bill beside Walt\'s and Anjali\'s'},
            'sav_median': {'S14': 'the same monthly saving, now stacked month by month', 'S27': 'Nora\'s saving as the yardstick for Anjali\'s'},
            'be_bal_median': {'S21': 'her real offer pays back at month 30: inside three years'},
            'be_simple_median': {'S12': 'two years, said in words'},
            'cut_today': {'S21': 'her real offer clears the half-point line'},
            'cut_today_words': {'S21': 'her real offer clears the half-point line'},
            'cut36_median': {'S29': 'the answer for Nora, beside Anjali and Walt'},
            'cut36_small': {'S29': 'the answer for Walt'}, 'cut36_large_words': {'S29': 'the answer for Anjali'},
            'hold36': {'S20': 'the full point is inside three years', 'S21': 'the three-year line decides', 'S29': 'the answer is stated for three years'},
            'k35': {'S15': 'the 35 payments already made are what the reset throws away'},
            'y3': {'S28': 'Anjali at three years', 'S31': 'one of the two horizons'}, 'y7': {'S31': 'one of the two horizons'},
            's10': {'S32': 'the one-point line is an analyst choice', 'S33': 'history of one-point drops'},
            'anchor_date': {'S32': 'date of the rate used'}, 'r_old': {'S32': 'method: how the old rate is set'}, 'r_today': {'S32': 'method: how the new rate is set'},
            'y2025': {'S32': 'method: data year'}, 'ge7_threshold': {'S32': 'analyst choice'}, 'term30': {'S32': 'method: new loan term'}}
    for cid, m in MEAN.items():
        C[cid]['callbacks'] = [{'scene': s, 'meaning': v} for s, v in m.items() if s in C[cid]['shownIn']]
    words = [len(re.findall(r"[\w$%.,'-]+", l['text'])) for l in lines]
    seen = set()
    for l in lines:
        seen |= set(l['claims'])
    report = {'scriptSource': 'story/script.md via out/script-draft.json', 'rowsWithClaims': len(lines), 'claims': len(C), 'claimsUsed': len(seen),
              'unusedClaims': [c for c in C if c not in seen]}
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    json.dump({'claims': list(C.values())}, open(os.path.join(HERE, 'out', 'claims.json'), 'w'), indent=1)
    json.dump({'scenario': {'borrowed': '2023-10', 'oldRate': r_old, 'paymentsMade': k, 'todayWeek': last_week, 'todayRate': r_today},
               'characters': ch, 'medianByCut': cuts, 'dateAnchor': {'date': last_week, 'text': anchor_txt, 'meaning': week_txt, 'fred': fred_latest}, 'largeBand': LARGE, 'conformingLimits': CLL, 'gapAtSimpleBreakEven': gap_at, 'costSharesByYear': shares, 'fixedSharePre2018': fixed, 'history': hist},
              open(os.path.join(HERE, 'out', 'model.json'), 'w'), indent=1)
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

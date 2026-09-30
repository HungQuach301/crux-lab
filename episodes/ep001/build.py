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
              model='refi.break_even_balance', **IL, asOf=last_week, **({'core': False, 'decisive': True} if n == 'median' else {}))
        claim(f'net36_{n}', c['net36'], usd(abs(c['net36'])), f'net_after(36 months) = savings + balance difference - closing cost ({usd(c["net36"])}; sign shown by wording), rate of {anchor_txt}', src, [2023, Y], model='refi.net_after', **IL, asOf=last_week)
        claim(f'net84_{n}', c['net84'], usd(abs(c['net84'])), f'net_after(84 months) ({usd(c["net84"])}), rate of {anchor_txt}', src, [2023, Y], model='refi.net_after', **IL, asOf=last_week)
        claim(f'cut36_{n}', round(c['cut36'], 2), f"{c['cut36']:.2f}".rstrip('0').rstrip('.'), f'smallest rate cut below {pct(r_old)} with the balance-counting break-even <= 36 months (bisection); independent of the date anchor except through k = {k}', src, [2023, Y],
              model='refi.cut_for_break_even_balance', **IL, **({'decisive': True, 'core': True} if n == 'median' else {'decisive': True} if n == 'small' else {}))
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
    claim('band150', 150000, '$150,000', 'loan-size band edge (analysis parameter)', None, None, role='axis', historical=False, **IL)
    claim('band750', 750000, '$750,000', 'loan-size band edge (analysis parameter; context band, not a character)', None, None, role='axis', historical=False, **IL)
    claim('band600', 600000, '$600,000', 'lower edge of the large character band (analysis parameter)', None, None, role='axis', historical=False, **IL)
    claim('band720', 720000, '$720,000', 'upper edge (exclusive) of the large character band: keeps the October 2023 loan under the 2023 baseline limit (analysis parameter)', None, None, role='axis', historical=False, **IL)
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
    # ---- context: the refinance window of 2026 opened and is closing (weekly MORTGAGE30US; the year 2026 runs to the date anchor)
    wy = [(d, v) for d, v in weekly if d.startswith(str(ly))]
    lo26 = min(wy, key=lambda x: (x[1], x[0]))
    assert [d for d, v in wy if v == lo26[1]] == [lo26[0]], 'the 2026 low is not unique'
    claim('low2026', lo26[1], pct(lo26[1]), f'min weekly MORTGAGE30US from the first week of {ly} to the date anchor (week ending {dtxt(lo26[0])}; {len(wy)} weeks, {dtxt(wy[0][0])}-{anchor_txt})',
          FRED, ly, date=lo26[0], asOf=last_week)
    claim('low2026_date', lo26[0], dtxt(lo26[0]), f'week of low2026 ({pct(lo26[1])}): PMMS week ending Thursday {dtxt(lo26[0])}', FRED, ly, date=lo26[0], asOf=last_week)
    lo26_tie = max(d for d, v in weekly if d < lo26[0] and v <= lo26[1])     # last earlier week at or below the 2026 low
    lo26_below6 = max(d for d, v in weekly if d < lo26[0] and v < 6.0)         # last earlier week under 6.00%
    yrs = (datetime.date.fromisoformat(lo26[0]) - datetime.date.fromisoformat(lo26_tie)).days / 365.25
    assert 3 < yrs < 4 and lo26_below6 == lo26_tie
    claim('low2026_since', lo26_tie, mname(lo26_tie),
          f'last week before {dtxt(lo26[0])} with a weekly rate <= {pct(lo26[1])}: week ending {dtxt(lo26_tie)} ({pct(wk[lo26_tie])}); no week from '
          f'{dtxt(min(d for d in wk if d > lo26_tie))} to {dtxt(max(d for d in wk if d < lo26[0]))} was at or below {pct(lo26[1])} ({yrs:.2f} years). '
          f'"Lowest since September 2022" and "lowest in more than three years" are both true; it was also the first week under 6% since {dtxt(lo26_below6)}',
          FRED, [int(lo26_tie[:4]), ly], date=lo26_tie, yearsBetween=round(yrs, 2), lastWeekUnder6=lo26_below6,
          sentence=f'In the week ending {dtxt(lo26[0])}, the average 30-year rate fell to {pct(lo26[1])}, its lowest since September 2022.')
    j26 = ('2026-01-15', wk['2026-01-15'])
    j26_tie = max(d for d, v in weekly if d < j26[0] and v <= j26[1])
    assert j26[1] == 6.06 and j26[1] > lo26[1]
    claim('jan2026', j26[1], pct(j26[1]),
          f'MORTGAGE30US, week ending Thursday {dtxt(j26[0])}: at that time the lowest since the week ending {dtxt(j26_tie)} ({pct(wk[j26_tie])}); NOT the 2026 low '
          f'(low2026 = {pct(lo26[1])}, {dtxt(lo26[0])}). There is no PMMS week dated January 12, 2026 (a Monday)', FRED, ly, date=j26[0], lowestSince=j26_tie)
    claim('jan2026_since', j26_tie, mname(j26_tie), f'last week before {dtxt(j26[0])} with a weekly rate <= {pct(j26[1])}: week ending {dtxt(j26_tie)} ({pct(wk[j26_tie])})',
          FRED, [int(j26_tie[:4]), ly], date=j26_tie, parent='jan2026')
    claim('cut_low2026', round(r_old - lo26[1], 2), f'{r_old - lo26[1]:.2f}', f'{pct(r_old)} (r_old, October 2023 monthly mean) - {pct(lo26[1])} (low2026, week ending {dtxt(lo26[0])}), percentage points',
          FRED, [2023, ly])
    k26 = months.index(lo26[0][:7]) - months.index('2023-10')  # same convention as k35: months from October 2023 to the refinance month
    Ml, Mc = M['loan'], M['cost']
    b26 = refi.both(Ml, r_old, k26, lo26[1], Mc)
    claim('k_low2026', k26, str(k26), f'monthly payments counted from October 2023 to {mname(lo26[0])} (month of low2026), same convention as k35', FRED, [2023, ly], **IL)
    fl26 = f'median character (loan_median {usd(Ml)}, cost_median {usd(Mc)}), borrowed October 2023 at {pct(r_old)}, refinancing in the week of low2026 ({dtxt(lo26[0])}, {pct(lo26[1])}) after {k26} payments'
    claim('sav_low2026_median', b26['monthlySavings'], usd(b26['monthlySavings']), f"payment({usd(Ml)}, {r_old:.2f}%, 360) - payment(balance after {k26} payments {usd(b26['balance'])}, {lo26[1]:.2f}%, 360): {fl26}",
          FRED, [2023, ly], model='refi.both', **IL)
    claim('be_simple_low2026_median', b26['simple'], str(b26['simple']), f'ceil(cost_median / sav_low2026_median) (the simple division): {fl26}', HMDA, [2023, Y], model='refi.break_even_months', **IL)
    claim('be_bal_low2026_median', b26['withBalance'], str(b26['withBalance']), f'refi.break_even_balance (counting what is still owed): {fl26}', HMDA, [2023, Y], model='refi.break_even_balance', **IL)
    f7 = max(d for d, v in weekly if d < last_week and v >= 7.0)
    below7 = [d for d, v in weekly if f7 < d < last_week]
    assert all(wk[d] < 7.0 for d in below7)
    claim('first7_since', f7, mname(f7), f'{anchor_txt} ({pct(r_today)}) is the first week at or above 7.00% since the week ending {dtxt(f7)} ({pct(wk[f7])}); '
          f'the {len(below7)} weeks in between ({dtxt(below7[0])}-{dtxt(below7[-1])}) were all under 7.00%. Same week as today_since (threshold {pct(r_today)}), different threshold',
          FRED, [int(f7[:4]), ly], date=f7, weeksUnder7=len(below7), asOf=last_week)
    wks = weekly.index((last_week, r_today)) - weekly.index(lo26)
    assert (anchor - datetime.date.fromisoformat(lo26[0])).days == 7 * wks
    claim('rise_since_low2026', round(r_today - lo26[1], 2), f'{r_today - lo26[1]:.2f}', f'{pct(r_today)} ({anchor_txt}) - {pct(lo26[1])} (low2026, {dtxt(lo26[0])}), percentage points, over {wks} weeks',
          FRED, ly, weeks=wks, asOf=last_week)
    claim('weeks_rise_since_low2026', wks, str(wks), f'weekly observations from {dtxt(lo26[0])} to {anchor_txt} (both PMMS Thursdays; {wks} x 7 days)', FRED, ly, parent='rise_since_low2026', asOf=last_week)
    thr = round(r_old - 1.0, 2)
    win = [(d, v) for d, v in wy if v <= thr + 1e-9]
    i0 = weekly.index(win[0])
    while i0 > 0 and weekly[i0 - 1][1] <= thr + 1e-9:
        i0 -= 1
    i1 = weekly.index(win[-1])
    assert weekly[i0:i1 + 1] == [x for x in weekly[i0:i1 + 1] if x[1] <= thr + 1e-9] and all(v > thr for d, v in weekly[i1 + 1:])
    claim('weeks_below_r_old_minus_1', len(win), str(len(win)), f'weeks of {ly} (to the date anchor) with MORTGAGE30US <= {pct(thr)} (r_old {pct(r_old)} minus 1.00 point): '
          f'{dtxt(win[0][0])}-{dtxt(win[-1][0])}, consecutive; the same run began the week ending {dtxt(weekly[i0][0])} ({i1 - i0 + 1} weeks in all) and every week after '
          f'{dtxt(win[-1][0])} is above {pct(thr)}', FRED, ly, threshold=thr, firstWeek=win[0][0], lastWeek=win[-1][0], runStart=weekly[i0][0], runWeeks=i1 - i0 + 1, asOf=last_week)
    claim('cut1_last_2026', win[-1][0], dtxt(win[-1][0]), f'last week with MORTGAGE30US <= {pct(thr)} (a cut of at least 1.00 point from r_old {pct(r_old)}): {pct(win[-1][1])}; '
          f'next week {dtxt(weekly[i1 + 1][0])} {pct(weekly[i1 + 1][1])}', FRED, ly, date=win[-1][0], parent='weeks_below_r_old_minus_1', asOf=last_week)
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

    # script (C5): the final narration story/script-v3.2.md, converted by preprod/script_from_v32.py into out/script-draft.json
    # (and out/script.json with the sentence times of the final video). Earlier: story/script.md v2 via preprod/script_from_story.py.
    dp = os.path.join(HERE, 'out', 'script-draft.json')
    lines = [r for r in json.load(open(dp))['sentences'] if r.get('claims')] if os.path.exists(dp) else []
    unknown = sorted({c for l in lines for c in l['claims'] if c not in C})
    assert not unknown, f'the script uses claim IDs not in claims.json: {unknown}'
    for l in lines:
        for cid in l['claims']:
            if l['kind'] == 'line':
                C[cid]['spoken'].append({'sentence': l['id'], 'scene': l['scene']})
            if l['scene'] not in C[cid]['shownIn']:
                C[cid]['shownIn'].append(l['scene'])
    # on screen: every claim the render page draws through CL(id), per scene (animatic/check-report.json claimsUsed, written by
    # animatic/src/check.py from the render logs; re-run build.py after the final render's check.py)
    cr = os.path.join(HERE, 'animatic', 'check-report.json')
    screen = json.load(open(cr)) if os.path.exists(cr) else {}
    bad = sorted({c for v in screen.values() for c in v.get('claimsUsed', []) if c not in C})
    assert not bad, f'the page draws claim IDs not in claims.json: {bad}'
    for sc in sorted(screen):
        for cid in screen[sc].get('claimsUsed', []):
            if sc not in C[cid]['shownIn']:
                C[cid]['shownIn'].append(sc)
    for c in C.values():
        c['shownIn'].sort()
    # callbacks: a number that comes back in a later scene, and what it means there (script v3.2, scenes S01-S20)
    MEAN = {'cost_median': {'S07': 'the bill from the letter, now explained: the real 2025 median', 'S09': 'the bar the monthly savings must reach',
                            'S14': 'Nora\'s bill beside Walt\'s, almost as big', 'S18': 'back to the letter: the same bill behind all three lines',
                            'S19': 'the middle of the wide range of real 2025 bills'},
            'cut_today': {'S08': 'her cut falls short of the one-point line', 'S11': 'her real cut beside a quarter point',
                          'S13': 'her real offer clears the half-point line'},
            'cut36_median': {'S16': 'Nora\'s half point beside the cut Walt needs', 'S17': 'Nora\'s half point beside Anjali\'s third',
                             'S18': 'Nora\'s line on the three-mark ruler'},
            'sav_median': {'S09': 'the same monthly saving, now stacked month by month', 'S15': 'Nora\'s saving beside Walt\'s much smaller one'},
            'be_simple_median': {'S09': 'division stops at month 24', 'S10': 'the month where the balance gap is measured'},
            'be_bal_median': {'S10': 'counting what she owes moves break-even from 24 to 30'},
            'hold36': {'S12': 'a full point is well inside three years', 'S13': 'the three-year line decides her answer',
                       'S18': 'the answer is stated for a three-year payback'},
            'k35': {'S10': 'the payments already made are what the fresh 30-year clock starts over'},
            's10': {'S08': 'the first quick answer', 'S12': 'the one-point line tested on Nora', 'S16': 'Walt needs more than the one-point line',
                    'S18': 'the one-point line fits none of the three'},
            'y3': {'S16': 'Walt sells after three years', 'S17': 'Anjali at three years', 'S20': 'one of the two horizons'},
            'y7': {'S20': 'the second horizon'},
            'r_old': {'S04': 'her rate, said again with her loan'},
            'loan_median': {'S18': 'Nora\'s loan size on the ruler'}, 'loan_small': {'S18': 'Walt\'s loan size on the ruler'},
            'loan_large': {'S18': 'Anjali\'s loan size on the ruler'},
            'cut36_small': {'S18': 'Walt\'s line on the ruler'}, 'cut36_large_words': {'S18': 'Anjali\'s line on the ruler'},
            'r_today': {'S06': 'the offer\'s rate = the national average of the date anchor'}, 'anchor_date': {'S06': 'date of the rate used'}}
    for cid, m in MEAN.items():
        C[cid]['callbacks'] = [{'scene': s, 'meaning': v} for s, v in m.items() if s in C[cid]['shownIn']]
        assert len(C[cid]['callbacks']) == len(m), (cid, [s for s in m if s not in C[cid]['shownIn']])
    words = [len(re.findall(r"[\w$%.,'-]+", l['text'])) for l in lines]
    seen = set()
    for l in lines:
        seen |= set(l['claims'])
    report = {'scriptSource': 'story/script-v3.2.md via out/script-draft.json (preprod/script_from_v32.py)', 'rowsWithClaims': len(lines), 'claims': len(C), 'claimsUsed': len(seen),
              'unusedClaims': [c for c in C if c not in seen]}
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    json.dump({'claims': list(C.values())}, open(os.path.join(HERE, 'out', 'claims.json'), 'w'), indent=1)
    write_window_section(C)
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


WINDOW_VI = {  # Vietnamese meaning column of numbers.md section H (the values, dates and sources come from the claims)
    'low2026': 'Lãi tuần thấp nhất năm 2026 (tới ngày mốc)',
    'low2026_date': 'Tuần của mức thấp nhất 2026',
    'low2026_since': 'Đáy 2026 thấp nhất kể từ tuần này (lần gần nhất trước đó lãi ≤ mức đáy); cũng là lần đầu dưới 6% kể từ tuần này. "Lowest since September 2022" và "lowest in more than three years" đều đúng',
    'jan2026': 'Lãi tuần kết thúc 15/1/2026: lúc đó thấp nhất kể từ tuần 15/9/2022. **Không phải** đáy 2026 (đáy là `low2026`). Không có tuần PMMS nào ghi ngày 12/1/2026',
    'jan2026_since': 'Mức 6.06% tuần 15/1/2026 thấp nhất kể từ tuần này',
    'cut_low2026': 'Chênh giữa lãi cũ của nhân vật (`r_old`) và đáy 2026, điểm %',
    'k_low2026': 'Số kỳ trả đã qua nếu vay lại ở tháng đáy 2026 (10/2023 → 2/2026, cùng quy ước với `k35`)',
    'sav_low2026_median': 'Nhân vật median vay lại ở tuần đáy 2026: tiết kiệm mỗi tháng',
    'be_simple_low2026_median': 'Như trên: hoà vốn cách chia đơn giản (tháng)',
    'be_bal_low2026_median': 'Như trên: hoà vốn tính cả dư nợ (tháng)',
    'first7_since': 'Ngày mốc là lần đầu lãi ≥ 7.00% kể từ tuần này (cùng tuần với `today_since`, nhưng ngưỡng 7.00% thay vì 7.03%)',
    'rise_since_low2026': 'Lãi ngày mốc cao hơn đáy 2026 bao nhiêu điểm',
    'weeks_rise_since_low2026': 'Số tuần từ đáy 2026 tới ngày mốc',
    'weeks_below_r_old_minus_1': 'Số tuần năm 2026 lãi thấp hơn `r_old` ít nhất 1 điểm (≤ 6.62%): "cửa sổ" mở bao lâu trong năm; chuỗi liền bắt đầu từ tuần 14/8/2025',
    'cut1_last_2026': 'Tuần cuối cùng của cửa sổ đó (sau tuần này lãi luôn > 6.62%)',
}
BEGIN, END = '<!-- build.py: section H BEGIN (generated, do not edit) -->', '<!-- build.py: section H END -->'


def write_window_section(C):
    """Writes numbers.md section H (the 2026 refinance window) from the claims, between the BEGIN/END markers."""
    p = os.path.join(HERE, 'numbers.md')
    text = open(p).read()
    rows = ['### H. Cửa sổ tái cấp vốn 2026: từng mở, đang khép (sinh bởi `build.py`)', '',
            'Tuần = tuần PMMS kết thúc thứ Năm. Test tính lại độc lập từ CSV: `model/test_refi.py::test_window2026_recomputed_from_csv`.', '',
            '| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |', '|---|---|---|---|---|---|---|']
    for cid, vi in WINDOW_VI.items():
        c = C[cid]
        yr = c.get('date') or c.get('dataYear') or c.get('dataYears')
        yr = f"{yr}; as of {c['asOf']}" if c.get('asOf') else yr
        src = f"{c['source']['id']} ({c['source']['url']})" if c.get('source') else '—'
        nom = 'danh nghĩa (USD năm dữ liệu)' if c.get('basis') == 'nominal' else 'n/a'
        rows.append(f"| `{cid}` | {c['display']} | {vi} | {src} | {yr} | {'ILLUSTRATIVE' if c['illustrative'] else ''} | {nom} |")
    block = BEGIN + '\n' + '\n'.join(rows) + '\n' + END
    if BEGIN in text:
        text = text[:text.index(BEGIN)] + block + text[text.index(END) + len(END):]
    else:
        anchor = '\n## 5. '
        text = text.replace(anchor, '\n' + block + '\n' + anchor, 1)
    open(p, 'w').write(text)


if __name__ == '__main__':
    main()

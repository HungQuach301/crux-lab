"""Episode 1 pre-production build: model -> claims -> script (numbers filled from claims only).

    python3 episodes/ep001/build.py            # writes out/model.json, out/claims.json, out/script-draft.json, script/script.md

Every number in the narration comes from a claim computed here from the committed data (FRED MORTGAGE30US weekly,
HMDA aggregates in data/normalized/hmda_refi_costs.csv). Scenario variables (holding period) are ILLUSTRATIVE.
Also checks, before any voice is recorded (DX-S7): new numbers per scene <= 2, mean <= 1 new number per 8 s
(estimated at 155 wpm), sentence-length CV >= 0.35.
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
DEF = {'id': 'series-definition', 'url': 'https://fred.stlouisfed.org/series/MORTGAGE30US'}
WPM = 155.0


def usd(v):
    return '${:,.0f}'.format(v)


def pct(v, d=2):
    return f'{v:.{d}f}%'


def main():
    weekly = refi.load_weekly()
    monthly = refi.monthly_means(weekly)
    hm = list(csv.DictReader(open(os.path.join(HERE, 'data', 'normalized', 'hmda_refi_costs.csv'))))
    H = lambda y, p, b, k: float(next(r for r in hm if r['year'] == str(y) and r['purpose'].startswith(p) and r['loanSize'] == b)[k])
    years = sorted({int(r['year']) for r in hm})
    Y = max(years)
    P31 = 'refinance (31)'

    peak = max(weekly, key=lambda x: x[1]); low = min(weekly, key=lambda x: x[1])
    r_old = dict(monthly)['2023-10']
    loan = H(Y, P31, 'all sizes', 'loan_p50_usd')
    cost = H(Y, P31, 'all sizes', 'cost_p50_usd')
    cases = {s: refi.refi(loan, r_old, 360, r_old - s, cost) for s in (0.25, 0.5, 1.0, 2.0)}
    bands = {'small': ('under $150k', 150_000), 'big': ('$750k and over', 750_000)}
    sp36 = {'mid': refi.spread_for_break_even(loan, r_old, cost, 36)}
    for k, (b, _) in bands.items():
        sp36[k] = refi.spread_for_break_even(H(Y, P31, b, 'loan_p50_usd'), r_old, H(Y, P31, b, 'cost_p50_usd'), 36)
    shares = {y: H(y, P31, 'all sizes', 'cost_p50_pct') for y in years}
    fixed = statistics.median(shares.values())
    hist = refi.history(monthly, lambda y: (shares[y], False) if y in shares else (fixed, True), spreads=(0.5, 1.0, 2.0))
    one = [(e, next(c for c in e['cases'] if c['spread'] == 1.0)) for e in hist]
    one = [(e, c) for e, c in one if c['reached']]
    bes = [c['breakEvenMonths'] for _, c in one]
    further = [(e, c) for e, c in one if c['beforeBreakEvenAnotherDrop']]
    # example: the most recent episode where a further full point came before break-even
    ex_e, ex_c = further[-1] if further else one[-1]
    mi = lambda m: [x[0] for x in monthly].index(m)
    ex_gap = mi(ex_c['beforeBreakEvenAnotherDrop']) - mi(ex_c['refiMonth']) if ex_c['beforeBreakEvenAnotherDrop'] else None
    month_name = lambda m: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][int(m[5:]) - 1] + ' ' + m[:4]

    C = {}

    def claim(cid, value, display, formula, source, year=None, **kw):
        C[cid] = {'claimId': cid, 'value': value, 'display': display, 'formula': formula, 'source': source,
                  **({'dataYear': year} if isinstance(year, int) else {'dataYears': year} if year else {}),
                  'historical': bool(source) and kw.pop('historical', True), 'illustrative': kw.pop('illustrative', False),
                  **({'basis': 'nominal'} if display.startswith('$') else {}), 'callbacks': [], 'shownIn': [], 'spoken': [], **kw}

    last_y = int(weekly[-1][0][:4])
    claim('term30', 30, '30', 'loan term of the series and of the HMDA filter (30-year fixed; loan_term = 360 months)', DEF, last_y, historical=False)
    claim('y1971', 1971, '1971', 'first observation of MORTGAGE30US (week of 1971-04-02)', FRED, 1971)
    claim('y1981', int(peak[0][:4]), peak[0][:4], f'year of the weekly maximum ({peak[0]})', FRED, int(peak[0][:4]))
    claim('peak', peak[1], pct(peak[1]), f'max of MORTGAGE30US weekly, 1971-{last_y} (week of {peak[0]})', FRED, int(peak[0][:4]))
    claim('y2021', int(low[0][:4]), low[0][:4], f'year of the weekly minimum ({low[0]})', FRED, int(low[0][:4]))
    claim('low', low[1], pct(low[1]), f'min of MORTGAGE30US weekly, 1971-{last_y} (week of {low[0]})', FRED, int(low[0][:4]))
    claim('y2025', Y, str(Y), 'latest HMDA data year used', HMDA, Y)
    claim('y2018', min(years), str(min(years)), 'first HMDA year with total_loan_costs', HMDA, min(years))
    claim('y2017', 2017, '2017', 'first year of the Optimal Blue 30-year conforming index (OBMMIC30YF, from 2017-01-03)', OB, 2017)
    claim('n31', int(H(Y, P31, 'all sizes', 'n')), '{:,}'.format(int(H(Y, P31, 'all sizes', 'n'))),
          f'count of HMDA {Y} originated refinances (loan_purpose 31), first lien, loan_term 360, total_loan_costs > 0', HMDA, Y)
    claim('cost_med', cost, usd(cost), f'median total_loan_costs, HMDA {Y}, loan_purpose 31, first lien, 360 months', HMDA, Y, core=True, decisive=True)
    claim('cost_p25', H(Y, P31, 'all sizes', 'cost_p25_usd'), usd(H(Y, P31, 'all sizes', 'cost_p25_usd')), '25th percentile, same population', HMDA, Y)
    claim('cost_p75', H(Y, P31, 'all sizes', 'cost_p75_usd'), usd(H(Y, P31, 'all sizes', 'cost_p75_usd')), '75th percentile, same population', HMDA, Y)
    claim('band150', 150000, '$150,000', 'loan-size band edge chosen for the analysis (not a data value)', None, None, illustrative=False, role='axis', historical=False)
    C['band150'].pop('basis', None); C['band150']['basis'] = 'nominal'; C['band150']['formula'] += '; analysis parameter'
    claim('band750', 750000, '$750,000', 'loan-size band edge chosen for the analysis (not a data value)', None, None, role='axis', historical=False)
    for k, (b, _) in bands.items():
        v = H(Y, P31, b, 'cost_p50_pct')
        claim('share_' + k, v, pct(v, 1), f'median of total_loan_costs / loan_amount, HMDA {Y}, loan_purpose 31, loans {b}', HMDA, Y)
    claim('loan_med', loan, usd(loan), f'median loan_amount, HMDA {Y}, loan_purpose 31 (public data bins amounts to $10,000 midpoints)', HMDA, Y)
    claim('r_old', r_old, pct(r_old), 'monthly mean of MORTGAGE30US, October 2023 (peak month of the latest drop episode)', FRED, 2023)
    claim('oct2023', 2023, 'October 2023', 'month of the monthly peak that starts the latest drop episode', FRED, 2023)
    claim('hold36', 36, '36', 'holding-period target of the scenario (3 years): an assumption, not data', None, None, illustrative=True, historical=False)
    for s, key in ((0.25, '025'), (0.5, '05'), (1.0, '10'), (2.0, '20')):
        claim('s' + key, s, f'{s:g}', 'rate cut in percentage points (analysis grid)', None, None, historical=False)
        C['s' + key]['formula'] += '; scenario grid value'
        c = cases[s]
        claim('sav' + key, c['monthlySavings'], usd(c['monthlySavings']), f"payment({usd(loan)}, {r_old:.2f}%, 360) - payment({usd(loan)}, {r_old - s:.2f}%, 360)", FRED, [2023, Y], model='refi.refi')
        claim('be' + key, c['breakEvenMonths'], str(c['breakEvenMonths']), f"ceil(cost_med / sav{key}) = ceil({cost:.2f} / {c['monthlySavings']:.2f})", HMDA, [2023, Y], model='refi.break_even_months',
              **({'core': True} if key == '10' else {}))
    for k in ('mid', 'small', 'big'):
        claim('sp36_' + k, round(sp36[k], 2), f'{sp36[k]:.2f}'.rstrip('0'), f'smallest rate cut with break-even <= 36 months (bisection), loan and cost medians of {"all sizes" if k == "mid" else bands[k][0]}, HMDA {Y}, old rate {r_old:.2f}%', HMDA, [2023, Y],
              model='refi.spread_for_break_even', illustrative=False, **({'decisive': True, 'core': True} if k == 'mid' else {}))
    claim('n_eps', len(hist), str(len(hist)), 'drop episodes: zig-zag swings of the monthly mean rate of >= 1.00 point, 1971-' + str(last_y), FRED, [1971, last_y], model='refi.drop_episodes')
    claim('beh_min', min(bes), str(min(bes)), 'min break-even months over the episodes, refinance at a 1-point cut, $300,000 loan (ILLUSTRATIVE size; months do not depend on it)', FRED, [1971, last_y], model='refi.history')
    claim('beh_max', max(bes), str(max(bes)), 'max of the same', FRED, [1971, last_y], model='refi.history')
    claim('n_further', len(further), str(len(further)), 'episodes where the rate fell another full point before the 1-point refinance broke even', FRED, [1971, last_y], model='refi.history')
    claim('n_nofurther', len(one) - len(further), str(len(one) - len(further)), 'the other episodes that reached a 1-point cut', FRED, [1971, last_y], model='refi.history')
    claim('ex_peak', int(ex_e['peak'][:4]), month_name(ex_e['peak']), 'peak month of the example episode', FRED, int(ex_e['peak'][:4]))
    claim('ex_refi', int(ex_c['refiMonth'][:4]), month_name(ex_c['refiMonth']), 'refinance month of the example (first month 1 point under the peak)', FRED, int(ex_c['refiMonth'][:4]))
    claim('ex_be', ex_c['breakEvenMonths'], str(ex_c['breakEvenMonths']), 'break-even months of the example', FRED, int(ex_c['refiMonth'][:4]), model='refi.history',
          illustrative=bool(ex_c['costIllustrative']))
    claim('ex_gap', ex_gap, str(ex_gap), 'months from the refinance to the first month another full point lower', FRED, int(ex_c['refiMonth'][:4]), model='refi.history')
    # extra claims for the expanded script
    claim('cost_med_co', H(Y, 'cash-out', 'all sizes', 'cost_p50_usd'), usd(H(Y, 'cash-out', 'all sizes', 'cost_p50_usd')), f'median total_loan_costs, HMDA {Y}, loan_purpose 32 (cash-out), first lien, 360 months', HMDA, Y)
    y21 = 2021 if 2021 in years else Y
    claim('n31_2021', int(H(y21, P31, 'all sizes', 'n')), '{:,}'.format(int(H(y21, P31, 'all sizes', 'n'))), f'count of HMDA {y21} loan_purpose 31, first lien, 360 months, total_loan_costs > 0', HMDA, y21)
    claim('cost_med_2021', H(y21, P31, 'all sizes', 'cost_p50_usd'), usd(H(y21, P31, 'all sizes', 'cost_p50_usd')), f'median total_loan_costs, HMDA {y21}, loan_purpose 31', HMDA, y21)
    for h_, key in ((60, 'hold60'), (84, 'hold84')):
        claim(key, h_, str(h_), f'holding-period target of the scenario ({h_ // 12} years): an assumption, not data', None, None, illustrative=True, historical=False)
        v = refi.spread_for_break_even(loan, r_old, cost, h_)
        claim(f'sp{h_}_mid', round(v, 2), f'{v:.2f}'.rstrip('0'), f'smallest rate cut with break-even <= {h_} months, median loan and cost, HMDA {Y}, old rate {r_old:.2f}%', HMDA, [2023, Y], model='refi.spread_for_break_even')
    epi = lambda pfx: next((e, next(c for c in e['cases'] if c['spread'] == 1.0)) for e in hist if e['peak'].startswith(pfx))
    claim('y1980s', 1980, '1980s', 'decade of the three largest drop episodes (1980-04, 1981-10, 1984-07 peaks)', FRED, [1980, 1987])
    e81, c81 = epi('1981')
    claim('m81', c81['monthsOnOldLoan'], str(c81['monthsOnOldLoan']), 'months from the 1981-10 monthly peak to the first month 1 point lower', FRED, 1981, model='refi.history')
    claim('be81', c81['breakEvenMonths'], str(c81['breakEvenMonths']), 'break-even months of that refinance (closing-cost share fixed, pre-HMDA)', FRED, 1981, model='refi.history', illustrative=True)
    claim('g81', mi(c81['beforeBreakEvenAnotherDrop']) - mi(c81['refiMonth']), str(mi(c81['beforeBreakEvenAnotherDrop']) - mi(c81['refiMonth'])), 'months from that refinance to the first month another full point lower', FRED, 1982, model='refi.history')
    e87, c87 = epi('1987')
    claim('y1987', 1987, '1987', 'peak month of the episode: ' + e87['peak'], FRED, 1987)
    d87 = mi(e87['trough']) - mi(e87['peak'])
    claim('d87', d87, str(d87), f"months from the monthly peak {e87['peak']} to the trough {e87['trough']}", FRED, [1987, 1988], model='refi.drop_episodes')
    e06, c06 = epi('2006')
    claim('y2006', 2006, '2006', 'peak month of the episode: ' + e06['peak'], FRED, 2006)
    claim('r06', int(c06['refiMonth'][:4]), month_name(c06['refiMonth']), 'refinance month (first month 1 point under the peak)', FRED, int(c06['refiMonth'][:4]))
    e23, c23 = epi('2023')
    claim('r23', int(c23['refiMonth'][:4]), month_name(c23['refiMonth']), 'refinance month (first month 1 point under the 2023-10 peak)', FRED, int(c23['refiMonth'][:4]))
    claim('be23', c23['breakEvenMonths'], str(c23['breakEvenMonths']), f"break-even months, HMDA {c23['refiMonth'][:4]} median cost share", HMDA, int(c23['refiMonth'][:4]), model='refi.history',
          illustrative=bool(c23['costIllustrative']))
    for c_ in C.values():
        if c_['source'] is None:
            c_['illustrative'] = c_['illustrative'] or c_.get('role') != 'axis' and not c_['claimId'].startswith('s')

    # script
    lines, act = [], None
    for raw in open(os.path.join(HERE, 'script', 'script.tpl.md')):
        raw = raw.rstrip('\n')
        if act is None and not raw.startswith('@act'):
            continue
        if raw.startswith('@act'):
            act = raw.split()[1]
            continue
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
    # callbacks: every re-appearance of a core claim after the first, with the meaning it carries there
    MEAN = {'cost_med': {'a2-loan': 'the bill that the monthly savings must repay', 'a3-median': 'a median: half of borrowers paid more'},
            'be10': {'a2-thumb': 'where the one-point rule of thumb comes from', 'a3-answer': 'part of the answer to the open question'},
            'sp36_mid': {'a3-answer': 'the answer to the open question of the cold open'}}
    for cid, m in MEAN.items():
        C[cid]['callbacks'] = [{'scene': s, 'meaning': v} for s, v in m.items() if s in C[cid]['shownIn']]

    # pre-voice checks
    words = [len(re.findall(r"[\w$%.,'-]+", l['text'])) for l in lines]
    est = sum(words) / WPM * 60
    seen, per_scene = set(), {}
    for l in lines:
        new = [c for c in l['claims'] if c not in seen and C[c].get('role') != 'axis']
        seen |= set(l['claims'])
        per_scene[l['scene']] = new
    over = {s: n for s, n in per_scene.items() if len(n) > 2}
    cv = statistics.pstdev(words) / statistics.mean(words)
    report = {'sentences': len(lines), 'words': sum(words), 'estSpeechSeconds': round(est, 1), 'newNumbers': len(seen - {c for c in C if C[c].get('role') == 'axis'}),
              'scenesOver2New': over, 'sentenceLengthCV': round(cv, 3), 'claims': len(C), 'unusedClaims': [c for c in C if not C[c]['spoken']]}
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    json.dump({'claims': list(C.values())}, open(os.path.join(HERE, 'out', 'claims.json'), 'w'), indent=1)
    json.dump({'loan': loan, 'cost': cost, 'oldRate': r_old, 'cases': cases, 'sp36': sp36, 'costSharesByYear': shares, 'fixedSharePre2018': fixed,
               'history': hist}, open(os.path.join(HERE, 'out', 'model.json'), 'w'), indent=1)
    json.dump({'sentences': lines, 'check': report}, open(os.path.join(HERE, 'out', 'script-draft.json'), 'w'), indent=1)
    with open(os.path.join(HERE, 'script', 'script.md'), 'w') as f:
        f.write('# Episode 1 — script (generated from script.tpl.md and out/claims.json; do not edit)\n\n')
        a = None
        for l in lines:
            if l['act'] != a:
                a = l['act']; f.write(f'\n## {a}\n\n')
            f.write(f"- `{l['scene']}` {l['text']}\n")
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()

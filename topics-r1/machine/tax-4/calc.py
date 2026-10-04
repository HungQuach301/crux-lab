"""tax-4: a single hourly worker paid the typical production/nonsupervisory wage (rounded to whole dollars) can add
8 hours a week for 50 weeks either as overtime at time-and-a-half or at a second W-2 job paying the same hourly
amount. Federal income tax (2026 single brackets, standard deduction, overtime-premium deduction) plus employee
payroll tax on each path; break-even side-job rate. Reads data/ only; prints one JSON object {id: value}.

`python3 calc.py --statement N` (N = 1-based index into statements.json, or `all`) recomputes from data/ the
numbers used in statement N, renders each with the rounding the sentence uses, checks that the rendered text appears
in the sentence as written, that the sentence still appears verbatim in its source file, that no digit in the
sentence is left without a quantity (orphan), and that the statement's named claims hold; prints True or False.
Default mode (no arguments) is unchanged."""
import csv, json, os, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# 2026 rules (single filer), quoted in sources.json provisions
STD = 16100
BRACKETS = [(0, 0.10), (12400, 0.12), (50400, 0.22), (105700, 0.24), (201775, 0.32), (256225, 0.35), (640600, 0.37)]
OT_CAP = 12500           # overtime-premium deduction cap (single)
OT_PHASE_START = 150000  # MAGI where the cap starts to phase down (not reached here)
FICA = 0.062 + 0.0145    # employee social security + medicare (wage base not reached)

HOURS_YEAR = 2080        # 40 h x 52 weeks
EXTRA_H = 8 * 50         # 8 extra hours a week, 50 weeks

rows = [r for r in list(csv.reader(open(os.path.join(D, 'AHETPI.csv'))))[1:] if len(r) > 1 and r[1] not in ('', '.')]
ahe_date, ahe = rows[-1][0], float(rows[-1][1])
W = float(round(ahe))    # regular hourly rate used for the viewer


def income_tax(taxable):
    t = 0.0
    for i, (lo, r) in enumerate(BRACKETS):
        hi = BRACKETS[i + 1][0] if i + 1 < len(BRACKETS) else float('inf')
        if taxable > lo:
            t += (min(taxable, hi) - lo) * r
    return t


base = W * HOURS_YEAR
tax_base = income_tax(max(0.0, base - STD))


def extra_net(extra_pay, ot_premium):
    agi = base + extra_pay
    ded = min(ot_premium, OT_CAP)  # MAGI below phase-down start in all cases here
    assert agi <= OT_PHASE_START
    tax = income_tax(max(0.0, agi - STD - ded))
    return extra_pay - FICA * extra_pay - (tax - tax_base), tax - tax_base


ot_rate = 1.5 * W
ot_pay = ot_rate * EXTRA_H
premium = 0.5 * W * EXTRA_H
ot_net, ot_itax = extra_net(ot_pay, premium)
side_net, side_itax = extra_net(ot_pay, 0.0)

lo, hi = ot_rate, 3 * ot_rate  # side-job hourly rate giving the same extra take-home as overtime
for _ in range(200):
    mid = (lo + hi) / 2
    if extra_net(mid * EXTRA_H, 0.0)[0] < ot_net:
        lo = mid
    else:
        hi = mid

# ---------------------------------------------------------------------------------------------------------------
# --statement mode (topic-dossier standard, playbook/topic-dossier.md section 3). Not used by the default output.
# ---------------------------------------------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
EXTRA_H_WEEK, EXTRA_WEEKS = 8, 50       # viewer scenario: 8 extra hours a week for 50 weeks (= EXTRA_H)
REG_H_WEEK, REG_WEEKS = 40, 52          # regular job (= HOURS_YEAR); 40 = FLSA overtime threshold
OT_MULT, PREMIUM_MULT = 1.5, 0.5        # 29 U.S.C. 207(a)(1); 26 U.S.C. 225(c)(1) (excess over the regular rate)
TAX_YEAR, OT_FIRST_YEAR, OT_LAST_YEAR = 2026, 2025, 2028
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def scenario(w):
    """Whole model for a regular hourly rate w (same rules as the default computation above)."""
    b = w * HOURS_YEAR
    tb = income_tax(max(0.0, b - STD))
    otr = OT_MULT * w
    pay = otr * EXTRA_H
    prem = PREMIUM_MULT * w * EXTRA_H

    def net(extra_pay, otp):
        agi = b + extra_pay
        tax = income_tax(max(0.0, agi - STD - min(otp, OT_CAP)))
        return extra_pay - FICA * extra_pay - (tax - tb), tax - tb, agi

    o_net, o_tax, _ = net(pay, prem)
    s_net, s_tax, s_agi = net(pay, 0.0)
    a, z = otr, 3 * otr
    for _ in range(200):
        m = (a + z) / 2
        if net(m * EXTRA_H, 0.0)[0] < o_net:
            a = m
        else:
            z = m

    def rate_at(taxable):  # marginal bracket rate at a taxable income
        return [r for lo_, r in BRACKETS if taxable > lo_][-1]
    lo_t, hi_ot, hi_side = b - STD, b + pay - STD - min(prem, OT_CAP), b + pay - STD
    rates = {rate_at(lo_t + 0.01), rate_at(hi_ot), rate_at(hi_side)}
    return dict(w=w, base=b, ot_rate=otr, pay=pay, prem=prem, o_net=o_net, s_net=s_net, o_tax=o_tax, s_tax=s_tax,
                adv=o_net - s_net, breakeven=z, markup=z - otr, payroll=FICA * pay, max_agi=s_agi,
                marg=rates.pop() if len(rates) == 1 else None, net=net)


def quantities():
    """Every quantity a dossier sentence may use: name -> value (recomputed from data/ and the rule constants)."""
    sc = scenario(W)
    q = dict(out)
    q.update({
        'premium_per_hour_usd': PREMIUM_MULT * W,
        'marginal_bracket_pct': None if sc['marg'] is None else 100 * sc['marg'],
        'breakeven_markup_usd': round(hi, 2) - ot_rate,
        'ot_advantage_per_hour_usd': (ot_net - side_net) / EXTRA_H,
        'EXTRA_HOURS_PER_WEEK': EXTRA_H_WEEK, 'EXTRA_WEEKS': EXTRA_WEEKS, 'EXTRA_HOURS_YEAR': EXTRA_H,
        'REGULAR_HOURS_PER_WEEK': REG_H_WEEK, 'REGULAR_WEEKS': REG_WEEKS,
        'OT_MULTIPLIER': OT_MULT, 'PREMIUM_MULTIPLIER': PREMIUM_MULT, 'OT_CAP_SINGLE_USD': OT_CAP,
        'OT_PHASE_START_MAGI_USD': OT_PHASE_START, 'STD_DEDUCTION_SINGLE_USD': STD,
        'BRACKET_RATE_12_PCT': 100 * BRACKETS[1][1], 'BRACKET_RATE_22_PCT': 100 * BRACKETS[2][1],
        'TAX_YEAR': TAX_YEAR, 'OT_DEDUCTION_FIRST_YEAR': OT_FIRST_YEAR, 'OT_DEDUCTION_LAST_YEAR': OT_LAST_YEAR,
    })
    return q, sc


def render(v, fmt):
    if fmt == 'usd0':
        return '$' + format(v, ',.0f')
    if fmt == 'usd2':
        return '$' + format(v, ',.2f')
    if fmt == 'pct0':
        return format(v, '.0f') + '%'
    if fmt == 'pct2':
        return format(v, '.2f') + '%'
    if fmt == 'num0':
        return format(v, ',.0f')
    if fmt == 'year':
        return '%d' % v
    if fmt == 'mult':
        return format(v, 'g') + 'x'
    if fmt == 'num':
        return format(v, 'g')
    if fmt == 'month':
        y, m = str(v)[:7].split('-')
        return '%s %s' % (MONTHS[int(m) - 1], y)
    raise ValueError(fmt)


def provisions_text():
    src = json.load(open(os.path.join(HERE, 'sources.json')))
    return {p['cite']: p['cite'] + ' ' + p['quote'] for p in src['provisions']}


def claim_checks(q, sc):
    """Named non-numeric claims a sentence makes about the result (True = the claim holds in the model)."""
    prov = provisions_text()
    mfj = [t for c, t in prov.items() if c == 'IRS IR-2025-103 (2026 single brackets)'][0]
    s12, s40 = scenario(16.0), scenario(40.0)   # a 12%-bracket worker; a second 22%-bracket worker
    checks = {
        'same_gross_both_paths': lambda: sc['pay'] == q['extra_pay_usd'] == q['ot_rate_usd'] * EXTRA_H,
        'deduction_only_income_tax': lambda: q['payroll_tax_on_extra_usd'] == round(FICA * ot_pay, 2)
            and q['ot_income_tax_on_extra_usd'] < q['side_income_tax_on_extra_usd'],
        'payroll_full_both_paths': lambda: abs(sc['payroll'] - FICA * sc['pay']) < 1e-9
            and abs((sc['pay'] - sc['o_net'] - sc['o_tax']) - (sc['pay'] - sc['s_net'] - sc['s_tax'])) < 1e-6,
        'overtime_not_tax_free': lambda: sc['o_tax'] > 0 and sc['payroll'] > 0,
        'guess_contradicted': lambda: sc['o_tax'] > 0 and sc['adv'] > 0 and sc['markup'] < 0.25 * sc['ot_rate'],
        'gap_is_premium_times_bracket': lambda: sc['marg'] is not None
            and abs(sc['adv'] - min(sc['prem'], OT_CAP) * sc['marg']) < 0.005,
        'markup_few_dollars': lambda: 1 <= sc['markup'] < 10,
        'breakeven_exists': lambda: abs(sc['net'](sc['breakeven'] * EXTRA_H, 0.0)[0] - sc['o_net']) < 0.01,
        'twelve_pct_bracket_gains_less': lambda: s12['marg'] == BRACKETS[1][1] and s12['adv'] < sc['adv']
            and abs(s12['adv'] - s12['prem'] * BRACKETS[1][1]) < 0.005,
        'married_bracket_differs': lambda: '$100,800 for married couples filing jointly' in mfj
            and '22% for incomes over $50,400' in mfj and BRACKETS[2][0] == 50400,
        'breakeven_depends_on_example': lambda: round(s40['breakeven'], 2) != round(sc['breakeven'], 2),
        'markup_is_general_at_22pct': lambda: s40['marg'] == sc['marg']
            and render(s40['markup'], 'num0') == render(sc['markup'], 'num0'),
        'wage_rounded_to_dollar': lambda: W == round(ahe) and abs(W - ahe) <= 0.5,
        'magi_below_phase_down': lambda: sc['max_agi'] < OT_PHASE_START and sc['prem'] <= OT_CAP,
    }
    return checks


# constant -> provision cite (sources.json) whose cite or quote must contain the constant as rendered
CONST_CITES = {
    'OT_CAP_SINGLE_USD': ('26 U.S.C. 225(b)(1) (cap $12,500 single)', '$12,500'),
    'OT_PHASE_START_MAGI_USD': ('26 U.S.C. 225(b)(2)(A) (phase-down above $150,000 MAGI)', '$150,000'),
    'OT_DEDUCTION_LAST_YEAR': ('26 U.S.C. 225(g) (termination after 2028)', '2028'),
    'STD_DEDUCTION_SINGLE_USD': ('IRS IR-2025-103 (2026 standard deduction, single)', '$16,100'),
    'TAX_YEAR': ('IRS IR-2025-103 (2026 standard deduction, single)', 'tax year 2026'),
    'BRACKET_RATE_12_PCT': ('IRS IR-2025-103 (2026 single brackets)', '12% for incomes over $12,400'),
    'BRACKET_RATE_22_PCT': ('IRS IR-2025-103 (2026 single brackets)', '22% for incomes over $50,400'),
    'REGULAR_HOURS_PER_WEEK': ('29 U.S.C. 207(a)(1) (time-and-a-half over 40 hours)', 'over 40 hours'),
    'OT_MULTIPLIER': ('29 U.S.C. 207(a)(1) (time-and-a-half over 40 hours)', 'one and one-half times'),
    'PREMIUM_MULTIPLIER': ('26 U.S.C. 225(c)(1) (only the amount in excess of the regular rate)',
                           'in excess of the regular rate'),
}


def source_text(source):
    if source == 'claim-risk.md':
        return open(os.path.join(HERE, 'claim-risk.md')).read()
    fname, field = source.split(':', 1)
    obj = json.load(open(os.path.join(HERE, fname)))
    if '[' in field:
        key, idx = field.rstrip(']').split('[')
        return obj[key][int(idx)]
    return obj[field]


def check_statement(st, q, sc, verbose=False):
    import re
    problems = []
    text = st['text']
    if text not in source_text(st['source']):
        problems.append('text not verbatim in ' + st['source'])
    prov = provisions_text()
    try:
        rnums = {n['id']: n['value'] for n in json.load(open(os.path.join(HERE, 'result.json')))['numbers']}
    except (OSError, KeyError, ValueError):
        rnums = {}
    rest = text
    tokens = []
    for name, fmt in zip(st['uses'], st['render']):
        if name not in q or q[name] is None:
            problems.append('unknown or undefined quantity ' + name)
            continue
        if name in rnums and rnums[name] != q[name]:
            problems.append('%s recomputed %r != result.json %r' % (name, q[name], rnums[name]))
        if name in CONST_CITES:
            cite, needle = CONST_CITES[name]
            if needle not in prov.get(cite, ''):
                problems.append('%s not supported by provision %s' % (name, cite))
        tokens.append((render(q[name], fmt), name))
    for tok, name in sorted(tokens, key=lambda t: -len(t[0])):
        pat = (r'(?<![\d.,])' if tok[0].isdigit() else '') + re.escape(tok) + r'(?![\d]|[.,]\d)'
        if not re.search(pat, text):
            problems.append('%s rendered as %r not found in sentence' % (name, tok))
        rest = re.sub(pat, ' ', rest)
    for lab in st.get('labels', []):
        rest = rest.replace(lab, ' ')
    orphans = re.findall(r'\d[\d,.]*', rest)
    if orphans:
        problems.append('orphan digits (no quantity): ' + ', '.join(orphans))
    checks = claim_checks(q, sc)
    for c in st.get('claims', []):
        if c not in checks:
            problems.append('unknown claim ' + c)
        elif not checks[c]():
            problems.append('claim does not hold: ' + c)
    if verbose:
        for p_ in problems:
            print('  - ' + p_, file=sys.stderr)
    return not problems


def statement_mode(argv):
    import argparse
    ap = argparse.ArgumentParser(description='Check dossier sentences against recomputed numbers.')
    ap.add_argument('--statement', required=True, help='1-based index into statements.json, or "all"')
    ap.add_argument('-v', '--verbose', action='store_true', help='list problems on stderr')
    a = ap.parse_args(argv)
    sts = json.load(open(os.path.join(HERE, 'statements.json')))
    q, sc = quantities()
    if a.statement == 'all':
        for i, st in enumerate(sts, 1):
            print(i, check_statement(st, q, sc, a.verbose), 'expected', st.get('expected', True))
        return 0
    n = int(a.statement)
    if not 1 <= n <= len(sts):
        print('False')
        return 2
    print(check_statement(sts[n - 1], q, sc, a.verbose))
    return 0

out = {
    'ahe_latest': ahe,
    'ahe_date': ahe_date,
    'regular_rate_usd': W,
    'ot_rate_usd': ot_rate,
    'extra_pay_usd': ot_pay,
    'ot_premium_deduction_usd': premium,
    'deductible_share_of_ot_pay_pct': round(100 * premium / ot_pay, 2),
    'ot_income_tax_on_extra_usd': round(ot_itax, 2),
    'side_income_tax_on_extra_usd': round(side_itax, 2),
    'payroll_tax_on_extra_usd': round(FICA * ot_pay, 2),
    'ot_extra_take_home_usd': round(ot_net, 2),
    'side_extra_take_home_usd': round(side_net, 2),
    'ot_advantage_usd': round(ot_net - side_net, 2),
    'ot_total_tax_rate_on_extra_pct': round(100 * (1 - ot_net / ot_pay), 2),
    'side_total_tax_rate_on_extra_pct': round(100 * (1 - side_net / ot_pay), 2),
    'side_breakeven_rate_usd': round(hi, 2),
}
if len(sys.argv) > 1:
    sys.exit(statement_mode(sys.argv[1:]))
print(json.dumps(out))

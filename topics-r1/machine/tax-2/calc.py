"""tax-2: for a married couple who bought in 2000, the purchase price above which a home that appreciated like its
metro's house price index has a gain larger than the fixed $500,000 joint home-sale exclusion (2026 Q2 values),
and what the 1997 limit would be in today's dollars. Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os, re, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
EXCL_JOINT = 500000   # joint-return limit (quoted in provisions)
EXCL_SINGLE = 250000  # single limit (quoted in provisions)
NOW = '2026-04-01'    # 2026 Q2, latest quarter in every file
BUY_YEAR = '2000'

METROS = {  # FHFA all-transactions index, metropolitan division / MSA code -> short name
    '31084': 'los_angeles', '41740': 'san_diego', '41884': 'san_francisco', '41940': 'san_jose',
    '42644': 'seattle', '14454': 'boston', '35614': 'new_york', '33124': 'miami',
    '19740': 'denver', '38060': 'phoenix', '19124': 'dallas', '16984': 'chicago',
}


def load(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0]] = float(row[1])
    return out


def growth(s):
    base = [v for k, v in s.items() if k.startswith(BUY_YEAR)]
    assert len(base) == 4
    return s[NOW] / (sum(base) / 4)


out = {}
thr = {}
for code, name in METROS.items():
    g = growth(load(f'ATNHPIUS{code}Q'))
    out[f'growth_{name}'] = round(g, 4)
    thr[name] = EXCL_JOINT / (g - 1)
    out[f'threshold_joint_{name}_usd'] = round(thr[name], -2)
g_us = growth(load('USSTHPI'))
out['growth_us'] = round(g_us, 4)
out['threshold_joint_us_usd'] = round(EXCL_JOINT / (g_us - 1), -2)
out['threshold_single_us_usd'] = round(EXCL_SINGLE / (g_us - 1), -2)
out['threshold_joint_min_usd'] = round(min(thr.values()), -2)
out['threshold_joint_max_usd'] = round(max(thr.values()), -2)
out['metros_threshold_under_200k'] = sum(1 for v in thr.values() if v < 200000)
out['metros_threshold_under_300k'] = sum(1 for v in thr.values() if v < 300000)
cpi = load('CPIAUCNS')
out['cpi_1997_05'] = cpi['1997-05-01']
out['cpi_2026_08'] = cpi['2026-08-01']
out['excl_joint_1997_in_2026_usd'] = round(EXCL_JOINT * cpi['2026-08-01'] / cpi['1997-05-01'], -3)
# ---------------------------------------------------------------------------------------------------------------
# --statement N (dossier standard, playbook/topic-dossier.md section 3). Not used by the default run above.
# Recomputes from data/ every number that statement N of statements.json uses, renders it with the rounding the
# sentence uses, checks the rendered text (with the words that tie it to its case: metro, period, limit) appears in
# the sentence as written, checks scope facts, and checks no digit in the sentence is left without a source
# (orphan). Prints True or False.
# ---------------------------------------------------------------------------------------------------------------
NAMES = {'los_angeles': 'Los Angeles', 'san_diego': 'San Diego', 'san_francisco': 'San Francisco',
         'san_jose': 'San Jose', 'seattle': 'Seattle', 'boston': 'Boston', 'new_york': 'New York',
         'miami': 'Miami', 'denver': 'Denver', 'phoenix': 'Phoenix', 'dallas': 'Dallas', 'chicago': 'Chicago'}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def _usd(x):
    return '${:,.0f}'.format(x)


def _month(key):  # '2026-08-01' -> 'August 2026'
    return f'{MONTHS[int(key[5:7]) - 1]} {key[:4]}'


def _quarter(key):  # '2026-04-01' -> '2026 Q2'
    return f'{key[:4]} Q{(int(key[5:7]) - 1) // 3 + 1}'


def _statement(n):
    here = os.path.dirname(os.path.abspath(__file__))
    st = json.load(open(os.path.join(here, 'statements.json')))[n - 1]
    assert st['n'] == n
    res = json.load(open(os.path.join(here, 'result.json')))
    card = json.load(open(os.path.join(here, 'card.json')))
    srcs = json.load(open(os.path.join(here, 'sources.json')))
    cr = open(os.path.join(here, 'claim-risk.md')).read()
    fname, _, field = st['source'].partition(':')
    pool = {'result.json': lambda: res[field], 'card.json': lambda: card[field], 'claim-risk.md': lambda: cr}[fname]()
    text = st['text']
    prov = {p['cite'].split(' (')[0]: p['quote'] for p in srcs['provisions']}

    # quantities recomputed from data/ (unrounded where the id is unrounded upstream)
    hpi = {name: load(f'ATNHPIUS{code}Q') for code, name in METROS.items()}
    us = load('USSTHPI')
    g = {name: growth(s) for name, s in hpi.items()}
    t = {name: EXCL_JOINT / (gg - 1) for name, gg in g.items()}
    t_us, t_single = EXCL_JOINT / (growth(us) - 1), EXCL_SINGLE / (growth(us) - 1)
    under300 = {m for m, v in t.items() if v < 300000}
    under200 = {m for m, v in t.items() if v < 200000}
    cpi_ = load('CPIAUCNS')
    cpi_last = max(cpi_)
    eff = '1997-05-01'  # month of 'sales after May 6, 1997'
    real = EXCL_JOINT * cpi_[cpi_last] / cpi_[eff]
    now_is_last = all(max(s) == NOW for s in list(hpi.values()) + [us])
    statute_joint = '"$500,000"' in prov['26 U.S.C. 121(b)(2)(A)']
    statute_single = '$250,000' in prov['26 U.S.C. 121(b)(1)']
    eff_quote = 'May 6, 1997' in prov['Pub. L. 105-34 effective date note to 26 U.S.C. 121']
    yr = BUY_YEAR
    thr_r = {m: _usd(round(v, -2)) for m, v in t.items()}

    E, A = 'expect', 'assert'
    spec = {
        1: [(E, 'excl_joint_limit_usd', 'The $500,000 joint limit'), (A, 'excl_joint_limit_usd', statute_joint),
            (E, 'exclusion_effective_month', 'took effect in ' + _month(eff)), (A, 'exclusion_effective_month', eff_quote),
            (E, 'exclusion_effective_month', f'that {eff[:4]} limit'),
            (A, 'cpi_1997_05', '1997-05-01' in cpi_),
            (E, 'cpi_2026_08', f'in {_month(cpi_last)} prices'), (A, 'cpi_2026_08', cpi_last == '2026-08-01'),
            (E, 'excl_joint_1997_in_2026_usd', 'about ' + _usd(round(real, -3)))],
        2: [(E, 'buy_year', f'bought in {yr}'), (E, 'excl_joint_limit_usd', f'exceeds {_usd(EXCL_JOINT)}'),
            (A, 'excl_joint_limit_usd', statute_joint)],
        3: [(E, 'buy_year', f'from {yr} to'), (E, 'sale_quarter', f'to {_quarter(NOW)}'), (A, 'sale_quarter', now_is_last),
            (E, 'buy_year', f'the {yr} purchase price')]
           + [(E, f'threshold_joint_{m}_usd', f'{thr_r[m]} in {NAMES[m]}') for m in METROS.values()]
           + [(E, 'threshold_joint_us_usd', 'national index: ' + _usd(round(t_us, -2))),
              (E, 'excl_single_limit_usd', f'the {_usd(EXCL_SINGLE)} limit'), (A, 'excl_single_limit_usd', statute_single),
              (E, 'threshold_single_us_usd', 'limit: ' + _usd(round(t_single, -2)))],
        4: [(E, 'metros_threshold_under_300k', f'In {len(under300)} of these'),
            (E, 'n_metros', f'these {len(METROS)} metros'),
            (E, 'threshold_cutoff_300k_usd', 'threshold is under $300,000'),
            (E, 'metros_threshold_under_200k', f'in {len(under200)} it is under'),
            (E, 'threshold_cutoff_200k_usd', 'under $200,000')],
        5: [(A, 'basis_at_death_rule', "fair market value of the property at the date of the decedent's death"
             in prov['26 U.S.C. 1014(a)(1)']),
            (A, 'long_term_gain_rule', 'capital asset held for more than 1 year' in prov['26 U.S.C. 1222(3)'])],
        6: [(E, 'excl_joint_limit_usd', f"'{_usd(EXCL_JOINT)} is more than our profit'")],
        7: [(E, 'metros_threshold_under_300k', f'In {len(under300)} of the'),
            (E, 'n_metros', f'the {len(METROS)} metros'),
            (E, 'buy_year', f'a {yr} purchase price'),
            (E, 'threshold_cutoff_300k_usd', 'under $300,000'),
            (A, 'metros_under_300k_names', 'phoenix' in under300 and 'dallas' in under300),
            (A, 'threshold_joint_phoenix_usd', t['phoenix'] < 300000),
            (A, 'threshold_joint_dallas_usd', t['dallas'] < 300000)],
        8: [(A, f'threshold_joint_{m}_usd', m in t) for m in METROS.values()],
        9: [(E, 'excl_joint_limit_usd', f'the {_usd(EXCL_JOINT)} home-sale limit'),
            (E, 'buy_year', f'for {yr} buyers'), ('ident', 'topic id', 'tax-2')],
        10: [(E, 'buy_year', f'in {yr},')],
        11: [(A, f'threshold_joint_{m}_usd', abs(t[m] * (g[m] - 1) - EXCL_JOINT) < 1e-6) for m in METROS.values()],
        12: [(E, 'buy_year', f'Most {yr} buyers')],
        13: [(E, 'buy_year', f'of {yr} purchase prices'),
             (A, 'buy_year', all(f.startswith(('ATNHPIUS', 'USSTHPI', 'CPIAUCNS')) for f in os.listdir(D)))],
        14: [(E, 'buy_year', f'a {yr} price')],
        15: [(E, 'excl_joint_1997_in_2026_usd', 'about ${:.2f} million'.format(real / 1e6)),
             (E, 'cpi_2026_08', f'in {_month(cpi_last)} prices')],
        16: [(E, 'sale_quarter', f'values to {_quarter(NOW)}'), (A, 'sale_quarter', now_is_last)],
        17: [(A, 'threshold_joint_los_angeles_usd',
              'Los Angeles-Long Beach-Glendale, CA (metro division)'
              in next(s['provider'] for s in srcs['series'] if s['id'] == 'ATNHPIUS31084Q'))],
        18: [(A, 'excl_joint_limit_usd', statute_joint)],
        # E1 (applied 2026-10-04): '2-year' (surviving spouse) is read from the 26 U.S.C. 121(b)(4) quote.
        19: [(E, 'surviving_spouse_window_years', '(2-year window)'),
             (A, 'surviving_spouse_window_years',
              'not later than 2 years after the date of death of such spouse' in prov.get('26 U.S.C. 121(b)(4)', ''))],
        20: [(A, 'threshold_single_us_usd',
              [k for k in out if k.startswith('threshold_single')] == ['threshold_single_us_usd'])],
        21: [(E, 'buy_year', f'Home in {yr}?'), (E, 'excl_joint_limit_usd', f'The {_usd(EXCL_JOINT)} Tax-Free')],
        22: [(E, 'buy_year', f'house in {yr}')],
        23: [(E, 'buy_year', f'bought in {yr} now'), (E, 'excl_joint_limit_usd', f'the {_usd(EXCL_JOINT)} tax-free limit')],
        24: [(E, 'buy_year', f'since {yr}')] + [(A, f'growth_{m}', g[m] > 1) for m in METROS.values()]
            + [(A, 'excl_joint_limit_usd', statute_joint), (A, 'excl_joint_1997_in_2026_usd', real > EXCL_JOINT)],
    }[n]

    ok = text in pool
    fails = [] if ok else ['text not verbatim in ' + st['source']]
    covered = [False] * len(text)  # characters explained by an expected rendering (overlaps allowed)
    for kind, q, v in spec:
        if kind == A and not v:
            fails.append(f'assert {q}')
        if kind in (E, 'ident'):
            if v not in text:
                fails.append(f'missing {q}: {v!r}')
            for m in re.finditer(re.escape(v), text):
                covered[m.start():m.end()] = [True] * len(v)
    orphans = [c for c, cov in zip(text, covered) if c.isdigit() and not cov]
    if orphans:
        fails.append('orphan digits: ' + ''.join(c if cov else '_' for c, cov in zip(text, covered)))
    used = {q for kind, q, v in spec if kind != 'ident'}
    if used != set(st['uses']):
        fails.append(f'uses mismatch: {sorted(used ^ set(st["uses"]))}')
    if fails:
        print('\n'.join(fails), file=sys.stderr)
    return not fails


if len(sys.argv) > 1:
    args = sys.argv[1:]
    verbose = '-v' in args
    args = [a for a in args if a != '-v']
    if len(args) != 2 or args[0] != '--statement' or not (args[1] == 'all' or args[1].isdigit()):
        sys.exit('usage: calc.py [--statement N|all [-v]]')
    if args[1] == 'all':
        n_all = len(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'statements.json'))))
        results = [(n, _statement(n)) for n in range(1, n_all + 1)]
        for n, r in results:
            print(f'{n}: {r}' if verbose else r)
        if verbose:
            print(f'{sum(r for _, r in results)}/{len(results)} True')
    else:
        print(_statement(int(args[1])))
else:
    print(json.dumps(out))

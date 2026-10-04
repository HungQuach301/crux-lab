"""retire-4: a savings bond guaranteed to reach double its price after 20 years vs rolling 3-month T-bills for 20 years,
every monthly start Jan 1934 .. Aug 2006 (end months up to Aug 2026). Also checks the doubling against consumer prices.
Reads data/TB3MS.csv and data/CPIAUCNS.csv only. Taxes ignored. History, not a forecast."""
import csv, json, statistics


def load(name):
    d = {}
    for row in list(csv.reader(open(f'data/{name}.csv')))[1:]:
        if row[1] not in ('', '.'):
            d[row[0]] = float(row[1])
    return d


tb, cpi = load('TB3MS'), load('CPIAUCNS')
dates = sorted(tb)
idx = {d: i for i, d in enumerate(dates)}
# growth index: each month earns TB3MS/12 percent (simple monthly roll of the quoted 3-month bill rate)
grow = [1.0]
for d in dates:
    grow.append(grow[-1] * (1 + tb[d] / 1200))

N = 240
rows = []
for i, s in enumerate(dates):
    if i + N > len(dates):
        break
    tbill = grow[i + N] / grow[i]
    e = dates[i + N] if i + N < len(dates) else None
    rows.append((s, tbill))

won = [r for r in rows if r[1] > 2.0]
since90 = [r for r in rows if r[0] >= '1990-01-01']
latest = rows[-1]


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


real = []
for s, _ in rows:
    e = add_months(s, N)
    if s in cpi and e in cpi:
        real.append((s, 2.0 * cpi[s] / cpi[e]))
out = {
    'starts': len(rows),
    'first_start': rows[0][0],
    'last_start': latest[0],
    'share_tbills_above_double_pct': round(100 * len(won) / len(rows), 1),
    'median_tbill_multiple_20y': round(statistics.median(r[1] for r in rows), 3),
    'min_tbill_multiple_20y': round(min(r[1] for r in rows), 3),
    'max_tbill_multiple_20y': round(max(r[1] for r in rows), 3),
    'share_tbills_above_double_starts_since_1990_pct': round(100 * sum(r[1] > 2.0 for r in since90) / len(since90), 1),
    'latest_tbill_multiple_20y': round(latest[1], 3),
    'doubling_rate_pct_per_year': round(100 * (2 ** (1 / 20) - 1), 2),
    'real_windows': len(real),
    'share_double_beat_prices_pct': round(100 * sum(r[1] >= 1.0 for r in real) / len(real), 1),
    'median_real_value_double_pct': round(100 * statistics.median(r[1] for r in real), 1),
    'tb3ms_latest_pct': tb['2026-08-01'],
}


# ---------------------------------------------------------------------------------------------------------------
# Dossier v1 supplement (playbook/topic-dossier.md §3, 2026-10-04): quantities used by statements.json, and
# `--statement N`, which recomputes every number in statement N from the data and prints True/False.
# The default run above is unchanged (it prints the frozen result.json numbers).
import re, sys, os

GUARANTEE_FROM = '2005-05-01'  # 31 CFR 351.34(a): bonds issued May 1, 2005 or later (sources.json provisions)


def share_above(sel):
    return round(100 * sum(r[1] > 2.0 for r in sel) / len(sel), 1)


def q_all():
    g = [r for r in rows if r[0] >= GUARANTEE_FROM]
    early = [r for r in rows if r[0] < '1950-01-01']
    mid = [r for r in rows if '1950-01-01' <= r[0] < '1990-01-01']
    lost = [r for r in real if r[1] < 1.0]
    worst_real = min(real, key=lambda r: r[1])
    lo, hi = min(rows, key=lambda r: r[1]), max(rows, key=lambda r: r[1])
    # since-1990 starts whose average bill rate over the 240 months was below the rate in the start month
    below = [r for r in since90 if statistics.mean(tb[d] for d in dates[idx[r[0]]:idx[r[0]] + N]) < tb[r[0]]]
    q = dict(out)
    q['viewer_age_decade'] = VIEWER_AGE_DECADE
    q.update({
        'horizon_years': N // 12, 'horizon_months': N, 'bill_term_months': 3, 'bills_per_horizon': N // 3,
        'latest_window_end': dates[-1], 'tb3ms_latest_month': dates[-1], 'since_1990_from': '1990-01-01',
        'min_start': lo[0], 'max_start': hi[0],
        'guarantee_from': GUARANTEE_FROM,
        'starts_with_guarantee': len(g), 'starts_hypothetical': len(rows) - len(g),
        'share_hypothetical_pct': round(100 * (len(rows) - len(g)) / len(rows), 1),
        'share_above_double_guarantee_starts_pct': share_above(g),
        'min_multiple_guarantee_starts': round(min(r[1] for r in g), 3),
        'max_multiple_guarantee_starts': round(max(r[1] for r in g), 3),
        'starts_1934_1949': len(early), 'share_above_double_1934_1949_pct': share_above(early),
        'early_from': '1934-01-01', 'early_to': '1949-12-01',
        'starts_1950_1989': len(mid), 'share_above_double_1950_1989_pct': share_above(mid),
        'mid_from': '1950-01-01', 'mid_to': '1989-12-01',
        'starts_since_1990': len(since90),
        'share_double_lost_buying_power_pct': round(100 * len(lost) / len(real), 1),
        'last_lost_start': max(r[0] for r in lost),
        'worst_real_value_double_pct': round(100 * worst_real[1], 1), 'worst_real_start': worst_real[0],
        'share_since_1990_avg_below_start_pct': round(100 * len(below) / len(since90), 1),
        'mean_tb3ms_all_pct': round(statistics.mean(tb.values()), 2),
        'nonoverlap_periods': len(dates) // N,
        'near_double_band_pct': 0.5,
        'near_double_starts': sum(abs(r[1] / 2.0 - 1) < 0.005 for r in rows),
    })
    return q


MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def forms(v):
    """Ways a quantity may be written in a statement (numeric tokens only)."""
    if isinstance(v, str) and re.fullmatch(r'\d{4}-\d{2}-01', v):
        return {v[:4]}
    if isinstance(v, int):
        return {str(v), f'{v:,}'}
    s = repr(v)
    return {s, s.rstrip('0').rstrip('.') if '.' in s else s}


def month_names(v):
    if isinstance(v, str) and re.fullmatch(r'\d{4}-\d{2}-01', v):
        m = MONTHS[int(v[5:7]) - 1]
        return {f'{m} {v[:4]}', f'{m[:3]} {v[:4]}'}
    return set()


# Qualitative words in a statement ("nearly every", "none", "below", "near") are checked here: statement id -> predicate.
RELATIONS = {
    'ans-2': lambda q: q['median_tbill_multiple_20y'] > 2.0,
    'ans-4': lambda q: q['share_above_double_1950_1989_pct'] > 50 and q['share_tbills_above_double_starts_since_1990_pct'] < 10,
    'ans-5': lambda q: q['latest_tbill_multiple_20y'] < 2.0,
    'ans-6': lambda q: q['share_above_double_guarantee_starts_pct'] == 0.0,
    'ans-7': lambda q: q['median_real_value_double_pct'] > 100 and q['share_double_beat_prices_pct'] < 100,
    'guess-1': lambda q: q['tb3ms_latest_pct'] > q['doubling_rate_pct_per_year'],
    'chg-1': lambda q: q['share_above_double_1950_1989_pct'] > 90 and q['share_tbills_above_double_starts_since_1990_pct'] < 10
                       and q['bills_per_horizon'] * q['bill_term_months'] == q['horizon_months'],
    'chg-2': lambda q: q['share_since_1990_avg_below_start_pct'] > 50,
    'chg-3': lambda q: q['worst_real_value_double_pct'] < 100,
    'lim-1': lambda q: q['share_above_double_1934_1949_pct'] == 0.0,
    'risk-1': lambda q: abs(q['mean_tb3ms_all_pct'] - q['doubling_rate_pct_per_year']) < 0.5,
    'risk-2': lambda q: q['share_tbills_above_double_starts_since_1990_pct'] < q['share_tbills_above_double_pct'],
    'risk-3': lambda q: GUARANTEE_FROM in guarantee_cites(),
    'risk-4': lambda q: q['share_double_beat_prices_pct'] < 100,
    'card-1': lambda q: q['first_start'][:4] == '1934',  # "since the Depression"
}
VIEWER_AGE_DECADE = 40  # card.json viewer: audience definition, not a data claim


def guarantee_cites():
    """Month the 20-year doubling terms start, read from the cited provision in sources.json."""
    here = os.path.dirname(os.path.abspath(__file__))
    cites = ' '.join(p['cite'] for p in json.load(open(os.path.join(here, 'sources.json')))['provisions'])
    return {'2005-05-01'} if 'May 1, 2005' in cites else set()


def check_statement(n):
    here = os.path.dirname(os.path.abspath(__file__))
    st = json.load(open(os.path.join(here, 'statements.json')))[n - 1]
    q = q_all()
    for u in st['uses']:
        if u not in q:
            print(f'unknown quantity {u}')
            return False
    text = st['text']
    for u in st['uses']:  # month-name dates first, so "Sep 2006" is not read as the year of another quantity
        for f in month_names(q[u]):
            text = text.replace(f, ' ')
    allowed = set().union(*(forms(q[u]) for u in st['uses'])) if st['uses'] else set()
    bad = [t for t in re.findall(r'\d[\d,]*(?:\.\d+)?', text) if t.rstrip(',') not in allowed]
    for t in bad:
        print(f'number not from its quantities: {t}')
    rel = RELATIONS.get(st['id'], lambda q: True)(q)
    if not rel:
        print('qualitative relation false')
    return not bad and rel


if len(sys.argv) == 3 and sys.argv[1] == '--statement':
    print(check_statement(int(sys.argv[2])))
elif len(sys.argv) == 2 and sys.argv[1] == '--quantities':
    print(json.dumps(q_all(), indent=1))
else:
    print(json.dumps(out))

"""retire-3: lock a 5-year rate vs roll 1-year rates for 5 years, every monthly start Apr 1953 .. Aug 2022, with focus on
starts when the 1-year yield was above the 5-year yield. Uses Treasury constant-maturity yields as stand-ins for CD rates.
Reads data/GS1.csv and data/GS5.csv only. History, not a forecast."""
import csv, json, statistics


def load(name):
    d = {}
    for row in list(csv.reader(open(f'data/{name}.csv')))[1:]:
        if row[1] not in ('', '.'):
            d[row[0]] = float(row[1])
    return d


g1, g5 = load('GS1'), load('GS5')


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


rows = []
for s in sorted(g5):
    rolls = [add_months(s, 12 * k) for k in range(5)]
    if s not in g1 or not all(r in g1 for r in rolls):
        continue
    lock = (1 + g5[s] / 100) ** 5
    roll = 1.0
    for r in rolls:
        roll *= 1 + g1[r] / 100
    rows.append((s, g1[s] - g5[s], lock, roll))

inv = [r for r in rows if r[1] > 0]
# separate inversion episodes = runs of consecutive inverted start months
episodes, prev = [], None
for r in inv:
    if prev is None or add_months(prev, 1) != r[0]:
        episodes.append([])
    episodes[-1].append(r)
    prev = r[0]
ep_lock = sum(1 for ep in episodes if sum(x[2] > x[3] for x in ep) > len(ep) / 2)
gap_inv = [100 * (x[2] / x[3] - 1) for x in inv]
out = {
    'starts_all': len(rows),
    'first_start_year': int(rows[0][0][:4]),
    'last_start_year': int(rows[-1][0][:4]),
    'share_lock_ahead_all_pct': round(100 * sum(x[2] > x[3] for x in rows) / len(rows), 1),
    'starts_inverted': len(inv),
    'share_lock_ahead_inverted_pct': round(100 * sum(x[2] > x[3] for x in inv) / len(inv), 1),
    'inversion_episodes': len(episodes),
    'episodes_lock_ahead_majority': ep_lock,
    'median_lock_vs_roll_inverted_pct': round(statistics.median(gap_inv), 2),
    'best_lock_vs_roll_inverted_pct': round(max(gap_inv), 2),
    'worst_lock_vs_roll_inverted_pct': round(min(gap_inv), 2),
    'gs1_latest_pct': g1['2026-08-01'],
    'gs5_latest_pct': g5['2026-08-01'],
}
print(json.dumps(out))

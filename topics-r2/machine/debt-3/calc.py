"""debt-3: a fixed mortgage payment that starts at 35% of pay; how long did average pay growth take to bring it to 28%?
Reads data/AHETPI.csv (average hourly earnings of production and nonsupervisory employees, monthly, seasonally adjusted).
Prints one JSON {id: value}."""
import csv, json, statistics

w = {r[0]: float(r[1]) for r in list(csv.reader(open('data/AHETPI.csv')))[1:] if r[1] not in ('', '.')}
m = sorted(w)
TARGET = 35 / 28   # pay must grow by this factor for a fixed payment to fall from 35% to 28%
res = []
for i, a in enumerate(m):
    k = next((j - i for j in range(i, len(m)) if w[m[j]] >= w[a] * TARGET - 1e-12), None)
    if k is not None:
        res.append((a, k))
months = [k for _, k in res]
s90 = [k for a, k in res if a >= '1990-01-01']
share5 = [35 * w[m[i]] / w[m[i + 60]] for i in range(len(m) - 60) if m[i] >= '1990-01-01']
fast = min(res, key=lambda t: t[1])
out = {
    'n_starts': len(res), 'first_start': res[0][0], 'last_start': res[-1][0],
    'median_months': statistics.median(months), 'min_months': fast[1], 'min_start': fast[0],
    'max_months': max(months), 'share_le48': round(sum(k <= 48 for k in months) / len(months), 3),
    'n_starts_1990': len(s90), 'median_months_1990': statistics.median(s90),
    'min_months_1990': min(s90), 'share_le48_1990': round(sum(k <= 48 for k in s90) / len(s90), 3),
    'median_share_after60_1990': round(statistics.median(share5), 1),
    'n_share5_1990': len(share5),
}
print(json.dumps(out))

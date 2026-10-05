import csv, json, statistics, sys
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

def load(sid):
    out = {}
    for row in csv.DictReader(open('data/%s.csv' % sid)):
        v = row[sid].strip()
        if v in ('', '.'): continue
        y, m, _ = row['observation_date'].split('-')
        out[(int(y), int(m))] = Decimal(v)   # exact decimal values
    return out
GS = {k: load(k) for k in ('GS1', 'GS2', 'GS3', 'GS5')}

def add(ym, n):
    i = ym[0]*12 + ym[1]-1 + n
    return (i//12, i % 12 + 1)

def yld(t, m):
    if m == 4: return (GS['GS3'][t] + GS['GS5'][t]) / 2
    if m == 3: return GS['GS3'][t]
    if m == 2:
        if t in GS['GS2']: return GS['GS2'][t]
        return (GS['GS1'][t] + GS['GS3'][t]) / 2
    if m == 1: return GS['GS1'][t]

END = (2026, 8)
starts = sorted(s for s in GS['GS5'] if s >= (1953, 4) and add(s, 60) <= END)

def run(thresh, exact=True):
    res = []
    for s in starts:
        r = GS['GS5'][s]
        called = False; val = None
        for k in (1, 2, 3, 4):
            t = add(s, 12*k); m = 5 - k
            y = yld(t, m)
            cond = (r - y >= thresh) if exact else (float(r) - float(y) >= float(thresh))
            if cond:
                called = True
                val = (1 + (float(r)+0.5)/100)**k * (1 + float(y)/100)**m
                break
        if not called:
            val = (1 + (float(r)+0.5)/100)**5
        nc = (1 + float(r)/100)**5
        d = 100*(val**0.2 - nc**0.2)
        res.append((s, called, d))
    return res

def rnd(x, q):
    return float(Decimal(repr(x)).quantize(Decimal(q), rounding=ROUND_HALF_UP))
def pct(n, d): return rnd(100*n/d, '0.1')

R = run(Decimal('0.25')); R5 = run(Decimal('0.50'))
N = len(R)
called = [x for x in R if x[1]]
since = [x for x in R if x[0] >= (2000, 1)]
ds = [x[2] for x in R]
fmt = lambda s: '%04d-%02d-01' % s
out = {
 'starts': N,
 'first_start': fmt(starts[0]),
 'last_start': fmt(starts[-1]),
 'share_called_pct': pct(len(called), N),
 'share_callable_ahead_pct': pct(sum(d > 0 for d in ds), N),
 'median_diff_pts_per_year': rnd(statistics.median(ds), '0.01'),
 'mean_diff_pts_per_year': rnd(statistics.fmean(ds), '0.01'),
 'worst_diff_pts_per_year': rnd(min(ds), '0.01'),
 'best_diff_pts_per_year': rnd(max(ds), '0.01'),
 'share_ahead_when_called_pct': pct(sum(x[2] > 0 for x in called), len(called)),
 'starts_since_2000': len(since),
 'share_called_since_2000_pct': pct(sum(x[1] for x in since), len(since)),
 'share_callable_ahead_since_2000_pct': pct(sum(x[2] > 0 for x in since), len(since)),
 'share_called_thresh050_pct': pct(sum(x[1] for x in R5), N),
 'share_callable_ahead_thresh050_pct': pct(sum(x[2] > 0 for x in R5), N),
 'gs5_latest_pct': float(GS['GS5'][END]),
}
json.dump(out, open('result.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
# diagnostics: float-comparison alternative, unrounded values
Rf = run(0.25, exact=False); Rf5 = run(0.50, exact=False)
print('float-compare diffs 0.25:', sum(a[1] != b[1] for a, b in zip(R, Rf)), ' 0.50:', sum(a[1] != b[1] for a, b in zip(R5, Rf5)), file=sys.stderr)
print('raw median %.6f mean %.6f min %.6f max %.6f' % (statistics.median(ds), statistics.fmean(ds), min(ds), max(ds)), file=sys.stderr)
print('called', len(called), 'ahead', sum(d > 0 for d in ds), 'zero d', sum(d == 0 for d in ds), file=sys.stderr)

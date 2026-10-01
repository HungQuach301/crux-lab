"""Tập 2 — mô hình (bên dựng). Lõi giống hệt topics-r1/machine/debt-2/calc.py (đã chạy lại: khớp result.json);
thêm các đại lượng phạm vi (b) định nghĩa ở gates/V0-defs.md. Đọc data/raw/TB3MS.csv. Ghi out/model.json.
python3 episodes/ep002/model/model.py"""
import csv, json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
P, N, FIXED, VAR0 = 50000.0, 120, 9.00, 7.50
FIRST_START, SPLIT = '1954-01-01', '1981-01-01'
GAPS = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
CAPS = [12.0, 15.0, 18.0, 25.0]

rows = [(r[0], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:]
        if r[1] not in ('', '.')]
dates = [d for d, _ in rows]
tb = [v for _, v in rows]
IDX = tb[-1]


def run(path):
    """-> (total interest, list of 120 monthly payments)"""
    bal, tot, cur, pay, pays = P, 0.0, None, 0.0, []
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200
            pay = bal * x / (1 - (1 + x) ** -(N - k))
            cur = r
        i = bal * r / 1200
        tot += i
        bal -= pay - i
        pays.append(pay)
    return tot, pays


FIX_INT, FIX_PAYS = run([FIXED] * N)
starts = [s for s in range(len(tb)) if dates[s] >= FIRST_START and s + N <= len(tb)]


def windows(var0, cap=None):
    m = var0 - IDX
    out = []
    for s in starts:
        path = [round(m + max(0.0, IDX + tb[s + k] - tb[s]), 6) for k in range(N)]
        if cap is not None:
            path = [min(cap, r) for r in path]
        vi, pays = run(path)
        out.append({'start': dates[s], 'diff': vi - FIX_INT, 'maxRate': max(path), 'maxPay': max(pays),
                    'path': path})
    return out


def share(ws, pred=lambda w: True):
    sel = [w for w in ws if pred(w)]
    return round(100 * sum(w['diff'] > 0 for w in sel) / len(sel), 1), len(sel)


def summary(ws):
    worst = max(ws, key=lambda w: w['diff'])
    return {
        'share_costlier': share(ws)[0],
        'share_costlier_1954_1980': share(ws, lambda w: w['start'] < SPLIT)[0],
        'share_costlier_1981_on': share(ws, lambda w: w['start'] >= SPLIT)[0],
        'median_diff': round(statistics.median(w['diff'] for w in ws)),
        'worst_diff': round(worst['diff']), 'worst_start': worst['start'],
        'best_diff': round(min(w['diff'] for w in ws)),
    }


base = windows(VAR0)
s = summary(base)
early = [w for w in base if w['start'] < SPLIT]
late = [w for w in base if w['start'] >= SPLIT]
maxpay_w = max(base, key=lambda w: w['maxPay'])
worst_w = max(base, key=lambda w: w['diff'])
out = {
    'conventions': {'loan': P, 'termMonths': N, 'fixedRate': FIXED, 'variableStart': VAR0,
                    'index': 'FRED TB3MS', 'firstStart': FIRST_START, 'regimeSplit': SPLIT},
    'base': {
        'n_starts': len(base), 'first_start': base[0]['start'], 'last_start': base[-1]['start'],
        'fixed_total_interest': round(FIX_INT),
        'share_variable_costlier': s['share_costlier'],
        'median_variable_minus_fixed': s['median_diff'],
        'worst_variable_minus_fixed': s['worst_diff'], 'worst_start': s['worst_start'],
        'best_variable_minus_fixed': s['best_diff'],
        'max_variable_rate_any_window': round(max(w['maxRate'] for w in base), 2),
        'n_starts_1954_1980': len(early), 'share_costlier_1954_1980': s['share_costlier_1954_1980'],
        'n_starts_1981_on': len(late), 'share_costlier_1981_on': s['share_costlier_1981_on'],
        'share_rate_above_fixed': round(100 * sum(w['maxRate'] > FIXED for w in base) / len(base), 1),
        'worst_peak_rate': round(worst_w['maxRate'], 2),
        'best_start': min(base, key=lambda w: w['diff'])['start'],
        'index_today': IDX, 'index_date': dates[-1], 'margin': round(VAR0 - IDX, 2),
    },
    'payments': {
        'fixed_payment': round(FIX_PAYS[0], 2),
        'variable_first_payment': round(run([VAR0] * N)[1][0], 2),
        'max_variable_payment_any_window': round(maxpay_w['maxPay'], 2),
        'max_variable_payment_start': maxpay_w['start'],
        'median_window_max_payment': round(statistics.median(w['maxPay'] for w in base), 2),
        'share_windows_max_payment_above_fixed': round(100 * sum(w['maxPay'] > FIX_PAYS[0] for w in base) / len(base), 1),
    },
    'gaps': {f'{g:.1f}': summary(windows(FIXED - g)) for g in GAPS},
    'caps': {f'{c:g}': summary(windows(VAR0, c)) for c in CAPS},
    'windows': [{'start': w['start'], 'diff': round(w['diff'], 2), 'maxRate': round(w['maxRate'], 4),
                 'maxPay': round(w['maxPay'], 2)} for w in base],
    'worstPath': {'start': worst_w['start'], 'rates': [round(r, 4) for r in worst_w['path']]},
}
os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
json.dump(out, open(os.path.join(EP, 'out/model.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ('windows', 'worstPath')}, indent=1))

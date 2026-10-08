"""Token thực từ log phiên (REPORT §1). Đầu vào: JSONL trích từ sự kiện `result` của transcript phiên
(list_events kinds=["result"]); mỗi dòng: s, uuid, t, pti, origin, u=[in, ghi cache, đọc cache, ra] của lượt
(luồng chính), mu={model: [in, ghi cache, đọc cache, ra]} TÍCH LUỸ cả phiên (gồm agent con, qua các lần khởi động lại).
Khử trùng theo uuid. Trần = đầu vào mới (in + ghi cache) + sinh ra; đọc cache báo riêng.
    python3 tongket-t5/token_log.py tongket-t5/logs/*.jsonl [--windows tongket-t5/windows.json]
"""
import json, sys

def load(paths):
    rows = {}
    for p in paths:
        for line in open(p):
            line = line.strip()
            if line:
                d = json.loads(line); rows[d['uuid']] = d
    return sorted(rows.values(), key=lambda d: (d['s'], d['t']))

def tot(mu):
    a = [0, 0, 0, 0]
    for v in (mu or {}).values():
        for i in range(4):
            a[i] += v[i] or 0
    return a

def ceil(a):
    return a[0] + a[1] + a[3]

def per_session(rows):
    out = {}
    for d in rows:
        if d.get('mu'):
            c = tot(d['mu'])
            if d['s'] not in out or ceil(c) >= ceil(out[d['s']]['cum']):
                out[d['s']] = {'cum': c, 'mu': d['mu'], 't': d['t']}
    return out

def turns(rows):
    """Mỗi lượt: delta tích luỹ (chính + agent con) và phần luồng chính (u)."""
    res, prev = [], {}
    for d in rows:
        if not d.get('mu'):
            continue
        c = tot(d['mu']); p = prev.get(d['s'], [0, 0, 0, 0])
        delta = [c[i] - p[i] for i in range(4)]
        if ceil(delta) < 0:            # tích luỹ không được giảm; nếu giảm thì báo
            print('CẢNH BÁO: tích luỹ giảm', d['s'], d['t'], file=sys.stderr)
        prev[d['s']] = c
        res.append({'s': d['s'], 't': d['t'], 'delta': delta, 'main': d.get('u') or [0, 0, 0, 0],
                    'origin': d.get('origin'), 'txt': d.get('txt', '')})
    return res

def fmt(n):
    return f'{n/1e6:.2f}'

if __name__ == '__main__':
    args = sys.argv[1:]
    win = None
    if '--windows' in args:
        i = args.index('--windows'); win = json.load(open(args[i + 1])); args = args[:i] + args[i + 2:]
    rows = load(args)
    print('| phiên | lượt result | sinh ra | đầu vào mới | đọc cache | trần (mới + ra) |')
    for s, v in per_session(rows).items():
        c = v['cum']; n = sum(1 for d in rows if d['s'] == s)
        print(f'| {s} | {n} | {fmt(c[3])} | {fmt(c[0]+c[1])} | {fmt(c[2])} | **{fmt(ceil(c))}** |')
    if win:
        T = turns(rows)
        print('\n| cửa sổ | từ | đến | trần cả (triệu) | luồng chính | agent con | đọc cache |')
        for w in win:
            sel = [x for x in T if x['s'] == w['s'] and w['from'] <= x['t'] < w['to']]
            a = [sum(x['delta'][i] for x in sel) for i in range(4)]
            m = [sum(x['main'][i] for x in sel) for i in range(4)]
            print(f"| {w['name']} | {w['from'][5:16]} | {w['to'][5:16]} | {fmt(ceil(a))} | {fmt(ceil(m))} | {fmt(ceil(a)-ceil(m))} | {fmt(a[2])} |")

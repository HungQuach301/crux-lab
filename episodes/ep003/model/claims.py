"""Tập 3 · out/claims.json theo checks/CONTRACT.md (K3.7): `value` CHƯA làm tròn (từ model.py → out/claim-values.json),
`display` = dạng hiện trên hình/lời. Tự kiểm: làm tròn `value` theo số chữ số của numbers.md phải trùng numbers.md.
    python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/claims.py"""
import json, os, re
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
vals = json.load(open(f'{EP}/out/claim-values.json'))
rows, ctx = {}, {}
for ln in open(f'{EP}/numbers.md', encoding='utf-8'):
    m = re.match(r'^\| `([a-z0-9_]+)` \| ([^|]+) \| ([^|]+) \| ([^|]*) \|', ln)
    if m:
        cid, a, b, c = (x.strip() for x in m.groups())
        if cid.startswith('ctx_'):
            ctx[cid] = {'what': a, 'source': b, 'level': c}
        else:
            rows[cid] = {'num': a, 'unit': b, 'meaning': c}
claims, bad = [], []
for cid, r in rows.items():
    v, num, unit = (40 if cid == 'viewer_age_decade' else vals.get(cid)), r['num'], r['unit']   # tuổi Dana: định nghĩa khán giả, ILLUSTRATIVE
    if re.match(r'^\d{4}-\d{2}-\d{2}$', num):
        disp = f'{MON[int(num[5:7]) - 1]} {num[:4]}'
        if v != num:
            bad.append((cid, v, num))
    else:
        dec = len(num.split('.')[1]) if '.' in num else 0
        disp = f'×{num}' if unit == 'multiple' else f'{num}%' if unit.startswith('%') else num
        if v is None or f'{v:.{dec}f}' != num:
            bad.append((cid, v, num))
    claims.append({'claimId': cid, 'value': v, 'display': disp, 'unit': unit, 'formula': r['meaning'],
                   'source': {'id': 'model', 'url': None} if cid != 'viewer_age_decade' else None,
                   'dataYears': [1934, 2026], 'historical': cid != 'viewer_age_decade', 'illustrative': cid == 'viewer_age_decade',
                   'shownIn': [], 'spoken': None})
for cid, r in ctx.items():
    claims.append({'claimId': cid, 'value': None, 'display': r['what'], 'kind': 'context', 'formula': None,
                   'source': {'id': r['source'], 'url': None}, 'historical': False, 'illustrative': False, 'shownIn': [], 'spoken': None})
json.dump({'claims': claims}, open(f'{EP}/out/claims.json', 'w'), indent=1, ensure_ascii=False)
print(len(claims), 'claims;', len(rows), 'model/definition rows;', 'rounding self-check mismatches:', bad)
raise SystemExit(1 if bad else 0)

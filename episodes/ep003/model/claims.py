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
CTX_FORMULA = {  # how each context claim is established (REVIEWER C5 #5: one honest line each, not a generic filler)
    'ctx_guarantee': 'rule quoted from 31 CFR 351.34(a) and 351.35(f)(2): EE bonds issued from 2005-05 reach original maturity at 20 years, worth at least double the price (book-entry)',
    'ctx_hypothetical': 'episode assumption: today\'s guarantee applied to every start before 2005-05; count = model.json windows before subsetFrom:guarantee (856 of 873)',
    'ctx_penalty': 'rule quoted from 31 CFR 351.35(e): a bond redeemed before 5 years forfeits the last 3 months of interest',
    'ctx_ee_rate': 'rate quoted from the TreasuryDirect release of 2026-05-01: fixed 2.40% for EE bonds issued May to October 2026; the rate for new bonds is reset every May and November (re-check the rate announced 2026-11-01 right before publishing)',
    'ctx_tb_sep': 'FRED TB3MS value for 2026-09 (published 2026-10-01), outside the pinned data; not used on screen or in the narration',
    'ctx_cpi_rights': 'terms label quoted from the FRED series pages of TB3MS and CPIAUCNS (2026-10-04): "Public Domain: Citation Requested"',
}
# C5: where each claim is said (claim column of story/script.md) and shown (design/c5/shown.json: the page's own claim spans by scene,
# written by design/c5/probe.js); context claims carry how they are established as their formula
import os
spoken = {}
for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
    m = re.match(r'^(S\d\d)\.(\d+) \| .+? \| (.*?) \| ', ln)
    if m:
        for c in re.split(r'[,\s]+', m.group(3).strip()):
            if c and c != '—':
                spoken.setdefault(c, []).append({'scene': m.group(1), 'sentence': f'{m.group(1)}.{m.group(2)}'})
shown = json.load(open(f'{EP}/design/c5/shown.json')) if os.path.exists(f'{EP}/design/c5/shown.json') else {}
for c in claims:
    c['spoken'] = spoken.get(c['claimId'], [])
    c['shownIn'] = shown.get(c['claimId'], [])
    if c.get('formula') is None:
        c['formula'] = CTX_FORMULA[c['claimId']]
json.dump({'claims': claims}, open(f'{EP}/out/claims.json', 'w'), indent=1, ensure_ascii=False)
print(len(claims), 'claims;', len(rows), 'model/definition rows;', 'rounding self-check mismatches:', bad)
raise SystemExit(1 if bad else 0)

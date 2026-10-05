"""Tập 3 · C4: gộp hai lượt (ghi trước, ý đồ C4 v2 "Đếm và gộp"). Đọc `tally --json` của lượt NGHĨA và lượt KHUYÊN.
- Nghĩa (chỉ nhịp loại 1): tự tính từ `scores` theo dừng sớm §5.6, KHÔNG dùng cột advice của lượt nghĩa: 2 người đầu cùng đúng (điểm 1) → PASS,
  cùng không đúng → FAIL, lệch → cần người thứ 3; có 3 → PASS khi ≥ 2 đúng.
- Khuyên (7 nhịp): chỉ đọc cột `advice` (số người bị cờ). ≥ 1 → nhịp có khuyên.
- Nhịp loại 1 đạt = nghĩa PASS ∧ khuyên 0. Cổng = (#đạt / 6) ≥ 0,8 ∧ không nhịp nào (gồm KEY-3) có khuyên. Trong ±5% quanh 0,8 → nêu tên.
    python3 episodes/ep003/review-c4/combine.py MEAN_TALLY.json ADV_TALLY.json OUT.md [--prev PREV_COMBINED.json]"""
import json, sys
mean, adv, out = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), sys.argv[3]
prev = json.load(open(sys.argv[sys.argv.index('--prev') + 1])) if '--prev' in sys.argv else None


def mstatus(scores):
    c = [s == 1 for s in scores]
    if len(c) < 2:
        return 'PENDING'
    if len(c) == 2:
        return 'PASS' if all(c) else 'FAIL' if not any(c) else 'NEED_3RD'
    return 'PASS' if sum(c) >= 2 else 'FAIL'


rows = {}
for r in mean['rows']:
    if r['set'] == mean['candidate_set']:
        rows.setdefault(r['id'], {})['mean'] = {'scores': r['scores'], 'status': mstatus(r['scores'])}
for r in adv['rows']:
    if r['set'] == adv['candidate_set']:
        rows.setdefault(r['id'], {})['adv'] = {'flags': r['advice'], 'readers': r['readers']}
if prev:  # vòng 2: nhịp không kiểm lại giữ kết quả vòng trước
    for k, v in prev['rows'].items():
        for part in ('mean', 'adv'):
            if part in v and part not in rows.get(k, {}):
                rows.setdefault(k, {})[part] = {**v[part], 'carried': True}
img = [k for k in sorted(rows) if 'mean' in rows[k]]
ok = [k for k in img if rows[k]['mean']['status'] == 'PASS' and rows[k].get('adv', {}).get('flags', 1) == 0]
advb = [k for k in sorted(rows) if rows[k].get('adv', {}).get('flags', 0) > 0]
pend = [k for k in sorted(rows) if rows[k].get('mean', {}).get('status') in ('NEED_3RD', 'PENDING') or 'adv' not in rows[k]]
share = len(ok) / 6
verdict = 'PENDING' if pend else 'PASS' if share >= 0.8 and not advb else 'FAIL'
res = {'rows': rows, 'pass': ok, 'adviceBeats': advb, 'pending': pend, 'share': share, 'verdict': verdict, 'near': abs(share - 0.8) <= 0.05}
json.dump(res, open(out.replace('.md', '.json'), 'w'), indent=1)
L = ['| Nhịp | Nghĩa (điểm theo thứ tự) | Nghĩa | Khuyên (cờ/người) | Nhịp đạt |', '|---|---|---|---|---|']
for k in sorted(rows):
    m, a = rows[k].get('mean'), rows[k].get('adv')
    L.append(f"| {k} | {' · '.join(map(str, m['scores'])) if m else '— (loại 2)'}{' (giữ vòng trước)' if m and m.get('carried') else ''} | "
             f"{m['status'] if m else '—'} | {(str(a['flags']) + '/' + str(a['readers'])) if a else '—'}{' (giữ)' if a and a.get('carried') else ''} | "
             f"{'ĐẠT' if k in ok else '—' if not m else 'không'} |")
L.append(f"\n**Cổng C4: {len(ok)}/6 nhịp loại 1 đạt = {share:.0%} (ngưỡng 80%); khuyên ở: {', '.join(advb) or 'không nhịp nào'} → {verdict}"
         f"{' — trong ±5% quanh ngưỡng' if res['near'] else ''}.**" + (f" Chờ: {', '.join(pend)}." if pend else ''))
open(out, 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))

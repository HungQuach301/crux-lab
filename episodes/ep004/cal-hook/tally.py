"""Gộp hiệu chuẩn so cặp móc theo INTENT.md (ngưỡng không đổi)."""
import json, os
R = os.path.dirname(os.path.abspath(__file__))
key = {k['file']: k for k in json.load(open(f'{R}/key.json'))}
ans = [json.loads(l) for l in open(f'{R}/answers.jsonl')]
rows, tot = [], 0; by = {'A': [0, 0], 'B': [0, 0]}; pos = {'X': [0, 0], 'Y': [0, 0]}
for a in ans:
    k = key[a['file']]; o = 'X' if k['X'].endswith('orig') else 'Y'; hit = k[a['KEEP']].endswith('orig')
    tot += hit; by[k['sample']][0] += hit; by[k['sample']][1] += 1; pos[o][0] += hit; pos[o][1] += 1
    rows.append(f"| {a['file']} | {k['sample']} | {o} | {a['KEEP']} | {'gốc' if hit else 'kém'} | {a['STRENGTH']} |")
c1 = tot >= 7; c2 = all(v[0] >= 3 for v in by.values()); c3 = all(v[0] >= 3 for v in pos.values())
ok = c1 and c2 and c3
L = ['# Kết quả hiệu chuẩn so cặp móc (ngưỡng theo INTENT.md bản 2)', '', '| file | mẫu | gốc ở | chọn | = | độ mạnh |', '|---|---|---|---|---|---|'] + rows + ['',
     f'1. Chọn gốc: **{tot}/8** (cần ≥ 7) → {"đạt" if c1 else "TRƯỢT"}',
     f'2. Theo mẫu: A {by["A"][0]}/4, B {by["B"][0]}/4 (cần ≥ 3/4 mỗi mẫu) → {"đạt" if c2 else "TRƯỢT"}',
     f'3. Theo vị trí: gốc ở X {pos["X"][0]}/4, gốc ở Y {pos["Y"][0]}/4 (cần ≥ 3/4) → {"đạt" if c3 else "TRƯỢT"}', '',
     f'**Phép so cặp móc: {"ĐẠT" if ok else "KHÔNG ĐẠT"}**']
open(f'{R}/RESULT.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))

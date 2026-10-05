"""Gộp so cặp vòng tròn móc + tiêu đề (tham khảo) theo INTENT.md."""
import json, os, collections
R = os.path.dirname(os.path.abspath(__file__)); K = json.load(open(f'{R}/key.json')); key = {k['file']: k for k in K['key']}
ans = [json.loads(l) for l in open(f'{R}/answers.jsonl')]
W = collections.Counter(); TW = collections.Counter(); TA = collections.Counter(); rows = []; posX = 0
for a in ans:
    k = key[a['file']]; win = k[a['KEEP']]; W[win] += 1; posX += a['KEEP'] == 'X'
    tw = k['title1'] if a['CLICK'] == 1 else k['title2']; TW[tw] += 1; TA[k['title1']] += 1; TA[k['title2']] += 1
    rows.append(f"| {a['file']} | {k['X']} vs {k['Y']} | {win} | {k['title1']}–{k['title2']} | {tw} |")
L = ['# Chọn móc: so cặp vòng tròn (INTENT.md)', '', '| file | X vs Y | thắng | tiêu đề 1–2 | click |', '|---|---|---|---|---|'] + rows + ['',
     '**Lượt thắng móc:** ' + ', '.join(f'{h} {W[h]}/6' for h in ['H1', 'H2', 'H3']) + f' · chọn vị trí X {posX}/9',
     '**Tiêu đề (tham khảo):** ' + ', '.join(f'{t} {TW[t]}/{TA[t]}' for t in ['T1', 'T2', 'T3'])]
top = max(W.values()); best = [h for h in W if W[h] == top]
L.append(f"**Móc được chọn: {best[0] if len(best) == 1 else 'HOÀ ' + '/'.join(best) + ' → WRITER + REVIEWER chọn'}**")
open(f'{R}/RESULT.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))

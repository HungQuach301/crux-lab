"""Mechanical tally of the C6 blind pair test (no judgement): chosen card -> key.json -> winner. Counts per round, per role, total;
position bias; per pair both orders; verbatim reasons. Writes review-c6/pack-test/tally.json and tally.md (pasted into results.md).
python3 episodes/ep002/preprod/thumbs_c6/tally.py"""
import json, re
from collections import defaultdict
from pathlib import Path
EP = Path(__file__).resolve().parents[2]
D = EP / 'review-c6/pack-test'
key = json.loads((D / 'key.json').read_text())
ROLES = ['G', 'P', 'R', 'C']
rows = []
for pid, p in key['pairs'].items():
    for r in ROLES:
        f = D / pid / f'answer-{r}.md'
        txt = f.read_text()
        a = int(re.search(r'ANSWER:\s*([12])', txt).group(1))
        why = re.search(r'WHY:\s*(.+)', txt, re.S)
        rows.append({'id': pid, 'round': p['round'], 'role': r, 'one': p['1'], 'two': p['2'], 'pick': a, 'winner': p[str(a)], 'loser': p[str(3 - a)],
                     'why': (why.group(1) if why else txt).strip().replace('\n', ' ')})
out = {'rows': rows, 'rounds': {}}
md = []
for rd, items in (('T', list(key['roundT']['titles'])), ('M', list(key['roundM']['thumbs']))):
    R = [x for x in rows if x['round'] == rd]
    wins = {i: defaultdict(int) for i in items}; apps = {i: defaultdict(int) for i in items}
    for x in R:
        for i in (x['one'], x['two']):
            apps[i][x['role']] += 1; apps[i]['all'] += 1
        wins[x['winner']][x['role']] += 1; wins[x['winner']]['all'] += 1
    pos1 = {r: sum(1 for x in R if x['role'] == r and x['pick'] == 1) for r in ROLES}; pos1['all'] = sum(pos1.values())
    n = {r: sum(1 for x in R if x['role'] == r) for r in ROLES}; n['all'] = len(R)
    # per unordered pair: winner in each order, per role
    pairs = defaultdict(lambda: defaultdict(list))
    for x in R:
        k = tuple(sorted((x['one'], x['two'])))
        pairs[k][x['role']].append(x['winner'])
    pair_rows = []
    for k, byr in sorted(pairs.items()):
        allw = [w for r in ROLES for w in byr[r]]
        both = {r: (byr[r][0] if len(set(byr[r])) == 1 else 'split') for r in ROLES}
        pair_rows.append({'pair': k, 'wins': {i: allw.count(i) for i in k}, 'perRole': both})
    out['rounds'][rd] = {'wins': {i: dict(wins[i]) for i in items}, 'appearances': {i: dict(apps[i]) for i in items}, 'pos1': pos1, 'n': n, 'pairs': pair_rows}
    md.append(f'### Vòng {rd}: thắng / số lần xuất hiện\n')
    md.append('| Mục | ' + ' | '.join(f'vai {r}' for r in ROLES) + ' | **Tổng** |')
    md.append('|---|' + '---|' * (len(ROLES) + 1))
    for i in sorted(items, key=lambda i: -wins[i]['all']):
        md.append(f'| {i} | ' + ' | '.join(f"{wins[i][r]}/{apps[i][r]}" for r in ROLES) + f" | **{wins[i]['all']}/{apps[i]['all']}** |")
    md.append('')
    md.append('Lệch vị trí (chọn ô 1 / số lượt): ' + ' · '.join(f"{r} {pos1[r]}/{n[r]}" for r in ROLES) + f" · tổng {pos1['all']}/{n['all']}.\n")
    md.append('| Cặp | Thắng (tổng 8 lượt) | ' + ' | '.join(f'vai {r} (2 thứ tự)' for r in ROLES) + ' |')
    md.append('|---|---|' + '---|' * len(ROLES))
    for pr in pair_rows:
        md.append(f"| {pr['pair'][0]} – {pr['pair'][1]} | " + ' · '.join(f"{i} {c}" for i, c in pr['wins'].items()) + ' | ' + ' | '.join(pr['perRole'][r] for r in ROLES) + ' |')
    md.append('')
md.append('### Lý do nguyên văn (vòng · vai · ô 1 vs ô 2 → chọn)\n')
md.append('```')
for x in sorted(rows, key=lambda x: (x['round'], x['role'], x['one'], x['two'])):
    md.append(f"{x['round']} {x['role']} {x['one']} vs {x['two']} pick {x['pick']} = {x['winner']} | {x['why']}")
md.append('```')
(D / 'tally.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
(D / 'tally.md').write_text('\n'.join(md) + '\n')
print('\n'.join(md[:40]))

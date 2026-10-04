"""C1 kiểm mù: sinh mẫu kể lại (một file .md tên hex / thư mục) + thẻ so cặp tiêu đề (PNG). Khoá: review-c1/key.json.
python3 episodes/ep002/review-c1/make_c1.py  (cần node + playwright cho thẻ)"""
import json, os, re, secrets, subprocess, random
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = '/tmp/claude-0/-home-user-crux-lab/ce118c19-8f87-59ac-a641-3486272a248d/scratchpad/blind/C1'
src = open(os.path.join(EP, 'gates/C1-loglines.md')).read()
quote = lambda h: re.search(r'## ' + h + r'.*?\n> (.+?)\n', src, re.S).group(1).strip()
LOG = {'A': quote('Logline A'), 'B': quote('Logline B'), 'W': re.search(r'kể lại W:\*\*\n> (.+?)\n', src, re.S).group(1).strip()}
os.makedirs(DEST, exist_ok=True)
key = {'_': 'GIẢI MÃ — chỉ mở sau khi chấm.', 'retell': {}, 'pairs': {}}
used = set()
def hx():
    while True:
        h = secrets.token_hex(4)
        if h not in used: used.add(h); return h
jobs = []
for s in ('A', 'B', 'W'):
    for r in ['T'] * 5 + ['G']:
        jobs.append((s, r))
random.SystemRandom().shuffle(jobs)
for s, r in jobs:
    h = hx(); os.makedirs(f'{DEST}/{h}')
    open(f'{DEST}/{h}/{h}.md', 'w').write('# Video description\n\n' + LOG[s] + '\n')
    key['retell'][h] = {'sample': s, 'role': r}
TITLES = {'A1': 'Need Private Grad Loans? Variable vs Fixed Through History',
          'B1': 'Why a Variable Loan Can Rise Above Fixed and Still Cost Less',
          'D': '7.5% Variable or 9% Fixed? Grad Loans Through History',
          'X': 'Fixed vs Variable Student Loans Explained'}
roles = ['T', 'S', 'P', 'C']
pj = []
for i, c in enumerate(('A1', 'B1', 'D')):
    rs = roles[(i % 2) * 2:(i % 2) * 2 + 2] if i < 2 else [roles[1], roles[2]]
    # vai xoay: A1 -> T,S ; B1 -> P,C ; D -> S,P ... đảm bảo mỗi vai 3 lượt
    rs = {'A1': [('T', 'S'), ('P', 'C')], 'B1': [('P', 'C'), ('T', 'S')], 'D': [('C', 'T'), ('S', 'P')]}[c]
    pj += [(c, 'X', rs[0][0]), (c, 'X', rs[0][1]), ('X', c, rs[1][0]), ('X', c, rs[1][1])]
random.SystemRandom().shuffle(pj)
cards = []
for a, b, r in pj:
    h = hx(); os.makedirs(f'{DEST}/{h}')
    key['pairs'][h] = {'1': a, '2': b, 'role': r}
    cards.append({'id': h, 't1': TITLES[a], 't2': TITLES[b], 'out': f'{DEST}/{h}/{h}.png'})
json.dump(cards, open(f'{DEST}/_cards.json', 'w'))
json.dump({**key, 'titles': TITLES, 'loglines': LOG}, open(os.path.join(EP, 'review-c1/key.json'), 'w'), indent=1)
subprocess.run(['node', os.path.join(EP, 'review-c1/cards.js'), f'{DEST}/_cards.json'], check=True,
               env={**os.environ, 'NODE_PATH': '/opt/node22/lib/node_modules', 'PLAYWRIGHT_BROWSERS_PATH': '/opt/pw-browsers'})
os.remove(f'{DEST}/_cards.json')
from collections import Counter
print('retell', len(key['retell']), 'pairs', len(key['pairs']), Counter(v['role'] for v in key['pairs'].values()))

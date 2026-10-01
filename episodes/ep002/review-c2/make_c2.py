"""C2 kiểm mù: lời thuần ứng viên (script.md v2) + đối chứng yếu (M1b Tập 1). Một file hex / thư mục. Khoá review-c2/key.json."""
import json, os, re, secrets, random
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep002'
DEST = '/tmp/claude-0/-home-user-crux-lab/ce118c19-8f87-59ac-a641-3486272a248d/scratchpad/blind/C2'
def cand():
    out, cur = [], None
    for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
        m = re.match(r'^(S\d\d)\.\d+ \| (.+?) \| ', ln)
        if not m: continue
        t = re.sub(r'^\[[\w\- ]+\]\s*', '', m.group(2).strip())
        if m.group(1) != cur and out: out.append('')
        cur = m.group(1); out.append(t)
    paras, buf = [], []
    for l in out + ['']:
        if l: buf.append(l)
        elif buf: paras.append(' '.join(buf)); buf = []
    return '\n\n'.join(paras)
def weak():
    txt = open(f'{ROOT}/archive/ep001-v1/script-m1b.md', encoding='utf-8').read()
    lines = []
    for ln in txt.split('\n'):
        ln = ln.strip()
        if not ln or ln.startswith('#') or ln.startswith('|---') or ln.startswith('>'): continue
        if ln.startswith('|'):
            cells = [c.strip() for c in ln.strip('|').split('|')]
            ln = max(cells, key=len)
        ln = re.sub(r'\[[^\]]*\]', '', ln); ln = re.sub(r'`[^`]*`', '', ln); ln = re.sub(r'^\S*\d+\.\d+\s*', '', ln)
        ln = re.sub(r'\*\*|__', '', ln).lstrip('- ').strip()
        if len(ln.split()) >= 3: lines.append(ln)
    return ' '.join(lines)
os.makedirs(DEST, exist_ok=True)
jobs = [('cand', 'T')] * 5 + [('cand', 'G')] + [('weak', 'T')] * 3
random.SystemRandom().shuffle(jobs)
key = {'_': 'GIẢI MÃ — chỉ mở sau khi chấm.', 'items': {}}
T = {'cand': cand(), 'weak': weak()}
for s, r in jobs:
    h = secrets.token_hex(4); os.makedirs(f'{DEST}/{h}')
    open(f'{DEST}/{h}/{h}.txt', 'w').write(T[s] + '\n'); key['items'][h] = {'sample': s, 'role': r}
open(f'{EP}/review-c2/transcript.txt', 'w').write(T['cand'] + '\n')
open(f'{EP}/review-c2/weak-control.txt', 'w').write(T['weak'] + '\n')
json.dump(key, open(f'{EP}/review-c2/key.json', 'w'), indent=1)
print({k: len(v.split()) for k, v in T.items()}); print(json.dumps(key['items']))

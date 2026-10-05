"""Chia mẫu mù: degr-*.raw.txt → degr-*.txt (id D.n + mốc ước theo wpm của tập); mỗi mẫu một file tên hex trong scratch; khoá ở key.json (commit trước khi chấm)."""
import json, os, random, secrets, sys
R = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
WPM = {'ep002': 129, 'ep003': 145}
def mmss(t): return f'{int(t // 60)}:{int(t % 60):02d}'
def lines(path): return [l.rstrip('\n') for l in open(path) if l.strip()]
for ep in WPM:
    raw = lines(f'{R}/degr-{ep}.raw.txt'); t = 0; out = []
    for i, s in enumerate(raw, 1):
        out.append(f'D.{i} [{mmss(t)}] {s}'); t += len(s.split()) / WPM[ep] * 60 + 0.8
    open(f'{R}/degr-{ep}.txt', 'w').write('\n'.join(out) + '\n')
FULL = open(f'{R}/reader-full.txt').read(); PAIR = open(f'{R}/reader-pair.txt').read()
def first30(path): return '\n'.join(l for l in lines(path) if int(l.split('[')[1].split(':')[0]) * 60 + int(l.split(':')[1][:2]) < 30)
random.seed(20261005); key = []
for ep in WPM:
    for ver in ['orig', 'degr']:
        for r in range(3):
            h = secrets.token_hex(4); open(f'{OUT}/{h}.txt', 'w').write(FULL + '\n\n' + open(f'{R}/{ver}-{ep}.txt').read())
            key.append({'file': h, 'kind': 'full', 'ep': ep, 'ver': ver})
    for r in range(3):
        xo = random.random() < 0.5; X, Y = (('orig', 'degr') if xo else ('degr', 'orig'))
        h = secrets.token_hex(4)
        open(f'{OUT}/{h}.txt', 'w').write(PAIR + '\n\n=== OPENING X ===\n' + first30(f'{R}/{X}-{ep}.txt') + '\n\n=== OPENING Y ===\n' + first30(f'{R}/{Y}-{ep}.txt') + '\n')
        key.append({'file': h, 'kind': 'pair', 'ep': ep, 'X': X, 'Y': Y})
random.shuffle(key); json.dump(key, open(f'{R}/key.json', 'w'), indent=1); print(len(key), 'samples')

"""Chia mẫu hiệu chuẩn so cặp móc (INTENT.md): 2 mẫu × 4 người đọc, gốc ở X 2 lần / Y 2 lần.
(v2 sau REVIEWER: bỏ câu tiêu đề.) Mỗi người đọc một file tên hex trong OUT; khoá key.json."""
import json, os, re, secrets, sys, random
R = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
txt = open(f'{R}/samples.md').read()
def sec(h): return re.search(rf'### {h}[^\n]*\n(.*?)\n(?=#|\Z)', txt, re.S).group(1).strip()
ROLE = {'A': 'You are a US homeowner aged 30-55 who is paying a mortgage', 'B': 'You are a US hourly worker aged 25-50'}
T = dict(re.findall(r'- (T\d): (.*)', txt))
pairs = [('T1', 'T2'), ('T2', 'T1'), ('T1', 'T2'), ('T1', 'T3'), ('T3', 'T1'), ('T1', 'T3'), ('T2', 'T3'), ('T3', 'T2')]
rng = random.SystemRandom(); rng.shuffle(pairs)
slots = [(s, o) for s in 'AB' for o in ('X', 'X', 'Y', 'Y')]
key = []
for (s, o), tp in zip(slots, pairs):
    X, Y = (f'{s}-orig', f'{s}-degr') if o == 'X' else (f'{s}-degr', f'{s}-orig')
    h = secrets.token_hex(4)
    body = (f"{ROLE[s]}, scrolling YouTube for personal-finance videos. Below are the first ~30 seconds of narration of two versions "
            f"(X and Y) of the same faceless data-explainer video. Read both once.\n\n=== OPENING X ===\n{sec(X)}\n\n=== OPENING Y ===\n{sec(Y)}\n\n"
            "Answer in EXACTLY this format, nothing else:\nKEEP: <X or Y> (which opening would make you keep watching?)\n"
            "STRENGTH: <1-3> (1 = slight, 3 = clear)\nWHY: <one sentence>\n")
    open(f'{OUT}/{h}.txt', 'w').write(body)
    key.append({'file': h, 'sample': s, 'X': X, 'Y': Y})
rng.shuffle(key); json.dump(key, open(f'{R}/key.json', 'w'), indent=1); print(len(key), 'mẫu')

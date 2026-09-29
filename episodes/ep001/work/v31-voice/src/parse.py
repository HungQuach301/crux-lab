"""Tập 1 · lời đọc v3.1: tách câu từ story/script-v3.1.md, chuẩn hoá sang chữ đọc như C2.
Không gửi gì. In ra rows (JSON) cho gen.py."""
import json, os, re, subprocess
ROOT = '/home/user/crux-lab'
EP = f'{ROOT}/episodes/ep001'
SKIP = ('#', '*Hình:*', '*Ghi chú:*', '*Câu hỏi', '---', '>', '**—', '|', '*Thẻ')
PAUSE = {'first': 0.0, 'same': 0.45, 'beat': 1.0, 'scene': 1.4, 'sequence': 2.0}
ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
ORD = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth',
       13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth', 30: 'thirtieth'}
TENS = {2: 'twenty', 3: 'thirty'}
MONTHS = 'January February March April May June July August September October November December'.split()


def ordinal(d):
    if d in ORD: return ORD[d]
    return TENS[d // 10] + '-' + ORD[d % 10]


def parse(path=f'{EP}/story/script-v3.1.md'):
    rows, seq, scene, pend = [], None, None, None
    started = False
    for line in open(path, encoding='utf-8'):
        s = line.strip()
        m = re.match(r'^## SEQUENCE (\d+)', s)
        if m:
            seq = int(m.group(1)); started = True; pend = 'sequence' if rows else 'first'; continue
        if not started: continue
        if s.startswith('**— thẻ phương pháp'): break
        m = re.match(r'^### (S\d\d)', s)
        if m:
            scene = m.group(1)
            if pend != 'sequence' and rows: pend = 'scene'
            if not rows: pend = 'first'
            continue
        if not s or s.startswith(SKIP): continue
        if s == '[beat]':
            pend = 'beat'; continue
        plain = re.sub(r'\s*\[[A-Za-z0-9_]+\]', '', s).strip()
        for k, sent in enumerate(re.split(r'(?<=[.?!])\s+(?=[A-Z$])', plain)):
            p = pend if k == 0 and pend else 'same'
            rows.append({'sequence': seq, 'scene': scene, 'script_line': s, 'text_plain': sent, 'pause_kind': p, 'pause_before_s': PAUSE[p]})
            pend = None
    return rows


def to_tts(texts):
    pre = []
    for t in texts:
        t = re.sub(r'\b(' + '|'.join(MONTHS) + r') (\d{1,2}),', lambda m: f'{m.group(1)} {ordinal(int(m.group(2)))},', t)
        pre.append(t)
    js = "const n=require('%s/toolkit/voice/normalize.js');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(a.map(x=>n.toSpoken(x))))" % ROOT
    out = json.loads(subprocess.run(['node', '-e', js], input=json.dumps(pre), capture_output=True, text=True, check=True).stdout)
    res = []
    for t in out:
        t = re.sub(r'dollars (loan|bill)\b', r'dollar \1', t)
        res.append(t[:1].upper() + t[1:])
    return res


if __name__ == '__main__':
    rows = parse()
    for r, t in zip(rows, to_tts([r['text_plain'] for r in rows])): r['tts_text'] = t
    c2 = json.load(open(f'{EP}/review-c2/table-read.json'))['rows']
    c2map = {r['tts_text']: r for r in c2}
    for i, r in enumerate(rows):
        r['n'] = i + 1
        m = c2map.get(r['tts_text'])
        r['reuse_c2'] = {'n': m['n'], 'take_file': m['take_file'], 'seed': m['seed']} if m else None
        print(r['n'], r['scene'], r['pause_before_s'], 'R' if m else '-', r['tts_text'])
    json.dump(rows, open('/tmp/claude-0/-home-user-crux-lab/7328d23d-30a0-526e-bd92-001685250b0f/scratchpad/rows.json', 'w'), indent=1)
    print(len(rows), 'reuse', sum(1 for r in rows if r['reuse_c2']), 'new chars', sum(len(r['tts_text']) for r in rows if not r['reuse_c2']))

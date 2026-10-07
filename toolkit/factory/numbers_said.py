"""Mốc V · B+2 — luật "≤ 2 số MỚI được NÓI mỗi cảnh" (spine/spec). Số thứ ba trở đi chuyển thành NHÃN trên hình.
  python3 toolkit/factory/numbers_said.py <script.md|script.json> [--max 2]
- "Số" = một lượng CÓ ĐƠN VỊ trong lời đã chuẩn hoá (toolkit/voice/normalize.js toSpoken): percent, year(s), month(s), dollar(s),
  times, quarter … (số đếm không đơn vị như "three illustrative buyers" không tính; năm lịch như "two thousand" không tính).
- "Mới" = cặp (giá trị, đơn vị) chưa được nói ở câu nào trước đó trong tập.
- spec.py gọi `check_scenes()` → BLOCK 'spoken_numbers' khi một cảnh vượt ngưỡng; thông báo nêu số thứ ba để chuyển thành nhãn.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)

LEGACY = {'ep003'}   # đã phát hành trước B+2 → spec.py hạ BLOCK thành WARN (Tập 4 đã đạt sẵn)
UNITS = r'(percent|years?|months?|dollars?|times|quarters?|points?|basis points)'
NUMW = (r'(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|'
        r'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|point|and|a|half|\d[\d,.]*)')
PAT = re.compile(r'\b((?:' + NUMW + r')(?:[\s-]+' + NUMW + r')*)\s+' + UNITS + r'\b', re.I)


def numbers_in(spoken):
    out = []
    for m in PAT.finditer(spoken):
        val = re.sub(r'^(?:(?:a|and)\s+)+', '', m.group(1).strip().lower())
        if not re.search(r'\d|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|teen|ty|hundred|thousand|million|half', val):
            continue
        unit = re.sub(r's$', '', m.group(2).lower())
        out.append({'text': f'{val} {m.group(2).lower()}', 'value': val, 'unit': unit})
    return out


def check_scenes(sentences, spoken, limit=2):
    """sentences: [{id, scene}] in order; spoken: same order (normalised text). → (per-scene report, problems)"""
    said, rep, P = set(), {}, []
    for s, sp in zip(sentences, spoken):
        r = rep.setdefault(s['scene'], {'new': [], 'repeat': []})
        for n in numbers_in(sp):
            k = (n['value'], n['unit'])
            (r['repeat'] if k in said else r['new']).append({**n, 'sid': s['id']})
            said.add(k)
    for sc, r in rep.items():
        if len(r['new']) > limit:
            allnew = ', '.join(f"\"{n['text']}\" ({n['sid']})" for n in r['new'])
            P.append({'level': 'BLOCK', 'rule': 'spoken_numbers',
                      'msg': f"{sc}: {len(r['new'])} new spoken numbers > {limit} [{allnew}]; keep {limit} in the line, move the rest to on-screen labels (editor picks which), scope unchanged"})
    return rep, P


def load(path):
    if path.endswith('.json'):
        return json.load(open(path))['sentences']
    LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
    return [{'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip()}
            for m in (LINE.match(ln) for ln in open(path, encoding='utf-8')) if m]


def main():
    sents = load(sys.argv[1]); limit = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 2
    import voice as V
    TAG = re.compile(r'^\[[a-z ]+\]\s+')
    spoken = V.to_spoken([TAG.sub('', s['text']) for s in sents])
    rep, P = check_scenes(sents, spoken, limit)
    for sc, r in rep.items():
        if r['new'] or r['repeat']:
            print(sc, 'new:', [n['text'] for n in r['new']], '| repeat:', [n['text'] for n in r['repeat']])
    for p in P: print(p['level'], p['msg'])
    sys.exit(1 if P else 0)


if __name__ == '__main__':
    main()

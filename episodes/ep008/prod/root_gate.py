"""Tập 8 · cổng gốc TẮT TIẾNG trên animatic xám / nháp (mô hình xưởng M2 Previz, M5) — ý đồ `gates/M2-root-intent.md` (ghi trước khi chạy).
Chép rút gọn từ episodes/ep007/c4/blind_c4.py (phần A). Chạy từ gốc tập (episodes/ep008), khoá Console (headless.sh).
  python3 prod/root_gate.py strips <video> <run>          # review-m2/<run>/strips/<Bxx>.png (6 khung đều trong cảnh ±0,2 s, tắt tiếng)
  python3 prod/root_gate.py read <run> [--slots 1,2] [--only B07,B24]
  python3 prod/root_gate.py pack <run>   ·   grade <run> [--graders 2]   ·   tally <run>
Gộp THẬN TRỌNG (chủ dự án 13/10): 2 người chấm độc lập; điểm của người đọc = điểm thấp nhất; cờ khuyên bật nếu bất kỳ người chấm nào bật."""
import argparse, json, re, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]; ROOT = EP.parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
sys.path.insert(0, str(ROOT / 'toolkit' / 'blind')); import packets  # noqa: E402
T = ("You are an American renter in 2026. You have saved enough for a 20% down payment on a home near the national median price, and you came "
     "wondering: once you count interest, property tax, insurance and repairs, does renting actually cost more than buying?")
Q = ("Answer in plain sentences:\n1. What idea is this showing?\n2. What changes over time?\n3. What does it mean?\n"
     "4. What advice, if any, would a viewer take from this?\n"
     "5. Did the animation itself (picture or on-screen text) suggest this, or is it your own conclusion? If you gave no advice in 4, answer 'none'.\n")
QUESTION_ID = 'M2 Tập 8: vai T + câu 1–5 (gates/M2-root-intent.md)'


def beats():
    out = {}
    for ln in open(EP / 'story/beats.md', encoding='utf-8'):
        m = re.match(r'^\| (B\d\d) \| (S\d\d) \| (\d) \|', ln)
        if m:
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            out[m[1]] = {'scene': m[2], 'type': m[3], 'muted_read': c[12].strip('"“” ')}
    return out


IMAGE = [b for b, v in beats().items() if v['type'] == '1']


def tl():
    return json.load(open(EP / 'out/factory/timeline.json'))


def rdir(run):
    return (EP / 'review-m2' / run).resolve()


def keydir(run):
    d = (EP / 'review-m2' / (run + '.key')).resolve(); d.mkdir(parents=True, exist_ok=True); return d


def do_strips(video, run):
    sc = {s['id']: s for s in tl()['scenes']}; bt = beats(); o = rdir(run); o.mkdir(parents=True, exist_ok=True)
    spans = {b: [round(sc[bt[b]['scene']]['start'] + 0.2, 3), round(sc[bt[b]['scene']]['start'] + sc[bt[b]['scene']]['dur'] - 0.2, 3)] for b in IMAGE}
    json.dump({'video': str(video), 'spans': spans, 'muted_read': {b: bt[b]['muted_read'] for b in IMAGE}}, open(o / 'spans.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(spans, open(o / 'spans-flat.json', 'w'))
    subprocess.run([sys.executable, str(ROOT / 'toolkit/blind/strips.py'), str(video), str(o / 'spans-flat.json'), str(o / 'strips')], check=True)
    print(len(spans), 'dải', o / 'strips')


def do_read(run, slots, only):
    o = rdir(run); rd = o / 'readers'; rd.mkdir(exist_ok=True); kd = keydir(run); kp = kd / 'KEY.json'
    key = json.load(open(kp)) if kp.exists() else {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': QUESTION_ID, 'candidate_set': 'ep008', 'items': {}}
    taken = {(v['id'], v['slot']) for v in key['items'].values()}; jobs = []
    for b in IMAGE:
        if only and b not in only: continue
        for k in slots:
            if (b, k) in taken: sys.exit(f'đã chia {b} cho người đọc {k}')
            h = secrets.token_hex(4); dst = rd / f'{h}-1.png'; dst.write_bytes((o / 'strips' / f'{b}.png').read_bytes())
            (rd / f'{h}.txt').write_text(f'{T}\n\nUse the Read tool to open exactly this one file and nothing else: {dst}\nThe image shows six numbered frames, in order, '
                                         f'taken from a short silent animation in a personal-finance video. Look only at the image.\n{Q}')
            key['items'][h] = {'id': b, 'set': 'ep008', 'kind': 'image', 'slot': k, 'sha256': packets._sha(rd / f'{h}.txt')}; jobs.append(h)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(rd / f'{h}.txt', rd / f'{h}.json', read=True), jobs)))
    json.dump(key, open(kp, 'w'), indent=1, ensure_ascii=False)
    ans = json.load(open(kd / 'answers.json')) if (kd / 'answers.json').exists() else {}
    ans.update({h: r['answer'] for h, r in res.items() if r}); json.dump(ans, open(kd / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({'runs': len(jobs), 'ok': sum(1 for r in res.values() if r), 'failed': [h for h in jobs if not res[h]]}))


def rubric():
    bt = beats()
    rules = ('Score the MEANING against the expected reading (1 = the idea is there; 0.5 = part of it; 0 = only shapes/colours/labels or a different idea). '
             'Advice flags: advice_stated = the reader says the ANIMATION itself (picture or on-screen text) states or implies a financial action: buy, keep '
             'renting, buy now / before something, wait, hold N years, invest, pick a month. advice_inferred = the reader drew that action themself (answer 5 '
             'says own conclusion or none). caution_only = general care only (check your own numbers, ask an adviser). Quote the reader verbatim for any '
             'flag. Also return "q5": "video" | "own" | "none".')
    return {'rules': rules, 'items': {b: {'meaning': bt[b]['muted_read'], 'description_only': 'lists shapes, colours, numbers or labels without the idea above'} for b in IMAGE}}


def do_pack(run):
    o = rdir(run); kd = keydir(run)
    json.dump(rubric(), open(o / 'rubric.json', 'w'), indent=1, ensure_ascii=False)
    labs = packets.packet(str(kd / 'KEY.json'), str(kd / 'answers.json'), str(o / 'rubric.json'), str(o / 'packet.json'), str(o / 'rubric-key.json'))
    print(len(labs), 'nhãn')


def do_grade(run, n):
    o = rdir(run); pk = json.load(open(o / 'packet.json'))
    body = ('# Grading packet (blind). You are an independent grader. Each label Rxx is one reader\'s answers about a short silent animation from a '
            'personal-finance video. Grade each label literally with the rules and the expected meaning given for it. You know nothing else.\n\n'
            + json.dumps(pk, indent=1, ensure_ascii=False) + '\n\nOutput JSON only (no prose, no code fence), one entry per label: ' + pk['return'] + ' — and add "q5".\n')
    (o / 'grade-prompt.txt').write_text(body)

    def one(k):
        r = blind.run(o / 'grade-prompt.txt', o / f'grade-g{k}.json')
        txt, dec, objs, i = r['answer'], json.JSONDecoder(), [], 0
        while (j := txt.find('{', i)) >= 0:
            try: ob, e = dec.raw_decode(txt[j:]); objs.append(ob); i = j + e
            except ValueError: i = j + 1
        json.dump({kk: v for kk, v in objs[-1].items() if isinstance(v, dict)}, open(o / f'scores-g{k}.json', 'w'), indent=1, ensure_ascii=False)
        return k
    with cf.ThreadPoolExecutor(n) as ex: print(list(ex.map(one, range(1, n + 1))))


def do_tally(run):
    o = rdir(run); kd = keydir(run)
    sc = sorted(str(p) for p in o.glob('scores-g*.json'))
    res = packets.tally(str(kd / 'KEY.json'), str(o / 'rubric-key.json'), sc, threshold=0.8)
    json.dump(res, open(o / 'tally.json', 'w'), indent=1, ensure_ascii=False)
    md = packets.markdown(res); (o / 'tally.md').write_text(md); print(md)


if __name__ == '__main__':
    a = sys.argv[1:]
    sl = [int(x) for x in a[a.index('--slots') + 1].split(',')] if '--slots' in a else [1, 2]
    on = a[a.index('--only') + 1].split(',') if '--only' in a else None
    {'strips': lambda: do_strips(a[1], a[2]), 'read': lambda: do_read(a[1], sl, on), 'pack': lambda: do_pack(a[1]),
     'grade': lambda: do_grade(a[1], int(a[a.index('--graders') + 1]) if '--graders' in a else 2), 'tally': lambda: do_tally(a[1])}[a[0]]()

"""K4.4 · A32 — hiệu chuẩn cổng gốc: đo biên nhiễu bằng ≥ 3 lượt đọc lại master bản giao Tập 6 (f96da0ea…), đối chứng dương (đảo thứ tự khung).
Ngưỡng ghi trước ở PREREG.md (commit trước lượt đọc đầu). Dùng lại vai, câu hỏi, rubric mới của episodes/ep006/c4/blind_c4.py và lời dẫn ảnh của
toolkit/factory/f14/root_v4.py (chỉ đọc, không sửa). Người đọc/người chấm headless (toolkit/blind/headless.sh, sonnet) chi bằng khoá Console.
Chạy từ gốc repo, với ANTHROPIC_API_KEY="$CONSOLE_API_KEY":
  python3 checks-runs/K44/a32/a32.py strips                 # strips-ctl (23 nhịp) + strips-pos (B01, B10, B24 đảo thứ tự 6 khung)
  python3 checks-runs/K44/a32/a32.py pass <pN> [--pos]      # đọc 2 người/nhịp → chấm → người thứ 3 khi tách đôi → chấm lại toàn gói → tally
  python3 checks-runs/K44/a32/a32.py report                 # bảng phân bố, nhịp lật, luật cũ/mới trên đối chứng âm và dương → result.json
"""
import json, os, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
ROOT = Path.cwd()
EP = ROOT / 'episodes/ep006'
OUT = ROOT / 'checks-runs/K44/a32'
sys.path.insert(0, str(EP / 'c4')); sys.path.insert(0, str(EP)); sys.path.insert(0, str(ROOT / 'toolkit/blind'))
import blind_c4 as BC  # noqa: E402
import blind  # noqa: E402
import packets  # noqa: E402

PROMPT = 'The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image.'
POS = ['B01', 'B10', 'B24']   # nghĩa nằm ở chiều thời gian (tắt dần / tụt xuống / mờ dần): đảo thứ tự khung = nghĩa ngược
MASTER = EP / 'out/video.mp4'
MASTER_SHA = 'f96da0ea19e6426aa3b4bd37759f3e7c8fb9819e489a1fab317683fd5edcaa74'
TW, TH, GAP, LAB = 624, 351, 12, 50


def strips():
    tl, bt = BC.timeline(), BC.beats()
    sc = {s['id']: s for s in tl['scenes']}
    spans = {b: [round(sc[bt[b]['scene']]['start'] + 0.2, 3), round(sc[bt[b]['scene']]['end'] - 0.2, 3)] for b in BC.IMAGE}
    json.dump(spans, open(OUT / 'spans.json', 'w'), indent=1)
    subprocess.run([sys.executable, str(ROOT / 'toolkit/blind/strips.py'), str(MASTER), str(OUT / 'spans.json'), str(OUT / 'strips-ctl')], check=True)
    from PIL import Image
    (OUT / 'strips-pos').mkdir(exist_ok=True)
    cw, ch = TW + GAP, TH + LAB + GAP
    for b in POS:
        im = Image.open(OUT / 'strips-ctl' / f'{b}.png').convert('RGB')
        new = im.copy()
        boxes = [((i % 3) * cw + GAP, (i // 3) * ch + GAP) for i in range(6)]
        tiles = [im.crop((x, y, x + TW, y + TH)) for x, y in boxes]   # chỉ ô hình; dải số 1–6 giữ nguyên
        for (x, y), t in zip(boxes, reversed(tiles)):
            new.paste(t, (x, y))
        new.save(OUT / 'strips-pos' / f'{b}.png')
    print('strips', OUT)


def _read(o, key, jobs_spec):
    jobs = []
    for st, b, k in jobs_spec:
        h = secrets.token_hex(4)
        dst = o / f'{h}-1.png'; dst.write_bytes((OUT / f'strips-{st}' / f'{b}.png').read_bytes())
        (o / f'{h}.txt').write_text(f'{BC.T}\n\nUse the Read tool to open exactly this one file and nothing else: {dst}\n{PROMPT}\n{BC.QS["root"]}')
        key['items'][h] = {'id': b, 'set': st, 'kind': 'image', 'slot': k, 'sha256': packets._sha(o / f'{h}.txt')}
        jobs.append(h)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(o / f'{h}.txt', o / f'{h}.json', read=True), jobs)))
    json.dump(key, open(o / 'KEY.json', 'w'), indent=1, ensure_ascii=False)
    ans = json.load(open(o / 'answers.json')) if (o / 'answers.json').exists() else {}
    ans.update({h: r['answer'] for h, r in res.items() if r})
    json.dump(ans, open(o / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    cost = sum((r.get('cost_usd') or 0) for r in res.values() if r)
    print(json.dumps({'runs': len(jobs), 'ok': sum(1 for r in res.values() if r), 'cost_usd': round(cost, 3)}))
    return cost


def _pack_grade(o):
    rub = BC.rubric()
    rub['items'].update({f'ctrl:{b}': rub['items'][b] for b in BC.IMAGE})
    json.dump(rub, open(o / 'rubric.json', 'w'), indent=1, ensure_ascii=False)
    for f in ('rubric-key.json', 'packet.json'):
        (o / f).unlink(missing_ok=True)
    packets.packet(str(o / 'KEY.json'), str(o / 'answers.json'), str(o / 'rubric.json'), str(o / 'packet.json'), str(o / 'rubric-key.json'))
    BC.do_grade(os.path.relpath(o, EP), 2)
    return sum((json.load(open(o / f'grade-g{k}.json')).get('cost_usd') or 0) for k in (1, 2))


def _tally(o, st):
    key, rk = packets._load(str(o / 'KEY.json')), packets._load(str(o / 'rubric-key.json'))
    scs = [packets._load(str(p)) for p in sorted(o.glob('scores-g*.json'))]
    return packets._tally_one(dict(key, candidate_set=st), rk, scs, 0.8, None, 'new')


def run_pass(name, pos):
    o = OUT / name; o.mkdir(parents=True, exist_ok=True)
    key = {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': BC.QUESTION_ID, 'candidate_set': 'ctl', 'items': {},
           'master_sha256': MASTER_SHA}
    cost = _read(o, key, [('ctl', b, k) for b in BC.IMAGE for k in (1, 2)] + ([('pos', b, k) for b in POS for k in (1, 2)] if pos else []))
    cost += _pack_grade(o)
    third = [(st, r['id']) for st in (['ctl', 'pos'] if pos else ['ctl']) for r in _tally(o, st)['rows'] if r['set'] == st and r['status'] == 'NEED_3RD']
    if third:
        cost += _read(o, key, [(st, b, 3) for st, b in third])
        cost += _pack_grade(o)
    res = {st: _tally(o, st) for st in (['ctl', 'pos'] if pos else ['ctl'])}
    res['cost_usd'] = round(cost, 3); res['third_reader'] = third
    json.dump(res, open(o / 'tally.json', 'w'), indent=1, ensure_ascii=False)
    for st in res:
        if isinstance(res[st], dict) and 'rows' in res[st]:
            rows = [r for r in res[st]['rows'] if r['set'] == st]
            print(st, f"PASS {sum(r['status'] == 'PASS' for r in rows)}/{len(rows)}", 'advice', res[st]['advice_beats'], 'cost', res['cost_usd'])


def report():
    passes = sorted(p.name for p in OUT.glob('p[0-9]') if (p / 'tally.json').exists())
    st = {}
    for p in passes:
        t = json.load(open(OUT / p / 'tally.json'))
        st[p] = {r['id']: r['status'] for r in t['ctl']['rows'] if r['set'] == 'ctl'}
        if 'pos' in t:
            st[p + '+pos'] = dict(st[p], **{r['id']: r['status'] for r in t['pos']['rows'] if r['set'] == 'pos'})
    n = {p: sum(v == 'PASS' for v in s.values()) for p, s in st.items()}
    ctl = [p for p in passes]
    floor = min(n[p] for p in ctl) - 1 if ctl else None
    drop = lambda c, x: [b for b in BC.IMAGE if st[c].get(b) == 'PASS' and st[x].get(b) != 'PASS']
    neg = [{'control': c, 'candidate': x, 'drops': drop(c, x), 'new_rule': 'TRƯỢT' if len(drop(c, x)) >= 2 or n[x] < floor else
            ('XÁC NHẬN 1 nhịp' if len(drop(c, x)) == 1 else 'ĐẠT'),
            'old_rule': 'ĐẠT' if n[x] >= 20 and not drop(c, x) else 'TRƯỢT'} for c in ctl for x in ctl if c != x]
    pos = [{'control': p, 'candidate': p + '+pos', 'drops': drop(p, p + '+pos'),
            'new_rule': 'TRƯỢT' if len(drop(p, p + '+pos')) >= 2 or n[p + '+pos'] < floor else 'ĐẠT'} for p in ctl if p + '+pos' in st]
    flips = {b: [st[p].get(b) for p in ctl] for b in BC.IMAGE if len({st[p].get(b) for p in ctl}) > 1}
    cost = sum(json.load(open(OUT / p / 'tally.json')).get('cost_usd', 0) for p in passes)
    res = {'passes': {p: n[p] for p in ctl}, 'pos': {p: n[p] for p in st if p.endswith('+pos')}, 'floor': floor, 'flips': flips,
           'negative': neg, 'positive': pos, 'cost_usd': round(cost, 3), 'status': st}
    json.dump(res, open(OUT / 'result.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k != 'status'}, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'strips': strips()
    elif c == 'pass': run_pass(sys.argv[2], '--pos' in sys.argv)
    elif c == 'report': report()

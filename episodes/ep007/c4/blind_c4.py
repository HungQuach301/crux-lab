"""Tập 7 · C4 kiểm mù theo gates/C4-intent.md (A cổng gốc tắt tiếng · B bản có lời cả tập · C bản có lời S21, S23–S24, S25). Chép Tập 6.
  python3 c4/blind_c4.py strips <video> [--tag r1]          # review-c4/spans.json + review-c4/strips/<id>.png (+ 4 tấm cả tập)
  python3 c4/blind_c4.py read <run> <set> [--slots 1,2] [--only B07,B24]   # set: root | voiced (B + C); người đọc headless mới mỗi lượt
  python3 c4/blind_c4.py pack <run>                         # gói chấm (packets.py packet) + khoá nhãn → COMMIT trước khi chấm
  python3 c4/blind_c4.py grade <run> [--graders 2]          # 2 người chấm headless độc lập trên cùng gói → scores-g<k>.json
  python3 c4/blind_c4.py tally <run>                        # packets.py tally hai người chấm, hai rubric → tally.json / tally.md
<run> = c4/<tên lượt> (vd c4/root-r1, c4/voiced-r1). Chạy từ gốc tập (episodes/ep007)."""
import argparse, json, os, re, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]
ROOT = EP.parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
sys.path.insert(0, str(ROOT / 'toolkit' / 'blind')); import packets  # noqa: E402
REV = EP / 'review-c4'
T = ("You are an American buying a home in an expensive city, with a mortgage of about $320,000 and a large monthly payment. You can just afford a "
     "15-year payment, and you came wondering: should you pay extra on a mortgage, or invest the spare cash instead?")
Q14 = ("Answer in plain sentences:\n1. What idea is this showing?\n2. What changes over time?\n3. What does it mean?\n"
       "4. What advice, if any, would a viewer take from this?\n")
QS = {'root': Q14 + "5. Did the animation itself (picture or on-screen text) suggest this, or is it your own conclusion? If you gave no advice in 4, answer 'none'.\n",
      'voiced': Q14 + "5. Did the video itself (picture, on-screen text or narration) suggest this, or is it your own conclusion? If you gave no advice in 4, answer 'none'.\n"}
QUESTION_ID = 'C4 Tập 7: vai T + câu 1–5 (gates/C4-intent.md)'
IMAGE = ['B01', 'B04', 'B05', 'B06', 'B08', 'B09', 'B10', 'B11', 'B13', 'B15', 'B18', 'B19', 'B21', 'B22', 'B23', 'B25', 'B28', 'B29', 'B30', 'B31', 'B33']
EXTRA = ('Also return "extra_layer_seen": true if the reader describes something EXTRA being added on top of each month\'s payment (a slab, layer, '
         'top-up or additional payment placed on the monthly tiles), false if they only describe blocks, colours or a grid changing.')
BEAT = ('Also return "must_beat_or_guaranteed": true if the reader says the video tells them that any other use of the money HAS TO BEAT / must clear '
        'the 7.40% rate, or that paying extra is a guaranteed / sure / risk-free saving or return; quote it. False otherwise.')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{\w+\}\s+)?(?:\[[a-z ]+\]\s+)?(.+?)\s*<!--')


def beats():
    """{B07: {scene: S07, muted_read: "..."}} từ bảng nhịp (cột 'muted read' chép nguyên văn)."""
    out = {}
    for ln in open(EP / 'story/beats.md', encoding='utf-8'):
        if not ln.startswith('| B'):
            continue
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        bid = re.match(r'(B\d\d)', c[0])[1]
        out[bid] = {'scene': c[1], 'type': c[4], 'muted_read': c[5].strip('"“” ')}
    return out


def narration(scenes):
    out = []
    for ln in open(EP / 'story/script.md', encoding='utf-8'):
        m = LINE.match(ln)
        if m and m[1] in scenes:
            out.append(m[3].strip())
    return '\n'.join(out)


def srt_cues():
    out = []
    for blk in (EP / 'out/captions.srt').read_text().strip().split('\n\n'):
        ln = blk.strip().split('\n')
        a, b = ln[1].split(' --> ')
        sec = lambda x: int(x[:2]) * 3600 + int(x[3:5]) * 60 + float(x[6:].replace(',', '.'))
        out.append((sec(a), sec(b), ' '.join(ln[2:])))
    return out


def heard(scene_ids):
    """Lời như người xem nghe: phụ đề có tâm nằm trong khoảng giờ các cảnh (REVIEWER PHỤ-9)."""
    sc = [s for s in timeline()['scenes'] if s['id'] in scene_ids]
    return '\n'.join(t for a, b, t in srt_cues() if any(s['start'] <= (a + b) / 2 < s['end'] for s in sc))


def timeline():
    return json.load(open(EP / 'out/timeline.json'))


def sheet(video, times, out, cols=4):
    """Tấm ảnh nhiều khung đánh số theo thứ tự giờ (bản có lời cả tập: 12 khung/hồi)."""
    tmp = Path(out).with_suffix('')
    tmp.mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(times):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.3f}', '-i', str(video), '-frames:v', '1', '-vf',
                        f"scale=480:270,drawtext=text='{i + 1}':x=8:y=8:fontsize=28:fontcolor=white:box=1:boxcolor=black@0.6",
                        str(tmp / f'{i:02d}.png')], check=True)
    rows = (len(times) + cols - 1) // cols
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(tmp / '%02d.png'), '-vf', f'tile={cols}x{rows}:padding=6:color=0x06080B',
                    '-frames:v', '1', str(out)], check=True)


def do_strips(video, tag):
    tl, bt = timeline(), beats()
    sc = {s['id']: s for s in tl['scenes']}
    REV.mkdir(exist_ok=True)
    spans, meta = {}, {}
    for b in IMAGE:
        s = sc[bt[b]['scene']]
        spans[b] = [round(s['start'] + 0.2, 3), round(s['end'] - 0.2, 3)]
        meta[b] = {'scene': bt[b]['scene'], 'muted_read': bt[b]['muted_read'], 'span': spans[b]}
    json.dump({'video': str(video), 'tag': tag, 'strips': meta}, open(REV / 'spans.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(spans, open(REV / 'spans-flat.json', 'w'))
    subprocess.run([sys.executable, str(ROOT / 'toolkit/blind/strips.py'), str(video), str(REV / 'spans-flat.json'), str(REV / 'strips')], check=True)
    # B: 4 tấm theo hồi (12 khung đều mỗi tấm)
    groups = [('sheet1', ['cold-open', 'ident', 'act1']), ('sheet2', ['act2']), ('sheet3', ['act3']), ('sheet4', ['method', 'outro'])]
    acts = {}
    for s in tl['scenes']:
        acts.setdefault(s.get('act'), []).append(s)
    used = set()
    for name, ids in groups:
        ss = [s for a in ids for s in acts.get(a, []) if s['id'] not in used]
        if not ss:
            continue
        used |= {s['id'] for s in ss}
        t0, t1 = min(s['start'] for s in ss), max(s['end'] for s in ss)
        sheet(video, [t0 + (i + 0.5) * (t1 - t0) / 12 for i in range(12)], REV / f'{name}.png')
    left = [s for s in tl['scenes'] if s['id'] not in used]
    if left:
        sys.exit(f'cảnh không vào tấm nào (acts trong timeline khác dự kiến): {[s["id"] for s in left]}')
    print('strips + sheets', REV)


def samples(kind):
    """(id, set, kind, prompt-body, [files]) theo ý đồ."""
    bt = beats()
    if kind == 'root':
        return [(b, 'ep007', 'image', 'The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image.',
                 [REV / 'strips' / f'{b}.png']) for b in IMAGE]
    srt = (EP / 'out/captions.srt').read_text()
    whole = ('The images show frames from a whole personal-finance video (about 10 minutes), in time order: sheet 1 is the opening and first part, '
             'sheet 2 the second part, sheet 3 the third part, sheet 4 the limits and ending. This is the full narration you hear, with times:\n---\n' + srt + '\n---')

    def voiced(prev, scenes, n):
        lead = 'The image shows' if n == 1 else f'The {n} images show, in order,'
        return (f'{lead} six numbered frames, in order, from a short animation in a personal-finance video. The line just before: "'
                + heard({prev}).split('\n')[-1] + '"\nThis is the narration you hear over these frames:\n---\n' + heard(set(scenes)) + '\n---')
    st = REV / 'strips'
    return [('WHOLE', 'ep007', 'voiced', whole, sorted(REV.glob('sheet?.png'))),
            ('S21', 'ep007', 'voiced', voiced('S20', ['S21'], 1), [st / 'B21.png']),
            ('S23-S24', 'ep007', 'voiced', voiced('S22', ['S23', 'S24'], 2), [st / 'B23.png', st / 'B24.png']),
            ('S25', 'ep007', 'voiced', voiced('S24', ['S25'], 1), [st / 'B25.png'])]


def do_read(run, kind, slots, only):
    o = (EP / run).resolve(); o.mkdir(parents=True, exist_ok=True)
    kp = o / 'KEY.json'
    key = json.load(open(kp)) if kp.exists() else {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': QUESTION_ID,
                                                    'candidate_set': 'ep007', 'items': {}}
    taken = {(v['set'], v['id'], v['slot']) for v in key['items'].values()}
    jobs = []
    for sid, st, kd, body, files in samples(kind):
        if only and sid not in only:
            continue
        for k in slots:
            if (st, sid, k) in taken:
                sys.exit(f'đã chia {sid} cho người đọc {k}')
            h = secrets.token_hex(4)
            fl = []
            for i, f in enumerate(files):
                dst = o / f'{h}-{i + 1}{Path(f).suffix}'
                dst.write_bytes(Path(f).read_bytes()); fl.append(str(dst))
            opn = ('Use the Read tool to open exactly ' + ('this one file' if len(fl) == 1 else f'these {len(fl)} files') + ' and nothing else: ' + ', '.join(fl))
            (o / f'{h}.txt').write_text(f'{T}\n\n{opn}\n{body}\n{QS["root" if kd == "image" else "voiced"]}')
            key['items'][h] = {'id': sid, 'set': st, 'kind': 'image' if kd == 'image' else 'voiced', 'slot': k, 'sha256': packets._sha(o / f'{h}.txt')}
            jobs.append(h)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(o / f'{h}.txt', o / f'{h}.json', read=True), jobs)))
    json.dump(key, open(kp, 'w'), indent=1, ensure_ascii=False)
    ans = json.load(open(o / 'answers.json')) if (o / 'answers.json').exists() else {}
    ans.update({h: r['answer'] for h, r in res.items() if r})
    json.dump(ans, open(o / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    tok = {h: sum(v['input'] + v['cache_write'] + v['output'] for v in r['tokens'].values()) for h, r in res.items() if r}
    print(json.dumps({'runs': len(jobs), 'ok': len(tok), 'trần': sum(tok.values()), 'failed': [h for h in jobs if not res[h]]}))


def rubric():
    bt = beats()
    rules = ('Score the MEANING against the expected reading. Advice flags (gates/C4-intent.md, new rubric): advice_stated = the reader says the VIDEO itself '
             '(picture, on-screen text or narration) states or implies a financial action: pick the 15-year or the 30-year, pay extra principal, invest '
             'instead, pay monthly rather than yearly (or the reverse), wait for or lock a rate, a rate forecast. advice_inferred = the reader drew that '
             'action themself (answer 5 says own conclusion, or says the video does not say it). caution_only = general care only (check your own numbers, '
             'ask the lender or an adviser, compare your loan rate with other uses of the money, know the price of the fallback) — not advice. Quote the '
             'reader verbatim for any flag. Also return "q5": "video" | "own" | "none" from the reader\'s answer 5. Some items ask for one more flag in '
             'their meaning text: return it for that item.')
    items = {b: {'meaning': bt[b]['muted_read'] + (' ' + EXTRA if b == 'B21' else ''), 'description_only': 'lists shapes, colours, numbers or labels without the idea above'} for b in IMAGE}
    c2 = (EP / 'c2/rubric-r3.md').read_text()
    whole = c2[c2.index('**Đúng câu hỏi**'):c2.index('**Câu khuyên')].strip()   # nguyên văn c2/rubric-r3.md
    items.update({'WHOLE': {'meaning': whole, 'description_only': 'retells scenes without the idea'},
                  'S21': {'meaning': bt['B21']['muted_read'] + ' ' + EXTRA, 'description_only': 'lists tiles and colours without the idea'},
                  'S23-S24': {'meaning': bt['B23']['muted_read'] + ' Then: paying yearly costs about $8,200 more interest, but the money waits in an account '
                              'in the meantime, and what it earns there is not counted — a cost of timing, not a verdict.', 'description_only': 'lists blocks without the idea'},
                  'S25': {'meaning': bt['B25']['muted_read'] + ' The bar is the loan rate, before taxes: interest no longer charged, not an investment return; '
                          'no investment is compared. ' + BEAT, 'description_only': 'describes the beam without the idea'}})
    return {'rules': rules, 'items': items}


def do_pack(run):
    o = (EP / run).resolve()
    json.dump(rubric(), open(o / 'rubric.json', 'w'), indent=1, ensure_ascii=False)
    labs = packets.packet(str(o / 'KEY.json'), str(o / 'answers.json'), str(o / 'rubric.json'), str(o / 'packet.json'), str(o / 'rubric-key.json'))
    print(len(labs), 'nhãn; commit packet.json + rubric-key.json + KEY.json trước khi chấm')


def do_grade(run, n):
    o = (EP / run).resolve()
    pk = json.load(open(o / 'packet.json'))
    body = ('# Grading packet (blind). You are an independent grader. Each label Rxx is one reader\'s answers about part of a personal-finance video. '
            'Grade each label literally with the rules and the expected meaning given for it. You know nothing else.\n\n'
            + json.dumps(pk, indent=1, ensure_ascii=False) + '\n\nOutput JSON only (no prose, no code fence), one entry per label: ' + pk['return'] + ' — and add "q5": "video" | "own" | "none" to every entry, plus any extra flag an item asks for.\n')
    (o / 'grade-prompt.txt').write_text(body)

    def one(k):
        r = blind.run(o / 'grade-prompt.txt', o / f'grade-g{k}.json')
        txt, dec, objs, i = r['answer'], json.JSONDecoder(), [], 0   # P3c: người chấm đôi khi in hai khối (bản sửa sau) → lấy khối JSON cuối
        while (j := txt.find('{', i)) >= 0:
            try:
                ob, e = dec.raw_decode(txt[j:]); objs.append(ob); i = j + e
            except ValueError:
                i = j + 1
        sc = {k: v for k, v in objs[-1].items() if isinstance(v, dict)}
        json.dump(sc, open(o / f'scores-g{k}.json', 'w'), indent=1, ensure_ascii=False)
        return k, sum(v['input'] + v['cache_write'] + v['output'] for v in r['tokens'].values())
    with cf.ThreadPoolExecutor(n) as ex:
        print(dict(ex.map(one, range(1, n + 1))))


def do_tally(run):
    o = (EP / run).resolve()
    sc = sorted(str(p) for p in o.glob('scores-g*.json'))
    key, rk = packets._load(str(o / 'KEY.json')), packets._load(str(o / 'rubric-key.json'))
    if any(v['kind'] == 'image' for v in key['items'].values()):
        res = packets.tally(str(o / 'KEY.json'), str(o / 'rubric-key.json'), sc, threshold=0.8)
        json.dump(res, open(o / 'tally.json', 'w'), indent=1, ensure_ascii=False)
        (o / 'tally.md').write_text(packets.markdown(res))
        print(packets.markdown(res))
        return
    # B/C/E: đếm thẳng (không theo nhịp): mỗi mẫu, mỗi người đọc → nghĩa (điểm thấp nhất), cờ theo hai rubric (bất kỳ người chấm)
    scs = [json.load(open(p)) for p in sc]
    rows = {}
    for lab, h in rk.items():
        it = key['items'][h]; vs = [s[lab] for s in scs if lab in s]
        r = rows.setdefault(f"{it['set']}/{it['id']}", {'readers': 0, 'meaning1': 0, 'old': 0, 'new': 0, 'inferred': 0, 'caution': 0, 'quotes': []})
        r['readers'] += 1
        r['meaning1'] += min(v['score'] for v in vs) == 1
        r['old'] += any(packets._advice(v, 'old') for v in vs)
        r['new'] += any(packets._advice(v, 'new') for v in vs)
        r['inferred'] += any(v.get('advice_inferred') and not v.get('advice_stated') for v in vs)
        r['caution'] += any(v.get('caution_only') for v in vs)
        r['quotes'] += [v.get('quote') for v in vs if v.get('quote')]
        r['extra_layer_seen'] = r.get('extra_layer_seen', 0) + all(v.get('extra_layer_seen') for v in vs)
        r['must_beat_or_guaranteed'] = r.get('must_beat_or_guaranteed', 0) + any(v.get('must_beat_or_guaranteed') for v in vs)
        r.setdefault('q5', []).append('/'.join(sorted({str(v.get('q5', '?')) for v in vs})))
    json.dump({'graders': len(scs), 'rows': rows}, open(o / 'tally.json', 'w'), indent=1, ensure_ascii=False)
    L = ['| Mẫu | Người đọc | Nghĩa = 1 | Khuyên (rubric cũ) | advice_stated (mới) | advice_inferred | caution_only | extra_layer_seen | must_beat_or_guaranteed | Câu 5 |', '|---|---|---|---|---|---|---|---|---|---|']
    L += [f"| {k} | {r['readers']} | {r['meaning1']} | {r['old']} | {r['new']} | {r['inferred']} | {r['caution']} | {r['extra_layer_seen']} | {r['must_beat_or_guaranteed']} | {', '.join(r['q5'])} |" for k, r in sorted(rows.items())]
    L.append(f'\n{len(scs)} người chấm; gộp thận trọng (điểm thấp nhất, cờ nếu bất kỳ người chấm nào bật).')
    (o / 'tally.md').write_text('\n'.join(L) + '\n'); print('\n'.join(L))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('a', nargs='?'); ap.add_argument('b', nargs='?')
    ap.add_argument('--tag', default='r1'); ap.add_argument('--slots', default='1,2'); ap.add_argument('--only', default=''); ap.add_argument('--graders', type=int, default=2)
    x = ap.parse_args()
    if x.cmd == 'strips':
        do_strips(x.a, x.tag)
    elif x.cmd == 'read':
        do_read(x.a, x.b, [int(s) for s in x.slots.split(',')], set(filter(None, x.only.split(','))))
    elif x.cmd == 'pack':
        do_pack(x.a)
    elif x.cmd == 'grade':
        do_grade(x.a, x.graders)
    elif x.cmd == 'tally':
        do_tally(x.a)

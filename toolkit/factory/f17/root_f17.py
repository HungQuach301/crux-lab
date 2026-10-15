"""F-17 · cổng gốc CHẨN ĐOÁN (INTENT T13; A32: thước nhiễu) trên 3 nhịp của 3 cảnh v4: B01 (S01, đoạn a), B15 (S15, đoạn c), B29 (S29, đoạn g).
Hai bản: `ctl` = cảnh Tập 7 không lớp (episodes/ep007/world/c4/<đoạn>, page.html) · `cine` = cùng cảnh có lớp (toolkit/factory/f17/trial/<đoạn>).
Dải = 6 khung 1080p RENDER THẬT (render_shots.js --stills) ở đúng thời điểm của toolkit/blind/strips.py (tâm 6 lát của [đầu cảnh + 0,2; cuối − 0,2]),
cùng bố cục 3×2 đánh số. Vai, câu hỏi, rubric mới của episodes/ep007/c4/blind_c4.py; người đọc mới mỗi lượt; 2 người chấm trên MỘT gói chung (nhãn trộn).
Chạy từ gốc repo:
  python3 toolkit/factory/f17/root_f17.py strips <run>                 # <run> = toolkit/factory/f17/root
  python3 toolkit/factory/f17/root_f17.py read <run> [--slots 1,2]
  python3 toolkit/factory/f17/root_f17.py pack <run> | grade <run> | tally <run>
Chi: headless khoá Console (ANTHROPIC_API_KEY="$CONSOLE_API_KEY"), không agent con (headless.sh chỉ bật Read hoặc không công cụ), trần chi CỨNG của phiên
F17_CAP_USD (mặc định 4) theo sổ <run>/spend.json: trước mỗi lượt kiểm tổng đã chi + ước lượng lượt; vượt → dừng (không gọi API).
"""
import argparse, json, os, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
EP = ROOT / 'episodes/ep007'
sys.path[:0] = [str(EP / 'c4'), str(EP), str(ROOT / 'toolkit/blind')]
import blind_c4 as BC  # noqa: E402
import blind  # noqa: E402
import packets  # noqa: E402
import strips as SP  # noqa: E402

BEATS = {'B01': 'a-s01-s03', 'B15': 'c-s10-s15', 'B29': 'g-s29-s33'}
TRIAL = {'a-s01-s03': 'a', 'c-s10-s15': 'c', 'g-s29-s33': 'g'}
PROMPT = 'The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image.'
CAP = float(os.environ.get('F17_CAP_USD', 4)); EST = {'read': 0.12, 'grade': 0.6}
WORK = Path('/var/tmp/f17/root')


def spend(run, add=None, what=''):   # sổ chi CHUNG của phiên F-17 (cổng gốc + REVIEWER): toolkit/factory/f17/spend.json
    p = ROOT / 'toolkit/factory/f17/spend.json'; s = json.load(open(p)) if p.exists() else {'cap_usd': CAP, 'items': []}
    if add is not None: s['items'].append({'what': what, 'usd': add}); json.dump(s, open(p, 'w'), indent=1)
    return sum(x['usd'] or 0 for x in s['items'])


def guard(run, n, kind):
    tot = spend(run)
    if tot + n * EST[kind] > CAP: sys.exit(f'TRẦN: đã chi ${tot:.2f} + ước {n} × ${EST[kind]} > trần ${CAP}')


def strips(run):
    o = ROOT / run; o.mkdir(parents=True, exist_ok=True)
    sc = {s['id']: s for s in BC.timeline()['scenes']}; bt = BC.beats(); spans, times = {}, {}
    env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
    for b, seg in BEATS.items():
        sp = json.load(open(EP / f'world/c4/{seg}/spine.json')); t0e = sp['episode_t0']; s = sc[bt[b]['scene']]
        spans[b] = [round(s['start'] + 0.2, 3), round(s['end'] - 0.2, 3)]
        times[b] = [round(t - t0e, 3) for t in SP.frame_times(*spans[b])]
        for st, d in (('ctl', f'episodes/ep007/world/c4/{seg}'), ('cine', f'toolkit/factory/f17/trial/{TRIAL[seg]}')):
            od = WORK / st / b; od.mkdir(parents=True, exist_ok=True)
            subprocess.run(['node', 'toolkit/factory/world/render_shots.js', d, '1080', str(od / 'x.mp4'), '--stills', ','.join(map(str, times[b])),
                            '--stills-dir', str(od)], cwd=ROOT, env=env, check=True)
            pngs = sorted(od.glob('*.png'), key=lambda p: float(p.stem.split('-t')[-1]))
            assert len(pngs) == 6, (b, st, len(pngs))
            compose(pngs, o / f'strips-{st}' / f'{b}.png')
    json.dump({'spans_episode': spans, 'times_segment': times, 'beats': BEATS}, open(o / 'spans.json', 'w'), indent=1)
    print('strips', o)


def compose(pngs, out):   # bố cục của toolkit/blind/strips.py (khung 624×351, khe 12, dải số 50, nền #06080B)
    out.parent.mkdir(parents=True, exist_ok=True); font = SP._font(); TW, TH, GAP, LAB = SP.TW, SP.TH, SP.GAP, SP.LAB
    cmd = ['ffmpeg', '-v', 'error', '-y']
    for p in pngs: cmd += ['-i', str(p)]
    ch, lab = [], []
    for i in range(6):
        c = f'[{i}:v]scale={TW}:{TH}:flags=lanczos,setsar=1,pad={TW + GAP}:{TH + LAB + GAP}:{GAP}:{GAP}:color={SP.BG}'
        if font: c += f",drawtext=fontfile='{font}':text={i + 1}:fontsize=34:fontcolor={SP.FG}:x={GAP}+({TW}-text_w)/2:y={GAP + TH}+({LAB}-text_h)/2"
        ch.append(c + f'[f{i}]'); lab.append(f'[f{i}]')
    W, H = TW + GAP, TH + LAB + GAP
    lay = '|'.join(f'{(i % 3) * W}_{(i // 3) * H}' for i in range(6))
    fc = ';'.join(ch) + ';' + ''.join(lab) + f'xstack=inputs=6:layout={lay}:fill={SP.BG},pad=iw+{GAP}:ih+{GAP}:0:0:color={SP.BG}[out]'
    subprocess.run(cmd + ['-filter_complex', fc, '-map', '[out]', '-frames:v', '1', str(out)], check=True)


def read(run, slots):
    o = ROOT / run; kp = o / 'KEY.json'
    key = json.load(open(kp)) if kp.exists() else {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': BC.QUESTION_ID, 'candidate_set': 'cine', 'items': {}}
    taken = {(v['set'], v['id'], v['slot']) for v in key['items'].values()}; jobs = []
    for st in ('ctl', 'cine'):
        for b in BEATS:
            for k in slots:
                if (st, b, k) in taken: sys.exit(f'đã chia {st}/{b} cho người đọc {k}')
                h = secrets.token_hex(4); dst = WORK / 'readers' / f'{h}-1.png'; dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes((o / f'strips-{st}' / f'{b}.png').read_bytes())
                (o / f'{h}.txt').write_text(f'{BC.T}\n\nUse the Read tool to open exactly this one file and nothing else: {dst}\n{PROMPT}\n{BC.QS["root"]}')
                key['items'][h] = {'id': b, 'set': st, 'kind': 'image', 'slot': k, 'sha256': packets._sha(o / f'{h}.txt')}; jobs.append(h)
    guard(run, len(jobs), 'read')
    with cf.ThreadPoolExecutor(4) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(o / f'{h}.txt', o / f'{h}.json', read=True), jobs)))
    json.dump(key, open(kp, 'w'), indent=1, ensure_ascii=False)
    ans = json.load(open(o / 'answers.json')) if (o / 'answers.json').exists() else {}
    ans.update({h: r['answer'] for h, r in res.items() if r}); json.dump(ans, open(o / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    for h, r in res.items(): spend(run, (r or {}).get('cost_usd') or 0, f'read {h}')
    print(json.dumps({'runs': len(jobs), 'ok': sum(1 for r in res.values() if r), 'spent': round(spend(run), 3)}))


def pack(run):
    o = ROOT / run; rub = BC.rubric(); rub['items'] = {b: rub['items'][b] for b in BEATS}; rub['items'].update({f'ctrl:{b}': rub['items'][b] for b in BEATS})   # cùng nghĩa kỳ vọng hai bản (như f14)
    json.dump(rub, open(o / 'rubric.json', 'w'), indent=1, ensure_ascii=False)
    for f in ('rubric-key.json', 'packet.json'): (o / f).unlink(missing_ok=True)
    labs = packets.packet(str(o / 'KEY.json'), str(o / 'answers.json'), str(o / 'rubric.json'), str(o / 'packet.json'), str(o / 'rubric-key.json'))
    print(len(labs), 'nhãn trong một gói chung')


def grade(run, n=2):
    o = ROOT / run; guard(run, n, 'grade'); pk = json.load(open(o / 'packet.json'))
    body = ('# Grading packet (blind). You are an independent grader. Each label Rxx is one reader\'s answers about part of a personal-finance video. '
            'Grade each label literally with the rules and the expected meaning given for it. You know nothing else.\n\n'
            + json.dumps(pk, indent=1, ensure_ascii=False) + '\n\nOutput JSON only (no prose, no code fence), one entry per label: ' + pk['return']
            + ' — and add "q5": "video" | "own" | "none" to every entry, plus any extra flag an item asks for.\n')
    (o / 'grade-prompt.txt').write_text(body)

    def one(k):
        r = blind.run(o / 'grade-prompt.txt', o / f'grade-g{k}.json'); spend(run, (r or {}).get('cost_usd') or 0, f'grade g{k}')
        txt, dec, objs, i = r['answer'], json.JSONDecoder(), [], 0
        while (j := txt.find('{', i)) >= 0:
            try: ob, e = dec.raw_decode(txt[j:]); objs.append(ob); i = j + e
            except ValueError: i = j + 1
        json.dump({kk: v for kk, v in objs[-1].items() if isinstance(v, dict)}, open(o / f'scores-g{k}.json', 'w'), indent=1, ensure_ascii=False)
    with cf.ThreadPoolExecutor(n) as ex: list(ex.map(one, range(1, n + 1)))
    print('spent', round(spend(run), 3))


def tally(run):
    o = ROOT / run; key, rk = packets._load(str(o / 'KEY.json')), packets._load(str(o / 'rubric-key.json'))
    scs = [packets._load(str(p)) for p in sorted(o.glob('scores-g*.json'))]; out = {}
    for st in ('ctl', 'cine'):
        r = packets._tally_one(dict(key, candidate_set=st), rk, scs, 0.8, None, 'new'); out[st] = r
        print(f'== {st}: PASS {r["gate_pass"]}/{r["gate_beats"]} · chờ {r["pending"]} · advice_stated {r["advice_beats"]}')
    rows = {st: {x['id']: x for x in out[st]['rows'] if x['set'] == st} for st in out}
    for b in BEATS:
        c, v = rows['ctl'].get(b, {}), rows['cine'].get(b, {})
        print(f"{b}  ctl {' · '.join(map(str, c.get('scores', [])))} {c.get('status')}  |  cine {' · '.join(map(str, v.get('scores', [])))} {v.get('status')}")
    json.dump(out, open(o / 'tally.json', 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('run'); ap.add_argument('--slots', default='1,2'); x = ap.parse_args()
    {'strips': lambda: strips(x.run), 'read': lambda: read(x.run, [int(s) for s in x.slots.split(',')]), 'pack': lambda: pack(x.run),
     'grade': lambda: grade(x.run), 'tally': lambda: tally(x.run)}[x.cmd]()

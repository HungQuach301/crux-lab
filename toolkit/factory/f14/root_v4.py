"""F-14 v4 · cổng gốc theo INTENT §8: đối chứng (master bản giao) và v4 đọc bởi người đọc MỚI, chấm trong CÙNG một gói (nhãn trộn, 2 người chấm).
Dùng lại hàm của episodes/ep006/c4/blind_c4.py (vai, câu hỏi, rubric mới) và toolkit/blind (strips, headless, packets). Chạy từ gốc repo/worktree.
  python3 toolkit/factory/f14/root_v4.py strips <ctl.mp4> <v4.mp4> <run>       # <run> = episodes/ep006/c4/<tên>; dải 6 khung mỗi nhịp, mỗi bản một thư mục
  python3 toolkit/factory/f14/root_v4.py read <run> [--slots 1,2] [--only B13,B16] [--sets ctl,v4]
  python3 toolkit/factory/f14/root_v4.py pack <run>                              # đóng gói LẠI TOÀN BỘ câu trả lời (một gói chung)
  python3 toolkit/factory/f14/root_v4.py grade <run>                             # 2 người chấm headless trên cùng gói
  python3 toolkit/factory/f14/root_v4.py tally <run>                             # bảng từng bản (rubric mới, gộp thận trọng) → tally-v4.json
"""
import argparse, json, os, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
ROOT = Path.cwd()
EP = ROOT / 'episodes/ep006'
sys.path.insert(0, str(EP / 'c4')); sys.path.insert(0, str(EP)); sys.path.insert(0, str(ROOT / 'toolkit/blind'))
import blind_c4 as BC  # noqa: E402
import blind  # noqa: E402
import packets  # noqa: E402

PROMPT = 'The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image.'


def strips(ctl, v4, run):
    o = ROOT / run; o.mkdir(parents=True, exist_ok=True)
    tl, bt = BC.timeline(), BC.beats()
    sc = {s['id']: s for s in tl['scenes']}
    spans = {b: [round(sc[bt[b]['scene']]['start'] + 0.2, 3), round(sc[bt[b]['scene']]['end'] - 0.2, 3)] for b in BC.IMAGE}
    json.dump(spans, open(o / 'spans.json', 'w'))
    for name, video in (('ctl', ctl), ('v4', v4)):
        subprocess.run([sys.executable, str(ROOT / 'toolkit/blind/strips.py'), str(video), str(o / 'spans.json'), str(o / f'strips-{name}')], check=True)
    print('strips', o)


def read(run, slots, only, sets):
    o = ROOT / run
    kp = o / 'KEY.json'
    key = json.load(open(kp)) if kp.exists() else {'_': 'GIẢI MÃ — không đưa cho người đọc hay người chấm.', 'question': BC.QUESTION_ID,
                                                    'candidate_set': 'v4', 'items': {}}
    taken = {(v['set'], v['id'], v['slot']) for v in key['items'].values()}
    jobs = []
    for st in sets:
        for b in BC.IMAGE:
            if only and b not in only:
                continue
            for k in slots:
                if (st, b, k) in taken:
                    sys.exit(f'đã chia {st}/{b} cho người đọc {k}')
                h = secrets.token_hex(4)
                dst = o / f'{h}-1.png'; dst.write_bytes((o / f'strips-{st}' / f'{b}.png').read_bytes())
                (o / f'{h}.txt').write_text(f'{BC.T}\n\nUse the Read tool to open exactly this one file and nothing else: {dst}\n{PROMPT}\n{BC.QS["root"]}')
                key['items'][h] = {'id': b, 'set': st, 'kind': 'image', 'slot': k, 'sha256': packets._sha(o / f'{h}.txt')}
                jobs.append(h)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(o / f'{h}.txt', o / f'{h}.json', read=True), jobs)))
    json.dump(key, open(kp, 'w'), indent=1, ensure_ascii=False)
    ans = json.load(open(o / 'answers.json')) if (o / 'answers.json').exists() else {}
    ans.update({h: r['answer'] for h, r in res.items() if r})
    json.dump(ans, open(o / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({'runs': len(jobs), 'ok': sum(1 for r in res.values() if r), 'failed': [h for h in jobs if not res[h]]}))


def pack(run):
    o = ROOT / run
    rub = BC.rubric()
    rub['items'].update({f'ctl:{b}': rub['items'][b] for b in BC.IMAGE})   # cùng nghĩa kỳ vọng cho hai bản; gói không lộ bản nào
    json.dump(rub, open(o / 'rubric.json', 'w'), indent=1, ensure_ascii=False)
    for f in ('rubric-key.json', 'packet.json'):
        (o / f).unlink(missing_ok=True)
    labs = packets.packet(str(o / 'KEY.json'), str(o / 'answers.json'), str(o / 'rubric.json'), str(o / 'packet.json'), str(o / 'rubric-key.json'))
    print(len(labs), 'nhãn trong một gói chung')


def tally(run):
    o = ROOT / run
    key, rk = packets._load(str(o / 'KEY.json')), packets._load(str(o / 'rubric-key.json'))
    scs = [packets._load(str(p)) for p in sorted(o.glob('scores-g*.json'))]
    out = {}
    for st in ('ctl', 'v4'):
        k2 = dict(key, candidate_set=st)
        r = packets._tally_one(k2, rk, scs, 0.8, None, 'new')
        out[st] = r
        print(f'== {st}: PASS {r["gate_pass"]}/{r["gate_beats"]} · chờ {r["pending"]} · advice_stated {r["advice_beats"]}')
    ctl = {x['id']: x for x in out['ctl']['rows'] if x['set'] == 'ctl'}
    v4 = {x['id']: x for x in out['v4']['rows'] if x['set'] == 'v4'}
    for b in BC.IMAGE:
        c, v = ctl.get(b, {}), v4.get(b, {})
        flag = ' ← TỤT' if c.get('status') == 'PASS' and v.get('status') not in ('PASS', None) else ''
        print(f"{b}  ctl {' · '.join(map(str, c.get('scores', [])))} {c.get('status')}  |  v4 {' · '.join(map(str, v.get('scores', [])))} {v.get('status')}{flag}")
    json.dump(out, open(o / 'tally-v4.json', 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('a', nargs='*')
    ap.add_argument('--slots', default='1,2'); ap.add_argument('--only', default=''); ap.add_argument('--sets', default='ctl,v4')
    x = ap.parse_args()
    if x.cmd == 'strips': strips(*x.a)
    elif x.cmd == 'read': read(x.a[0], [int(s) for s in x.slots.split(',')], set(filter(None, x.only.split(','))), x.sets.split(','))
    elif x.cmd == 'pack': pack(x.a[0])
    elif x.cmd == 'grade': BC.do_grade(os.path.relpath(ROOT / x.a[0], EP), 2)
    elif x.cmd == 'tally': tally(x.a[0])

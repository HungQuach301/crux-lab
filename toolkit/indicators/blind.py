"""Hai thước mù headless chống tụt hình (tổng kết Tập 5 §3.3.1 và §3.3.3) — CHỈ BÁO, chưa là ngưỡng.

frames  — chấm mù khung (cine-lab Q27): 1 khung/20 s của mỗi video (video ngắn: đủ để có ≥ 6 khung), cùng cỡ 640 px, trộn theo hạt
          giống = SHA-256 của các video, đặt tên F01…; 3 người chấm headless có ảnh (`toolkit/blind/headless.sh --read`), mỗi khung
          3 tiêu chí 1–10 (beauty, clarity, craft). Không ai biết khung thuộc tập nào; khoá giải mã nằm ngoài đầu bài.
flow    — xem liền mạch mù (cine-lab #73: cửa sổ ±6 s tự tạo lỗi giả → dùng 1 khung/2,5 s, tức ±1,25 s quanh mỗi mốc): mỗi video thành
          tờ khung 4×4 (40 s/tờ) + lời có mốc giây; 3 người xem headless báo mốc "đổi phong cách" / "đứng hình" và điểm liền mạch 1–10.
          Điểm được ≥ 2/3 người cùng nêu (cách ≤ 4 s) là điểm chung. Sửa điểm ≥ 2/3 sau khi kiểm trên khung thật.
    python3 toolkit/indicators/blind.py frames prep  <ra-dir> <tên>=<video> …
    python3 toolkit/indicators/blind.py flow   prep  <ra-dir> <tên>=<video>=<lời.json>        (lời: script.json hoặc spine.json)
    bash <ra-dir>/run.sh            (chạy NỀN bằng công cụ nền của phiên, không `&` — episode.md §11b)
    python3 toolkit/indicators/blind.py frames tally <ra-dir>   |   python3 toolkit/indicators/blind.py flow tally <ra-dir>
"""
import hashlib, json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import video as V  # noqa: E402

HEADLESS = os.path.join(os.path.dirname(HERE), 'blind', 'headless.sh')
N_READERS = 3


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def write_run(out, jobs):
    lines = ['#!/usr/bin/env bash', 'set -uo pipefail', f'cd "{os.path.abspath(out)}"']
    for prompt, res in jobs:
        lines.append(f'[ -s {res} ] || bash {HEADLESS} {prompt} {res} --read || echo "LỖI {res}"')
    open(os.path.join(out, 'run.sh'), 'w').write('\n'.join(lines) + '\n')


# ---------------- frames ----------------
FR_PROMPT = """You are rating still frames from short explainer videos about personal finance. Judge each frame as a viewer would, on its own.
There are {n} images. Open each with the Read tool, in order: {files}
For EACH frame give three integer scores 1-10:
- beauty: how good the picture looks (composition, color, polish);
- clarity: how clearly the picture itself shows an idea a viewer could read;
- craft: how finished and professional it looks (no clutter, no overlap, legible text).
Use the whole scale. Answer ONLY with JSON lines, one per frame, nothing else:
{{"f": "F01", "beauty": 0, "clarity": 0, "craft": 0}}
"""


def frames_prep(out, items):
    os.makedirs(os.path.join(out, 'img'), exist_ok=True)
    vids = [(k, p) for k, p in items]
    seed = hashlib.sha256(''.join(sorted(sha(p) for _, p in vids)).encode()).hexdigest()
    pool = []
    for k, p in vids:
        dur = V.probe(p)
        step = 20.0 if dur / 20 >= 6 else dur / 7
        t = step / 2
        while t < dur - 0.5:
            pool.append((k, round(t, 2)))
            t += step
    random.Random(seed).shuffle(pool)
    key = {}
    for i, (k, t) in enumerate(pool, 1):
        f = f'F{i:02d}'
        V.grab(dict(vids)[k], t, os.path.join(out, 'img', f + '.jpg'))
        key[f] = {'video': k, 't': t}
    json.dump({'seed': seed, 'videos': {k: {'path': p, 'sha256': sha(p)} for k, p in vids}, 'key': key},
              open(os.path.join(out, 'key.json'), 'w'), indent=1)
    files = ', '.join(os.path.abspath(os.path.join(out, 'img', f + '.jpg')) for f in key)
    prompt = FR_PROMPT.format(n=len(key), files=files)
    jobs = []
    for r in range(1, N_READERS + 1):
        open(os.path.join(out, f'prompt-R{r}.txt'), 'w').write(prompt)
        jobs.append((f'prompt-R{r}.txt', f'R{r}.json'))
    write_run(out, jobs)
    print(f'{len(key)} khung → {out}; chạy {out}/run.sh')


def parse_lines(txt):
    res = []
    for m in re.finditer(r'\{[^{}]*\}', txt):
        try:
            res.append(json.loads(m.group(0)))
        except Exception:  # noqa: BLE001
            pass
    return res


def frames_tally(out):
    key = json.load(open(os.path.join(out, 'key.json')))['key']
    per, tok = {}, 0
    for r in range(1, N_READERS + 1):
        p = os.path.join(out, f'R{r}.json')
        if not os.path.exists(p):
            continue
        d = json.load(open(p))
        tok += sum(v.get('input', 0) + v.get('cache_write', 0) + v.get('output', 0) for v in d['tokens'].values())
        for row in parse_lines(d['answer']):
            if row.get('f') in key:
                s = (row['beauty'] + row['clarity'] + row['craft']) / 3
                per.setdefault(key[row['f']]['video'], {}).setdefault(f'R{r}', []).append(s)
    res = {}
    for v, rs in per.items():
        means = {r: round(sum(x) / len(x), 2) for r, x in rs.items()}
        res[v] = {'mean': round(sum(means.values()) / len(means), 2), 'by_reader': means, 'n': len(next(iter(rs.values())))}
    print(json.dumps({'frames': res, 'tokens_ceiling': tok}, ensure_ascii=False, indent=1))
    return res, tok


# ---------------- flow ----------------
FL_PROMPT = """You are watching a {dur:.0f}-second explainer video as contact sheets (no sound), with the narration below.
Sheets (open each with the Read tool, in order): {files}
Each sheet is a 4x4 grid read left-to-right, top-to-bottom; one frame every 2.5 seconds. Sheet k (k = 1, 2, …) starts at {span:.0f}*(k-1) seconds,
so the frame in row r, column c (both from 1) of sheet k is at {span:.0f}*(k-1) + 2.5*(4*(r-1) + (c-1)) seconds.
Narration (start second: sentence):
{lines}
Tasks:
1. List every moment where the picture BREAKS continuity: a sudden change of visual style (looks like a different video), or the picture
   stays frozen while the narration moves on. Give the second and the kind ("style" or "frozen") and a few words why.
2. Rate overall visual flow 1-10 (10 = the pictures flow as one continuous piece).
Answer ONLY with JSON lines, nothing else:
{{"t": 0, "kind": "style", "why": "..."}}
{{"flow": 0}}
"""


def load_lines(path):
    d = json.load(open(path))
    if 'sentences' in d:
        return [(s['start'], s['text']) for s in d['sentences']]
    out, cur, t0 = [], [], None   # spine: gom từ theo câu (sid)
    sid = None
    for w in d.get('words', []):
        if w['w'].startswith('['):
            continue
        if w.get('sid') != sid and cur:
            out.append((t0, ' '.join(cur))); cur = []
        if not cur:
            t0 = w['s']
        sid = w.get('sid'); cur.append(w['w'])
    if cur:
        out.append((t0, ' '.join(cur)))
    return out


def flow_prep(out, items):
    jobs = []
    meta = {}
    for name, vid, lines in items:
        hid = hashlib.sha256((name + sha(vid)).encode()).hexdigest()[:8]   # thư mục tên hex: người xem không thấy tên tập
        d = os.path.join(out, hid)
        os.makedirs(d, exist_ok=True)
        span = 40.0
        subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', vid, '-vf', 'fps=0.4,scale=320:-2,tile=4x4', '-q:v', '4',
                               os.path.join(d, 'sheet-%02d.jpg')])
        sheets = sorted(f for f in os.listdir(d) if f.startswith('sheet-'))
        dur = V.probe(vid)
        L = '\n'.join(f'{t:.0f}: {s}' for t, s in load_lines(lines))
        prompt = FL_PROMPT.format(dur=dur, span=span, files=', '.join(os.path.abspath(os.path.join(d, f)) for f in sheets), lines=L)
        for r in range(1, N_READERS + 1):
            open(os.path.join(d, f'prompt-R{r}.txt'), 'w').write(prompt)
            jobs.append((f'{hid}/prompt-R{r}.txt', f'{hid}/R{r}.json'))
        meta[name] = {'dir': hid, 'video': vid, 'sha256': sha(vid), 'lines': lines, 'sheets': len(sheets), 'dur': dur}
    json.dump(meta, open(os.path.join(out, 'meta.json'), 'w'), indent=1)
    write_run(out, jobs)
    print(f'{len(jobs)} lượt → {out}; chạy {out}/run.sh')


def flow_tally(out):
    meta = json.load(open(os.path.join(out, 'meta.json')))
    res, tok = {}, 0
    for name, m in meta.items():
        pts, flows = [], []
        for r in range(1, N_READERS + 1):
            p = os.path.join(out, m['dir'], f'R{r}.json')
            if not os.path.exists(p):
                continue
            d = json.load(open(p))
            tok += sum(v.get('input', 0) + v.get('cache_write', 0) + v.get('output', 0) for v in d['tokens'].values())
            for row in parse_lines(d['answer']):
                if 'flow' in row:
                    flows.append(float(row['flow']))
                elif 't' in row:
                    pts.append((float(row['t']), r, row.get('kind', '')))
        pts.sort()
        agreed, used = [], set()
        for i, (t, r, k) in enumerate(pts):
            if i in used:
                continue
            grp = [(j, x) for j, x in enumerate(pts) if abs(x[0] - t) <= 4 and j not in used]
            readers = {x[1] for _, x in grp}
            if len(readers) >= 2:
                agreed.append({'t': round(sum(x[0] for _, x in grp) / len(grp), 1), 'readers': len(readers),
                               'kinds': sorted({x[2] for _, x in grp})})
                used |= {j for j, _ in grp}
        res[name] = {'flow_mean': round(sum(flows) / len(flows), 2) if flows else None, 'flows': flows, 'points_all': len(pts),
                     'agreed': agreed, 'agreed_per_min': round(len(agreed) / (m['dur'] / 60), 2)}
    print(json.dumps({'flow': res, 'tokens_ceiling': tok}, ensure_ascii=False, indent=1))
    return res, tok


if __name__ == '__main__':
    kind, act, out = sys.argv[1:4]
    rest = sys.argv[4:]
    if kind == 'frames' and act == 'prep':
        frames_prep(out, [tuple(x.split('=', 1)) for x in rest])
    elif kind == 'frames':
        frames_tally(out)
    elif act == 'prep':
        flow_prep(out, [tuple(x.split('=', 2)) for x in rest])
    else:
        flow_tally(out)

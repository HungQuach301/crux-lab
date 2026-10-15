"""Tập 9 · M5: kiểm mù NHỚ LẠI (vai Đạo diễn sáng tạo, chỉ báo) + CHỖ MUỐN TUA (vai Editor, ngưỡng: không cảnh nào ≥ 2/3) — ý đồ gates/M5-intent.md §3, C5.
  python3 prod/recall.py sheets <video> <run>        # review-m5/<run>/sheet{1..4}.png (12 khung/hồi) + narration.txt (lời có mốc giây, out/factory/captions.srt)
  python3 prod/recall.py read <run>                  # 3 người đọc "recall" + 3 người đọc "skip" (mỗi người MỚI, headless --read)
  python3 prod/recall.py grade <run>                 # 1 người chấm độc lập mỗi bài → scores-*.json + tally.md
Người đọc chỉ thấy 4 tấm + lời; không tên dự án. Khoá ở review-m5/<run>.key/."""
import json, re, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]; ROOT = EP.parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
import yaml  # noqa: E402
INTRO = ('The four images show frames from a whole personal-finance video (about 10 minutes), in time order: image 1 = the opening and first part, '
         'image 2 = the second part, image 3 = the third part, image 4 = the limits and the ending. Below is the full narration you hear, with times.')
Q = {'recall': 'Answer in plain sentences:\n1. What three moments of the video do you remember most? Describe each (what you saw, what you heard).\n2. What question was the video asking?\n',
     'skip': 'Answer in plain sentences:\n1. Where, if anywhere, would you skip ahead? Give the start time (m:ss) from the narration and say why.\n2. Where were you most engaged? Give the time.\n'}


def o(run): d = (EP / 'review-m5' / run).resolve(); d.mkdir(parents=True, exist_ok=True); return d
def kd(run): d = (EP / 'review-m5' / (run + '.key')).resolve(); d.mkdir(parents=True, exist_ok=True); return d


def sheets(video, run):
    tl = json.load(open(EP / 'out/factory/timeline.json')); S = {s['id']: s for s in tl['scenes']}
    Y = yaml.safe_load(open(EP / 'episode.yaml'))
    groups = [['cold-open', 'act1'], ['act2'], ['act3'], ['method']]
    acts = {a['id']: a['scenes'] for a in Y['acts']}
    for k, g in enumerate(groups):
        sc = [S[s] for a in g for s in acts[a]]
        t0, t1 = min(s['start'] for s in sc), max(s['start'] + s['dur'] for s in sc)
        tmp = o(run) / f'sheet{k + 1}'; tmp.mkdir(exist_ok=True)
        for i in range(12):
            t = t0 + (i + 0.5) * (t1 - t0) / 12
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.3f}', '-i', str(video), '-frames:v', '1', '-vf',
                            f"scale=480:270,drawtext=text='{i + 1}':x=8:y=8:fontsize=28:fontcolor=white:box=1:boxcolor=black@0.6", str(tmp / f'{i:02d}.png')], check=True)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(tmp / '%02d.png'), '-vf', 'tile=4x3:padding=6:color=0x06080B', '-frames:v', '1',
                        str(o(run) / f'sheet{k + 1}.png')], check=True)
    srt = re.sub(r'\[[a-z ]+\]\s*', '', (EP / 'out/factory/captions.srt').read_text())
    (o(run) / 'narration.txt').write_text(srt)
    print('4 tấm + lời', o(run))


def read(run):
    d, k = o(run), kd(run); rd = d / 'readers'; rd.mkdir(exist_ok=True)
    key = {}; jobs = []
    narr = (d / 'narration.txt').read_text()
    for kind in ('recall', 'skip'):
        for slot in (1, 2, 3):
            h = secrets.token_hex(4); fl = []
            for i in range(4):
                dst = rd / f'{h}-{i + 1}.png'; dst.write_bytes((d / f'sheet{i + 1}.png').read_bytes()); fl.append(str(dst))
            (rd / f'{h}.txt').write_text(f'Read it once, as an ordinary YouTube viewer.\n\nUse the Read tool to open exactly these 4 files and nothing else: {", ".join(fl)}\n{INTRO}\n---\n{narr}\n---\n{Q[kind]}')
            key[h] = {'kind': kind, 'slot': slot}; jobs.append(h)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(jobs, ex.map(lambda h: blind.run(rd / f'{h}.txt', rd / f'{h}.json', read=True), jobs)))
    json.dump(key, open(k / 'KEY.json', 'w'), indent=1)
    json.dump({h: r['answer'] for h, r in res.items() if r}, open(k / 'answers.json', 'w'), indent=1, ensure_ascii=False)
    print({'runs': len(jobs), 'ok': sum(1 for r in res.values() if r)})


def grade(run):
    d, k = o(run), kd(run); key = json.load(open(k / 'KEY.json')); ans = json.load(open(k / 'answers.json'))
    tm = (EP / 'preprod/TAM-NHIN.md').read_text()
    moments = tm[tm.index('## 1.'):tm.index('## 2.')]
    q = re.search(r'\*\*Câu hỏi của phim\*\*[^:]*: (.+)', tm)[1]
    tl = json.load(open(EP / 'out/factory/timeline.json'))
    scenes = [[s['id'], round(s['start'], 1), round(s['start'] + s['dur'], 1)] for s in tl['scenes']]
    out = {}
    for kind in ('recall', 'skip'):
        labs = {f'R{i + 1}': h for i, h in enumerate(sorted(h for h in key if key[h]['kind'] == kind))}
        if kind == 'recall':
            rule = ('Expected moments (the film plan, in Vietnamese):\n' + moments + '\nExpected question of the film (Vietnamese): ' + q +
                    '\nFor each label return {"moments": [which of K1,K2,K3 the reader clearly recalls], "question_ok": true|false, "why": "<one line>"}.')
        else:
            rule = ('Scenes with start/end seconds: ' + json.dumps(scenes) + '\nFor each label return {"skip": [scene ids the reader would skip ahead in, from the times they give; [] if none], '
                    '"engaged": [scene ids], "why": "<one line>"}.')
        body = ('# Grading packet (blind). You are an independent grader. Grade each reader label literally.\n\n' + rule + '\n\n' +
                '\n\n'.join(f'### {lab}\n{ans[h]}' for lab, h in labs.items()) + '\n\nOutput JSON only: {"R1": {...}, ...}\n')
        (d / f'grade-{kind}.txt').write_text(body)
        r = blind.run(d / f'grade-{kind}.txt', d / f'grade-{kind}.json')
        txt = r['answer']; txt = txt[txt.find('{'):txt.rfind('}') + 1]
        out[kind] = json.loads(txt); json.dump({'labels': labs, 'scores': out[kind]}, open(d / f'scores-{kind}.json', 'w'), indent=1, ensure_ascii=False)
    rc = out['recall']; n_ok = sum(1 for v in rc.values() if len(v.get('moments', [])) >= 2)
    q_ok = sum(1 for v in rc.values() if v.get('question_ok'))
    from collections import Counter
    sk = Counter(s for v in out['skip'].values() for s in set(v.get('skip', [])))
    worst = sk.most_common(3)
    md = (f"# M5 nhớ lại + chỗ muốn tua ({run})\n\n- **Nhớ lại (chỉ báo):** {n_ok}/3 người kể ≥ 2/3 khoảnh khắc · câu hỏi đúng {q_ok}/3\n"
          f"- **Chỗ muốn tua (ngưỡng: không cảnh nào ≥ 2/3):** {dict(sk) or 'không ai muốn tua'} → **{'TRƯỢT' if worst and worst[0][1] >= 2 else 'ĐẠT'}**\n\n"
          + '\n'.join(f"- recall {l}: {v}" for l, v in rc.items()) + '\n' + '\n'.join(f"- skip {l}: {v}" for l, v in out['skip'].items()) + '\n')
    (d / 'tally.md').write_text(md); print(md)


if __name__ == '__main__':
    a = sys.argv[1:]
    {'sheets': lambda: sheets(a[1], a[2]), 'read': lambda: read(a[1]), 'grade': lambda: grade(a[1])}[a[0]]()

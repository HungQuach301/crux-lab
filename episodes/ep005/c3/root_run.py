"""Tập 5 · cổng gốc mù (headless có ảnh) cho dải 6 khung tắt tiếng.
  python3 c3/root_run.py read  <outdir> <id>=<png> [<id>=<png> …] [--n 2]
  python3 c3/root_run.py grade <outdir> <spans.json>        # muted read lấy từ spans.json["strips"][id]["muted_read"]
Người đọc: mỗi lượt mới, chỉ mở một PNG tên hex (toolkit/blind/headless.sh --read). Người chấm độc lập, rubric A9 (gates/C3-root-intent.md)."""
import json, os, secrets, shutil, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
T = "You are an American in your late 20s or early 30s, renting, who has saved about 10% of a home's price and is thinking about buying your first home."
Q = ("The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. Look only at the image. "
     "Answer in plain sentences:\n1. What idea is this animation showing?\n2. What changes over time across the frames?\n3. What does it mean?\n"
     "4. What advice, if any, would a viewer take from this?\n")


def read(outdir, items, n):
    o = Path(outdir).resolve(); o.mkdir(parents=True, exist_ok=True)
    kp = o / 'key.json'; key = json.load(open(kp)) if kp.exists() else []
    new = []
    for it in items:
        sid, png = it.split('=', 1)
        for _ in range(n):
            h = secrets.token_hex(4); dst = o / f'{h}.png'; shutil.copy(png, dst)
            (o / f'{h}.txt').write_text(f"{T}\n\nUse the Read tool to open exactly this one file and nothing else: {dst}\n{Q}")
            new.append({'file': h, 'sample': sid, 'role': 'T'})
    with cf.ThreadPoolExecutor(6) as ex:
        res = list(ex.map(lambda k: blind.run(o / f"{k['file']}.txt", o / f"{k['file']}.json", read=True), new))
    json.dump(key + new, open(kp, 'w'), indent=1)
    print(json.dumps({'runs': len(new), 'ok': sum(1 for r in res if r),
                      'tokens': sum(sum(v['in'] + v['out'] for v in r['tokens'].values()) for r in res if r)}))


def grade(outdir, spans):
    o = Path(outdir).resolve(); key = json.load(open(o / 'key.json'))
    sp = json.load(open(spans))['strips']
    intent = (EP / 'gates/C3-root-intent.md').read_text()
    rub = intent[intent.index('- **Chấm:**'):intent.index('- **Ngưỡng')]
    rub += "\n\nMuted read (đáp án đúng) theo hình:\n" + '\n'.join(f"- {k['sample']}: {sp[k['sample']]['muted_read']}" for k in {k['sample']: k for k in key}.values())
    parts = ["# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare "
             "against its muted read. Grade literally.\n\n## Rubric\n" + rub +
             '\n\nOutput JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}\n']
    lab = {}
    for i, k in enumerate(sorted(key, key=lambda k: k['file'])):
        L = f'R{i + 1}'; lab[L] = k['file']
        parts.append(f"### {L} (strip {k['sample']})\n" + json.load(open(o / f"{k['file']}.json"))['answer'] + '\n')
    (o / 'packet.md').write_text('\n'.join(parts)); json.dump(lab, open(o / 'label-key.json', 'w'))
    r = blind.run(o / 'packet.md', o / 'grade.json'); txt = r['answer']; sc = json.loads(txt[txt.find('{'):txt.rfind('}') + 1])
    out = [{**k, **sc[L]} for L, f in lab.items() for k in key if k['file'] == f]
    json.dump(out, open(o / 'scores.json', 'w'), indent=1, ensure_ascii=False)
    print('grader', sum(v['in'] + v['out'] for v in r['tokens'].values()))
    for s in sorted(out, key=lambda s: s['sample']): print(s['sample'], s['score'], 'ADV' if s['advice'] else '-', s['why'][:170])


if __name__ == '__main__':
    if sys.argv[1] == 'read':
        n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 2
        read(sys.argv[2], [a for a in sys.argv[3:] if '=' in a], n)
    else:
        grade(sys.argv[2], sys.argv[3])

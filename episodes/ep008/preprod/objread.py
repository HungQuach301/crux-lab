"""Đọc mù clip vật thể (ý đồ gates/PRE-objects-intent.md): dải 6 khung tắt tiếng → 2 người đọc headless mới mỗi vật (+1 khi lệch) → người chấm.
    ANTHROPIC_API_KEY="$CONSOLE_API_KEY" python3 episodes/ep008/preprod/objread.py read <vật…> <outdir> [--n 2]
    ANTHROPIC_API_KEY="$CONSOLE_API_KEY" python3 episodes/ep008/preprod/objread.py grade <outdir>
Người đọc chỉ thấy MỘT PNG tên hex trong thư mục tạm (không tên vật, không ngữ cảnh dự án)."""
import json, os, secrets, shutil, subprocess, sys, tempfile, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]
ROOT = EP.parents[1]
HEADLESS = ROOT / 'toolkit/blind/headless.sh'
ROLE = ('You are an American renter in 2026 who keeps wondering whether paying rent costs you more than buying a home would. '
        'You have never seen this video before.')
QS = ['What is this showing?', 'What changes over time?', 'What does it mean?', 'What advice, if any, would a viewer take from this?',
      'Did the animation itself suggest this, or is it your own conclusion?']
RUBRIC = (EP / 'gates/PRE-objects-intent.md').read_text().split('## Rubric nghĩa')[1]


def run(prompt, out, read):
    cmd = ['bash', str(HEADLESS), str(prompt), str(out)] + (['--read'] if read else [])
    for _ in range(3):
        if subprocess.run(cmd, capture_output=True, text=True).returncode == 0 and Path(out).exists():
            return json.load(open(out))
    return None


def read(objs, outdir, n):
    o = Path(outdir).resolve(); o.mkdir(parents=True, exist_ok=True)
    key = json.load(open(o / 'key.json')) if (o / 'key.json').exists() else []
    jobs = []
    for obj in objs:
        png = EP / 'work/objclip/strips' / f'{obj}.png'
        for _ in range(n):
            h = secrets.token_hex(4); d = Path(tempfile.mkdtemp(prefix='r'))
            shutil.copy(png, d / f'{h}.png')
            qs = '\n'.join(f'{i + 1}. {q}' for i, q in enumerate(QS))
            (o / f'{h}.txt').write_text(f'{ROLE}\n\nRead the image file {d}/{h}.png. It shows 6 frames, numbered in time order, from a short muted '
                                        f'animation.\n\nAnswer these questions, numbered, plain text:\n{qs}\n')
            key.append({'file': h, 'obj': obj}); jobs.append(h)
    json.dump(key, open(o / 'key.json', 'w'), indent=1)
    with cf.ThreadPoolExecutor(6) as ex:
        list(ex.map(lambda h: run(o / f'{h}.txt', o / f'{h}.json', True), jobs))
    print(len(jobs), 'lượt đọc')


def grade(outdir):
    o = Path(outdir).resolve(); key = json.load(open(o / 'key.json'))
    labels, parts = {}, [f'# Grading packet (blind). You are an independent grader. Each label is one reader\'s answers about a short muted animation of '
                         f'object X (named in the label header). Grade literally with the rubric (Vietnamese). Flags: advice_stated (the animation, its text '
                         f'or picture states or implies buy, rent, wait, choose/avoid), advice_inferred (reader\'s own conclusion), caution_only.\n\n'
                         f'## Rubric\n{RUBRIC}\n\nOutput JSON only (no prose, no code fence): {{"R1": {{"score": 1|0.5|0, "advice_stated": true|false, '
                         f'"advice_inferred": true|false, "caution_only": true|false, "why": "<one line, quote the reader>"}}, ...}}\n']
    names = {'street': 'N1 the street', 'tag': 'N2 the rent tag', 'nina': 'N3 Nina + đèn riêng', 'box': 'N4 the glass box', 'fog': 'N5 the fog'}
    for i, k in enumerate(sorted(key, key=lambda k: k['file'])):
        lab = f'R{i + 1}'; labels[lab] = k['file']
        parts.append(f'### {lab} — object {names[k["obj"]]}\n{json.load(open(o / (k["file"] + ".json")))["answer"]}\n')
    (o / 'packet.md').write_text('\n'.join(parts)); json.dump(labels, open(o / 'label-key.json', 'w'), indent=1)
    r = run(o / 'packet.md', o / 'grade.json', False)
    txt = r['answer'].strip().strip('`'); txt = txt[txt.find('{'):txt.rfind('}') + 1]
    sc = json.loads(txt)
    out = [{**k, **sc[lab]} for lab, f in labels.items() for k in key if k['file'] == f]
    json.dump(out, open(o / 'scores.json', 'w'), indent=1, ensure_ascii=False)
    for s in sorted(out, key=lambda s: s['obj']):
        print(s['obj'], s['score'], 'stated' if s['advice_stated'] else '-', s['why'][:140])


if __name__ == '__main__':
    if sys.argv[1] == 'read':
        n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 2
        args = [a for a in sys.argv[2:] if a != '--n' and a != str(n)]
        read(args[:-1], args[-1], n)
    else:
        grade(sys.argv[2])

#!/usr/bin/env python3
"""Kiểm mù headless cho Tập 5 (episode.md §2): tạo đầu bài người đọc, chạy song song, gói chấm, chạy người chấm.
  python3 blind.py read  <spec.json> <outdir>   # spec: {"samples":{id:text}, "roles":{T:..,G:..}, "plan":[[sample,role],..], "intro":..., "questions":[...]}
  python3 blind.py grade <outdir> <rubric.md> [--fields '...']
Đầu bài người đọc chỉ có vai + văn bản + câu hỏi (mù: không tên dự án, không file khác). Nhãn ngẫu nhiên; khoá ở <outdir>/key.json.
"""
import json, os, secrets, subprocess, sys, concurrent.futures as cf
from pathlib import Path
HEADLESS = Path(__file__).resolve().parents[2] / 'toolkit/blind/headless.sh'

def run(prompt, out, read=False):
    cmd = ['bash', str(HEADLESS), str(prompt), str(out)] + (['--read'] if read else [])
    for _ in range(3):
        if subprocess.run(cmd, capture_output=True, text=True).returncode == 0 and Path(out).exists():
            return json.load(open(out))
    return None

def read(spec_path, outdir):
    spec = json.load(open(spec_path)); o = Path(outdir); o.mkdir(parents=True, exist_ok=True)
    key = []
    for sample, role in spec['plan']:
        h = secrets.token_hex(4)
        role_txt = spec['roles'].get(role, '')
        qs = '\n'.join(f'{i+1}. {q}' for i, q in enumerate(spec['questions']))
        text = (f"{role_txt}\n\n" if role_txt else '') + f"{spec['intro']}\n\n---\n{spec['samples'][sample]}\n---\n\nAnswer these questions, numbered, plain text, no tools:\n{qs}\n"
        (o / f'{h}.txt').write_text(text); key.append({'file': h, 'sample': sample, 'role': role})
    json.dump(key, open(o / 'key.json', 'w'), indent=1)
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip([k['file'] for k in key], ex.map(lambda k: run(o / f"{k['file']}.txt", o / f"{k['file']}.json"), key)))
    tok = sum(sum(m['in'] + m['out'] for m in r['tokens'].values()) for r in res.values() if r)
    print(json.dumps({'runs': len(key), 'ok': sum(1 for r in res.values() if r), 'tokens': tok}))

def grade(outdir, rubric, fields):
    o = Path(outdir); key = json.load(open(o / 'key.json'))
    labels = {}
    parts = [f"# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.\n\n## Rubric\n{Path(rubric).read_text()}\n\nOutput JSON only (no prose, no code fence): {{\"R1\": {fields}, ...}}\n"]
    for i, k in enumerate(sorted(key, key=lambda k: k['file'])):
        lab = f'R{i+1}'; labels[lab] = k['file']
        a = json.load(open(o / f"{k['file']}.json"))['answer']
        parts.append(f'### {lab}\n{a}\n')
    (o / 'packet.md').write_text('\n'.join(parts)); json.dump(labels, open(o / 'label-key.json', 'w'), indent=1)
    r = run(o / 'packet.md', o / 'grade.json')
    txt = r['answer'].strip().strip('`'); txt = txt[txt.find('{'):txt.rfind('}') + 1]
    scores = json.loads(txt)
    out = [{**k, **scores[lab]} for lab, f in labels.items() for k in key if k['file'] == f]
    json.dump(out, open(o / 'scores.json', 'w'), indent=1, ensure_ascii=False)
    tok = sum(m['in'] + m['out'] for m in r['tokens'].values())
    print(json.dumps({'grader_tokens': tok, 'scores': out}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    if sys.argv[1] == 'read': read(sys.argv[2], sys.argv[3])
    else:
        f = sys.argv[sys.argv.index('--fields') + 1] if '--fields' in sys.argv else '{"score": 1|0.5|0, "advice": true|false, "why": "<one line>"}'
        grade(sys.argv[2], sys.argv[3], f)

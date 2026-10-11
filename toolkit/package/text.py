#!/usr/bin/env python3
"""Chữ gói phát hành do Claude viết (D-012 mục 3, tổng kết Tập 6 §4b): 3 tiêu đề, mô tả (2 dòng đầu chứa cụm từ tìm kiếm), chương có từ khoá,
tag tối thiểu — từ out/claims.json + out/timeline.json + mô tả máy + hồ sơ cầu + khuôn thắng (market/REPORT.md §3) + video neo (G1, nếu có).
Rồi tự kiểm: S21 (luật khoá, trên bản sao tối thiểu ngoài repo) + claim-risk (S10 ADVICE/FORECAST/FOUR/WE_BAD, số có claim, cụm bắt buộc,
ILLUSTRATIVE) + chương khớp timeline + từ chỉ vật thể của video (--objects; cấm từ thay thế --banned). Chữ do máy viết; chủ dự án chọn.

  python3 toolkit/package/text.py episodes/epNNN --topic q13-15-vs-30-mortgage --objects crates,check --banned basket,baskets,groceries \
      [--g1-title "…"] [--anchors <anchors.json>] [--out <thư mục>] [--model claude-opus-5-5]
Ra: <out>/text.json (tiêu đề + mô tả + chương + tag + kết quả kiểm) và <out>/description.md. Mặc định <out> = <tập>/out/package/text/.
Một lượt `claude -p` khoá Console (headless, không công cụ, 0 agent con); chi ghi vào text.json.
"""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'toolkit' / 'market'))
from package_check import scan, bad_numbers, chapters, claim_number_set   # noqa: E402  (dùng lại kiểm gói P4)
from brief import section                                                  # noqa: E402

RULES = """Hard rules: US personal-finance channel that replays real history with data. Titles <= 60 characters, put the phrase a viewer would
type into YouTube search FIRST. Use only the allowed numbers, written exactly. No advice ("you should", "best", "must"), no prediction
("will", "next year"), no "your money/loan will". Characters are ILLUSTRATIVE. Name the video's own objects with exactly these words: {objects};
never use: {banned}. No clickbait the video does not pay off. Description line 1+2 together <= 150 characters, contain the search phrase,
and say what the video replays. Chapter names: 2-6 words, contain a search keyword where natural, describe that part honestly.
Tags: at most 5 (YouTube says tags matter little), plain search phrases."""


def ask(prompt, model):
    env = dict(os.environ, ANTHROPIC_API_KEY=os.environ.get('CONSOLE_API_KEY', ''))
    p = subprocess.run(['claude', '-p', '--model', model, '--output-format', 'json', '--no-session-persistence', '--tools', ''],
                       input=prompt, capture_output=True, text=True, env=env, cwd=tempfile.mkdtemp(), timeout=900)
    d = json.loads(p.stdout)
    t = d.get('result', '')
    t = t[t.find('{'): t.rfind('}') + 1]
    return json.loads(t), d.get('total_cost_usd'), d.get('modelUsage', {})


def main(a):
    ep = pathlib.Path(a[0]); opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d   # noqa: E731
    topic, model = opt('--topic'), opt('--model', 'claude-opus-5-5')
    objects, banned = opt('--objects', ''), opt('--banned', '')
    out = pathlib.Path(opt('--out', ep / 'out' / 'package' / 'text')); out.mkdir(parents=True, exist_ok=True)
    cl = json.loads((ep / 'out' / 'claims.json').read_text()); cl = cl['claims'] if isinstance(cl, dict) else cl
    allowed = sorted({str(c['display']) for c in cl if c.get('display') and re.search(r'\d', str(c['display'])) and (c.get('spoken') or c.get('shownIn'))})
    tl = json.loads((ep / 'out' / 'timeline.json').read_text())
    mdesc = (ep / 'out' / 'package' / 'description.md').read_text()
    acts = [(0 if x['id'] == 'cold-open' else int(x['start']), x['id']) for x in tl['acts'] if x['id'] != 'ident']
    named = {t: n for t, n in chapters(mdesc)}
    acts = [(t, next((v for k, v in named.items() if abs(k - t) <= 2), n)) for t, n in acts]
    tm = (ROOT / 'market' / 'topics' / f'{topic}.md').read_text() if topic else ''
    qs = [re.sub(r'^\d+\.\s*', '', l).split(' — ')[0] for l in section(tm, 'Câu hỏi khán giả').splitlines() if re.match(r'^\d+\.', l)]
    kw = section(tm, 'Từ khoá mô tả').replace('\n', ' ')
    frames = [l.split(':', 1)[1].strip() for l in section((ROOT / 'market' / 'REPORT.md').read_text(), 'Cho brief').splitlines() if l.startswith('- title:')]
    anchors = json.loads(pathlib.Path(opt('--anchors')).read_text()) if opt('--anchors') else []
    prompt = f"""You write the YouTube packaging text for one finished video. Return ONLY JSON:
{{"titles":[{{"title":"...","search_phrase":"...","frame":"which winning frame or 'question'","why":"<=15 words"}} x3, best first],
"description_head":"two lines separated by \\n","chapters":[{{"t":<seconds, copy exactly>,"name":"..."}}],"tags":["..."]}}

{RULES.format(objects=objects or '(see summary)', banned=banned or '(none)')}

Video summary (machine description, factual): {mdesc.split(chr(10)+chr(10))[0]}
Approved working title at G1: {opt('--g1-title', '(none)')}
Allowed numbers: {', '.join(allowed)}
Chapter start times (keep the times, rename): {json.dumps(acts)}
Audience questions (dossier, highest weight first): {json.dumps(qs[:5])}
Search keywords seen in this niche (dossier; may be off-topic, use only if they describe THIS video): {kw}
Title frames that win in this niche: {json.dumps(frames)}
Anchor videos this one follows (same question, rising now; do not copy their titles): {json.dumps([{k: x.get(k) for k in ('channel', 'gap', 'phrase')} for x in anchors])}
"""
    r, cost, usage = ask(prompt, model)
    titles = r.get('titles', [])[:3]
    head = r.get('description_head', '').strip()
    chap = '\n'.join(f"{int(c['t']) // 60}:{int(c['t']) % 60:02d} {c['name']}" for c in r.get('chapters', []))
    body = mdesc.split('\n\n', 1)[1] if '\n\n' in mdesc else ''
    body = re.sub(r'(?ms)^Chapters\n(?:\d+:\d\d .*\n?)+', 'Chapters\n' + chap + '\n', body)
    desc = head + '\n\n' + mdesc.split('\n\n')[0] + '\n\n' + body
    (out / 'description.md').write_text(desc)
    # ---- kiểm
    ok = claim_number_set(cl); fails = []
    for t in titles:
        s = t['title']
        if len(s) > 60: fails.append(f'title "{s}": {len(s)} ký tự > 60')
        fails += [f'title "{s}": {k} "{m}"' for k, m in scan(s)] + [f'title "{s}": số "{n}" không có claim' for n in bad_numbers(s, ok)]
        if t.get('search_phrase') and not s.lower().startswith(t['search_phrase'].lower()[:12]): fails.append(f'title "{s}": cụm tìm kiếm không đứng đầu')
    if len(head) > 160: fails.append(f'2 dòng đầu mô tả {len(head)} ký tự > 150')
    fails += [f'mô tả: {k} "{m}"' for k, m in scan(desc)] + [f'mô tả: số "{n}" không có claim' for n in bad_numbers(head, ok)]
    allt = ' '.join([t['title'] for t in titles] + [head, chap, ' '.join(r.get('tags', []))]).lower()
    fails += [f'từ cấm "{b}" (vật thể của video là: {objects})' for b in banned.split(',') if b and re.search(rf'\b{re.escape(b)}\b', allt)]
    starts = [x[0] for x in acts]
    fails += [f'chương {c["t"]} không khớp đầu hồi' for c in r.get('chapters', []) if not any(abs(c['t'] - s) <= 2 for s in starts)]
    if len(r.get('tags', [])) > 5: fails.append(f"{len(r['tags'])} tag > 5")
    with tempfile.TemporaryDirectory() as td:   # S21 trên bản sao tối thiểu (không ghi vào tập)
        tp = pathlib.Path(td) / ep.name; (tp / 'out' / 'package').mkdir(parents=True)
        for f in ('out/claims.json', 'out/timeline.json', 'contract.json'):
            if (ep / f).exists(): shutil.copy(ep / f, tp / f)
        (tp / 'out' / 'package' / 'description.md').write_text(desc)
        subprocess.run([sys.executable, str(ROOT / 'checks/py/run.py'), str(tp), '--only', 'S21'], capture_output=True)
        rep = json.loads((tp / 'out/checks/report-partial.json').read_text())
        s21 = next((x for x in rep['results'] if x['id'] == 'S21'), {})
        if s21.get('status') != 'PASS': fails.append(f"S21 {s21.get('status')}: {json.dumps(s21.get('details'))[:300]}")
    res = {**r, 'description_file': str(out / 'description.md'), 'check': {'pass': not fails, 'fails': fails, 'S21': s21.get('status')},
           'cost_usd': cost, 'usage': usage, 'model': model}
    (out / 'text.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(json.dumps({'titles': [t['title'] for t in titles], 'head': head, 'chapters': chap.split('\n'), 'tags': r.get('tags'),
                      'check': res['check'], 'cost_usd': cost}, ensure_ascii=False, indent=1))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

"""K4.0.2 — luật tập 3 của K-brief Tập 6 qua S19 (claims.forbiddenAmounts): chạy trên câu của story/script.md (chưa có out/script.json, chưa có trang:
chỉ cửa sổ "sentence") + một câu đối chứng dương. python3 checks-runs/K402/s19_ep006.py <gốc ep006> [--out …]"""
import json, os, re, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'checks', 'py'))
import common, run  # noqa: E402,E401,F401
ep = os.path.join(os.path.abspath(sys.argv[1]), 'episodes', 'ep006')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
sents = [{'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip(), 'start': 0, 'end': 1}
         for m in (LINE.match(ln) for ln in open(os.path.join(ep, 'story', 'script.md'), encoding='utf-8')) if m]
FA = {'claims': {'forbiddenAmounts': [{'id': 'annuity_total_received', 'terms': ['more money', 'pays more', 'total', 'in total', 'more overall'], 'window': 'sentence'}]}}
R = {f.rid: f for f in common.RULES}
res = {}
for name, extra in (('script', []), ('control', [{'id': 'X.1', 'scene': 'X', 'text': 'Over 20 years the level check pays $41,000 more in total.', 'start': 0, 'end': 1}])):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'out'))
    json.dump({'sentences': sents + extra}, open(os.path.join(d, 'out', 'script.json'), 'w'))
    json.dump({'claims': []}, open(os.path.join(d, 'out', 'claims.json'), 'w'))
    json.dump({'episode': 'ep006', **FA}, open(os.path.join(d, 'contract.json'), 'w'))
    r = common.safe(R['S19'], common.Ctx(d))
    res[name] = {'status': r['status'], 'metrics': r['metrics'], 'details': r['details']}
    print(name, r['status'], len(sents) + len(extra), 'câu', r['details'][:2])
res['_about'] = 'luật tập 3 (K-brief Tập 6): không câu nào so tổng tiền nhận được giữa khoản đều và khoản 2 %. S19 bắt câu/khung có từ khoá + số $ không có claim nguồn; câu so sánh KHÔNG có số (vd "the level check pays more") là phán đoán nghĩa → REVIEWER/kiểm mù.'
res['contractSnippet'] = FA
if '--out' in sys.argv:
    json.dump(res, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False)

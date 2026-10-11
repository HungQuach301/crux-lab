"""K4.2b — trước/sau A28 trên kiểm mù C4 Tập 6: mỗi lượt có KEY.json, rubric-key.json, scores-g1/g2.json; `tally` của main (mặc định old, lệch → giữ old)
so với K4.2b (mặc định new). Lượt chấm theo ý đồ (slot > 3) không qua tally → ghi là không áp dụng.
  python3 checks-runs/K42/before_after_a28.py <toolkit/blind cũ> [--out checks-runs/K42/a28-before-after.json]"""
import importlib.util, json, os, sys
def load(p, name):
    sp = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
old = load(os.path.join(sys.argv[1], 'packets.py'), 'packets_old')
new = load('toolkit/blind/packets.py', 'packets_new')
rows = []
base = 'episodes/ep006/c4'
for run in sorted(os.listdir(base)):
    o = os.path.join(base, run)
    if not os.path.isfile(os.path.join(o, 'KEY.json')):
        continue
    sc = [os.path.join(o, f) for f in ('scores-g1.json', 'scores-g2.json') if os.path.isfile(os.path.join(o, f))]
    row = {'run': run}
    for tag, m in (('main', old), ('k42b', new)):
        try:
            r = m.tally(os.path.join(o, 'KEY.json'), os.path.join(o, 'rubric-key.json'), sc, threshold=0.8)
            row[tag] = {'gate': r['advice_rubric'], 'verdict': r['verdict'], 'pass': f"{r['gate_pass']}/{r['gate_beats']}", 'advice_beats': r['advice_beats'],
                        'verdict_old': r['verdict_old'], 'verdict_new': r['verdict_new'], 'disagree': r['rubric_disagree']}
        except SystemExit as e:
            row[tag] = {'notApplicable': str(e)[:120]}
    rows.append(row); print(json.dumps(row, ensure_ascii=False))
if '--out' in sys.argv:
    json.dump(rows, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False)

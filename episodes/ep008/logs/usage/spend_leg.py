"""Tập 8 chặng sau G1 (M2→G2): chi Console thật, trần CỨNG $25 (chủ dự án 13/10) — chạm thì dừng hỏi.
Cộng api.sh *.jsonl (result.total_cost_usd) + headless *.json (cost_usd) có mtime sau mốc mở chặng.
    python3 episodes/ep008/logs/usage/spend_leg.py"""
import glob, json, os, pathlib, datetime
EP = pathlib.Path(__file__).resolve().parents[2]
T0 = datetime.datetime(2026, 10, 13, 16, 0, tzinfo=datetime.timezone.utc).timestamp()
BASE = set(l.strip() for l in open(EP / 'logs/usage/leg-baseline.txt'))   # tệp có sẵn lúc mở chặng (P1) — không cộng
skip = lambda f: './' + os.path.relpath(f, EP) in BASE
api, hl, rows = 0.0, 0.0, []
for f in glob.glob(str(EP / '**' / '*.jsonl'), recursive=True):
    if skip(f) or os.path.getmtime(f) < T0 or '/out/' in f: continue
    for l in open(f):
        try: d = json.loads(l)
        except Exception: continue
        if d.get('type') == 'result' and d.get('total_cost_usd'):
            api += d['total_cost_usd']; rows.append((os.path.relpath(f, EP), round(d['total_cost_usd'], 3)))
for f in glob.glob(str(EP / '**' / '*.json'), recursive=True):
    if skip(f) or os.path.getmtime(f) < T0 or '/out/' in f or '/data/' in f: continue
    try: d = json.load(open(f))
    except Exception: continue
    if isinstance(d, dict) and 'cost_usd' in d and 'answer' in d:
        hl += d['cost_usd'] or 0
tot = api + hl
print(json.dumps({'api_sh': round(api, 3), 'headless': round(hl, 3), 'TOTAL': round(tot, 3), 'cap': 25, 'STOP': tot >= 25}))
for r in rows: print(' ', *r)

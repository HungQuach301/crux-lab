"""Tập 8 P1: cộng chi Console thật (trần CỨNG $12): api.sh *.jsonl (result.total_cost_usd) + headless *.json (cost_usd) + ai.py ledger hôm nay.
    python3 episodes/ep008/logs/usage/spend.py"""
import glob, json, os, pathlib, datetime
EP = pathlib.Path(__file__).resolve().parents[2]
tot, rows = 0.0, []
for f in glob.glob(str(EP / 'logs' / '*.jsonl')):
    for l in open(f):
        try: d = json.loads(l)
        except Exception: continue
        if d.get('type') == 'result' and d.get('total_cost_usd'):
            tot += d['total_cost_usd']; rows.append((os.path.basename(f), d['total_cost_usd']))
hl = 0.0
for f in glob.glob(str(EP / '**' / '*.json'), recursive=True):
    if '/out/' in f or '/data/' in f: continue
    try: d = json.load(open(f))
    except Exception: continue
    if isinstance(d, dict) and 'cost_usd' in d and 'answer' in d:
        hl += d['cost_usd'] or 0
led = pathlib.Path.home() / 'market-cache'
ai = 0.0
for f in led.glob('*/ai-ledger.jsonl'):
    for l in f.read_text().splitlines():
        r = json.loads(l)
        if r['t'] > datetime.datetime(2026, 10, 13, 15, tzinfo=datetime.timezone.utc).timestamp(): ai += r['cost_usd'] or 0
print(json.dumps({'api_sh': round(tot, 3), 'headless_readers': round(hl, 3), 'market_ai': round(ai, 3), 'TOTAL': round(tot + hl + ai, 3), 'cap': 12}))

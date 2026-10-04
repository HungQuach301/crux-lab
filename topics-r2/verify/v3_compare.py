"""V3: compare each blind recomputation (topics-r2/verify/v3/<id>/result.json) with the frozen result.json numbers[].value.
Same tolerance as V2 (verify.close). Writes topics-r2/verify/out/<id>.v3.json. Usage: python3 topics-r2/verify/v3_compare.py"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from verify import close, MACHINE, OUT  # noqa: E402

os.makedirs(OUT, exist_ok=True)
for tid in sorted(os.listdir(os.path.join(HERE, 'v3'))):
    th = json.load(open(os.path.join(MACHINE, tid, 'result.json')))
    rp = os.path.join(HERE, 'v3', tid, 'result.json')
    res = {'id': tid, 'items': [], 'ok': True}
    if not os.path.exists(rp):
        res.update(ok=False, why='no result.json')
    else:
        got = json.load(open(rp))
        for n in th['numbers']:
            ok = n['id'] in got and close(got[n['id']], n.get('value'))
            res['items'].append({'id': n['id'], 'declared': n.get('value'), 'recomputed': got.get(n['id']), 'ok': ok})
            res['ok'] &= ok
    json.dump(res, open(os.path.join(OUT, f'{tid}.v3.json'), 'w'), indent=1, ensure_ascii=False)
    bad = [i['id'] for i in res['items'] if not i['ok']]
    print(tid, 'V3', res['ok'], ('fail: ' + ', '.join(bad)) if bad else res.get('why', ''))

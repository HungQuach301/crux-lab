"""K4.2b — trước/sau A31 (2b) trên Tập 4–7: lấy số đo ĐÃ GHI trong báo cáo checks cuối của mỗi tập (thời lượng F07, điểm chèn S14, tổng timeline S15)
và áp ngưỡng cũ (main, LOCK d9a694e5) và ngưỡng mới (K4.2b). Video/master ngoài git nên không đo lại; luật chỉ đổi ngưỡng, không đổi cách đo.
  python3 checks-runs/K42/before_after_a31.py [--out checks-runs/K42/a31-before-after.json]"""
import json, sys
REP = {'ep004': 'episodes/ep004/out/checks/report.json', 'ep005': 'episodes/ep005/out/checks/report.json', 'ep006': 'episodes/ep006/out/checks/run-c5d/report.json'}
OLD = {'F07': {f: [480.0, 900.0] for f in ('lab', '101', 'deep')}, 'breaks': {'lab': 2, '101': 1}, 'floor': {'lab': 540.0, '101': None}}
NEW = {'F07': {'101': [480.0, 540.0], 'lab': [540.0, 660.0], 'deep': [840.0, 1020.0]}, 'breaks': {'lab': 2, '101': 1, 'deep': [2, 3]},
       'floor': {'lab': 540.0, '101': None, 'deep': 840.0}, 'gap': {'deep': 180.0}}


def judge(T, fmt, dur, br, total):
    lo, hi = T['F07'][fmt]
    nb = T['breaks'].get(fmt)
    ok_n = None if nb is None else (nb[0] <= len(br) <= nb[1] if isinstance(nb, list) else len(br) == nb)
    g = T.get('gap', {}).get(fmt)
    sb = sorted(br)
    close = sum(1 for a, b in zip(sb, sb[1:]) if g and b - a < g)
    fl = T['floor'].get(fmt)
    return {'F07': lo <= dur <= hi, 'S14.count': ok_n, 'S14.gap': close == 0, 'S15.total': True if not fl else total >= fl}


rows = []
for ep, p in REP.items():
    r = {x['id']: x for x in json.load(open(p))['results']}
    fmt = json.load(open(f'episodes/{ep}/contract.json')).get('format') or 'lab'
    dur = next(m['value'] for m in r['F07']['metrics'] if m['name'] == 'duration s')
    br = next((d['breaks'] for d in r['S14'].get('details', []) if isinstance(d, dict) and 'breaks' in d), [])
    total = next((m['value'] for m in r['S15']['metrics'] if m['name'] == 'total s'), None) or json.load(open(f'episodes/{ep}/out/timeline.json'))['total']
    rows.append({'episode': ep, 'report': p, 'format': fmt, 'duration': dur, 'breaks': br, 'total': total,
                 'statusInReport': {k: r[k]['status'] for k in ('F07', 'S14', 'S15')}, 'old': judge(OLD, fmt, dur, br, total), 'new': judge(NEW, fmt, dur, br, total)})
rows.append({'episode': 'ep007', 'report': None, 'format': 'lab', 'duration': 605.0, 'breaks': [], 'total': 605.0, 'note': 'chưa dựng: ước 10:05 của kịch bản C2 v3 (episodes/ep007/gates/G1.md); chỉ F07/S15 theo độ dài ước',
             'old': dict(judge(OLD, 'lab', 605.0, [], 605.0), **{'S14.count': None, 'S14.gap': None}), 'new': dict(judge(NEW, 'lab', 605.0, [], 605.0), **{'S14.count': None, 'S14.gap': None})})
for x in rows:
    ch = {k: (x['old'][k], x['new'][k]) for k in x['new'] if x['old'][k] != x['new'][k]}
    print(x['episode'], x['format'], x['duration'], x['breaks'], 'đổi:', ch or 'không')
if '--out' in sys.argv:
    json.dump(rows, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False)

"""Tập 5 · C4 · báo cáo F-1 trên nhật ký trang của mỗi đoạn thế giới (work/factory/world/<id>-<res>.log.json, mỗi 0,1 s):
mỗi lần đổi chế độ (move 'mode'): kiểu (fly/dissolve), độ nghiêng LỚN NHẤT của cạnh đứng vật thế giới trên màn hình (độ) trong cửa sổ,
che khung lớn nhất và thời gian che > 60 % liên tục (s), số vi phạm quy tắc 1 trong cửa sổ. Ngưỡng: nghiêng ≤ 3°, che > 60 % không quá 0,3 s.
  python3 episodes/ep005/c4/fly_report.py [--res 540] → out/factory/fly-report.json + in bảng"""
import json, os, sys
import yaml
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
res = sys.argv[sys.argv.index('--res') + 1] if '--res' in sys.argv else '540'
Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
out, rows = [], []
for w in Y['world']:
    sp = json.load(open(os.path.join(EP, w['dir'], 'spine.json')))
    lp = os.path.join(EP, 'work', 'factory', 'world', f"{w['id']}-{res}.log.json")
    logs = sorted(json.load(open(lp)), key=lambda l: l['t'])
    for m in sp['moves']:
        if m['verb'] != 'mode':
            continue
        L = [l for l in logs if m['t0'] - 1e-6 <= l['t'] <= m['t1'] + 1e-6]
        tilt = max(L, key=lambda l: l.get('tilt', {}).get('deg', 0)) if L else None
        cov = max(L, key=lambda l: l.get('cover', {}).get('f', 0)) if L else None
        run, best = 0.0, 0.0
        for l in L:
            run = run + 0.1 if l.get('cover', {}).get('f', 0) > 0.6 else 0.0
            best = max(best, run)
        r1 = sum(len(l.get('violations', [])) for l in L)
        x = {'segment': w['id'], 'move': m['id'], 'from': m['from'], 'to': m['to'], 'style': m.get('style', 'dissolve'), 'via': m.get('via'),
             't0_ep': round(sp['episode_t0'] + m['t0'], 2), 'dur': round(m['t1'] - m['t0'], 2),
             'tilt_max_deg': tilt['tilt']['deg'] if tilt else None, 'tilt_obj': tilt['tilt']['obj'] if tilt else None, 'tilt_t': round(tilt['t'], 2) if tilt else None,
             'cover_max': cov['cover']['f'] if cov else None, 'cover_obj': cov['cover']['obj'] if cov else None, 'cover_over60_s': round(best, 1), 'rule1': r1}
        x['pass'] = (x['tilt_max_deg'] or 0) <= 3.0 and best <= 0.3 and r1 == 0
        out.append(x)
json.dump(out, open(os.path.join(EP, 'out', 'factory', 'fly-report.json'), 'w'), indent=1)
for x in out:
    print(f"{x['segment']:10} {x['move']:8} {x['style']:8} t={x['t0_ep']:7.2f} tilt {x['tilt_max_deg']}° ({x['tilt_obj']}) cover {x['cover_max']} ({x['cover_obj']}) >60%: {x['cover_over60_s']} s r1 {x['rule1']} {'OK' if x['pass'] else 'FAIL'}")
print('fly', sum(x['style'] == 'fly' for x in out), 'dissolve', sum(x['style'] != 'fly' for x in out), 'max tilt', max(x['tilt_max_deg'] or 0 for x in out))

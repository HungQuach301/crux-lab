"""Tập 3 C3 · dữ liệu cho mẫu đối chứng V4 (thư viện hình, Tập 2 KEY-1): ridge TB3MS từ 1953-01 (cùng file ghim),
đường lãi thả nổi của Leah (start 1962-12, var0 7.5, mức cố định 9) theo replayPath của d2/engine.js. Chỉ để kiểm bộ đo, không phải số của tập."""
import csv, json, os
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
tb = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:]]
ridge = [{'m': m, 'r': r} for m, r in tb if m >= '1953-01']
idx = ridge[-1]['r']; s = [d['m'] for d in ridge].index('1962-12')
path = [round(7.5 - idx + max(0, idx + ridge[s + k]['r'] - ridge[s]['r']), 6) for k in range(120)]
starts = [d['m'] for d in ridge if d['m'] >= '1954-01'][:753]
D = {'ridge': ridge, 'starts': starts, 'k1': {'path': path}, 'claims': {'fixed_rate': '9%', 'var_start': '7.5%'}}
os.makedirs(os.path.join(EP, 'design/c3/work'), exist_ok=True)
open(os.path.join(EP, 'design/c3/work/ctrl-data.js'), 'w').write('window.DATA = ' + json.dumps(D) + ';\n')
print('ctrl data', len(ridge), 'months; path', path[:3])

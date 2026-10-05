"""Tập 3 C4 · dữ liệu cho đối chứng hiệu chuẩn V1 (thư viện, `h3/scenes.js` K5): TB3MS ghim 1954-01…2026-08, mọi cửa sổ 120 tháng,
cờ "vượt 9%" theo công thức ở đầu scenes.js (khoản vay Leah của Tập 2, ILLUSTRATIVE). Chỉ để kiểm bộ đo, không phải số của tập.
    python3 episodes/ep003/design/c4/ctrl/build_ctrl.py"""
import csv, json, os
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
tb = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:] if r[0][:7] >= '1954-01']
S = [v for _, v in tb]; NM = len(S); IDX = S[-1]; MARGIN = 7.5 - IDX
rate = lambda i, k: MARGIN + max(0.0, IDX + S[i + k] - S[i])
W = [{'start': tb[i][0], 'above': any(rate(i, k) > 9 + 1e-9 for k in range(120))} for i in range(NM - 120 + 1)]
D = {'series': tb, 'windows': W, 'worstIdx': 0, 'ex': {'fall': {'i': 0}}, 'sweep': [{'g': 0, 'bits': [], 'worst': 0}],
     'claims': {'first_start': {'display': 'January 1954'}, 'best_start_year': {'display': '1981'}}}
os.makedirs(os.path.join(EP, 'design/c4/work'), exist_ok=True)
open(os.path.join(EP, 'design/c4/work/ctrl-data.js'), 'w').write('window.DATA = ' + json.dumps(D) + ';\n')
print(NM, 'months;', len(W), 'windows')

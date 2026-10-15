"""Dữ liệu clip vật thể thử (P1 Tập 8): mỗi tháng bắt đầu 10 năm → người mua hơn? ở neo 4/5/6 %. Từ model/model.py (cùng định nghĩa).
    python3 episodes/ep008/preprod/objclip/data.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'model'))
import model as M
hpi, cpi, tb, rate, rml, lw = M.load()
D = (hpi, cpi, tb, rate)
ss = M.starts(10, D)
out = {'starts': ss, 'ahead': {str(y): [M.run(s, 10, D, y0=y / 100)['adv'] > 0 for s in ss] for y in (4, 5, 6)}}
for y, a in out['ahead'].items():
    print(y, sum(a), len(a), round(100 * sum(a) / len(a), 1))
json.dump(out, open(os.path.join(HERE, 'data.json'), 'w'))

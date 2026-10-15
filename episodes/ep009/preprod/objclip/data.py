"""Tập 9 · dữ liệu clip vật thể N6 (đống cổ phiếu): quỹ người thuê ở cổ phiếu theo tháng, cửa sổ 10 năm có đáy thấp nhất (min_pot_stocks_10y).
    python3 episodes/ep009/preprod/objclip/data.py  → data.json {start, pot[121], low, lowMonth}"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(EP, 'model')); import model as M
D = M.load(); hpi, cpi, rate, stk = D
def path(s):
    r = rate[s] / 1200; loan = M.P * (1 - M.DOWN); pay = loan * r / (1 - (1 + r) ** -M.N)
    y = M.Y0 * (cpi[s] / hpi[s]) / (cpi[M.ANCHOR] / hpi[M.ANCHOR]); rent0 = y * M.P / 12
    pot, out = M.P * (M.DOWN + M.CLOSE), []
    out.append(pot)
    for k in range(120):
        m = M.mo(s, k); pot += pay + M.OWN / 12 * M.P * hpi[m] / hpi[s] - rent0 * cpi[m] / cpi[s]; pot *= 1 + stk[m]; out.append(pot)
    return out
best = min(M.starts(10, D), key=lambda s: min(path(s)))
p = path(best); i = p.index(min(p))
json.dump({'start': best, 'pot': [round(x) for x in p], 'low': round(min(p)), 'lowMonth': M.mo(best, i - 1)}, open(os.path.join(HERE, 'data.json'), 'w'))
print(best, round(min(p)), M.mo(best, i - 1), round(p[-1]))

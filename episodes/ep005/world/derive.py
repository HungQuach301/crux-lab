"""Tập 5 · dữ liệu hình cho các đoạn thế giới 3D, dẫn xuất từ model/model.py của tập (không sửa mô hình).
  python3 episodes/ep005/world/derive.py → episodes/ep005/work/world-data/derived.json (KHÔNG commit: dẫn xuất từ chuỗi FRED/Freddie Mac)
                                         + episodes/ep005/world/claims.json (chỉ claim hiển thị, từ out/model.json)
Như moc-v/seg/ep005/derive.py (E5k), thêm: cột phát lại (mỗi tháng mua tập B: tháng tới 80 % trên giấy, lịch 80 % ở lãi tháng đó),
tập A ở 24 tháng (B_24 / chỉ số), chỉ số giá quốc gia theo tháng mua (chuẩn hoá), lịch dư nợ của khoản minh hoạ (0→120) và 3 người mua."""
import importlib.util, json, os, statistics
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('m5', os.path.join(EP, 'model/model.py')); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
hpi = M.load('HPIPONM226N'); wk = M.load('MORTGAGE30US'); rate, complete, _ = M.monthly_rates(wk)
r, A, B, hit, l24, ltv, first_hit = M.run(hpi, rate)
model = json.load(open(os.path.join(EP, 'out/model.json'))); raw = model['raw']
assert r['medianB_months_to80'] == raw['medianB_months_to80'] and r['maxB_months_to80'] == raw['maxB_months_to80'] and r['nB'] == raw['nB']
rl = raw['rate_latest']
sched = [M.balance(rl, k) for k in range(0, 121)]
paths = []
for s in B:
    n = min(hit[s], 120)
    paths.append({'m': s, 'hit': hit[s], 'p': [round(ltv(s, k), 4) for k in range(0, n + 1)]})
med = statistics.median([p['hit'] for p in paths])
typ = min((p for p in paths if p['hit'] == med), key=lambda p: abs(int(p['m'][:4]) - 2014))
slow = max(paths, key=lambda p: p['hit'])
months = sorted(hpi)
bars = [{'m': s, 'hit': hit[s], 'sched': M.sched(rate[s], 0.8)} for s in B]
setA = [{'m': s, 'l24': round(l24[s], 4)} for s in A]
h0 = hpi[B[0]]
index = [{'m': m, 'v': round(hpi[m] / h0, 4)} for m in months if m >= B[0]]
buyers = {}
for key in ('owen', 'grace', 'victor'):
    m = raw[f'buyer_{key}_purchaseMonth']; i0 = months.index(m); n = hit[m] + 6
    buyers[key] = {'m': m, 'hit': hit[m], 'sched': raw[f'buyer_{key}_sched80Months'], 'rate': raw[f'buyer_{key}_rate'],
                   'paper': [round(ltv(m, k), 4) for k in range(0, n + 1)], 'sched_line': [round(M.balance(rate[m], k), 4) for k in range(0, n + 1)],
                   'index': [round(hpi[months[i0 + k]] / hpi[m], 4) for k in range(0, n + 1)]}
os.makedirs(os.path.join(EP, 'work/world-data'), exist_ok=True)
json.dump({'sched': [round(x, 4) for x in sched], 'paths': paths, 'typical': typ['m'], 'slow': slow['m'], 'sched80': raw['sched80_months_latest'],
           'sched78': raw['sched78_months_latest'], 'bars': bars, 'setA': setA, 'index': index, 'buyers': buyers},
          open(os.path.join(EP, 'work/world-data/derived.json'), 'w'))
keep = ['sched80_months_latest', 'sched78_months_latest', 'ex_sched80_years', 'medianB_months_to80', 'maxB_months_to80', 'minB_months_to80', 'nB', 'nA',
        'shareB_over60', 'shareB_le_sched80', 'shareA_ltv24_le75', 'shareA_ltv24_le80', 'ex_payment_pi', 'rate_latest', 'ex_price', 'ex_loan',
        'value_removal_ltv_early', 'value_removal_seasoning_years', 'maxB_start']
cl = {k: {'value': raw[k], 'display': model['rounded'].get(k)} for k in keep if k in raw}
cl['request_ltv'] = {'value': 0.8, 'display': '80%'}; cl['down_share'] = {'value': 0.1, 'display': '10%'}; cl['twenty'] = {'value': 0.2, 'display': '20%'}
cl['start_ltv'] = {'value': 0.9, 'display': '90%'}
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1)
print('B', len(paths), 'median', med, typ['m'], 'slow', slow['m'], slow['hit'], 'sched80', raw['sched80_months_latest'], 'rate', rl, 'A', len(setA))

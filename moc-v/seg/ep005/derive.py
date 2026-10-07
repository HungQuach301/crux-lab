"""Mốc V · đoạn (b) Tập 5 — dẫn xuất dữ liệu hình từ BẢN SAO mô hình ep005 (moc-v/work/ep005-copy; không sửa episodes/ep005/).
  python3 moc-v/seg/ep005/derive.py   → moc-v/work/ep005-data/derived.json (không commit: dẫn xuất từ chuỗi FRED/Freddie Mac)
               + moc-v/seg/ep005/claims.json (chỉ claim hiển thị, từ out/model.json đã khớp nhánh ep005)
Đường: (1) lịch trả nợ của khoản minh hoạ ở lãi tháng mới nhất: dư nợ ÷ giá mua, tháng 0→120; (2) 'trên giấy' cho mọi tháng mua tập B
(1991-01 → 2016-07): dư nợ ÷ giá trị theo chỉ số giá nhà quốc gia, tháng 0 → lúc chạm 80 % (cắt ở 120); đánh dấu tháng trung vị và chậm nhất."""
import importlib.util, json, os, statistics, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CP = os.path.join(ROOT, 'moc-v/work/ep005-copy/episodes/ep005')
spec = importlib.util.spec_from_file_location('m5', os.path.join(CP, 'model/model.py')); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
hpi = M.load('HPIPONM226N'); wk = M.load('MORTGAGE30US'); rate, complete, _ = M.monthly_rates(wk)
r, A, B, hit, l24, ltv, first_hit = M.run(hpi, rate)
model = json.load(open(os.path.join(CP, 'out/model.json')))
raw = model['raw']
assert r['medianB_months_to80'] == raw['medianB_months_to80'] and r['maxB_months_to80'] == raw['maxB_months_to80']
rl = raw['rate_latest']
sched = [M.balance(rl, k) for k in range(0, 121)]
paths = []
for s in B:
    h = hit[s]; n = min(h, 120)
    paths.append({'m': s, 'hit': h, 'p': [round(ltv(s, k), 4) for k in range(0, n + 1)]})
med = statistics.median([p['hit'] for p in paths])
typ = min((p for p in paths if p['hit'] == med), key=lambda p: abs(int(p['m'][:4]) - 2014))   # cùng trung vị; ưu tiên gần Grace (2014)
slow = max(paths, key=lambda p: p['hit'])
os.makedirs(os.path.join(ROOT, 'moc-v/work/ep005-data'), exist_ok=True)
json.dump({'sched': [round(x, 4) for x in sched], 'paths': paths, 'typical': typ['m'], 'slow': slow['m'], 'sched80': raw['sched80_months_latest']},
          open(os.path.join(ROOT, 'moc-v/work/ep005-data/derived.json'), 'w'))
keep = {'sched80_months_latest': None, 'ex_sched80_years': None, 'medianB_months_to80': None, 'maxB_months_to80': None, 'nB': None}
cl = {k: {'value': raw[k], 'display': model['rounded'].get(k)} for k in keep}
cl['request_ltv'] = {'value': 0.8, 'display': '80%'}; cl['down_share'] = {'value': 0.1, 'display': '10%'}; cl['twenty'] = {'value': 0.2, 'display': '20%'}
cl['start_ltv'] = {'value': 0.9, 'display': '90%'}
json.dump(cl, open(os.path.join(ROOT, 'moc-v/seg/ep005/claims.json'), 'w'), indent=1)
print('B', len(paths), 'median', med, typ['m'], 'slow', slow['m'], slow['hit'], 'sched80', raw['sched80_months_latest'], 'rate', rl)

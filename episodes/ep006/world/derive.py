"""Tập 6 · dữ liệu hình cho các đoạn thế giới 3D (C3, N1 hàng 10 thùng), dẫn xuất từ model/model.py của tập (không sửa mô hình).
  python3 episodes/ep006/world/derive.py → episodes/ep006/world/claims.json
claims.json = (a) claim hiển thị {value, display} chép từ out/model.json + numbers.md (display = chuỗi đúng như trên hình);
(b) đường sức mua theo năm k = 0..20 của khoản tăng 2 % (% so khoản đầu) cho Ruth (2006-08), Carl (1966-01), Edna (1949-01):
100·1,02^k / (I(s+12k)/I(s)) — định nghĩa ở model.py; chỉ là tỉ số (không chép chuỗi FRED). Kiểm: Ruth = guide_path, cuối Carl = worst_*,
Edna ≥ 100 ở năm 20 (kept_up_last_start_20y)."""
import importlib.util, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('m6', os.path.join(EP, 'model/model.py')); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
I = M.load(M.PARAMS['index']['file'])
model = json.load(open(os.path.join(EP, 'out/model.json'))); raw, rnd = model['raw'], model['rounded']


def path(s):
    return [round(100 * 1.02 ** k / (I[M.addm(s, 12 * k)] / I[s]), 3) for k in range(21)]


ruth, carl, edna = path(raw['guide_start']), path(raw['worst_window_start_20y']), path(raw['kept_up_last_start_20y'])
assert all(abs(a - b['real_2pct_pct']) < 1e-3 for a, b in zip(ruth, raw['guide_path']))
assert abs(carl[-1] - raw['worst_real_value_2pct_payment_after_20y_pct']) < 1e-3 and abs(ruth[-1] - raw['guide_real_2pct_end_pct']) < 1e-3
assert edna[-1] >= 100 and all(b < a for a, b in zip(carl, carl[1:])) and raw['worst_window_years_2pct_fell_20y'] == 20
keep = ['guide_real_2pct_end_pct', 'latest_window_real_value_2pct_payment_pct', 'worst_real_value_2pct_payment_after_20y_pct', 'raise_needed_all_20y_pct',
        'worst_window_start_year_20y', 'worst_window_years_2pct_fell_20y', 'guide_years_2pct_at_or_above_100', 'kept_up_last_start_20y',
        'windows_2pct_kept_up_20y', 'guide_start', 'two_pct_growth_20y_pct', 'windows_20y', 'guide_last_year_2pct_at_or_above_100']
cl = {k: {'value': raw[k], 'rounded': rnd.get(k)} for k in keep}
# chuỗi hiển thị trên hình (numbers.md, cột Hiển thị); mọi số trên hình đi qua đây
disp = {'guide_real_2pct_end_pct': '90.4%', 'latest_window_real_value_2pct_payment_pct': 'about 9 in 10', 'worst_real_value_2pct_payment_after_20y_pct': '43.1%',
        'raise_needed_all_20y_pct': '6.38% a year', 'worst_window_start_year_20y': 'Jan 1966', 'worst_window_years_2pct_fell_20y': '20 of 20',
        'guide_years_2pct_at_or_above_100': 'early years', 'kept_up_last_start_20y': 'Jan 1949', 'windows_2pct_kept_up_20y': '17',
        'guide_start': 'Aug 2006', 'two_pct_growth_20y_pct': '2%', 'windows_20y': '20', 'guide_last_year_2pct_at_or_above_100': '15'}
for k, v in disp.items(): cl[k]['display'] = v
cl['paths'] = {'ruth': ruth, 'carl': carl, 'edna': edna, 'start': {'ruth': raw['guide_start'][:7], 'carl': raw['worst_window_start_20y'][:7], 'edna': raw['kept_up_last_start_20y'][:7]}}
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1)
print('ruth', ruth[-1], 'carl', carl[-1], 'edna', edna[-1], 'edna max', max(edna), edna.index(max(edna)))

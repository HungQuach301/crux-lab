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

# C4 (cả tập): lưới phát lại (V1/V2) cho đoạn d — mỗi ô = một tháng bắt đầu, giá trị = sức mua của khoản tăng 2 % sau H năm (% khoản đầu);
# đường theo năm của ô (điển hình, S16/S17) và độ vững (CPI-W, PCE). Chỉ tỉ số, không chép chuỗi chỉ số. Ghi episodes/ep006/world/grid.json.
G = 1.02
def grid(J, H, first='1947-01-01'):
    return [[s[:7], round(100 * G ** H / P, 3)] for s, e, P in M.windows(J, H, first)]
g20, g25 = grid(I, 20), grid(I, 25)
CW, PC = M.load(M.PARAMS['robust']['cpiw']['file']), M.load(M.PARAMS['robust']['pce']['file'])
gw, gp = grid(CW, 20), grid(PC, 20)
assert len(g20) == raw['windows_20y'] and sum(v >= 100 for _, v in g20) == raw['windows_2pct_kept_up_20y']
assert len(g25) == raw['windows_25y'] and sum(v >= 100 for _, v in g25) == raw['windows_2pct_kept_up_25y']
assert sum(v >= 100 for _, v in gw) == raw['robust_cpiw_kept_up_20y'] and sum(v >= 100 for _, v in gp) == raw['robust_pce_kept_up_20y']
assert all(abs(a[1] - round(b['real_2pct_pct'], 3)) < 1e-9 for a, b in zip(g20, raw['windows']))
# đường mức (khoản đều) của cửa sổ trung vị theo năm: k = 0..20, 100/(I(s+12k)/I(s)) — S17 "about year 8"
med = sorted(raw['windows'], key=lambda w: w['real_2pct_pct'])[len(raw['windows']) // 2]
lvl = [round(100 / (I[M.addm(med['start'], 12 * k)] / I[med['start']]), 3) for k in range(21)]
r2p = [round(100 * G ** k / (I[M.addm(med['start'], 12 * k)] / I[med['start']]), 3) for k in range(21)]
gl = [round(r['real_level_pct'], 3) for r in raw['guide_path']]
json.dump({'_about': 'derive.py (C4): % of the first check after H years, per start month (YYYY-MM); kept up = value >= 100',
           'cpiu20': g20, 'cpiu25': g25, 'cpiw20': gw, 'pce20': gp, 'ruth_level': gl,
           'median_window': {'start': med['start'][:7], 'rising': r2p, 'level': lvl},
           'raise_grid': raw['raise_grid'], 'by_decade': raw['by_decade']}, open(os.path.join(HERE, 'grid.json'), 'w'))
print('grid', len(g20), len(g25), len(gw), len(gp), 'median window', med['start'][:7], r2p[-1])

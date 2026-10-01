"""Tập 2 — sinh contract.json (hợp đồng tập, checks/CONTRACT.md; khoá K3.5 bd1948d9). Phần chưa chốt ghi trong `todo`.
python3 episodes/ep002/contract_build.py"""
import json, os
EP = os.path.dirname(os.path.abspath(__file__))
SPREADS = json.load(open(os.path.join(EP, 'out/model.json')))['sensitivity']
params = {
    'index': {'file': 'data/normalized/tb3ms_monthly.csv', 'dateColumn': 'month', 'valueColumn': 'rate'},
    'principal': 50000, 'termMonths': 120, 'fixedRate': 9.0, 'floatStartRate': 7.5, 'firstStart': '1954-01',
    'indexFloor': 0.0, 'periodBreaks': ['1981-01'], 'spreads': [float(s) for s in SPREADS],
}
# claim của tập -> khoá S05 (K3.5). Tỉ lệ trong claims.json ghi CHƯA làm tròn (dung sai 0,005).
mclaims = {
    'n_starts': 'nWindows', 'fixed_int': 'fixedTotalInterest', 'share_all': 'shareCostlier',
    'median_diff': 'medianDifference', 'worst_diff': 'worstDifference', 'best_diff': 'bestDifference',
    'max_rate_any': 'maxRate', 'max_payment': 'maxPayment', 'fixed_payment': 'fixedPayment',
    'index_today': 'indexToday', 'margin': 'margin',
    'worst_start_year': 'worstStartYear', 'worst_start_month': 'worstStartMonth',
    'best_start_year': 'bestStartYear', 'best_start_month': 'bestStartMonth',
    'n_early': 'nWindows:1954-01', 'n_late': 'nWindows:1981-01',
    'share_early': 'shareCostlier:1954-01', 'share_late': 'shareCostlier:1981-01',
}
for s in SPREADS:
    t = s.replace('-', 'm').replace('.', '')
    mclaims[f'spread{t}_share'] = f'shareCostlierAtSpread:{s}'
c = {
    'episode': 'ep002',
    'lock': 'bd1948d9a3c90dbcc356fcfbd9db4c57a362d0c769f8c4deb180e5d52d377fef (K3.5)',
    'question': 'How much lower does a variable rate have to start than a fixed rate before the risk has been worth it in history?',
    'targetDurationSec': [480, 900],
    'characters': {'note': 'TODO C2/C3: nhân vật (WRITER) + màu/hình (C3, qua mô phỏng protan/deutan)'},
    'claims': {'file': 'out/claims.json', 'core': ['share_early', 'share_late', 'worst_diff'], 'decisive': ['share_early', 'share_late', 'worst_diff'],
               'illustrative': 'TODO: sinh từ out/claims.json (illustrative:true) ở C2',
               'assumptions': [
                   {'id': 'illustrative-offers', 'pattern': 'illustrative', 'what': '7.5% variable / 9% fixed is an illustrative pair'},
                   {'id': 'tbill-index', 'pattern': 'treasury bill|t-bill', 'what': '3-month T-bill stands in for the lender index (SOFR-type)'},
                   {'id': 'no-cap', 'pattern': 'no cap|no rate cap|uncapped', 'what': 'no rate cap in the main replay'},
                   {'id': 'repay-now', 'pattern': 'repayment starts|no deferment', 'what': 'repayment starts at once; no deferment, fees, discounts'}]},
    'model': {'kind': 'float-vs-fixed-replay', 'output': 'out/model.json', 'code': 'model/model.py', 'params': params,
              'claims': mclaims},
    'data': {'sources': 'data/sources.json', 'hosts': {'primary': ['fred.stlouisfed.org'], 'crosscheck': ['fred.stlouisfed.org']},
             'crosscheck': [{'series': 'tb3ms', 'tolerance': 0.05, 'used': 'crosscheck',
                             'primary': {'file': 'data/normalized/tb3ms_monthly.csv', 'key': 'month', 'column': 'rate'},
                             'crosscheck': {'file': 'data/normalized/dtb3_monthly_mean.csv', 'key': 'month', 'column': 'rate'},
                             'what': 'TB3MS (monthly) vs mean of daily DTB3 (H.15), every month 1954-01..2026-08'}],
             'fetch': 'python3 episodes/ep002/data/fetch.py --verify (FRED files are not committed: amendments.md E2-A1)'},
    'coverage': [{'attribute': 'case', 'act': 'TODO', 'values': ['period-1954-1980', 'period-1981-on', 'worst-1977-04'],
                  'what': 'gen của tập: luôn hiện cả hai thời kỳ cùng trường hợp xấu nhất'}],
    'sonification': {'stem': 'sonify', 'bandsHz': 'TODO C3 (bảng âm S2 Tập 1, Q1=A)'},
    'artefacts': {'M3': 'TODO C5'},
    'todo': ['characters (C2/C3)', 'coverage.act (C2)', 'claims.illustrative list (C2)', 'sonification.bandsHz (C3)', 'artefacts (C5)',
             'claims chưa có khoá K3.5 → checks-notes.md (sau C2, K3.6)'],
}
json.dump(c, open(os.path.join(EP, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
print('contract ok', len(mclaims), 'model claims')

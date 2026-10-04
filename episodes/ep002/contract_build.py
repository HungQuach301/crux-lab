"""Tập 2 — sinh contract.json (hợp đồng tập, checks/CONTRACT.md; khoá K3.5 bd1948d9). Phần chưa chốt ghi trong `todo`.
python3 episodes/ep002/contract_build.py"""
import json, os
EP = os.path.dirname(os.path.abspath(__file__))
ILLUS = [c['claimId'] for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims'] if c.get('illustrative')]
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
# K3.6 (LOCK 2fcc9fcc): khoá cho các claim kịch bản trước đây chưa có khoá
mclaims.update({
    'first_start': 'firstStart', 'last_start': 'lastStart', 'worst_start': 'worstStart', 'best_start': 'bestStart',
    'var_first_payment': 'floatFirstPayment', 'first_payment_gap': 'firstPaymentGap',
    'worst_peak_rate': 'worstWindowMaxRate', 'share_rate_above_fixed': 'shareRateAboveFixed', 'worst_share_of_fixed': 'worstShareOfFixed',
    'min_gap_early': 'minShareCostlierOverSpreads:1954-01',
    'gap_worst_start_all': 'worstStartAtSpread:1.5',   # chỉ một khoảng chênh có khoá; K3.6 tự xác nhận 1977-04 ở cả 15 (ledger)
})
for g in ('-1', '-0.5', '0', '0.5', '1', '1.5', '2', '2.5', '3'):
    t = ('m' + g[1:] if g.startswith('-') else g).replace('.', '')
    t = {'m1': 'm10', 'm05': 'm05', '0': '00', '05': '05', '1': '10', '15': '15', '2': '20', '25': '25', '3': '30'}[t]
    mclaims[f'gap{t}_early'] = f'shareCostlierAtSpread:{g}:1954-01'
    mclaims[f'gap{t}_late'] = f'shareCostlierAtSpread:{g}:1981-01'
    mclaims[f'gap{t}_worst'] = f'worstDifferenceAtSpread:{g}'
for s in SPREADS:
    t = s.replace('-', 'm').replace('.', '')
    mclaims[f'spread{t}_share'] = f'shareCostlierAtSpread:{s}'
c = {
    'episode': 'ep002',
    'lock': '2fcc9fcc9a94b73084c43ba59970d88f539cd29363334faf52b0640efc2cc801 (K3.6)',
    'question': 'How much lower does a variable rate have to start than a fixed rate before the risk has been worth it in history?',
    'targetDurationSec': [480, 900],
    'characters': {'leah': {'color': 'ink', 'shape': 'diamond', 'side': 'centre', 'illustrative': True, 'words': ['Leah'],
                            'what': 'ILLUSTRATIVE: a graduate student with two private offers, 9% fixed or variable starting at 7.5%, $50,000 over 10 years '
                                    '(not a real lender\'s offer); the only character',
                            'wordsFrom': 'story/script.md v5 (out/script.json): "Leah" in S01-S12',
                            'designFrom': 'design/c3/final/system.md + tokens.json roles.leah: ink + DIAMOND (bead at the head of her rate path; diamond cut-out on the person figure)'}},
    'claims': {'file': 'out/claims.json', 'core': ['share_early', 'share_late', 'worst_diff'], 'decisive': ['share_early', 'share_late', 'worst_diff'],
               'illustrative': ILLUS,
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
    'coverage': [{'attribute': 'case', 'act': 'act3', 'values': ['period-1954-1980', 'period-1981-on', 'worst-1977-04'],
                  'what': 'gen của tập: luôn hiện cả hai thời kỳ cùng trường hợp xấu nhất',
                  'where': 'act3 = S09-S10 (out/timeline.json): the two columns of KEY-7 (before 1981 / from 1981) at every head start, and the April 1977 '
                           'marker (S10.2 "April 1977", gap_worst_start_all); page objects of each column carry case = period-1954-1980 / period-1981-on, '
                           'the worst marker case = worst-1977-04 (window.CHECKS objects, stream P)'}],
    'sonification': {'stem': 'sonify', 'bandsHz': [[60, 270], [4500, 7000]],
                     'from': 'palette S2 of Tập 1 (Q1=A; sổ gu G-005): low pulse MIDI 36-60 (65-262 Hz) + filtered tick 4.5-7 kHz; stream A C5: '
                             'out/sonify-events.json "_about" (values -> MIDI 36..60, palette S2 as Tập 1) = SON_BANDS of episodes/ep001/work/audio/src/mix.py',
                     'todo': 'T1 measures that these bands hold >= 50% of the sonify stem energy once stream A renders the stem'},
    'artefacts': {
        'M1': ['out/claims.json', 'out/model.json', 'story/script.md', 'story/beats.md', 'numbers.md', 'contract.json', 'data/sources.json',
               'design/c3/final/tokens.json', 'animatic/timing.json'],
        'M2': ['out/script.json', 'out/timeline.json', 'out/voice/takes.json', 'out/page.json', 'out/camera.json', 'out/cues.json', 'out/tempo-map.json',
               'out/transitions.json', 'out/sonify-events.json', 'out/sfx-events.json'],
        'M3': ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/timeline.json', 'out/script.json', 'out/claims.json',
               'out/audio/stems/voice.*', 'out/audio/stems/music.*', 'out/audio/stems/sfx.*', 'out/audio/stems/whoosh.*', 'out/audio/stems/room.*',
               'out/audio/stems/sonify.*', 'out/voice/takes.json', 'out/camera.json', 'out/sfx-events.json', 'out/sonify-events.json',
               'out/tempo-map.json', 'out/transitions.json', 'out/cues.json', 'out/tension-map.json', 'out/tension-map.png', 'out/adbreaks.json',
               'preprod/shotlist.json', 'preprod/storyboard.*', 'preprod/color-script.*', 'design/tokens.json',
               'out/package/thumb-1.png', 'out/package/thumb-2.png', 'out/package/thumb-3.png',
               'out/package/thumb-1.json', 'out/package/thumb-2.json', 'out/package/thumb-3.json', 'out/page.json', 'out/model.json',
               'data/sources.json', 'data/normalized/tb3ms_monthly.csv', 'data/normalized/dtb3_monthly_mean.csv', 'contract.json',
               'out/rights.json', 'out/visual-assets.json'],
        'note': 'thumbnails are C6 (Q2=A): F11 reports them not delivered until then; data/normalized/*.csv are not committed (fetch.py --verify)'},
    'rights': {'visual': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter',
                           'paths': ['fonts/inter-latin-*-normal.woff2', '../../toolkit/render/fonts/inter-latin-*-normal.woff2']}],
               'generated': [],
               'note': 'the render page (animatic/src/page.html, P) loads no image, PDF, 3D model or texture: every picture is canvas 2D from project code; '
                       'fonts by @font-face from toolkit/render/fonts (served at /fonts/). Ledger: out/rights.json (preprod/rights_c5.py); '
                       'manifest: out/visual-assets.json'},
    'timeline': {'source': 'out/timeline.json (preprod/dossier_c5.py; sentence times animatic/timing.json)',
                 'acts': 'cold-open S01 · act1 S02-S05 · act2 S06-S08 · act3 S09-S10 · method S11 · outro S12-S13',
                 'climax': {'act1': 'S05.4', 'act2': 'S08.7', 'act3': 'S10.6'}, 'adBreaks': 'out/adbreaks.json (act2 and act3 starts)'},
    'todo': ['coverage: KEY-7 columns and the April 1977 marker must carry case = period-1954-1980 / period-1981-on / worst-1977-04 on the page (P)',
             'sonification.bandsHz: T1 checks the >= 50% energy share on the rendered sonify stem (A)',
             'artefacts.M3: thumbnails at C6',
             'claims chưa dùng trong kịch bản (cap*, median_max_payment, share_payment_above_fixed) không có khoá — không cần'],
}
json.dump(c, open(os.path.join(EP, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
print('contract ok', len(mclaims), 'model claims')

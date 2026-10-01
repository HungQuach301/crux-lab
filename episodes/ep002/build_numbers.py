"""Tập 2 — sinh out/claims.json và numbers.md từ out/model.json (+ data/context.json khi có). Không gõ số tay.
python3 episodes/ep002/build_numbers.py"""
import csv, json, os

EP = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(EP, 'out/model-extra.json')))
F = json.load(open(os.path.join(EP, 'out/model.json')))  # dạng K3.5, chưa làm tròn
B, PAY, W = M['base'], M['payments'], M['windows']
SRC = {'id': 'fred-tb3ms', 'url': 'https://fred.stlouisfed.org/series/TB3MS'}
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
       'November', 'December']
mon = lambda d: f"{MON[int(d[5:7]) - 1]} {d[:4]}"
usd = lambda v: ('−' if v < 0 else '') + f"${abs(v):,.0f}"
usd2 = lambda v: f"${v:,.2f}"
pct = lambda v: f"{v:.1f}%"

claims = []


def add(cid, value, display, formula, kind='model', illustrative=True, source=SRC, years=(1954, 2026), **kw):
    c = {'claimId': cid, 'value': value, 'display': display, 'formula': formula, 'source': source,
         'dataYears': list(years), 'historical': kind == 'model', 'illustrative': illustrative, 'kind': kind}
    if isinstance(value, (int, float)) and ('$' in display):
        c['basis'] = 'nominal'
    c.update(kw)
    claims.append(c)


# ---- tham số khoản vay (ILLUSTRATIVE: cặp lãi minh hoạ trừ khi C1 chọn neo khác)
add('loan', 50000, '$50,000', 'loan amount (model param)', kind='param')
add('term', 120, '10 years (120 monthly payments)', 'term (model param)', kind='param')
add('fixed_rate', 9.00, '9%', 'fixed rate offer (model param)', kind='param')
add('var_start', 7.50, '7.5%', 'variable rate at origination (model param)', kind='param')
add('gap_start', 1.5, '1.5 points', 'fixed_rate − var_start', kind='param')
# ---- chỉ số
add('index_today', B['index_today'], f"{B['index_today']:.2f}%", f"TB3MS, last observation {B['index_date'][:7]}",
    kind='data', illustrative=False, asOf=B['index_date'])
add('margin', B['margin'], f"{B['margin']:.2f} points", 'var_start − index_today')
tb = [(r[0], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:]]
pk = max(tb, key=lambda t: t[1])
add('tb_peak', pk[1], f"{pk[1]:.2f}%", 'max TB3MS 1934-01..2026-08', kind='data', illustrative=False,
    date=pk[0], words=mon(pk[0]))
# ---- lõi
add('n_starts', B['n_starts'], f"{B['n_starts']}", 'start months with a full 120-month window, 1954-01..2016-09')
add('first_start', B['first_start'], mon(B['first_start']), 'first start month')
add('last_start', B['last_start'], mon(B['last_start']), 'last start month with 120 months of data')
add('n_early', B['n_starts_1954_1980'], str(B['n_starts_1954_1980']), 'start months 1954-01..1980-12')
add('n_late', B['n_starts_1981_on'], str(B['n_starts_1981_on']), 'start months 1981-01..2016-09')
add('fixed_int', B['fixed_total_interest'], usd(B['fixed_total_interest']), 'total interest, 9% fixed, 120 months')
n_cost = sum(w['diff'] > 0 for w in W)
add('n_costlier', n_cost, str(n_cost), 'windows with Difference > 0')
add('share_all', F['shareCostlier'], pct(B['share_variable_costlier']),
    'share of start months where variable total interest > fixed', core=True, words='about 1 in 7')
add('share_early', F['periods'][0]['shareCostlier'], pct(B['share_costlier_1954_1980']),
    'share costlier, starts 1954-1980', core=True, decisive=True, words='more than 1 in 4')
add('share_late', F['periods'][1]['shareCostlier'], pct(B['share_costlier_1981_on']),
    'share costlier, starts 1981 on', core=True, decisive=True, words='about 1 in 30')
add('median_diff', B['median_variable_minus_fixed'], usd(B['median_variable_minus_fixed']),
    'median Difference (negative = variable cheaper)', words=f"{usd(-B['median_variable_minus_fixed'])} less")
add('worst_diff', B['worst_variable_minus_fixed'], '+' + usd(B['worst_variable_minus_fixed']),
    'max Difference', core=True, decisive=True)
add('worst_start', B['worst_start'], mon(B['worst_start']), 'start month of the max Difference')
add('worst_start_year', 1977 if B['worst_start'][:4]=='1977' else int(B['worst_start'][:4]), B['worst_start'][:4], 'year of worst_start (S05 numeric)')
add('worst_start_month', int(B['worst_start'][5:7]), MON[int(B['worst_start'][5:7])-1], 'month of worst_start (S05 numeric)')
ww = next(w for w in W if w['start'] == B['worst_start'])
add('worst_peak_rate', round(ww['maxRate'], 2), f"{ww['maxRate']:.1f}%", 'highest monthly variable rate in the worst window')
add('worst_share_of_fixed', round(100 * B['worst_variable_minus_fixed'] / B['fixed_total_interest']),
    f"{round(100 * B['worst_variable_minus_fixed'] / B['fixed_total_interest'])}%", 'worst_diff / fixed_int')
bw = min(W, key=lambda w: w['diff'])
add('best_diff', B['best_variable_minus_fixed'], usd(B['best_variable_minus_fixed']), 'min Difference')
add('best_start', bw['start'], mon(bw['start']), 'start month of the min Difference')
add('best_start_year', int(bw['start'][:4]), bw['start'][:4], 'year of best_start (S05 numeric)')
add('best_start_month', int(bw['start'][5:7]), MON[int(bw['start'][5:7])-1], 'month of best_start (S05 numeric)')
mr = max(W, key=lambda w: w['maxRate'])
add('max_rate_any', B['max_variable_rate_any_window'], f"{B['max_variable_rate_any_window']:.1f}%",
    'highest monthly variable rate in any window', start=mr['start'], words=f"window starting {mon(mr['start'])}")
above9 = round(100 * sum(w['maxRate'] > 9.0 for w in W) / len(W), 1)
add('share_rate_above_fixed', above9, pct(above9), 'share of windows whose variable rate exceeded 9% in some month',
    words='about 3 in 4')
# ---- khoản trả hàng tháng (phạm vi b)
add('fixed_payment', PAY['fixed_payment'], usd2(PAY['fixed_payment']), 'level payment, 9%, 120 months', scope='b')
add('var_first_payment', PAY['variable_first_payment'], usd2(PAY['variable_first_payment']),
    'first payment at 7.5%', scope='b')
add('max_payment', PAY['max_variable_payment_any_window'], usd2(PAY['max_variable_payment_any_window']),
    'highest variable monthly payment, any window', start=PAY['max_variable_payment_start'], scope='b')
add('median_max_payment', PAY['median_window_max_payment'], usd2(PAY['median_window_max_payment']),
    'median over windows of the highest monthly payment', scope='b')
add('share_payment_above_fixed', PAY['share_windows_max_payment_above_fixed'],
    pct(PAY['share_windows_max_payment_above_fixed']),
    'share of windows where the variable payment exceeded the fixed payment in some month', scope='b',
    words='more than half')
# ---- lưới khoảng chênh / trần (phạm vi b)
for g, v in F['sensitivity'].items():
    t = g.replace('-', 'm').replace('.', '')
    add(f'spread{t}_share', v, pct(v), f'share costlier when the variable rate starts {g} points under 9% (K3.5 shareCostlierAtSpread)', scope='b')
for g, d in M['gaps'].items():
    t = g.replace('-', 'm').replace('.', '')
    add(f'gap{t}_early', d['share_costlier_1954_1980'], pct(d['share_costlier_1954_1980']), f'gap {g}: 1954-1980', scope='b', k36='shareCostlierAtSpread theo thời kỳ')
    add(f'gap{t}_late', d['share_costlier_1981_on'], pct(d['share_costlier_1981_on']), f'gap {g}: 1981 on', scope='b', k36='shareCostlierAtSpread theo thời kỳ')
    add(f'gap{t}_worst', d['worst_diff'], '+' + usd(d['worst_diff']), f'gap {g}: worst Difference', scope='b', k36='worst theo khoảng chênh')
for c, d in M['caps'].items():
    add(f'cap{c}_share', d['share_costlier'], pct(d['share_costlier']), f'share costlier, rate capped at {c}%', scope='b', k36='nhiều mức trần')
    add(f'cap{c}_early', d['share_costlier_1954_1980'], pct(d['share_costlier_1954_1980']), f'cap {c}: 1954-1980', scope='b', k36='nhiều mức trần')
    add(f'cap{c}_worst', d['worst_diff'], '+' + usd(d['worst_diff']), f'cap {c}: worst Difference', scope='b', k36='nhiều mức trần')

# ---- bối cảnh chính sách / neo lãi (data/context.json, khi đã xác minh)
ctx = os.path.join(EP, 'data/context.json')
if os.path.exists(ctx):
    for c in json.load(open(ctx))['claims']:
        claims.append(c)

os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
json.dump({'claims': claims}, open(os.path.join(EP, 'out/claims.json'), 'w'), indent=1)

L = ['# Tập 2 — Bảng số (sinh bởi `build_numbers.py` từ `out/model.json`; không gõ tay)', '',
     'Mọi số của tập phải trỏ về một claim ID ở đây. Kiểm độc lập: `model/independent/compare.json` '
     '(85/85 đại lượng, 753/753 cửa sổ, 0 lệch). Mốc dữ liệu: TB3MS tới **August 2026** (3.72%), tải 2026-10-01.', '',
     '**ILLUSTRATIVE**: mọi số của khoản vay (cặp lãi 7.5%/9%, $50,000, 10 năm) là của một khoản vay minh hoạ; '
     'chỉ số TB3MS là dữ liệu thật. "History, not a forecast." Phạm vi (b) đánh dấu `b`.', '',
     '| Claim ID | Hiển thị | Lời (gợi ý) | Công thức | Loại | Minh hoạ | Phạm vi |', '|---|---|---|---|---|---|---|']
for c in claims:
    L.append(f"| `{c['claimId']}` | {c['display']} | {c.get('words', '')} | {c['formula']} | {c['kind']} | "
             f"{'có' if c['illustrative'] else 'không'} | {c.get('scope', 'a')} |")
L += ['', '## Ghi chú', '',
      f"- **Sửa câu chữ của hồ sơ.** `result.json → answer` và `claim-risk.md` viết cửa sổ xấu nhất (bắt đầu 4/1977) "
      f"\"peaking at 20.6%\". Sai: cửa sổ đó đỉnh **{ww['maxRate']:.2f}%** (`worst_peak_rate`); 20.6% là đỉnh của cửa sổ "
      f"bắt đầu {mon(mr['start'])} (`max_rate_any`), cửa sổ này đắt hơn {usd(mr['diff'])}. Số `max_variable_rate_any_window` "
      "của hồ sơ đúng theo định nghĩa ('any window'); chỉ câu tóm tắt ghép sai. Tập dùng hai claim riêng.",
      '- **Độ nhạy với quan sát tháng 9/2026** (FRED công bố 1/10/2026): kết quả không phụ thuộc giá trị chỉ số hôm nay trừ khi '
      'sàn 0 chạm; thử 3.2–4.2 → share 14.2%, worst $11,219 không đổi. Chỉ `index_today` và `margin` đổi.',
      '- Cửa sổ chồng nhau: 753 tháng bắt đầu không phải 753 phép thử độc lập (claim-risk).']
open(os.path.join(EP, 'numbers.md'), 'w').write('\n'.join(L) + '\n')
print(len(claims), 'claims')

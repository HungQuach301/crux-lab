"""Tập 8: sinh numbers.md từ out/model.json (claim ID = khoá quantities).  python3 episodes/ep008/model/numbers_md.py"""
import json, os

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = json.load(open(os.path.join(EP, 'out', 'model.json')))['quantities']
v = lambda k: q[k]['value']

HEAD = """# Claim — Tập 8 (Việc 0; claim ID = khoá `quantities` của `out/model.json`)

Dữ liệu (FRED, tải 2026-10-13, `data/fetch.py`; không commit): HPIPONM226N (FHFA, đến 2026-07), CUUR0000SEHA (BLS CPI tiền thuê, đến 2026-08; 2025-10 trống → trung bình nhân), MORTGAGE30US (Freddie Mac PMMS tuần, đến 2026-10-08), TB3MS (đến 2026-09). **Bản ghim hồ sơ: 4/4 SHA khớp**, bản mới = bản ghim (không quan sát mới). calc.py hồ sơ 11/11 câu True, `result.json` tái tạo trùng. `model/model.py` (viết lại từ định nghĩa, không gọi calc.py): **76/76 trùng `result.json`**. Kiểm độc lập (headless Sonnet khoá Console, chỉ đọc data/raw + định nghĩa, `model/independent/`): **49/49 dòng so được trùng**; một khác định nghĩa (không phải lệch số): `worst_price_change` đầu bài kiểm hỏi "nhỏ nhất mọi cửa sổ" (0,6 %, 2/2006), mô hình là "của cửa sổ tệ nhất" (3,2 %, 6/2006) → lời chỉ dùng nghĩa sau.

**Tỉ lệ tiền thuê/giá nhà — điều kiện G1 lô (chủ dự án): ĐẠT cả hai vế.** (1) Nguồn công khai: Census Housing Vacancy Survey (phạm vi công cộng chính phủ Mỹ) — giá thuê hỏi trung vị nhà trống cho thuê × 12 / giá bán hỏi trung vị nhà trống để bán: Q4 2025 $1,464 / $363,800 → **4,83 %/năm**; Q1 2026 $1,579 / $339,100 → **5,59 %/năm** (bản tin `census.gov/housing/hvs/files/qtr425/Q425press.pdf`, `qtr126/Q126press.pdf`, đọc qua đoạn trích WebSearch 13/10 — census.gov bị mạng phiên chặn: **cần mở PDF xác minh trước C4**). Giả định hồ sơ 5 % nằm trong dải. Hai rổ nhà trống khác nhau (nhà thuê thường nhỏ hơn nhà bán) → chỉ là dải đối chiếu, không phải tỉ lệ của một căn. (2) Độ nhạy: quét 3,0–7,0 % (`out/model.json → sweep`): người mua hơn ở 56,0 % (3 %) → 100 % (≥ 6,8 %); ở hai mốc Census **73,6 %** và **87,3 %**; đa số lật về người thuê chỉ khi tỉ lệ < **FLIP %** (`flip_yield_10y`) — dưới mọi mốc công khai. Câu nói được: "the share moves with the rent you assume; across the public range it stays above seven in ten" — không nói "buying wins".

**Luật nói (claim-risk hồ sơ + novelty 13/10):** không khuyên (mua/thuê); không dự báo — "history, not a forecast"; "US only"; nhà = chỉ số FHFA quốc gia, không phải một căn; tiền thuê khởi đầu là GIẢ ĐỊNH (5 %/năm giá, neo 7/2026) kéo lùi theo CPI tiền thuê / chỉ số giá; CPI tiền thuê theo người đang thuê, chậm hơn giá thuê hỏi và **có thể đánh giá thấp tăng tiền thuê dài hạn** (Shertzer & Allison) → nói như giới hạn; quỹ người thuê để tiền mặt (biến thể T-bill), **không cổ phiếu** (câu hỏi khán giả 4 không trả); không thuế (khấu trừ lãi, miễn thuế lãi vốn), không tái cấp vốn, không phí chuyển nhà; nhân vật ILLUSTRATIVE; không nói tập là "first" (Beracha & Johnson 2012, FPA 2018 đã làm dạng học thuật).

| Claim ID | Giá trị | Hiển thị | Định nghĩa |
|---|---|---|---|"""

DISP = {
    'n_10y': '307 start months', 'first_10y': 'January 1991', 'last_10y': 'July 2016',
    'share_buyer_ahead_10y': 'about 3 in 4 (75.6%)', 'median_adv_10y': '$157,104 (about $157,000)',
    'best_start_10y': 'April 2012', 'best_adv_10y': '$483,975 (about $484,000)',
    'worst_start_10y': 'June 2006', 'worst_adv_10y': '$82,385 behind (about $82,000)',
    'n_renter_ahead_10y': '75 of 307', 'share_buyer_ahead_5y': '74.4%', 'worst_start_5y': 'May 2006',
    'worst_adv_5y': '$149,392 behind', 'n_15y': '247', 'share_buyer_ahead_15y': 'every one (100%)',
    'worst_adv_15y': '$79,829 ahead', 'era_1990s_share': 'every 1990s start (100%)',
    'era_2002-2007_n': '72', 'era_2002-2007_share': '6 of 72 (8.3%)', 'era_2009-2016_share': 'every start 2009 to mid-2016',
    'renter_first_10y': 'April 2001', 'renter_last_10y': 'December 2007',
    'worst_price_change_10y': 'up 3.2% in ten years', 'best_price_change_10y': 'up 114.3% (more than doubled)',
    'worst_rate_10y': '6.68%', 'best_rate_10y': '3.91%', 'worst_equity_10y': '$115,374', 'worst_pot_10y': '$197,760',
    'share_tbills_10y': '66.4% (about 2 in 3)', 'share_yield4pct_10y': '64.2%', 'share_yield6pct_10y': '92.2%',
    'hvs_yield_2025Q4': '4.83% a year', 'hvs_yield_2026Q1': '5.59% a year',
    'share_hvs_2025Q4_10y': '73.6%', 'share_hvs_2026Q1_10y': '87.3%', 'flip_yield_10y': 'below about 2.4%',
    'rate_month_latest': 'September 2026', 'rate_latest': '6.86% (September 2026 average)',
    'today_buyer_month1': '$2,933 a month', 'today_rent_month1': '$1,667 a month', 'today_rent_to_outlay': '56.8%',
    'rent_to_outlay_min_10y': '57.9%', 'rent_to_outlay_min_start_10y': 'July 2006',
    'price': '$400,000', 'yield_anchor_pct': '5% a year (assumption)',
}
rows = ['| `%s` | %s | %s | %s |' % (k, v(k), d, q[k]['definition']) for k, d in DISP.items()]
txt = HEAD.replace('FLIP', str(v('flip_yield_10y'))) + '\n' + '\n'.join(rows) + \
    '\n\nĐại lượng còn lại ở `out/model.json`; chỉ dòng trên được nói/hiện. Câu "today" so tháng đầu, **không phải dự báo** (claim-risk hồ sơ).\n'
open(os.path.join(EP, 'numbers.md'), 'w').write(txt)
print(len(rows), 'dòng claim')

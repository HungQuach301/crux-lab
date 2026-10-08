# Chạy thử hồi tố A25, A26 trên Tập 3–5 (08/10/2026) — CHỈ BÁO

Không sửa tập đã phát hành (cine-lab #57, Q-L23b: không sửa video đã đăng). Mã: `retro_a25_a26.py` (định nghĩa ở đầu tệp).

**Đọc:** A25 bắt 1 lỗi thật (Tập 3 `1954` trong phần nguồn của mô tả, không có claim) — đúng loại cine-lab #53. A26 sau khi bỏ tham số/luật còn 5 câu; Tập 3 S01.1 là dương giả (tuổi nhân vật minh hoạ), Tập 5 S20.2 (★) là phép so sánh có chủ ý giữa "lịch hôm nay" và "lịch sử" đã gọi tên hai thước — K cần luật ngoại lệ "gọi tên cả hai nguồn/kỳ" trước khi khoá. Lượt đầu tính cả tham số/luật: Tập 5 22 câu (nhiễu, đã bỏ).

| Tập | A25: số trong mô tả không có claim | A26: đơn vị ghép khác nguồn/kỳ (câu · khung) | A26 có từ so sánh |
|---|---|---|---|
| ep003 | 1 | 1 (1 · 0) | 0 |
| ep004 | 0 | 0 (0 · 0) | 0 |
| ep005 | 0 | 4 (4 · 0) | 1 |

## ep003

**A25** (1):
- dòng 14: `1954` — - Monthly average 3-month bill rate (secondary market, discount basis) from the Federal Reserve Board's H.15 r

**A26** (1; ★ = có từ so sánh):
- câu S01.1: viewer_age_decade, horizon_years · nguồn ['?', 'model'] · kỳ ['(1934, 2026)'] — "Dana is in her forties, and she has a chunk of savings she has promised herself she won't touch for 20 years."

## ep004

**A25** (0):

**A26** (0; ★ = có từ so sánh):

## ep005

**A25** (0):

**A26** (4; ★ = có từ so sánh):
- câu S10.2: nB, ex_extra_down_for_20 · nguồn ['model'] · kỳ ['(1991, 2026)', 'now'] — "For each one, we set up the same 10 percent down loan at that month's average rate."
- câu S12.3: nA, shareA_ltv24_le75, value_removal_ltv_early · nguồn ['model'] · kỳ ['(1991, 2026)', 'now'] — "Two years after purchase, only 15.6 percent of them were at or below the 75 percent bar Fannie Mae sets for its loans wh"
- câu S18.2: sched80_months_latest, medianB_months_to80 · nguồn ['model'] · kỳ ['(1991, 2026)', 'now'] — "So a plan can be measured against two benchmarks from this history."
- ★ câu S20.2: sched80_months_latest, minB_months_to80, maxB_months_to80, maxB_years · nguồn ['model'] · kỳ ['(1991, 2026)', 'now'] — "On the schedule, the answer is set the day the loan starts; on paper, history gave answers from about a year to more tha"

# Hai cách tính hoà vốn — bảng so sánh (Tập 1, M1b)

Kịch bản: vay tháng 10/2023 ở lãi trung bình tháng đó (7.62%), đã trả 35 kỳ, tái cấp vốn ở lãi tuần gần nhất (7.03%, tuần 2026-09-24); khoản vay mới 30 năm cho đúng dư nợ còn lại, phí đóng hồ sơ trả bằng tiền mặt. Maya, Dan, Priya: ILLUSTRATIVE, khoản vay và phí là trung vị HMDA 2025 theo quy mô.

- **Cách đơn giản** (cách phần lớn máy tính dùng): hoà vốn = phí ÷ số tiền trả hằng tháng giảm được.
- **Cách có chênh lệch dư nợ** (đáp án chính của tập): tháng đầu tiên mà (tiết kiệm cộng dồn + dư nợ khoản cũ − dư nợ khoản mới) ≥ phí. Khoản mới bắt đầu lại 30 năm nên trả gốc chậm hơn; khoản vay càng lâu năm thì chênh lệch càng lớn.

| Trường hợp | Khoản vay | Phí | Giảm mỗi tháng | Cách đơn giản (tháng) | Có dư nợ (tháng) | Bán sau 3 năm | Bán sau 7 năm | Mức giảm cần để hoà vốn ≤ 36 tháng |
|---|---|---|---|---|---|---|---|---|
| Maya (today, cut 0.59 pt) | $375,000 | $5,124 | $221 | 24 | **30** | $1,039 | $8,093 | 0.50 |
| Dan (today, cut 0.59 pt) | $115,000 | $3,667 | $68 | 55 | **75** | -$1,777 | $386 | 1.12 |
| Priya (today, cut 0.59 pt) | $1,005,000 | $5,034 | $593 | 9 | **11** | $11,482 | $30,387 | 0.20 |
| Maya, cut 0.25 pt | $375,000 | $5,124 | $137 | 38 | **never** |  |  |  |
| Maya, cut 0.5 pt | $375,000 | $5,124 | $199 | 26 | **36** |  |  |  |
| Maya, cut 0.75 pt | $375,000 | $5,124 | $260 | 20 | **23** |  |  |  |
| Maya, cut 1 pt | $375,000 | $5,124 | $321 | 16 | **18** |  |  |  |
| Maya, cut 1.5 pt | $375,000 | $5,124 | $440 | 12 | **12** |  |  |  |
| Maya, cut 2 pt | $375,000 | $5,124 | $556 | 10 | **9** |  |  |  |
| history 1974-10 -> refi 1975-03 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,775 | $240 | 20 | **18** |  |  |  |
| history 1980-04 -> refi 1980-05 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,785 | $496 | 10 | **10** |  |  |  |
| history 1981-10 -> refi 1981-12 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,785 | $369 | 13 | **13** |  |  |  |
| history 1984-07 -> refi 1984-11 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,783 | $247 | 20 | **19** |  |  |  |
| history 1987-10 -> refi 1988-02 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,779 | $311 | 16 | **14** |  |  |  |
| history 1989-04 -> refi 1989-07 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,781 | $264 | 19 | **17** |  |  |  |
| history 1994-12 -> refi 1995-05 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,773 | $271 | 18 | **16** |  |  |  |
| history 1996-06 -> refi 1997-10 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,735 | $235 | 21 | **19** |  |  |  |
| history 2000-05 -> refi 2000-12 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,765 | $245 | 20 | **17** |  |  |  |
| history 2006-07 -> refi 2008-01 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,708 | $224 | 21 | **20** |  |  |  |
| history 2013-09 -> refi 2016-07 (1 pt) * | $300,000 (ILLUSTRATIVE) | $4,557 | $245 | 19 | **19** |  |  |  |
| history 2018-11 -> refi 2019-06 (1 pt) | $300,000 (ILLUSTRATIVE) | $3,564 | $200 | 18 | **14** |  |  |  |
| history 2023-10 -> refi 2024-08 (1 pt) | $300,000 (ILLUSTRATIVE) | $5,039 | $240 | 21 | **19** |  |  |  |

Dòng "history …": mỗi đợt lãi giảm ≥ 1 điểm kể từ 1971, tái cấp vốn ở tháng đầu tiên thấp hơn đỉnh 1 điểm; * = phí theo tỉ lệ cố định trước 2018 (ILLUSTRATIVE). Trong lịch sử, khoản vay mới vài tháng tuổi khi tái cấp vốn, nên hai cách gần như trùng nhau; với Maya (35 kỳ) thì khác.

Nguồn: FRED `MORTGAGE30US` (Freddie Mac PMMS), HMDA 2018–2025 (CFPB/FFIEC). Tính bằng `model/refi.py` (`break_even_balance`, `both`, `net_after`, `history`); test `model/test_refi.py` (12 test, có bản cài đặt độc lập tính từng tháng). CSV: `out/break-even-methods.csv`.

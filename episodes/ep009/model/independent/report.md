# Kiểm độc lập Tập 9 (Việc 0)

Người kiểm: Claude Code headless **Sonnet** khoá Console (`briefs/independent.md`, log `logs/independent.jsonl`, $0,20), chỉ đọc `data/raw/*` + định nghĩa, viết `check.py` (thư viện chuẩn). Bash bị chặn trong lượt nên điều phối chạy `check.py` (không sửa).

**34/34 dòng trùng.**

| đại lượng | kiểm độc lập | model.json | |
|---|---|---|---|
| n_windows_10y | 307 | 307 | trùng |
| last_start | 2016-07 | 2016-07 | trùng |
| share_buyer_ahead_cash | 75.6 | 75.6 | trùng |
| renter_ahead_count_cash | 75 | 75 | trùng |
| median_advantage_cash | 157104 | 157104 | trùng |
| share_buyer_ahead_stocks | 49.5 | 49.5 | trùng |
| renter_ahead_count_stocks | 155 | 155 | trùng |
| median_advantage_stocks | -5827 | -5827 | trùng |
| share_buyer_ahead_lump | 63.8 | 63.8 | trùng |
| renter_ahead_count_lump | 111 | 111 | trùng |
| median_advantage_lump | 90280 | 90280 | trùng |
| cash_ahead_stocks_not | 80 | 80 | trùng |
| windows_stocks_dollar_below_1 | 16 | 16 | trùng |
| stocks_min.start | 1991-01 | 1991-01 | trùng |
| stocks_min.value | -485063 | -485063 | trùng |
| stocks_max.start | 2012-10 | 2012-10 | trùng |
| stocks_max.value | 297855 | 297855 | trùng |
| h15.n | 247 | 247 | trùng |
| h15.cash | 100.0 | 100.0 | trùng |
| h15.stocks | 21.9 | 21.9 | trùng |
| era 1990s cash | 100.0 | 100.0 | trùng |
| era 1990s stocks | 67.6 | 67.6 | trùng |
| era 2002-2007 cash | 8.3 | 8.3 | trùng |
| era 2002-2007 stocks | 0.0 | 0.0 | trùng |
| era 2009-2016 cash | 100.0 | 100.0 | trùng |
| era 2009-2016 stocks | 78.0 | 78.0 | trùng |
| adv 2006-06 cash | -82385 | -82385 | trùng |
| adv 2006-06 stocks | -261689 | -261689 | trùng |
| adv 2012-04 cash | 483975 | 483975 | trùng |
| adv 2012-04 stocks | 237632 | 237632 | trùng |
| adv 1991-01 cash | 48410 | 48410 | trùng |
| adv 1991-01 stocks | -485063 | -485063 | trùng |
| sweep 4% stocks | 30.9 | 30.9 | trùng |
| sweep 6% stocks | 62.2 | 62.2 | trùng |

## Đối chiếu nguồn cổ phiếu (B7: nguồn độc lập)

French (CRSP, mọi cổ phiếu Mỹ, giá trị-trọng) vs Shiller (S&P Composite, giá trung bình tháng + cổ tức/12), 1991-01..2023-05, 389 tháng:

- tương quan lợi nhuận tháng **0.543** (Shiller dùng giá trung bình tháng nên làm trơn — tương quan < 1 là đúng dạng);
- $1 → **25.81** (French) vs **25.24** (Shiller); lãi kép năm 10.55 % vs 10.47 %.
- Kết luận: hai nguồn cùng bậc; lời chỉ dùng French (Shiller ở URL Yale dừng 2023-09).

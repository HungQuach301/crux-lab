# C1 — Logline và tiêu đề nháp (nguyên văn đưa người đọc mù)

Claim: `numbers.md`. Mọi kết quả trước 5/2005 là giả định — cả hai logline nói rõ ngay câu đầu tiên có kết quả (`ctx_hypothetical`).

## Logline A — "người như tôi" + lời hứa đáp án
If you have money you won't need for 20 years, a US Series EE savings bond promises to double it, about 3.5% a year, while 3-month Treasury bills paid 3.72% in August 2026. Today's doubling terms apply to bonds bought since May 2005, and earlier bonds had other terms, so for earlier years we apply them as if they had existed: we roll T-bills through every 20-year stretch since 1934 to show how often the roll ended above double, when it fell short, and whether double even kept up with prices.

Claim: `horizon_years`, `doubling_rate_pct_per_year` (3.53 → "about 3.5%"), `bill_term_months`, `tb3ms_latest_pct`, `tb3ms_latest_month`, `guarantee_from`, `ctx_hypothetical`, `first_start`.

## Logline B — khoảnh khắc có bảo đảm thật (nghịch lý)
In August 2026 a 3-month T-bill paid 3.72%, more than the 3.53% a year it takes to double money in 20 years. Yet for the few savers who bought a US Series EE savings bond under today's doubling terms between May 2005 and September 2006 and held it 20 years, rolling T-bills over the same years ended at only about 1.38 times the money — a short, single-era sample. Over every 20-year stretch since 1934, with the guarantee applied as if it had existed then, the roll ended above double only about half the time; we show when it won and when it didn't.

Claim: `tb3ms_latest_pct`, `tb3ms_latest_month`, `doubling_rate_pct_per_year`, `horizon_years`, `guarantee_from`, `last_start`, `min_multiple_guarantee_starts`/`max_multiple_guarantee_starts` (1.378–1.388 → "about 1.38"), `first_start`, `share_tbills_above_double_pct` (52.3 → "about half"), `ctx_hypothetical`.

## Đối chứng yếu W — diễn giải số đơn thuần (kiểu G-008/G-009 đã bị chê)
A backtest of 873 overlapping 240-month windows of the TB3MS series from 1934 to 2026 against a fixed 2.0 multiple, with CPIAUCNS deflation of the terminal value.

## Đối chứng yếu W2 — dễ hiểu nhưng sai trọng tâm (thêm theo REVIEWER, trước khi chạy)
A friendly beginner's guide to US savings bonds and Treasury bills: what each one is, how to buy them online, and how their interest is taxed.

## Tiêu đề nháp
- **T1** (hồ sơ): "Savings Bonds That Double in 20 Years vs T-Bills"
- **A1** (logline A): "Money You Won't Touch for 20 Years: Savings Bond or T-Bills?"
- **B1** (logline B): "Double in 20 Years or Roll T-Bills? What History Shows"
Claim tiêu đề: T1, A1 `horizon_years`, `ctx_guarantee`; B1 `horizon_years`, `ctx_guarantee`, `first_start`, `ctx_hypothetical` (phần lịch sử là giả định trước 5/2005 — gói C1 ghi rủi ro). B1 đổi từ "…Every 20-Year Stretch Since 1934" (ngụ ý bảo đảm có từ 1934; REVIEWER).
- Đối chứng **X**: "EE Savings Bonds Explained"

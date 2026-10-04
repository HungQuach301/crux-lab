# C1 — Logline và tiêu đề nháp (nguyên văn đưa người đọc mù)

Claim: `numbers.md`. Mọi kết quả trước 5/2005 là giả định — cả hai logline nói rõ ngay câu đầu tiên có kết quả (`ctx_hypothetical`).

## Logline A — "người như tôi" + lời hứa đáp án
If you have money you won't need for 20 years, a US savings bond promises to double it, about 3.5% a year, while 3-month Treasury bills paid 3.72% in August 2026. That doubling guarantee only exists for bonds bought since May 2005, so we apply it to the past as if it had always existed: we roll T-bills through every 20-year stretch since 1934 to show how often the roll ended above double, when it fell short, and whether double even kept up with prices.

Claim: `horizon_years`, `doubling_rate_pct_per_year` (3.53 → "about 3.5%"), `bill_term_months`, `tb3ms_latest_pct`, `tb3ms_latest_month`, `guarantee_from`, `ctx_hypothetical`, `first_start`.

## Logline B — khoảnh khắc có bảo đảm thật (nghịch lý)
In August 2026 a 3-month T-bill paid 3.72%, more than the 3.53% a year it takes to double money in 20 years. Yet for anyone who could actually have bought the US savings bond's doubling guarantee and held it 20 years — starting May 2005 to September 2006 — rolling T-bills over the same years ended at about 1.38 times the money. We replay every 20-year stretch back to 1934, applying the guarantee as if it had existed then, to see when the roll beat double and when it didn't.

Claim: `tb3ms_latest_pct`, `tb3ms_latest_month`, `doubling_rate_pct_per_year`, `horizon_years`, `guarantee_from`, `last_start`, `min_multiple_guarantee_starts`/`max_multiple_guarantee_starts` (1.378–1.388 → "about 1.38"), `first_start`, `ctx_hypothetical`.

## Đối chứng yếu W — diễn giải số đơn thuần (kiểu G-008/G-009 đã bị chê)
A backtest of 873 overlapping 240-month windows of the TB3MS series from 1934 to 2026 against a fixed 2.0 multiple, with CPIAUCNS deflation of the terminal value.

## Tiêu đề nháp
- **T1** (hồ sơ): "Savings Bonds That Double in 20 Years vs T-Bills"
- **A1** (logline A): "Money You Won't Touch for 20 Years: Savings Bond or T-Bills?"
- **B1** (logline B): "A Bond That Only Doubles vs T-Bills: Every 20-Year Stretch Since 1934"
- Đối chứng **X**: "EE Savings Bonds Explained"

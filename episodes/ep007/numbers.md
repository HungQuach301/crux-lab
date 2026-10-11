# Claim — Tập 7 (Việc 0; claim ID = khoá `quantities` của `out/model.json`)

Dữ liệu (FRED, tải 2026-10-11, `data/fetch.py`; không commit): MORTGAGE30US + MORTGAGE15US (Freddie Mac PMMS, tuần) → **1.833 tuần ghép, 1991-08-30 → 2026-10-08**. Đối chiếu Optimal Blue OBMMIC30YF/OBMMIC15YF (trung bình 7 ngày, từ 2017): **510/510 tuần trong 0,5 điểm** cho cả hai (lệch lớn nhất 0,384 / 0,282). Bản ghim hồ sơ `topics-r2/machine/debt-1/sources.json` (coed=2026-09-24): **SHA khớp**, tiền tố tệp mới trùng, +2 tuần.
Tính: `model/model.py` (từ định nghĩa hồ sơ, không gọi calc.py). calc.py hồ sơ trên bản ghim: **18/18 trùng `result.json`**; trên dữ liệu mới: số "hiện tại" đổi theo tuần 2026-10-08 (7,40 % / 6,73 %). Kiểm độc lập (headless khoá Console, chỉ đọc data/raw): **57/57 khớp** (5 khớp do làm tròn → hiển thị đô la nguyên) — `model/independent/report.md`.

**Tuần dữ liệu (G1 câu 2, 11/10): mọi số "hiện tại" (`*_now`, gồm $120/tháng) là lãi khảo sát PMMS tuần 2026-10-08 — nói/ghi "the week of October 8, 2026" (hoặc "October 8" sau lần đầu), không nói "this week"/"this week's rates"; lời S03.1, S07.2, S09.3, S12.2, S21.2, S23.2, S33.3; hình B01, B03, B32, B33; mô tả + thumbnail ghi cùng mốc.**

**Luật nói (claim-risk `topics-r2/machine/debt-1/claim-risk.md` + hồ sơ cầu):** không khuyên ("take the 15-year", "always prepay", "invest instead"); cái giá đặt **cạnh** sự linh hoạt, không phán xét; **không dự báo lãi hay chênh lệch** — "history, not a forecast"; số hiện tại chỉ đúng **ở lãi khảo sát tuần 2026-10-08 trên $320,000**, đề nghị thật của từng người khác (điểm, phí, kỳ hạn); chỉ gốc + lãi (không thuế nhà, bảo hiểm, PMI, khấu trừ thuế); giá trị của sự linh hoạt (mất việc, khẩn cấp) **không đo**; "mỗi đô la trả thêm được 7,40 %" = **lãi không còn phải trả, trước thuế**, không phải lợi suất đầu tư và không so với thị trường; nhân vật ILLUSTRATIVE; "US only". Lãi 30 năm "luôn cao hơn 0,6 điểm" → SAI: chênh 0,2–1,0 điểm.

| Claim ID | Giá trị | Hiển thị | Định nghĩa | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `n_weeks` | 1833 | 1,833 weeks | Number of paired weeks. | data/normalized/pmms_weekly.csv | history |
| `first_week` | 1991-08-30 | August 1991 | First paired week. | data/normalized/pmms_weekly.csv | history |
| `last_week` | 2026-10-08 | the week of October 8, 2026 | Last paired week ("now" of the data). | data/normalized/pmms_weekly.csv | present fact |
| `r30_now` | 7.4 | 7.40% | 30-year rate in the last paired week. | data/normalized/pmms_weekly.csv | present fact |
| `r15_now` | 6.73 | 6.73% | 15-year rate in the last paired week. | data/normalized/pmms_weekly.csv | present fact |
| `spread_now` | 0.67 | 0.67 point | 30-year minus 15-year rate in the last paired week. | data/normalized/pmms_weekly.csv | present fact |
| `pay15_now` | 2828.16 | $2,828 a month | Payment on a 15-year loan (n=180) at the last week 15-year rate. | data/normalized/pmms_weekly.csv | present fact; ILLUSTRATIVE loan |
| `pay30_now` | 2215.62 | $2,216 a month | Required payment on a 30-year loan (n=360) at the last week 30-year rate. | data/normalized/pmms_weekly.csv | present fact; ILLUSTRATIVE loan |
| `pay30on15_now` | 2948.28 | $2,948 a month | Payment that retires the 30-year loan in 15 years: n=180 at the last week 30-year rate. | data/normalized/pmms_weekly.csv | present fact; ILLUSTRATIVE loan |
| `extra_vs15_month_now` | 120.12 | $120 a month | pay30on15_now minus pay15_now (unrounded inputs). | data/normalized/pmms_weekly.csv | present fact |
| `extra_vs15_total_now` | 21622 | $21,622 (about $21,600) | (pay30on15_now - pay15_now) * 180, unrounded inputs: extra paid over 15 years for paying the 30-year loan on a 15-year schedule instead of taking the 15-year loan. | data/normalized/pmms_weekly.csv | present fact |
| `fallback_gap_now` | 612.55 | about $613 a month | pay15_now minus pay30_now: how much lower the 30-year required payment is than the 15-year payment. | data/normalized/pmms_weekly.csv | present fact |
| `extra_principal_needed_now` | 732.67 | $733 a month | pay30on15_now minus pay30_now: extra principal each month on top of the 30-year required payment to finish in 180 months. | data/normalized/pmms_weekly.csv | present fact |
| `months_at_pay15_now` | 194.6 | about 195 months (16 years and 3 months) | Months to pay off the 30-year loan at the last week 30-year rate when paying exactly pay15_now each month (continuous formula). | data/normalized/pmms_weekly.csv | present fact |
| `months_late_at_pay15_now` | 14.6 | about 15 months late | months_at_pay15_now minus 180. | data/normalized/pmms_weekly.csv | present fact |
| `interest_15_now` | 189069 | $189,069 (about $189,000) | Total interest on the 15-year loan: pay15_now*180 - 320000. | data/normalized/pmms_weekly.csv | present fact |
| `interest_30on15_now` | 210691 | $210,691 (about $211,000) | Total interest on the 30-year loan paid in 15 years: pay30on15_now*180 - 320000. | data/normalized/pmms_weekly.csv | present fact |
| `interest_30full_now` | 477622 | $477,622 (about $478,000) | Total interest on the 30-year loan paid on its own 30-year schedule: pay30_now*360 - 320000. | data/normalized/pmms_weekly.csv | present fact |
| `spread_mean` | 0.57 | 0.57 point | Mean weekly spread (30-year minus 15-year). | data/normalized/pmms_weekly.csv | history |
| `spread_min` | 0.2 | 0.2 point | Smallest weekly spread. | data/normalized/pmms_weekly.csv | history |
| `spread_max` | 1.0 | 1.0 point | Largest weekly spread. | data/normalized/pmms_weekly.csv | history |
| `share_spread_ge_050` | 0.63 | 63% (about 2 in 3 weeks) | Share of paired weeks with spread >= 0.50 point. | data/normalized/pmms_weekly.csv | history |
| `extra_total_median` | 16631 | $16,631 (about $16,600) | For every paired week: (n=180 payment at the 30-year rate - n=180 payment at the 15-year rate) * 180. Median over weeks. | data/normalized/pmms_weekly.csv | history |
| `extra_total_min` | 6097 | $6,097 (about $6,100) | Same weekly quantity as extra_total_median; minimum over weeks. | data/normalized/pmms_weekly.csv | history |
| `extra_total_min_week` | 2008-12-04 | December 2008 | Week of extra_total_min. | data/normalized/pmms_weekly.csv | history |
| `extra_total_max` | 29502 | $29,502 (about $29,500) | Same weekly quantity as extra_total_median; maximum over weeks. | data/normalized/pmms_weekly.csv | history |
| `extra_total_max_week` | 2023-01-26 | January 2023 | Week of extra_total_max. | data/normalized/pmms_weekly.csv | history |
| `share_extra_ge_now` | 0.187 | 18.7% (fewer than 1 in 5 weeks) | Share of paired weeks whose extra_total is at least extra_vs15_total_now (unrounded). | data/normalized/pmms_weekly.csv | history |
| `bar_now` | 7.4 | 7.40% a year, before taxes | Return earned by each extra dollar of principal on the 30-year loan = the loan rate (interest no longer charged), before taxes: the last week 30-year rate. | data/normalized/pmms_weekly.csv | present fact; rule |
| `r30_min` | 2.65 | 2.65% | Lowest weekly 30-year rate over the paired weeks. | data/normalized/pmms_weekly.csv | history |
| `r30_min_week` | 2021-01-07 | January 2021 | First week of r30_min. | data/normalized/pmms_weekly.csv | history |
| `r30_max` | 9.25 | 9.25% | Highest weekly 30-year rate over the paired weeks. | data/normalized/pmms_weekly.csv | history |
| `r30_max_week` | 1994-11-25 | November 1994 | First week of r30_max. | data/normalized/pmms_weekly.csv | history |
| `share_r30_ge_now` | 0.19 | 19% (about 1 week in 5) | Share of paired weeks with a 30-year rate at least r30_now. | data/normalized/pmms_weekly.csv | history |
| `leo_r30` | 2.65 | 2.65% | 30-year rate in the week 2021-01-07. | data/normalized/pmms_weekly.csv | history; ILLUSTRATIVE (Leo) |
| `leo_r15` | 2.16 | 2.16% | 15-year rate in the week 2021-01-07. | data/normalized/pmms_weekly.csv | history; ILLUSTRATIVE (Leo) |
| `leo_extra_vs15_total` | 13231 | $13,231 (about $13,200) | extra_total for the week 2021-01-07. | data/normalized/pmms_weekly.csv | history; ILLUSTRATIVE (Leo) |
| `leo_extra_vs15_month` | 73.51 | $74 a month | (n=180 payment at the 30-year rate - n=180 payment at the 15-year rate) in the week 2021-01-07. | data/normalized/pmms_weekly.csv | history; ILLUSTRATIVE (Leo) |
| `leo_fallback_gap` | 793.4 | about $793 a month | 15-year payment minus 30-year required payment in the week 2021-01-07. | data/normalized/pmms_weekly.csv | history; ILLUSTRATIVE (Leo) |
| `era1991_median_extra_total` | 15118 | $15,118 (about $15,100) | Median weekly extra_total over paired weeks 1991-08-30 to 1999-12-31. | data/normalized/pmms_weekly.csv | history |
| `era1991_median_r30` | 7.73 | 7.73% | Median weekly 30-year rate over paired weeks 1991-08-30 to 1999-12-31. | data/normalized/pmms_weekly.csv | history |
| `era1991_median_spread` | 0.46 | 0.46 point | Median weekly spread over paired weeks 1991-08-30 to 1999-12-31. | data/normalized/pmms_weekly.csv | history |
| `era2000_median_extra_total` | 14210 | $14,210 (about $14,200) | Median weekly extra_total over paired weeks 2000-01-07 to 2009-12-31. | data/normalized/pmms_weekly.csv | history |
| `era2000_median_r30` | 6.18 | 6.18% | Median weekly 30-year rate over paired weeks 2000-01-07 to 2009-12-31. | data/normalized/pmms_weekly.csv | history |
| `era2000_median_spread` | 0.45 | 0.45 point | Median weekly spread over paired weeks 2000-01-07 to 2009-12-31. | data/normalized/pmms_weekly.csv | history |
| `era2010_median_extra_total` | 20374 | $20,374 (about $20,400) | Median weekly extra_total over paired weeks 2010-01-07 to 2019-12-26. | data/normalized/pmms_weekly.csv | history |
| `era2010_median_r30` | 4.03 | 4.03% | Median weekly 30-year rate over paired weeks 2010-01-07 to 2019-12-26. | data/normalized/pmms_weekly.csv | history |
| `era2010_median_spread` | 0.72 | 0.72 point | Median weekly spread over paired weeks 2010-01-07 to 2019-12-26. | data/normalized/pmms_weekly.csv | history |
| `era2020_median_extra_total` | 21345 | $21,345 (about $21,300) | Median weekly extra_total over paired weeks 2020-01-02 to 2026-10-08. | data/normalized/pmms_weekly.csv | history |
| `era2020_median_r30` | 6.28 | about 6.3% | Median weekly 30-year rate over paired weeks 2020-01-02 to 2026-10-08. | data/normalized/pmms_weekly.csv | history (median 6.275: show one decimal) |
| `era2020_median_spread` | 0.7 | 0.70 point | Median weekly spread over paired weeks 2020-01-02 to 2026-10-08. | data/normalized/pmms_weekly.csv | history |
| `monthly_extra_months` | 180 | 180 months (15 years) | Monthly simulation at r30_now: required payment + extra_principal_needed_now every month; number of payments until the balance reaches zero. | data/normalized/pmms_weekly.csv | present fact; rule |
| `monthly_extra_interest` | 210691 | $210,691 | Total interest in the monthly-extra simulation. | data/normalized/pmms_weekly.csv | present fact |
| `yearly_lump` | 8792.03 | $8,792 once a year | 12 * extra_principal_needed_now, paid once a year with payments 12, 24, ... | data/normalized/pmms_weekly.csv | present fact |
| `yearly_lump_months` | 184 | 184 months (4 months later) | Monthly simulation at r30_now: required payment every month + yearly_lump with payments 12, 24, ...; number of payments until the balance reaches zero. | data/normalized/pmms_weekly.csv | present fact |
| `yearly_lump_interest` | 218857 | $218,857 (about $218,900) | Total interest in the yearly-lump simulation. | data/normalized/pmms_weekly.csv | present fact |
| `yearly_vs_monthly_interest` | 8166 | $8,166 (about $8,200) | yearly_lump_interest minus monthly_extra_interest (unrounded). | data/normalized/pmms_weekly.csv | present fact |

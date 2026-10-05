# Việc 0 — định nghĩa cho kiểm độc lập (ghi TRƯỚC khi giao; agent không đọc mã dựng)

Dữ liệu: `TB3MS.csv`, `CPIAUCNS.csv` (FRED, coed=2026-08-01; cột `observation_date,<ID>`; ô trống = không có số). Tháng viết YYYY-MM-01.

## Definitions (English, handed to the checker verbatim)
- TB3MS: 3-month Treasury bill rate, % a year, monthly. CPIAUCNS: consumer price index, monthly.
- Start month s: every TB3MS month from 1934-01-01 such that TB3MS has values for all 240 months s, s+1, …, s+239.
- Roll multiple M(s) = product over those 240 months of (1 + TB3MS/1200).
- Lock (savings bond) = exactly 2.0 at 20 years. "Above double" = M(s) > 2.0 (strict).
- Real value of double V(s) = 2.0 × CPI(s) / CPI(s+240 months), only when CPI has values at both months.
- Groups of start months: 1934-01..1949-12; 1950-01..1989-12; 1990-01..last start; "guarantee" = 2005-05..last start.

## Quantities to report (unrounded and rounded as shown)
starts; first_start; last_start; share_tbills_above_double_pct (0.1); median/min/max of M (0.001) and the start month of min and max (earliest on ties); share above double for each group (0.1) and the number of starts in each group; latest window M(last start) (0.001); min and max M within the guarantee group (0.001); doubling_rate_pct_per_year = 100(2^(1/20)−1) (0.01); real_windows; share with V ≥ 1 (0.1); share with V < 1 (0.1); median V in % (0.1); min V in % (0.1) and its start; the latest start month with V < 1; the start months that have no V; for starts from 1990-01: share whose average TB3MS over their 240 months is below TB3MS in the start month (0.1); mean of all TB3MS months (0.01); number of starts with |M/2 − 1| < 0.005; TB3MS in the last data month and that month; floor(number of TB3MS months / 240).

## Dung sai so máy
Đếm và tháng: chính xác. Số làm tròn: bằng nhau sau làm tròn; số chưa làm tròn: |Δ| ≤ 1e-9 tương đối. Mọi M(s) (873 cửa sổ) so từng cửa sổ.

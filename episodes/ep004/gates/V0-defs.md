# Việc 0 — định nghĩa cho người kiểm độc lập (Tập 4)

Người kiểm là agent mới; chỉ đọc file này và `episodes/ep004/data/*.csv`; **không** đọc `episodes/ep004/model/`, `episodes/ep004/out/`, `topics-r1/machine/tax-2/calc.py` hay `result.json`. Viết mã riêng vào `episodes/ep004/model/independent/`, ghi `independent.json` (giá trị CHƯA làm tròn).

## Definitions (English, for the checker)
Data: FRED CSV files, header row, columns `observation_date, <SERIES_ID>`; skip empty or "." values.
Series (key → file): los_angeles ATNHPIUS31084Q, san_diego ATNHPIUS41740Q, san_francisco ATNHPIUS41884Q, san_jose ATNHPIUS41940Q, seattle ATNHPIUS42644Q, boston ATNHPIUS14454Q, new_york ATNHPIUS35614Q, miami ATNHPIUS33124Q, denver ATNHPIUS19740Q, phoenix ATNHPIUS38060Q, dallas ATNHPIUS19124Q, chicago ATNHPIUS16984Q (the 12 "metros"), us USSTHPI (national, not a metro). CPI: CPIAUCNS (monthly).

For each series s (13 including us):
1. `base_s` = mean of the four quarterly values dated 2000-01-01, 2000-04-01, 2000-07-01, 2000-10-01.
2. `growth_s` = value at 2026-04-01 / base_s (2026-04-01 must be the last row).
3. `threshold_joint_s` = 500000 / (growth_s − 1).
4. For P in {200000, 300000} (label 200k, 300k): `gain_at_<label>_s` = P × (growth_s − 1).
   `cross_quarter_at_<label>_s` = earliest quarter date d ≥ 2001-01-01 with P × (value_d / base_s − 1) > 500000 (strict), or null.
   `stay_quarter_at_<label>_s` = earliest quarter d ≥ 2001-01-01 such that the strict inequality holds for d and every later quarter through 2026-04-01, or null.
Also: `threshold_single_us` = 250000 / (growth_us − 1); `threshold_joint_min` / `threshold_joint_max` = min / max of threshold_joint over the 12 metros (and the metro key); `metros_threshold_under_200k` / `_300k` = count of metros with threshold strictly below 200000 / 300000; `metros_crossed_at_200k` / `_300k` = count of metros whose cross_quarter is not null; `cpi_base` = CPI 1997-05-01, `cpi_now` = CPI 2026-08-01 (must be the last row); `excl_joint_1997_in_now` = 500000 × cpi_now / cpi_base.

Output key names: `<quantity>_<series key>` exactly as above (e.g. `threshold_joint_miami`, `cross_quarter_at_300k_us`).

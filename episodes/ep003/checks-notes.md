# Ghi chú cho phiên K — Tập 3 (P1, 2026-10-04)

Phiên K chạy **một lần** cho tập này (`playbook/episode.md` §7). **Tên `model.kind` và `params` do phiên K quyết**; phiên dựng theo. Mọi thứ dưới đây là đề xuất/đầu vào, không phải tên chốt.

## 1. Mô hình — kind MỚI
- Đặc tả: `topics-r1/machine/retire-4/model.json → newKindNeeds` (đầu vào, phép tính, đầu ra, bất biến; tham số hoá: lăn lãi `R` mỗi `p` tháng × khoá bội số hằng `m` **hoặc** chuỗi lãi khoá `L` mỗi `q` tháng, kỳ `H`). Nhãn làm việc của chủ dự án: `lock-vs-roll-replay`.
- Instance Tập 3: `roll` TB3MS, `p = 1`; `lock.multiple = 2.0`; `H = 240`; `firstStart` 1934-01; nhóm `1934-1949`, `1950-1989`, `since-1990`, `guarantee` (từ 2005-05); deflator CPIAUCNS; `nearBandPct` 0.5. Thêm ở C2: `steady_breakeven_tb3ms_pct` = 1200(2^(1/240) − 1); `share_avg_rule_agrees_pct` (trung bình cộng TB3MS 240 tháng > 3.47 ⇔ bội số > 2).
- Dùng lại: retire-3 (`roll` GS1 `p = 12`, `lock` GS5 `q = 12`, `H = 60`, `startFilter: rollRateAboveLockRate`, runs). Bản dựng `episodes/ep003/model/model.py --retire3` khớp 11/11 số hồ sơ retire-3.
- Bản dựng: `episodes/ep003/model/model.py` → `out/model.json` (chưa làm tròn; mọi cửa sổ). Sẽ đổi dạng theo tên/params K chốt.
- Kiểm độc lập đã có: `model/independent/recompute.py` (agent mới, từ `gates/V0-defs.md`): 873/873 cửa sổ trùng, 36/36 đại lượng + 2 đại lượng thêm ở C2 khớp.
- Bất biến đề xuất (S05): xem `newKindNeeds.invariants` (lãi hằng → công thức đóng; p = 1 ⇒ tích = tỉ số chỉ số tích luỹ; tổng tỉ lệ = 100; đơn điệu theo lãi; `m = 2, H = 240` ⇒ 3.526%/năm).

## 2. Claim kịch bản dùng (46, `story/script.md` C2 v1) — mọi ID trong `numbers.md`
Mô hình: `starts, first_start, last_start, share_tbills_above_double_pct, median_tbill_multiple_20y, min_tbill_multiple_20y, min_start, max_tbill_multiple_20y, max_start, share_above_double_1934_1949_pct (early_from, early_to), share_above_double_1950_1989_pct (mid_from, mid_to), share_tbills_above_double_starts_since_1990_pct (since_1990_from), starts_with_guarantee, guarantee_from, min_multiple_guarantee_starts, max_multiple_guarantee_starts, share_above_double_guarantee_starts_pct, latest_window_end, real_windows, share_double_beat_prices_pct, worst_real_value_double_pct, worst_real_start, share_since_1990_avg_below_start_pct, mean_tb3ms_all_pct, steady_breakeven_tb3ms_pct, share_avg_rule_agrees_pct, near_double_starts, near_double_band_pct, nonoverlap_periods, doubling_rate_pct_per_year, tb3ms_latest_pct, tb3ms_latest_month`.
Hằng/định nghĩa: `horizon_years, horizon_months, bill_term_months, bills_per_horizon`.
Bối cảnh (không phải mô hình): `ctx_guarantee` (31 CFR 351.34(a), 351.35(f)(2)), `ctx_hypothetical`, `ctx_penalty` (351.35(e)), `ctx_ee_rate` (2.40%, bond phát hành May–October 2026; **P3/C6 cập nhật lãi công bố 1/11/2026**), `viewer_age_decade` (định nghĩa người xem, ILLUSTRATIVE).
Nhân vật: **Dana — ILLUSTRATIVE** (tên chờ chủ dự án duyệt ở C3).

## 3. Giả định phải hiện trên màn hình (`claims.assumptions`, S02) — đề xuất
- **giả định bảo đảm trước 5/2005** (nhãn cố định trên mọi cửa sổ trước 5/2005, ví dụ "IF today's guarantee had existed") — luật của tập, chủ dự án C1 (a). Đề xuất K cân nhắc một luật kiểm: mọi khung hiện cửa sổ trước 2005-05 có nhãn này.
- không thuế; lãi chiết khấu trung bình tháng ÷ 12, kép tháng; giữ đủ 20 năm; bỏ hạn mức mua; cửa sổ chồng nhau (4 giai đoạn độc lập).

## 4. Dữ liệu và đối chiếu (S03, S04)
- Chính: FRED TB3MS, CPIAUCNS (coed=2026-08-01, SHA ở `retire-4/sources.json`; tải lại `episodes/ep003/data/fetch.py --verify`). Quyền: FRED "Public Domain: Citation Requested" (bls.gov bị proxy 403). Không commit dữ liệu.
- Đối chiếu đề xuất: TB3MS ↔ trung bình tháng DTB3 (như Tập 2, lệch ≤ 0,005 điểm); CPIAUCNS ↔ nguồn thứ hai do K chọn (BLS trực tiếp bị chặn).

## 5. Việc treo cho K
- Viết bản tính lại độc lập kind mới trong `checks/py/r_model.py` (S01/S05) — **cần merge `main` trước C4**.
- Claim thêm sau khi K khoá → gom cho K tập sau; nếu chặn phát hành → gói C6.

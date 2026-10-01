# Ghi chú cho phiên kiểm — Tập 2

Phiên này KHÔNG sửa `checks/`. Bản tính lại độc lập của loại mô hình mới do **Phiên K3.5** viết (chủ dự án mở riêng). Dưới đây chỉ là **đặc tả**, không có mã.

## K3.5 — `model.kind` mới: `rate-path-history`

**Câu hỏi của mô hình.** Một khoản vay trả đều N tháng, lãi cố định F so với lãi thả nổi bắt đầu ở V0 và đi theo một chỉ số lịch sử. Phát lại khoản thả nổi trên mọi cửa sổ N tháng của chuỗi chỉ số; so tổng tiền lãi.

**`params` đề xuất** (mọi trường bắt buộc trừ khi ghi "tuỳ chọn"):
| Trường | Dạng | Tập 2 |
|---|---|---|
| `loan` | số | 50000 |
| `termMonths` | số nguyên | 120 |
| `fixedRate` | % năm | 9.00 |
| `variableStart` | % năm | 7.50 |
| `index` | `{file, dateColumn, rateColumn}` (CSV, tháng) | `data/normalized/tb3ms_monthly.csv`, `month`, `rate` |
| `indexToday` | `{value, date}`: giá trị chỉ số hôm nay; phải bằng quan sát cuối của `index.file` | `{3.72, 2026-08}` |
| `startRange` | `[từ, đến]` (tháng, gồm hai đầu; "đến" = tháng cuối còn đủ N tháng dữ liệu) | `["1954-01", "2016-09"]` |
| `regimes` | `{tên: [từ, đến]}` | `{"1954_1980": ["1954-01","1980-12"], "1981_on": ["1981-01","2016-09"]}` |
| `floor` | số: chỉ số không xuống dưới mức này | 0 |
| `gaps` (tuỳ chọn) | mảng điểm %: V0 = F − g | [0.5, 1.0, 1.5, 2.0, 2.5, 3.0] |
| `caps` (tuỳ chọn) | mảng % năm: lãi thả nổi = min(cap, …) | [12, 15, 18] |

**Định nghĩa** (nguyên văn `gates/V0-defs.md`): margin = V0 − indexToday. Tháng k = 0..N−1 của cửa sổ bắt đầu s: rate_k = margin + max(floor, indexToday + I[s+k] − I[s]) (với cap: min(cap, rate_k)). Lãi tháng = dư nợ × rate/1200; khoản trả = khoản trả đều trên số tháng còn lại (N − k), **tính lại mỗi khi lãi đổi**. Difference = tổng lãi thả nổi − tổng lãi cố định (không chiết khấu).

**Khoá cho `model.claims` (S05) đề xuất:**
- `base.<khoá>`: `n_starts`, `first_start`, `last_start`, `fixed_total_interest`, `share_variable_costlier`, `median_variable_minus_fixed`, `worst_variable_minus_fixed`, `worst_start`, `best_variable_minus_fixed`, `max_variable_rate_any_window`, `n_starts_<regime>`, `share_costlier_<regime>`, `margin`.
- `payments.<khoá>`: `fixed_payment`, `variable_first_payment`, `max_variable_payment_any_window`, `max_variable_payment_start`, `median_window_max_payment`, `share_windows_max_payment_above_fixed`.
- `gaps.<g>.<khoá>`, `caps.<c>.<khoá>`: `share_costlier`, `share_costlier_<regime>`, `median_diff`, `worst_diff`, `worst_start`, `best_diff`.
- `windows[start].diff|maxRate|maxPay` (S01: tính lại cả 753 cửa sổ).

**Dung sai đề xuất (S01/S05):** như `gates/V0-defs.md` §Dung sai (đô ±1; cent ±0,01; % ±0,1 chỉ khi ở mép làm tròn; ngày so sau chuẩn hoá YYYY-MM ≡ YYYY-MM-01).

**Lưu ý cho K3.5.** (1) Ngày trong file mô hình viết `YYYY-MM-01`; trong `params` có thể viết `YYYY-MM`: so sau chuẩn hoá (bài học topics-r2 V3). (2) Phần nào của `params` K3.5 thấy thiếu để tính lại đủ thì ghi ở đây; P-ep002 bổ sung `contract.json`, không sửa luật. (3) Nếu chủ dự án chọn phạm vi (a) ở C1, các khối `payments/gaps/caps` vẫn có trong file nhưng không có claim.

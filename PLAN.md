# PLAN kênh Crux (≤ 1 trang) — cập nhật 08/10/2026

PLAN của từng tập: `episodes/epNNN/PLAN.md` (mẫu `playbook/templates/PLAN-tap.md`). PLAN Tập 1 cũ: `archive/ep001-v1/PLAN.md`. Thẩm quyền: `CHARTER.md` → `decisions/` (mới nhất D-011).

## Tập hiện hành
| Tập | Đề tài | Format | Nhánh | Trạng thái |
|---|---|---|---|---|
| 5 | #17 PMI 10 % trả trước | `101` | — (đã merge `main` 6e0ae01) | phát hành; tổng kết `tongket-t5/` áp xong (D-011) |
| **6** | **#12 "Does a 2% Annuity Raise Really Keep Up With Prices?"** (`topics-r1/machine/retire-1/`) | `101` hoặc `lab` (G1) | `ep006` (tạo từ `main` khi mở P1) | **chưa mở** — G1 từng tập; mức cảnh báo 15 triệu |
| 7 | đề xuất #2 tăng ca/việc thứ hai (`topics-r1/machine/tax-4/`) | — | — | G1 theo lô 2 tập từ Tập 7 (D-011 Q1) |

**Mở Tập 6:** phiên mới, gõ `Chạy Tập 6, đề tài #12` (`playbook/prompts/RUN.md`; mỗi chặng một phiên — D-011).

## Việc treo
- **Phiên K lô (tongket-t5 §4, D-011 Q3):** chạy **song song Tập 6 P1**, merge `main` **trước C3** Tập 6 (hàng chờ dưới).
- **Nhạc hiệu kênh** (episode.md §5b): dựng ở Tập 6, chủ dự án duyệt **bằng clip có âm ở C3 Tập 6**.
- **Thước chỉ báo** (episode.md §2b, `toolkit/indicators/`): báo ở Tập 6, chưa là ngưỡng; thước xếp sai thứ tự hiệu chuẩn đã bỏ.
- **M4 phải hiệu chuẩn lại ở G1 Tập 6:** ngưỡng móc đặt trên trục 2,4 từ/s; ở hằng mới 2,75 từ/s kịch bản Tập 5 đã duyệt cho M4 = 13,5 s (TRƯỢT) — G1 Tập 6 nêu tên.
- Nhà máy: `toolkit/factory/BACKLOG.md` (giữa tập chỉ sửa CHẶN + CHÍNH của tập đang làm; việc khác gom đầu tập, nhánh `factory-*`).

## Hàng chờ phiên K (`checks-appeal.md`, thứ tự Phiên T5)
1. Hỏi chủ dự án một gói (sửa luật cũ): **A22** V11 glyph/plate → **A10 + A16** F11/F12 đọc từ nhà máy → **A9 + A21** rubric khuyên.
2. Chỉ thêm, tự merge khi selftest đạt (D-008 §2): A20 → A17, A14, A18 → A13, A19, A24 → A23 → **A25, A26** (chỉ báo hồi tố Tập 3–5 đã chạy).
3. Báo cáo/chữ: A15, A12. Còn mở: A5, A7, A8, A11.

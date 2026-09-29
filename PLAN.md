# PLAN — Tập 1, quy trình 6 cổng (P2)

Nhánh: `ep001-v2` (tạo từ `ep001` @ `3cab8ba`). Chỉ P2 merge vào `main`. Khung: `playbook/quality-framework.md`. Bài học: `playbook/lessons.md`.

**Đề tài:** "Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí vay lại?" — Nora ($375,000, 7.62%, 10/2023), Walt ($115,000), Anjali ($655,000).

## Tài sản giữ (không làm lại)
Dữ liệu và mô hình (`data/`, `model/`, kiểm độc lập 619/619), `numbers.md` (claim ID), ba nhân vật, `story/treatment.md` (qua Cổng A), bảng âm S2.

## Trạng thái cổng

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Việc 0 | XONG — merge `main` `7ebc7ea` | — | Khung 3 lớp duyệt; D-002 |
| C1 Ý tưởng | XONG | `episodes/ep001/gates/C1.md` | Logline C; bộ đo mới (vai khán giả đích, tiếng Anh, đối chứng yếu) |
| C2 Kịch bản | XONG | `episodes/ep001/gates/C2.md` | OK; lịch sử rút (a); câu hứa nói với người xem (2 phương án ở C3) |
| C3 Thiết kế và giọng | CHỜ CHỦ DỰ ÁN (hướng, giọng, câu hứa) | `episodes/ep001/gates/C3.md` | |
| C4 Animatic có chuyển động | chờ | | |
| C5 Render và L1 | chờ (cần khoá K3 của Phiên K) | | |
| C6 Chấm cuối | chờ | | |

## Việc treo cần chủ dự án (không chặn cổng)
- Proxy phiên chặn đẩy tag và xoá nhánh (HTTP 403). Tag `ep001-v1-stopped` (`3cab8ba`) có ở máy phiên, chưa lên GitHub; bốn nhánh `claude/stoic-lamport-lt6z0z`, `claude/vigilant-tesla-xogj17`, `checks-v2`, `ccr-b659da90-fg2k6j` đã kiểm (ba nhánh đã merge vào main; `ccr-…` trùng `ep001`) nhưng chưa xoá được. `3cab8ba` vẫn an toàn trên nhánh `ep001`.

## Quy ước
- Ý đồ kiểm mù ghi trước ở `gates/Cx-intent.md`; kết quả nguyên văn ở `gates/Cx-blind.md`.
- Mỗi agent con, mỗi cổng: một dòng ở `episodes/ep001/ledger.md`.
- Điểm dừng an toàn sau mỗi cổng (commit + push `ep001-v2`).
- Luật F12 (chủ dự án nhắc ở C1 cho screenshot/bằng chứng) chưa có trong `checks/` (K2 tới F11) → cần Phiên K3 viết trước C3/C5.

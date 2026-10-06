**Từ phiên cuối Tập 4 (D-008): một prompt duy nhất `RUN.md` — "Chạy Tập N"; một phiên điều phối cho cả tập, dừng ở G1 và G2. Bảng dưới (D-006) giữ làm tham chiếu nội dung từng chặng.**

# Prompt mẫu cho một tập (playbook v3, D-006)

Chủ dự án mở phiên mới và gõ một dòng: **"Chạy Tập N, phiên P1"** (hoặc "Chạy Tập N, đề tài #k, phiên P1"), sau G1 là **"Chạy Tập N, phiên P3"**. **P2 chỉ chạy khi G1 ghi "cần C3"** (ký hiệu ngoài thư viện hình); không thì P2 gộp vào P3. Phiên đọc file prompt tương ứng và thay các chỗ điền `{N}`, `{NNN}`, `{k}`, `{đề tài}` (lấy từ `topics/season.md`, `topics/queue.md` hoặc `PLAN.md`).

| Phiên | File | Cổng | Trần token (`episode.md` §8) |
|---|---|---|---|
| P1 | `P1.md` | C1 máy → C2 → **G1** | 1,4 triệu |
| P2 (khi cần) | `P2.md` | C3 ký hiệu mới | 0,5 triệu |
| P3 | `P3.md` | C4 → C5 → **G2** → giao hàng → **G3** | 1,4 triệu |

Prompt chỉ trỏ tới file, không chép nội dung tập cũ. Mọi phiên mở bằng `bash toolkit/verify.sh <nhánh>`.

**Từ Tập 6 (D-011, thay D-008 §1): prompt `RUN.md` — "Chạy Tập N"; mỗi chặng một phiên điều phối, mở mới ở mỗi điểm dừng chờ chủ dự án (G1, C3 nếu có, G2); phiên cũ đóng bằng PLAN ≤ 1 trang + prompt phiên kế. Bảng dưới (D-006) giữ làm tham chiếu nội dung từng chặng.**

# Prompt mẫu cho một tập (playbook v3, D-006)

*(Tham chiếu D-006 cũ; từ Tập 6 mở bằng "Chạy Tập N" — RUN.md — và mỗi chặng sau là phiên mới dán prompt phiên kế, D-011; chặng P4 = P3 việc 5–7.)* Chủ dự án mở phiên mới và gõ một dòng: **"Chạy Tập N, phiên P1"** (hoặc "Chạy Tập N, đề tài #k, phiên P1"), sau G1 là **"Chạy Tập N, phiên P3"**. **P2 chỉ chạy khi G1 ghi "cần C3"** (ký hiệu ngoài thư viện hình); không thì P2 gộp vào P3. Phiên đọc file prompt tương ứng và thay các chỗ điền `{N}`, `{NNN}`, `{k}`, `{đề tài}` (lấy từ `topics/season.md`, `topics/queue.md` hoặc `PLAN.md`).

| Phiên | File | Cổng | Trần token (`episode.md` §8) |
|---|---|---|---|
| P1 | `P1.md` | C1 máy → C2 → **G1** | 1,4 triệu |
| P2 (khi cần) | `P2.md` | C3 ký hiệu mới | 0,5 triệu |
| P3 | `P3.md` | C4 → C5 → **G2** → giao hàng → **G3** | 1,4 triệu |

Prompt chỉ trỏ tới file, không chép nội dung tập cũ. Mọi phiên mở bằng `bash toolkit/verify.sh <nhánh>`.

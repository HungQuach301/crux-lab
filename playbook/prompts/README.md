# Prompt mẫu cho một tập (playbook v2)

Chủ dự án mở một phiên mới và gõ một dòng: **"Chạy Tập N, phiên P1"** (máy đề xuất ≤ 3 đề tài ở C1) hoặc **"Chạy Tập N, đề tài #k, phiên P1"**; rồi "Chạy Tập N, phiên P2", "… P3". Phiên đọc file prompt tương ứng và thay các chỗ điền: `{N}` (số tập, ví dụ 3 → nhánh `ep003`); `{NNN}` (ba chữ số); `{k}` và `{đề tài}` (số thứ tự và tiêu đề nháp trong `topics/queue.md`). Nếu không có #k, P1 để trống hai chỗ đó cho tới khi chủ dự án chọn ở C1; P2 và P3 lấy đề tài từ `PLAN.md`. Rồi phiên làm theo prompt.

| Phiên | File | Model điều phối | Effort |
|---|---|---|---|
| P1 — C1, C2, giao K | `P1.md` | Opus | Medium |
| P2 — C3, C4 | `P2.md` | Opus | Medium |
| P3 — C5, C6, giao hàng | `P3.md` | Opus | Medium |

Prompt chỉ trỏ tới file. Không chép nội dung tập cũ vào prompt.

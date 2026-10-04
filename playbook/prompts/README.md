# Prompt mẫu cho một tập (playbook v2)

Chủ dự án mở một phiên mới và gõ một dòng: **"Chạy Tập N, đề tài #k, phiên P1"** (rồi P2, P3). Phiên đọc file prompt tương ứng, thay `{N}` (số tập, ví dụ 3 → nhánh `ep003`), `{NNN}` (ba chữ số), `{k}` (số thứ tự trong `topics/queue.md`) và `{đề tài}` (tiêu đề nháp ở dòng #k), rồi làm theo.

| Phiên | File | Model điều phối | Effort |
|---|---|---|---|
| P1 — C1, C2, giao K | `P1.md` | Opus | Medium |
| P2 — C3, C4 | `P2.md` | Opus | Medium |
| P3 — C5, C6, giao hàng | `P3.md` | Opus | Medium |

Prompt chỉ trỏ tới file. Không chép nội dung tập cũ vào prompt.

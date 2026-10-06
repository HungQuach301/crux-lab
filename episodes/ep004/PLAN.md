# PLAN — Tập 4 (ep004), playbook v3

Nhánh `ep004` từ `main` @ `b9710d2` (đẩy song song lên `claude/tap4-p1-dinh-chuan-hq8xue`). Format `lab`. **G1 duyệt 2026-10-05** (`gates/G1-answer.md`): đề tài #3 (tax-2), logline L1b, cold open H2, nhân vật Rosa & Frank, tiêu đề T1, mở C3. Trần token tập **4,5 triệu** (P2 ≤ 1 triệu, P3 ≤ 1 triệu).

## 1. Bảng cổng
| Cổng | Trạng thái | File | Ghi chú |
|---|---|---|---|
| Việc 0 | XONG | `data/fetch.py`, `model/model.py`, `numbers.md`, `model/independent/` | SHA 14/14; độc lập 116/116 |
| Hiệu chuẩn so cặp móc | **ĐẠT** (sát ngưỡng) | `cal-hook/` | 7/8; thứ tự cân bằng; phát hiện lệch vị trí ở Mốc B |
| C1 | CHƯA ĐẠT (cờ khuyên), không vòng 2 | `gates/C1-*.md`, `c1/` | đưa L1 + L1b vào G1 |
| C2 | Kiểm máy ĐẠT; mù v2 6/6, khuyên 0/6; S18 → dự phòng V7 (chưa kiểm lại) | `story/`, `gates/C2-*.md`, `c2/`, `hook-rr/` | móc H2 (so cặp vòng tròn 5/6) |
| Giao phiên K | **SẴN SÀNG — chủ dự án mở phiên K** | `K-brief.md` | kind mới; một lần cho tập |
| **G1** | **XONG** — chủ dự án duyệt (issue #37; C2 tự động #36) | `gates/G1.md`, `gates/G1-answer.md` | trần 4,5 triệu |
| C3 (P2) | **GÓI GỬI — chờ chủ dự án** (cổng gốc: nghĩa 6/6 vòng 2, câu khuyên 12/12 → trượt theo luật) | `gates/C3.md`, `gates/C3-tally.md`, `design/c3/`, `review-c3/` | dựng bằng nhà máy; móc nạp ký hiệu +7/−3 |
| C4 (P3) | **CHỜ** khoá `checks-k38` merge `main` (LOCK hiện `a20c6878`) | — | |

## 2. Phiên sau đọc (phiên K trước; rồi P2 — C3)
`CHARTER.md` · `playbook/quality-framework.md` · `playbook/episode.md` · `episodes/ep004/PLAN.md` · `ledger.md` · `gates/G1.md` · `gates/G1-answer.md` · `story/script.md` · `story/beats.md` · `K-brief.md`.

## 3. Việc treo
- **Phiên K** (chủ dự án mở): kind mới theo `K-brief.md`. Luật nhãn "like … average" theo cảnh là **luật của tập** (`story/check_script.py`), không vào `checks/`.
- **P2 — C3** cho N1, N2 (≤ 2 ký hiệu mới). Sửa kịch bản nếu cần: **agent WRITER MỚI, đầu bài ngắn** (lessons G2).
- **Kiểm mù S18 (sau dự phòng V7) gộp vào lượt C4** (chủ dự án, G1).
- Phối nhạc style C và lời cả tập theo cảnh: P3 (cold open đã có take S01/S02 theo hash chữ).
- `episode.yaml` `midrolls` ghi khi định thời giọng thật (≈ 3:29, ≈ 6:41 ước).
- Không đụng `toolkit/`, `toolkit/factory/` (phiên nhà máy).
## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-06 (P2): main a291ef7 đã merge vào ep004; C3 N1/N2 dựng bằng nhà máy, 2 vòng kiểm mù, gói `gates/C3.md` gửi (issue). **Dừng chờ: (1) trả lời C3; (2) `checks-k38` merge `main`.** Rồi P3: C4. Dựng lại đoạn trích: dữ liệu như dưới → `python3 episodes/ep004/design/c3/build_inputs.py` → `bash toolkit/build.sh episodes/ep004/episode.yaml` (giọng cache theo băm; cài ffmpeg nếu thiếu).
2026-10-05: G1 xong; dừng chờ phiên K (chủ dự án mở), rồi P2. Dữ liệu không commit: `python3 episodes/ep004/data/fetch.py` (kiểm SHA) → `python3 episodes/ep004/model/model.py` → `python3 episodes/ep004/story/check_script.py`. Clip: `python3 episodes/ep004/story/cold_open.py` (take theo hash chữ, không sinh lại nếu chữ không đổi).

## 5. KPI + token so trần
| KPI | P1 thực | Đích Tập 4 |
|---|---|---|
| Chủ dự án tham gia | 1 (G1) | G1, G2 + G3 (+C3) |
| Vòng | C1 1 · C2 2 (+ dự phòng) | ≤ 2 |
| Agent | 42 (gồm REVIEWER G1) + P2 21 = 63 | ≤ 60 cả tập (P1 ≈ 25) |
| Ký tự ElevenLabs | 1.927 (P1) + 1.157 (P2) = 3.084 | ≤ 6.000 |
| Token agent con | ≈ 2,17 triệu | P1 ≤ 1,4 triệu |
| Token P2 | ≈ 0,80 triệu agent con (21 agent) + ≈ 0,2 triệu điều phối ⇒ ≈ 1,0 triệu (chạm trần; REVIEWER gói C3 bỏ) | P2 ≤ 1 triệu |
| Token cả P1 | ≈ 2,6 triệu (+ 84 %) | đã hỏi ở G1 → trần tập 4,5 triệu; còn ≈ 1,9 triệu cho K/P2/P3 (P2, P3 ≤ 1 triệu mỗi phiên) |

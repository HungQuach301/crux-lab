# PLAN — Tập 4 (ep004), playbook v3

Nhánh `ep004` từ `main` @ `b9710d2` (đẩy song song lên `claude/tap4-p1-dinh-chuan-hq8xue`). Format `lab`. Đề tài khuyến nghị #3 (tax-2) — **chờ G1**.

## 1. Bảng cổng
| Cổng | Trạng thái | File | Ghi chú |
|---|---|---|---|
| Việc 0 | XONG | `data/fetch.py`, `model/model.py`, `numbers.md`, `model/independent/` | SHA 14/14; độc lập 116/116 |
| Hiệu chuẩn so cặp móc | **ĐẠT** (sát ngưỡng) | `cal-hook/` | 7/8; thứ tự cân bằng; phát hiện lệch vị trí ở Mốc B |
| C1 | CHƯA ĐẠT (cờ khuyên), không vòng 2 | `gates/C1-*.md`, `c1/` | đưa L1 + L1b vào G1 |
| C2 | Kiểm máy ĐẠT; mù v2 6/6, khuyên 0/6; S18 → dự phòng V7 (chưa kiểm lại) | `story/`, `gates/C2-*.md`, `c2/`, `hook-rr/` | móc H2 (so cặp vòng tròn 5/6) |
| Giao phiên K | ĐÃ SOẠN, chạy khi G1 duyệt | `K-brief.md` | kind mới |
| **G1** | **CHỜ CHỦ DỰ ÁN** (issue `[G1] Tập 4`) | `gates/G1.md` | + ngoại lệ token |
| C3 (P2) | cần (2 ký hiệu mới N1, N2) nếu G1 duyệt | `story/beats.md` | |

## 2. Phiên sau đọc (P2 nếu G1 ghi "cần C3"; không thì P3)
`CHARTER.md` · `playbook/quality-framework.md` · `playbook/episode.md` · `episodes/ep004/PLAN.md` · `ledger.md` · `gates/G1.md` (+ trả lời G1) · `story/script.md` · `story/beats.md` · `K-brief.md`.

## 3. Việc treo
- **Trả lời G1** (đề tài, logline L1/L1b, H2, T1, C3), **2 việc ngoài §6** (luật v3; bỏ vòng 2 C1) và **ngoại lệ token** (a/b/c).
- Phiên K chạy kind mới khi G1 duyệt (`K-brief.md`).
- Phối nhạc style C và lời cả tập theo cảnh: **chưa làm ở P1** (tiết kiệm token/ký tự; không phí nếu chủ dự án đổi đề tài) → P3.
- S18 sau dự phòng chưa kiểm mù lại; "Glen" ASR (S01) kiểm lại khi sinh cả tập.
- `episode.yaml` `midrolls` ghi khi định thời giọng thật (≈ 3:29, ≈ 6:41 ước).
- Bài học đề xuất cho tổng kết: (1) gọi lại agent dài tốn bằng cả ngữ cảnh (WRITER ×3 ≈ 0,56 triệu); (2) luật kiểm máy theo câu ép lặp cụm từ (Goodhart) → theo cảnh; (3) Mốc B so cặp có lệch vị trí; (4) agent `Explore` ≈ 32–35 nghìn token/người đọc (rẻ hơn 44 nghìn đo ở Mốc B).
- Không đụng `toolkit/`, `toolkit/factory/` (phiên nhà máy).

## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-05: dừng ở G1. Dữ liệu không commit: `python3 episodes/ep004/data/fetch.py` (kiểm SHA) → `python3 episodes/ep004/model/model.py` → `python3 episodes/ep004/story/check_script.py`. Clip: `python3 episodes/ep004/story/cold_open.py` (take theo hash chữ, không sinh lại nếu chữ không đổi).

## 5. KPI + token so trần
| KPI | P1 thực | Đích Tập 4 |
|---|---|---|
| Chủ dự án tham gia | 0 (G1 đang chờ) | G1, G2 + G3 (+C3) |
| Vòng | C1 1 · C2 2 (+ dự phòng) | ≤ 2 |
| Agent | 42 (gồm REVIEWER G1) | ≤ 60 cả tập (P1 ≈ 25) |
| Ký tự ElevenLabs | 821 | ≤ 6.000 |
| Token agent con | ≈ 2,17 triệu | P1 ≤ 1,4 triệu |
| Token cả P1 | ≈ 2,6 triệu (+ 84 %) | **vượt > 25 % → hỏi ở G1** |

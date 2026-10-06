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
| C3 (P2) | **XONG** — chủ dự án duyệt (issue #39, `gates/C3-answer.md`): N1, N2 ký hợp đồng bản vòng 2; ngoại lệ cờ khuyên Tập 4 | `gates/C3.md`, `gates/C3-tally.md`, `design/c3/`, `review-c3/` | dựng bằng nhà máy; móc nạp ký hiệu +7/−3 |
| C4 (phiên cuối, D-008) | XONG — checks lần 1; kiểm mù gộp (đối chứng dương ĐẠT, âm có hạn chế; C3 theo A9 khuyên_tính 0/12; S18 2/4); **cổng gốc 3/7 TRƯỢT** (B06, B10, B11, B15); chủ dự án trả lời ngoại lệ (`gates/C4-answer.md`) | `gates/C4*.md` | trần nâng 2,0 tr / 30 agent |
| C5 | XONG — nhạc style C, −14,2 LUFS / −1,6 dBTP; checks lần 2 CHẶN 24/35 (còn F11, F12, S03, S04 + luật trang ngoại lệ); Shorts 3/3 SH01–SH05 ĐẠT; ASR "rose" | `gates/C5.md` | bản vá Shorts toolkit chưa commit (`design/c5/factory-shorts.patch`) |
| **G2** | **CHỜ chủ dự án** — gói sau REVIEWER (1 CHẶN + 7 CHÍNH đã sửa) | `gates/G2.md`, `gates/REVIEW-G2.md`, `gates/G2-*.md`, `review-g2/` | khuyến nghị (b): sửa nhãn + vòng 2 cổng gốc với trần mới |

## 2. Phiên sau đọc (phiên C4 + P3)
`CHARTER.md` · `playbook/quality-framework.md` · `playbook/episode.md` · `playbook/prompts/P3.md` · `episodes/ep004/PLAN.md` · `ledger.md` · `gates/G1-answer.md` · **`gates/C3-answer.md`** · `gates/C3.md` · `story/script.md` · `story/beats.md` · `episode.yaml` · `design/c3/NOTES.md` · `toolkit/factory/README.md` · `checks-appeal.md` A9.

**Điều kiện mở C4:** `checks-k38` đã merge `main` (`checks/LOCK` khác `a20c6878`); merge `main` vào `ep004` trước; `bash toolkit/verify.sh ep004`.

## 3. Việc treo (P3)
- **Lô K sau:** `checks/README.md` mục K3.8 còn chữ "chờ chủ dự án duyệt" — sửa ở lô K sau (D-008).
- **REVIEWER bị bỏ ở gói C3 (trần token P2) → bắt buộc chạy REVIEWER cho gói kế tiếp** (gói C4/G2), soát cả phần C3 đã gửi.
- **Lượt C4 gộp:** (a) đối chứng câu khuyên (A9): một hình thư viện không liên quan thuế, cùng câu hỏi vai T, ≈ 2 người đọc; chấm cờ khuyên theo rubric tách hai loại (thận trọng chung không tính; khuyên sản phẩm/hành động tài chính tính), cùng một đối chứng dương ("Sell before prices drop"); (b) kiểm mù S18 sau dự phòng V7 (G1).
- **Móc nạp ký hiệu nhà máy** (`build.py`, `page.html`, `spec.py`, +7/−3): viết **selftest** (`toolkit/tests/`: một ký hiệu giả trong thư mục tạm → spec không BLOCK id lạ đã khai; job có ký hiệu; đổi mã ký hiệu → băm cache đổi; thiếu file → spec BLOCK) rồi merge cùng tập ở P3. Ngoài móc, không đụng `toolkit/`.
- Dựng cả tập bằng nhà máy: thêm cảnh còn lại vào `episode.yaml` (`scope` full), Shorts 2–3, `midrolls` khi có giọng thật (≈ 3:29, ≈ 6:41 ước). Mã hình chỉ N1/N2 + thư viện.
- ASR S14.1 nghe "rose" thành "rows" (từ đồng âm, không phải từ khoá) → nghe lại khi kiểm tiếng cả tập.
- Phối nhạc style C, lời cả tập theo cảnh (cold open có take S01/S02 theo hash chữ; S08, S13, S14 đã cache).
- Luật nhãn "like … average" theo cảnh là **luật của tập** (`story/check_script.py`), không vào `checks/`.
## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-06 (phiên cuối, D-008): LOCK `250ab298` khớp; merge `main` (`b528736`); D-008 + `playbook/prompts/RUN.md`; selftest móc `toolkit/tests/test_symbol_hook.py` 5/5 (điều (d): spec chưa BLOCK file ký hiệu thiếu — `load_inputs` dừng trước API; thêm kiểm vào `spec.py` bị chặn quyền → hàng chờ); C4 dựng + checks lần 1; kiểm mù gộp. Chủ dự án trả lời (`gates/C4-answer.md`) → cổng gốc, C5, gói G2, REVIEWER. **DỪNG ở G2.** Dựng lại: `python3 episodes/ep004/design/c4/build_inputs.py && bash toolkit/build.sh episodes/ep004/episode.yaml && python3 episodes/ep004/design/c4/build_inputs.py --out` (av 14.2.0 cho faster-whisper).
2026-10-06 (P2, xong): C3 duyệt (issue #39); S14.5 sửa + sinh lại + ASR. **P2 DỪNG. C4 + P3 ở phiên mới, sau khi `checks-k38` merge `main`.** Dựng lại đoạn trích: dữ liệu như dưới → `python3 episodes/ep004/design/c3/build_inputs.py` → `bash toolkit/build.sh episodes/ep004/episode.yaml` (giọng cache theo băm; cài ffmpeg nếu thiếu).
2026-10-05: G1 xong; dừng chờ phiên K (chủ dự án mở), rồi P2. Dữ liệu không commit: `python3 episodes/ep004/data/fetch.py` (kiểm SHA) → `python3 episodes/ep004/model/model.py` → `python3 episodes/ep004/story/check_script.py`. Clip: `python3 episodes/ep004/story/cold_open.py` (take theo hash chữ, không sinh lại nếu chữ không đổi).

## 5. KPI + token so trần
| KPI | P1 thực | Đích Tập 4 |
|---|---|---|
| Chủ dự án tham gia | G1 + C3 = 2 | G1, G2 + G3 (+C3) |
| Vòng | C1 1 · C2 2 (+ dự phòng) · C3 2 | ≤ 2 |
| Agent | P1 42 + P2 21 = 63 (vượt đích 60; P3 cần gọn) | ≤ 60 cả tập (P1 ≈ 25) |
| Ký tự ElevenLabs | P1 1.927 + P2 1.627 (S08/S13/S14 1.157 + S14 sinh lại 470) = 3.554 | ≤ 6.000 |
| Token agent con | ≈ 2,17 triệu | P1 ≤ 1,4 triệu |
| Token P2 | ≈ 0,80 triệu agent con (21 agent) + ≈ 0,2 triệu điều phối ⇒ ≈ 1,0 triệu (chạm trần; REVIEWER gói C3 bỏ → chạy ở gói kế tiếp); sau C3: + ≈ 0,05 triệu điều phối (sửa S14.5, ghi sổ) | P2 ≤ 1 triệu |
| Token cả P1 | ≈ 2,6 triệu (+ 84 %) | đã hỏi ở G1 → trần tập 4,5 triệu; còn ≈ 1,9 triệu cho K/P2/P3 (P2, P3 ≤ 1 triệu mỗi phiên) |

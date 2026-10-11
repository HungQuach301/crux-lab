# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` (P3c đẩy cả `ep006` và `claude/gracious-brown-rccz2m`, cùng SHA) · **Đề tài:** #12 · **Format:** `101` · **Phiên vừa đóng:** P3c (`session_01QNrEnsRn8CMnf6J5ujL79c`, chủ dự án cho chạy tiếp quá 300 nghìn ngữ cảnh) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**G2 chờ** — gói `gates/G2.md`, issue [#51](https://github.com/HungQuach301/crux-lab/issues/51), REVIEWER `gates/REVIEW-G2.md` (ĐẠT có sửa, đã áp). Bản giao 1080p **536,6 s = 8:56,6** (MR1 3:28), master SHA `f96da0ea…`, 720p `ef3a3ffd…` (`review-g2/`). Checks **`run-c5d`: Tập ĐẠT, CHẶN 36/36, CHÍNH 13/13, F11 ĐẠT** (lịch sử: run-c5 TRƯỢT → C5b → run-c5b ĐẠT → C5c → run-c5c ĐẠT có giải thích V11 → REVIEWER → C5d). Cổng gốc **20/23 = 87 %**, `advice_stated` 0 (B01, B15 hết 3 vòng; B04 dao động 0,5–1). qc 6 TRƯỢT như Tập 5 (−1,8 dBTP, freezedetect, đối trọng master 0 khung log). Shorts SH1–SH3 ĐẠT (móc một dòng). Thumbnail: 2 khung thế giới + 1 đối chứng 2D.

## 2. Việc tiếp (≤ 3) và việc treo
1. **P4 việc 5:** chép câu trả lời G2 → `gates/G2-answer.md`; áp quyết định (sửa → dựng lại đoạn đổi + `c5/checks_split.sh` đủ bộ, trần 2 h → `RESUME=1`); `taste-ledger.md`, `AUTHORSHIP.md`, ledger; `HUONG-DAN-DANG.md` theo mẫu; `audience.md`.
2. **P4 việc 6 — giao hàng** (`episode.md` §6, `toolkit/deliver/deliver.py`): master `out/video.mp4` + Shorts `out/shorts/` + gói `out/package/` + SHA-256 → G3 (chủ dự án đăng, xác nhận).
3. **P4 việc 7:** KPI vào ledger, so Tập 5; merge **squash** `ep006` → `main` (fetch trước; gồm F-13; 265 MB WAV), cập nhật PLAN kênh.
- Treo: lô K — `checks-appeal.md` A28; đề xuất qc nhà máy đọc đối trọng master ở đoạn thế giới; REG không so run trước (REVIEWER G2 §7); nghi vấn "none since" che mép dải cảnh báo S15 (B15).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · F-13 trên `ep006` · C4 rubric MỚI → `gates/C4-answer.md` · 10/10 P3c: việc nặng headless khoá Console (trần $170), không lượt đạo diễn, ≤ 10 ảnh/phiên, đẩy cả `ep006` và nhánh phiên; bỏ ngưỡng 300 nghìn ngữ cảnh cho P3c.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 r2–r3 | a–f | nghĩa B01 B04 B12 B15 B32 | séc ngang/lớn, "?" phần thiếu, mốc năm | B04 B12 1·1; B01 B15 0,5 | G2 trước/sau |
| C5 | a d e f | C14 | lớp tối vẽ trước chữ | 6/6 verify | — |
| C5b | hợp đồng, b d e f | CHẶN 13, CHÍNH 4 (run-c5) | sổ claim S07/S17, gói, huy hiệu S30, "starting month", mép 102, séc tắt trước thẻ | run-c5b ĐẠT; B04 B29 tụt | C5c |
| C5c | e (b) | B29 tụt (số thùng xám) | số thùng giữ ink | B29 1·1·1 | — |
| C5d | b, mô tả | REVIEWER: ngoại lệ V11 không có số đo hại; REVIEW-G1 #8 | "?" có tấm nền; câu tháng bỏ 10/2005 + 2 claim | run-c5d ĐẠT, V11 0 | — |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL **7.699/7.700** (P3c: 0). Agent con P3c: **0**.
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless | Giờ render |
|---|---|---|---|---|---|---|---|
| P3b | 2026-10-09 10:08 | 1,35 | 71,18 | 475,72 | 72,52 | 0,64 | ≈ 2,5 h |
| P3c | 2026-10-11 03:20 | 0,48 | 2,19 | 109,11 | **2,67** | xem chi API | 1080p ≈ 7,7 h (6 lần) · checks ≈ 10,3 h (4 lượt) |
**Chi API Console P3c (trần $170): ≈ $25,5** — Haiku $0,002 · kiểm mù ≈ $1,8 (cổng gốc r2–r4, C5b, đối chứng, C5c) · dựng X $4,01, Y $4,92, Z $4,56, C5b-A $3,50, C5b-B $3,31, C (thumbnail) $1,38 · REVIEWER G2 $1,98. Cộng tập ≈ 78 / 15 triệu (D-009: chỉ cảnh báo).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` (§6 giao hàng) 3. `episodes/ep006/PLAN.md` 4. `episodes/ep006/ledger.md` 5. `episodes/ep006/gates/G2.md` 6. `episodes/ep006/gates/REVIEW-G2.md` 7. `playbook/prompts/P3.md` (chặng P4) 8. `playbook/templates/HUONG-DAN-DANG.md`

**Tệp lớn ngoài git** (mất container → dựng lại trước khi giao): `cd toolkit/factory/world/vendor && npm ci` · `pip install "av>=12,<15" --only-binary=:all:` · `python3 episodes/ep006/data/fetch.py --verify` · `python3 episodes/ep006/world/derive.py && python3 episodes/ep006/c4/build_inputs.py --timeline && bash toolkit/build.sh episodes/ep006/episode.yaml && python3 episodes/ep006/c4/build_inputs.py --out` (≈ 2,8 h nền, trần 2 h → chạy lại, đoạn trúng cache); rồi `cp episodes/ep006/work/factory/SH{1,2,3}.mp4 episodes/ep006/out/shorts/`; kiểm SHA master = `f96da0ea…` (`review-g2/full-720p.mp4.sha256`).

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P4 (giao file). Nhánh ep006 (@ SHA đóng P3c hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Gói đã gửi: episodes/ep006/gates/G2.md (issue #51). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep006/gates/G2-answer.md, commit, push.
Chặng này: P3.md chặng P4 việc 5–7 (áp G2 → giao hàng → G3 → merge squash ep006 vào main) → dừng ở G3/merge (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Container mới thì dựng lại tệp lớn theo PLAN §6 trước (≈ 2,8 h nền) và kiểm SHA master. Việc nặng headless khoá Console (`episodes/ep006/c5/api.sh`, BƯỚC 0 như P3c); không chạy song song checks với render.
Câu trả lời G2:
<<DÁN CÂU TRẢ LỜI G2 Ở ĐÂY>>
```

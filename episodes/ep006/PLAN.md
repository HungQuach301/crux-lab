# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` (P3c đẩy cả `ep006` và `claude/gracious-brown-rccz2m`, cùng SHA) · **Đề tài:** #12 · **Format:** `101` · **Phiên vừa đóng:** P3c (`session_01QNrEnsRn8CMnf6J5ujL79c`) — đóng **giữa C5** (chốt an toàn: ngữ cảnh phiên ≈ 265 nghìn, sát ngưỡng 300 nghìn) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C4 xong.** Cổng gốc (rubric MỚI): **21/23 = 91,3 % ĐẠT**, `advice_stated` = 0 mọi lượt (`c4/ROOT-SUMMARY-P3c.md`); B04, B12 sửa bằng hình → 1·1; **B01, B15 hết 3 vòng (0,5) → G2 nêu trước/sau** (dải `review-c4/r1`, `r2`, `r3` → `strips/`); B32 trả về bản vòng 2 (khoá nghĩa). Nhận xét đạo diễn "Treo" đã sửa: khung chuyển máy 0,6–0,9 → 0 s; "44.3%" +0,08 s; nhãn outro chỉ ở đồ thị; **"3%" còn trễ 1,26 s** (quy tắc 7 × quy tắc 1, bậc 3 % sáng đúng "three" ở thế giới) → ngoại lệ G2 kèm số đo. **C5:** 1080p dựng xong **536,6 s = 8:56,6** (≥ 8:00, ≤ 9:00), 6/6 đoạn verify OK gồm **C14** (sửa: lớp tối vẽ trước chữ — ident a, mờ vào d/e/f); Shorts SH1–SH3 dựng. qc nhà máy 8 TRƯỢT: 6 giống Tập 5 đã đăng (đối trọng master "0 khung log", freezedetect, true peak −1,8 dBTP); **mới: SH1, SH3 móc ra ngoài vùng an toàn dọc (186 / 98 hộp)**. Checks đủ bộ lần 2 (cây C5 thật, `out/checks/run-c5`): TRƯỢT (CHẶN F10 F11 S03 S04 S07 S08 S10 S17 SH01–05) → **C5b** (lượt A hợp đồng/sổ claim/gói, lượt B hình) → `run-c5b`: **Tập ĐẠT, CHẶN 36/36, CHÍNH 13/13, F11 ĐẠT**, V11.plateOverGraphics 2.550. Cổng gốc lại trên nhịp đổi: B14, B30 1·1; **B04, B29 tụt 0,5** (đối chứng dải C4: 1·0,5, 1·1) → trả '?' không nền, bỏ lùi xám số thùng → C5c (đang dựng b, e).

## 2. Việc tiếp (≤ 3) và việc treo
1. **Checks đủ bộ trên cây C5** (`bash episodes/ep006/c5/checks_split.sh <ngoài repo>/chk-c5 --first`; dừng ở trần 2 h → `RESUME=1` cùng lệnh, cache trang theo cảnh): **F11 phải ĐẠT** (trượt → báo, quay lại K2); V11.plateOverGraphics chép cho REVIEWER; CHẶN/CHÍNH sửa trước G2. P3c: run-c5 TRƯỢT → run-c5b ĐẠT; C5c (b, e) cần checks lại + cổng gốc B04, B29; V11 S04 '?' → ngoại lệ CHÍNH có số đo nếu V11 trượt lại.
2. **Shorts:** sửa móc SH1 ("A raise every year, and still less") và SH3 ra ngoài vùng an toàn dọc (xuống dòng/ngắn hơn trong `episode.yaml shorts`, móc do máy chọn); dựng lại Shorts (`build.sh` trúng cache đoạn); ghi `contract.json shorts`. `sync_audit.py out/video.mp4 <ra.json> --spine …` mỗi đoạn ±0,2 s (ghi thêm: sfx tick đè "three" e 96,7 s SNR 14 dB — F-2 WARN).
3. **G2** (`P3.md` việc 4): gói ≤ 3 câu + phiếu L3 + REVIEWER (headless chỉ đọc, `c5/api.sh review`); nêu B01/B15 trước/sau, "3%" 1,26 s, true peak −1,8 dBTP (như Tập 5); clip ≤ 3 phút, bản 720p (`out/factory` phần 720p). Đóng phiên.
- Treo: P4 merge **squash** `ep006` → `main` (gồm F-13). Lô K: `checks-appeal.md` A28; đề xuất: qc nhà máy đọc đối trọng master ở đoạn world (0 khung log ở Tập 5–6).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · F-13 sửa trên `ep006` · **C4 rubric MỚI** → `gates/C4-answer.md` · 10/10 P3c: chi API qua khoá Console (`CONSOLE_API_KEY`, trần $170); không lượt đạo diễn; ≤ 10 ảnh/phiên; đẩy cả `ep006` và nhánh phiên.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 r2 | a–f | nghĩa B01 B04 B12 B15 B32; treo đạo diễn | séc ngang + viền séc đầu; hai séc chênh + "?"; vạch 90 %; thanh Ruth; khung máy | gốc r3: B32 tụt → trả bản cũ | — |
| C4 r3 | a–d | B01 B04 B12 B15 | séc lớn qua cả S01 (nốt theo hình); phần thiếu gạch + "?"; năm 5/20; mốc năm + "start month" | B04, B12 1·1; B01, B15 0,5 | G2 trước/sau |
| C5 | a, d–f | C14 chữ dưới lớp tối | lớp tối vẽ trước chữ | 6/6 verify OK | — |
| C5b | b d e f + hợp đồng | CHẶN 13, CHÍNH 4 | sổ claim, cờ S17, gói, huy hiệu S30, 'starting month', mép 102, séc tắt trước thẻ | run-c5b Tập ĐẠT; B04 B29 tụt | C5c |
| C5c | b, e | B04, B29 tụt nghĩa | '?' không nền; số thùng giữ ink | đang dựng | checks + cổng gốc |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL **7.699/7.700** (P3c: 0). Agent con P3c: **0** (lượt dựng/đọc chạy headless bằng khoá Console).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless | Giờ render |
|---|---|---|---|---|---|---|---|
| P3b | 2026-10-09 10:08 | 1,35 | 71,18 | 475,72 | 72,52 | 0,64 | ≈ 2,5 h |
| P3c | 2026-10-10 06:55 | 0,39 | 1,55 | 81,16 | **1,94** | xem chi API | ≈ 3,9 h (1080p 7.135 + 2.729 s; dải nhịp ≈ 0,5 h) |
**Chi API Console P3c (trần $170): ≈ $21,9** — C5b lượt A $3,50 · B $3,31 · cổng gốc C5b $0,28 + đối chứng $0,13 · Haiku thử $0,002 · cổng gốc vòng 2/3/4 $0,51 + $0,41 + $0,27 · dựng X $4,01 · Y $4,92 · Z $4,56 (Opus; token từng lượt ở commit 9895edf, 89e4e8c và log `c5/api.sh`). Cộng tập ≈ 76,7 / 15 triệu (D-009: chỉ cảnh báo).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `episodes/ep006/PLAN.md` 4. `episodes/ep006/ledger.md` 5. `episodes/ep006/c4/ROOT-SUMMARY-P3c.md` 6. `episodes/ep006/out/factory/qc.md` 7. `playbook/prompts/P3.md` 8. `playbook/templates/G2.md` (nếu có)

**Tệp lớn ngoài git** (mất container → dựng lại): `cd toolkit/factory/world/vendor && npm ci` (three) · `pip install "av>=12,<15" --only-binary=:all:` · `python3 episodes/ep006/data/fetch.py --verify` · `python3 episodes/ep006/world/derive.py && python3 episodes/ep006/c4/build_inputs.py --timeline && bash toolkit/build.sh episodes/ep006/episode.yaml && python3 episodes/ep006/c4/build_inputs.py --out` (1080p không cache ≈ 2,8 h: lệnh nền trần 2 h → chạy lại `build.sh`, đoạn đã dựng trúng cache).

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3d. Nhánh ep006 (@ SHA đóng P3c hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md và làm mục 2 (việc tiếp 1–3) đến G2, rồi đóng phiên theo D-011.
Container mới thì dựng lại theo PLAN §6 "Tệp lớn ngoài git" trước (1080p ≈ 2,8 h nền).
Việc nặng chạy headless bằng khoá Console (`episodes/ep006/c5/api.sh`, BƯỚC 0 như P3c); ghi chi API vào PLAN §5 sau mỗi bước; không chạy song song checks với render.
Ghi chú thêm của chủ dự án (nếu có):
<<DÁN GHI CHÚ Ở ĐÂY>>
```

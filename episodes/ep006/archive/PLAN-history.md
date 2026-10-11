# PLAN Tập 6 — lịch sử (bản PLAN cũ khi đóng mỗi phiên)


## Bản đóng P1 (G1, @ 2627822)

# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 (`topics-r1/machine/retire-1/`) · **Format:** `101` đề xuất (chờ G1) · **Phiên hiện hành:** P1 (`session_019BA5MXtsQ6jZqogoJGeCBF`) — đóng ở G1

## 1. Trạng thái
**G1 chờ** (issue [#48](https://github.com/HungQuach301/crux-lab/issues/48), gói `gates/G1.md`). Việc 0: SHA khớp hồ sơ, kiểm độc lập 43/43. C1: L1 3/3. C2 v2: kiểm máy ĐẠT trừ độ dài (ước 7:50, thiếu 24 s); kiểm mù vòng 2 6/6, khuyên 0, không khối ≥ 4/6; M1 3,6 · M2 27,5 · M3 13,9 · M4 6,06 · M5 33,3 · M6 0 s (bản đọc thật). REVIEWER ĐẠT có sửa (1 CHẶN + 4 CHÍNH đã sửa). 0 CHẶN/CHÍNH mở.

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời G1 → `gates/G1-answer.md`; ghi `taste-ledger.md`, `AUTHORSHIP.md`, ledger. Áp: (a) → chạy check với `--g1-short`; (b) → WRITER mới thêm ≈ 60 từ chất có nguồn + kiểm mù lại hồi 2–3.
2. **P2 → C3** (G1 dự kiến "cần C3"): ký hiệu mới N1 "hàng 10 thùng" (3D, `beats.md`) + **nhạc hiệu kênh** (clip có âm, `episode.md` §5b); cổng gốc; sửa bằng hình ba khối 2/6 (S31.2 phương pháp, S03.1/S06.3 định nghĩa, S09/S12 số dày) + 7 PHỤ `gates/REVIEW-G1.md`.
3. Khi `main` có khoá K mới (lô `checks-k40`, kind cho `K-brief.md`) → merge `main` vào `ep006`, chạy S01/S05; viết `contract.json`.
- Treo: lô K (`checks-k40`, chưa thấy trên origin lúc 15:00 UTC; `main` vẫn 447690e, LOCK d93276a4). Đề xuất sửa mẫu `playbook/templates/check_script.py`: khối M4 cắt ở khoảng lặng > 1,5 s (Tập 5 ước 13,5 → 9,1 s, đo 9,8) — chờ tổng kết Tập 6.

## 3. Quyết định đã có (chủ dự án)
- 08/10 D-011 Q1: Tập 6 = #12; G1 từng tập; Q3 phiên K lô song song (không mở K riêng).
- 08/10 lệnh P1: năm luật §2b, M4 hiệu chuẩn 2,75 từ/s, đề xuất format theo 2,52 từ/s không độn, claim-risk #12. G1: chờ → `gates/G1-answer.md`.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 v1→v2 | S18–S23 | mất chú ý "số dày" 6/6 (thập kỷ 94,8/99,5 %; PCE 19,2 %) | dự phòng: 12 câu → 3, số lên nhãn B19/B22, V7, mô tả; S30.5 đối trọng | 6/6, khuyên 0, khối ≤ 2/6 | độ dài −24 s |
| G1 REVIEWER | S08.1, S12.1–2, B08 | CHẶN-1 thùng của khoản đều không nguồn | "6 in 10 / 9 in 10" so khoản đầu của chính nó | check ĐẠT | — |
| G1 REVIEWER | S04.3, S31.3, nhãn góc | CHÍNH-2 "pays more money"; CHÍNH-5 thiếu "US consumer prices" | "compare the dollars both checks pay out"; "US consumer prices · US only" | check ĐẠT | — |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập: **15** triệu (trần = đầu vào mới + sinh ra, log phiên). EL ≤ 6.000 ký tự (dùng **1.114**) · ≤ 40 agent con (dùng **4**).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
Lấy bằng `python3 toolkit/usage/from_events.py --session session_019BA5MXtsQ6jZqogoJGeCBF --close episodes/ep006/archive/usage/p1-page*.json`; lượt đóng (áp REVIEWER, PLAN, issue) cộng ở phiên sau. Cộng P1 ≈ 0,89 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/G1.md` 7. `episodes/ep006/gates/G1-answer.md` (phiên kế tạo) 8. `playbook/prompts/P2.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P2. Nhánh ep006 (@ e677bf1 hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Gói đã gửi: episodes/ep006/gates/G1.md (issue #48). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep006/gates/G1-answer.md, commit, push; ghi taste-ledger.md, AUTHORSHIP.md, ledger.
Nếu main đã có khoá K mới (lô checks-k40, kind cho episodes/ep006/K-brief.md): merge main vào ep006 trước.
Chặng này: áp G1 → C3 (ký hiệu "hàng 10 thùng" + nhạc hiệu kênh, clip có chuyển động và âm) → dừng ở C3 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên"). Nếu G1 ghi "không cần C3" thì làm P3 → dừng ở G2.
Câu trả lời G1:
<<DÁN CÂU TRẢ LỜI G1 Ở ĐÂY>>
```

---

## PLAN khi đóng P2 (2026-10-08, trước P3)

# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên hiện hành:** P2 (`session_01VWvKx3ATmgiMnpR3FiPq12`) — đóng ở C3 · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C3 chờ** (gói `gates/C3.md`, issue [#49](https://github.com/HungQuach301/crux-lab/issues/49)). G1 áp (b): C2 v3 1.287 từ nói, ước 8:30, check ĐẠT không cờ; mid-roll đủ điều kiện theo ước (chốt thật ở P3). Kiểm mù lời v3: đúng 6/6, **khuyên 5/6 chấm gốc / 1/6 chấm trộn (v2 cũng 1/6)** → chủ dự án quyết. N1 hàng 10 thùng: S07/S24/S27 ĐẠT (vòng 2), **S29 trượt sau 3 vòng** (khuyên 1/2, giữ v2). Nhạc hiệu A/B + khúc đóng. 0 CHẶN mở; REVIEWER gói: `gates/REVIEW-C3.md`.

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời C3 → `gates/C3-answer.md`; ghi sổ gu, AUTHORSHIP, ledger; áp (S29, nhạc, kiểm mù/S04.2, EL).
2. **Chặn C4:** `main` chưa có khoá K gồm kind Tập 6 (K4.0.1 LOCK 79aeec0d đã merge, KINDS 6 loại cũ → S01/S05 MISSING). Có khoá → merge `main`, chạy S01/S05, viết `contract.json`. Không có → không mở C4, làm việc không phụ thuộc K (giọng cả tập nếu EL duyệt, đo độ dài thật ≥ 8:10, nhà máy F-12 trên `factory-*`).
3. P3: giọng cả tập (`story/voice_scenes.py`, chỉ cảnh chưa có take) → độ dài thật trên timeline ≥ 8:10 (thiếu → sửa trước render) → C4 → C5 (≥ 8:00, mid-roll hợp lệ) → G2.
- Treo: phiên K (kind Tập 6 + sửa luật cũ, `K-brief.md` có claim mới `worst_window_years_2pct_fell_20y`). Hàng chờ C4: lượt đạo diễn (S24 10–19 s đứng, S27 thanh thời gian thiếu mốc năm, S29 nhấn "month"), đồng bộ S24 5/7 · S27 7/8 · S29 4/7, C14 trên 1080p, 4 PHỤ `REVIEW-C2v3.md`. Lịch sử `ep006` có ≈ 265 MB WAV (df9c2d4) — chủ dự án quyết xoá.

## 3. Quyết định đã có (chủ dự án)
- 08/10 G1: L1 sửa · H-B + C2 v2 · `101` (b) ≥ 1.275 từ, ≤ 1 số mới · T1 · bài học T6-1 (đích 8:25 ước / 8:10 thật / 8:00 C5; dòng mid-roll ở G1) → `gates/G1-answer.md`.
- 08/10 lệnh P2: merge K4.0 ngay, không chờ phiên K; P3 không mở C4 khi `main` chưa có khoá K gồm kind Tập 6.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| G1 b | S16, S24, S27, S29 | độ dài 7:50 < 8:00 (mid-roll) | +93 từ: Carl/Edna theo năm bằng thùng; 1 số mới (20/20) | check ĐẠT, 8:30 (sau S27.5) | dư 12 từ |
| REVIEWER | S27.5 | CHÍNH-1 nghe sai nhân quả | "came at the end of her stretch … and at the start of his" | check ĐẠT | CHÍNH-3 S04.2 → C3 |
| C3 r1→r2 | N1 ×4 | khuyên 8/8 (tưởng khoản đều) | séc lớn lên ×1,02^k cạnh hàng | khuyên 1/8, nghĩa 8/8 | S29 |
| C3 r3 | S29 | khuyên 1/2 | trục tháng bắt đầu + séc cùng cỡ | khuyên 2/2 → loại | giữ r2, chủ dự án chọn |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL ≤ 6.000 (dùng **2.446**; cả tập ước 7.699 → hỏi ở C3) · agent con **12/40**.
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
| P2 | 2026-10-08 16:28 | 0,30 | 1,01 | 47,60 | **1,31** | 0,28 (30 lượt) | 0,34 h |
Log phiên (`list_events` kinds=result, `modelUsage` tích luỹ gồm agent con); lượt sau 16:28 (vòng 3, đạo diễn, REVIEWER gói, đóng) cộng ở P3. Cộng tập ≈ 2,5 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/C3.md` 7. `episodes/ep006/gates/C3-answer.md` (phiên kế tạo) 8. `playbook/prompts/P3.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3. Nhánh ep006 (@ 856bbd5 hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Gói đã gửi: episodes/ep006/gates/C3.md (issue #49). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep006/gates/C3-answer.md, commit, push; ghi taste-ledger.md, AUTHORSHIP.md, ledger.
KHÔNG mở C4 khi main chưa có khoá K mới gồm kind Tập 6 (KINDS trong checks/py/r_model.py; K4.0.1 LOCK 79aeec0d chưa có). Có khoá → merge main vào ep006, chạy S01/S05, viết contract.json rồi mới C4. Chưa có → chỉ làm việc không phụ thuộc K (áp C3, giọng cả tập nếu EL được duyệt, đo độ dài thật ≥ 8:10, nhà máy F-12 trên factory-*), rồi dừng và báo.
Chặng này: áp C3 → giọng cả tập → độ dài thật trên timeline ≥ 8:10 → C4 → C5 (≥ 8:00, mid-roll hợp lệ) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Câu trả lời C3:
<<DÁN CÂU TRẢ LỜI C3 Ở ĐÂY>>
```

## PLAN trước khi đóng P3b (thay ở 09/10)

# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên hiện hành:** P3 (`session_01JVoRpJ84UMpxj63PnNqCJ6`) — đóng **trước C4** (chưa có khoá K) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C3 đã áp, C4 bị chặn.** Câu trả lời C3 → `gates/C3-answer.md`. Giọng cả tập xong (EL **7.699/7.700**, ASR 30/30 không mất từ khoá). **Độ dài thật trên timeline 8:56,6 (536,6 s) ≥ 8:10 ĐẠT** (`story/timeline_len.py`, phép tính nhà máy; kiểm ngược Tập 5 465,67 s); ±5 % quanh trần `101` 9:00 (−3,4 s) → nêu tên; tốc độ thật 2,40 từ/s (ước 2,52). Mid-roll ≈ 3:27,7 sau S12.4, cách cuối 329 s → hợp lệ. F-12 xong trên `factory-f12` @ 9b0fb2d (test 92 OK), **chưa vào `main`/`ep006`** (quyền phiên chặn push `main` và merge). `main` @ 2c5eacf: KINDS vẫn 6 loại cũ → S01/S05 MISSING.

## 2. Việc tiếp (≤ 3) và việc treo
1. **Chủ dự án/phiên có quyền:** merge `factory-f12` → `main` (chỉ thêm, mặc định tắt, trùng byte tập cũ), rồi `main` → `ep006` (xung đột 2 dòng: F-12 `BACKLOG.md`, W10 visual-library README → lấy bản `main`).
2. **Có khoá K gồm kind Tập 6 trên `main`** → merge `main` vào `ep006`, chạy S01/S05, viết `contract.json`, rồi C4 (animatic 720p; `episode.yaml` đủ cảnh/shot; `audio: {close_lift_db: 12, ident: {after: S03}}`; S03 tail 4,0, S12 tail 1,5, S31 5, S32 2). Hàng chờ C4: lượt đạo diễn (S24 10–19 s đứng; S27 mốc năm; S29 nhấn "month"), đồng bộ S24 5/7 · S27 7/8 · S29 4/7, C14 trên 1080p, 4 PHỤ `REVIEW-C2v3.md`. **Chốt C4:** kiểm mù bản có lời cả tập + riêng S29, khuyên sản phẩm = 0, chấm song song rubric cũ + ba cờ, 2 người chấm; S29 không đạt → hỏi chủ dự án.
3. **K4.1 (V11, F11, rubric khuyên) phải có trên `main` trước C5**; chưa có → dừng trước C5 và báo.
- Treo: phiên K (kind Tập 6, khoá K4.0.2; K4.1). P4 merge **squash** `ep006` → `main` (≈ 265 MB WAV ở df9c2d4).

## 3. Quyết định đã có (chủ dự án)
- 08/10 G1: L1 sửa · H-B + C2 v2 · `101` (b) · T1 · T6-1 (8:25 ước / 8:10 thật / 8:00 C5) → `gates/G1-answer.md`.
- 08/10 C3: N1 + séc lớn lên duyệt S07/S24/S27 (W10); S29 (a) ngoại lệ, chốt C4; nhạc hiệu A + khúc đóng A, +12 dB sau chữ cuối (−14 LUFS, ≤ −1 dBTP); kịch bản v3 (a), "hỏi báo giá" = thận trọng chung; EL ≈ 7.700; squash ở P4 → `gates/C3-answer.md`.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| G1 b | S16, S24, S27, S29 | 7:50 < 8:00 (mid-roll) | +93 từ, 1 số mới | 8:30 ước → **8:56,6 thật** | gần trần 9:00 |
| C3 r1→r2 | N1 ×4 | khuyên 8/8 (khoản đều) | séc lớn lên ×1,02^k | khuyên 1/8, nghĩa 8/8 | S29 → chốt C4 |
| P3 | F-12 | điểm chạm khúc đóng mất dưới −20 dB | `music.post()` +12 dB/0,5 s sau chữ cuối; ident A 3 s | −14,0 LUFS · −1,0 dBTP · A07 19,97 dB | chờ merge `main` |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL duyệt **7.700** (dùng **7.699**) · agent con **13/40** (+1 P3: nhà máy F-12).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
| P2 | 2026-10-08 16:28 | 0,30 | 1,01 | 47,60 | **1,31** | 0,28 (30 lượt) | 0,34 h |
| P3 | 2026-10-08 23:46 | ≈ 0,03 | ≈ 0,25 | ≈ 8,20 | **≈ 0,28** (+ agent F-12 ≈ 0,18 chưa vào log lúc đó) | 0 | 0 |
P3 đọc từ `list_events` kết quả lượt 23:45 (`modelUsage` tích luỹ); lượt đóng và P2 sau 16:28 chưa cộng — cộng ở P4. Cộng tập ≈ 3,0 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/C3-answer.md` 7. `toolkit/factory/README.md` (F-12, sau merge) 8. `playbook/prompts/P3.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3b. Nhánh ep006 (@ 8a7c51b hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
C3 đã áp (gates/C3-answer.md); giọng cả tập xong, độ dài thật 8:56,6. Việc đầu tiên: nếu main chưa có F-12 thì merge factory-f12 → main (lấy bản main ở hai dòng xung đột), rồi main → ep006.
KHÔNG mở C4 khi main chưa có khoá K gồm kind Tập 6 (KINDS trong checks/py/r_model.py). Có khoá → chạy S01/S05, viết contract.json rồi C4. Chưa có → đóng phiên và báo.
K4.1 (V11, F11, rubric khuyên) phải có trên main trước C5; chưa có thì dừng trước C5 và báo.
Chặng này: C4 (chốt kiểm mù bản có lời cả tập + S29, khuyên sản phẩm = 0, rubric cũ + ba cờ, 2 người chấm) → C5 (≥ 8:00, mid-roll hợp lệ) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Ghi chú thêm của chủ dự án (nếu có):
<<DÁN GHI CHÚ Ở ĐÂY>>
```

---
## PLAN khi đóng P3b (chép nguyên khi đóng P3c, 2026-10-10)
# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên vừa đóng:** P3b (`session_01426YSqdhTHTztxkQ5Ax1jg`) — đóng **giữa C4** theo lệnh chốt an toàn (hạn mức tuần ≈ 6 %) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
F-12 + K4.0.2 + K4.1 trên `main` (9f16de0) và `ep006`; LOCK `4d688acd` khớp. `contract.json` (kind `fixed-raise-vs-index-windows`, `index.name: cpiu`): S01 89/0, S05 45/45 + 8/8. **Animatic 720p cả tập** (6 đoạn thế giới a–f): **536,6 s = 8:56,6** (≤ 9:00, dư 3,4 s), MR1 208,15 s, giọng 30/30 cache, EL 0; vòng sửa 1 bố cục xong, dựng lại @ ddf5bf1 (6/6 verify). F-13 (mux `-shortest` rơi khung) sửa trên `ep006`, bằng chứng `c4/f13/EVIDENCE.md`. **Kiểm mù C4** (rubric MỚI theo `gates/C4-answer.md`): bản có lời cả tập 0/3 · S29 0/3 `advice_stated` → **chốt C3 ĐẠT**; cổng gốc vòng 0 (trên bản trước sửa): `advice_stated` chỉ B08; nghĩa 0,5 ở B01 B03 B15 B32. Checks lần 1: luật Python — CHẶN còn F01 (720p) và F11 (chốt ở C5); đủ bộ (gồm trang) trên bản sửa: xem §2.1.

## 2. Việc tiếp (≤ 3) và việc treo
1. **Checks đủ bộ lần 1** trên bản @ ddf5bf1: nếu chưa có `checks-runs`/báo cáo commit thì chạy lại khi máy rảnh: `bash episodes/ep006/c4/checks.sh <ngoài repo>/chk-c4 --first` — **P3b chạy 2 lần, cả hai bị dừng ở trần 2 h của lệnh nền** (lần 2 máy rảnh) khi bộ lấy mẫu trang chưa xong → tách: `SKIP_PAGE=` chạy `node checks/page/sampler.js` riêng (nền, `K_JOBS=4`) rồi `SKIP_PAGE=1 checks/run.sh` cho phần Python; luật Python đã có (CHẶN còn F01, F11).
2. **Cổng gốc chỉ các nhịp B01 B03 B08 B15 B32** trên dải mới `review-c4/strips/` (đã sửa bằng hình vòng 1; luật 3 vòng, khoá nghĩa): `python3 c4/blind_c4.py read c4/root-r2 root --only B01,B03,B08,B15,B32` → `pack` → commit → `grade --graders 2` → tally `--advice-rubric new` (rubric cũ báo song song). Trượt → sửa bằng hình (vòng 2/3) → đọc lại; hết 3 vòng → G2 nêu trước/sau. Rồi lượt đạo diễn 2 lượt chỉ nếu đổi lớn.
3. **C5 → Shorts → G2**: `res: 1080` (C14, V11.plateOverGraphics cho REVIEWER), **F11 ĐẠT trên cây C5 thật** (trượt → báo, quay lại K2), `sync_audit.py` ±0,2 s, ≥ 8:00 và ≤ 9:00 đo lại sau mỗi lần dựng; Shorts SH1–SH3 (`episode.yaml shorts`, ghi `contract.json shorts`); gói G2 + REVIEWER; đóng phiên.
- Treo: lượt đạo diễn còn ghi — khung chuyển máy (đồ thị nửa ngoài khung ≤ 0,5 s), "44.3%" sớm 0,7 s, "3%" thang trễ 1,9 s (quy tắc 1 + 7), nhãn thêm "check: +2% a year" ở outro (B32). P4 merge **squash** `ep006` → `main` (gồm F-13). Lô K: `checks-appeal.md` A28 (mặc định rubric mới).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · 09/10 P3b: F-13 sửa trên `ep006` (điều kiện, bằng chứng) · **C4 rubric MỚI** → `gates/C4-answer.md` · Tập 4 không đăng, Tập 3/5 đã đăng (sổ gu).

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 l1 | c, f | F-2 chữ × chữ/đường | dời nhãn trục; số vào thanh | 104 → 0; 177 → 0 | — |
| C4 l2 | c, f | quy tắc 7 | mở 5 s ở thế giới | verify OK | — |
| F-13 | nhà máy | mux `-shortest` rơi 2–4 khung | bỏ `-shortest` | splice OK; Tập 5 trùng byte hình | vào `main` P4 |
| C4 r1 | a–f | cắt mép, đè chân trang, chồng nhãn, ident đen, Edna mất (hideColumn), khung tĩnh dài | `c4/FIX-R1.md` | F-2 0, mép 0 (phát lại) | đọc lại B01 B03 B08 B15 B32 |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL **7.699/7.700** (P3b: 0). Agent con P3b: **10** (cộng tập 23/40).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P3b | 2026-10-09 10:08 | **1,35** | **71,18** | 475,72 | **72,52** | 0,64 (126 lượt) | ≈ 2,5 h |
| P3c (đang chạy) | 2026-10-10 06:55 | 0,26 | 0,70 | 43,92 | **0,96** (sau cổng gốc vòng 4) | API Console bên dưới | 1080p đang dựng |

**Chi API Console (P3c, khoá `CONSOLE_API_KEY`, BƯỚC 0 đạt: apiKeySource = ANTHROPIC_API_KEY; trần $170):** thử Haiku $0,002 · cổng gốc vòng 2 (15 đọc + 4 chấm, Sonnet) $0,51 · dựng X (a–c, Opus, 83 lượt: vào 110 · ghi cache 158.937 · đọc cache 6,81 tr · ra 69.057) $4,01 · dựng Y (d–f, 95 lượt: vào 154 · ghi cache 181.236 · đọc cache 10,87 tr · ra 64.823) $4,92 · cổng gốc vòng 3 $0,41 · dựng Z (vòng sửa 3, 104 lượt: vào 140 · ghi cache 169.867 · đọc cache 9,79 tr · ra 61.955) $4,56 · cổng gốc vòng 4 $0,27 → **cộng $14,67**.
**Vượt mức cảnh báo ≈ 4,8 lần** (D-009: chỉ cảnh báo) — gần hết là agent con dựng/đạo diễn đọc nhiều ảnh (đạo diễn A 3.731 lượt công cụ). Cộng tập ≈ 75,5 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `episodes/ep006/PLAN.md` 4. `episodes/ep006/ledger.md` 5. `episodes/ep006/gates/C4-answer.md` 6. `episodes/ep006/gates/C4-intent.md` 7. `episodes/ep006/c4/FIX-R1.md` 8. `playbook/prompts/P3.md`

**Tệp lớn ngoài git** (mất container → dựng lại): `data/raw/*.csv` (CPIAUCNS `f79e3a78…`, CPIAUCSL `f8ecddf5…`, CWUR0000SA0 `27ceaacf…`, PCEPI `0f416a34…`) ← `python3 episodes/ep006/data/fetch.py --verify` · `out/video.mp4` 720p `0267f00e…` (1,1 GB), `out/audio/stems/*.flac`, `work/factory/world/{a…f}-720.mp4` (a `6006c569…` b `77b8afaf…` c `048b5b88…` d `54978488…` e `b45fc385…` f `57fdc9c9…`), `work/factory/music/bed.wav` `47ff2d28…`, `work/factory/SH{1,2,3}.mp4` ← `python3 episodes/ep006/world/derive.py && python3 episodes/ep006/c4/build_inputs.py --timeline && bash toolkit/build.sh episodes/ep006/episode.yaml` (nền, ≈ 1,5 h không cache) `&& python3 episodes/ep006/c4/build_inputs.py --out`. Checks cần `av` < 15 (`pip install "av>=12,<15"`; av 19 làm A12–A15, S18, R03, R07, V10, L1 ERROR).

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3c. Nhánh ep006 (@ SHA đóng P3b hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
C4 dở: animatic 720p đã sửa vòng 1 (536,6 s); cổng khuyên dùng rubric MỚI (gates/C4-answer.md) — bản có lời cả tập + S29 ĐẠT. Container mới thì dựng lại theo PLAN §6 "Tệp lớn ngoài git" trước.
Việc: (1) checks đủ bộ lần 1 nếu chưa có báo cáo; (2) cổng gốc chỉ B01 B03 B08 B15 B32 (luật 3 vòng, khoá nghĩa); (3) C5 (1080p, ≥ 8:00, ≤ 9:00, mid-roll hợp lệ; REVIEWER đọc V11.plateOverGraphics; F11 phải ĐẠT trên cây C5 thật, trượt thì báo) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Việc nặng chạy nền rồi giao agent MỚI đầu bài ngắn; không chạy song song checks với render/kiểm mù.
Ghi chú thêm của chủ dự án (nếu có):
<<DÁN GHI CHÚ Ở ĐÂY>>
```

## Bản PLAN khi đóng P3c-mở-rộng (2026-10-11) — trước khi viết lại
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

# REVIEW-G2 — Tập 5 (REVIEWER, 2026-10-08, nhánh `ep005` @ `c96cea4`)

**Kết luận: ĐẠT có sửa.** Video không có CHẶN. Các sửa dưới đây đều nằm ở giấy tờ (G2.md, explanations.json, sổ sách). Không cần dựng lại.

## R1 — không nêu số tiền phí PMI: **R1: 0**
- **Lời** (`out/script.json`, 68 câu, cả `text` lẫn `spoken`): có 0 số tiền hay tỉ lệ phí đứng cạnh PMI/insurance. S04.3 "this video puts no dollar figure on it", S06.3 "Taxes, home insurance and the mortgage insurance all come on top of it" đều không kèm số.
- **Hình:**
  - Lấy 155 khung từ `review-g2/full-720p.mp4` (cứ 3 s một khung) và đọc hết.
  - Thêm 8 khung S03.3 lấy dày (36–43 s) và 8 khung cuối S17 (387,5–391,5 s).
  - Có 0 vi phạm.
  - Chỗ sát nhất là S06 (≈1:51): "taxes, home insurance and PMI on top" nằm ngay trên "$2,362/month · principal + interest". Đây là khoản gốc + lãi có claim và ghi rõ PMI tính thêm, nên mục "Không tính" loại trừ nó. Không vi phạm.
  - S04 có nhãn "cost: not shown in this video", đúng R1.
- **Shorts** SH1/SH2/SH3 (35 khung): 0. **Thumbnail** 1/2/3: 0. **Tiêu đề** T1: 0. **Mô tả**: 0. Mô tả có câu "this video puts no dollar figure on it".

## Gen được bảo vệ (CHARTER §4): đạt
- **Không khuyên, không dự báo:**
  - Mọi khung có số đều có dòng chân "Past buyers, measured · not a reason to buy, rent or wait" hoặc "A measurement, not a next step".
  - Nhãn lựa chọn S01/S18.6 "buying now + mortgage insurance" / "still renting, still saving" là mô tả trung tính: không mệnh lệnh, không số.
  - Mốc "a plan" ở S18 có kèm "≈ 2 years matched the typical month — not the slow ones, not the lender's step". Đây là nghĩa thận trọng, không phải lời khuyên. Kiểm mù so đủ mẫu cũng cho khuyên 0/6 ở C5c.
- **"US only" và "history, not a forecast":** có trên mọi khung dữ liệu, ở thẻ phương pháp, cuối phim, trên Shorts, thumbnail và mô tả.
- **ILLUSTRATIVE:** có trên Owen, Grace, Victor, ví dụ $400,000, các khung luật, thumb-3 và cả ba Short.
- **"on paper":** có trên mọi số đếm, gồm 23 months, 13, 112, 14.7 %, "80% on paper", "from about 1 year to more than 9 years · on paper" và các thumbnail.
- **Phạm vi Fannie Mae:**
  - S03.3 nói "for Fannie Mae loans, that's a waiting period and a 75 percent bar". S12.3 nói "the 75 percent bar Fannie Mae sets for its loans … a separate route from the law's schedule". Cả hai đúng phạm vi.
  - Nhãn `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` **có trên hình**, nhưng chỉ ≈ 1,0 s (41,0–42,0 s, ngay trước khi cắt sang ba người mua).
  - Animatic C4 cũng vậy (≈ 41,4–42,4 s), nên không phải hồi quy. Lời và nguồn "Fannie Mae Servicing Guide B-8.1-04" đã mang phạm vi.
  - Không CHẶN. Ghi lại cho tập sau: nhãn nên hiện cùng chữ "Fannie Mae" (≈ 38 s).
- S12 có nhãn "Fannie Mae's early bar" và nguồn "Fannie Mae B-8.1-04". Đạt.

## Đối chiếu số trong G2.md với nguồn
| Mục G2 | Nguồn | Kết quả |
|---|---|---|
| CHẶN 35/35, CHÍNH 9/11 (F07, V11), Tập ĐẠT, khoá `d93276a4` | `run-c5c/report.md` | khớp. Master SHA `d2a04ca7…` khớp `out/video.mp4`; 720p `7a929ef7…` khớp `.sha256` |
| 7:46 | F07 465,67 s | khớp |
| 12/12 nhịp loại 1 ở C4; chốt chặn có lời S06 3/3, S13 3/3, khuyên 0 | `C4-root.md` | khớp |
| B02 6/6 so với 5/6; B18 5/6 so với 1/6 | `C5-root.md`, `c5/cmp-c4-c5c/scores.json` | khớp (tôi đếm lại 24 nhãn). Dải C5c cắt từ master `d2a04ca7` (`strips.json`). Phép so ghi trước (`b4b0356`), rồi mới chạy (`9886777`) |
| "kiểm lại 8 nhịp" | `strip-spans.json` | 8 mục, nhưng gồm cả N2: thực tế là 7 nhịp loại 1 + N2 (sửa 3) |
| ASR 20/20; S04 seed 1007; S15 seed 1006 | `asr-all.json`, `S04/S15-seeds.json` | khớp. Tôi chạy ASR medium.en lại trên master: S04 có "the lender if"; S15 "Grace bought" rõ; S05.1 "in dollars of the day" đúng |
| Nghiêng ≤ 2,21° | `fly-report.json` | 22 lần di chuyển kiểu fly, max 2,21°, tất cả pass |
| −14,0 LUFS / −1,9 dBTP | A01/A02 run-c5c | khớp |
| **nhạc dưới lời 19,6 dB; né dải 1–4 kHz 13,5 dB** | A07 = 19,53; A08 = 13,08 (run-c5c) | **sai: số của run-c5** (19,56 / 13,52) (sửa 1) |
| F08 không còn dải màu | F08 0,33 % ≤ 5 | khớp |
| Shorts 22,7 / 37,8 / 43,5 s, 1080×1920 | ffprobe; SH01–SH05 PASS | khớp |
| EL 1.672 (812 + 604 + 256); cả tập 10.850 | `ledger.md` | khớp: 1.234 + 410 + 4.887 + 938 + 1.266 + 443 + 1.416 + 256 = 10.850 |
| Token ≈ 7 triệu từ C3; ≈ 10 triệu cả tập | `ledger.md` | **không kiểm được**: tổng cột token của ledger chỉ ≈ 3,56 triệu, vì thiếu dòng sau C5b (sửa 6). Phần kiểm mù cộng từ các phiếu: C4 ≈ 1,02 triệu + C5 ≈ 0,74 triệu ≈ 1,8 triệu. G2 ghi "≈ 2,0", chấp nhận được |
| P01 4 chữ < 90 px | run-c5c | khớp |

## Thay đổi từ C4 (nghĩa và R1)
- **S05.1 "in dollars of the day"** cùng chân "All $ in dollars of the day" và "median new home sold Q2 2026: $410,700": nhất quán với lời "a little under the national median price of new homes sold from April through June". Không đổi nghĩa, R1 sạch.
- **Nhãn lựa chọn S01/S18.6:** trung tính, không số, không khuyên. Đạt.
- **Màu người mua mới** (Grace hồng, Owen tím nhạt, Victor xanh bạc hà):
  - Rõ và nhất quán trong video và Shorts.
  - Riêng **thumb-3** tô Victor màu **xanh dương**, trong khi xanh dương ở video là đường chỉ số giá và màu nhấn. Không chặn, chỉ nên thống nhất nếu còn thời gian.
- **Tấm nền (plates):** chữ dễ đọc. Đây là gốc số đếm V11 (xem sửa 4).

## sync_audit đoạn d (S15–S20)
- **`a5.renting`:** cue trong `world/c4/d-s15-s20/spine.json` vẫn mang nhãn cũ "keep renting, keep saving". Chữ trên hình (scene.js dòng 191) đã là "still renting, still saving", nên kiểm đồng bộ tìm không ra chữ, tức báo trượt giả. Trên hình, hai nhãn hiện đúng lúc (khung 144–145). Không ảnh hưởng video, chỉ sửa sổ (sửa 8).
- **`v3.show`:** "not in this data" hiện mờ, chỉ ≈ 0,5 s ở cuối S17 (≈ 388,5–389 s), sau chữ "show", rồi cắt. Lời "this data can't show" và ngôi nhà có "?" đã mang nghĩa, nên không quan trọng với nghĩa. Ghi lại cho tập sau.

## Mô tả (`out/package/description.md`)
- Chương khớp với các act trong `out/timeline.json`:
  - 0:00 cold-open;
  - 0:58 act1 (58,0);
  - 3:09 act2 (189,03);
  - 5:21 act3 (321,67);
  - 7:14 method (434,97: làm tròn xuống 0,97 s, chấp nhận);
  - 7:25 outro (445,73).
  - Mọi chương ≥ 10 s.
- Số khớp claim: 23 months, 307 tháng (01/1991–07/2016), 403 tháng (01/1991–07/2024), 80 %/78 %, 4902, B-8.1-04. "We" chỉ người phân tích.
- Không lỗi chính tả. Lỗi lặp "months months" đã sửa ở `77d1f7b`.
- Không cần sửa.

## Sửa (cũ → mới)
**G2.md**
1. `nhạc dưới lời 19,6 dB, né dải 1–4 kHz 13,5 dB` → `nhạc dưới lời 19,5 dB, né dải 1–4 kHz 13,1 dB`
2. `mọi số 80 % kèm "on paper";` → `mọi số đếm (23 months, 14.7 %, 13/112 months) kèm "on paper";` (thumbnail không có số 80 %)
3. `kiểm lại 8 nhịp có hình đổi đáng kể` → `kiểm lại 7 nhịp loại 1 có hình đổi đáng kể (+ N2)`
4. Dưới gạch V11, thêm: `CHÍNH chưa sửa → theo CHARTER §5 cần anh chấp nhận ngoại lệ (A22 mới là đề xuất).` Dòng **Trả lời gọn** thêm ` · V11: chấp nhận/sửa`.
5. Thêm một dòng về các bản trước/sau mà C4-root đã hứa: `revert-B02/B18.mp4: thay bằng phép so đủ mẫu C5c (giữ C5c); S13 giữ bản v2 — trước/sau ở review-g2/revert-B13.mp4 nếu anh muốn xem.`
6. Mục **Số đo**: `Token ước ≈ 7 triệu` → `Token ước ≈ 7 triệu (ledger chưa ghi đủ: tổng cột hiện ≈ 3,6 triệu)`, **hoặc** bổ sung `ledger.md` các dòng còn thiếu:
   - các vòng kiểm mù C4 r1/r2/r3/b11;
   - C5b/C5c dựng;
   - C5b r1/r1x/voiced;
   - C5c r2;
   - cmp-c4-c5c 296.448 + 46.325;
   - REVIEWER G2.

**out/explanations.json**
7. `"_about": "C5b (out/checks/run-c5b, LOCK d93276a4)…"` → `"_about": "C5c (out/checks/run-c5c, LOCK d93276a4)…"`; trong `V11`: `"2,605 samples"` → `"2,612 samples"`. Mục `S09` đã cũ: S09 là CHẶN và đã PASS, nên **xoá** mục này. Nếu muốn giữ để tham khảo thì `"0 extra ElevenLabs characters in this build"` → `"EL 256 characters (ledger, C5)"`.

**Sổ sách (không ảnh hưởng video)**
8. `world/c4/d-s15-s20/spine.json`: `"a5.renting": "keep renting, keep saving"` → `"a5.renting": "still renting, still saving"`.
9. `out/voice/takes.json`:
   - S04 `"raw": "voice-takes/0ecc4f7fd0ca5b35.mp3"` → `"voice-takes/68d5dbe4da841180.mp3"`;
   - S15 `"raw": "voice-takes/98a63f707efd4dfa.mp3"` → `"voice-takes/b0d912d29478ac29.mp3"`.
   - Hiện đường dẫn trỏ vào take seed 1005 nhưng trường seed ghi 1007/1006. Master thực tế dùng take mới (đã kiểm bằng ASR). Cùng lỗi cũ ở `review-c4/asr-all.json` cho S05/S15.

## CHẶN trong video: không có.

# Đầu bài sửa C4 Tập 7 — vòng 3 (P3, 11/10): sau cổng gốc C4 r1 + đạo diễn lượt 3. KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push**. Không in, không ghi khoá API.
**Chỉ sửa tệp trong `episodes/ep007/world/c4/{a-s01-s03,b-s04-s09,e-s21-s24,f-s25-s28}/`**. Không sửa `world/c4kit.*`, `obj7.js`, `c3kit.*`, `derive.py`, claims (đoạn c, d, g giữ cache). Cần kit → dừng, mô tả.
**Chạy được lệnh kiểm**: dùng lệnh đơn, không `cd … &&`, không ống phức tạp (lượt trước Bash bị chặn): `python3 episodes/ep007/world/c4/<đoạn>/spine.py`, `python3 toolkit/tests/comment_guard.py episodes/ep007/world`, `node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>`, `ffmpeg -v error -y -ss <t> -i <mp4> -frames:v 1 <png>`.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C3 r3 | S21 | lớp trả thêm `ink` trên ô: "all blocks white" | lớp phủ 72 % | không thấy lớp | CHÍNH (C3 câu 1) |
| C4 v1 | S21 | — | tấm dày phát sáng rơi | thử nhanh 2/2 "tiles turn white" | |
| C4 v2 | S21 | — | tờ đô la 62 % ô trên mỗi ô | **cổng gốc r1 B21: nghĩa 2/2 nhưng `extra_layer_seen` 0/2** ("no slab described"; có lời: "green fill vague") | vòng 3 = vòng cuối → hết thì G2 nêu trước/sau |
| C4 r1 | B01 | chồng dừng ở 1 bó (hàng chờ C3 §3) | | **nghĩa 0,5 · 0,5**: "misses stack growing per beat" | |
| C4 r1 | B09 | | tháp thu khi về thế giới | **0,5 · 0,5**: "misses extra section lifting off to become the stack" | |
| C4 r1 | B23 | | xấp 12 tờ ở hàng sau | **0,5 · 0,5/1**: "block mechanism only loosely", "fence" | |
| C4 r1 | S25 có lời | | bóng tách, bỏ nét đứt | **`must_beat_or_guaranteed` 2/2** ("the bar that any other use has to clear/beat") — phần lớn từ lời S25.4–S25.5 (đã duyệt, không đổi ở vòng này) | sửa hình + nhãn (C3 câu 5) |

Kết quả đủ: `c4/root-r1/tally.md`, `c4/voiced-r1/tally.md`; lời đạo diễn lượt 3: `c4/director-r3.out` (đọc; **chỉ áp phần không trái quyết định C3** — xem dưới).

## Sửa
1. **S21 (CHÍNH, vòng 3 — đổi loại hình lần cuối: cận cảnh MỘT đơn vị).** Người tắt tiếng phải tả: *"each month's tile gets an extra bill put on top of it"*.
   - Ở "$733"/"add" (S21.3; xem spine): **máy đẩy vào cận cảnh cột đầu**: một ô tháng tối (`ink-muted`) chiếm ~1/4 khung; **một tờ đô la to, xanh tiền, sáng, có bóng đổ** hạ xuống nằm trên ô (≈ 70 % cạnh ô, nổi rõ, thấy cạnh dày); nốt dữ liệu; giữ ≥ 1,2 s. Rồi máy lùi ra trong khi tờ tiền rơi vào từng cột theo nhịp (như vòng 2); ô trễ rút về từng ô khi tiền tới; khung cuối: lưới hai màu, **mỗi ô tối có một tờ tiền sáng nằm trên** thấy được ở 720p (tờ đủ to, tương phản cao, máy 3/4 vừa đủ gần).
   - Đạo diễn lượt 3: nhãn "about 15 months late" màu amber đè lên ô amber → **đặt trên nền tối** (plate) phía trên vách; tờ tiền không chồng ở cột 1 trước khi lời nói tới phần trả thêm; tên "Tessa · ILLUSTRATIVE" không chạm mép lưới.
2. **S23:** tấm/tờ không lơ lửng lạc (khung 1,3 s cảnh như lỗi dựng) — nằm yên trên ô rồi nhấc theo một quét có thứ tự; **khối năm đi theo đường**: xấp thứ N hạ đúng ô 12, 24, 36… (không đứng sẵn thành "hàng rào" ở mép sau), các ô giữa hai xấp mờ đi (tháng không có trả thêm); không đổi góc máy giữa câu (mở bằng góc S21 kết thúc); 4 ô trễ: máy đẩy vào vách khi chúng sáng, Tessa quay về phía đó.
3. **S01 (B01 "grows by one bundle on each beat"):** chồng **lớn dần 3–4 bó theo nhịp trong S01.1** (chế độ thế giới, từ cửa nhà, chạm tường nhà), **dừng trước "$320,000"** (S01.2 — giữ sửa C3: không mọc trong lời số tiền vay); nhãn giá vẫn ở 5,94 s (C3 câu 3 = a, không đổi); chồng sát tường nhà, không trượt xa khi máy lùi (đạo diễn #3).
4. **S06** (đạo diễn #1, #2): ngoặc/vạch "fallback" mờ gần như đen trên đen ở ~2,7 s → sáng lên đủ đọc; **bỏ cú nhảy khung ~13,5 s** (nhà + Tessa biến mất, thanh nhảy trái, nhãn $2,948 sát huy hiệu ILLUSTRATIVE, rồi bật về ở ~18,9 s) — giữ một khung; lát bay đều đặn từ "Over" (giữ sửa C3: chồng chỉ dựng từ S06.3).
5. **S09 (B09 "the extra top section lifts off and lands beside Tessa's house as the stack"):** phần chênh (warn) trên tháp 30-năm-trả-15 **nhấc lên rõ ràng** (máy theo, đường bay thấy được, chạm đúng the stack cạnh nhà, nốt), tháp 15 năm đứng cạnh để thấy "phần dôi"; nhãn "difference = the stack: $21,622" đi cùng phần nhấc.
6. **S25 (C3 câu 5: không đọc ra "phải vượt / guaranteed"):** giữ thiết kế C3 (bóng tách, không cầm sát thanh, không xà) — **không** áp ý đạo diễn "Tessa giơ đô la sát đầu thanh" (trái C3). Sửa:
   - thước: vạch 0 ở sàn + một vạch "7.40%" đúng độ cao thanh (đạo diễn #2), thanh trồi từ tường nhà;
   - "interest no longer charged, not an investment return": **bằng hình** — một đồng lãi (interest) sắp rơi vào nhà bị tờ đô la trên thanh chặn lại rồi mờ đi ở "no longer pays" (đạo diễn #3), rút bớt chữ;
   - bóng "any other use": nhãn kèm chữ **"not tested"** ngay cạnh bóng (bóng = câu hỏi để mở, không phải đối thủ phải vượt); bóng không đứng ngang thanh ở khung nào giữ > 0,3 s.
7. Đồng bộ: giữ mọi cue ±0,2 s; tổng timeline 602,70 s không đổi.

## Kiểm (bắt buộc chạy, như đầu file)
comment_guard; `spine.py` của a, b, e, f; smoke a, b, e, f (0 lỗi JS, 0 chồng chữ, 0 ra mép, 0 quy tắc 1). Có thể trích ≤ 8 khung từ `work/factory/video.mp4` (bản r1) để so.

## Trả về (≤ 25 dòng)
Mỗi mục đã làm gì (S21: một câu mô tả hình mới cho ý đồ kiểm mù); kết quả kiểm; rủi ro.

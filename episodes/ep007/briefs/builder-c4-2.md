# Đầu bài dựng C4 Tập 7 — lượt 2/2 (P3, 11/10): đoạn c (S10–S15), d (S16–S20), e (S21–S24), f (S25–S28), g (S29–S33). KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push** (phiên chính commit). Không in, không ghi khoá API ra đâu.
Lượt 1 đã viết khung cả tập (`episode.yaml` với `world:` 7 đoạn, `c4/build_inputs.py`, `world/c4kit.{py,js}`, `world/music/`, `contract.json`) và đoạn a, b — **đọc chúng trước, dùng lại, không viết lại** (sửa khung chỉ khi đoạn c–g cần; ghi lý do).

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 r3 | S21–S24 | số dày 3/6 | "195 months", "$8,792" chỉ trên hình | checker ĐẠT 9:54 | đo lại C4 |
| C3 r3 | S21, S23, S25 | ô trễ sót, teal = "còn nợ", "guaranteed / has to beat" | N1 `ink-muted`/`ink`/`warn`, gom 12 lớp, bóng đô la tách | cổng gốc 5/5 2/2, stated 0 | hàng chờ C4 (dưới) |
| C4 l1 | a, b | (xem `PLAN.md` §4 / kết quả lượt 1) | | | |

## Đọc
`episodes/ep007/briefs/builder-c4-1.md` (luật chung, ràng buộc) · tệp lượt 1 viết · mẫu Tập 6 `episodes/ep006/world/c4/{d-s13-s23,e-s24-s29,f-s30-s32}/` · Tập 7 `story/script.md`, `story/beats.md`, `numbers.md`, `world/{c3kit.*,obj7.js,claims.json,derive.py}`, `world/c3/README.md` + `world/c3/{s21-track,s23-track,s25-bar}/` (bản C3 đã duyệt có điều kiện — giữ ý hình), `gates/C3.md` §2–§3, `gates/C3-answer.md`.

## Làm
1. Đoạn **c–g** theo beats.md (B10 V3 "one assumed rate" vs hai đường thật + lưới V1 1.833 ô, ô cuối = Tessa; B11–B12 V3 + V6 có nhãn; B13–B15 W2 hàng chồng theo tuần + W5 dải đỉnh, Tessa trong số ít tuần cao; B16–B20 tách thập kỷ, ngoặc khoảng cách; B21–B24 N1 Month track; B22 mức khoản bắt buộc đứng yên; B24 chồng lãi nhỏ + một tờ đô la từ tay Tessa; B25–B28 the bar + lịch sử lãi 30 năm; B29–B30 Leo bên trái Tessa; B31 ô thứ ba trống; B32 thẻ V7; B33 quay lại khung cold open, hai thẻ nhập thành "15-year + a fallback"). 8 quy tắc hình–âm; chữ tối thiểu (nhãn ≤ ~8 từ, ≥ 48 px ở 1080, hiện ≥ 1 s/3 từ).
2. **S21 — lỗi CHÍNH của C3 (câu 1: "lớp trả thêm không thấy bằng hình = lỗi CHÍNH, C4 phải sửa và kiểm mù lại").** Đạo diễn r1 + r3 và 2/2 người đọc r3 tả lưới là "all blocks white": lớp trả thêm `ink` trên ô bắt buộc `ink-muted` không tách được. Sửa **bằng hình trước, nhãn là cách cuối** (D-009); vòng này phải **đổi loại hình** (lessons T6-7: vòng trước trượt cùng câu trả lời) chứ không chỉ chỉnh độ sáng:
   - lớp trả thêm là **vật riêng có độ dày** (tấm nổi rõ trên mặt ô, cạnh bên thấy được từ góc 3/4 — không nhìn thẳng xuống lúc lớp phủ), **rơi/trượt vào từng cột** theo nhịp (mỗi cột một nốt), khác hẳn ô bắt buộc về độ sáng (ô bắt buộc tối hẳn xuống khi lớp phủ tới, lớp phủ phát quang) — người xem tắt tiếng phải tả được "something extra is added on top of each month";
   - **nhân quả đúng thứ tự**: các cột lấp tới vách 15 năm trước, rồi ô trễ mới hiện quá vách (đang hiện trước khi cột tới vách); sau đó lớp trả thêm phủ, ô trễ rút về và tắt trước nhãn (giữ quy tắc vòng 3: không khung nào vừa đủ lớp phủ vừa còn ô warn);
   - thêm nhãn "about 15 months late" (beats B21, chưa lên hình ở C3) cạnh ô trễ;
   - **lệch làm tròn**: hình đang có "$2,216 required + $733 a month" (người đọc cộng ra $2,949 ≠ $2,948 ở S06). Dùng dạng không mời phép cộng sai, qua claim (vd "$733 extra on top of the $2,216 required" kèm "about"; hoặc hiện $2,948 đúng claim `pay30on15_now` làm tổng) — số chỉ qua `display` của claim, thêm claim/khoá ở `derive.py` nếu cần (ghi lý do).
3. **S23** (`gates/C3.md` §3 #5): không đứng yên ~6 s đầu — **thấy lớp tháng trước khi gom** (các lớp mỏng hằng tháng hiện ngắn rồi trượt về ô thứ 12); khối năm đọc được là **12 lớp** (khe giữa lớp, đếm được ở 720p), không nằm lẫn ở hàng đầu; **lưới không đổi màu không lý do**; 4 ô trễ to hơn, **không khuất sau vách** (máy hoặc vách mờ). Nhãn làm tròn: "$8,792 once a year (12 × $732.67)" hoặc "about $8,800 once a year" (claim `yearly_lump`; chọn một, ghi lý do). Nhịp Q3 phải giữ được câu đối trọng S24.2 trên hình (B24) — **không hình nào nói "trả tháng tốt hơn trả năm"** (chốt C3 câu 2: bản có lời kiểm mù `advice_stated` = 0).
4. **S25** (`gates/C3.md` §3 #6; chốt C3 câu 5: bản có lời không còn "phải vượt / guaranteed"): 7,40 % có **thang độ cao** (vạch đo sàn → thanh có khắc), không chỉ chữ; **bóng "any other use" không bao giờ dừng ngang mép thanh** (đọc thành "hoà mốc") — chuyển động liên tục qua lại cả trên lẫn dưới, kể cả khung cuối đoạn/đuôi; **nhãn "any other use" đi theo bóng**; gộp 4 khối chữ bên phải còn ≤ 3 (giữ đủ ý: before taxes · interest no longer charged, not an investment return · not tested: how any investment compares, once risk and taxes count). Không xà/cột đỡ, không "trèo qua" (G1 câu 1).
5. **Đồng bộ ±0,2 s** (`sync_audit`, C3 r3): S21 `a0.pay` +0,50 · S23 `a0.once` +0,37, `a1.extra` −0,31 · S25 `a0.charged` −0,20, `a3.measured` −0,30 → mỗi cue hình đúng đầu từ của spine.
6. Tessa: cử động nhỏ đúng lúc vật chạm/dâng (như lượt 1). Leo (S29–S30): ILLUSTRATIVE, nhà bên trái, ngày "Jan 2021".
7. Thẻ góc nguồn "Freddie Mac…" ở cảnh mô phỏng S21/S23/S25: xét tiêu đề nguồn hợp với cảnh (mô phỏng trên lãi tuần Oct 8, 2026); giữ "US only · history, not a forecast" và ILLUSTRATIVE (luật kênh).

## Ràng buộc cứng
Như lượt 1: không đổi chữ kịch bản, không sinh giọng (33/33 take cache), `lab` ≤ 11:00 cứng, số chỉ qua claim, gen được bảo vệ, **không render** (chỉ comment_guard, spine + kiểm quy tắc, spec, `numbers_said.py`, `build_inputs.py`, đo timeline), không sửa `checks/`, `toolkit/`.

## Trả về (≤ 25 dòng)
Tệp đã viết/sửa; tổng timeline (s), MR1/MR2; kết quả lint/spine/spec; S21 đã đổi loại hình thế nào (một đoạn mô tả để phiên chính viết ý đồ kiểm mù); S23, S25 làm gì; đồng bộ dự kiến; rủi ro; **lệnh build chính xác** cả tập.

## Kết quả lượt 1 (đọc trước khi làm)
Ranh giới (s): a 0–54,93 · b –189,33 · c –294,17 · d –358,60 · e –442,70 · f –489,20 · g –602,70; MR1 188,58, MR2 441,94; số neo S06.1, S18.1, S28.1 (lặng 0,75 s trong đuôi cảnh trước). Lượt 1 đã khai `contract.json coverage` = 1.833 tuần ở hồi 2: **đoạn c phải gắn `case` theo tuần cho vật dữ liệu** (lưới V1 / hàng chồng), nếu không S06 của checks trượt. Kiểm khai: `node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>`. Thay khung tối thiểu c–g bằng đoạn thật.

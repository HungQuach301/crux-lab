# C3 · Tập 7 — năm đoạn thế giới 3D (the stack · N1 Month track · the bar)

Ý đồ cổng gốc: `../../gates/C3-root-intent.md`. Mẫu: Tập 6 C3 (`episodes/ep006/world/c3/`). Lời thật (Eric, ElevenLabs `eleven_v3`, seed 1007) — mỗi cảnh một take,
`voice_c3.py` → `voice-scenes.json` (take, độ dài, ký tự, chữ take == lời kịch bản); take commit ở `episodes/ep007/voice-takes/`.
Mốc giờ chỉ từ `spine.json` (đầu từ theo năng lượng, `../wlib.py`); ≥ 5 s đầu ở thế giới; mọi số/nhãn so sánh chỉ ở đồ thị; mỗi động tác máy có lý do + âm;
mỗi lần vật đổi trạng thái = một nốt dữ liệu (`../c3kit.py steps`, cao độ = giá trị; nốt "trễ" có bội âm sáng `over`). Số trên hình chỉ qua `../claims.json`.

| Đoạn | Nhịp · cảnh | Hình |
|---|---|---|
| `s01-stack` | B01 KEY-1 · S01 | Tessa cạnh nhà; the stack (W2) hiện cạnh nhà, +1 bó ở mỗi nhịp lời (6 bó) → đồ thị: "$120 a month" trên chồng, "$320,000 loan · week of Oct 8, 2026" trên nhà |
| `s06-stack` | B06 KEY-3 · S06 | (vòng 2) hai thanh khoản trả (ink): 15 năm, 30 năm (ngắn hơn); "finishing" vạch mức 15 năm (ink-muted) qua cả hai → đồ thị (sau "takes"): "$2,828 a month" ở vạch, "required: $2,216 a month" trên thanh 30 năm; "forty" thanh 30 năm dâng tới $2,948, lát warn trên vạch, "30-year paid in 15: $2,948 a month"; "+$120 a month"; "same" → mỗi nhịp lát tách khỏi đỉnh thanh 30 năm bay sang chồng (15 bó), "the stack: $21,622 extra paid over 15 years" |
| `s21-track` | B21 KEY-9 · S21 | **N1** từ nhà Tessa: 15 cột-năm × 12 ô → vạch 15 năm → đồ thị: 14,6 ô warn quá vạch ("about 195 months", "about 15 months late") → lớp trả thêm phủ từng cột, ô trễ tắt dần, đường xong đúng ô 180 ("to finish in 180 months: +$733 a month") |
| `s23-track` | B23 · S23 | **N1** (trạng thái cuối S21): mỗi cột-năm gom 12 lớp mỏng thành MỘT khối trên ô thứ 12 → 4 ô warn quá vạch ("$8,792 once a year", "ends in 184 months: 4 months later") |
| `s25-bar` | B25 KEY-10 · S25 | đô la trả thêm từ tay Tessa đặt lên the bar (W3 `Beam`, ink-muted) đang sát sàn; thanh dâng tới độ cao lãi → đồ thị: vạch đo sàn→thanh, "the bar: 7.40% a year, before taxes", "interest no longer charged, / not an investment return" (hai dòng), đô la thứ hai "any other use" **đặt áp vào đầu thanh, ngang thanh** (không trèo/vượt — G1 câu 1), "not tested: whether any investment clears it". Không có lợi suất đầu tư nào |

## N1 Month track (`../obj7.js`, `MonthTrack`) — vật thể mới
- Một ô low-poly = **một khoản trả tháng**; mọi ô giống hệt; trái → phải = thời gian. Tham số: `n` (180), `cols` (12), `spare` (cột dự phòng cho ô trễ);
  `.set({lit, late, extra, gathered, yearly, markA, pulse})`; `userData.checks` trên ô / lớp / khối / vạch như `obj6.js`.
- **Bố cục: lịch 15 cột × 12 ô (cột = một năm), không phải một hàng 180 ô.** Lý do: (1) một hàng 180 ô ở 1080p chỉ ~9 px mỗi ô — không đếm được
  15 hay 4 ô trễ; lưới cột-năm cho thấy ngay "15 năm đủ" + "thêm hơn một năm" (14,6 ô = một cột đủ + 2,6 ô) hoặc "4 ô"; (2) "khối mỗi ô thứ 12"
  thành một hàng khối dọc mép sau — đọc thành "mỗi năm một lần" không cần chữ; (3) cột vẫn nối trái → phải = thời gian (§1), vạch 15 năm là thanh
  đứng yên dọc sau cột 15. Đồ thị = máy nhìn gần thẳng xuống lưới (nghiêng ~27°, tiêu cự dài) để đếm ô; thế giới = đường lát chạy từ cửa nhà.
- Ô trễ sáng theo PHẦN như W10 (14,6 → 14 ô đủ + ô thứ 15 sáng 60 %; số tháng không làm tròn trên hình, nhãn ghi "about 15").
- **Màu** (E2, beats.md Colour roles): ô thường `ink` (khoản trả); ô trễ `warn` (trễ — đúng vai "late months on N1"); vạch 15 năm `ink-muted` (mốc cố định).
  **Lớp/khối trả thêm = `cushion`.** Lý do: phần trả thêm ($733) là tiền lấy từ chính "khoảng dự phòng" mà khoản 30 năm chừa ra (vai `cushion` =
  "the fallback room") — tô cushion cho thấy trả thêm là tự nguyện, có thể bỏ trong tháng khó; `ink` sẽ hoà vào ô bắt buộc, `warn` đã là "trễ",
  `accent` chỉ cho lãi thị trường, `costlier` không dùng. Lớp phủ 72 % mặt ô để vành `ink` của khoản bắt buộc vẫn thấy ("on top of the required payment").
  Khối năm = cùng mặt cắt, cao đúng 12 lớp (cùng thể tích = cùng tổng tiền, S23.2 "the same total"). Rủi ro đã biết: hũ đệm Tập 2 (cushion) từng bị
  đọc thành "tiết kiệm" → xem kết quả cổng gốc.
- Không chữ trên ô; số tháng chỉ ở chế độ đồ thị, qua claim (`months_at_pay15_now`, `months_late_at_pay15_now`, `monthly_extra_months`, `yearly_lump_months`).

## The stack, thanh khoản trả, the bar
- **The stack** (W2): bó mệnh giá CỐ ĐỊNH = một năm của khoản dự phòng (`extra_vs15_total_now / 15` ≈ 12 × $120); 15 bó = $21,622; bó `warn`
  ("the stack's bills"). S01 thêm 6 bó theo nhịp lời (không nhãn tổng); S06 15 bó, mỗi bó rơi từ phần warn của thanh 30 năm (một năm của phần dôi).
- **Thanh khoản trả** (`PayBar`, obj7.js): `ink`, phần trên mức khoản 15 năm `warn`; thang USD/tháng riêng với thang của chồng (hai đại lượng khác nhau,
  mỗi cái có nhãn số ở đồ thị).
- **The bar** (W3 `Beam`, `ink-muted`, dày ×2,2 để đọc ở 540p): độ cao = lãi (0,3 đơn vị / điểm %); không cột đỡ (cột đỡ biến thanh thành xà nhảy cao
  → "phải vượt qua", trái G1 câu 1). Đô la thứ nhất đứng trên mặt thanh; đô la thứ hai đứng ở đầu thanh, tâm ngang thanh = "đặt áp vào để so".
- Tờ đô la (`Bill`, obj7.js): thẻ phẳng màu vật liệu tiền của lib3d + huy hiệu tròn sáng, không chữ.

## Dữ liệu
`../derive.py` → `../claims.json`: `display` của mỗi claim là đoạn NGUYÊN VẸN của cột "Hiển thị" (`numbers.md`, kiểm trong derive.py); thêm
`last_week_short` ("Oct 8, 2026", cùng ngày `last_week`), `yearly_lump_late` ("4 months later", từ display của `yearly_lump_months`) và
**`principal` ($320,000 = `params.principal` của `out/model.json` — numbers.md không có dòng claim riêng; ghi là vấn đề mở)**. `_geom` = số hình học
(bó, tháng trễ) có kiểm chéo số học.
Lớp bắt buộc (như c3kit.js Tập 6): ILLUSTRATIVE + nguồn "Freddie Mac weekly mortgage survey" + "US only · history, not a forecast" trên mọi khung
(kể cả S01 — beats.md nói nhãn góc bắt đầu từ S03.2 trong phim; ở clip C3 đứng riêng giữ lớp bắt buộc).

## Số đo (r1, 11/10)
| Đoạn | Dài (s) | Render (s máy) | verify | Cue ±0,2 s (sync_audit) | Lệch lời ASR (trung vị / p90) |
|---|---|---|---|---|---|
| s01-stack | 13,65 | 66 | OK | 4/4 | 0,003 / 0,29 |
| s06-stack | 27,81 | 128 | OK | 4/5 (`a1.same` −0,24: bó bay bắt đầu trước khi chạm) | −0,07 / 0,58 |
| s21-track | 26,69 | 174 | OK | 5/7 (`a0.pay` +0,20, `a2.add` +0,27: dốc 0,2 s của cột đầu) | 0,007 / 0,15 |
| s23-track | 14,05 | 99 | OK | 4/5 (`a1.extra` −0,21: cột gom cuối) | 0,014 / 0,10 |
| s25-bar | 30,05 | 131 | OK (vòng 1 F-2 BLOCK: vạch đo × tên Tessa → Tessa sang trái nhà) | 6/7 (`a3.measured` −0,30: đô la thứ hai trượt vào trước khi chạm) | −0,017 / 0,10 |
Clip duyệt `review-c3/c3-clip.mp4`: 118,33 s, −14,0 LUFS, −1,9 dBTP (`c3-clip.json`). Giọng: 1.493 ký tự ElevenLabs (trần 3.000).

## Vòng 2 (11/10) — sửa `s06-stack` sau cổng gốc tắt tiếng (nghĩa 0,5 + 0,5 → TRƯỢT)
Người đọc vòng 1 không thấy thanh 30 năm được **nâng** (lúc nâng còn ở chế độ thế giới, chưa có nhãn; ở đồ thị đã nâng xong) và đọc chồng thành
"tiền để dành / đầu tư phần chênh" (bó rơi từ không trung, nhãn chồng không nói đó là tiền ĐÃ TRẢ). Sửa bằng hình trước (D-009), nhãn cuối:
- **Trước khi nâng, ở đồ thị**: chuyển chế độ sớm (ngay sau "takes", 5,90 → 6,90 s; vẫn ≥ 5 s đầu ở thế giới); thanh 30 năm đứng ở mức bắt buộc,
  rõ ràng ngắn hơn, nhãn "required: $2,216 a month" (claim mới `pay30_now`); "$2,828 a month" (claim `pay15_month`, `of: pay15_now`, = cả cột
  Hiển thị) ở đầu trái **vạch mức 15 năm**.
- **Vạch mức 15 năm** (3D, `ink-muted` = TRACK.mark, đứng yên, trước mặt hai thanh, kéo qua cả hai) vẽ từ trái ở "finishing" (nốt tick; là
  cue hình `a0.finishing` thay cho cú nâng cũ).
- **Dâng**: thanh 30 năm dâng ở "forty-eight" trong 1,4 s (âm `rise`), qua vạch một lát warn; "required" tắt, "30-year paid in 15: $2,948 a month" hiện.
- **Lát tách khỏi thanh**: thứ tự trái → phải nhà · chồng · thanh 15 năm · thanh 30 năm (chồng giữa nhà và thanh); mỗi lát bay bắt đầu TRÙNG lát
  warn trên đỉnh thanh 30 năm (cùng bề ngang/sâu/dày), nhấc lên, vòng ra trước thanh 15 năm (z) rồi thành bó trên đỉnh chồng; vệt đường bay
  warn mờ, nét đứt nối đỉnh thanh với lát (chỉ ở đồ thị). Bay 0,8 s, ≤ 2 lát cùng lúc; lát đầu rời thanh đúng "same" (vòng 1 `a1.same` −0,24 s);
  mỗi lần chạm một nốt dữ liệu như cũ. Thanh 30 năm giữ nguyên $2,948 (khoản trả lặp lại mỗi tháng).
- **Nhãn chồng**: "the stack: $21,622 extra paid over 15 years" (định nghĩa `extra_vs15_total_now` = phần trả thêm qua 15 năm); không chữ khuyên,
  không "save/invest". "$2,828 a month" tắt ở "same" (đường bay đi qua chỗ nó).
- `derive.py`: thêm `pay30_now` vào `disp` và `pay15_month` (claims.json sửa tay khớp đúng đầu ra derive — chạy lại derive.py để xác nhận).

## Lệnh (từ gốc repo; cần `npm ci` trong `toolkit/factory/world/vendor` một lần)
```
python3 episodes/ep007/world/derive.py
python3 episodes/ep007/world/c3/voice_c3.py            # in số ký tự (trần C3 3.000); --go để sinh (take có rồi = 0 ký tự)
python3 toolkit/tests/comment_guard.py episodes/ep007/world
for s in s01-stack s06-stack s21-track s23-track s25-bar; do python3 toolkit/factory/world/build_seg.py episodes/ep007/world/c3/$s --res 540 --out episodes/ep007/world/c3/out/$s.mp4; done
python3 episodes/ep007/world/c3/review.py                # spans.json + dải review-c3/strips-r1/ + clip duyệt review-c3/c3-clip.mp4 (+ .json loudness)
for s in s01-stack s06-stack s21-track s23-track s25-bar; do python3 toolkit/factory/world/sync_audit.py episodes/ep007/world/c3/out/$s.mp4 episodes/ep007/world/c3/out/$s.sync.json --spine episodes/ep007/world/c3/$s/spine.json; done
```

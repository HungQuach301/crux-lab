# Đầu bài dựng C4 Tập 7 — lượt 1/2 (P3, 11/10): khung cả tập + đoạn a (S01–S03) và b (S04–S09). KHÔNG render

Nhánh `ep007` (main @76ef2b1 đã merge: K4.2 kind `term-pair-weekly-replay` + SH06, K4.2b A28/A31; LOCK dc4981b3). Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push** (phiên chính commit). Không in, không ghi khoá API ra đâu.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 r3 | S21–S24 | số dày 3/6 | "195 months", "$8,792" chỉ trên hình | checker ĐẠT 9:54 | đo lại C4 |
| C3 r2 | S06 | chồng = "tiền để dành", không thấy thanh dâng | nhãn trước khi dâng, vạch 15 năm, lát bay từ đỉnh thanh, "extra paid" | 2/2 | — |
| C3 r3 | S01, S21, S23, S25 | tiết kiệm 3/3, ô trễ sót, teal = "còn nợ", "guaranteed / has to beat" | bó từ cửa nhà, N1 `ink-muted`/`ink`/`warn`, gom 12 lớp, bóng đô la tách | cổng gốc 5/5 2/2, stated 0 | hàng chờ C4 (dưới) |

## Đọc
`toolkit/factory/README.md` (mục Thế giới 3D, F-12, splice) · **mẫu Tập 6 C4 (cả tập là thế giới):** `episodes/ep006/episode.yaml`, `episodes/ep006/c4/build_inputs.py`, `episodes/ep006/world/c4kit.{py,js}`, `episodes/ep006/world/c4/*/{spine.py,scene.js}`, `episodes/ep006/world/music/{bed,tension}.py`, `episodes/ep006/contract.json` · **Tập 7:** `story/script.md`, `story/beats.md` (bảng nhịp = hình phải làm; cột "on-screen text" = chữ trên hình), `numbers.md`, `contract.json` (khối `model` đã PASS S01 — giữ nguyên), `world/{c3kit.*,obj7.js,derive.py,claims.json,wlib.py}`, `world/c3/README.md` + `world/c3/{s01-stack,s06-stack}/` (đoạn C3 đã duyệt — **giữ ý hình đã duyệt**), `gates/C3.md` §3, `gates/C3-answer.md`, `review-g1/voice-scenes.json` (độ dài take thật, 33/33 cảnh), `out/timeline-len.json`.

## Làm (lượt 1)
1. **Khung cả tập** theo mẫu Tập 6: `episodes/ep007/episode.yaml` đủ (`scope: full`, `res: 720` — animatic C4; C5 đổi 1080, `fps: 30`, `script/claims/tokens/data` từ `c4/gen/`, acts theo các dòng `=== … ===` của script.md, `scenes` với `tail` = max(1,0; hold câu cuối) + ident 3 s sau S03, `audio: {lufs: -14, true_peak: -2.0, music: …, music_cmd: …, ident: {after: S03}, close_lift_db: 12}`, **2 mid-roll** (`lab`): MR1 trong hold 1,5 s sau S09.3, MR2 trong hold 1,5 s sau S24.3 — lặng ≥ 1 s cả bản trộn, ≥ 120 s từ đầu/cuối; `counterweights` (US only · history, not a forecast; ILLUSTRATIVE; not advice), `world:` 7 đoạn liên tiếp: **a S01–S03 · b S04–S09 · c S10–S15 · d S16–S20 · e S21–S24 · f S25–S28 · g S29–S33** (lượt này viết spine/scene cho a, b; c–g chỉ khai trong yaml + thư mục rỗng có `spine.py` khung tối thiểu nếu nhà máy đòi), `shorts:` nháp 3 cái (ứng viên: B01+B06 the stack; B21 N1; B25 the bar — móc ≤ 1 dòng ≤ 26 ký tự, không chữ số, SH06 đo trước render). `c4/build_inputs.py` (gen script/claims/tokens/data từ `out/model.json` + `world/claims.json`; claim chưa làm tròn + `display`), `world/c4kit.{py,js}` (dùng lại `c3kit`, `obj7.js`, `wlib.py`), `world/music/{bed,tension}.py` (mỗi hồi một cue, không lặp vòng; lặng 0,7–0,9 s trước ≤ 3 số neo `anchor: true`, nằm trong đuôi cảnh trước; nhạc về 0 quanh MR1, MR2).
2. **`contract.json`**: giữ nguyên `model`, `lock`, `format`; điền `characters` (tessa, leo: màu/side/shape theo mã thật, illustrative), `claims.{illustrative, core, decisive, conditions, assumptions}` (điều kiện "history, not a forecast", "US only", "before taxes" cho `bar_now`), `data` (sources, crosscheck theo `data/sources.json`), `sonification`, `shorts`, `artefacts`; bỏ khối `pending` khi đã điền.
3. **Đoạn a (S01–S03 + ident)** và **b (S04–S09)**: mọi cảnh là thế giới 3D (D-010, 8 quy tắc hình–âm: ≥ 5 s đầu ở thế giới, số/nhãn so sánh chỉ ở đồ thị, mỗi động tác máy có lý do + âm, mỗi lần vật đổi trạng thái một nốt dữ liệu). S01 = bản C3 `s01-stack`, S06 = bản C3 `s06-stack`, **cộng các sửa bắt buộc dưới**. Các cảnh khác theo beats.md (V4 adapted thẻ hai khoản; V6 ngoặc `cushion` có nhãn; W2 ×2 chồng lãi S08–S09, phần chênh nhấc lên thành the stack; V1 xem trước ở S02).
4. **Hàng chờ C4 bắt buộc trong lượt này (gates/C3.md §3, nhận xét lặp ở hai lượt đạo diễn; C3-answer câu 4):**
   - **Tessa** (mọi đoạn có Tessa): một cử động nhỏ (quay đầu/nghiêng người/giơ tay) đúng lúc vật chạm/dâng ở chế độ đồ thị — không đứng yên cả đoạn.
   - **S01:** giữ nhãn giá ở 5,94 s (C3 câu 3 = a, luật "≥ 5 s đầu ở thế giới"). Chồng **dừng sau bó đầu** — không mọc tiếp trong lời "$320,000" (đạo diễn r1 #3 + r3 #3 đọc thành "savings" / "the loan is $720"); khoản vay $320,000 bằng **vật riêng** gắn với nhà (không phải chồng); **không còn bó sót ở cửa nhà** (r3 #2 lúc 9,57 s) — mọi bó về một chồng.
   - **S06:** chồng chỉ bắt đầu dựng ở "Over those 15 years" (S06.3), không trước; nhãn "30-year paid in 15: $2,948 a month" hiện **đúng "forty"** (±0,2 s; `a0.forty` đang +1,29) — cho đỉnh thanh qua vạch sớm hơn hoặc hiện nhãn khi bắt đầu dâng; **lát trên vạch đọc được trên điện thoại** (dày hơn ~4 px ở 540p và/hoặc máy đẩy vào đỉnh thanh); chồng và thanh không đọc thành cùng thang (chồng thấp hơn đỉnh thanh, hoặc tách bằng khoảng/nền rõ, mỗi cái có nhãn riêng); `a1.same` (+0,53) về ±0,2 s.
5. Âm theo `episode.md` §5b (không tăng mật độ sfx; bỏ sfx "land" đè từ khoá số neo).

## Ràng buộc cứng
- **Không đổi chữ kịch bản, không sinh giọng**: 33/33 take đã có ở `voice-takes/` (cache theo băm) — build phải trúng cache, 0 ký tự EL. Lệch băm → dừng, báo.
- **Độ dài `lab` 9:00–11:00**, tối đa cứng 11:00; mọi đuôi/hold/lặng tính vào; ghi tổng timeline (s).
- Số trên hình chỉ qua claim (`display` nguyên vẹn của numbers.md); gen được bảo vệ: ILLUSTRATIVE trên mọi khung có Tessa/Leo; "US only · history, not a forecast" trên khung số lịch sử; không câu khuyên; không lợi suất đầu tư nào.
- **Không render**: không chạy `build.sh`, `build_seg.py` render, Playwright dài. Chỉ: `python3 toolkit/tests/comment_guard.py episodes/ep007/world`, kiểm khai/spec, mỗi `spine.py` + kiểm quy tắc, `numbers_said.py`, `build_inputs.py`, đo timeline. Phiên chính chạy build nền.
- Không sửa `checks/`, `toolkit/` (cần sửa nhà máy cho CHẶN/CHÍNH của tập → dừng và báo).

## Trả về (≤ 25 dòng)
Tệp đã viết; ranh giới đoạn; tổng timeline (s), MR1/MR2 (giây, khoảng lặng); số neo chọn; kết quả lint/spine/spec; từng mục hàng chờ ở mục 4 đã làm thế nào; rủi ro; **lệnh build chính xác** cho đoạn a, b (gồm bước trước/sau như Tập 6).

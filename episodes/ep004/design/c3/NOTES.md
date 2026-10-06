# Tập 4 · C3 style frame có chuyển động — N1 "inflation shadow", N2 "threshold ladder"

Dựng bằng nhà máy (Mốc B), đoạn trích S08 + S13 + S14 (78,7 s), 2026-10-06.

```
python3 episodes/ep004/data/fetch.py --verify        # 14/14 SHA khớp hồ sơ
python3 episodes/ep004/model/model.py                # out/model.json
python3 episodes/ep004/design/c3/build_inputs.py     # gen/script.json, gen/claims.json, gen/tokens.json, work/data.js
bash toolkit/build.sh episodes/ep004/episode.yaml    # spec → giọng → render → mix → qc
python3 toolkit/blind/strips.py episodes/ep004/work/factory/video.mp4 episodes/ep004/review-c3/spans.json episodes/ep004/review-c3
```

## File

| File | Việc |
|---|---|
| `n1.js` | N1 "inflation shadow" (B08): trần $500,000 liền `ink-muted` 10 px, đứng yên; đường ĐỨT cùng màu chạy theo CPI-U hằng tháng (DATA.cpi) từ tháng 5/1997 tới "≈ $1,046,000 (Aug 2026 dollars)"; chú thích "consumer prices (CPI-U), not house prices" (S08.4 phóng 48 → 64 px trong 2 s). Trục giá trị từ 0. |
| `n2.js` | N2 "threshold ladder" (B13 `mode: phoenix`, B14 `mode: ladder`): thước giá dọc cùng thang ($100,000–$400,000, vị trí). B13: mốc Phoenix, chấm Rosa & Frank $200,000 ngay trên (ILLUSTRATIVE), thước tách trung tính / `warn`. B14: 12 bậc thành phố + bậc quốc gia đứt, thanh tăng trưởng mảnh chỉ trái (`accent`, dài ∝ ×tăng, dài nhất ở dưới), vạch $300,000 (ILLUSTRATIVE), tiêu đề cuối. |
| `build_inputs.py` | Chuyển script.md → `gen/script.json`; numbers.md + model.json → `gen/claims.json` (display dựng từ giá trị; số làm tròn của mô hình mang "≈"; historical/illustrative); visual-library tokens → `gen/tokens.json` (+ vai tập: cap/gain/above/index); CPIAUCNS.csv + model.json → `work/data.js` (không commit). |
| `../../episode.yaml` | Thêm khối nhà máy (scope excerpt, 3 cảnh, 4 shot), `counterweights`, `custom_symbols`; `voice` đổi tên "Eric" → id Eric (như Tập 3), seed 1004. |

Mọi chữ số trên hình đi qua claim `{claimId}`; vị trí bậc/thanh lấy từ `out/model.json` (làm tròn như numbers.md). Shot còn lại dùng mẫu thư viện: S13.1 = `bignum` (`threshold_joint_phoenix`).

## Móc nạp mẫu riêng của tập (toolkit/, 7 dòng thêm / 3 dòng bỏ, 3 file)

- `toolkit/factory/build.py` (+5/−2): `custom_symbols: [{id, file}]` (file tương đối với tập) → `self.symbols = [{id, url}]`; mã các file này cộng vào `code_hash` (cache đoạn render đổi khi ký hiệu đổi); job thêm khoá `symbols`.
- `toolkit/factory/page.html` (+1): `for (const c of job.symbols) TEMPLATES[c.id] = (await import(c.url))[c.id.toLowerCase()] || default`.
- `toolkit/factory/spec.py` (+1/−1): id trong `custom_symbols` được coi là template hợp lệ (nếu không, spec BLOCK "unknown template"). Luật ≤ 2 → ASK giữ nguyên.

Không sửa engine, templates, render, qc, voice.

## Kết quả

- spec: 0 BLOCK/ASK (1 WARN: đoạn trích không có Short).
- Giọng ElevenLabs Eric `eleven_v3`, seed 1004: **1.157 ký tự** (S08 426, S13 274, S14 457), 3 cảnh, cache; các lần dựng sau 0 ký tự.
- qc (`out/factory/qc.md`): **12/12 ĐẠT** — sàn chữ 42,01 px, tương phản 7,5:1, 0 va chạm, 0 khung thiếu nhãn, đối trọng 1.398 khung, freeze ∩ lời 0 s, −14,0 LUFS / −1,5 dBTP (sát ngưỡng TP, đúng trần Tập 3).
- Kiểm mù: `review-c3/B08.png`, `B13.png`, `B14.png` (6 khung, tắt tiếng, giữ chữ/số; `strips.json` có thời điểm + SHA), clip 720p `B08-clip.mp4`, `B13-clip.mp4`, `B14-clip.mp4` (~0,5–1 MB, CÓ tiếng — tắt khi kiểm mù), ảnh xem trước `N1-preview.png`, `N2-preview.png`.

## Ý người xem phải đọc ra (beats.md, muted read)

- B08: "The cap stayed flat since 1997, while the same cap, kept up with consumer prices, would now be about $1,046,000."
- B13: "There is one purchase price where the gain lands exactly on the cap; the couple's price sits above it, so their line is over."
- B14: "Each city has its own 2000 purchase price above which the gain passes the cap; those prices run from about $114,700 in Miami to about $373,400 in Chicago, and all but Chicago sit under the $300,000 line."

## Lệch khỏi beats.md / script.md và vì sao

1. **Giữ hình giữa cảnh** (S08.3 1,2 s, S14.2 1,2 s) không có: nhà máy chỉ có `tail` cuối cảnh (S08 1,2 s, S13 1,2 s, S14 1,5 s = chỗ MR2). Lời đọc liền một lượt mỗi cảnh.
2. **B13 "slider đưa đầu đường lãi lên trần"** không dựng: thư viện không có slider, thêm sẽ là ký hiệu thứ 3. S13.1 dùng `bignum` "≈ $179,200" + "Phoenix · 2000 price where the gain reaches the cap"; thước N2 vào từ S13.2.
3. **S14.5 "biểu đồ Hồi 1 thu nhỏ vào đầu thang"** không dựng (biểu đồ Hồi 1 không nằm trong đoạn trích); chỉ hiện tiêu đề "2000 price where the gain / reaches the $500,000 cap".
4. **Đối trọng** viết đúng nguyên văn claim-risk "A home that rose like the metro average" (spec.py so khớp chữ), không phải dạng "its metro area's average" của S14.1 lời nói.
5. **Tên thành phố** một cột bên phải, có đường dẫn: cụm 11 bậc nằm trong $151,500–$259,000 (≈ 220 px) nên nhãn San Francisco / San Jose / US average đứng cao hơn vạch $300,000 dù bậc của chúng ở dưới; vạch $300,000 chỉ cắt thanh + thước, không qua cột tên. Chỉ Miami, Chicago mang giá (beats: "on screen only"); Phoenix mang giá ở B13.
6. **Trục phải N1** ghi "today", không ghi "Aug 2026" riêng (tháng chỉ nằm trong nhãn claim `excl_joint_1997_in_now`); chú thích dùng dạng script "consumer prices (CPI-U), not house prices".
7. **Màu**: thanh tăng trưởng `accent` (= chỉ số thị trường, bảng E2); bậc thành phố `ink`; bậc quốc gia đứt `ink-muted`; vạch $300,000 `ink` 4 px; thước B13 dưới mốc `ink-muted` 75 % (trung tính), trên mốc `warn`.
8. **Giọng**: normalize đọc "a 2000 price" (S14.5) thành "a two thousand price" — nghe lại ở C4.
9. Không có Short (đoạn trích; spec WARN).

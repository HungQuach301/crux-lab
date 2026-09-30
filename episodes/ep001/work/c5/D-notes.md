# C5 · Luồng D (hồ sơ) — ghi chú cho P, A, P2

29/09/2026. Mọi file của D sinh lại được bằng mã; chạy lại theo thứ tự:
```
python3 episodes/ep001/preprod/script_from_v32.py   # out/script.json, out/script-draft.json
python3 episodes/ep001/build.py                     # out/claims.json (shownIn đọc animatic/check-report.json)
python3 episodes/ep001/preprod/dossier_c5.py [--method-card A B] [--end-screen A B]
NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep001/preprod/thumbs_c5.js
THREE_DIR=<node_modules/three/build> python3 episodes/ep001/preprod/rights_c5.py
python3 episodes/ep001/contract_build.py
```

## P (hình) còn nợ / cần biết
1. **S02 (CHẶN) cần giả định trên màn hình trong hồi `method`.** `contract.json claims.assumptions` có 6 mẫu: `offer-average` ("matches the national average"), `fees-in-cash` ("paid in cash"), `payback-3y` ("within 3 years"), `oct2023-rate` ("October 2023 rate"), `median-bill` ("median 2025 bills"), `new-loan-30y` ("30-year term|clock|loan"). Ngoài hồi method đã có đủ (S06, S07/S11/S18, S18, S18, S02/S18, S10). **Trong hồi method chưa có gì**: hồi method hiện là **S19** (không có thẻ phương pháp sau S20). Hai cách: (a) thêm vào S19 một chú thích cố định, ví dụ "Assumes: offer matches the national average rate · October 2023 rate · median 2025 bills · fees paid in cash · 30-year term · paid back within 3 years" (2 dòng ≥ note 48 px); hoặc (b) thêm thẻ phương pháp + end screen sau S20 như script v3.2 (không đổi thời điểm câu), rồi báo D cửa sổ để chạy `dossier_c5.py --method-card A B --end-screen B C` (hồi đổi thành act3 = S14–S20, method = thẻ, outro = end screen) và thêm chương vào mô tả.
2. Sau render cuối: chạy `animatic/src/check.py` để `check-report.json` có `claimsUsed` mới, rồi `build.py` (shownIn của claims theo màn hình).
3. `coverage`: cột S18 mang `case` = `median`/`small`/`large` (đã thấy trong diff `s18.js`, khớp hợp đồng).
4. Không nhúng chapter vào MP4, hoặc nhúng đúng các mốc của `out/package/description.md` (F10 so hai bên).
5. `out/visual-assets.json` khai: chỉ phông **Inter** (họ "Inter"). Nếu trang nạp thêm file ảnh/texture/phông khác thì báo D (F12 trượt nếu nạp mà không khai).

## A (tiếng) còn nợ / cần biết
1. `out/rights.json` ghi mã sinh của music/sfx/whoosh/room/sonify = `work/audio/src/mix.py` (tính từ gốc tập). **Phải commit file này** (F12 kiểm đường dẫn tồn tại). Nếu đổi đường dẫn, báo D hoặc sửa `AUDIO_GEN` trong `preprod/rights_c5.py`.
2. Điểm quảng cáo `out/adbreaks.json`: 241,54 s và 372,2 s (ranh giới act2, act3; khe lời 240,43–241,89 và 370,97–372,55). S14 cần ≥ 1 s master ≤ −40 dBFS quanh mỗi điểm.
3. `out/transitions.json` để `audio: null` (J/L cut là của mix; A sửa trường này nếu có).
4. Sau khi có stem: chạy lại `dossier_c5.py` để `tension-map` đo musicLevel/audioDensity từ stem (hiện là "planned").
5. `contract.json sonification.bandsHz` = [[60,270],[4500,7000]] = `SON_BANDS` của `mix.py`.

## P2
- **F12**: giọng Eric chờ trích nguyên văn ElevenLabs: dán vào `out/rights.json` (`terms.quote`, `terms.url`, `commercial: true`) — hoặc sửa `preprod/rights_c5.py` rồi chạy lại. Hiện `"PENDING-OWNER-PASTE"` (19 ký tự < 20) nên F12 trượt thật.
- **S09 (CHẶN), phần lời**: 26 câu có số $ mà câu đó và câu trước (cùng cảnh) không có chữ cơ sở ("nominal", "dollars of the day", "before inflation"…). Lời chỉ nói "dollars of the day" một lần (S04). Lời đã khoá (C4) → cần chủ dự án quyết (khiếu nại luật hay đổi lời); D không sửa `text` vì phụ đề phải đúng lời (F09) và ASR (A14).
- `RIGHTS.md` dòng F-INTER đã có trích nguyên văn (nhánh `ep001-v2`), P2 đồng bộ sang main.

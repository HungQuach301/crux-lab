# C3 · H1 — "Vật thể thật" (3D real objects, render CPU)

**Ý tưởng.** Mỗi con số là một vật thể có thật trong nhà Nora: biển lãi trong sân, tấm séc trong hộp thư, xấp giấy phí trên bàn bếp, cọc tiền $221 mỗi tháng, lịch để bàn, hai căn nhà. Kích thước vật thể **là** dữ liệu (chiều cao chồng giấy ∝ đô la trong cùng khung; thể tích nhà ∝ khoản vay; kim trên thước lãi đúng giá trị). Không ẩn dụ trừu tượng (bể nước, khối đá). Chữ quan trọng in phẳng trên mặt vật (texture 2D đối diện máy quay) hoặc vẽ trong không gian màn hình, neo theo vật → luôn sắc, không méo phối cảnh. Ý đồ từng khung: `intent.md` (commit trước khi render).

| File | Nhịp | Dài | Poster | Dải 6 khung |
|---|---|---|---|---|
| `F1.mp4` | Cold open: cửa sổ lỡ — biển lãi 7.62% → 5.98% (Feb 26, 2026) → 7.03% (Sep 24, 2026); séc "$459 / month" bay ra khỏi hộp thư rồi xám và rơi về | 9.0 s | `F1-poster.png` | `F1-strip.png` |
| `F2.mp4` | Hoà vốn 24 → 30: xấp giấy "Loan costs $5,124" vs cột cọc $221; tháng 24 ngang nhau → tờ đỏ "+$1,133 more owed" đè lên xấp → thêm 6 cọc tới tháng 30 | 10.0 s | `F2-poster.png` | `F2-strip.png` |
| `F3.mp4` | Walt/Anjali: hai nhà (thể tích 5.7×), hai xấp phí gần bằng, hai cột tiết kiệm $68 / $387 mọc 36 tháng; biển sân "1.12 points" / "about 1/3" | 9.5 s | `F3-poster.png` | `F3-strip.png` |

Clip 1280×720, 30 fps, H.264 High yuv420p (CRF 18, BT.709), không tiếng; 1.2–1.7 MB mỗi clip. Dải 6 khung: 1920×220, số 1–6 và thời điểm dưới mỗi ô.

## Số trên màn hình → claim (`numbers.md` / `out/claims.json`)
- F1: `low2026` 5.98%, `low2026_date` Feb 26 2026, `low2026_since` Sept 2022, `oct2023`, `r_old` 7.62%, `sav_low2026_median` $459, `r_today` 7.03% + `anchor_date` Sep 24 2026, `seven`, `first7_since` Jan 2025.
- F2: `cost_median` $5,124, `sav_median` $221, `be_simple_median` 24, `gap24` $1,133, `be_bal_median` 30.
- F3: `loan_small` $115,000, `cost_small` $3,667, `sav_small` $68, `cut36_small` 1.12, `loan_large` $655,000, `cost_large` $5,514, `sav_large` $387, `cut36_large_words` "about a third of a point" (biển ghi "about 1/3 of a point"), `hold36`/`y3`.
- Nhãn ILLUSTRATIVE luôn hiện (góc trên phải + trên séc); "nominal $" góc trên phải; dòng nguồn dưới trái.

## Chỗ hình là nội suy / mô hình (không phải dữ liệu)
- F1: kim trên biển lãi đi **trơn** giữa ba mốc có claim (Oct 2023 → Feb 26 2026 → Sep 24 2026); lúc kim đang chạy ô số hiện "···" để không có số trung gian bịa. Đường thật giữa các mốc có răng cưa.
- F2: độ dày phần đỏ theo từng tháng lấy từ `model/refi.py` (`balance_after`, đúng tham số nhân vật median: $375,000, 7.62%, 35 kỳ đã trả, khoản mới 7.03%/30 năm) — khớp $1,133 ở tháng 24 và hoà vốn 30. Chỉ in số $1,133.
- F3: cột tiết kiệm là cộng đơn giản (chưa trừ hiệu ứng dư nợ); không in số thiếu/dư. Thể tích nhà ∝ khoản vay (cạnh × ∛5.70 = 1.79) — ghi "house volume ∝ loan size" trên hình.

## Màu và chữ
- Màu UI: token kênh (`genre-spec/channel/visual-tokens.json`): bg `#0E1116`, ink `#F2F4F7`, muted `#9AA4B2`, warn `#F2B441` (ILLUSTRATIVE, Walt ▲), positive `#3FBF7F` (tiết kiệm, cửa sổ lãi thấp, hoà vốn), negative `#E5484D` (vạch 7%, phần nợ ẩn, Anjali ■). Theo ghi chú `design/tokens.json`: ở F3 (có dấu nhân vật) băng phí dùng xám đậm `#2E3440`, không dùng đỏ.
- Màu vật liệu (không phải token): giấy `#EFEBE2`, gỗ bàn, tường nhà, cỏ, trời đêm `#0A0F1C`.
- Chữ: Inter 400/600/700 (`toolkit/render/fonts`), số tabular. Chữ màn hình ≥ 20 px ở 720p cho nội dung (dòng nguồn 15–16 px); số chính 30–46 px; số trên biển/séc/lịch in ở texture 1024 px.

## Kỹ thuật & thời gian render (CPU)
- three.js 0.186.1 (MIT) trong Chromium headless 1194 (Playwright), WebGL qua **ANGLE → SwiftShader** (Vulkan phần mềm, không GPU). Bóng PCF 1024², tone map ACES, MSAA của SwiftShader. Khung 2D (drawImage WebGL + chữ phẳng) → RGBA → PyAV (libx264). Không ffmpeg CLI.
- Máy: 4 vCPU Intel Xeon 2.80 GHz. Một trang Chromium, tuần tự (số đo thật ở `render-log-F*.json`):

| Khung | Frames | Giây máy | **Giây máy / giây phim** |
|---|---|---|---|
| F1 (đêm, sao, 3 đèn điểm) | 270 | 101 | **11.3** |
| F2 (bàn, 30 cọc + đèn spot) | 300 | 129 | **12.9** |
| F3 (2 nhà, 72 cọc, cây) | 285 | 90 | **9.4** |

→ **~9–13 s máy cho 1 s phim, dưới ngưỡng 60 s.** Ước cho toàn tập ~9.5 phút (570 s): ~1.8–2.1 giờ với một tiến trình; chạy 3–4 trang Chromium song song theo đoạn (như `toolkit/render/render.js` làm với WORKERS) dự kiến còn ~40–60 phút (chưa đo; SwiftShader tự dùng nhiều luồng nên tăng tốc không tuyến tính). Ở 1920×1080 chi phí điểm ảnh ×2.25 → ước ~20–30 s/s phim một tiến trình. Cách giảm nếu cần: tắt MSAA và render 1.25× rồi thu nhỏ chỉ cho cảnh nhiều cạnh; nướng bóng tĩnh (cây, nhà) vào texture; giảm shadow map 512²; chia đoạn song song.

Chạy lại:
```
npm i three@0.186.1            # trong một thư mục tạm
THREE_DIR=<tạm>/node_modules/three/build NODE_PATH=/opt/node22/lib/node_modules \
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node src/render.js F1   # F2, F3; --still 4.6 ; --strip-only
```
Nguồn: `src/common.js` (renderer, chữ phẳng, nhà, giấy), `src/f1.js`–`f3.js` (mỗi cảnh là hàm tất định theo t), `src/render.js`, `src/encode.py`.

## Giới hạn
- Hình học đơn giản (hộp, lăng trụ, nón): đọc là "đồ vật thật" nhưng chưa đạt mức ảnh thực (không có mô hình chi tiết, không GI, không đổ bóng mềm thật). Nâng cấp cần mô hình glTF có giấy phép rõ hoặc tự dựng — tốn thời gian dựng hơn thời gian render.
- Chữ in trên vật (séc, biển sân, lịch) nhỏ ở vài khung; mọi số quan trọng đã có bản chữ phẳng trên màn hình hoặc in đủ lớn, nhưng ở thumbnail 320 px của dải 6 khung chữ nhỏ khó đọc.
- F1: chỉ ba mốc lãi có claim; không có đường lãi tuần thật (dữ liệu FRED không commit, E1-A2). Nếu chọn H1, có thể thay bằng một dải giấy in đường lãi tuần thật chạy qua biển (dữ liệu tải bằng `fetch.py`).
- F2: phần đỏ sau tháng 24 dày thêm theo mô hình nhưng không in số (không có claim cho tháng 25–30).
- F3: cột chưa tính hiệu ứng dư nợ, nên điểm cột Anjali vượt phí (tháng ~15) sớm hơn `be_bal_large` 18; không in số tháng này.
- Chưa có lời/âm; nhịp khung chưa khớp lời table read (khớp ở C4).
- three.js không vendor trong repo (cài bằng npm, xem trên); SwiftShader cảnh báo "GPU stall due to ReadPixels" (vô hại).

# Tập 1 · C3 final — Hệ hình (hướng D: H1 + H3, một bộ token)

DESIGN LEAD C3 final, 29/09/2026. Quyết định chủ dự án (`gates/C3.md`, sổ gu "G-009 · C3", G-014): hướng **D** — H1 "vật thể thật" (three.js, CPU) + H3 "hình học của tiền" (2D), **chọn theo từng nhịp**; H1 và H3 **chung một hệ màu và phông**; chữ và số **đọc được ở 25%**; ký hợp đồng hình ảnh **qua clip** (`review-c3/contract.mp4`).
Máy đọc: `tokens.json` (cùng thư mục). Mã dùng chung: `src/engine.js` (mọi khung H1 và H3 đi qua cùng hàm chữ, cùng token, cùng `CL()`).

## 1. Màu (một bảng cho cả H1 và H3)

Token kênh (`genre-spec/channel/visual-tokens.json`), bí danh tập (`design/tokens.json`). Không thêm màu UI mới.

| Vai | Token | Giá trị | Dùng |
|---|---|---|---|
| Nền | `bg` | `#0E1116` | nền 2D; nền phòng/bầu trời đêm 3D gần giá trị này |
| Chữ | `ink` / `ink-muted` | `#F2F4F7` / `#9AA4B2` | chữ chính / phụ, nguồn, trục |
| Lãi thị trường | `accent` | `#4C8DFF` | đường lãi tuần; **cửa sổ** = `accent` 18% chỉ trên các tuần có lãi ≤ lãi Nora − 1 điểm |
| Nora | `positive` + ● | `#3FBF7F` | chấm tròn, cột Nora ở thước ba mốc |
| Walt | `warn` + ▲ | `#F2B441` | tam giác, cột Walt |
| Anjali | `negative` + ■ | `#E5484D` | vuông, cột Anjali |
| Còn nợ thêm (khoản mới so với khoản cũ) | hoa văn sọc chéo `negative` trên giấy | — | tấm "owed" (H1) / sọc chéo (H3). **Hoa văn** là thứ tách nó khỏi ô vuông đặc của Anjali (quy tắc `design/tokens.json`: không tô bill/saved bằng màu nhân vật khi marker đang trên màn hình, trừ khi có hoa văn) |
| Đã lỡ / đã đóng | sọc chéo `ink-muted` | — | cửa sổ đã đóng (SF1) |
| Huy hiệu | `warn` nền, chữ `bg` | — | ILLUSTRATIVE |

**Vật liệu 3D (không phải màu UI, không dùng cho chữ hay đồ thị):** giấy `#EFEBE2`, tiền `#DCE9DF` + băng `#C9B27A`, gỗ `#5E412D`, tường `#1A1E26`, nhà `#C9BBA4`/mái `#3B3F48`. Tiền là giấy xanh chung chung có băng, **không** mô phỏng tiền giấy Mỹ.

## 2. Chữ (Inter 400/600/700, số tabular) — luật G-014

Inter cao chữ hoa = 0,727 em. Để đọc được ở 25% (1920×1080 → 480×270), **chữ nhỏ nhất 48 px** (chữ hoa 34,9 px ở 1080p = 8,7 px ở 25%), **số chính ≥ 96 px** (chữ hoa 70 px).

| Bậc | px @1080p | Đậm | Chữ hoa @1080 / @25% | Dùng |
|---|---|---|---|---|
| hero | 150 | 700 | 109 / 27 px | một số của nhịp (ít dùng) |
| number | 96 | 700 | 70 / 17 px | số chính: 5.98%, $459, 7.03%, $1,133, 1.12 points, "Never" |
| head | 72 | 700 | 52 / 13 px | tiêu đề khung |
| caption | 64 | 600 | 47 / 12 px | câu mang nghĩa khi tắt tiếng; câu hứa |
| label | 54 | 600 | 39 / 10 px | nhãn cạnh vật/điểm |
| note | 48 | 400 | 35 / 8,7 px | **nhỏ nhất**: nguồn, đơn vị, chú thích |
| badge | 48 | 700 | 35 / 8,7 px | ILLUSTRATIVE |

- Hàm `text()` chỉ nhận 6 bậc trên → không thể vẽ chữ < 48 px. Mỗi chuỗi được ghi log kèm hộp bao; chuỗi nào ra khỏi vùng an toàn `[40, 1880] × [36, 1062]` bị đánh dấu (render log, `src/check.py`). Lề thiết kế thực tế 96 px.
- Chữ đặt trên nền 3D có bóng đổ hoặc tấm nền `bg` 80–92% (`plate`), không đặt chữ trần lên tường sáng.
- Chữ in trên vật (lá thư, xấp phí, hồ sơ vay) là phụ; con số nào cần đọc thì có bản chữ phẳng trên màn hình.
- Mỗi khung ≤ 1 dòng nguồn, ngắn (≤ ~62 ký tự ở 48 px). Dòng nguồn dùng lời thường: "Freddie Mac weekly rate survey, via FRED", "median 2025 refinance bill (HMDA)", "Dollars of the day". **Không** còn "nominal $", "∝", "Crux model (model/refi.py)".
- Đơn vị "point": luôn giải nghĩa trên khung có số điểm: "point = one percentage point of the rate" (hoặc "1 percentage point below Nora's rate").

## 3. Chuyển động — mỗi loại một nghĩa (dùng chung H1 và H3)

| Chuyển động | Nghĩa | H3 | H1 |
|---|---|---|---|
| **vẽ** (đường kéo trái → phải) | thời gian trôi | đường lãi tuần; đường "savings minus what she still owes" | — |
| **chồng** (một đơn vị rơi xuống mỗi tháng) | tiền dồn lại; 1 đơn vị = 1 tháng | dải tháng | cọc tiền $221 / $68 / $387 |
| **mọc** (khối mọc lên / thêm lên đỉnh) | một khoản xuất hiện | cột "rate cut needed" | tấm "owed" mọc trên chồng "new loan"; nhà mô hình |
| **nhấc lên** (vật rời chồng, sáng, lơ lửng) | một khoản từng được đề nghị | — | tấm $459 nhấc khỏi khoản trả hằng tháng |
| **rơi về** (xám đi, rơi lại chỗ cũ) | không nhận / đã mất | — | tấm $459 rơi về |
| **chuyển** (vật bay từ chồng này sang chồng kia) | khoản đó phải tính vào chỗ mới | — | tấm $1,133 bay từ chồng "new loan" lên xấp phí |
| **trượt** (dấu trượt dọc thước rồi dừng) | đọc một giá trị trên thang | vạch "1-point rule of thumb" trượt qua ba cột | — |
| **gạch** (vạch đỏ ngang) | câu trả lời đó sai | "$5,124 ÷ $221 = 24 months", "24" | "$459 a month less" |
| **viền** (nhà chỉ có đường viền, không số) | khoản vay của chính người xem | nhà nét đứt "your loan?" | nhà khung dây "your loan?" |
| **cắt** (cắt thẳng H3 ↔ H1) | đổi thang: thị trường ↔ một hộ | SF1 | SF1 |
| máy quay | chỉ đẩy vào chậm (≤ 20 px/s) | — | không rung, không quay vòng, không hạt |

Giữ yên ≥ 1 s ở cuối mỗi khung; chữ hiện ≥ 1,5 s trước khi đổi.

## 4. Luật vật thể 3D (H1)

1. **Vật thật mang số**: xấp giấy = phí, cọc tiền = tiết kiệm mỗi tháng, chồng giấy "balance paid off" = gốc đã trả, tấm sọc = còn nợ thêm, nhà = khoản vay, lá thư = đề nghị vay lại. Không ẩn dụ trừu tượng (bể nước, khối đá).
2. **Kích thước = dữ liệu, một thang đô la mỗi khung**: mọi chồng tiền/giấy trong một khung dùng cùng hệ số đơn vị/đô la (`K` trong mã). Nhà: **thể tích** tỉ lệ khoản vay (cạnh × ∛(khoản/115,000)); ghi bằng lời "House size is to scale with the loan" (bỏ ký hiệu ∝).
3. Chiều cao theo từng tháng lấy từ `model/refi.py` (qua `src/build_data.py`, có assert so với claim); **chỉ in số có claim**. Thước tháng: 36 vạch, chỉ đánh số tháng có claim (24, 30; "3 years").
4. Ánh sáng: một đèn chính ấm + trời/phòng xanh lạnh, bóng PCF 1024². Không GI, không ảnh chụp, không mô hình bên thứ ba.
5. Vật nào mang con số quan trọng phải có nhãn phẳng cạnh nó (bậc label trở lên); chữ in trên vật chỉ là phụ.

## 5. ILLUSTRATIVE, số và nguồn

- Huy hiệu **ILLUSTRATIVE** cố định góc trên phải (48 px) mỗi khi có số của nhân vật (Nora, Walt, Anjali) hoặc mốc giả định (3 năm, 0.25). Dòng nguồn nói bằng lời: "Nora is an illustrative borrower" / "Walt, Anjali: illustrative" — để người xem không nghi số thị trường (C3-blind: ILLUSTRATIVE làm nghi số ≥ 6).
- Mọi số trên màn hình đi qua `CL(claimId)` → đúng chuỗi `display` của `out/claims.json`. Không in số nội suy (kim/đường đi giữa các mốc không có số; thước tháng chỉ có tháng có claim). `src/check.py` kiểm lại từ log render: mọi token số của mọi chuỗi phải có trong `display` của claim.
- Tiền: "Dollars of the day" (không điều chỉnh lạm phát), thay "nominal $".
- Dữ liệu FRED: chỉ đọc cục bộ khi render (`src/data.js`, `.gitignore`), không commit.

## 6. Khi nào H1, khi nào H3 (luật chọn)

- **H1** khi phép tính là "tiền chồng lên, so chiều cao hai chồng cạnh nhau, một khoản chuyển từ chỗ này sang chỗ kia": người xem kiểm được bằng mắt vì mọi vật cùng một thang (hoà vốn 24 → 30, Walt/Anjali, $459 nhấc lên rồi rơi).
- **H3** khi ý là một đường theo thời gian (lãi tuần), một ngưỡng trên thang (1-point line, rate cut needed), một hàm qua nhiều giá trị (đường "never"), hoặc một phân phối.
- **Kết hợp** = cắt thẳng giữa hai thế giới (luật "cắt"), cùng token, cùng chữ; không lồng biểu đồ 2D vào không gian 3D (trừ thước tháng phẳng dưới khung).

## 7. Bảng chọn H1/H3 cho từng cảnh (script-v3.1)

| Cảnh | Chọn | Lý do (1 câu) |
|---|---|---|
| S01 Tuần lãi chạm đáy | **Kết hợp** (H3 → H1 → H3) — SF1 | Đường lãi tuần và cửa sổ là dữ liệu thời gian (H3); $459 là một khoản rời khỏi khoản trả hằng tháng trên bàn bếp (H1). |
| S02 Lá thư và câu hứa | **H1** — SF2 | Lá thư, dòng "Loan costs $5,124", ba nhà mô hình và nhà viền "your loan?" là vật thật tự kể. |
| S03 Gần đỉnh | **Kết hợp** | Đường lãi 2023 tới 7.79% là H3; "ba trong mười" là một con phố mười nhà H1, ba nhà sáng đèn. |
| S04 Nora | **H1** | Nhà, thùng chuyển nhà, hồ sơ vay điền dần: giới thiệu người, không có phép tính. |
| S05 Cửa sổ và vạch một điểm | **H3** | Đường lãi tuần, vạch 1 điểm, 29 tuần, khe 1.64: thuần thang đo thời gian (tô cửa sổ đúng tuần dữ liệu như SF1). |
| S06 Đề nghị | **Kết hợp** | Lá thư + chồng khoản trả hằng tháng tách tấm $221 (H1, cùng ngữ pháp $459); khe 7.62→7.03 là thước phẳng H3. |
| S07 Hoá đơn | **Kết hợp** | Xấp $5,124 nhấc khỏi lá thư đặt cạnh tấm $221 cùng thang (H1); đám mây điểm 2025 và "median" là H3. |
| S08 Hai câu trả lời | **H3** | Thước rate cut với vạch 1 điểm và phép chia 5,124 ÷ 221 là hai thang đo đặt cạnh nhau. |
| S09 Hoà vốn nghĩa là gì | **H1** — SF3 (nửa đầu) | Cọc $221 chồng lên tới ngang xấp phí ở tháng 24: phép chia hiện thành vật. |
| S10 Đồng hồ chạy lại | **H1** — SF3 | Hai chồng "balance paid off" (cũ/mới) cho thấy vì sao còn nợ thêm $1,133; tấm sọc bay lên xấp phí; hoà vốn 30. |
| S11 Một phần tư điểm | **H3** — SF4 | "Never" là hình dạng của một hàm qua 325 tháng; vật thể không cho thấy được. |
| S12 Một điểm | **H3** | Cùng đồ thị S11, đường cắt vạch phí ở tháng 18. |
| S13 Nửa điểm | **H3** | Thước rate cut có dấu 0.5 và chấm thật 0.59: đọc giá trị trên thang. |
| S14 Walt | **H1** | Nhà nhỏ, cùng lá thư, xấp $3,667 đặt cạnh xấp của Nora: "phí gần bằng" thấy bằng mắt. |
| S15 Phí gần như không nhỏ đi | **H1** | Khối khoản vay và xấp phí cùng thang, cột $68 lên chậm tới 75: so chiều cao vật. |
| S16 Walt bán sau 3 năm | **Kết hợp** — SF5 | Thiếu $1,777 là khoảng hở giữa cột tiền và xấp phí + tấm sọc (H1); 1.12 trên thước (H3). |
| S17 Anjali | **H1** — SF5 | Nhà lớn, xấp phí gần bằng, cột $387 vượt ở tháng 18, dư $5,250 sau 3 năm. |
| S18 Thước ba mốc | **Kết hợp** — SF6 | Lá thư quay lại (H1) rồi thước ba mốc H3 để người xem tự đặt khoản vay (G-013). |
| S19 Điều này không nói | **H3** | Dải phí $3,443–$8,270 và chấm $5,124 là một phân phối. |
| S20 Câu hỏi ở lại | **H1** | Nhà của Nora, cọc dư mọc ở mốc 3 năm và 7 năm dọc lối đi (thước tháng phẳng). |

**Tổng: H1 8 cảnh · H3 6 cảnh · kết hợp 6 cảnh.**

## 8. Lỗi người đọc mù (C3-blind) → cách sửa trong hệ này

| Chỗ vấp | Sửa |
|---|---|
| Chữ bị cắt mép (H2 F1/F3) | vùng an toàn + log hộp bao mọi chuỗi; 0 chuỗi ra ngoài (README) |
| "∝" | "House size is to scale with the loan" |
| "Crux model (model/refi.py)" | bỏ; nguồn bằng lời thường |
| "nominal $" | "Dollars of the day" |
| "points" hai nghĩa | "point = one percentage point of the rate" trên khung có số điểm |
| Vì sao tháng 24 còn nợ thêm $1,133 | SF3: hai chồng "balance paid off" (old loan / new loan) cùng thang; phần chênh (sọc) = "$1,133 still owed on the new loan vs the old one" rồi bay lên xấp phí |
| Vùng "cửa sổ" không khớp dữ liệu (H3 F1) | SF1: chỉ tô các tuần có lãi ≤ 7.62% − 1 điểm (14/8/2025 → 23/7/2026, 29 tuần của 2026 khớp claim `weeks_below_r_old_minus_1`); mép phải cửa sổ đánh dấu tuần 23/7/2026 |
| Thiếu lãi cũ/mới (F3) | SF5: "Same offer for both: 7.62% → 7.03%" |
| "1.12" không đơn vị | "1.12 points" + định nghĩa point |
| Séc rơi về hộp thư khó hiểu (H1 F1) | SF1: tấm $459 nhấc khỏi chính chồng "khoản trả hằng tháng", có nhãn, bị gạch, "She didn't take it." |

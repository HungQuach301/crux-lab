# C3 Tập 2 · H1 — "Vật thể thật" (3D, three.js trên CPU)

**Ý tưởng.** Cả lập luận là đồ vật trên **một mặt bàn**. Lịch sử lãi T-bill 1954→8/2026 là một **dãy núi** thật (TB3MS từng tháng) nằm dọc bàn; hai **khay** nằm ngay dưới hai nửa của nó. Một **khung kính 10 năm** úp lên núi là một lần chạy lại; trong khung có **thanh ray thép** đặt cao hơn sống núi ở mép trái đúng 1,5 điểm — vì lãi của Leah = 7,5% + (T-bill lúc đó − T-bill lúc bắt đầu), nên **"lãi vượt 9%" chính là "sống núi nhô lên trên thanh ray"**: núi tự là đường ray, hạt kim cương của Leah cưỡi lên nó. Kết quả mỗi lần chạy rơi xuống khay thành một ô (đỏ cao = đắt hơn tổng cộng, xám dẹt = không). Tiền lãi là chồng xu bạc, phần đắt hơn là khối xu đỏ; phần đệm là hũ nước xanh. Ý đồ từng nhịp viết trước khi render: `intent.md`.

| File | Nhịp | Dài | Chuyển động mang ý (tắt tiếng, che chữ) |
|---|---|---|---|
| `K1.mp4` | KEY-1 · S01.2–3 | 8 s | Thanh ray thẳng đứng yên; hạt bắt đầu **dưới** ray, đi lên xuống (lần chạy thật bắt đầu 1/2002); phía trước hạt ba nhánh mờ rung rinh = tương lai không biết; khe hạt–ray sáng xanh, ray hổ phách khi hạt vượt lên; hai thẻ (đường thẳng / đường gợn) và mốc kim cương Leah giữa chúng, đung đưa |
| `K2.mp4` | KEY-2 · S03.5–8 | 10 s | Kẹp xanh bập vào giữa ray và hạt cạnh một thước khắc; giãn (bigger) → co (smaller) → dẹt (zero) → lật thành khung xám, ray hổ phách (negative) |
| `K5.mp4` | KEY-5 · S04.1–2 / S11.4–6 | 10 s | Khung đáp xuống mép trái núi; sợi dây sáng chạy theo sống núi, hạt cưỡi một lần; ô trắng rơi thẳng xuống khay; khung bước sang phải từng nấc, nhanh dần, để lại bóng viền 24/48/72 tháng trước (chồng nhau); hai khay đầy dần theo đúng cột năm |
| `K3.mp4` | KEY-3 · S05.2–4 | 10 s | Khung quét hết 753 tháng: thanh ray dài dưới chân núi sáng hổ phách ở 574 đoạn; cùng lúc ô rơi: 107 đỏ cao, còn lại xám; khay trái đỏ hơn rõ; ô 4/1977 cao gấp đôi, vòng tối, nhấp một lần |
| `K4.mp4` | KEY-4 · S06.1–5 | 10 s | Ba lần chạy thật cùng thang: 1956-05 (một cú vượt ngắn → hũ chỉ lõm), 1976-06 (leo sớm → hũ đầy chút rồi cạn khô, ray hổ phách tiếp), 1989-03 (lãi trôi xuống → hũ đầy mãi); dòng xanh rót vào hũ khi hạt dưới ray; chồng giấy nợ thấp dần |
| `K6.mp4` | KEY-6 · S08.1–7 | 10 s | Khung đáp lên sườn leo dốc nhất (4/1977); hạt leo rất xa trên ray, ray hổ phách nhiều năm; hũ đầy chút rồi cạn; hai chồng xu ($500/xu) mọc theo tháng; phần chồng thả nổi vượt chồng cố định thành **khối xu đỏ** = 43% chồng cố định |
| `K7.mp4` | KEY-7 · S09.4–S10.3 | 10 s | Núm trên thanh trượt mang ray–kẹp–hạt; kẹp to dần: ô đỏ hạ thành xám ở cả hai khay, khay phải sạch hẳn từ 2 điểm, khay trái luôn còn lớp đỏ mỏng, khối xu đỏ nhỏ lại nhưng còn; trượt ngược về −1: hai khay đỏ lại, khối đỏ cao lên |
| `thumb-concept.png` + `.json` | gói | — | Khung trên sườn 1977, hạt cao trên ray hổ phách, hai chồng xu với khối đỏ; "Variable / or fixed?" (3 chữ, 80 px); huy hiệu ILLUSTRATIVE 32 px ở vùng chừa góc trên phải; không số |

Mỗi clip 1280×720, 30 fps, H.264 High (yuv420p, BT.709, CRF 20), **không track âm** (ffprobe: 1 stream video). Dải: `K*-strip.png` và `K*-strip-masked.png` = lưới 3×2 (6 khung 636×358, số 1–6 ở dải trên mỗi khung, không chú thích). Bản che dựng bằng cờ trong mã (`APP.strip(times, true)` → `MODE.mask`): **mọi hộp chữ, kể cả chữ ILLUSTRATIVE, được thay bằng khối phẳng `surface #171B22` đúng hộp glyph** (tấm nền `bg` vẫn vẽ; viên huy hiệu `warn` còn lại như một khung rỗng). Không có chữ in trên vật thể nào (thẻ đề nghị chỉ có hình vẽ), nên không còn chữ nào lọt qua lớp che.

## Số trên màn hình → claim (`numbers.md`, qua `CL(id)` = đúng chuỗi `display` của `out/claims.json`)
- K1: `fixed_rate` 9%, `var_start` 7.5%. K2: `gap_start` 1.5 points (các mức khác chỉ là chữ: bigger / smaller / zero / negative). K5: `first_start` January 1954, `term` "10 years (120 monthly payments)", `last_start` September 2016.
- K3: `share_rate_above_fixed` 76.2%, `share_all` 14.2%, `share_early` 28.4%, `share_late` 3.5%. Nhãn thời kỳ "starts 1954–1980" / "starts 1981 on" = cách chia của mô hình (`n_early`, `n_late`, như lời kịch bản). Hai số 28.4% / 3.5% hiện **cùng lúc** (một phép so) — ngoại lệ duy nhất với "một số mỗi lúc".
- K6: `worst_start` April 1977, `worst_peak_rate` 19.3%, `fixed_int` $26,005, `worst_diff` +$11,219. K7: `gap_start` 1.5 points, `gap20_late` 0%, `gap30_early` 10.5%.
- Hình (không in số) cũng đúng dữ liệu: 574/753 đoạn ray hổ phách (= 76.2%), 107 ô đỏ ở 1.5 điểm (= 14.2%), ô đỏ theo từng khoảng chênh −1…3 bước 0,25 (`sensitivity`, `gap*`), khối đỏ K7 = `worstAt[gap]`, K6 xu = lãi từng tháng. `src/build_data.py` chạy lại đúng lõi `model/model.py` và **assert** khớp `out/model.json` (753 cửa sổ, 15 mức `sensitivity`) và claim (`share_rate_above_fixed`, `gap20_early`, `gap30_early`, `gap20_late` = 0, xấu nhất luôn 1977-04).
- ILLUSTRATIVE luôn hiện ở K1–K7 (mọi khung đều là khoản vay của Leah). Nguồn dãy núi: "3-month Treasury bill rate, via FRED" (K3–K7).

## Màu (mọi hex dùng trên hình)
**Token (UI và vai, `episodes/ep001/design/c3/final/tokens.json`, không thêm màu UI):**

| Vai | Token | Hex | Ở đâu |
|---|---|---|---|
| nền, tấm nền chữ | `bg` | `#0E1116` | nền canvas, tấm nền đặc dưới **mọi** chuỗi (D2) |
| khối che chữ (bản masked) | `surface` | `#171B22` | chỉ trong `K*-strip-masked.png` |
| chữ chính, số nhấn; **Leah** (hạt/mốc bát diện) | `ink` | `#F2F4F7` | kênh thứ hai của Leah = **hình bát diện** |
| chữ phụ cạnh số (D5), nguồn; lãi cố định (thép); ô "không đắt hơn" | `ink-muted` | `#9AA4B2` | ô xám **dẹt** |
| T-bill (dãy núi, dây sống núi, khung) | `accent` | `#4C8DFF` | dây sống núi `#9CC2FF`, viền khung `#8DB6FF` (sắc sáng hơn của accent cho vật phát sáng) |
| lãi vượt 9% | `warn` | `#F2B441` | **chỉ** ống sáng trên thanh ray; + nền huy hiệu ILLUSTRATIVE (chữ `bg`) |
| đắt hơn tổng cộng | `negative` | `#E5484D` | **chỉ** ô khay (cao gấp 5 ô xám) và xu đỏ phần đắt hơn; không bao giờ trên ray |
| đệm / tiết kiệm, kẹp khoảng chênh | `positive` | `#3FBF7F` | nước trong hũ (mặt nước `#7FE0AE`), dòng rót, khe hạt–ray, kẹp |

**Vật liệu 3D (không phải màu UI, không dùng cho chữ):** gỗ `#5E412D` (vân `#62442F`, `#5A3E2A`, `#3B281C`, `#2A1C12`), tường `#1A1E26`, giấy `#EFEBE2` / `#DCD6C8` / thẻ `#D6CFBF`, `#CFC8B8`, đường in trên thẻ `#5B6573` (thẳng) và `#2F63C4` (gợn), thép `#8E98A6`, xu `#C3C8CF`, khay `#232831`, ô chưa có kết quả `#E6E1D6`, thuỷ tinh `#CFE3F2` / vành `#DDE6EE`, đế mốc `#3A3F48`, vòng tối ô xấu nhất `#1A1D24`, thanh trượt `#2A303B`, ánh sáng `#FFE6C4` (đèn chính) / `#8FA3C8`–`#1A1410` (bán cầu) / `#A9B6CF` (viền), phát xạ hạt `#C9D2E0`, bóng mờ viền khung `rgba(14,17,22,0.45)`.

**D3 — mô phỏng protan/deutan** (`src/colors.py`, Machado 2009 mức 1.0 trên sRGB tuyến tính; bảng đầy đủ `logs/colors.md`, gồm cả màu **lấy mẫu từ khung đã render**):

| Cặp phải phân biệt | ΔE00 protan / deutan (token) | (render) | Xám | Đạt? → kênh thứ hai |
|---|---|---|---|---|
| ô đỏ vs ô xám | 29.7 / 30.6 | 26.2 / 22.5 | 1.55 (render 1.75) | **đạt**; thêm chiều cao (đỏ cao 5×) |
| hổ phách vs đỏ | 30.0 / **18.1** | 24.6 / **14.7** | 2.12 | **trượt deutan** → không bao giờ chung vật: hổ phách chỉ là ống trên ray, đỏ chỉ là ô/xu |
| xanh vs đỏ | 24.4 / **11.5** | 22.4 / **16.3** | 1.67 | **trượt deutan** → hũ chất lỏng vs ô/xu; chỉ cùng khung ở K6 (hũ cạn khi xu đỏ mọc) và K7 (kẹp vs ô) |
| xanh vs hổ phách | **11.8** / **18.2** | **16.3** / **19.4** | **1.27** (render 1.12) | **trượt** → kẹp/khe xanh là thanh **đứng** giữa hạt và ray, hổ phách là ống **nằm** bọc ray; ở K2 kẹp đổi sang xám khi ray hổ phách |
| hổ phách vs thép (ray thường) | 35.5 / 36.9 | 24.8 / 24.5 | **1.37** (render 1.08) | ΔE đạt, thang xám trượt → ống hổ phách to hơn ray 1,45× (độ dày) |
| núi (accent) vs ô xám | 20.0 / 21.9 | 24.7 / 27.9 | **1.27** (render 1.60) | đạt ΔE; khác vật/khác chỗ |
| Leah (ink) vs thép | 20.2 / 20.9 | — | 2.29 | đạt; + hình bát diện |

Vì bộ màu là token cố định (Q1=A), ba cặp trượt không sửa được bằng màu; đã dựa vào hình dạng/vị trí như trên. Đề nghị P kiểm lại bằng mô phỏng của mình trên các dải.

## Tự kiểm khi dựng (đo từ khung render, `logs/render-log-K*.json → audit`)
Đo mỗi 1/6 s (K1 48 khung … K7 60 khung; 1 125 lượt chuỗi), chỉ tính chuỗi đã hiện đủ (alpha 1): khung được vẽ lại **không glyph**, rồi đo khoảng cách từ hộp glyph tới pixel gần nhất khác màu tấm nền của nó (= nét đồ hoạ hoặc mép tấm nền khác), và khoảng cách hình học hộp–hộp giữa các chuỗi.

| Clip | Khoảng cách nhỏ nhất chữ→đồ hoạ (D4 ≥ 4) | chữ→chữ (≥ 4) | Tương phản nhỏ nhất (≥ 4,5) | Cỡ nhỏ nhất @720 → @1080 (≥ 40) | Ra vùng an toàn |
|---|---|---|---|---|---|
| K1 | 7 px | 36 px | 7.50:1 (`fixed`, muted/bg) | 30 → 45 px | 0 |
| K2 | 7 px | 37 px | 7.50:1 | 30 → 45 px | 0 |
| K3 | 8 px | 38 px | 7.50:1 | 27 → 40.5 px | 0 |
| K4 | 7 px | — (1 chuỗi + huy hiệu, nguồn) | 7.50:1 | 27 → 40.5 px | 0 |
| K5 | 7 px | 30.6 px | 7.50:1 | 27 → 40.5 px | 0 |
| K6 | 7 px | 19 px | 7.50:1 | 27 → 40.5 px | 0 |
| K7 | 7 px | 36 px | 7.50:1 | 27 → 40.5 px | 0 |
| thumb | 8 px | 49 px | 10.25:1 (huy hiệu `bg` trên `warn`) | 32 (huy hiệu) / 80 (chữ) | 0 |

- D2: **mọi** chuỗi nằm trên tấm nền **đặc** `bg #0E1116` (đệm 12×8 px) — kể cả chuỗi chỉ đè lên tường/núi; không chuỗi nào chạm vật liệu 3D. Tương phản đo trên tấm nền: `ink` 17.16:1, `ink-muted` 7.50:1, huy hiệu `bg`/`warn` 10.25:1.
- D4: khoảng cách 7–8 px là đệm tấm nền (nét đồ hoạ bị tấm nền che); không có nét 2D nào vẽ đè lên tấm nền.
- D5: mọi chữ phụ cạnh một số nhấn ("fixed", "variable, starts lower", "head start", "rate above 9% at some point", "cost more in total", "starts …", "Leah") dùng `ink-muted`; số dùng `ink`.
- G-014: bậc chữ = Tập 1 × 0,8 (G-009 C3) × 2/3 (1080→720): hero 80, number 52, head 40, caption 34, label 30, note 27, badge 32 px @720 (= 120 / 78 / 60 / 51 / 45 / **40,5** / 48 @1080). Hàm `text()` không nhận cỡ khác.

## Thời gian render (CPU, đo thật)
Chromium headless (Playwright, `/opt/pw-browsers`) + WebGL **SwiftShader** (ANGLE/Vulkan phần mềm), three.js 0.186.1, bóng PCF 2048², ACES; khung RGBA → PyAV libx264. Máy 4 vCPU Intel Xeon 2.80 GHz, **2 tiến trình song song** (máy dùng chung với H2/H3).

| Clip | Frame | Giây máy | Giây máy / giây phim |
|---|---|---|---|
| K1 | 240 | 108 | 13.5 |
| K2 | 300 | 163 | 16.3 |
| K3 | 300 | 168 | 16.8 |
| K4 | 300 | 200 | 20.0 |
| K5 | 300 | 195 | 19.5 |
| K6 | 300 | 168 | 16.8 |
| K7 | 300 | 158 | 15.8 |
| **Tổng** | 2 040 (68 s) | 1 160 | **17.1** |

(Thời gian là phần render video; mỗi clip thêm ~40–60 s cho lượt đo D4 và hai dải.) Ước cho cả tập ~9 phút ở 720p: ~2,6 giờ một tiến trình; ở 1080p chi phí điểm ảnh ×2,25.

## Chạy lại
```
npm i three@0.186.1                                  # trong một thư mục tạm, không vendor
python3 src/build_data.py                            # đọc data/raw/TB3MS.csv (fetch.py), assert, ghi src/data.js (gitignore)
THREE_DIR=<tạm>/node_modules/three/build src/run2.sh K1 K2 K3 K4 K5 K6 K7 THUMB
node src/render.js K3 --still 6.2 [--mask]           # ảnh tĩnh vào work/
python3 src/colors.py logs/sampled-colors.json       # D3
```
Mã: `src/engine.js` (chữ, che, đo, dải), `src/world.js` (mọi vật), `src/hist.js` (bàn lịch sử), `src/k1.js`…`k7.js`, `src/thumb.js`, `src/render.js`, `src/encode.py` (chép từ Tập 1).

## Tự đánh giá khi che chữ (trước kiểm mù)
- **Mạnh:** KEY-2 (độ dài kẹp đổi, lật), KEY-3 (ray gần hết hổ phách, khay ít đỏ, trái đỏ hơn), KEY-6 (khối đỏ trên chồng xu), KEY-7 (đỏ rút khi kẹp to, khay phải sạch, khay trái không sạch).
- **Vừa:** KEY-5 (khung trượt + ô rơi rõ; "chép hình lịch sử" nhờ hạt cưỡi chính sống núi, nhưng ô trắng "chưa có kết quả" có thể khó hiểu); KEY-4 (ba hũ đầy/lõm/cạn đọc được; chồng giấy nợ và "dòng to nhất lúc đầu" khó thấy — lãi của ba lần chạy đổi nhiều hơn dư nợ).
- **Yếu:** KEY-1 — "đứng yên vs lên xuống, tương lai mờ" rõ, nhưng "**có người** đang cân nhắc" chỉ là một mốc kim cương đung đưa giữa hai thẻ; người xem có thể không đọc ra một con người.

## Giới hạn
- Hình học đơn giản (hộp, trụ, ống, khối đùn); không GI; đọc là "đồ vật trên bàn" chứ chưa phải ảnh thực.
- Dãy núi là TB3MS thật nhưng không có trục năm (chỉ mốc chữ ở K5/K6 và nhãn thời kỳ ở K3/K7); "nửa leo / nửa xuống" đọc bằng hình núi.
- K4: thang hũ $14,000 = đầy (chung ba hũ); K6 dùng thang riêng $2,000 = đầy để thấy "đầy chút ít" (mỗi khung một thang, không in số).
- K6: xu = $500, làm tròn tới xu gần nhất (fixed 52, variable 74 → khối đỏ 22 xu ≈ 43%).
- Chuyển động giữa các nấc khung và giữa các mức khoảng chênh K7 là nội suy hình (ô đỏ đổi dần giữa hai mức 0,25); không in số trung gian.
- Ba cặp màu trượt ngưỡng D3 dưới deutan/protan (bảng trên) — giữ token, dựa vào hình dạng.
- `work/` (ảnh tĩnh, log thô, ảnh kiểm 10% thumbnail) và `src/data.js` không commit (`.gitignore` của thư mục).

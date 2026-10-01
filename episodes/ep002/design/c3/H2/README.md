# H2 · "Hình học của lãi" — Tập 2, C3 (DESIGN, 01/10/2026)

Ý đồ viết trước khi render: `intent.md`. Không commit/push (P commit).

## Ý tưởng hướng

Mọi ý nằm trên **một mặt phẳng lãi suất** (ngang = tháng, dọc = lãi). Lãi cố định là **thanh ray** ngang ở 9%. Lãi thả nổi của Leah là **một đường** (đầu đường là hạt thoi của Leah) chép đúng hình dạng **dải địa hình T-bill** 1954–2026. Phần giữa đường và ray là **diện tích**: dưới ray = xanh (`positive`, tháng rẻ hơn), trên ray = hổ phách (`warn`, tháng vượt 9%; đoạn ray bên dưới sáng hổ phách). Diện tích xanh tích vào một **bể** (phần đệm); tháng hổ phách rút bể. Kết quả của một lần chạy là **dấu của phần còn lại trong bể**: trên vạch 0 (xanh) hay dưới vạch 0 (đỏ sọc, `negative`). Mỗi lần chạy thả một **ô** thẳng xuống **hai thùng** nằm đúng dưới hai nửa địa hình (nửa leo / nửa xuống); thùng sắp lại thành **thanh tỉ lệ** (diện tích đỏ = tỉ lệ đắt hơn). Tiền lãi phải trả là **diện tích khối** (KEY-6, KEY-7): khối xám lãi cố định, khối đỏ sọc chồng lên = phần trả thêm.

## Từng KEY mang nghĩa thế nào (khi tắt tiếng, che chữ)

| KEY | Clip | Chuyển động mang ý | Tự đánh giá khi che chữ |
|---|---|---|---|
| KEY-1 | `K1.mp4` 8 s | Ray kéo ngang rồi đứng yên; hạt thoi hiện ngay dưới ray; phía trước hạt, nhiều đường tương lai rẽ lên/xuống thay nhau sáng rồi tắt; khe giữa hạt và ray sáng xanh. | Trung bình: "một mức đứng yên vs một đường bắt đầu thấp hơn rồi lang thang" đọc được; "ai đó đang cân nhắc" chỉ có hạt thoi gánh. |
| KEY-2 | `K2.mp4` 9 s | Ngoặc bật vào khe ray–hạt cạnh một thước có vạch; hạt trượt xuống (ngoặc dãn), lên (co), chạm ray (khép thành "="), vượt lên (ngoặc lật, xanh → hổ phách). Lát diện tích đầu tiên đổi cỡ theo ngoặc. | Mạnh. |
| KEY-5 | `K5.mp4` 10 s | Dải địa hình mọc từ trái sang; khung 10 năm đặt lên; đoạn địa hình trong khung **bay lên** và thành đường của hạt (cùng hình, dời về 7,5%); khung bước phải, nhanh dần, vệt khung cũ chồng lên nhau (phần chung tô đậm), mỗi bước một ô xám rơi thẳng xuống thùng dưới chỗ bắt đầu; phễu nối khung với mặt phẳng. | Trung bình–mạnh trong clip; trên dải 6 khung yếu hơn (cú "chép" chỉ thấy ở khung 2). |
| KEY-3 | `K3.mp4` 10 s | Khung quét cả lịch sử; mỗi lần dừng ray sáng hổ phách; hai hàng ô: hàng trên (vượt 9%) gần kín hổ phách, hàng dưới (đắt hơn) chủ yếu xám, đỏ dồn về nửa trái; cuối cùng hai hàng dời lên, phóng to và **sắp lại** thành thanh tỉ lệ: hổ phách dài, đỏ ngắn, đỏ trái ≫ đỏ phải; ô xấu nhất (viền `ink`) đứng yên trong thùng trái. | Mạnh về "nhiều hổ phách, ít đỏ, đỏ nằm bên trái"; người xem phải tự ghép hai hàng là cùng các lần chạy. |
| KEY-4 | `K4.mp4` 10 s | Ba lần chạy cùng lúc, một thang đô la: đường trôi xuống → bể đầy nhanh nhất lúc đầu (nêm nợ xám cao nhất) rồi đầy tràn; một nhấp ngắn trên ray → mép bể lóe hổ phách, bể chỉ lõm nhẹ; leo sớm và cao nhiều năm (khởi đầu 4/1976) → bể cạn rồi sang đỏ dưới vạch 0. | Mạnh (so ba bể cuối: đầy / vừa / âm). Vết lõm của nhịp ngắn chỉ ~$40 nên thấy bằng mép lóe hổ phách, không thấy bằng chiều cao. |
| KEY-6 | `K6.mp4` 10 s | Khung trượt và **hạ** xuống đoạn leo dốc ở nửa trái; đường leo xa trên ray, diện tích hổ phách khổng lồ nhiều năm; bể lên chút xíu, cạn, chìm sâu đỏ; khối đỏ gấp lại bay lên **đặt trên** khối xám lãi cố định — cao 43% khối xám. | Mạnh. |
| KEY-7 | `K7.mp4` 10 s | Thanh trượt kéo dãn ngoặc 1,5 → 2 → 3; thanh đỏ của hai thùng co: thùng phải hết đỏ ở 2, thùng trái còn lớp đỏ mỏng ở 3; khối đỏ trên khối xám co nhưng không mất; kéo ngược về −1 (ngoặc khép, lật hổ phách): hai thùng đỏ dâng, khối phình. | Mạnh. |

Giữa hai mốc tham số đã chạy (bước 0,5 điểm) thanh tỉ lệ và khối đỏ nội suy tuyến tính trong lúc trượt; **chỉ in số ở mốc có claim** (1.5, 2, 3).

## Số trên hình → claim ID (`numbers.md`)

| Clip | Chuỗi | Claim |
|---|---|---|
| K1 | 9% · 7.5% | `fixed_rate`, `var_start` |
| K2 | 9% · 1.5 points | `fixed_rate`, `gap_start` |
| K3 | 76.2% · 14.2% · 28.4% · 3.5% (lần lượt, mỗi lúc một số) | `share_rate_above_fixed`, `share_all`, `share_early`, `share_late` |
| K4 | (không số) | — |
| K5 | January 1954 · 10 years | `first_start`, `term` |
| K6 | 9% · April 1977 · 19.3% · $26,005 (muted) · +$11,219 | `fixed_rate`, `worst_start`, `worst_peak_rate`, `fixed_int`, `worst_diff` |
| K7 | 1.5 points · 8.8% (ở 2 điểm) · 4.5% (ở 3 điểm) | `gap_start`, `spread2_share`, `spread3_share` |

Mọi số đi qua `CL(claimId)` (chuỗi `display` của `out/claims.json`; riêng "10 years" viết tay, khớp `term`). `src/check.py`: 0 token số ngoài claim. Mọi khung có huy hiệu **ILLUSTRATIVE** (góc trên phải, 48 px @1080 = 32 px @720) vì mọi khung là khoản vay của Leah. Hình dạng đường/diện tích/bể/thùng/khối đều tính lại từ dữ liệu (`src/build_data.py`, cùng công thức `model/model.py`, assert khớp 27 claim: `n_starts`, `share_all/early/late`, `share_rate_above_fixed`, `worst_diff` (+ 4/1977, đỉnh 19.3%), `fixed_int`, `gap{m10,00,10,20,30}_{early,late,worst}`, `spread{m1,0,1,2,3}_share`).

## Màu (chỉ token Tập 1, `episodes/ep001/design/c3/final/tokens.json`)

| Vai | Token | Hex | Kênh thứ hai |
|---|---|---|---|
| nền | `bg` | `#0E1116` | — |
| khối che chữ (dải che) | `surface` | `#171B22` | — |
| viền bể/thùng, phễu, trục địa hình | `grid` | `#2A303B` | — |
| ray 9% (cố định), vạch 0 của bể, chữ chính | `ink` | `#F2F4F7` | đường ngang dày, không bao giờ động |
| Leah | `ink` | `#F2F4F7` | **hình thoi** (viền `bg`) |
| chữ phụ, thước, nêm nợ, ô "không đắt hơn", khối lãi cố định | `ink-muted` | `#9AA4B2` | — |
| T-bill / đường thả nổi / dải địa hình | `accent` | `#4C8DFF` | đường mảnh có đỉnh gợn |
| lãi vượt 9% | `warn` | `#F2B441` | luôn **trên** ray; diện tích + đoạn ray sáng |
| đắt hơn tổng cộng | `negative` | `#E5484D` | **sọc chéo `bg`** trên mọi diện tích; luôn **dưới** vạch 0 của bể; ô vuông |
| đệm / tiết kiệm | `positive` | `#3FBF7F` | luôn **dưới** ray (diện tích) / **trên** vạch 0 (bể); mảng đặc |
| huy hiệu | `warn` nền, chữ `bg` | — | — |

Alpha dùng trên `bg`: diện tích xanh 0,55 (≈ `#2A7353`), diện tích hổ phách 0,72 (≈ `#B48634`), dải địa hình `accent` 0,16, ô xám 0,55.

**D3 · mô phỏng protan/deutan** (`src/cvd.py`, Machado 2009 mức 1,0, CIEDE2000; cặp vai cần phân biệt):

| cặp | ΔE00 thường | protan | deutan | tương phản thang xám |
|---|---|---|---|---|
| warn / negative | 40.3 | 30.0 | **18.1** | 2.12:1 |
| positive / negative | 70.8 | 24.4 | **11.5** | 1.67:1 |
| positive / warn | 38.7 | **11.8** | **18.2** | **1.27:1** |
| accent / ink-muted | **17.8** | 20.0 | 21.9 | **1.27:1** |
| ink-muted / negative (ô xám / ô đỏ) | 35.1 | 29.7 | 30.6 | 1.55:1 |
| accent / positive | 47.8 | 48.2 | 44.9 | **1.37:1** |
| accent / warn | 58.0 | 59.5 | 63.7 | 1.73:1 |
| ink / warn | 30.7 | 32.2 | 30.4 | 1.67:1 |
| ink / accent (ray / đường thả nổi) | 34.6 | 33.2 | 37.4 | 2.90:1 |

Ba cặp **không đạt** ΔE ≥ 20 dưới CVD (warn/negative deutan 18,1; positive/negative deutan 11,5; positive/warn 11,8/18,2 và thang xám 1,27) — giới hạn của bộ token đã ký, không thêm màu. Bù bằng kênh thứ hai: **vị trí** (xanh luôn dưới ray / trên vạch 0; hổ phách luôn trên ray; đỏ luôn dưới vạch 0) và **hoa văn** (đỏ luôn có sọc chéo, xanh và hổ phách đặc). Đỏ và hổ phách không bao giờ ở cùng một vật (hàng/thùng khác nhau; trong bể mép hổ phách chỉ hiện khi bể còn dương). `accent`/`ink-muted` (17,8 thường) không đứng cạnh nhau như hai vai cần phân biệt: ray là `ink` (không phải `ink-muted`). P kiểm lại bằng mô phỏng trên dải.

## Tự kiểm khi dựng (đo trên khung đã render, `render-log-K*.json → selfCheck`, mỗi khung thứ 3; px ở 720p)

Cách đo: dựng lại khung **không có lớp chữ**; với mỗi hộp chữ (hộp mực thật `measureText`) đang hiện đủ (alpha ≥ 0,98): khoảng cách tới điểm ảnh đồ hoạ gần nhất (khác `bg` > 30/765) trong bán kính 14 px; tương phản = chữ so với điểm ảnh tệ nhất dưới hộp; khoảng cách hộp–hộp.

| Clip | min chữ→đồ hoạ (D4) | min chữ→chữ | min tương phản (D2) | chữ nhỏ nhất (G-014) | ra ngoài vùng an toàn |
|---|---|---|---|---|---|
| K1 | ≥ 14 px | 12,6 px* | 7,50:1 | 48 px @1080 (32 @720) | 0 |
| K2 | ≥ 14 px | 12,6 px* | 7,50:1 | 48 | 0 |
| K3 | 6,0 px | ≥ 14 px | 10,25:1 | 48 | 0 |
| K4 | ≥ 14 px | ≥ 14 px | 7,50:1 | 48 | 0 |
| K5 | ≥ 14 px | ≥ 14 px | 7,50:1 | 48 | 0 |
| K6 | 10,0 px | 12,6 px* | 7,50:1 | 48 | 0 |
| K7 | ≥ 14 px | ≥ 14 px | 10,25:1 | 48 | 0 |
| thumb | ≥ 14 px | 22,7 px | 10,25:1 | 32 px @720 (huy hiệu), chữ chính 100 px @720 | 0 |

\* 12,6 px là khoảng trắng giữa số và chữ phụ trong cùng một nhãn ("9%" + "fixed").
- Vòng đầu đo được 5 chỗ trượt (K1 "fixed" chạm đường tương lai 0 px / 1,51:1; K6 "fixed" 0 px; K4 "still owed" 3 px; K5 "10 years" 3,7 px; K7 "4.5%" 3,3 px) → đã dời nhãn/đổi thời điểm, render lại; bảng trên là bản cuối.
- Chữ đều nằm trên nền `bg` phẳng (không có chữ trên diện tích màu), nên tương phản cục bộ = tương phản token: `ink` 17,16, `ink-muted` 7,50, chữ `bg` trên huy hiệu `warn` 10,25.
- D5: chữ phụ cạnh số ("fixed", "variable") và số phụ ("$26,005" cạnh "+$11,219") dùng `ink-muted`.
- Mỗi lúc tối đa một số nhấn (+ huy hiệu); riêng cuối K6 có "$26,005" (muted) cạnh "+$11,219".
- Viên huy hiệu ILLUSTRATIVE (đo từ mép viên, `render.js --badge-check`, mọi khung thứ 3): ≥ 14 px ở K1, K2, K4–K7 và thumbnail; **12,6 px** ở K3 (t = 2,5 s, đỉnh đường của lần chạy 1972 bên dưới).
- Không đo: chữ trong lúc mờ dần (alpha < 0,98).

## Thời gian render (CPU, 4 lõi dùng chung, 2 tiến trình song song)

| Clip | giây phim | giây máy | giây máy / giây phim |
|---|---|---|---|
| K1 | 8 | 32,3 | 4,0 |
| K2 | 9 | 36,5 | 4,1 |
| K3 | 10 | 79,1 | 7,9 |
| K4 | 10 | 52,1 | 5,2 |
| K5 | 10 | 44,5 | 4,5 (chạy một mình) |
| K6 | 10 | 55,2 | 5,5 |
| K7 | 10 | 47,1 | 4,7 |

Cả bộ (7 clip + 14 dải + thumbnail + tự kiểm) ≈ 3 phút đồng hồ. Ước tính phim 9 phút toàn H2: ~40–70 phút máy. Canvas 2D thuần, không WebGL.

## Tệp

- `K1.mp4…K7.mp4` (1280×720, 30 fps, H.264 High yuv420p BT.709, không tiếng); `K*-strip.png` / `K*-strip-masked.png` (lưới 3×2, đánh số 1–6; bản che thay mọi hộp chữ và cả viên huy hiệu bằng khối `surface` ngay trong mã dựng, cờ `mask`).
- `thumb-concept.png` + `thumb-concept.json` (`texts[{text, box:[x,y,w,h] @1280×720, fontPx}]` + kết quả tự kiểm); `endscreen.md`; `rights.md`; `intent.md`.
- `render-log-K*.json`: claim ID, mọi chuỗi, tự kiểm từng chuỗi, thời gian.
- `src/`: `engine.js` (mẫu mã từ engine Tập 1: bậc chữ, `CL()`, easing, API khung), `k1…k7.js`, `thumb.js`, `render.js`, `render_all.sh`, `build_data.py`, `check.py`, `cvd.py`, `sheet.py`, `page.html`.
- `work/` (không commit, `.gitignore`): `data.js` (chuỗi suy từ FRED TB3MS), ảnh tĩnh kiểm tra.

Dựng lại: `python3 src/build_data.py && src/render_all.sh && python3 src/check.py` (cần `data/raw/TB3MS.csv`, tải bằng `data/fetch.py`).

## Giới hạn

- Đường thả nổi trên mặt phẳng nối tuyến tính giữa các tháng (lãi thật đổi theo bậc tháng); diện tích dưới/trên ray là hình **lãi suất**, còn bể là **đô la** (đã nhân dư nợ); hai thứ liên hệ bằng chuyển động đồng bộ và nêm nợ, không cùng một thang. Đây là chỗ H2 "đúng hình" kém nhất: diện tích hổ phách to không tỉ lệ thẳng với đô la mất (tháng cuối dư nợ nhỏ).
- KEY-4: vết lõm thật của nhịp ngắn (~$40) quá nhỏ để thấy bằng chiều cao; hình dựa vào mép bể lóe hổ phách.
- KEY-3: 753 ô ở 720p rộng ~1,2 px mỗi ô; đọc như dải mật độ, không đếm được từng ô.
- Không có nhãn chữ cho hai nửa lịch sử (năm 1980/1981 không có claim `display`); nửa trái/phải đọc bằng hình địa hình phía trên.
- Ba cặp màu dưới ngưỡng CVD (xem trên) — cần P/ chủ dự án xác nhận kênh thứ hai là đủ.
- Chưa kiểm mù (việc của P).

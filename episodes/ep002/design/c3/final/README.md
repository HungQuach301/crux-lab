# Tập 2 · C3 final (D2) — giai đoạn 1: KEY-1 và KEY-7 thiết kế lại

Hệ hình: `system.md`; token: `tokens.json` (Tập 1 + E2). Không commit/push. Dựng lại: `python3 src/build_data.py`, rồi `NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node src/render.js K1` (và `K7`). `work/` (data.js suy từ FRED, render log, ảnh tĩnh) không commit.

| Tệp | |
|---|---|
| `K1.mp4` (8 s), `K7.mp4` (10 s) | 1280×720, 30 fps, H.264 High, không tiếng |
| `K1/K7-strip.png`, `-strip-masked.png` | 6 khung 3×2 đánh số; bản che: mọi hộp chữ + huy hiệu thay bằng khối `surface` bằng cờ `mask` trong `engine.js → text()/badge()` |

## KEY-1 (nền H2) — "một người, hai lời mời"
Một hình người chung chung (`ink`, không mặt, thoi khoét ở ngực = Leah) đứng một mình (khung 1) → hai tấm thẻ lời mời (viền `ink-muted`, góc gấp) bay lên hai tay (2) → thẻ trái: một đường **bằng phẳng** (3) → thẻ phải: bắt đầu **thấp hơn** (ngoặc `cushion` dưới bản sao mờ của mức thẻ trái), rồi **lên xuống** (một lần chạy thật của khoản vay Leah, bắt đầu 12/1962, không ghi nhãn) với hạt thoi ở đầu (4) → bập bênh: thẻ trái nâng, đầu nghiêng về nó, rồi ngược lại (5) → đứng yên, cả hai thẻ đầy đủ (6).

## KEY-7 (nền H3 + nêm) — "khởi đầu lớn hơn → ít đỏ hơn; nửa sau sạch, nửa trước còn đỏ"
Một chiều duy nhất: **−1 điểm trước** (hai thùng ô gần kín đỏ) → nới dần qua 0, 1.5 (Leah, thoi ở mép nêm) → **2** (thùng phải sạch hẳn, viền sáng `ink`) → **3**, giữ tới hết clip. Dưới mỗi nửa lịch sử một "thang": một thanh đỏ sọc mỗi mức khởi đầu đã qua + nêm (`warn` khi âm, `cushion` khi dương) mở rộng bên dưới — mọi khung đều thấy vệt "nêm rộng hơn → thanh ngắn hơn". **Khung 5 và 6 đều ở trạng thái rộng (3 điểm, đỏ thấp nhất); không có cảnh quét ngược.** Phần "khởi đầu nhỏ/đảo thì tệ hơn" của S10.1 được kể bằng phần đầu của cùng một chiều (−1 trước); số của S10.1 để lại cho phase 2.

## Số trên hình → claim ID
| Clip | Chuỗi | Claim |
|---|---|---|
| K1 | 9% · 7.5% | `fixed_rate`, `var_start` |
| K7 | 1.5 points · 0% (nửa 1981 về sau, ở 2 điểm) · 10.5% (nửa 1954–1980, ở 3 điểm) | `gap_start`, `gap20_late`, `gap30_early` |

Thanh và ô K7 tính lại từ dữ liệu (`src/build_data.py`, cùng công thức `model/model.py`, assert khớp `gap{m10,m05,00,05,10,15,20,25,30}_{early,late,worst}`, `n_starts`, `n_early`, `n_late`); giữa hai mức đã chạy (bước 0,5) thanh nội suy tuyến tính, ô đổi màu mờ chuyển; số chỉ in ở mức có claim.

## Tự kiểm (đo trên khung render, mỗi khung thứ 3 + 6 khung dải; px ở 720p; `work/render-log-K*.json`)
| Clip | min chữ→đồ hoạ (≥ 4) | min chữ→chữ | min tương phản (≥ 4,5:1) | chữ nhỏ nhất (≥ 40 @1080) | ngoài vùng an toàn |
|---|---|---|---|---|---|
| K1 | ≥ 14 px (bán kính đo) | 12,6 px* | 7,50:1 (`ink-muted` "fixed"/"variable" trên `bg`) | 48 px (label 54, badge 48) | 0 |
| K7 | 8,3 px ("10.5%" ↔ thanh 1 điểm) | ≥ 14 px | 10,25:1 (huy hiệu); chữ khác 17,16:1 | 48 px (badge; label 54, number 96) | 0 |

\* khoảng trắng giữa số và chữ phụ trong cùng nhãn ("9%" + "fixed"). Huy hiệu đo từ mép viên. Không có chữ trên mảng màu; `costlier` không dùng cho chữ. Render: K1 ≈ 30 s máy, K7 ≈ 36 s máy (CPU, canvas 2D).

## Giới hạn
- K1: đường thẻ phải là dữ liệu thật nên lởm chởm theo tháng; "bắt đầu thấp hơn" dựa vào ngoặc `cushion` + vạch mờ (chênh 1,5 điểm ≈ 41 px ở 720p).
- K7: thanh/ô không có nhãn năm (không claim cho 1980/1981); hai nửa đọc bằng vị trí dưới địa hình và vạch đứt ở đỉnh 1981. Khối "lãi thêm của trường hợp tệ nhất" chưa đưa vào (để phase 2 nếu cần).
- Chưa kiểm mù (P, `gates/C3-K17-intent.md`).

## Vòng 2 (sau `gates/C3-K17-blind.md`: KEY-1 0/3, KEY-7 0/3) — bản hiện hành
Bản vòng 1 được giữ lại: `K1-r1.*`, `K7-r1.*`, `src/k1_r1.js`, `src/k7_r1.js`. `K1.mp4`, `K7.mp4` và các dải là bản vòng 2.
- **KEY-1 (8 s):** hai thẻ cùng độ cao và **không di chuyển** (chỉ hiện dần lúc đầu). **Một vạch 9% kéo liền qua cả hai thẻ**, cùng một thang đo. Thẻ phải: hạt thoi bắt đầu rõ **dưới** vạch (thanh `cushion` ở điểm đầu). Mảng `cushion` lấp khe giữa vạch và đường cho tới lần cắt vạch đầu tiên (tháng 36), sau đó đường lên xuống. Người chỉ quay đầu. (`cushion #269783` là bí danh E2 của `positive`.)
- **KEY-7 (10 s):** bỏ lưới 753 ô, bỏ nêm, bỏ địa hình. **Núm ở trên, to:** thanh cố định (`ink-muted`) và thanh "lãi thả nổi bắt đầu" (`ink`, có thoi). Khe `cushion` giữa hai thanh nới rộng theo từng mốc 0 → 1 → 1.5 → 2 → 2.5 → 3 rồi giữ nguyên. **Hai cột lớn** ("before 1981" / "from 1981") có phần đỏ sọc co lại cùng nhịp với khe. Cột phải về 0 ở mốc 2 (viền sáng `ink`). Cột trái vẫn còn đỏ ở mốc 3. Khung 6 là khe rộng nhất; không có cảnh quét ngược.
- **Số trên hình:** K1 dùng `fixed_rate`, `var_start`. K7 dùng `fixed_rate` (9%), `gap_start` (1.5 points), `gap20_late` (0%), `gap30_early` (10.5%). Nhãn cột "before 1981"/"from 1981" ghi theo `n_early`/`n_late`; số "1981" cũng có trong display của `best_start`.
- **Tự kiểm (px ở 720p):**

| Clip | chữ→đồ hoạ (≥ 4) | chữ→chữ | tương phản (≥ 4,5:1) | chữ nhỏ nhất | ngoài vùng an toàn |
|---|---|---|---|---|---|
| K1 | ≥ 14 | 12,6* | 7,50:1 | 48 px @1080 | 0 |
| K7 | ≥ 14 | 12,6* | 7,50:1 | 48 px @1080 | 0 |

\* khoảng trắng giữa "9%" và "fixed" trong cùng một nhãn.

## Giai đoạn 2 — K2–K6 trong hệ D2+E2 (K1 r2 giữ nguyên; K7 chờ chủ dự án, không đụng)
Mỗi nhịp bám sát clip H2/H3 mà chủ dự án đã xem. Chỉ đổi ba thứ cho khớp hệ: (a) màu E2: costlier `#C72323` thay `negative`, cushion `#269783` thay `positive`; (b) ray 9% dùng `ink-muted`, đường lãi của Leah dùng `ink` + thoi (`accent` chỉ dùng cho T-bill); (c) chữ không bao giờ tô màu costlier: các số K3 trước là đỏ nay là `ink`.

| Nhịp | Nền | Mã | Thời lượng | Thay đổi so với clip gốc |
|---|---|---|---|---|
| K2 | H2 | `src/k2.js` + `src/engine.js` | 9 s | màu E2, ray/đường như (b) |
| K4 | H2 | `src/k4.js` (dữ liệu `detail` trong `src/build_data.py`) | 10 s | màu E2 (bể cushion, sọc costlier), (b) |
| K3 | H3 | `src/h3/scenes.js` (`K3`) | 10 s | màu E2; số đổi từ đỏ sang `ink` |
| K5 | H3 | `src/h3/scenes.js` (`K5`) | 10 s | màu E2 (ô trung tính, không đổi hình) |
| K6 | H3 | `src/h3/scenes.js` (`K6`) | 10 s | màu E2. Dòng chú thích "Starting April 1977" ghi tên giai đoạn tệ nhất (`worst_start`). Khối thêm cao đúng 43,1% chồng cố định ($11,218.65 / $26,005.46). Nhãn cuối là **"43% more"** (`worst_share_of_fixed`), thay cho "+$11,219" |

Dựng lại: `python3 src/build_data.py && python3 src/h3/build_data.py`, sau đó chạy `node src/render.js K2|K4` và `node src/h3/render.js K3|K5|K6`, đều kèm `NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`. Dữ liệu `work/h3data.js` được assert khớp 753/753 cửa sổ trong `out/model.json`. Dải che làm bằng cờ trong mã dựng: `FLAGS.mask` (H2) hoặc `FLAGS.MASK` (H3).

**Số trên hình → claim ID** (mọi khung có khoản vay của Leah đều mang huy hiệu ILLUSTRATIVE):

| Clip | Chuỗi | Claim |
|---|---|---|
| K2 | 9% · 1.5 points | `fixed_rate`, `gap_start` |
| K3 | 76.2% · 14.2% · 28.4% · 3.5% · trục 1954 / 1981 | `share_rate_above_fixed`, `share_all`, `share_early`, `share_late`; `first_start`, `best_start_year` |
| K4 | (không có số) | — |
| K5 | "Every 10-year stretch since January 1954" · trục 1954 / 1981 | `term`, `first_start`; `best_start_year` |
| K6 | April 1977 · 19.3% · $26,005 · 43% · trục 1954 / 1981 | `worst_start`, `worst_peak_rate`, `fixed_int`, `worst_share_of_fixed`; `first_start`, `best_start_year` |

**Tự kiểm D2–D5.** Đo trên mọi khung thứ 3, chữ đã hiện đủ. Khoảng cách tính ra px ở 720p. Bộ đo H2 dừng tìm ở bán kính 14 px, bộ đo H3 ở 16 px thiết kế (= 10,7 px ở 720p); "≥" nghĩa là không có nét nào trong bán kính đó.

| Clip | chữ→đồ hoạ (≥ 4) | chữ→chữ | tương phản (≥ 4,5:1) | chữ nhỏ nhất (≥ 40 @1080) |
|---|---|---|---|---|
| K2 | ≥ 14 | 12,6* | 7,50:1 | 48 |
| K4 | ≥ 14 | ≥ 14 | 7,50:1 | 48 |
| K3 | ≥ 10,7 | 40,4 | 7,50:1 | 48 |
| K5 | ≥ 10,7 | 61 | 7,50:1 | 48 |
| K6 | 8,9 ("43%" ↔ chồng xu) | 64,5 | 7,50:1 | 48 |

\* khoảng trắng giữa số và chữ phụ trong cùng nhãn. D5: chữ phụ cạnh số ("fixed", "more", "went above the fixed rate", "cost more in total") dùng `ink-muted`. Số nhấn dùng `ink`; riêng 76.2% dùng `warn` (10,2:1).

Giới hạn: dải 6 khung của các nhịp H3 giữ khuôn của H3 (số trong ô vàng phía trên khung), còn các nhịp H2 và K1/K7 đánh số dưới khung. Bể/hũ ở K6 gần như không đầy (đệm tối đa $218, theo đúng dữ liệu).

## KEY-7 vòng 3 — phương án (A) của chủ dự án (ý đồ đã ghi trước ở `gates/C3-K7-intent-r3.md`)
Bản vòng 2 được giữ lại: `K7-r2.mp4`, `K7-r2-strip(-masked).png`, `src/k7_r2.js`, `work/render-log-K7-r2.json`. `K7.*` hiện là bản (A): 9 s, 1280×720, 30 fps, H.264 High.
- **Bố cục:** ba ô tĩnh cạnh nhau, hiện lần lượt từ trái sang phải ở 0,6 s / 3,0 s / 5,4 s. Mỗi ô hiện ra đã đầy đủ (mờ dần vào trong 0,25 s) rồi đứng yên tới cuối; không có gì lớn dần.
- **Đầu mỗi ô:** hình KEY-1 r2, gồm vạch 9% (`ink-muted`) và điểm bắt đầu thả nổi (đường `ink` có thoi) nằm thấp hơn vạch đúng bằng khoảng chênh 0 / 1.5 / 3 điểm. Cả ba ô dùng chung một thang, 70 px thiết kế mỗi điểm. Khe giữa vạch và điểm bắt đầu tô `cushion #269783`.
- **Dưới mỗi ô:** hai thùng token kiểu KEY-3, trái "1954–1980", phải "from 1981". Mỗi thùng có **20 token**, xếp 5×4. Token đỏ (`#C72323`) là đắt hơn và nằm dồn xuống đáy; token còn lại màu `grid`. Số token đỏ = tỉ lệ đắt hơn × 20, làm tròn:

| Ô | khoảng chênh (claim) | 1954–1980 | from 1981 |
|---|---|---|---|
| 1 | "0 points" (`gap00_early`/`gap00_late`, formula "gap 0.0") | 79% → **16/20** (`gap00_early`) | 42% → **8/20** (`gap00_late`) |
| 2 | "1.5 points" (`gap_start`) | 28.4% → **6/20** (`gap15_early`) | 3.5% → **1/20** (`gap15_late`) |
| 3 | "3 points" (`gap30_early`/`gap30_late`, formula "gap 3.0") | 10.5% → **2/20** (`gap30_early`) | 0% → **0/20**, sạch hẳn (`gap30_late`) |

- **Chữ:** trên hình chỉ có nhãn khoảng chênh, nhãn thùng (ghi theo `n_early`/`n_late`) và huy hiệu ILLUSTRATIVE. Không in tỉ lệ nào; các tỉ lệ chỉ thể hiện bằng số token đỏ.
- **Lưu ý về claim:** "0 points" và "3 points" không có claim nào có display đúng chuỗi đó; giá trị lấy từ formula "gap 0.0"/"gap 3.0". "1980" cũng không có trong display nào; nó lấy từ formula của `n_early` ("1954-01..1980-12").
- **Dải 6 khung (t = 1.2, 2.6, 3.6, 5.0, 6.0, 8.8):** ô 1 → ô 1 → ô 1+2 → ô 1+2 → cả ba → cả ba. Bản che làm bằng cờ `mask`.
- **Tự kiểm (px ở 720p):** chữ→đồ hoạ nhỏ nhất 8,6 (huy hiệu ↔ viền ô 3); các nhãn khác ≥ 14. Chữ→chữ ≥ 29,6. Tương phản nhỏ nhất 7,50:1 (nhãn thùng `ink-muted`); huy hiệu 10,25:1. Chữ nhỏ nhất 48 px @1080. Không có chữ ngoài vùng an toàn.

## Vòng sửa K2 và K4 (sau `gates/C3-K245-blind.md`)
Bản trước được giữ lại: `K2-v1.*`, `K4-v1.*`, `src/k2_v1.js`, `src/k4_v1.js`, `work/render-log-K2-v1.json`, `work/render-log-K4-v1.json`. `K2.*` và `K4.*` hiện là bản mới.

**K2 (8 s), dựng trên hình KEY-1 r2:** một người cầm hai thẻ cùng độ cao, vạch 9% chạy liền qua cả hai thẻ. Trên thẻ thả nổi chỉ có **điểm bắt đầu** đổi chỗ, và đổi bằng **cú nhảy**: mỗi lần nhảy, thẻ lật trong 0,36 s như thay một lời mời khác. Thứ tự: dưới xa 3 điểm → dưới gần 1.5 điểm → nằm trên vạch 0 → **cao hơn vạch −1 điểm, giữ tới cuối clip**. Khe giữa vạch và điểm bắt đầu tô `cushion` khi điểm ở dưới vạch, tô `warn` khi ở trên. Sau điểm bắt đầu không vẽ đường nào. Dải 6 khung: dưới xa → đang lật → 1.5 → trên vạch → cao hơn vạch → cao hơn vạch.
- Số trên hình: 9% (`fixed_rate`); 1.5 points (`gap_start`, chỉ hiện ở trạng thái 1.5). Huy hiệu ILLUSTRATIVE luôn bật.

**K4 (10 s): một đường lãi, một cái hũ.** Đường là lần chạy thật của khoản vay Leah bắt đầu 4/1976. Hũ chạy đồng bộ với đường từng tháng:
- Khi lãi dưới 9%, một dòng `cushion` chảy từ khe dưới vạch vào miệng hũ và hũ đầy dần.
- Khi lãi trên 9%, mặt nước viền `warn` và một dòng `warn` chảy ra từ vòi.
- Tháng 21–22 có một nhịp vượt 9% ngắn: hũ chỉ hụt khoảng $1 trên khoảng $1,036, tức gần như không đổi.
- Từ tháng 25 lãi leo dài, hũ cạn ở tháng 40.
- Từ lúc hũ cạn, một khối `costlier #C72323` có sọc hiện ra dưới hũ và lớn dần theo khoản trả thêm; cuối lần chạy là $7,577.
- **Thang đo:** hũ dùng một thang đô la ($1,046 ↔ 380 px). Khối đỏ dùng **thang riêng** ($7,577 ↔ 150 px) để vừa khung; điều này phải ghi lại vì hai thang không giống nhau.
- Số trên hình: chỉ có 9% (`fixed_rate`). Các con số $ ở trên chỉ ghi trong README, không hiện trên hình. Huy hiệu ILLUSTRATIVE luôn bật.

**Tự kiểm (px ở 720p):**

| Clip | chữ→đồ hoạ (≥ 4) | chữ→chữ | tương phản (≥ 4,5:1) | chữ nhỏ nhất (≥ 40 @1080) | ngoài vùng an toàn |
|---|---|---|---|---|---|
| K2 | 12,3 | 12,6* | 7,50:1 | 48 | 0 |
| K4 | ≥ 14 | 12,6* | 7,50:1 | 48 | 0 |

\* khoảng trắng giữa "9%" và "fixed" trong cùng một nhãn.

## K4 — sửa kỹ thuật C3d (C4, 01/10/2026)
Theo quyết định C3d (Câu 2a): hũ **bắt đầu rỗng** và **đầy lên thấy rõ** trong 2 khung đầu của dải (1/3 đầu nhịp). Bản trước giữ ở `K4-v2.mp4`, `K4-v2-strip(-masked).png`, `src/k4_v2.js`, `work/render-log-K4-v2.json`.
- Chỉ đổi định thời trong `src/k4.js`: lần chạy bắt đầu ở 0,9 s (trước đó hũ rỗng, hạt thoi ở điểm bắt đầu dưới vạch 9%); tháng 21 (≈ $1,036 trên đỉnh $1,046) ở 2,6 s; nhịp vượt ngắn 21–22; leo dài từ tháng 25 (3,3 s); hũ cạn ở tháng 40 (5,0 s); khối đỏ lớn tới cuối (8,8 s). Hình, màu, thang không đổi.
- Dải 6 khung nay lấy **đều** (tâm của 6 khoảng bằng nhau: 0,83 / 2,5 / 4,17 / 5,83 / 7,5 / 9,17 s), cùng luật với dải animatic C4: khung 1 hũ rỗng, khung 2 hũ gần đầy, khung 3 đang cạn (vạch hổ phách), khung 4–6 hũ rỗng + khối đỏ lớn dần.
- Tự kiểm: chữ→đồ hoạ ≥ 14; chữ→chữ 12,6*; tương phản 7,50:1; chữ nhỏ nhất 48 px @1080; 0 ngoài vùng an toàn. Khối đỏ vẫn **không cùng thang** với hũ ($7,577 ↔ 150 px so với $1,046 ↔ 380 px).

## K4 — nhãn "not to scale" (chủ dự án C4 Q3a)
Bản trước giữ ở `K4-v3.mp4`, `K4-v3-strip(-masked).png`, `src/k4_v3.js`, `work/render-log-K4-v3.json`. Khi khối đỏ hiện, một nhãn nhỏ **"not to scale"** (`ink-muted`, bậc `note` 48 px @1080) đứng bên trái khối (canh phải cách khối 24 px thiết kế, đường chân 1000). Tự kiểm: chữ→đồ hoạ ≥ 14 px @720; tương phản 7,50:1; 0 ngoài vùng an toàn. Hình, màu, định thời không đổi.

## C5 · V03 (vùng an toàn)
Huy hiệu ILLUSTRATIVE dời trái 18 px (H2, `src/engine.js`) / 16 px (H3, `src/h3/engine.js`) để viên nền kết thúc ở x 1824 (trước: 1842 / 1840), cùng cỡ, cùng độ cao. Các clip K*.mp4 ở thư mục này chưa dựng lại (vẫn là bản ký); phim C5 và animatic dùng vị trí mới.

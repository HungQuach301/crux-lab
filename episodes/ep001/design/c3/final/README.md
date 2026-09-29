# C3 final — style frame có chuyển động = hợp đồng hình ảnh (Tập 1)

DESIGN LEAD C3 final, 29/09/2026. Hướng **D** (H1 vật thể thật + H3 hình học của tiền, chọn theo từng nhịp, một bộ token). Hệ hình: `system.md` (màu, chữ, chuyển động, luật vật 3D, ILLUSTRATIVE, nguồn, **bảng chọn H1/H3 cho S01–S20**). Token máy đọc: `tokens.json`. Quyền: `rights.md`.

**Clip để ký:** `episodes/ep001/review-c3/contract.mp4` — 75,5 s, 1280×720, 30 fps, H.264, không tiếng, 5,65 MB; thẻ mở 1,5 s + thẻ tiêu đề 1 s trước mỗi frame (tên nhịp, cảnh, H1/H3).

## Danh sách frame (1920×1080, 30 fps, H.264 High yuv420p BT.709, không tiếng)

| File | Nhịp | Cảnh áp dụng | Hướng | Dài | Ý phải đọc được khi tắt tiếng |
|---|---|---|---|---|---|
| `SF1.mp4` | Cold open: cửa sổ lỡ | S01 (và ngữ pháp cửa sổ cho S05) | **Kết hợp** H3 → H1 → H3 | 12,0 s | Lãi tuần rơi vào vùng "cửa sổ" (chỉ các tuần ≥ 1 điểm dưới 7.62% của Nora) tới đáy 5.98%; ở bàn bếp tấm "$459 a month less" nhấc khỏi khoản trả hằng tháng rồi xám đi, bị gạch, rơi về ("She didn't take it."); cửa sổ đóng sau tuần 23/7/2026, lãi lên lại 7.03%. |
| `SF2.mp4` | Lá thư + câu hứa | S02 (ngữ pháp lá thư cho S06, S07, S18) | **H1** | 11,0 s | Lá thư "Refinance offer", dòng "Loan costs $5,124" sáng lên; ba nhà mô hình (nhỏ, Nora, lớn; thể tích = khoản vay) và nhà chỉ có đường viền "your loan?"; câu hứa trên màn hình. |
| `SF3.mp4` | Hoà vốn 24 → 30 | S09–S10 | **H1** | 12,0 s | Cọc $221 chồng tới ngang xấp phí ở tháng 24; hai chồng "balance paid off since refinancing" (old loan / new loan) cho thấy khoản mới trả gốc chậm hơn; phần chênh (sọc) "$1,133 still owed on the new loan vs the old one" bay lên xấp phí; thêm cọc tới tháng 30 → "Break-even: month 30". |
| `SF4.mp4` | Một phần tư điểm: "never" | S11 (S12, S13 cùng đồ thị) | **H3** | 10,0 s | Phép chia (chỉ tiết kiệm) cắt vạch phí ở tháng 38; đường "savings minus what she still owes" lên gần, không chạm, rồi rơi → "Never", không trước kỳ trả cuối của khoản cũ. |
| `SF5.mp4` | Walt và Anjali | S14–S17 | **H1** (+ thước phẳng ở S16) | 12,0 s | Cùng đề nghị 7.62% → 7.03%; nhà theo tỉ lệ khoản vay; phí gần bằng, cọc tiết kiệm $68 vs $387; sau 3 năm Walt "$1,777 short", Anjali "paid back month 18" rồi "$5,250 ahead"; đáp án "1.12 points" vs "about a third of a point". |
| `SF6.mp4` | Thước ba mốc (G-013) | S18 | **H3** (S18 = kết hợp với lá thư SF2) | 11,0 s | Ba cột rời theo cỡ khoản vay ($115,000 · $375,000 · $655,000): 1.12 points · 0.5 point · about a third of a point; vạch "1-point rule of thumb" trượt qua, không khớp cột nào; nhà nét đứt "your loan?" trượt dọc trục, dừng giữa hai mốc, không số. |

Mỗi frame kèm `SFn-strip.png` (1920×250, 6 khung đánh số + thời điểm), `SFn-poster.png` = **đúng khung cuối** (t = (N−1)/30; so với khung cuối giải mã từ mp4: sai khác trung bình 1,5–2,0/255 = nhiễu nén), `render-log-SFn.json` (thời gian, claim ID dùng, mọi chuỗi trên màn hình kèm cờ ra-ngoài-vùng-an-toàn).

## Số trên màn hình → claim (`out/claims.json`, qua `CL()`)
- SF1: `low2026` `low2026_date` `low2026_since` `r_old` `oct2023` `sav_low2026_median` `seven` `first7_since` `r_today` `anchor_date` `cut1_last_2026` `s10` `y2025`.
- SF2: `cost_median`.
- SF3: `cost_median` `sav_median` `be_simple_median` `gap24` `be_bal_median`.
- SF4: `s025` `cost_median` `be_simple_025` `be_bal_025`.
- SF5: `r_old` `r_today` `loan_small` `loan_large` `cost_small` `cost_large` `sav_small` `sav_large` `be_bal_large` `net36_small` `net36_large` `y3` `cut36_small` `cut36_large_words`.
- SF6: `loan_small` `loan_median` `loan_large` `cut36_small` `cut36_median` `cut36_large_words` `y3` `s10` `oct2023` `y2025`.

`src/check.py` (chạy trên log render): **0 token số ngoài claim**, 0 chuỗi ra khỏi vùng an toàn, chữ nhỏ nhất 48 px ở cả 6 frame (`work/check.txt`, không commit). Không in số nội suy: kim/đường giữa các mốc không có số; thước tháng chỉ đánh số 24, 30 và "3 years"; tháng 25–30 của tấm sọc, chiều cao chồng "balance paid off", đường "never" lấy từ `model/refi.py` (qua `src/build_data.py`, có assert với claim) nhưng không in.

## Tự kiểm 25% (G-014)

Cách làm: khung khó nhất của mỗi clip (khung cuối — nhiều chữ nhất) thu nhỏ **4× trung bình hộp** (1920×1080 → 480×270, như điện thoại ở 25%), mở ảnh và tự đọc lại từng chuỗi. Theo bậc chữ: chữ nhỏ nhất 48 px → chữ hoa 34,9 px ở 1080p = **8,7 px ở 25%**; số chính 96 px → 17,5 px.

| Frame | Kết quả đọc ở 480×270 |
|---|---|
| SF1 (khung cuối, đồ thị) | Đọc được mọi chuỗi: tiêu đề, "latest: week ending September 24, 2026", "Nora 7.62%", "5.98%", "7.03%", "7%", "1 percentage point / below Nora's rate", "window closed", nhãn tháng, hai câu chú thích, dòng nguồn. |
| SF2 (khung cuối, bàn bếp) | Đọc được câu hứa hai dòng, "smaller loan", "Nora", "larger loan", "your loan?", "fees $5,124", dòng nguồn, ILLUSTRATIVE. **Không** đọc được chữ in trên lá thư ("REFINANCE OFFER", thân thư) — chữ trang trí trên vật; số của thư có bản phẳng "fees $5,124". |
| SF3 (khung cuối) | Đọc được "Break-even: month 30", "loan costs / + still owed", "+$221 a month", "loan costs", "old loan", "new loan", "balance paid off / since refinancing", "24" (gạch), "30", "months", dòng nguồn; "LOAN COSTS $5,124" in trên xấp phí cũng đọc được. |
| SF4 (khung cuối) | Đọc được mọi chuỗi, kể cả "point = one percentage point of the rate", "closest: still short", "not before the old / loan's last payment", "months →". |
| SF5 (khung cuối) | Đọc được hai dòng tiêu đề, "1.12 points", "about a third of a point", "$1,777 short / after 3 years", "$5,250 ahead / after 3 years", "loan costs", "+$68/mo", "+$387/mo", hai dòng tên + khoản vay, dòng nguồn; "$3,667"/"$5,514" in trên xấp phí đọc được. "+$68/mo" (xanh trên nền cỏ tối) đọc được nhưng tương phản thấp nhất khung. |
| SF6 (khung cuối) | Đọc được mọi chuỗi. |

Ảnh 25%: `work/SFn-25.png` (và bản phóng 2× `-25-x2.png`), sinh lại bằng `src/check.py`; không commit.

## Thời gian render (CPU, đo thật, `render-log-SFn.json`)

Máy 4 vCPU Intel Xeon, không GPU. H1: three.js 0.186.1 trong Chromium headless 1194, WebGL qua ANGLE → SwiftShader; H3: canvas 2D cùng trang; RGBA → PyAV libx264 (CRF 20, preset slow).

| Frame | Loại | Khung | Giây máy | **Giây máy / giây phim** | Ghi chú |
|---|---|---|---|---|---|
| SF1 | 2D + 3D (3,8 s) | 360 | 205,5 | **17,1** | chạy song song với SF2 |
| SF2 | 3D | 330 | 331,4 | **30,1** | song song với SF1 |
| SF3 | 3D | 360 | 282,4 | **23,5** | chạy một mình |
| SF4 | 2D | 300 | 91,2 | **9,1** | một mình |
| SF5 | 3D | 360 | 278,3 | **23,2** | song song với SF3 (bản trước) |
| SF6 | 2D | 330 | 96,8 | **8,8** | một mình |

→ 1080p: H1 ~23–30 s máy/giây phim (đúng ước của H1 README ×2,25 điểm ảnh), H3 ~9 (ở 1080p phần lớn là chuyển ảnh base64 khỏi trình duyệt và mã hoá, không phải vẽ). Ước cả tập (~9,7 phút; theo bảng chọn ~55% thời lượng là H1): ~3–3,5 giờ một tiến trình; chia đoạn 2 trang song song ~2 giờ (2 trang song song trên 4 vCPU không nhanh gấp đôi: SF2 chậm hơn SF3 chạy một mình). Hợp đồng `contract.mp4`: ghép (giải mã 1080p, thu về 720p, mã hoá) 179 s máy.

## Dựng lại
```
python3 episodes/ep001/data/fetch.py --verify                 # nếu thiếu data/normalized/*.csv (FRED, không commit)
python3 episodes/ep001/design/c3/final/src/build_data.py      # -> src/data.js (không commit)
npm i three@0.186.1                                            # trong một thư mục tạm
cd episodes/ep001/design/c3/final/src
THREE_DIR=<tạm>/node_modules/three/build NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js SF1   # … SF6; --still 3.9,11.95
python3 check.py SF1 SF2 SF3 SF4 SF5 SF6                       # claim, vùng an toàn, cỡ chữ, ảnh 25%
NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node cards.js && python3 contract.py
```
Mã: `src/engine.js` (token, chữ theo bậc, `CL()`, vật liệu, nhà, boot 2D/3D), `src/sf1.js`–`sf6.js` (mỗi frame là hàm tất định theo t), `src/render.js`, `src/encode.py`, `src/check.py`, `src/cards.js`, `src/contract.py`. Dùng lại từ H1 (`common.js`: renderer, nhà, giấy, cọc tiền) và H3 (`scenes.js`: đường lãi tuần, hoa văn, ngữ pháp dải tháng; `build_data.py`).

## Giới hạn
- Chưa có lời/âm; nhịp khung chưa khớp lời Eric (khớp ở C4 animatic).
- Chưa kiểm mù các frame cuối (bài học C3: kiểm tắt tiếng phải che chú thích hoặc hỏi "hiểu nhờ hình hay nhờ chữ" — làm ở C4).
- SF1 chỉ mở cửa sổ từ tháng 8/2025 (mốc cửa sổ mở 14/8/2025 lấy từ dữ liệu, không có claim riêng; không in ngày mở).
- SF3: chồng "balance paid off" cao hơn các vật khác (gốc đã trả > phí) nên thước đô la nhỏ; tấm sọc $1,133 mỏng so với xấp phí — đúng tỉ lệ, cố ý không phóng.
- SF5: nhà thể tích theo khoản vay đọc là "nhà to hơn", không đọc được tỉ lệ 5,7×; cọc $68 rất mỏng (đúng thang).
- SF6: nhà 2D có **diện tích** theo khoản vay (H3), trong khi nhà 3D có **thể tích** theo khoản vay (H1) — ghi rõ ở `system.md`; không so trực tiếp giữa hai frame.
- Hình học 3D đơn giản (hộp, lăng trụ), chưa mức ảnh thực; bóng PCF, không GI.
- Thẻ tiêu đề trong clip hợp đồng bằng tiếng Anh (Inter bản latin không có dấu tiếng Việt); danh sách tiếng Việt ở bảng trên.

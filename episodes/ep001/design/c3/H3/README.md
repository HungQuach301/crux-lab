# H3 — "Hình học của tiền" (C3, Tập 1)

DESIGNER H3, 29/09/2026. Ý đồ từng khung (viết và commit trước khi render, `f7a62d9`): `intent.md`.

## Ý tưởng
2D phẳng, tối giản; **chiều cao/diện tích = đô la, trục ngang = thời gian**, cùng một thang trong một khung. Chỉ có ba loại chuyển động, mỗi loại một ý: **vẽ** (thời gian trôi), **lấp** (tiền dồn lại, mỗi dải = một tháng), **mọc thêm / co lại** (một khoản hiện ra hoặc mất đi). Người xem tắt tiếng đọc ý từ hình dạng: thanh co lại còn bóng rỗng = khoản đã lỡ (F1); khối tưởng đầy mọc thêm phần nợ ẩn = hoà vốn trễ (F2); hai khối phí gần bằng nhau lấp với hai tốc độ = khoản nhỏ cần giảm lãi nhiều hơn (F3).

| Khung | File | Dài | Dải 6 khung | Poster |
|---|---|---|---|---|
| F1 · cửa sổ lỡ | `F1.mp4` | 9 s | `F1-strip.png` | `F1-poster.png` (t = 8.6 s) |
| F2 · hoà vốn 24 → 30 | `F2.mp4` | 10 s | `F2-strip.png` | `F2-poster.png` (t = 9.3 s) |
| F3 · Walt và Anjali | `F3.mp4` | 10 s | `F3-strip.png` | `F3-poster.png` (t = 9.5 s) |

1280×720, 30 fps, H.264 High yuv420p, không tiếng; 0.25–0.4 MB mỗi file.

## Màu và chữ
Chỉ token kênh (`genre-spec/channel/visual-tokens.json`, bí danh ở `episodes/ep001/design/tokens.json`); nền `bg #0E1116` (không đen tuyền).

| Vai | Token | Dùng |
|---|---|---|
| Lãi thị trường | `accent #4C8DFF` | đường PMMS, vùng "window" |
| Tiền tiết kiệm | `positive #3FBF7F` + vạch nối nền giữa các dải | dải tháng, thanh $459, khung "break-even" |
| Hoá đơn / phí | `ink-muted #9AA4B2` viền, `surface #171B22` trong | khối phí; không tô đỏ (đỏ = Anjali) |
| Phần nợ ẩn (F2) | `warn #F2B441` gạch chéo | F2 không có Walt trên màn hình. Ở F3 phần này gạch chéo xám |
| Nhân vật | Nora `positive` ●, Walt `warn` ▲, Anjali `negative` ■ | đúng `tokens.json` (màu + hình) |
| Chữ | `ink #F2F4F7`, phụ `ink-muted` | Inter 400/600/700; số lớn 30–32 px, nhãn 20–24 px, phụ 16 px (≥ 24 px ở 1080p) |

Huy hiệu ILLUSTRATIVE (`warn` nền, chữ `bg`) đặt sát mọi số của nhân vật, hiện cùng lúc với số.

## Lý do
- G-011 / A4: ý nằm trong chuyển động, không trong chữ — tắt tiếng vẫn thấy "lấp", "mọc thêm", "co lại".
- G-012 (c): biểu đồ và số tự đọc được; không ẩn dụ vật thể (bể nước, khối đá bị chê ở bài D): khối ở đây là cột biểu đồ đúng tỉ lệ, không phải vật.
- G-004 (d): mỗi khung có một khoảnh khắc 1 giây (đáy $459 → bóng rỗng; khối hổ phách mọc trên đỉnh; hai điểm trên thước).
- Trung thực: phần nợ ẩn ở F2 lớn dần **từ tháng 1** (bóng mờ), chỉ "đặc lại" ở tháng 24 — đúng mô hình (dư nợ khoản mới − khoản cũ tăng đều), không phải một khoản rơi từ trời xuống ở tháng 24. Thanh F1 ở mọi tuần tính bằng cùng mô hình với `sav_low2026_median` (k = số kỳ đã trả theo quy ước `k35`), `build_data.py` assert lại $459, $221, $1,133, 30/75/18 tháng và tuần July 23, 2026.
- Số trên màn hình chỉ qua `claims.json → display` (hàm `CL()` trong `src/scenes.js`); trục không có số tick ngoài claim (thước tháng F2 chỉ đánh số 24, 30, 36; thước F3 chỉ "no cut" và "1 point").

Claim dùng: F1 `r_old s10 low2026 low2026_date low2026_since sav_low2026_median cut1_last_2026 r_today anchor_date seven first7_since`; F2 `cost_median sav_median be_simple_median gap24 be_bal_median hold36`; F3 `loan_small loan_large cost_small cost_large sav_small sav_large be_bal_large y3 s10 cut36_small cut36_large_words`.

## Thời gian render (đo từ `render-log.json`)
Máy: 4 CPU, không GPU; Chromium headless (Playwright) vẽ canvas 2D từng khung → RGBA → PyAV libx264 (`preset slow`, `crf 16`). Một trang, tuần tự, trong lúc các agent khác cũng render.

| Khung | Khung hình | Wall | **Giây render / giây phim** |
|---|---|---|---|
| F1 | 270 | 39.8 s | **4.4** |
| F2 | 300 | 47.0 s | **4.7** |
| F3 | 300 | 47.5 s | **4.75** |

Ước tính cả tập (~12 phút) theo hướng này: ~55 phút một trang; chia 4 trang song song như `toolkit/render/render.js` → ~15–20 phút. Phần lớn thời gian là chuyển ảnh base64 ra khỏi trình duyệt và mã hoá, không phải vẽ.

## Dựng lại
```
python3 episodes/ep001/data/fetch.py --verify          # nếu thiếu data/normalized/*.csv
python3 episodes/ep001/design/c3/H3/src/build_data.py  # -> src/data.js (không commit: có giá trị FRED, E1-A2)
cd episodes/ep001/design/c3/H3 && NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node src/render.js
```
Không dùng `toolkit/render/` (engine 2.5D có camera/parallax — trái với "phẳng, tối giản" của H3); chỉ dùng lại font Inter ở `toolkit/render/fonts`.

## Giới hạn
- Dải 6 khung 1920×220: chữ 16 px của khung gốc chỉ còn ~4 px — AI kiểm mù đọc được hình dạng (khối, thanh, đường) và số lớn, không đọc được nhãn phụ. Nếu kiểm mù cần đọc nhãn, dùng poster.
- F3: phần dư của Anjali sau tháng 18 chồng cao gấp ~1.6 khối phí (đúng số: $387 × 36 so với $5,514 + dư nợ) và lấn thị giác so với khối Walt; nếu chủ dự án thấy rối, có thể dừng lấp khi đầy và thay bằng nhãn.
- F3 hiển thị `cut36_large_words` nguyên văn "about a third of a point" (không rút thành "about 1/3" như gợi ý, vì phải đúng `display`).
- F1 bắt đầu từ tuần đầu 12/2025 — lúc đó đường đã ở trong cửa sổ (cửa sổ mở từ 14/8/2025 theo `weeks_below_r_old_minus_1`); khung không cho thấy lúc cửa sổ mở.
- Dải tháng mới mọc lên (lấp) chứ không "rơi" từ trên xuống; nhịp đều 0.15 s/tháng ở tháng 1–24, chậm lại 0.37 s/tháng ở 25–30 để nhấn phần trễ.
- Chưa có kiểm mù; chưa có bản đồ (không cần cho ba nhịp, và không có dữ liệu bản đồ đã rõ quyền trong repo).
- Không grain/vignette/grade: hình phẳng có chủ ý; dải tối có thể có banding nhẹ sau nén ở màn hình kém.

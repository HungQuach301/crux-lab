# H3 · Dòng thời gian lịch sử — Tập 2, C3 (DESIGN, 01/10/2026)

**Ý tưởng.** Cả lịch sử T-bill 3 tháng (TB3MS, 1/1954 → 8/2026) là **một dải địa hình** nằm ngang (`accent`). Một **khung 10 năm** trượt dọc dải; mỗi lần dừng thả **một ô** thẳng xuống **dải 753 ô** ngay bên dưới: mỗi năm bắt đầu là một cột 12 ô (tháng 1 ở trên), cột nằm đúng dưới năm đó của địa hình. Nửa trái dải ô (1954–1980) vì vậy luôn nằm dưới **sườn đi lên**, nửa phải (1981 về sau) dưới **sườn đi xuống**; vạch đứt `ink-muted` từ đỉnh 1981 rơi xuống tách hai nửa. Đọc như biểu đồ báo chí; chuyển động (khung bước, ô rơi, ô lật màu, con trượt) là phương pháp. Ý đồ viết trước khi render: `intent.md`.

## Sản phẩm
| File | Nội dung |
|---|---|
| `K1.mp4` … `K7.mp4` | 7 style frame có chuyển động, 1280×720, 30 fps, H.264 High yuv420p BT.709, không tiếng; K1 8 s, K2 9 s, K3–K7 10 s |
| `K*-strip.png` / `K*-strip-masked.png` | 6 khung theo thời gian (lưới 3×2, số 1–6, không chú thích); bản masked: mọi chữ/số thay bằng khối phẳng `surface #171B22` đúng hộp chữ, làm bằng cờ `MASK` trong mã dựng (`engine.js → text()`), không làm mờ sau |
| `thumb-concept.png` + `.json` | concept thumbnail 1280×720; 3 chữ "Fixed or variable?" (100 px ở 1280) + huy hiệu ILLUSTRATIVE 32 px góc trên phải; không số |
| `endscreen.md` | kế hoạch đuôi end screen 18 s |
| `intent.md` | ý đồ từng KEY khi tắt tiếng và che chữ (viết trước khi render) |
| `rights.md` | tài sản và quyền |
| `src/` | `build_data.py` (chạy lại mô hình, assert 753/753 cửa sổ khớp `out/model.json`), `engine.js`, `scenes.js`, `page.html`, `render.js`, `cvd.py`; `src/data.js` sinh ra từ dữ liệu |
| `work/render-log-K*.json` | thời gian render, claim dùng, mọi chuỗi trên màn hình, số đo tự kiểm |

Chạy lại: `python3 episodes/ep002/design/c3/H3/src/build_data.py` rồi trong `src/`: `NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js K1` (… K7; `node render.js THUMB --thumb`).

## Mỗi KEY mang nghĩa thế nào (tắt tiếng, che chữ)
| KEY | Hình | Đọc được khi che chữ? (tự đánh giá) |
|---|---|---|
| K1 | ray ngang `ink-muted` mọc ra; dưới nó đường `ink` của hạt thoi (Leah) bắt đầu thấp hơn và lượn; phía trước là chùm 7 đường mờ thay hình liên tục; khe hạt–ray sáng `positive` | **trung bình**: "một mức đứng yên, một mức thấp hơn nhưng không chắc" rõ; "ai đó đang cân nhắc" chỉ có hạt thoi, không có người |
| K2 | ngoặc bật vào giữa ray và hạt; hạt (kéo cả đường) xuống → ngoặc rộng; lên → hẹp; chạm ray → khép; vượt ray → ngoặc lật, lòng `positive` → `warn`; 4 ngoặc nhỏ góc trái dưới ghi lại các cỡ đã thử | **khá**: thứ thay đổi là khoảng chênh; "đây là thứ được đo" dựa vào ngoặc |
| K5 | đường ngắn phóng ra thành cả địa hình; khung bước từng nấc (3 viền khung trước còn mờ = chồng nhau), nhanh dần; mỗi nấc thả một ô xuống đúng năm/tháng bắt đầu; 753 ô lấp đầy | **mạnh** |
| K3 | khung quét lại; dải hổ phách (một vạch mỗi tháng bắt đầu, sáng khi lần chạy đó từng vượt 9%) sáng gần kín; rồi ô lật màu trái → phải: phần lớn xám, ít đỏ, đỏ dồn nửa trái; hai nửa lần lượt được làm nổi | **mạnh** (diện tích hổ phách ≫ diện tích đỏ; đỏ ở dưới sườn lên) |
| K4 | ba lần chạy phóng to, khung trên địa hình nhỏ cho biết ở đâu: 1/1970 (đệm đầy, cú vượt 9% cuối kỳ chỉ làm lõm rất ít → ô xám), 7/1975 (đệm lên ~$3,089 rồi cạn sạch → ô đỏ), 8/1981 (đi xuống, đệm đầy mãi → ô xám); nêm nợ `grid` cao bên trái | **khá**; cú "lõm" của lần 1 rất nhỏ (thật theo dữ liệu: ~$3 trên $10,9 nghìn) nên đọc là "hổ phách ngắn không làm gì được hũ" |
| K6 | ô xấu nhất khoanh nhấp nháy → khung phóng to 4/1977; hạt leo xa trên ray, ray `warn` gần hết 10 năm; hũ gần như không đầy (thật: đệm tối đa $218); hai chồng xu: chồng thả nổi = chồng cố định + khối đỏ 43% | **khá**; hũ "đầy chút rồi cạn" gần như không thấy vì dữ liệu |
| K7 | con trượt trên thước kéo ngoặc (góc trái dưới) rộng ra → ô đỏ tắt ở cả hai nửa; ở 2 điểm nửa phải xám hoàn toàn; nửa trái giữ lớp đỏ; khối đỏ trên chồng xu co nhưng không mất; quét ngược tới −1: cả hai nửa đỏ lại, khối đỏ cao vọt; ô xấu nhất (khoanh) không đổi chỗ | **mạnh** |

## Màu (chỉ token Tập 1, `episodes/ep001/design/c3/final/tokens.json`)
| Vai | Token | Hex |
|---|---|---|
| nền | `bg` | `#0E1116` |
| khối che chữ (bản masked) | `surface` | `#171B22` |
| ô "không đắt hơn", nêm nợ còn lại, vạch dải đếm khi không vượt | `grid` | `#2A303B` |
| chữ chính; Leah = hạt **hình thoi** + đường của nó; khung 10 năm; ngoặc | `ink` | `#F2F4F7` |
| lãi cố định (ray), chồng xu, chữ phụ cạnh số (D5), vạch tách hai nửa, ô trung tính trước khi lộ kết quả (K5) | `ink-muted` | `#9AA4B2` |
| địa hình T-bill | `accent` | `#4C8DFF` (mặt địa hình: cùng màu, alpha 0,14–0,20) |
| lãi vượt 9% (đoạn ray sáng, dải đếm, lòng ngoặc khi đảo) | `warn` | `#F2B441` |
| đắt hơn tổng cộng (ô đỏ, khối thêm trên chồng xu, số % đắt hơn) | `negative` | `#E5484D` |
| đệm/tiết kiệm (hũ, diện tích dưới ray, lòng ngoặc) | `positive` | `#3FBF7F` (diện tích: alpha 0,35; lòng ngoặc 0,55) |
| huy hiệu | `warn` nền, chữ `bg` | — |

Alpha chỉ dùng trên chính màu token (mặt địa hình, diện tích đệm, ô làm mờ khi làm nổi một nửa ở K3, viền khung cũ ở K5).

**Mô phỏng protan/deutan** (`src/cvd.py`, Machado 2009 mức 1,0, ΔE2000; thang xám = tương phản độ chói):

| cặp | thường | protan | deutan | xám |
|---|---|---|---|---|
| warn / negative | 40.3 | 30.0 | **18.1** | 2.12:1 |
| warn / positive | 38.7 | **11.8** | **18.2** | **1.27:1** |
| positive / negative | 70.8 | 24.4 | **11.5** | 1.67:1 |
| negative / grid | 42.8 | 29.1 | 44.8 | 3.39:1 |
| warn / grid | 66.2 | 62.8 | 69.3 | 7.18:1 |
| accent / warn | 58.0 | 59.5 | 63.7 | 1.73:1 |
| accent / positive | 47.8 | 48.2 | 44.9 | **1.37:1** |
| accent / negative | 44.3 | 45.4 | 53.8 | **1.22:1** |
| ink / ink-muted | 20.6 | 20.2 | 20.9 | 2.29:1 |
| negative / ink-muted | 35.1 | 29.7 | 30.6 | 1.55:1 |
| warn / ink-muted | 34.8 | 35.5 | 36.9 | **1.37:1** |
| positive / ink-muted | 29.6 | 26.3 | 22.0 | **1.08:1** |

Cặp **trượt** (in đậm) là giới hạn của bộ token Tập 1, không sửa được mà không thêm màu (brief cấm). Cách hệ hình bù bằng kênh thứ hai: `warn` chỉ ở **đường ray và dải mảnh** giữa địa hình và dải ô, `negative` chỉ ở **ô** và **khối xu** — khác vật, khác vị trí, không bao giờ cùng một vật; `positive` (hũ, diện tích dưới ray) và ô đỏ chỉ cùng khung ở K4, nơi ô kết quả nằm dưới hũ và chỉ xuất hiện khi hũ đã cạn; ngoặc `positive`/`warn` khác nhau thêm bằng **hướng** (dưới ray / trên ray). Accent so với đỏ/xanh: địa hình là đường + mặt mờ, không phải ô. P cần quyết có chấp nhận hay đổi token.

## Tự kiểm (lessons D2–D5, G-014) — đo từ chính bản dựng
Cách đo (`engine.js → check()`, chạy trên **mỗi khung thứ 3** của mỗi clip, chữ alpha ≥ 0,99): vẽ khung hai lần — đủ và không chữ; khoảng cách từ hộp chữ (hộp tấm nền với huy hiệu) tới mọi điểm ảnh khác nền trong bản không chữ (bán kính tìm 16 px; 16 = "≥ 16"); khoảng cách hộp–hộp giữa các chữ (cặp số + chữ phụ cùng một nhãn, vd. "9%"+" fixed", "76.2%"+"went above…", được tính là một nhãn); tương phản chữ với trung vị độ chói nền dưới hộp chữ (hoặc tấm nền). Đơn vị px ở 1080p.

| Clip | khung đo | chữ nhỏ nhất (px@1080) | cách nét đồ hoạ nhỏ nhất | cách chữ khác nhỏ nhất | tương phản nhỏ nhất | render (s máy / s phim)* |
|---|---|---|---|---|---|---|
| K1 | 80 | 48 | ≥ 16 | 98.1 | 7.50 (ink-muted/bg) | 29.4 s / 8 s = 3.7 |
| K2 | 90 | 48 | 10.6 | 23.1 | 7.50 | 42.6 s / 9 s = 4.7 |
| K3 | 100 | 48 | ≥ 16 | 60.6 | 4.83 (negative/bg, "14.2%") | 49.7 s / 10 s = 5.0 |
| K4 | 100 | 48 | ≥ 16 | 518 | 7.50 | 74.5 s / 10 s = 7.5 |
| K5 | 100 | 48 | ≥ 16 | 91.5 | 7.50 | 72.6 s / 10 s = 7.3 |
| K6 | 100 | 48 | 14.6 | 96.7 | 7.50 | 40.2 s / 10 s = 4.0 |
| K7 | 100 | 48 | 10.0 | 115.8 | 4.83 (negative/bg, "8.8%") | 48.1 s / 10 s = 4.8 |
| thumb | 1 | 48 (32 px ở 1280) | ≥ 16 | 741.6 | 10.25 (bg/warn, huy hiệu) | — |

\*Bao gồm cả mã hoá ffmpeg, dải, và tự kiểm (tự kiểm chạy sau, không tính trong số này); chạy 2 tiến trình song song trên 4 CPU (K4/K5 chạy song song nên chậm hơn). Toàn bộ 7 clip ≈ 6 phút máy.

- D4 (≥ 4 px): đạt, nhỏ nhất **10.0 px** (K7, "8.8%" cách con trượt). D5: chữ phụ cạnh số nhấn ("fixed", "variable", "went above the fixed rate", "cost more in total", nhãn năm, "1.5 points" trên thước) dùng `ink-muted`. D2: không có vật liệu 3D; chữ chỉ đặt trên nền `bg` phẳng (huy hiệu: tấm `warn`). G-014: chữ nhỏ nhất 48 px ở 1080p (= 32 px ở 720p, cao chữ hoa 8,7 px ở 25%). Chữ đỏ `#E5484D` trên nền là trường hợp sát nhất: **4.83:1** (cao hơn ngưỡng 4,5 khoảng 7%, ngoài vùng ±5% của quality-framework §2.2, nêu ra để P biết).
- Mọi chuỗi trên màn hình nằm trong vùng an toàn thiết kế (lề 96 px).
- Chưa đo: chữ đang mờ dần (alpha < 0,99) — chỉ ở 0,3–0,4 s mỗi lần hiện/ẩn.

## Số trên hình → claim ID (`numbers.md`, qua `CL()` → đúng chuỗi `display` của `out/claims.json`)
K1 `fixed_rate` 9%, `var_start` 7.5% · K2 `fixed_rate`, `gap_start` 1.5 points · K3 `share_rate_above_fixed` 76.2%, `share_all` 14.2%, `share_early` 28.4%, `share_late` 3.5% · K4 `fixed_rate` · K5 `first_start` January 1954 (cả "10-year" theo `term`) · K6 `worst_start` April 1977, `worst_peak_rate` 19.3%, `fixed_int` $26,005, `worst_diff` +$11,219 · K7 `gap_start`, `spread2_share` 8.8%, `spread3_share` 4.5%. Nhãn năm trục: "1954" (`first_start`), "1981" (`best_start_year`), "today". Không in số nội suy: thước K7 không đánh số vạch; hũ, chồng xu, ô không có số. Huy hiệu ILLUSTRATIVE trên mọi khung có khoản vay của Leah (cả 7 clip). Hình dạng dữ liệu (địa hình, đường của hạt, màu từng ô ở mọi head start −1…3 bước 0,05, đệm từng tháng, chiều cao xu) tính lại trong `build_data.py` và assert khớp `out/model.json` (753/753) và các claim `share_*`, `gap10/20/30_*`, `gap_worst_start_all`.

## Giới hạn
- K1 không có "người": Leah chỉ là hạt thoi + huy hiệu; ý "ai đó đang cân nhắc" phụ thuộc lời/tiêu đề.
- K4/K6: dữ liệu thật làm vài hình yếu đi (cú lõm của lần 1/1970 ~ vài px; hũ 4/1977 chỉ đầy ~6 px) — tôi không phóng đại.
- Ô 1 tháng = 1 hàng của cột năm: dải ô không trùng tuyệt đối vị trí tháng trên địa hình (lệch tối đa 11 tháng trong một cột).
- Đường của hạt trong khung là đường lãi Leah quy về đơn vị chỉ số (có sàn 0 của mô hình), nên trùng địa hình trừ khi sàn chạm (8/1981).
- Cặp màu trượt CVD ở trên (giới hạn token).
- K4 dùng 3 cửa sổ chọn bằng luật ghi trong `build_data.py` (không chọn tay): 1/1970, 7/1975, 8/1981.

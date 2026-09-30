# H2 — "Hồ sơ và bằng chứng" · ba khung phong cách có chuyển động

DESIGNER H2, 29/09/2026. Ý đồ từng khung (viết và commit trước khi render): `intent.md`. Quyền: `rights.md`; phương án quyền cho "bằng chứng": `rights-options.md`.

## Ý tưởng
Cả tập diễn ra trên **một mặt bàn giấy tờ** nhìn từ trên, hơi nghiêng (2.5D): bản in lãi tuần, hồ sơ vay, Closing Disclosure, sổ ghi, giấy kẻ ô. Camera trượt, dừng, đẩy vào; giấy ngoài tiêu điểm mờ theo độ sâu. **Bút đánh dấu đúng con số lời đang nói, rồi con số nhấc khỏi giấy thành một biểu đồ đơn giản** trên tờ bên cạnh. Nghĩa nằm ở động tác: khoanh (đây là mốc), tô (đây là khoảng), gạch (đã mất), chen vào (đẩy tổng đi).

Vì sao: G-012b (bằng chứng làm tăng tin cậy) + G-012a (vật thể thật, không ẩn dụ trừu tượng) + G-011 (hình tự nói khi tắt tiếng). Giấy tờ vay là đồ vật người xem đích (đang trả khoản vay ký 2022–2024, G-013) đã cầm trong tay — "người như tôi" nhìn thấy chính lá thư/biểu mẫu của mình.

| Khung | File | Dài | Dải 6 khung | Poster |
|---|---|---|---|---|
| F1 · Cửa sổ lỡ | `F1.mp4` | 9.0 s | `F1-strip.png` | `F1-poster.png` |
| F2 · Hoà vốn 24 → 30 | `F2.mp4` | 10.0 s | `F2-strip.png` | `F2-poster.png` |
| F3 · Walt và Anjali | `F3.mp4` | 9.5 s | `F3-strip.png` | `F3-poster.png` |

1280×720, 30 fps CFR, H.264 High, yuv420p, BT.709, không tiếng, CRF 26 (7.0 / 11.9 / 10.7 MB). Dải: 1920×220, 6 ô 320×180 đánh số 1–6 kèm giây.

## Bảng màu và chữ (chỉ token kênh)
| Vai | Token | Hex |
|---|---|---|
| Mặt bàn | `bg` / `surface` (vân gỗ tối bằng gradient) | #0E1116 / #171B22 |
| Giấy | `ink` | #F2F4F7 |
| Chữ in trên giấy / chữ phụ | `bg` / `grid` | #0E1116 / #2A303B |
| Đường lãi, bút khoanh | `accent` | #4C8DFF |
| Nora (tròn), dạ quang tiết kiệm | `positive` | #3FBF7F |
| Walt (tam giác), dấu ILLUSTRATIVE | `warn` | #F2B441 |
| Anjali (vuông); bút đỏ "gạch/ẩn" (chỉ ở F1–F2, khi không có Anjali) | `negative` | #E5484D |
| Bìa hồ sơ | `ink-muted` | #9AA4B2 |

Chữ: Inter 400/600/700, số tabular. Số chính 70–100 px thế giới (≈ 32–60 px trên màn hình); chữ phụ ≥ 22 px màn hình ở phần lớn khung. Dạ quang = khối màu `mix-blend-mode: multiply`, độ mờ 0.55.

## Số trên màn hình (claim ID)
F1: `term30` 30, `seven` 7, `low2026` 5.98%, `low2026_date` February 26, 2026, `low2026_since` September 2022, `oct2023`, `r_old` 7.62%, `sav_low2026_median` $459 (ILL.), `r_today` 7.03%, `anchor_date` September 24, 2026, `first7_since` January 2025.
F2: `cost_median` $5,124, `sav_median` $221 (ILL.), `gap24` $1,133 (ILL.), `be_simple_median` 24, `be_bal_median` 30, `y2025`.
F3: `loan_small` $115,000, `cost_small` $3,667, `sav_small` $68, `cut36_small` 1.12, `loan_large` $655,000, `cost_large` $5,514, `sav_large` $387, `cut36_large` 0.32 + `cut36_large_words`, `hold36` 36, `s10` 1, `oct2023`.

Không số nào khác đọc được: các dòng tuần khác trong bảng in ở F1 bị làm mờ 7 px (cố ý — "ngoài tiêu điểm"); các khoản A/B/C của Closing Disclosure là vạch xám, không có số; trục không có số chia.

## Thời gian render (4 CPU, không GPU)
| Khung | Giây phim | Chụp khung | Mã hoá | Tổng | **Giây máy / giây phim** |
|---|---|---|---|---|---|
| F1 | 9.0 | 54.6 s | 17.2 s | 74.3 s | **8.3** |
| F2 | 10.0 | 70.0 s | 22.0 s | 94.6 s | **9.5** |
| F3 | 9.5 | 73.9 s | 19.6 s | 96.5 s | **10.2** |

Số đo thật ở `src/timing-F*.json`. Một luồng Chromium; chia 4 luồng như `toolkit/render/render.js` sẽ còn ~3 s/giây phim → tập ~10 phút ≈ 30–60 phút CPU.

## Cách render lại
```
python3 episodes/ep001/data/fetch.py --verify        # dữ liệu FRED (không trong repo)
cd episodes/ep001/design/c3/H2/src
NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js F1   # F2, F3
```
`stage.html` + `common.js` (camera 2.5D, dạ quang, bút, dấu) + `f1.js`/`f2.js`/`f3.js` (mỗi khung một hàm `build`, một hàm `update(t)`). `encode.py` mã hoá bằng PyAV (máy không có ffmpeg).

## Giới hạn và điều cần biết
- **F2 — quy ước dựng:** phần dư nợ (sọc đỏ) tăng tuyến tính từ 0 tới $1,133 ở tháng 24 (`gap24`), rồi tới đúng mức để 30 × $221 chạm vạch ở tháng 30 (`be_bal_median`). Hình dạng giữa các mốc là nội suy, không phải claim; hai mốc là claim. Cột = tổng tiết kiệm tới tháng đó, cao đúng tỉ lệ, đáy 0.
- **F3:** mỗi cặp cột một thang riêng (ghi trên giấy "each pair on its own scale"); so sánh là **trong cặp**, không giữa các cặp.
- **Closing Disclosure là bản dựng lại** theo bố cục mẫu CFPB (chỉ mục Loan Costs), không phải ảnh của biểu mẫu; không logo CFPB.
- Không có screenshot bài báo và không có "bài báo giả MOCKUP" trong ba khung (chỉ loại 1 và 2; xem `rights-options.md`).
- Chữ nhỏ (chú thích nguồn, "nominal $") xuống ~14–16 px trên màn hình khi camera lùi xa (F3 cuối, F1 cuối) — đọc được trên màn lớn, khó trên điện thoại. Bản cuối nên phóng to chú thích hoặc đưa ra lớp chữ phẳng.
- Phối cảnh là CSS 3D (một mặt phẳng nghiêng + giấy nâng lên); không có ánh sáng thật hay nếp giấy. Muốn "vật thể thật" hơn (G-012a) cần texture giấy hoặc render 3D — tốn CPU hơn.
- Chưa kiểm mù. Câu hỏi đề xuất: tắt tiếng, xem một lần, "What happened, in one sentence?" — tiêu chí đạt ghi ở `intent.md`.

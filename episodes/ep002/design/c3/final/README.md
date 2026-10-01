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

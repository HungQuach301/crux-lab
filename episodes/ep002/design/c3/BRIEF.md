# C3 Tập 2 — Brief chung cho 3 hướng hình (P-ep002, 01/10/2026)

Đọc trước: `playbook/lessons.md` (A4, **D1–D5**), `playbook/quality-framework.md` §2, §5, `taste-ledger.md` (G-004, G-011, G-012, G-013, **G-014**: sàn chữ 40 px ở 1080p, đọc được ở 25%), `playbook/references.md` (chỉ mô tả; không tải, không chép), `playbook/packaging.md` §5 (C3: concept thumbnail + đuôi end screen), `episodes/ep002/story/script.md` (v4), `episodes/ep002/story/beats.md` (**7 nhịp then chốt KEY-1…7**, cột "idea a muted, text-masked viewer must read"), `episodes/ep002/numbers.md`.
**Hệ nhận diện giữ từ Tập 1 (chủ dự án Q1=A):** token và phông `episodes/ep001/design/c3/final/tokens.json` + `system.md` (Inter, bậc chữ, `bg #0E1116`, `ink`, `ink-muted`, `accent`, `warn`, `positive`, `negative`, badge ILLUSTRATIVE). Không thêm màu UI ngoài token. Được dùng lại **mã** engine (`episodes/ep001/design/c3/final/src/`, `episodes/ep001/animatic/src/engine.js`); **không** dùng lại cảnh, vật thể, câu chữ hay bố cục của Tập 1.

## Ba hướng (mỗi agent một hướng)
| Hướng | Ý | Gợi ý vật/hình |
|---|---|---|
| **H1 · Vật thể thật** (3D, three.js trên CPU như Tập 1 H1; G-012a) | Khoản vay là đồ vật trên một bàn: hai lời mời, một thanh ray cố định và một hạt trượt trên đường ray gợn (thả nổi), tiền lãi là chồng xu, phần đệm là hũ xanh, hai thùng kết quả dưới hai nửa lịch sử | chữ đặt trên vật liệu 3D **luôn có tấm nền token `bg`** (D2) |
| **H2 · Hình học của lãi** (2D) | Mọi ý là diện tích và đường: lãi thả nổi là một đường quanh vạch 9%; phần dưới vạch tích thành diện tích "đệm", phần trên vạch rút dần diện tích đó; kết quả là dấu ± của diện tích còn lại | gần tinh thần "hình mang nghĩa"; không chép thiết kế tham chiếu |
| **H3 · Dòng thời gian lịch sử** (2D, dữ liệu) | Cả lịch sử T-bill 1954–2026 là một dải địa hình; một khung 10 năm trượt dọc; mỗi lần dừng thả một ô kết quả xuống dải 753 ô xếp theo năm bắt đầu; nửa trái/nửa phải đọc được bằng vị trí | đọc được như một biểu đồ báo chí nhưng chuyển động là phương pháp |

Vai màu (cả ba hướng, chỉ dùng token): **"lãi vượt 9%" = `warn`**; **"đắt hơn tổng cộng" = `negative`** (không bao giờ chung một vật với `warn`); **đệm/tiết kiệm = `positive`**; T-bill = `accent`; lãi cố định = `ink-muted` hoặc `ink`. Leah (minh hoạ): một màu token + **một hình dạng** riêng (kênh thứ hai). Ghi hex mọi màu dùng trong `README.md` để P kiểm mô phỏng **protan/deutan** (ΔE2000 ≥ 20 giữa mọi cặp vai phải phân biệt; thang xám ≥ 1,5:1) — D3.

## Việc của mỗi hướng (thư mục `episodes/ep002/design/c3/<H1|H2|H3>/`)
1. **`intent.md` viết TRƯỚC khi render** (P commit trước khi kiểm mù): với mỗi KEY-1…7: câu ý đồ (chép nguyên cột "idea…" của `beats.md`) + chuyển động nào mang ý đó **khi tắt tiếng và che hết chữ/số**.
2. **Style frame có chuyển động cho 7 nhịp then chốt:** `K1.mp4…K7.mp4`, mỗi clip 6–10 s, 1280×720, 30 fps, **không tiếng**, H.264 (ffmpeg có trên máy; nếu mất: `apt-get install -y ffmpeg`). Số trên hình đúng `numbers.md` (ghi claim ID trong README); số của Leah/khoản vay có huy hiệu ILLUSTRATIVE.
3. **Hai dải kiểm mù mỗi nhịp:** `K*-strip.png` (6 khung theo thời gian, lưới 3×2, đánh số 1–6, không chú thích) và **`K*-strip-masked.png`**: cùng 6 khung nhưng **mọi chữ và số bị che** bằng khối phẳng token `surface` (`#171B22`) đúng hộp chữ — làm bằng cờ trong mã dựng (lớp chữ thay bằng khối), không làm mờ sau.
4. **Concept thumbnail** `thumb-concept.png` 1280×720 dựng từ chính hệ hình (vật/hình "anh hùng" đọc được ở 10%), **chừa vùng huy hiệu ILLUSTRATIVE** (cỡ `type.badge` theo tỉ lệ: 32 px ở 1280), ≤ 4 chữ; kèm `thumb-concept.json` `{texts:[{text, box:[x,y,w,h], fontPx}]}`. Không số kết quả nếu không có claim.
5. **`endscreen.md`**: kế hoạch đuôi end screen 15–20 s (vị trí 2 ô video/1 nút đăng ký của YouTube trên hệ hình, hình nền gì, chuyển từ cảnh cuối thế nào).
6. **Tự kiểm khi dựng (lessons D2–D5), ghi số đo vào `README.md`:** khoảng cách nhỏ nhất từ hộp chữ tới mọi nét đồ hoạ và chữ khác (≥ 4 px, D4); tương phản nhỏ nhất chữ/nền cục bộ (≥ 4,5:1; chữ trên vật liệu 3D đo trên tấm nền, D2); chữ phụ cạnh số nhấn dùng `ink-muted` (D5); cỡ chữ nhỏ nhất (≥ 40 px quy về 1080p, G-014).
7. `README.md` (ý tưởng hướng, cách mỗi KEY mang nghĩa, màu hex, thời gian render mỗi giây phim, giới hạn), `rights.md` (mọi tài sản; Inter OFL đã có ở `toolkit/render/fonts`; không tài sản bên thứ ba dạng `data:`; không logo/thương hiệu).

## Kỹ thuật và ranh giới
- Chỉ CPU (không GPU). Chromium headless: `NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`. Tối đa 2 tiến trình render song song mỗi hướng (máy chung với 2 hướng khác).
- **Không commit, không push** (P commit cả ba hướng). Không sửa file ngoài thư mục hướng của mình. Không sửa `checks/`.
- Gu không tự quyết thay chủ dự án: hướng nào tốt hơn là việc của chủ dự án; mỗi hướng làm hết sức theo ý của mình.
- Tin nhắn cuối ≤ 12 dòng: KEY nào mạnh/yếu khi che chữ (tự đánh giá), thời gian render, số đo tự kiểm, giới hạn.

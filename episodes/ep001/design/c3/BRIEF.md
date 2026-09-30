# C3 — Brief chung cho 3 hướng hình (P2, 29/09/2026)

Đọc trước: `playbook/lessons.md` (A4: hình tĩnh không mang nghĩa), `playbook/quality-framework.md`, `taste-ledger.md` (G-004, G-011, **G-012**, G-013), `playbook/references.md` (chỉ đọc mô tả; **không** tải hay chép tham chiếu), `episodes/ep001/story/script-v3.md`, `design/tokens.json`, `genre-spec/channel/visual-tokens.json`.

## Việc của mỗi hướng
Ba **khung phong cách có chuyển động** (motion style frame) cho **cùng ba nhịp**:

| Nhịp | Lời (tóm) | Ý phải đọc được KHI TẮT TIẾNG |
|---|---|---|
| **F1 · Cold open: cửa sổ lỡ** | Lãi xuống 5.98% (tuần 26/2/2026, thấp nhất từ 9/2022); Nora (7.62%, ILLUSTRATIVE) lẽ ra bớt $459/tháng; cô không làm; lãi quay lại trên 7% (lần đầu từ 1/2025). | Có một khoảng lãi thấp; một người đã có thể tiết kiệm một khoản mỗi tháng; khoảng đó đã qua. |
| **F2 · Điểm hoà vốn dời từ 24 → 30 tháng** | Phí $5,124; bớt $221/tháng → phép chia nói 24 tháng; nhưng khoản mới trả gốc chậm hơn: ở tháng 24 cô nợ nhiều hơn $1,133 → tính cả phần đó, hoà vốn ở tháng 30. | Tiền tiết kiệm cộng dồn "lấp" hoá đơn; một phần bị ẩn (dư nợ cao hơn) làm điểm lấp đầy trễ từ 24 sang 30. |
| **F3 · Walt và Anjali** | Walt: vay $115,000, phí $3,667, bớt $68/tháng → cần giảm 1.12 điểm. Anjali: vay $655,000, phí $5,514, bớt $387/tháng → cần ~1/3 điểm. | Phí gần như bằng nhau dù khoản vay chênh ~6 lần; tiết kiệm thì chênh theo khoản vay → khoản nhỏ cần giảm lãi nhiều hơn. |

Mọi số trên màn hình lấy đúng `numbers.md`/`out/claims.json` (ghi claim ID trong ghi chú); số nhân vật có nhãn ILLUSTRATIVE; mọi tiền là danh nghĩa.

## Kỹ thuật
- Mỗi khung: clip **6–10 s**, 1280×720, 30 fps, **không tiếng**, MP4 (H.264). Máy **không có ffmpeg**: dùng Chromium headless (Playwright, `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`) chụp khung + PyAV (`import av`) mã hoá; hoặc Python (numpy/PIL/cairo nếu có) + PyAV. **Chỉ CPU** (không GPU). Có thể dùng lại `toolkit/render/`.
- Kèm cho mỗi khung: **dải 6 khung** theo thời gian (PNG 1920×~220, đánh số 1–6) để kiểm mù AI (AI không xem được video); và 1 poster PNG.
- Thư mục của bạn: `episodes/ep001/design/c3/<H>/` — `F1.mp4 F2.mp4 F3.mp4`, `F1-strip.png…`, `README.md` (ý tưởng hướng, bảng màu/chữ, lý do, thời gian render mỗi giây phim, giới hạn), `intent.md` (ý đồ từng khung: người xem tắt tiếng phải hiểu gì — **viết và commit TRƯỚC khi render**), `rights.md` (mọi tài sản: nguồn, giấy phép trích nguyên câu, phạm vi; font Inter đã có ở `toolkit/render/fonts`).
- Không sao chép thiết kế của Vox/3Blue1Brown/WSJ. Không dùng ảnh/đồ hoạ bên thứ ba khi chưa rõ quyền.
- Commit chỉ file trong thư mục của bạn (`git commit -- <paths>`), không push, message kết thúc bằng:
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` và `Claude-Session: https://claude.ai/code/session_016EPtam7ttrjQMg4sTyN4PK`. Video > 20 MB mỗi file: giảm bitrate.

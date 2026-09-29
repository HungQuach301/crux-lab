# Cổng C3 — Ký hợp đồng hình ảnh (qua clip)

**Xem (1:16, điện thoại):** https://github.com/HungQuach301/crux-lab/raw/ep001-v2/episodes/ep001/review-c3/contract.mp4 — 6 style frame cuối có chuyển động, 1080p gốc (clip ký 720p), không tiếng: SF1 cửa sổ lỡ (H3→H1→H3) · SF2 lá thư + câu hứa (H1) · SF3 hoà vốn 24→30 (H1) · SF4 một phần tư điểm "never" (H3) · SF5 Walt và Anjali (H1) · SF6 thước ba mốc để tự đối chiếu (H3).
**Nghe câu hứa bằng giọng B (23 s):** https://github.com/HungQuach301/crux-lab/raw/ep001-v2/episodes/ep001/review-c3/promise-S02.m4a

**Đã sửa theo kiểm mù C3:** vùng "cửa sổ" chỉ tô tuần lãi ≤ 6.62% (khớp claim 29 tuần); SF3 thêm hai chồng "dư nợ đã trả" khoản cũ/khoản mới để thấy vì sao còn nợ thêm $1,133; bỏ "∝", "Crux model", "nominal $" (→ "Dollars of the day"); ghi "point = one percentage point of the rate"; 0 chữ ra khỏi vùng an toàn; SF5 ghi "Same offer for both: 7.62% → 7.03%".
**Một hệ thống chung** (`design/c3/final/system.md`, `tokens.json`): một bộ màu và phông cho H1/H3; bảng chọn theo cảnh S01–S20: H1 8 · H3 6 · kết hợp 6.
**Kiểm độc lập số liệu:** `final/src/check.py` — 0 số trên màn hình ngoài `claims.json`; không in số nội suy.
**Đọc được ở 25% (G-014):** chữ nhỏ nhất 48 px (chữ hoa 35 px ở 1080p); tự kiểm 6/6 khung cuối đọc được ở 480×270; chữ in trang trí trên lá thư/bìa hồ sơ không đọc được (số của chúng đã có bản chữ phẳng); yếu nhất: "+$68/mo" ở SF5.
**Render CPU:** H1 23–30 · H3 ~9 giây máy/giây phim → cả tập ~3–3,5 giờ một tiến trình (~2 giờ nếu 2 trang song song).

## Câu hỏi
1. **Ký hợp đồng hình ảnh theo clip này?** OK / sửa (ghi 1 câu). — *Khuyến nghị: OK.*
2. **Câu hứa:** nhận dạng giọng (ASR) nghe "a loan your size" thành "**alone** your size" (hai chữ dính âm với giọng B). Nghe file 23 s rồi chọn: **giữ** nguyên văn / **đổi** thành "…— and where would your own loan fall?". — *Khuyến nghị: nghe rồi quyết; nếu tai anh/chị cũng nghe dính, chọn đổi.*

(Không cần trả lời: P2 sẽ cho WRITER đổi câu "far from alone" — ASR nghe "far from a loan" — thành "She wasn't the only one", và C4 nới khoảng nghỉ quanh vài câu đọc nhanh, không giãn giọng.)

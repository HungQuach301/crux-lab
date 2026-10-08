# C3 · N1 "hàng 10 thùng" — bốn đoạn thế giới 3D (Tập 6)

**Ký hiệu mới N1** (`../obj6.js`, `Crates`): 10 thùng low-poly màu kênh (ink = sáng, ink-muted sẫm = tối, nẹp grid; không chữ, không dáng thực phẩm/tiền) = những gì khoản trả ĐẦU TIÊN của nhân vật mua được. `value` = sức mua hiện tại / khoản đầu; thùng i sáng `clamp(10·value − i, 0, 1)` — mờ liên tục, không làm tròn (0,904 → 9 sáng + thùng 10 sáng 4 %; REVIEW-C2v3 PHỤ-4), trần 10 (Edna 105,7 %/100,2 % = 10; PHỤ-5).
**Vì sao mới:** W2 `Stack` nghĩa là đô la (chiều cao = USD); ở đây đại lượng là sức mua so với chính khoản đầu và tập không được nêu số tiền (giá niên kim không mô hình hoá) → chồng tiền sẽ gợi "khoản nào trả nhiều hơn" (beats.md, New symbols).
**Thiết kế đoạn** (lời thật từ `voice-takes/` qua `../wlib.py`; mốc giờ chỉ từ `spine.json`; ≥ 5 s đầu ở thế giới; mọi số/nhãn so sánh chỉ ở đồ thị chính diện; mỗi động tác máy có lý do + âm; mỗi lần hàng đổi trạng thái = một nốt dữ liệu, cao độ = sức mua):
- `s07-ruth` (B07): Ruth + 10 sáng → "less" mờ tới 0,904 → đồ thị: ngoặc 10 chỗ "first check: 10 crates", "today: about 9 in 10 crates (90.4%)".
- `s24-carl` (B24): Ruth → lia sang Carl, hàng mọc → đồ thị: 1966, 6.38 %; "every" = bộ đếm kỷ niệm 1 → 20, hàng mờ mỗi năm (không sáng lại) tới 4,31; "20 of 20"; ô nhỏ đường Ruth so với vạch khoản đầu.
- `s27-edna` (B27): Edna, "kept up" → bộ đếm 1 → 20 (trần 10) → lùi máy: thanh 1949–1969 và 1966–1986 trên một trục, 3 năm chồng tô; "end" hàng Edna năm 18–20 vẫn 10 sáng, "start" hàng Carl năm 1–3 mờ đi (giữ 2,6 s cuối để khung 6 của dải thấy).
- `s29-three` (B29): ba người, ba hàng mờ theo tên → đồ thị: "crates at year 20 · same 2% raise", 10 · about 9 · about 4, tháng bắt đầu sáng ở "month".
Dữ liệu: `../derive.py` → `../claims.json` (claim hiển thị + đường sức mua năm 0–20, tự kiểm với `out/model.json`). Chung: `../c3kit.py` (spine), `../c3kit.js` (cột người + hàng, nhãn, lớp bắt buộc). Cổng gốc: `spans.json` (6 khung đều mỗi clip, muted read chép nguyên văn beats.md).

Lệnh (từ gốc repo; cần `npm ci` trong `toolkit/factory/world/vendor` một lần):
```
python3 toolkit/tests/comment_guard.py episodes/ep006/world && for s in s07-ruth s24-carl s27-edna s29-three; do python3 episodes/ep006/world/c3/$s/spine.py; done
for s in s07-ruth s24-carl s27-edna s29-three; do python3 toolkit/factory/world/build_seg.py episodes/ep006/world/c3/$s --res 540 --out episodes/ep006/world/c3/out/$s.mp4; done
```

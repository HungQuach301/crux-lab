# C2 — kết quả kiểm mù lời

Ý đồ: `gates/C2-intent.md` (ghi trước). Mẫu `c2/sample.txt` (kịch bản sau REVIEWER + S03.3 sửa). Dữ liệu `c2/r1/`.

## Vòng 1 (headless 5 T + 1 G; + 3 `Explore` T chỉ để so)
| Nhóm | Đúng | Câu khuyên | Cảnh mất chú ý (gán máy, khớp 5 từ) |
|---|---|---|---|
| **Headless (cổng)** | **6/6** | **0/6** | **S19 4/6** (giới hạn "Not modeled here…" 3 + thẻ phương pháp 1) · S08 1 · S17 1 |
| `Explore` (so) | 3/3 | 0/3 | S10 3/3 (đoạn phương pháp phát lại) |

**Kết luận vòng 1: TRƯỢT** theo điều kiện "không cảnh nào ≥ 4/6 cùng là chỗ mất chú ý" (S19 = 4/6, đúng bằng ngưỡng → nêu tên). Đúng 6/6 và khuyên 0/6 đạt.
**Dự phòng ghi trước:** S19 rút còn 1 câu lời + thẻ V7 + mô tả. Cùng lượt WRITER mới, sửa các câu gây khó hiểu không đổi nghĩa (câu 3 của 8/9 người đọc): "the schedule's road from the opening", "the road behind the words on paper…", "In a wider set of months…" (tập nào?), "a pair of lines to sit against". Vòng 2: 6 người đọc headless mới + người chấm.

## So headless ↔ `Explore` (`episode.md` §2, ý đồ (c))
- Kết luận đúng/khuyên: **trùng** (cả hai nhóm đúng hết, 0 khuyên).
- Cảnh mất chú ý nhiều nhất: **không trùng** — headless S19 (4/6), `Explore` S10 (3/3). Ba người đọc `Explore` nhận cùng một đầu bài và trả lời gần như từng chữ (tương quan rất cao, lessons H3), nên 3/3 ≈ một ý kiến; headless phân tán hơn.
- Chỗ khó hiểu (câu 3): trùng ("road from the opening" ở 8/9).
- Token: headless 53.369 / 6 = **8,9 nghìn/lượt**; `Explore` ≈ **36 nghìn/lượt** (harness: 35,9–36,1). Người chấm (9 nhãn): 24.744.
- **Theo luật ghi trước: chưa đủ điều kiện "chuyển hẳn"** (cảnh mất chú ý không trùng). Khuyến nghị nêu ở G1: giữ headless cho Tập 5 (rẻ 4×, cùng kết luận cổng, cùng chỗ khó hiểu); điều kiện "cùng cảnh mất chú ý" là câu hỏi mở cho tổng kết Tập 5.

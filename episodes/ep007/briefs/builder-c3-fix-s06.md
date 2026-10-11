# Đầu bài SỬA C3 vòng 2 — đoạn `s06-stack` (Tập 7; headless khoá Console)

Repo `/home/user/crux-lab`. Chỉ sửa trong `episodes/ep007/world/` (không sửa `toolkit/`, `story/`, `numbers.md`; không git commit). Đọc trước: `episodes/ep007/world/c3/README.md`, `episodes/ep007/world/c3/s06-stack/{spine.py,scene.js}`, `episodes/ep007/world/{obj7.js,c3kit.js,c3kit.py,claims.json}`, `episodes/ep007/gates/C3-root-intent.md`, ảnh `episodes/ep007/review-c3/strips-r1/N1-s06-stack.png`.

**Kết quả cổng gốc vòng 1 (tắt tiếng, 2 người đọc): nghĩa 0,5 + 0,5 → TRƯỢT.** Muted read (B06): *"The 30-year bar is raised to finish in 15 years and ends just above the 15-year bar; the sliver above becomes bills that drop onto the stack, month after month, until it stands at its full height."* Người đọc:
- không thấy thanh 30 năm được **nâng lên** để xong trong 15 năm (một người tưởng thanh 30 năm vẫn ngắn hơn);
- đọc chồng tiền là **tiền tiết kiệm / đầu tư phần chênh** ("$120 she could invest… builds a pile of money") thay vì **phần trả THÊM (cái giá)**. Câu trích: *"A viewer might also read the result as a reason to invest the spare cash instead of paying extra on the mortgage."*

**Sửa bằng hình trước (D-009), nhãn là cách cuối; khoá nghĩa (không bỏ gì đang đúng):**
1. Trạng thái trước khi nâng phải đọc được ở chế độ đồ thị: thanh 15 năm có nhãn số khoản trả (claim `pay15_now`, "$2,828 a month"), thanh 30 năm có nhãn khoản bắt buộc (`pay30_now`, "required: $2,216 a month"), rõ ràng **ngắn hơn**; rồi thanh 30 năm **dâng lên** (chuyển động thấy được, có âm) tới $2,948, vượt mức 15 năm một lát mỏng; nhãn đổi thành "30-year paid in 15: $2,948 a month". Một vạch ngang mức 15 năm (`ink-muted`, đứng yên) kéo qua cả hai thanh để thấy lát dôi ra **trên** mức đó.
2. Lát dôi (+$120) phải **tách ra khỏi đỉnh thanh 30 năm và bay sang chồng** ở mỗi nhịp rơi (nhìn thấy nguồn gốc: tiền ĐÃ TRẢ cho khoản vay, không phải tiền để dành). Cân nhắc đặt chồng giữa thanh và nhà, hoặc vệt đường bay; mỗi lần rơi một nốt dữ liệu như hiện tại.
3. Nhãn chồng: "the stack: $21,622 extra paid over 15 years" (claim `extra_vs15_total_now` — định nghĩa là phần trả thêm qua 15 năm; hiển thị đúng `display`). Không thêm chữ khuyên, không chữ "save/invest".
4. Giữ mọi luật cũ (spine 2/3/7, sàn chữ, lớp bắt buộc, ≥ 5 s đầu ở thế giới, nhịp kết giữ ≥ 1 s). Không cần giọng mới (take S06 giữ nguyên).

**Ra:** dựng lại `python3 toolkit/factory/world/build_seg.py episodes/ep007/world/c3/s06-stack --res 540 --out episodes/ep007/world/c3/out/s06-stack.mp4`, rồi `python3 episodes/ep007/world/c3/review.py --strips-dir episodes/ep007/review-c3/strips-r2` (clip duyệt + dải mới). Tự xem dải s06 mới (Read ảnh) — chữ đè, cắt mép, số khớp claim. Ghi thay đổi vào `world/c3/README.md` (mục "Vòng 2"). Trả lời ≤ 20 dòng tiếng Việt.

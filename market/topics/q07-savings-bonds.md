# Hồ sơ cầu — Savings Bonds That Double in 20 Years vs T-Bills

Đề tài: dòng #7 trong `topics/queue.md` · id `q07-savings-bonds` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **thấp** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | thấp | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 12–19 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (SUY TỪ ĐỀ TÀI — chưa có bình luận đã lọc cho đề tài này; trọng số là ước của máy, làm mới ở Việc 0)
1. Do EE bonds really double in 20 years, and what rate do they actually earn? — trọng số cao
2. How do I I bonds' inflation-adjusted rate compare with T-bills right now? — trọng số cao
3. What are the lockup period and early-redemption penalty for I bonds and EE bonds? — trọng số vừa
4. Are savings bonds or T-bills safer, and can either lose money? — trọng số vừa
5. How do state and federal taxes differ across savings bonds and T-bills, and when is tax owed? — trọng số thấp

_Ghi chú máy: No audience comments were provided, so these questions, situations, weaknesses, and requests are inferred conservatively from the topic and the video titles. Rates and inflation adjustments change every six months and were not verified for the current date._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A conservative saver with an emergency fund who wants a government-backed place to park cash for 1 to 5 years.
- A parent opening a long-term account for a child's education who is weighing bonds against a 529 plan or a high-yield savings account.
- A retiree who wants inflation protection on part of a portfolio and is comparing I bonds, TIPS, and short-term T-bills.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Sources often compare rates without stating the date or the current inflation adjustment, so the numbers go stale quickly.
- Explanations of the 1-year lockup and 3-month interest penalty are often buried or skipped, which leaves viewers surprised by early-redemption costs.
- Videos rarely show a worked example in dollars, so viewers cannot see how the doubling claim or the inflation rate plays out over time.
- Phương pháp của 6 video đầu bảng: 3 ý kiến, không tính, 1 giả định cố định, 2 dữ liệu lịch sử thật.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Retire With Style | [pkbwgnRq8II](https://youtu.be/pkbwgnRq8II) | 5–10 phút | ý kiến, không tính |
| Harry's Bull Run | [thadNc64xNo](https://youtu.be/thadNc64xNo) | 10–15 phút | giả định cố định |
| Sab Invests | [5EhuvbJ9f0g](https://youtu.be/5EhuvbJ9f0g) | 10–15 phút | ý kiến, không tính |
| Be Your Own Chief Investment Officer | [P_RqgLUU4vQ](https://youtu.be/P_RqgLUU4vQ) | 15–20 phút | ý kiến, không tính |
| Finance Flow | [lThPhPQiiXQ](https://youtu.be/lThPhPQiiXQ) | 15–20 phút | dữ liệu lịch sử thật |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- X vs Y: Which Earns More After N Years?
- Inflation-Protected vs Fixed Government Savings: What Happens to $10,000?
- Are Savings Bonds Worth It? A Redemption-Penalty Breakdown
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
I bonds, EE bonds, savings bonds, treasury bills, TreasuryDirect, inflation-protected savings

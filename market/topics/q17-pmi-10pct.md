# Hồ sơ cầu — 10% Down and Mortgage Insurance: How Long Did It Last?

Đề tài: dòng #17 trong `topics/queue.md` · id `q17-pmi-10pct` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 5–9 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Does mortgage insurance on an FHA loan ever come off, and does it last for the whole loan even with a large down payment or substantial equity? — trọng số cao
2. Can PMI be avoided or bought out by paying it upfront at closing, or by splitting the loan into a first and second mortgage, and is that cheaper overall? — trọng số cao
3. When does lender-required PMI cancel automatically, and what can a borrower do when the lender refuses or says it will never go away? — trọng số cao
4. Can a new appraisal after renovations or rising home values get PMI removed, and does that appraisal affect homeowners insurance or property taxes? — trọng số cao
5. How do I tell PMI from FHA mortgage insurance or USDA insurance on my statement, and do the removal rules differ for each? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A conventional-loan owner who has paid down a lot of principal and made improvements, but whose lender insists the insurance runs until a set date and refuses a removal request.
- A first-time FHA buyer with a small down payment who cannot tell from the monthly statement whether the charge is PMI or MIP, and fears it lasts for the life of the loan.
- A buyer who avoided mortgage insurance with a piggyback second loan or a large down payment, and is now weighing a refinance against keeping a low rate.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Treats the lender's stated cancellation timeline as the only path and does not explain automatic cancellation versus borrower-requested removal.
- Describes FHA mortgage insurance as either always removable or always permanent without explaining how loan date and down payment change the rules.
- Recommends workarounds such as upfront payment or piggyback loans without showing the total cost or downsides.
- Phương pháp của 6 video đầu bảng: 4 giả định cố định, 2 ý kiến, không tính.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Home Loan Education | [PomJeQEkhaA](https://youtu.be/PomJeQEkhaA) | 15–20 phút | giả định cố định |
| Nathan Udomsri | [Yy0DP1EGPWA](https://youtu.be/Yy0DP1EGPWA) | 5–10 phút | giả định cố định |
| Wise Money Show | [3htUqeXWGio](https://youtu.be/3htUqeXWGio) | 5–10 phút | giả định cố định |
| Winning With Wade · Mortgage Education & Strategy | [5u_n29D1LlA](https://youtu.be/5u_n29D1LlA) | 5–10 phút | ý kiến, không tính |
| Interconnect Mortgage · Toni Taylor Gozza | [INt3KHJ6Bng](https://youtu.be/INt3KHJ6Bng) | 0–5 phút | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- Home Loan Education — [PomJeQEkhaA](https://youtu.be/PomJeQEkhaA) — 15–20 phút — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Can You Drop Mortgage Insurance Early? [N] Steps for [Loan Type] Borrowers
- Is Paying Mortgage Insurance Upfront Worth It? Break-Even at [N] Years
- [Loan Type] Mortgage Insurance: Permanent or Temporary? Check Your Statement in [N] Minutes
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
remove PMI, FHA mortgage insurance removal, PMI vs MIP, cancel PMI automatically, PMI at 20 percent down, mortgage insurance cancellation request

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A dedicated video on paying mortgage insurance upfront at closing, with a break-even calculation.
- A video on whether mortgage insurance removal still works after a loan recast.
- A video on mortgage insurance rules for manufactured homes.
- A state-specific video covering mortgage insurance removal rules in Florida and other high-cost states.
- A video on whether refinancing makes sense when the only goal is dropping mortgage insurance.

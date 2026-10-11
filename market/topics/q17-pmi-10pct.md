# Hồ sơ cầu — 10% Down and Mortgage Insurance: How Long Did It Last?

Đề tài: dòng #17 trong `topics/queue.md` · id `q17-pmi-10pct` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **vừa** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 6:54–8:18 | tứ phân vị 25–75 % của video đầu bảng cùng đề tài |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Can FHA mortgage insurance (MIP) ever be removed, or does it last the life of the loan? — trọng số cao
2. Can a higher appraisal or reappraisal get PMI dropped, and what does the lender actually require (appraisal, BPO, or a formal request)? — trọng số cao
3. Can I pay PMI upfront or buy it out at closing, and is that worth the cost compared with monthly premiums? — trọng số cao
4. Why does PMI or MIP still show on my statement after I've paid down past 20% equity? — trọng số vừa
5. When does the lender have to end PMI automatically, and does waiting until a set year or the 78% point apply? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A conventional buyer put 10% down, now has about 15% equity on a home whose value has stayed flat, and pays roughly $80 a month in PMI. They want to know whether a reappraisal or a lender request will drop it.
- An FHA borrower with 30% down has been on time for years and believes mortgage insurance lasts the whole loan. They are unsure whether their monthly payment includes PMI or MIP and whether a refinance is worth it.
- A homeowner renovated a property and now estimates its value well above the purchase price, but the lender refuses to act on that. They are weighing extra principal payments, a second loan, or an appraisal fee to remove the insurance.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Overhyped 'loophole' framing promises that lenders hide a secret, without showing the actual rules or the lender's written process.
- Advice to pay PMI upfront or use an 80/20 second loan is presented as always better, with no cost comparison or breakeven math.
- FHA loans get treated like conventional PMI, so MIP rules (including the loan-life rule for many FHA loans) are skipped or misstated.
- Phương pháp của 6 video đầu bảng: 2 giả định cố định, 3 ý kiến, không tính, 1 dữ liệu lịch sử thật.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Home Loan Education | [PomJeQEkhaA](https://youtu.be/PomJeQEkhaA) | 16:12 | giả định cố định |
| Nathan Udomsri | [Yy0DP1EGPWA](https://youtu.be/Yy0DP1EGPWA) | 5:24 | ý kiến, không tính |
| Wise Money Show | [3htUqeXWGio](https://youtu.be/3htUqeXWGio) | 8:18 | giả định cố định |
| Winning With Wade · Mortgage Education & Strategy | [5u_n29D1LlA](https://youtu.be/5u_n29D1LlA) | 6:54 | ý kiến, không tính |
| Money Rerouted | [1o-2RJ-DdfE](https://youtu.be/1o-2RJ-DdfE) | 7:48 | dữ liệu lịch sử thật |

## Video vượt trội cùng đề tài (cho dòng G1)

- Home Loan Education — [PomJeQEkhaA](https://youtu.be/PomJeQEkhaA) — 16:12 — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Dropping Mortgage Insurance Early: Does a Reappraisal Beat Waiting Out the Timeline?
- Upfront Premium vs Monthly Insurance: Which Costs Less Over the First 7 Years?
- Why Your Statement Still Shows Mortgage Insurance After You Hit 20% Equity
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
remove PMI, PMI removal, FHA MIP removal, 20 percent down vs 10 percent down, cancel PMI Homeowners Protection Act, mortgage insurance 80 percent LTV

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A breakeven calculator comparing monthly PMI, upfront premium, and an 80/20 second-loan setup over 5 to 10 years.
- A step-by-step guide to requesting PMI cancellation under the Homeowners Protection Act, including the 80% and 78% rules and what documents to send.
- A plain-language guide to reading a mortgage statement and telling PMI from FHA MIP, USDA fees, and escrow.
- A walkthrough of when an appraisal or BPO is accepted for PMI removal and what each usually costs.

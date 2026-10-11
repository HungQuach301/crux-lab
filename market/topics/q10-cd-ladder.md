# Hồ sơ cầu — 1-Year CD Pays More Than a 5-Year: Roll or Lock?

Đề tài: dòng #10 trong `topics/queue.md` · id `q10-cd-ladder` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 14–17 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Is chasing the highest cash yield worth the effort on a modest balance, or does the extra return disappear once you count time and hassle? — trọng số cao
2. Which is simpler and pays more for short-term cash: a CD ladder, self-directed Treasury bills through TreasuryDirect, or a T-bill ETF? — trọng số cao
3. How do state and federal income taxes change the ranking of CDs, T-bills, money market funds, and high-yield savings? — trọng số cao
4. When rates are moving, should you roll short-term CDs or lock a longer term to secure today's rate? — trọng số vừa
5. Are T-bill and bond ETFs as safe and liquid as CDs or money market funds for holding cash? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A saver with a $10,000 lump sum in a 12-month CD who rebuys a new CD each month so that one matures every month and the cash stays accessible.
- A California resident who moved cash from a money market fund into a T-bill ETF to avoid state income tax and to lower fees.
- A retiree with a roughly $400K cash position split across a money market fund, a T-bill ETF, and CDs, deciding whether to lock a multi-year rate or keep rolling short-term.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Compares headline yields without converting them to after-tax returns, so state-tax exemptions and federal rates are left out of the ranking.
- Skips the mechanics of building a T-bill or CD ladder, and never explains why self-directed Treasury purchases are an alternative to ETFs and funds.
- Uses oversimplified premises such as large lump sums and ignores the latest short-term Treasury auction rates, which many viewers consider more relevant than the funds it compares.
- Phương pháp của 6 video đầu bảng: 3 ý kiến, không tính, 3 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Rob Berger | [BkHhGbtb2EM](https://youtu.be/BkHhGbtb2EM) | 15–20 phút | ý kiến, không tính |
| Dividend Hustle Mark | [bN_KMvvItrI](https://youtu.be/bN_KMvvItrI) | 15–20 phút | giả định cố định |
| Dividend Hustle Mark | [B18i-RrxQpg](https://youtu.be/B18i-RrxQpg) | 10–15 phút | giả định cố định |
| Dividend Hustle Mark | [38XFfYhfYUg](https://youtu.be/38XFfYhfYUg) | 15–20 phút | giả định cố định |
| The Algorithm Investor | [xEyXGHjs0TQ](https://youtu.be/xEyXGHjs0TQ) | 10–15 phút | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- X vs Y vs Z: Which Cash Vehicle Keeps the Most After Tax Over N Years?
- Lock or Roll? How to Pick a CD Term When Rates Are Moving
- Build a Short-Term Treasury Ladder: TreasuryDirect vs CDs vs T-Bill ETFs
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
CD ladder, Treasury bills, TreasuryDirect, T-bill ETF, high yield savings, after-tax yield

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A comparison of a floating-rate Treasury ETF as a cash holding during rising-rate periods.
- A step-by-step walkthrough of building a T-bill ladder through TreasuryDirect.
- A look at the latest 26-week and 52-week T-bill auction rates versus current fund yields.
- Whether municipal bond funds make sense for cash held in a high-state-tax location.
- An explanation of brokerage sweep accounts versus core positions and how each affects cash yield and insurance.

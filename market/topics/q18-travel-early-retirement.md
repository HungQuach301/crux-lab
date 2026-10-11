# Hồ sơ cầu — Travel Early in Retirement or Wait?

Đề tài: dòng #18 trong `topics/queue.md` · id `q18-travel-early-retirement` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **thấp** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 13–27 phút | tứ phân vị 25–75 % của video vượt trội cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Should I spend more in my early retirement (go-go) years, or hold back for later? — trọng số cao
2. How do I know whether my portfolio can support higher spending, and how should I adjust withdrawals when markets rise or fall? — trọng số cao
3. How much should I set aside for healthcare, assisted living, or long-term care, and can those costs wipe out my savings? — trọng số cao
4. How do I stop being afraid to spend savings I was raised to protect? — trọng số vừa
5. How do taxes, Social Security timing, RMDs, and Medicare premiums change how much I can actually spend? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A frugal couple in their early 60s with about $1.2M saved and no debt wants to take a bucket-list anniversary trip while they're healthy, but one spouse keeps resisting because of a childhood of financial scarcity.
- A single retiree at 58 with a military pension and investment income is comfortable and debt-free, but is unsure whether to delay Social Security to 70 or spend more now while active.
- An adult child is covering a shortfall for a parent whose savings ran out before assisted living costs were planned, and is now deciding how much to save for their own care versus enjoying retirement early.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Uses gross figures and ignores US Medicare premiums, out-of-pocket medical and drug costs, and taxes, so retirement spending looks understated.
- Treats assisted living and long-term care as a minor caveat rather than modeling their high, unpredictable monthly cost.
- Relies on fixed success rates and rigid withdrawal assumptions, with examples that contain math errors and switch from conservative to aggressive return assumptions midway.
- Phương pháp của 6 video đầu bảng: 1 ý kiến, không tính, 2 dữ liệu lịch sử thật, 3 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Holy Schmidt! | [rWWH9jtVjUw](https://youtu.be/rWWH9jtVjUw) | 10–15 phút | ý kiến, không tính |
| James Shack | [-EGrPGUBGn0](https://youtu.be/-EGrPGUBGn0) | 15–20 phút | dữ liệu lịch sử thật |
| Erin Talks Money · Erin Moriarity | [XR_MAoJ9QXs](https://youtu.be/XR_MAoJ9QXs) | 10–15 phút | giả định cố định |
| Erin Talks Money · Erin Moriarity | [PCZ0UDPWG-U](https://youtu.be/PCZ0UDPWG-U) | 15–20 phút | giả định cố định |
| Erin Talks Money · Erin Moriarity | [IOPWlBtsPNU](https://youtu.be/IOPWlBtsPNU) | 15–20 phút | dữ liệu lịch sử thật |

## Video vượt trội cùng đề tài (cho dòng G1)

- Hannah Invests — [O3w5P-dc1vU](https://youtu.be/O3w5P-dc1vU) — 20–30 phút — ≥ 5× (tự tính)
- Holy Schmidt! — [rWWH9jtVjUw](https://youtu.be/rWWH9jtVjUw) — 10–15 phút — ≥ 5× (tự tính)
- Erin Talks Money · Erin Moriarity — [XR_MAoJ9QXs](https://youtu.be/XR_MAoJ9QXs) — 10–15 phút — ≥ 3× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- [Spend More Now] vs [Hold Back for Later]: Which Keeps You Solvent Past Age [N]?
- How Much Can a [Single/Couple] Spend in the Go-Go Years With $[X] Saved?
- [Dynamic Withdrawal Rule] Test: Does Spending More Early Survive a [N]-Year Retirement?
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
early retirement travel budget, go-go years retirement spending, retirement withdrawal guardrails, assisted living costs retirement, how much to spend in retirement

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- Model net-of-tax withdrawals, not gross, so the spending figure reflects take-home money.
- Add a full healthcare and long-term care module, including Medicare, IRMAA, and assisted living scenarios.
- Show annuity payouts by pension size for singles and couples, and the main factors that affect them.
- Include more single-focused scenarios, especially military pensions and their role in retirement planning.
- Compare Social Security claiming ages with the cost of working longer, including how each choice affects health-span years.

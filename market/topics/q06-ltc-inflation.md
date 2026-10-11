# Hồ sơ cầu — Long-Term Care Insurance: 3% or 5% Inflation Protection?

Đề tài: dòng #6 trong `topics/queue.md` · id `q06-ltc-inflation` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **vừa** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 12–27 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Will a long-term care policy actually pay out when I need it, and how hard is the claims process? — trọng số cao
2. Is paying premiums for decades worth it compared with investing that money and self-funding care? — trọng số cao
3. How much does care really cost, and how long do people typically need it? — trọng số cao
4. What are the realistic ways to pay for care, such as hybrid policies, HSAs, home equity, Medicaid, or tax deductions? — trọng số vừa
5. How do the numbers change for singles without children, for couples, and for people in different states? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- Single retiree in their late 60s with no children or nearby siblings, weighing whether to self-fund care or buy a policy and worried about who would manage the decisions.
- Married couple in their early 60s with a paid-off home and moderate savings, comparing a hybrid policy with investing the premium money in index funds.
- Adult child who has just finished managing a parent's dementia care, dealing with a stalled claim, and deciding whether to buy coverage for themselves.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Glosses over claim denials, heavy paperwork, and benefit triggers, which makes insurance look more reliable than viewers experience it.
- Omits hybrid policies, inflation riders, and death-benefit options, so the comparison covers only traditional policies.
- Presents slide percentages and averages that do not reconcile and ignore large state and regional differences in care costs and facility quality.
- Phương pháp của 6 video đầu bảng: 1 dữ liệu lịch sử thật, 1 giả định cố định, 4 ý kiến, không tính.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Erin Talks Money · Erin Moriarity | [ugef5CPZaFs](https://youtu.be/ugef5CPZaFs) | 20–30 phút | dữ liệu lịch sử thật |
| Erin Talks Money · Erin Moriarity | [nJYzAGFEk_M](https://youtu.be/nJYzAGFEk_M) | 20–30 phút | giả định cố định |
| Erin Talks Money · Erin Moriarity | [mb1VPz-neRM](https://youtu.be/mb1VPz-neRM) | 20–30 phút | ý kiến, không tính |
| The Art of Planning Before Investing | [2-_TDlxZhwk](https://youtu.be/2-_TDlxZhwk) | 10–15 phút | ý kiến, không tính |
| Erin Talks Money · Erin Moriarity | [ERIfxnZ50gg](https://youtu.be/ERIfxnZ50gg) | 5–10 phút | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- Erin Talks Money · Erin Moriarity — [ugef5CPZaFs](https://youtu.be/ugef5CPZaFs) — 20–30 phút — ≥ 3× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- [Payment Option A] vs [Payment Option B]: Which Leaves More Money After [N] Years of Care?
- The Real Odds of Needing Care by Age [X]: What the Numbers Mean for Your Plan
- Can [Asset Type] Cover [Care Setting] for [N] Years? A Scenario-by-Scenario Breakdown
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
long term care insurance inflation protection, hybrid life insurance long term care, paying for long term care in retirement, self-funding long term care costs, long term care costs by state, long term care claim denial

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- Break out the numbers for single people without heirs, including how early costs differ from later ones.
- State whether the couple figures assume both spouses need care, and show scenarios where only one does.
- Deep-dive on alternatives such as downsizing, family housing, and CCRC communities, including expert guests.
- Explain how care costs are treated for taxes, including itemizing, HSA use, and the 7.5 percent of AGI threshold.
- Cover Medicaid rules, state partnership programs, and how Medicaid coordinates with Medicare.

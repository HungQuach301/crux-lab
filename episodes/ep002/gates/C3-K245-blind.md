# C3c — Kiểm mù nhanh KEY-2/4/5 trên hệ hình cuối · vòng 1 (01/10/2026)

Ý đồ: `gates/C3-K245-intent.md`. Khoá: `review-c3/k245-key-r1.json`. Cả hai commit 58c62e5, trước khi chạy. 9 người đọc mới, thứ tự trộn.

## Nguyên văn

**eb9f0995** (KEY-2): A marker starts at a zero line and drops further below it while a green area grows (frames 2-3), which looks like a loan balance or debt deepening, probably from borrowing and accruing interest. The green area then shrinks back toward zero (frames 4-5) as the debt is paid down, and in frame 6 the marker rises above the line with an orange area, meaning the balance has turned positive (a net gain or surplus). I am fairly but not fully sure of this reading, since all labels are hidden.

**989b3530** (KEY-2): A marker starts below a baseline and a shaded teal bar grows from the baseline down to it, so the downward gap widens and then shrinks back to zero (frames 2-4). Frame 5 shows the marker back on the baseline, and in frame 6 it sits above the baseline with an amber bar. This looks like a balance moving from owing (negative, teal) to zero to surplus (positive, amber), or a deficit growing and then being paid off. In a loan context, that would be debt building up and then being repaid.

**01dc9cbc** (KEY-2): It looks like a bar/timeline chart where a balance (the diamond marker) starts below a baseline, which I read as debt. The shaded area grows (frames 2-3), which I read as interest piling up and the balance getting deeper, then shrinks (frame 4) and returns to the baseline (frame 5), which I read as paying the debt off. In frame 6 the marker and shaded area are above the baseline in amber, which I read as a surplus or savings. For a grad student with private loans, this would show how a loan balance grows with accruing interest and can only be brought back to zero, and then to positive, by repayment over time. I can't be sure of this reading because all the text and numbers are hidden.

**39ddb309** (KEY-4): Three parallel tracks (probably three scenarios or loan balances) are tracked over time against a baseline line, with a bar on the right summing each one's running result: the top track ends well above the line (a growing gain, green), the middle one ends modestly above it, and the bottom one swings above the line and ends in a large shortfall (orange peaks, red hatched bar). The idea seems to be that the same starting point can produce very different outcomes depending on how things fluctuate and compound over time, with the third path ending in a deficit or loss, such as debt growing instead of shrinking. I'm inferring this because all labels are covered.

**3f720894** (KEY-4): Three scenarios (rows) are tracked over time: in each one a running balance moves against a baseline, and the bar chart on the right summarizes the final result. The top scenario ends clearly positive (teal, a surplus or gain), the middle ends modestly positive, and the bottom swings far into the opposite region (orange, then a red hatched bar, a net shortfall or loss), meaning small differences in how things evolve (for example, rates or timing) can lead to very different outcomes, with the third path ending in the red.

**34b261e8** (KEY-4): Three parallel timelines (like three scenarios or loan balances) play out left to right, each tracking a value against a baseline: the top one stays steadily above the line (a growing positive gain, green), the middle one dips slightly above and below but ends modestly positive, and the bottom one swings mostly above the line into a large, volatile orange area that ends as a big negative on the summary bar (red hatched). It conveys that the same starting point can lead to very different cumulative outcomes over time, with the bottom case accumulating a large, risky shortfall or cost (such as growing debt/interest) while the top case builds a steady surplus.

**5897cce9** (KEY-5): The section shows a long-run line chart (looks like a market or interest-rate history) with a highlighted window sliding along it, and in the later frames a grid of small blocks builds up beneath it, filling in as the window passes a sharp peak and then the following decline. It seems to illustrate how outcomes depend on timing: looking at different periods of the same history (for example borrowing or repaying through a rate spike) gives very different results, and the accumulating blocks suggest a running count of periods or payments tied to those rates.

**f122a24a** (KEY-5): A fixed-length window slides forward one step at a time along a long historical line, which looks like an interest rate or similar rate that climbs to a sharp spike and later falls to near zero. Each window position is tallied as one square in a growing grid, so the video seems to be testing many overlapping periods, such as a loan's repayment term, against history to show how widely outcomes vary depending on when you start. For a borrower, the point is that a variable-rate private loan's cost depends heavily on which rate period you happen to borrow or repay in. This reading is an inference, since all text is hidden.

**b0540afc** (KEY-5): A highlighted window slides along a long time-series line (looking like a market or interest-rate history), first covering a calm early stretch and then moving to the huge spike and the decline after it. Beneath it, a growing grid of blocks fills in, as if counting up the periods or scenarios the window has covered. The likely point is that results depend heavily on which period you start in, so a longer history that includes the extreme peak gives a more complete picture of the risk than a quiet stretch does.

## Chấm
| Nhịp | Người đọc | Điểm | Lý do |
|---|---|---|---|
| KEY-2 | eb9f0995 | 0,5 | thấy khoảng cách so với vạch lớn lên, thu lại, về 0, đảo lên trên; nhưng đọc là **một khoản dư nợ theo thời gian**, không phải hai mức khởi đầu |
| KEY-2 | 989b3530 | 0,5 | như trên ("owing → zero → surplus") |
| KEY-2 | 01dc9cbc | 0,5 | như trên ("lãi chồng rồi trả hết") |
| KEY-4 | 39ddb309 | 0 | ba kịch bản, kết quả khác nhau; không thấy tích luỹ khi ở dưới hay rút khi ở trên |
| KEY-4 | 3f720894 | 0 | như trên |
| KEY-4 | 34b261e8 | 0 | như trên; đọc dải trên vạch thành "khoản lời" |
| KEY-5 | 5897cce9 | 1 | cửa sổ trượt dọc lịch sử, khối xếp dần; kết quả tuỳ giai đoạn |
| KEY-5 | f122a24a | 1 | cửa sổ dài cố định trượt từng bước, mỗi vị trí một ô; nhiều giai đoạn chồng nhau, tuỳ lúc bắt đầu |
| KEY-5 | b0540afc | 1 | cửa sổ trượt; lưới đếm các giai đoạn; kết quả tuỳ thời điểm bắt đầu |

**KEY-5: 3/3 → ĐẠT. KEY-2: 0/3 đúng (3 nửa) → TRƯỢT. KEY-4: 0/3 → TRƯỢT.** Theo lệnh C3c: sửa KEY-2 và KEY-4 **một vòng**, kiểm lại với 3 người đọc mới mỗi nhịp, ý đồ không đổi.

## Chẩn đoán
- **KEY-2:** chỉ có một vật (điểm thoi) di chuyển liên tục quanh một vạch, nên người đọc thấy một số dư thay đổi theo thời gian. Sửa: dùng lại hình KEY-1 đã đạt (một người, hai thẻ, vạch 9% liền qua hai thẻ). Chỉ **điểm bắt đầu** trên thẻ thả nổi **nhảy** giữa các vị trí rời (xa dưới / gần dưới / trên vạch / trên vạch), không trượt mượt. Mỗi lần nhảy, thẻ được "thay" như một lời mời khác (lật thẻ). Khoảng chênh tô `#269783` khi ở dưới, `warn` khi ở trên.
- **KEY-4:** ba đường song song và cột tổng kết bị đọc thành "ba kịch bản khác kết cục". Không ai thấy cơ chế "đệm". Sửa: **một** đường quanh vạch 9% và **một cái hũ** đặt cạnh. Khi đường ở dưới vạch, hũ đầy lên (`#269783`); khi ở trên, hũ rỉ ra (`warn`), đồng bộ từng tháng. Kết: hũ cạn, khối `#C72323` xuất hiện. Hũ là vật chứa nhìn thấy, không phải diện tích.

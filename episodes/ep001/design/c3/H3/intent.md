# H3 — "Hình học của tiền" · Ý đồ (viết TRƯỚC khi render)

DESIGNER H3, 29/09/2026. Nguồn gu: G-012 (c) "biểu đồ, bản đồ, chữ và số tự hiểu được"; G-011 "hình tự nói được ý khi tắt tiếng"; G-004 (d) "hiểu trong 1 giây"; A4 (nghĩa nằm ở chuyển động).

## Ngữ pháp chung (giữ nguyên qua F1–F3)

| Thứ trên màn hình | Nghĩa | Luôn luôn |
|---|---|---|
| Chiều cao / diện tích khối | Đô la (danh nghĩa) | Trong một khung chỉ có một thang $; khối to gấp đôi = tiền gấp đôi. |
| Trục ngang | Thời gian (tuần ở F1, tháng ở F2–F3) | Trái → phải = trước → sau. |
| Một dải mỏng rơi vào khối | Một tháng tiết kiệm | Mỗi dải = một tháng, cao đúng bằng khoản bớt/tháng. |
| Xanh lá (`positive`), có vạch nối dải | Tiền tiết kiệm được | Vạch nối là hoa văn để không lẫn với màu nhân vật (tokens.json, ghi chú màu). |
| Viền xám (`ink-muted`) | Hoá đơn / phí phải trả lại | Không tô đỏ (đỏ = màu Anjali). |
| Hổ phách gạch chéo (`warn`) — chỉ ở F2 | Phần nợ ẩn (dư nợ cao hơn) | F2 không có nhân vật hổ phách (Walt) trên màn hình. |
| Đường xanh dương (`accent`) | Lãi thị trường (PMMS tuần) | Tự vẽ theo thời gian, không nhảy. |

Chuyển động chỉ có ba loại, mỗi loại một ý: **vẽ** (thời gian trôi), **lấp** (tiền dồn lại), **mọc thêm / co lại** (một khoản mới hiện ra hoặc mất đi). Không có chuyển động trang trí (không trôi nền, không lắc camera, không hạt).

Số trên màn hình: chỉ số trong `out/claims.json`, viết đúng `display`. Số của nhân vật (Nora, Walt, Anjali) có nhãn **ILLUSTRATIVE** sát bên, hiện cùng lúc với số. Nhãn "nominal $" ở góc mỗi khung có tiền.

## F1 · Cold open: cửa sổ lỡ (~9 s)

**Người xem tắt tiếng phải hiểu:** lãi vay đã xuống thấp một thời gian (vùng sáng = "cửa sổ"); trong lúc đó Nora có thể bớt một khoản mỗi tháng (thanh xanh dài ra, lớn nhất $459/tháng ở đáy); rồi lãi leo lại, cửa sổ tắt, thanh co lại — chỉ còn cái bóng rỗng của $459 = khoản đã lỡ.

| t (s) | Chuyển động | Ý |
|---|---|---|
| 0–1 | Trục tuần 12/2025→9/2026 hiện; vạch ngang đứt "Nora's loan 7.62%" (chấm tròn xanh lá, ILLUSTRATIVE). | Có một người đang trả lãi 7.62%. |
| 1–1.8 | Vùng dưới vạch "7.62% − 1 point" sáng lên, nhãn "window". | Dưới vạch này, vay lại mới đáng. |
| 1.8–5 | Đường lãi tuần tự vẽ đi xuống vào vùng sáng. Thanh ngang "Nora could save / month" bên phải dài ra theo đúng khoản bớt tính ở tuần đó. Ở đáy: nhãn "5.98% · week ending February 26, 2026 · lowest since September 2022", thanh đạt "$459/mo" (ILLUSTRATIVE); một bóng viền đánh dấu độ dài này. | Lãi càng thấp, khoản bớt càng lớn; đỉnh là $459. |
| 5–7.2 | Đường leo lên; qua tuần July 23, 2026 nó ra khỏi vùng sáng → vùng tắt xám, chữ "window closed". Thanh co lại; bóng rỗng $459 ở lại. | Cơ hội đã qua; khoảng trống giữa bóng và thanh là thứ đã lỡ. |
| 7.2–9 | Đường chạm 7.03% (week ending September 24, 2026): nhãn "back above 7% — first time since January 2025". Giữ yên ~1 s. | Lãi đã quay lại trên 7%. |

Claim: `r_old`, `s10`, `low2026`, `low2026_date`, `low2026_since`, `sav_low2026_median`, `cut1_last_2026`, `r_today`, `anchor_date`, `seven`, `first7_since`. Độ dài thanh ở các tuần khác tính bằng cùng mô hình (`model/`: dư nợ trung vị sau k kỳ, k theo quy ước `k35`/`k_low2026`), không in số.

**Dải 6 khung phải cho thấy:** (1) vạch 7.62% (2) cửa sổ sáng (3) đường đi xuống, thanh dài ra (4) đáy 5.98%, $459 (5) cửa sổ tắt, thanh co, bóng rỗng (6) 7.03%, trên 7%.

## F2 · Hoà vốn dời từ 24 → 30 tháng (~10 s)

**Người xem tắt tiếng phải hiểu:** hoá đơn $5,124 là một khối rỗng; mỗi tháng một dải $221 rơi vào lấp dần; tới tháng 24 khối có vẻ đầy — nhưng một phần nợ ẩn ($1,133, đã lớn dần từ đầu dưới dạng bóng mờ) hiện thành khối hổ phách trên đỉnh; phải lấp thêm tới tháng 30 mới thật sự đầy.

| t (s) | Chuyển động | Ý |
|---|---|---|
| 0–1 | Khối viền xám "Loan costs $5,124" dựng từ đáy; nhãn "Nora" + ILLUSTRATIVE. Thước tháng 0–36 bên dưới. | Đây là hoá đơn phải lấy lại. |
| 1–1.6 | Dải đầu tiên "$221 saved / month" rơi vào đáy. | Mỗi tháng một dải. |
| 1.6–5.2 | Dải rơi đều, con trỏ trên thước chạy tháng 1→24. Phía trên khối, một bóng mờ gạch chéo lớn dần (gần như không thấy). | Tiền dồn; có thứ gì đó đang lớn mà ta chưa để ý. |
| 5.2–6.2 | Tháng 24: dải chạm miệng khối, nhãn "$5,124 ÷ $221 = 24 months" hiện. Rồi bóng mờ **đặc lại** thành khối hổ phách "+ $1,133 still owed (higher balance)"; miệng khối dời lên; "24" bị gạch. | Phép chia bỏ sót một phần nợ. |
| 6.2–8.8 | Dải tiếp tục rơi tới tháng 30 (phần hổ phách vẫn lớn chậm); khối đầy ở tháng 30: viền sáng, "break-even: month 30". | Hoà vốn thật ở tháng 30. |
| 8.8–10 | Giữ yên. | |

Claim: `cost_median`, `sav_median`, `be_simple_median`, `gap24`, `be_bal_median`. Đỉnh phần hổ phách ở tháng 25–30 theo mô hình (dư nợ khoản mới − khoản cũ), không in số khác $1,133.

**Dải 6 khung:** (1) khối rỗng $5,124 (2) vài dải đầu (3) nửa khối, bóng mờ phía trên (4) tháng 24 "tưởng đầy" (5) khối hổ phách mọc, 24 bị gạch (6) đầy ở 30.

## F3 · Walt và Anjali (~10 s)

**Người xem tắt tiếng phải hiểu:** hai khoản vay chênh nhau rất xa (thanh khoản vay ngắn / dài), nhưng hai hoá đơn phí gần bằng nhau; mỗi tháng Anjali lấp nhanh (dải dày $387), Walt lấp chậm (dải mỏng $68) — tới mốc 3 năm Anjali đã đầy từ lâu, Walt còn xa; vì vậy Walt cần giảm lãi 1.12 điểm, Anjali chỉ khoảng 1/3 điểm.

| t (s) | Chuyển động | Ý |
|---|---|---|
| 0–1.4 | Hai cột: Walt (tam giác hổ phách) trái, Anjali (vuông đỏ) phải; thanh khoản vay mọc ngang đúng tỉ lệ: $115,000 vs $655,000 (ILLUSTRATIVE). | Khoản vay chênh gần 6 lần. |
| 1.4–2.4 | Hai khối phí viền xám dựng lên cùng thang: $3,667 vs $5,514 — gần bằng nhau. | Phí thì gần như cố định. |
| 2.4–6.4 | Một đồng hồ tháng chung chạy 0→36. Dải rơi vào mỗi khối: Walt dải mỏng "+$68/mo", Anjali dải dày "+$387/mo". Anjali đầy ở tháng 18 (tính cả dư nợ; nhãn "month 18"). Tới "3 years" Walt mới lấp được khoảng một nửa. | Cùng thời gian, tốc độ lấp khác hẳn. |
| 6.4–9 | Thước "rate cut needed to break even in 3 years" (0 → 1.25 điểm) mọc ở đáy; vạch "1 point"; tam giác trượt tới "1.12", vuông trượt tới "about 1/3". | Khoản nhỏ cần giảm lãi nhiều hơn. |
| 9–10 | Giữ yên. | |

Claim: `loan_small`, `loan_large`, `cost_small`, `cost_large`, `sav_small`, `sav_large`, `be_bal_large`, `hold36`/`y3`, `s10`, `cut36_small`, `cut36_large_words` (hiển thị "about 1/3" — cần WRITER/DATA xác nhận cách viết tắt này, nếu không dùng "about a third of a point"). Phần nợ ẩn trong F3 vẽ như F2 nhưng không nhãn số.

**Dải 6 khung:** (1) hai thanh khoản vay (2) hai khối phí gần bằng (3) đang lấp, tốc độ khác (4) Anjali đầy ở 18 (5) tháng 36, Walt còn thiếu (6) thước 1.12 vs about 1/3.

## Không làm
- Không 3D, không ảnh, không bản đồ (không có dữ liệu bản đồ cần cho ba nhịp này).
- Không nền đen tuyền, không cặp màu xanh–nâu, không font ngoài Inter.
- Không số nào ngoài claim; không tick số trên trục ngoài claim.

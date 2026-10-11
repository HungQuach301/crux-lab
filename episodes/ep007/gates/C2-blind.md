# C2 — Kết quả kiểm máy + kiểm mù lời (ý đồ: `C2-intent.md`)

**(a) Máy:** `story/check_script.py` ĐẠT ở v1 và v2 (exit 0). v2: 1.454 từ nói → **ước 10:05** (`lab` 9:00–11:00), M1 3,8 · M2 28,2 · M3 18,8 · M4 8,7 · M5 39,2 · M6 0 s (cả 3 móc ĐẠT), 2 mid-roll (≈ 2:50 sau S09.3, ≈ 7:00 sau S24.3; hold 1,5 s). Cảnh báo: ≥ 3 số mới trong 8 s ở 4 chỗ (S11–S12, S13–S14, S16–S17, S26–S28); khuôn: limits −6,5 (chủ ý, story §3), concept +5,7 (THAM KHẢO).

**(b) Kiểm mù lời** (6 Sonnet headless khoá Console, 5 T vai "trả thêm hay đầu tư" + 1 G; 1 người chấm độc lập mỗi vòng):
| Vòng | Bản | Đúng | Khuyên | Khối mất chú ý (loại ≥ 2/6) | "Trả lời câu hỏi mang tới" |
|---|---|---|---|---|---|
| 1 | v1 | 6/6 | 0/6 | **phương pháp 6/6** (S32 giới hạn) → trượt ngưỡng cổng (≥ 4/6) | 1/6 (T 0/5) |
| 2 | v2 (S32 → 2 câu + thẻ V7 + mô tả; thêm S25.5 "không kiểm lợi suất đầu tư") | 6/6 | **6/6 theo người chấm vòng 2** | số dày 3/6 (S17 "2000s… 6.18", S21) · khác 2/6 (câu trỏ thẻ phương pháp) · định nghĩa 1/6 | 1/6 (T 0/5) |

**Đọc kết quả (sửa theo REVIEWER CHẶN, `gates/REVIEW-C2.md`; ý đồ không sửa):**
- **Câu khuyên TRƯỢT cả hai vòng theo rubric ghi trước** (`c2/rubric.md` có trước vòng 1, ghi rõ "trả theo tháng thay vì năm" là hành động): vòng 1 có 5/6 người đọc nêu "trả tháng hơn trả năm" ở câu 6 — người chấm vòng 1 chấm nới (0/6), đúng rubric là **5/6**; vòng 2 **6/6**. Nguồn: S23–S24 (câu hỏi khán giả 3) + câu đối trọng yếu S24.2. Không người đọc nào nói video bảo chọn khoản vay / đầu tư / dự báo lãi (câu 5: 12/12 "no").
- Khối mất chú ý: vòng 1 phương pháp 6/6 (S32) → v2 gỡ được; v2 số dày 3/6 (S17, S21).
- Đã hết 2 vòng (`episode.md` §2). **v3 sau REVIEWER (CHƯA kiểm mù):** S24.2 đối trọng mới ("That isn't a verdict on paying yearly: the money stays in her account longer, and what it earns there isn't counted."); S25.4–S25.5 bỏ "has to clear it to come out ahead" (người đọc viết "no risk / guaranteed"); S30.1, S15.3–S15.4 tách câu; ngày và lãi thập kỷ ở S13–S18, S26–S27 chuyển lên hình; S22.2 trả câu hỏi khán giả 5 (lãi tháng sau giảm); S33.3 "What she now knows". Kiểm máy v3 ĐẠT, ước **9:53**. → G1 nêu: cờ khuyên trượt 2 vòng; bản sửa chưa kiểm mù; khuyến nghị kiểm mù vòng 3 (6 người đọc) đầu chặng sau trước C3, hoặc bỏ nhịp Q3.
- **Câu hỏi mang tới: T 0/5 cả hai vòng** — người hỏi "trả thêm hay đầu tư" muốn vế đầu tư; tập chỉ đưa mốc (lãi khoản vay), không có lợi suất thị trường.
- Chi: vòng 1 + 2 ≈ 0,17 triệu trần headless, $0,60; WRITER v1 $3,34, v2 $0,91.

## Vòng 3 (P2, G1 câu 2 = a) — ý đồ ghi TRƯỚC khi chạy
- **Bản:** C2 v3.1 = v3 (REVIEWER) + mốc tuần dữ liệu thay "this week" (G1 câu 2) — `c2/sample-r3.txt` (33 cảnh, 1.280 từ viết), checker ĐẠT ước 10:01.
- **Người đọc:** 6 Sonnet headless khoá Console (5 T vai cũ "trả thêm hay đầu tư" + 1 G), câu hỏi 1–7 như vòng 2 + **câu 8** (nguồn lời khuyên: video / own / none — để chấm rubric mới) — `c2/spec-r3.json`. 1 người chấm độc lập, `c2/rubric-r3.md` (rubric MỚI theo G1 câu 2; phần đúng / mất chú ý / câu hỏi mang tới giữ nguyên).
- **Qua:** `advice_stated` = 0/6 **và** đúng ≥ 5/6 (dừng khi 2 sai) **và** không loại khối mất chú ý ≥ 4/6. `advice_inferred`/`caution_only` chỉ báo, câu trích vào bảng.
- **Trượt khuyên (`advice_stated` ≥ 1):** theo G1 câu 2 — bỏ nhịp Q3 (S23–S24), bù để đạt ≥ 3/5 câu hỏi khán giả (vd Q4 PMI), WRITER mới; không mở thêm vòng kiểm cùng bản.
- Loại khối mất chú ý ≥ 2/6 → ghi, sửa ở bản trước sinh giọng nếu sửa được bằng hình (D-009: hình trước, nhãn cuối).

### Vòng 3 — kết quả (`c2/r3/`; người đọc 67.796 token, chấm `c2/r3/grade.out`)
| Hex | Vai | Điểm | Cờ (S/I/C) | Câu 8 | Mất chú ý (loại: cảnh) |
|---|---|---|---|---|---|
| 2e1ac893 | T | 1 | C | video* | khác: S23 trả mỗi năm (lạc đề) |
| 5565cb0f | T | 1 | C | video* | số dày: S23–S24 ($8,792, four months, $8,200) |
| 6228463a | T | 1 | C | video* | khác: S23 trả mỗi năm (lạc đề) |
| 695e2793 | G | 1 | I · C | own | số dày: S21–S24 (195 months, 15 months late, $733, $8,792, $8,200) |
| 704516bf | T | 1 | C | — | số dày: S21 (195 months, 15 months late, $733) |
| 86277015 | T | 1 | C | video* | phương pháp: S31 "Any fixed-rate borrower can set their own pair beside hers" |

\* "video" ở câu 8 trỏ tới **khung hiểu** (S31 "set their own pair beside hers", S25.4 "the bar… gets measured against", S31 "hard to get back in a bad month"), không tới hành động — rubric: "so lãi khoản vay với cách dùng tiền khác / biết giá của đường lui là hiểu lời hứa" → `caution_only`.

**Kết luận theo luật ghi trước:** đúng **6/6** · **`advice_stated` 0/6 → QUA** (rubric mới) · `advice_inferred` 1/6 (G: *"my conclusion in 6 is my inference from its framing"*) · rubric cũ (song song, báo): 0/6 người đọc nêu "trả tháng hơn trả năm" — câu đối trọng S24.2 v3 gỡ được nguồn trượt vòng 1–2 · không loại khối ≥ 4/6 → **QUA cổng**. Nhịp Q3 (S23–S24) **giữ** (G1 câu 2: chỉ bỏ khi còn `advice_stated`).
- **Loại khối ≥ 2/6:** số dày **3/6** (S21–S24) + khác 2/6 (S23 "lạc đề") — cùng một đoạn. Sửa bằng hình (D-009): lời S21.2 bỏ "195 months", S23.2 bỏ "$8,792" → chỉ trên hình B21/B23 (checker ĐẠT, ước 9:54). Không mở vòng kiểm thêm; REVIEWER C3 đọc lại; C4 kiểm mù bản có lời đo lại đoạn này.
- **Câu trích cần REVIEWER đọc:** 2e1ac893 câu 7 *"extra principal earns the loan's rate (7.4% for Tessa) with no risk"* — người đọc tự thêm "no risk" dù lời đã bỏ "has to clear it"; 86277015 câu 6 *"the bar any alternative use of the money has to beat"* (diễn lại S25.4). Ghi cho chữ phát hành (G1 câu 1: không dùng "has to clear").
- **Câu hỏi mang tới:** T **một phần 4/5** (vòng 1–2: 0/5) — người đọc nhận nửa "trả thêm được bao nhiêu" (mốc 7,4 % trước thuế) và đường lui có giá; nửa đầu tư vẫn không (S25.5 chủ ý).

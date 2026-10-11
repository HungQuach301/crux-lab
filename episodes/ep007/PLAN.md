# PLAN Tập 7 — 30-Year Mortgage Paid Off in 15 Years (≤ 1 trang)

**Nhánh:** `ep007` · **Đề tài:** #13 (debt-1) · **Format:** `lab` · **Phiên hiện hành:** P1 (`session_01UTALjtLsD1NKGK7DGGcHq1`) → **dừng ở G1 lô Tập 7–8**

## 1. Trạng thái
**G1 lô chờ** (`gates/G1.md`). Việc 0 ĐẠT (kiểm độc lập 57/57) · C1 L1 3/3 · C2 v3 kiểm máy ĐẠT, ước 9:53, M1–M6 thật ĐẠT (M2 29,8 s sát ngưỡng) · kiểm mù lời đúng 6/6 hai vòng, **khuyên trượt hai vòng theo rubric** (nhịp Q3), v3 chưa kiểm mù · REVIEWER C2 + G1 ĐẠT có sửa (đã áp) · Tập 8 #20 hồ sơ §4 ĐẠT, logline 3/3 (rủi ro: tiền thuê ban đầu không nguồn).

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời G1 → `gates/G1-answer.md`; ghi `taste-ledger.md`, `AUTHORSHIP.md`, ledger. Nếu câu 2 = (a): kiểm mù vòng 3 C2 v3 (6 người đọc, `c2/spec.json` vai + câu hỏi, `c2/rubric.md` không sửa) **trước C3**.
2. **P2 = C3** (G1 cần C3): hình mới N1 "Month track" + W2 Stack ("the stack"), W3 Beam ("the bar") — clip có chuyển động và âm; cổng gốc.
3. Lô K Tập 7 (`K-brief.md`: kind MỚI + A29–A31) chạy song song, merge `main` trước C4.
- Treo: F-14 (`tongket-t6/F14-brief.md`, chủ dự án mở `factory-f14`); EL hạn mức (khoá thiếu `user_read`); CHARTER §5 dòng G2 (mặc định sửa ở phiên kế nếu anh không phản đối); `novelty.json` #20 chạy lại kiểm web ở P1 Tập 8; tỉ lệ thuê/giá có nguồn cho #20.

## 3. Quyết định đã có (chủ dự án)
- 11/10 tổng kết Tập 6: `tongket-t6/ANSWER.md` (1a·d·f·g duyệt; `deep` chỉ khi F-14 đạt trước G1 → Tập 7 `lab`; đóng gói ChatGPT ở P4 với brief (a)–(f)).

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 r1→v2 | S32 | mất chú ý phương pháp 6/6 | S32 → 2 câu + thẻ V7 + mô tả; S25.5 | r2 không khối ≥ 4/6 | số dày 3/6 (S17, S21) |
| REVIEWER → v3 | S24.2, S25.4–5, S30.1, S15.3, S13–S18, S26–S27, S22.2, S33.3 | khuyên (Q3), overclaim "has to clear", câu mơ hồ, số dày, Q5 lệch | câu nguyên văn REVIEWER; ngày/lãi lên hình | checker ĐẠT 9:53 | **chưa kiểm mù** |
| Bản đọc | S02.2 | M2 30,6 s | rút câu hứa | M2 29,8 s | sát ngưỡng |

## 5. Mức cảnh báo, token, chi (`episode.md` §8, `lab`: 15 triệu · Console $45)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Console |
|---|---|---|---|---|---|---|---|
| P1 | 11/10 13:49 (get_session) | 0,10 | 0,32 | 27,51 | **0,41 triệu** | 0,81 triệu | ≈ $8,9 (+ Haiku/Sonnet thị trường) |
0 agent con · YouTube ≈ 7.300 đơn vị · EL 1.233 ký tự · giờ render 0.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `episodes/ep007/PLAN.md` 4. `episodes/ep007/gates/G1.md` 5. `episodes/ep007/gates/G1-answer.md` 6. `episodes/ep007/story/beats.md` 7. `toolkit/visual-library/README.md` 8. `episodes/ep007/gates/C2-blind.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 7, phiên P2 (C3). Nhánh ep007. Mở bằng `bash toolkit/verify.sh ep007`; đọc mục 6 của episodes/ep007/PLAN.md.
Gói đã gửi: episodes/ep007/gates/G1.md (G1 lô Tập 7–8). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep007/gates/G1-answer.md, ghi taste-ledger.md, AUTHORSHIP.md, ledger; commit, push.
Chặng này: (nếu câu 2 = a) kiểm mù vòng 3 C2 v3 trước C3 → C3 hình mới (N1 Month track, the stack, the bar; clip có chuyển động và âm; cổng gốc) → dừng ở C3 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên"; sửa D-011: tệp lớn còn ở container thì chạy tiếp sau /compact). Song song: lô K Tập 7 (episodes/ep007/K-brief.md + A29–A31) trên nhánh checks-k*, merge main trước C4. Việc nặng: headless khoá Console (toolkit/api.sh), 0 agent con trừ khi cần công cụ phiên. Nếu câu trả lời không phản đối CHARTER §5: sửa dòng G2 theo D-012 câu 3.
Câu trả lời G1:
<<DÁN CÂU TRẢ LỜI G1 Ở ĐÂY>>
```

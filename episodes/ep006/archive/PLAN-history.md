# PLAN Tập 6 — lịch sử (bản PLAN cũ khi đóng mỗi phiên)


## Bản đóng P1 (G1, @ 2627822)

# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 (`topics-r1/machine/retire-1/`) · **Format:** `101` đề xuất (chờ G1) · **Phiên hiện hành:** P1 (`session_019BA5MXtsQ6jZqogoJGeCBF`) — đóng ở G1

## 1. Trạng thái
**G1 chờ** (issue [#48](https://github.com/HungQuach301/crux-lab/issues/48), gói `gates/G1.md`). Việc 0: SHA khớp hồ sơ, kiểm độc lập 43/43. C1: L1 3/3. C2 v2: kiểm máy ĐẠT trừ độ dài (ước 7:50, thiếu 24 s); kiểm mù vòng 2 6/6, khuyên 0, không khối ≥ 4/6; M1 3,6 · M2 27,5 · M3 13,9 · M4 6,06 · M5 33,3 · M6 0 s (bản đọc thật). REVIEWER ĐẠT có sửa (1 CHẶN + 4 CHÍNH đã sửa). 0 CHẶN/CHÍNH mở.

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời G1 → `gates/G1-answer.md`; ghi `taste-ledger.md`, `AUTHORSHIP.md`, ledger. Áp: (a) → chạy check với `--g1-short`; (b) → WRITER mới thêm ≈ 60 từ chất có nguồn + kiểm mù lại hồi 2–3.
2. **P2 → C3** (G1 dự kiến "cần C3"): ký hiệu mới N1 "hàng 10 thùng" (3D, `beats.md`) + **nhạc hiệu kênh** (clip có âm, `episode.md` §5b); cổng gốc; sửa bằng hình ba khối 2/6 (S31.2 phương pháp, S03.1/S06.3 định nghĩa, S09/S12 số dày) + 7 PHỤ `gates/REVIEW-G1.md`.
3. Khi `main` có khoá K mới (lô `checks-k40`, kind cho `K-brief.md`) → merge `main` vào `ep006`, chạy S01/S05; viết `contract.json`.
- Treo: lô K (`checks-k40`, chưa thấy trên origin lúc 15:00 UTC; `main` vẫn 447690e, LOCK d93276a4). Đề xuất sửa mẫu `playbook/templates/check_script.py`: khối M4 cắt ở khoảng lặng > 1,5 s (Tập 5 ước 13,5 → 9,1 s, đo 9,8) — chờ tổng kết Tập 6.

## 3. Quyết định đã có (chủ dự án)
- 08/10 D-011 Q1: Tập 6 = #12; G1 từng tập; Q3 phiên K lô song song (không mở K riêng).
- 08/10 lệnh P1: năm luật §2b, M4 hiệu chuẩn 2,75 từ/s, đề xuất format theo 2,52 từ/s không độn, claim-risk #12. G1: chờ → `gates/G1-answer.md`.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 v1→v2 | S18–S23 | mất chú ý "số dày" 6/6 (thập kỷ 94,8/99,5 %; PCE 19,2 %) | dự phòng: 12 câu → 3, số lên nhãn B19/B22, V7, mô tả; S30.5 đối trọng | 6/6, khuyên 0, khối ≤ 2/6 | độ dài −24 s |
| G1 REVIEWER | S08.1, S12.1–2, B08 | CHẶN-1 thùng của khoản đều không nguồn | "6 in 10 / 9 in 10" so khoản đầu của chính nó | check ĐẠT | — |
| G1 REVIEWER | S04.3, S31.3, nhãn góc | CHÍNH-2 "pays more money"; CHÍNH-5 thiếu "US consumer prices" | "compare the dollars both checks pay out"; "US consumer prices · US only" | check ĐẠT | — |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập: **15** triệu (trần = đầu vào mới + sinh ra, log phiên). EL ≤ 6.000 ký tự (dùng **1.114**) · ≤ 40 agent con (dùng **4**).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
Lấy bằng `python3 toolkit/usage/from_events.py --session session_019BA5MXtsQ6jZqogoJGeCBF --close episodes/ep006/archive/usage/p1-page*.json`; lượt đóng (áp REVIEWER, PLAN, issue) cộng ở phiên sau. Cộng P1 ≈ 0,89 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/G1.md` 7. `episodes/ep006/gates/G1-answer.md` (phiên kế tạo) 8. `playbook/prompts/P2.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P2. Nhánh ep006 (@ e677bf1 hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Gói đã gửi: episodes/ep006/gates/G1.md (issue #48). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep006/gates/G1-answer.md, commit, push; ghi taste-ledger.md, AUTHORSHIP.md, ledger.
Nếu main đã có khoá K mới (lô checks-k40, kind cho episodes/ep006/K-brief.md): merge main vào ep006 trước.
Chặng này: áp G1 → C3 (ký hiệu "hàng 10 thùng" + nhạc hiệu kênh, clip có chuyển động và âm) → dừng ở C3 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên"). Nếu G1 ghi "không cần C3" thì làm P3 → dừng ở G2.
Câu trả lời G1:
<<DÁN CÂU TRẢ LỜI G1 Ở ĐÂY>>
```

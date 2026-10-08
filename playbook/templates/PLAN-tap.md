# PLAN Tập {N} — {tiêu đề}  (≤ 1 trang; phiên điều phối cập nhật sau mỗi bước, viết lại khi đóng phiên)

Mẫu từ tổng kết Tập 5 §3.7 (chủ dự án duyệt 08/10; theo `cine-lab/playbook/PLAN-TAP-MAU.md`). Lịch sử (bảng cổng chi tiết, lệnh cũ, giao file, điểm dừng cũ) → `episodes/ep{NNN}/archive/PLAN-history.md`. **Quyết định còn hiệu lực luôn ở mục 3 hoặc `gates/*-answer.md`, không chỉ ở archive.**

**Nhánh:** `ep{NNN}` · **Đề tài:** #{k} · **Format:** `101`/`lab` · **Phiên hiện hành:** P{x} (`session_…`)

## 1. Trạng thái
<Việc 0 | C1 | C2 | G1 chờ | C3 chờ | C4 | C5 | G2 chờ | G3 | xong> — một dòng: đã đạt gì, số đo chính (CHẶN/CHÍNH, cổng gốc, M1–M6, độ dài ước).

## 2. Việc tiếp (≤ 3) và việc treo
1. …
- Treo: … (ai, chờ gì)

## 3. Quyết định đã có (chủ dự án)
- {dd/mm} {cổng}: … → `gates/{cổng}-answer.md`

## 4. Đã sửa gì, vì sao (vòng sửa; ≤ 10 dòng — chép nguyên vào đầu bài agent mới, `episode.md` §1)
| Vòng | Cảnh | Lỗi (mã luật / người đọc) | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập: {15} triệu (trần = đầu vào mới + sinh ra, log phiên). EL ≤ 6.000 ký tự · ≤ 40 agent con.
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
4 số lấy bằng `python3 toolkit/usage/from_events.py --session <id> --close trang*.json` khi đóng phiên.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep{NNN}/PLAN.md` (tệp này) 5. `episodes/ep{NNN}/ledger.md` 6. <gói cổng gần nhất> 7. <tệp câu trả lời> 8. <tệp của chặng kế>

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập {N}, phiên P{x+1}. Nhánh ep{NNN} (@ {sha}). Mở bằng `bash toolkit/verify.sh ep{NNN}`; đọc mục 6 của episodes/ep{NNN}/PLAN.md.
Gói đã gửi: episodes/ep{NNN}/gates/{cổng}.md. Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep{NNN}/gates/{cổng}-answer.md, commit, push.
Chặng này: {việc} → dừng ở {cổng kế} (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Câu trả lời {cổng}:
<<DÁN CÂU TRẢ LỜI {cổng} Ở ĐÂY>>
```

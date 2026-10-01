# PLAN — Tập 2, quy trình 6 cổng (P-ep002)

Nhánh: `ep002` (từ `main` `e117c49`). Chỉ P-ep002 merge `ep002` vào `main` (fetch + rebase trước; trong file dùng chung chỉ sửa phần Tập 2). Khung: `playbook/quality-framework.md`. Bài học: `playbook/lessons.md`. Khoá kiểm hiện hành: **K3.4 `64a15c4e`** (bản sao scratchpad `checks-k34/`, SHA khớp).

**Đề tài:** `topics/queue.md` #1 — hồ sơ duy nhất `topics-r1/machine/debt-2/`. Máy đề xuất (D-004): kết quả YouTube = số đo TRỄ.
**Đầu vào chủ dự án (01/10/2026):** Q1=A giữ hệ giọng/âm/nhận diện Tập 1 (C3 chỉ một clip nghe xác nhận ~30 s) · Q2=A gói phát hành vào C1/C3/C6 · Q3=A ≥ 70% nhịp then chốt đọc đúng khi tắt tiếng và che chữ/số ở C4, có đối chứng.

## Trạng thái cổng

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Việc 0 Khung tập | XONG — dữ liệu không đổi; kiểm độc lập 116/116 + 753/753; bối cảnh chính sách; neo 7,5/9 | — | — |
| C1 Ý tưởng và lời hứa | XONG | `gates/C1.md`, `gates/C1-blind.md` | A + tiêu đề A1; phạm vi (b), câu hỏi trung tâm "thả nổi phải thấp hơn bao nhiêu"; ILLUSTRATIVE |
| C2 Kịch bản | ĐANG LÀM — WRITER treatment | — | — |
| C3 Thiết kế | chưa | — | — |
| C4 Animatic có chuyển động | chưa | — | — |
| C5 Render và L1 | chờ K3.5 merge vào main (`float-vs-fixed-replay`, LOCK bd1948d9; chạy thử 0 lệch) | — | — |
| C6 Chấm cuối và chốt gói | chưa | — | — |

## Việc treo cần chủ dự án (không chặn cổng)
- K3.5 đang merge (LOCK bd1948d9) — C5 kiểm SHA trên main trước khi chạy.
- K3.6 (sau C2): danh sách claim chưa có khoá — báo ở gói C2.

## Điểm dừng an toàn (cập nhật trước mỗi bước dài)
- 2026-10-01 03:00 (1): Việc 0 bước 1–3 xong và đã commit. Nếu mất container: `python3 episodes/ep002/data/fetch.py --verify && python3 episodes/ep002/model/model.py && python3 episodes/ep002/model/compare_independent.py`. Đang: agent chính sách (`story/policy-context.md`) và agent neo 7,5/9 (`story/rate-anchor.md`) — nếu mất thì giao lại cùng đề bài (ledger 02:50).

## Quy ước
- Ý đồ kiểm mù ghi trước ở `gates/Cx-intent.md` (commit trước khi chạy); kết quả nguyên văn ở `gates/Cx-blind.md`.
- Mỗi agent con, mỗi cổng: một dòng ở `ledger.md` (kèm ký tự ElevenLabs).
- Gu không tự quyết; kỹ thuật tự quyết, ghi lý do ở ledger.
- Gen được bảo vệ của tập (`claim-risk.md`): không "your loan will…"; luôn hiện cả 1954–1980 và từ 1981 cùng trường hợp xấu nhất; không "variable is safe"/"wins X%" đứng riêng; kết quả chỉ đúng cho cặp lãi đang xét; "history, not a forecast"; lời và chữ trên hình ở dạng mô tả (S10: take/lock/choose).
- 2026-10-01 03:50 (2): gói C1 gửi. Chờ 3 câu trả lời. Sau khi trả lời: ghi taste-ledger/AUTHORSHIP (main) + ledger; giao WRITER treatment (C2).
- 2026-10-01 (3): C1 xong. Đang: WRITER treatment → beat sheet → kịch bản (C2). Nếu mất: đọc `gates/C1.md` + ledger dòng "Cổng C1", giao lại WRITER với đề bài ở `story/WRITER-brief.md`.
- 2026-10-01 (4): K3.5 đã merge main `a93637a` (LOCK bd1948d9, SHA khớp). Sổ gu/AUTHORSHIP C1 trên main `59a726f`. WRITER đang chạy (đầu bài `story/WRITER-brief.md`). Tiếp: CRITIC 1 vòng (tham khảo) → table read Eric v3 theo cảnh (`story/table-read/`) → kiểm mù C2 (đối chứng yếu M1b) → gói C2 + danh sách K3.6.

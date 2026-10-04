# PLAN — Tập 2, quy trình 6 cổng (P-ep002)

Nhánh: `ep002` (từ `main` `e117c49`). Chỉ P-ep002 merge `ep002` vào `main` (fetch + rebase trước; trong file dùng chung chỉ sửa phần Tập 2). Khung: `playbook/quality-framework.md`. Bài học: `playbook/lessons.md`. Khoá kiểm hiện hành: **K3.4 `64a15c4e`** (bản sao scratchpad `checks-k34/`, SHA khớp).

**Đề tài:** `topics/queue.md` #1 — hồ sơ duy nhất `topics-r1/machine/debt-2/`. Máy đề xuất (D-004): kết quả YouTube = số đo TRỄ.
**Đầu vào chủ dự án (01/10/2026):** Q1=A giữ hệ giọng/âm/nhận diện Tập 1 (C3 chỉ một clip nghe xác nhận ~30 s) · Q2=A gói phát hành vào C1/C3/C6 · Q3=A ≥ 70% nhịp then chốt đọc đúng khi tắt tiếng và che chữ/số ở C4, có đối chứng.

## Trạng thái cổng

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Việc 0 Khung tập | XONG — dữ liệu không đổi; kiểm độc lập 116/116 + 753/753; bối cảnh chính sách; neo 7,5/9 | — | — |
| C1 Ý tưởng và lời hứa | XONG | `gates/C1.md`, `gates/C1-blind.md` | A + tiêu đề A1; phạm vi (b), câu hỏi trung tâm "thả nổi phải thấp hơn bao nhiêu"; ILLUSTRATIVE |
| C2 Kịch bản | XONG — v5 (C2b (a): phương pháp 1 câu + thẻ; head start định nghĩa một lần) | `gates/C2.md`, `C2-blind.md`, `C2-blind-r2.md` | — |
| C3 Thiết kế | **GÓI ĐÃ GỬI — chờ chủ dự án** | `gates/C3.md`, `C3-blind.md`, `design/c3/cvd.md` | — |
| C4 Animatic có chuyển động | chưa | — | — |
| C5 Render và L1 | khoá **K3.6 `2fcc9fcc`** trên main; S01/S05 chạy thử PASS 0 lệch | — | — |
| C6 Chấm cuối và chốt gói | chưa | — | — |

## Việc treo cần chủ dự án (không chặn cổng)
- K3.5 đang merge (LOCK bd1948d9) — C5 kiểm SHA trên main trước khi chạy.

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
- 2026-10-01 (5): kịch bản v2 (84 câu, 1 462 từ) đã kiểm máy. Đang: table read `python3 episodes/ep002/story/table_read.py` (nohup, log `review-c2/table-read.log`; chạy lại cùng lệnh để tiếp, cảnh xong không tốn ký tự lại). Sau đó: kiểm mù C2 → gói C2.
- 2026-10-01 (6): kiểm mù C2 xong (5/5; `gates/C2-blind.md`). Table read lần 1 dừng (502 ở cảnh dài). WRITER v3 đang sửa theo kiểm mù + chia cảnh ≤ 900 ký tự. Tiếp: kiểm máy v3 → table read (xoá takes cũ, sinh lại cả tập) → gói C2.
- 2026-10-01 (7): kiểm mù C2 hai vòng xong. Table read DỪNG (S01–S02 có, 398 ký tự) chờ chủ dự án xác nhận tin nhắn giọng Bill. Tiếp khi rõ: chạy lại `story/table_read.py` (bỏ qua cảnh đã có) → clip C2 → gói C2.
- 2026-10-01 (8): chủ dự án: tin "GIỌNG KỂ" gửi nhầm (Cine Lab) — bỏ qua, giữ Eric v3. Table read chạy tiếp (S03 trở đi).
- 2026-10-01 (9): table read xong (10:10); gói C2 gửi. Chờ 3 câu. Sau đó: WRITER áp quyết định (v4 nếu có sửa) → C3 (3 hướng hình, style frame có chuyển động cho 7 KEY, concept thumbnail, đuôi end screen; clip giọng ~30 s xác nhận).
- 2026-10-01 (10): v4 + kiểm mù vòng 3 xong; gói C2b (1 câu: đoạn phương pháp). C3 bắt đầu song song (brief `design/c3/BRIEF.md`).
- 2026-10-01 (11): C2b duyệt → v5. K3.6 merge (2fcc9fcc), S01/S05 PASS. C3: đủ H1/H2/H3 + đối chứng Tập 1; tiếp: kiểm mù 28 mẫu (`gates/C3-intent.md`) → gói C3.
- 2026-10-01 (12): gói C3 gửi (hướng, màu, giọng). Sau khi trả lời: style frame cuối + ký hợp đồng hình qua clip → animatic C4 (giọng v5 theo cảnh, sửa KEY-1/KEY-7).

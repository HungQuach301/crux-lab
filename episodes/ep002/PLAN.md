# PLAN — Tập 2, quy trình 6 cổng (P-ep002)

Nhánh: `ep002` (từ `main` `e117c49`). Chỉ P-ep002 merge `ep002` vào `main` (fetch + rebase trước; trong file dùng chung chỉ sửa phần Tập 2). Khung: `playbook/quality-framework.md`. Bài học: `playbook/lessons.md`. Khoá kiểm hiện hành: **K3.4 `64a15c4e`** (bản sao scratchpad `checks-k34/`, SHA khớp).

**Đề tài:** `topics/queue.md` #1 — hồ sơ duy nhất `topics-r1/machine/debt-2/`. Máy đề xuất (D-004): kết quả YouTube = số đo TRỄ.
**Đầu vào chủ dự án (01/10/2026):** Q1=A giữ hệ giọng/âm/nhận diện Tập 1 (C3 chỉ một clip nghe xác nhận ~30 s) · Q2=A gói phát hành vào C1/C3/C6 · Q3=A ≥ 70% nhịp then chốt đọc đúng khi tắt tiếng và che chữ/số ở C4, có đối chứng.

## Trạng thái cổng

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Việc 0 Khung tập | XONG — dữ liệu không đổi; kiểm độc lập 116/116 + 753/753; bối cảnh chính sách; neo 7,5/9 | — | — |
| C1 Ý tưởng và lời hứa | **GÓI ĐÃ GỬI — chờ chủ dự án** | `gates/C1.md`, `gates/C1-blind.md` | — |
| C2 Kịch bản | chưa | — | — |
| C3 Thiết kế | chưa | — | — |
| C4 Animatic có chuyển động | chưa | — | — |
| C5 Render và L1 | **chờ K3.5 merge** (`model.kind` `rate-path-history`, đặc tả `checks-notes.md`) | — | — |
| C6 Chấm cuối và chốt gói | chưa | — | — |

## Việc treo cần chủ dự án (không chặn cổng)
- Xác minh **$20,500/năm, $100,000 tổng** (Direct Unsub sau đại học từ 1/7/2026) trên FR PDF 91 FR 23883 trước khi lên hình — proxy chặn govinfo/studentaid (`story/policy-context.md` §2).
- **K3.5** (chủ dự án mở phiên riêng): bản tính lại độc lập `rate-path-history` cho S01/S05 — đặc tả ở `checks-notes.md`. C5 chờ K3.5 merge (LOCK mới trên main, kiểm SHA).

## Điểm dừng an toàn (cập nhật trước mỗi bước dài)
- 2026-10-01 03:00 (1): Việc 0 bước 1–3 xong và đã commit. Nếu mất container: `python3 episodes/ep002/data/fetch.py --verify && python3 episodes/ep002/model/model.py && python3 episodes/ep002/model/compare_independent.py`. Đang: agent chính sách (`story/policy-context.md`) và agent neo 7,5/9 (`story/rate-anchor.md`) — nếu mất thì giao lại cùng đề bài (ledger 02:50).

## Quy ước
- Ý đồ kiểm mù ghi trước ở `gates/Cx-intent.md` (commit trước khi chạy); kết quả nguyên văn ở `gates/Cx-blind.md`.
- Mỗi agent con, mỗi cổng: một dòng ở `ledger.md` (kèm ký tự ElevenLabs).
- Gu không tự quyết; kỹ thuật tự quyết, ghi lý do ở ledger.
- Gen được bảo vệ của tập (`claim-risk.md`): không "your loan will…"; luôn hiện cả 1954–1980 và từ 1981 cùng trường hợp xấu nhất; không "variable is safe"/"wins X%" đứng riêng; kết quả chỉ đúng cho cặp lãi đang xét; "history, not a forecast"; lời và chữ trên hình ở dạng mô tả (S10: take/lock/choose).
- 2026-10-01 03:50 (2): gói C1 gửi. Chờ 3 câu trả lời. Sau khi trả lời: ghi taste-ledger/AUTHORSHIP (main) + ledger; giao WRITER treatment (C2).

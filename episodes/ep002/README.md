# Tập 2 — "7.5% Variable or 9% Fixed? Grad Loans Through History" (tiêu đề nháp của hồ sơ)

Đề tài: `topics/queue.md` #1, hồ sơ **duy nhất** `topics-r1/machine/debt-2/` (không phải `topics-r2/machine/debt-2`). Đề tài do máy đề xuất (D-004): kết quả YouTube của tập là số đo **TRỄ** của D-004 (`audience.md`, sau C6).
Phiên điều phối P-ep002, nhánh `ep002` (từ `main` `e117c49`). Quy trình 6 cổng (`playbook/quality-framework.md`). Tập 1 chỉ là mẫu quy trình, không phải mẫu nội dung.

| File | Nội dung |
|---|---|
| `PLAN.md` | bảng cổng, điểm dừng an toàn, việc treo cần chủ dự án |
| `ledger.md` | sổ chạy (mỗi agent, mỗi cổng một dòng; ký tự ElevenLabs) |
| `amendments.md` | miễn trừ / thay đổi riêng của tập |
| `checks-notes.md` | ghi chú cho phiên kiểm (K3.5: `model.kind` mới) |
| `data/` | `fetch.py --verify` tải lại TB3MS + DTB3 (không commit dữ liệu thô) |
| `model/model.py` | mô hình (lõi = `calc.py` của hồ sơ + phạm vi (b)) → `out/model.json` |
| `gates/` | ý đồ kiểm mù, kết quả nguyên văn, gói quyết định |
| `numbers.md` | bảng số, claim ID |

Dựng lại số: `python3 episodes/ep002/data/fetch.py --verify && python3 episodes/ep002/model/model.py && python3 episodes/ep002/build_numbers.py`.

# PLAN — Tập 1, quy trình 6 cổng (P2)

Nhánh: `ep001-v2` (tạo từ `ep001` @ `3cab8ba`). Chỉ P2 merge vào `main`. Khung: `playbook/quality-framework.md`. Bài học: `playbook/lessons.md`.

**Đề tài:** "Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí vay lại?" — Nora ($375,000, 7.62%, 10/2023), Walt ($115,000), Anjali ($655,000).

## Tài sản giữ (không làm lại)
Dữ liệu và mô hình (`data/`, `model/`, kiểm độc lập 619/619), `numbers.md` (claim ID), ba nhân vật, `story/treatment.md` (qua Cổng A), bảng âm S2.

## Trạng thái cổng

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Việc 0 | XONG — merge `main` `7ebc7ea` | — | Khung 3 lớp duyệt; D-002 |
| C1 Ý tưởng | XONG | `episodes/ep001/gates/C1.md` | Logline C; bộ đo mới (vai khán giả đích, tiếng Anh, đối chứng yếu) |
| C2 Kịch bản | XONG | `episodes/ep001/gates/C2.md` | OK; lịch sử rút (a); câu hứa nói với người xem (2 phương án ở C3) |
| C3 Thiết kế và giọng | XONG hình (hợp đồng ký, sàn chữ 40 px); **giọng: thử mù V1/V2/V3 đang làm** | `gates/C3.md`, `gates/C3-contract.md` | D theo nhịp; Eric eleven_v3; câu hứa "…where would your own loan fall?" |
| C4 Animatic có chuyển động | **GÓI ĐÃ GỬI** — kiểm mù 20/20 (sau sửa S11); giọng Y sinh lại cả tập; animatic 9:52; chờ chủ dự án | `gates/C4.md`, `gates/C4-blind.md` | Giọng Y (theo cảnh + thẻ thưa) |
| C5 Render và L1 | chờ (cần khoá K3 của Phiên K) | | |
| C6 Chấm cuối | chờ | | |

## Việc treo cần chủ dự án (không chặn cổng)
- Proxy phiên chặn đẩy tag và xoá nhánh (HTTP 403). Tag `ep001-v1-stopped` (`3cab8ba`) có ở máy phiên, chưa lên GitHub; bốn nhánh `claude/stoic-lamport-lt6z0z`, `claude/vigilant-tesla-xogj17`, `checks-v2`, `ccr-b659da90-fg2k6j` đã kiểm (ba nhánh đã merge vào main; `ccr-…` trùng `ep001`) nhưng chưa xoá được. `3cab8ba` vẫn an toàn trên nhánh `ep001`.

- Điều khoản thương mại ElevenLabs (gói trả phí): proxy chặn elevenlabs.io → cần chủ dự án dán nguyên văn (billing + Terms of Use) hoặc mở domain; L1 Chặn trước C5.

## Điểm dừng an toàn (cập nhật mỗi khi có thể phải dừng)
- 2026-09-29: C3 hình đã ký; giọng đang thử mù V1/V2/V3 (`review-c3/voice-v/`); animatic C4 đang dựng (`episodes/ep001/animatic/`). Tiếp tục: gửi gói thử giọng → chủ dự án chọn → sinh lại cả tập một kiểu → định thời animatic → kiểm mù tắt tiếng C4.

- 2026-09-29 (2): kiểm mù tắt tiếng C4 xong (63 agent, `gates/C4-blind.md`). Tiếp: chờ a/b/c giọng; sửa S11 (nhãn "division", đường trắng); gói C4.

- 2026-09-29 (3): chủ dự án chọn giọng Y (theo cảnh + thẻ cảm xúc thưa; sổ gu `e4fe3b1` main). WRITER v3.2 8 thẻ (`e80e28a`). Đang: VOICE sinh lại cả tập theo cảnh → định thời → render animatic. Tiếp: clip nổi bật ≤ 2 phút, gói C4, issue, đóng #5.
- 2026-09-29 16:25 UTC (4): container khởi động lại. Lời đọc v3.2 theo cảnh: **13/20 cảnh xong** (S01–S13, `work/v32-voice/takes/`, 0 từ khoá mất theo ASR). S14 lỗi 14:20 do proxy ngắt kết nối (ProxyError RemoteDisconnected), gen.py dừng; vòng chờ treo vì chờ dòng "calls" không bao giờ tới. Tiếp: `work/v32-voice/src/run_resume.sh` (chỉ sinh cảnh còn thiếu, thử lại 5 lần) → build lời → định thời → render → gói C4.
- 2026-09-29 16:35 UTC (5): lời v3.2 đủ 20/20 cảnh, ghép 9:52 (`cd6d846`); animatic định thời lại. Đang render 20 cảnh (3 hàng `render_all.sh`, log `animatic/work/logs/`). Nếu bị ngắt: chạy lại chỉ cảnh chưa có `work/scenes/Sxx.mp4` mới hơn `timing.json`, rồi `check.py` → `assemble.py` (trỏ `review-c4/narration-v32.m4a`) → clip ≤ 2 phút → gói C4.
- 2026-09-29 18:20 UTC (6): gói C4 gửi (`gates/C4.md`, clip `review-c4/c4-highlights.mp4`). Chờ trả lời 3 câu.

## Checklist C5 (Chặn)
- Rà quy ước quyền `quality-framework.md` §8: tìm `data:` trong mã dựng/bản dựng trang; đối chiếu mọi nguồn ghép hậu kỳ với `RIGHTS.md`.
- Điều khoản ElevenLabs trích nguyên văn; Inter OFL trích nguyên văn.

## Quy ước
- Ý đồ kiểm mù ghi trước ở `gates/Cx-intent.md`; kết quả nguyên văn ở `gates/Cx-blind.md`.
- Mỗi agent con, mỗi cổng: một dòng ở `episodes/ep001/ledger.md`.
- Điểm dừng an toàn sau mỗi cổng (commit + push `ep001-v2`).
- Luật F12 (chủ dự án nhắc ở C1 cho screenshot/bằng chứng) chưa có trong `checks/` (K2 tới F11) → cần Phiên K3 viết trước C3/C5.

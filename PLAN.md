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
| C4 Animatic có chuyển động | XONG | `gates/C4.md`, `gates/C4-blind.md` | OK sang C5; giữ 8 thẻ; hình mang ý: mục tiêu số 1 Tập 2 |
| C5 Render và L1 | ĐANG LÀM — khoá **K3.3 `beffb49b`** (SHA đã kiểm); nhãn góc gốc tiền; render lại cảnh có \$; mix sau render; checks | `gates/C5-plan.md`, `gates/C5-rights-audit.md` | ElevenLabs Creator; S09 → K3.2/K3.3; S18 bỏ sở hữu; T1/D1/thumb-3 |
| C6 Chấm cuối | ĐÃ CHẤM — L3 4/5/4/4/4/4; **phát hành CÓ sau khi sửa nhạc + checks đạt** | `gates/C6.md` | G-016 nhạc sáng/nhanh; dòng chân gốc tiền giữ S01, bỏ S06/S07 |

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
- 2026-09-29 (7): C4 duyệt (sổ gu main `31fe42b`). C5 chạy 3 luồng. Nếu bị ngắt: đọc `gates/C5-plan.md`, `work/c5/`, ledger; chạy tiếp luồng dở (render tiếp cảnh thiếu).
- 2026-09-30 (8): container khởi động lại lần 2, mất agent P và A. Ảnh chụp dở dang `524ac85`. Tiếng đã mix xong (master −14,0 LUFS, TP −1,5; stem trên đĩa, SHA trong `out/audio/manifest.json`). Hình: mới render 1080p S12. Đã khởi động lại P (chạy tiếp từ `524ac85`, ghi chú `work/c5/P-notes.md`) và A (kiểm, điểm quảng cáo, tự kiểm; `work/audio/NOTES.md`). ElevenLabs đã trích; chờ chủ dự án xác nhận gói trả phí và hướng S09/K3.2.
- 2026-09-30 (9): S18 sửa chữ + sinh lại (A14 qua). Nhãn gốc tiền: chủ dự án chọn nhãn góc (K3.3); bản hiện tại vẫn nhãn cạnh số (đạt K3.1), bản nhãn góc chuẩn bị sau cờ, **render lại sau khi K3.3 merge**; ảnh trước/sau S01/S07/S15/S18 đi kèm gói C6. Chờ: K3.2 + K3.3 merge → chạy checks. Đang: mix lại 17 739 khung, render S18–S20, ghép video.
- 2026-09-30 (10): K3.3 merge (`c6bdaea`, LOCK beffb49b, SHA khớp). `contract.json` khoá K3.3 (`58881d9`). Rà §8 xong (`gates/C5-rights-audit.md`). **ffmpeg/ffprobe cài bằng apt (mất khi container khởi động lại: `apt-get install -y ffmpeg`)**. Luồng P: bật nhãn góc, render lại 18 cảnh có \$ (≤ 2 hàng); `work/audio/src/mix_after_render.sh` chạy mix sau render; rồi ghép video, checks, gói C6.
- 2026-09-30 07:50 (11): container khởi động lại lần 3 (mất lần chạy checks đầu, sampler chưa ra page.json). Đang: (a) MUSIC 3 bản thử mù A/C/A+C (`review-c6/music-test/`), chờ chủ dự án chọn → sinh lại nhạc cả tập, mix lại; (b) P bỏ dòng chân S06/S07, render lại 2 cảnh, ghép lại hình. Sau (b): chạy sampler trang một lần; sau (a): mux lại, `SKIP_PAGE=1` run.py đầy đủ K3.3; CHẶN sửa, CHÍNH giải thích; rồi phát hành.
- 2026-09-30 09:46 (12): chủ dự án chọn nhạc **P = C** (năng động; sổ gu main `93c416c`). Container khởi động lại lần 4. Đang: mix cả tập `--music-style C` (nohup) → `work/c5/c6_final.sh` mux + SHA; sampler trang K3.3 chạy lại trên hình cuối (`work/c5/logs/sampler-c6.txt`). Tiếp: `SKIP_PAGE=1 checks/run.sh episodes/ep001 --first` (bản sao scratchpad/checks-k33) → CHẶN sửa, CHÍNH giải thích → cập nhật gói C6 → phát hành. Nếu mất: chạy lại mix (cache music C có thể mất → sinh lại), sampler, c6_final.sh.
- 2026-09-30 11:10 (13): **bản giao hiện hành** `episodes/ep001/out/video.mp4` 1 795 536 173 byte, SHA-256 `087830ea3c61968c7e04722fc4ad3b92f5e826588f3b5bf2663ac5577d5460aa` (hình `02a81f68…` + master nhạc C `2dac5abb…`). Không xoá; file nằm trong thư mục repo (còn qua các lần container khởi động lại). GitHub Release nháp: **403** "Creating, editing, or deleting releases is not permitted for this session type" → chờ chủ dự án chọn cách lấy file 1080p.
- 2026-09-30 14:30 (14): release/ep001-rc đủ 19/19 phần (chờ chủ dự án ghép + báo SHA khớp → xoá nhánh). Gói phát hành **chốt**: tiêu đề c2, Test & Compare W (mặc định) + thumb-3 + L, mô tả DA, end screen E1 (`ebb0767`; sổ gu main `4be41cd`; Drive có FINAL). Sampler trang xong 13:57, `out/checks/page.json` commit `a130377`. Container khởi động lại lần 6 (14:27) giết lần chạy checks sau F12 (F01–F12 PASS, log `scratchpad/checks-final-run1.log`). **Đang:** `SKIP_PAGE=1 run.sh --first` chạy lại (nohup). Nếu mất: chạy lại đúng lệnh đó (page.json đã commit). Tiếp: CHẶN sửa, CHÍNH → `out/explanations.json`, commit report, cập nhật `gates/C6.md`, gói xác nhận phát hành.

- 2026-09-30 15:10 (15): checks K3.3 đầy đủ xong (`out/checks/run-c6-1/`): CHẶN 28/29 sau khi sửa S07; S10 → chủ dự án mở **K3.4** (video giữ `087830ea`); CHÍNH V08/V09/V11/C05 chấp nhận. **Tiếp khi K3.4 merge (checks/LOCK trên main đổi khỏi beffb49b):** tạo bản sao checks mới từ main (`git archive <main> checks`), kiểm SHA khớp LOCK, đổi `contract.json` sang khoá mới, cài ffmpeg nếu thiếu, chạy sampler trang (~2 giờ, một mạch) + `SKIP_PAGE=1 run.sh --first`, gửi kết quả cuối. Sau đó: `playbook/episode.md` (tổng kết Tập 1).
## Checklist C5 (Chặn)
- Rà quy ước quyền `quality-framework.md` §8: tìm `data:` trong mã dựng/bản dựng trang; đối chiếu mọi nguồn ghép hậu kỳ với `RIGHTS.md`.
- Điều khoản ElevenLabs trích nguyên văn; Inter OFL trích nguyên văn.

## Quy ước
- Ý đồ kiểm mù ghi trước ở `gates/Cx-intent.md`; kết quả nguyên văn ở `gates/Cx-blind.md`.
- Mỗi agent con, mỗi cổng: một dòng ở `episodes/ep001/ledger.md`.
- Điểm dừng an toàn sau mỗi cổng (commit + push `ep001-v2`).
- Luật F12 (chủ dự án nhắc ở C1 cho screenshot/bằng chứng) chưa có trong `checks/` (K2 tới F11) → cần Phiên K3 viết trước C3/C5.

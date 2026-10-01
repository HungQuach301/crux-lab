# C5 Tập 2 — Render bản cuối + L1 (kế hoạch P-ep002, 01/10/2026)

Quyết định C4 (chủ dự án): sang C5; giữ bốn ký hiệu thay thế. S10.1: mỗi bậc một số chung ≥ 3 s, kèm hai thùng; số chi tiết vào mô tả. K4 thêm "not to scale". Chấm lại độc lập C4 chạy song song.
**Mẫu quy trình:** `episodes/ep001/gates/C5-plan.md`, `C5-rights-audit.md`, `episodes/ep001/out/*` (dạng file), `episodes/ep001/work/audio/src/` (mix, events, takes). Dùng lại **mã**, không dùng nội dung.
**Khoá kiểm:** K3.6 `2fcc9fcc9a94b73084c43ba59970d88f539cd29363334faf52b0640efc2cc801` trên main. Chạy checks trên **bản sao** (`git archive origin/main checks`), kiểm SHA so với LOCK trước khi chạy. Không sửa `checks/`.
**Gu đã khoá:** G-015·chọn (Eric `eleven_v3`, sinh theo cảnh, thẻ cảm xúc thưa, không speed, không thẻ ngắt); G-016·chọn (nhạc C); G-005·chọn (S2 sonify); G-006 (tiếng không lấn lời); hệ hình D2 + E2 đã ký.

| Luồng | Việc | Thư mục ghi |
|---|---|---|
| **A (tiếng)** | Lời cuối: dùng các take C2 của script v5 nếu ASR đủ từ khoá (cùng giọng, mô hình, thiết lập; ghi lý do), cảnh nào trượt thì sinh lại (seed kế), ghi ký tự EL; `out/voice/takes.json`. Mix: lời + nhạc C + tiếng dữ liệu S2 theo bản Tập 1 (G-005/G-006), stems 48 kHz stereo, master theo luật A01/A02; `out/tempo-map.json`, `out/cues.json`, `out/sonify-events.json`, `out/sfx-events.json` | `out/audio/`, `work/audio/`, các json âm thanh |
| **D (hồ sơ)** | `contract.json` (điền TODO: characters, coverage.act, sonification.bandsHz, artefacts; rights.visual), `out/script.json` (v5, thời điểm từ `animatic/timing.json`), `out/claims.json`, `out/timeline.json`, `out/captions.srt`, `out/package/description.md` (gồm số chi tiết S10.1, thẻ phương pháp, nguồn, "history, not a forecast", "US only"), chapters, `out/adbreaks.json`, `out/transitions.json`, `out/tension-map.json`, `preprod/shotlist.json`, `out/rights.json`, `out/visual-assets.json`, `RIGHTS.md` dòng Tập 2 | `contract.json`, `out/*.json` (trừ của P/A), `out/package/`, `preprod/` |
| **P (hình)** | Sau khi sửa C4 xong: `window.CHECKS` (seek/freeze/objects/layer) trên trang dựng, render 1080p30 `out/video.mp4` (hình + tiếng của A), `out/page.json`, `out/camera.json`, `design/tokens.json` | `animatic/src/`, `edit/`, `out/video*`, `out/page.json`, `out/camera.json` |
| **P-ep002** | Ghép, chạy checks (`--first`), sửa CHẶN, viết giải thích CHÍNH (`out/explanations.json`), A14 ("1954-to-1980"), rà §8, gói C5 | — |

Thumbnail, tiêu đề, gói phát hành: C6 (Q2=A).

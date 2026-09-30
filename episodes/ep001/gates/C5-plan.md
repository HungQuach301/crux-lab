# C5 — Render bản cuối + L1 (kế hoạch P2, 29/09/2026)

Quyết định C4 (sổ gu "G-009 · C4"): animatic OK; giữ 8 thẻ; sửa chỗ nhỏ; khoá kiểm **K3.1 `81cf3997`**; trích nguyên văn Inter OFL 1.1 và ElevenLabs trước khi chạy checks; **chỉ CHẶN chặn phát hành, CHÍNH phải giải thích** (`out/explanations.json`).

Định thời đã chốt: `animatic/timing.json` (lời `review-c4/narration-v32.m4a`, 9:51,7). Không đổi lời, không đổi thời điểm câu.

| Luồng | Việc | Thư mục ghi |
|---|---|---|
| **P (hình)** | 4 sửa C4 (giải thích HMDA/FRED/"Dollars of the day" trên hình; bỏ dòng xám giả chữ; nhãn ký hiệu S13/S16/S17/S19; chữ câu hứa "makes that"); `window.CHECKS` (seek/freeze/objects/layer) trên trang dựng; render 1080p30 `out/video.mp4` (hình + tiếng từ luồng A khi có); `out/page.json`, `out/camera.json`, `design/tokens.json` | `animatic/src/`, `edit/`, `out/video*`, `out/page.json`, `out/camera.json`, `design/tokens.json` |
| **A (tiếng)** | Mix: lời v3.2 + nhạc + tiếng dữ liệu bảng âm S2 (G-005/G-006: không lấn lời); stems 48 kHz stereo; master −14 LUFS/true peak theo luật A01/A02; `out/tempo-map.json`, `cues.json`, `sonify-events.json`, `sfx-events.json`; `out/voice/takes.json` | `out/audio/`, `work/audio/`, các file json âm thanh |
| **D (hồ sơ)** | `contract.json` (khoá K3.1, artefacts M3, rights.visual), `out/script.json` (v3.2, thời điểm từ timing), `out/claims.json` (v3.2), `out/timeline.json`, `out/captions.srt`, `out/package/description.md` + chapters, thumbnail ×3, `out/adbreaks.json`, `out/transitions.json`, `out/tension-map`, `preprod/shotlist.json`, `out/rights.json`, `out/visual-assets.json`; trích nguyên văn Inter OFL 1.1 (từ gói @fontsource/inter qua npm) | `contract.json`, `out/*.json` (trừ của P/A), `out/package/`, `preprod/`, `RIGHTS.md` (dòng F-INTER) |
| **P2** | Ghép, chạy `checks/run.sh --first` (khoá K3.1 kiểm SHA trước), sửa CHẶN, viết giải thích CHÍNH, rà §8 (`data:`, ghép hậu kỳ), gói C5 | — |

**Chặn chờ chủ dự án:** trích nguyên văn điều khoản ElevenLabs (elevenlabs.io bị proxy chặn).

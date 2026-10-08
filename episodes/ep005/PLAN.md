# PLAN — Tập 5 (ep005), một phiên điều phối (D-008)

Nhánh **`ep005`** (chủ dự án, G1; trước đó `ccr-a4da2518-3guqrl` @ `906f8be`) từ `main` @ `b1d3e79`. **D-009: chất lượng là ưu tiên tuyệt đối.** **TẠM DỪNG trước dựng hình, chờ Mốc V merge `main`.** Format **`101`** (D-007 thí điểm #1). Đề tài khuyến nghị **#17 debt-2** (PMI với 10 % trả trước). Trần tập **3,0 triệu token** theo loại việc (`episode.md` §8), ≤ 40 agent, ≤ 120 lượt headless, EL ≤ 6.000.

## 1. Bảng cổng
| Cổng | Trạng thái | File | Ghi chú |
|---|---|---|---|
| Việc 0 | XONG | `data/fetch.py`, `model/model.py`, `model/statements.py`, `numbers.md`, `model/independent/` | SHA khớp hồ sơ; 17/17 câu; độc lập 55/55; tháng lãi mới nhất = tháng đủ tuần (2026-09) |
| C1 | ĐẠT | `gates/C1-*.md`, `c1/` | L1 2/2, L2 2/2, cờ 0 → L2 |
| C2 | ĐẠT (vòng 2) | `story/`, `gates/C2-*.md`, `gates/REVIEW-C2.md`, `c2/` | H-A; M1–M5 thật ĐẠT (M4 9,41 s); mù v2 6/6, khuyên 0, S18 3/6 |
| Phiên K | **XONG** — K3.9 merge `main` a870e80 (LOCK d93276a4, kind `ltv-first-passage`); `main` đã merge vào `ep005` | `contract.json`, `out/checks/run-g1-k39/` | S01 104/0 · S03 · S04 PASS; S05 78/78 (claims thử); F11 FAIL + 85 MISSING chờ dựng |
| Contract + tên | **XONG** | `contract.json`, `model/rename_check.py`, `out/model.before-rename.json` | khoá `buyer_owen/grace/victor_*`, số trùng 100 %; `pending`: màu/hình/bên nhân vật, `sonification.bandsHz`, `rights.visual` (cần Mốc V) |
| REVIEWER R1 (không nêu phí PMI) | **0 vi phạm** | `REVIEWER-checklist.md`, `gates/REVIEW-R1.md` | bắt buộc mọi lượt REVIEWER Tập 5; luật máy đề xuất A20 |
| **G1** | **XONG** (issue #43; `gates/G1-answer.md`) | `gates/G1.md`, `gates/REVIEW-G1.md` | #17 · L2 · H-A · T1 · 75 % (a): nguyên văn B-8.1-04, phạm vi Fannie Mae |
| Lời theo cảnh | **XONG 20/20** (S18 seed 1006) | `story/voice_scenes.py`, `voice-takes/`, `review-g1/voice-scenes.json` | ASR từ khoá theo cảnh |
| Mốc V | **XONG** — merge `main` 16d7e1f vào `ep005` | — | CHARTER v4, D-009, D-010, nhà máy thế giới |
| B+2 S03 | **XONG** | `gates/S03-S12-*.md` | "a waiting period" + nhãn Fannie Mae; M4 9,8 s; mù S03→S12 6/6, khuyên 0 |
| **C3 (P2)** | **XONG** (issue #46; `gates/C3-answer.md`) | `gates/C3.md`, `gates/C3-root.md`, `gates/REVIEW-C3.md`, `review-c3/c3-clip.mp4`, `world/SPINE-PLAN.md` | spine v2; N3 ĐẠT; N1/N2 hết 3 vòng (câu khuyên tắt tiếng) → chủ dự án chọn |
| F-5, F-2, F-3, F-1 → C4 → C5 → Shorts → G2 | C4 XONG (khoá nghĩa) | `gates/C4-root.md` | |
| **C5** (render 1080p + checks đủ bộ) | **XONG** — C5c: Tập ĐẠT (CHẶN 35/35); nghĩa ≥ C4 (`gates/C5-root.md`) | `out/checks/run-c5/`, `out/explanations.json`, `HUONG-DAN-DANG.md` | 1080p −14,0 LUFS / −1,9 dBTP, A07 19,6 dB, A08 13,5 dB; CHẶN 29/35 (S07, S08, S09, S10, S17 + REG=S10); CHÍNH 5/11 (F07, V03, V08, V09, V11, V12 giải thích); Shorts SH1–SH3, thumbnail 3, gói mô tả — chờ chủ dự án |

| **G2** | **CHỜ CHỦ DỰ ÁN** (phiếu L3) | `gates/G2.md`, `gates/REVIEW-G2.md`, `review-g2/` | sau G2: G3 Release `ep005-v1` (§ G3) |

## 2. Phiên sau đọc (sau Mốc V merge)
`decisions/D-009.md` · đặc tả nhịp Mốc V (README/playbook do Mốc V ghi) · `CHARTER.md` · `playbook/episode.md` · `playbook/prompts/P3.md` · `episodes/ep005/PLAN.md` · `ledger.md` · `gates/G1.md` + trả lời G1 · `story/script.md` · `story/beats.md` · `episode.yaml` · `toolkit/factory/README.md`.

## 3. Việc treo
- **Câu 75 % — XONG (chủ dự án chọn (i), 2026-10-06):** S03.3 "Removal on today's value, when you ask, is the loan owner's rule; for Fannie Mae loans, that's two years and a 75 percent bar." · S12.3 "…the 75 percent bar Fannie Mae sets for its loans when a borrower asks to cancel on today's value, a separate route from the law's schedule." · S12.4 "that early bar". Sinh lại S03, S12; ASR 0 mất; móc thật M1 2,8 · M2 22,8 · M3 9,0 · **M4 9,71 s (±5 % quanh 10, nêu tên)** · M5 29,2 → ĐẠT; clip `review-g1/cold-open.m4a` cập nhật. **Ngoại lệ có tên:** S03 có 3 số mới (80 %, hai năm, 75 %) > 2 của story §3 — chữ do chủ dự án chỉ định; xem lại khi chuyển sang đặc tả Mốc V (ví dụ đưa "two years" lên nhãn hình).
- **S18.5 "illustrative" — XONG:** seed 1005 ASR "illustrated" (0,42/0,49); sinh lại cùng chữ seed **1006** "illustrative" 0,78/0,82 (chọn), 1007 0,62/0,65 (`review-g1/s18-seeds.json`). Không đổi chữ. **Việc cho Mốc V/nhà máy:** `build.py` dùng một seed cho cả tập → cần đọc `episode.yaml` `voice_overrides` (S18 seed 1006), nếu không nhà máy lấy lại take seed 1005.
- Freddie Mac Guide 8203.2 chưa kiểm (proxy chặn); claim chỉ dựa B-8.1-04.
- **`out/claims.json` phải ghi giá trị CHƯA làm tròn** (S05 sai số 0,005; với số làm tròn của numbers.md trượt 4 claim: % đổi chỉ số của 3 người mua + đỉnh–đáy). `contract.json` `pending`: điền màu/hình/bên nhân vật, `sonification.bandsHz`, `rights.visual` khi có thiết kế Mốc V; đề xuất `claims.conditions` "on paper" (18 claim), core/decisive, scenario `ten-percent-down` chờ duyệt ở C4.
- B06 (REVIEWER R1, THAM KHẢO): chip $2,362 dính liền nhãn "principal + interest".
- Hàng chờ G2 (CHÍNH không đổi nghĩa): `REVIEW-C2.md` K-3…K-14; câu 3 vòng 2 C2.
- `episode.yaml` chưa có `scenes/acts/midrolls/counterweights` cho nhà máy (thêm ở C4); `midrolls` theo giọng thật (ước ≈ 3:26 sau S09.4).
- So headless ↔ `Explore`: cảnh mất chú ý khác nhau → câu hỏi mở cho tổng kết Tập 5.

## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-07 (C5): **DỪNG chờ chủ dự án** (CHẶN trong hình khoá nghĩa). Dựng: `bash toolkit/build.sh episodes/ep005/episode.yaml` (res 1080, cache theo cảnh) → `python3 episodes/ep005/c4/build_inputs.py --out` → Shorts `cp work/factory/SH*.mp4 out/shorts/` → `bash episodes/ep005/c5/review_copies.sh` → checks `bash episodes/ep005/c5/checks.sh <thư mục tạm> --baseline episodes/ep005/out/checks/run-c4/report.json` (≈ 75 phút trang). Thumbnail: `NODE_PATH=$(npm root -g) node episodes/ep005/design/g2/thumbs.js`.
2026-10-07: **DỪNG chờ C3.** Đoạn thế giới: `python3 toolkit/factory/world/build_seg.py episodes/ep005/world/<đoạn> --res 540` (cache theo băm; vendor three.js: `npm ci` trong `toolkit/factory/world/vendor`). Cổng gốc: `python3 episodes/ep005/c3/root_run.py read|grade …`. Sau C3: BACKLOG F-5 → F-2 → F-3 → F-1 (thử 1 lần chuyển) → C4.
2026-10-06 (sau G1): **DỪNG chờ Mốc V.** Nhánh `ep005`. Lời theo cảnh: `python3 episodes/ep005/story/voice_scenes.py --skip S03,S12` (cache theo băm chữ; chỉ sinh cảnh đổi chữ; báo cáo `review-g1/voice-scenes.json`). Câu 75 % và S18 đã xong; đổi chữ cảnh nào thì `voice_scenes.py --only Sxx` (S18: `s18_seeds.py`, seed 1006), cảnh S01–S04 đổi thì chạy lại `table_read.py`.
2026-10-06: **DỪNG ở G1.** Tái tạo: `python3 episodes/ep005/data/fetch.py --verify && python3 episodes/ep005/model/model.py && python3 episodes/ep005/model/statements.py --all && python3 episodes/ep005/story/check_script.py`. Đọc thử: `python3 episodes/ep005/story/table_read.py` (take ở `voice-takes/`, không sinh lại khi chữ không đổi; cần `pip install av==14.2.0` cho faster-whisper). Kiểm mù: `python3 episodes/ep005/blind.py read|grade …`.

## 5. KPI + token so trần (tới G1)
| Loại việc | Thực | Trần | Ghi chú |
|---|---|---|---|
| Kiểm mù | ≈ 0,30 tr (headless 0,19 + `Explore` so 0,11) | 0,6 | 26 lượt headless |
| Dựng | ≈ 0,25 tr | 0,75 | Việc 0 + bổ sung nguồn |
| WRITER | ≈ 0,31 tr | 0,4 | **78 %** — giai đoạn dựng chỉ còn ≈ 0,09 |
| REVIEWER | ≈ 0,12 tr + G1 | 0,45 | |
| Checks | ≈ 0,07 tr | 0,15 | kiểm độc lập |
| Điều phối | ≈ 0,3 tr | 0,5 | |
| **Cộng** | **≈ 1,45 tr** | 3,0 | agent 12/40; EL 1.644/6.000; chủ dự án: G1 |

**Sau G1 (2026-10-06):** lời theo cảnh **20/20** trong `voice-takes/` (≈ 7:12 lời); EL cả tập **8.735/6.000 (+46 %)** (S03/S12 sinh lại 938, S18 hai seed 1.266) — D-009: không cắt chất lượng vì trần; nêu tên. Agent 12/40 (không thêm agent sau G1).

**C5 (2026-10-07):** giờ render 1080p: đoạn thế giới một lượt 1,48 h (a 0,22 · b 0,40 · c 0,50 · d 0,36) + d dựng lại 0,36 h (sửa nhật ký chữ lúc tối dần, điểm ảnh không đổi) + Shorts 0,26 h; tổng đồng hồ các lần build 3,8 h; trang kiểm checks 1,3 h. EL 0 ký tự.

## G3 — kế hoạch giao file (chủ dự án 08/10)
Sau G2 duyệt: GitHub Release tag **`ep005-v1`** (repo public) chứa master 1080p, Shorts, thumbnail, `captions.srt`, mô tả + **SHA256SUMS** (mỗi file < 2 GiB). Cách: REST API (`POST /repos/HungQuach301/crux-lab/releases`, tải tệp lên `uploads.github.com`) — proxy đính token GitHub App (quyền push/admin, kiểm 08/10 bằng GET chỉ đọc); `gh` CLI không dùng được (token phiên không hợp lệ). Sau khi đẩy: tải ngược từ link công khai `https://github.com/HungQuach301/crux-lab/releases/download/ep005-v1/<file>` → `sha256sum -c SHA256SUMS` → ghi kết quả vào `HUONG-DAN-DANG.md`. Không tạo được (quyền/proxy) → quay về nhánh tạm + phần 90 MB như Tập 4 (`toolkit/deliver/deliver.py`), báo lý do.

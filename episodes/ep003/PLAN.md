# PLAN — Tập 3 (playbook v2)

Nhánh: `ep003` (từ `main` `c0376d1`). Chỉ P3 merge `ep003` vào `main`. Khung: `playbook/quality-framework.md` v2; sổ tay: `playbook/episode.md`.

**Đề tài:** `topics/queue.md` #7 — "Savings Bonds That Double in 20 Years vs T-Bills" — hồ sơ `topics-r1/machine/retire-4/` (chủ dự án chỉ, 2026-10-04). Trụ: hưu trí (tập đầu của trụ). Mô hình: **kind mới** — đặc tả `retire-4/model.json → newKindNeeds` (nhãn làm việc `lock-vs-roll-replay`, tham số hoá để retire-3 dùng lại; **tên kind và params do phiên K quyết**).

## 1. Bảng cổng và quyết định

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Hồ sơ đạt `topic-dossier.md` | XONG — `retire-4/dossier-check.md` 4/4; commit `43350f3` | — | — |
| Việc 0 | XONG — SHA trùng; kiểm độc lập 873/873 cửa sổ, 36/36 đại lượng; retire-3 11/11 qua cùng mô hình | `numbers.md` | — |
| C1 (GU) | XONG (vòng 1) | `gates/C1.md`, `gates/C1-blind.md`, issue #26 | A + A1; giả định (a) trong cold open + nhãn hình; ghim 8/2026; lãi EE 2.40% V1 "for bonds issued May–October 2026" |
| C2 (TỰ ĐỘNG) | **XONG — QUA vòng 1** (máy ĐẠT; 6/6, khuyên 0); issue #28; phân loại nhịp #27 | `gates/C2.md`, `gates/C2-blind.md` | cấu trúc + cold open bản tạm → C3 |
| Giao phiên K | **XONG — khoá K3.7 có** (LOCK `a20c6878…`, kind `lock-vs-roll-replay`, `main` `ab7879e`, merge vào nhánh tập `d806f75`); S01/S05 trên bản sao khoá 0 lệch | `contract.json`, `review-k37/` | chủ dự án duyệt K3.7 (05/10) |
| C3 (GU) | **XONG** (issue [#31](https://github.com/HungQuach301/crux-lab/issues/31)) | `gates/C3.md`, `C3-tally*.md`, `C3-blind.md` | (a) cấu trúc C2 + Dana; lời chỉ 3.47; ký hợp đồng hình (A); bộ đo câu khuyên mới + hiệu chuẩn âm/dương trước C4; Eric + style C |
| C4 (TỰ ĐỘNG) | **XONG — QUA vòng 1**: hiệu chuẩn bộ đo khuyên đạt (âm 0/3, dương 3/3); nghĩa 6/6 nhịp loại 1, khuyên 0/14; checks đủ bộ lần 1: 19 PASS / 21 FAIL / 42 MISSING (TRƯỢT, dự kiến ở animatic) | `gates/C4.md`, `C4-tally.md`, `C4-cal-tally.md`, `review-c4/checks-run1/` | — |

## 2. Phiên sau đọc (P3: C5 → C6 → giao hàng)
1. `episodes/ep003/gates/C4.md` (kết quả C4 + danh sách CHẶN/MISSING phải xử lý ở C5)
2. `episodes/ep003/review-c4/checks-run1/report.md` (checks đủ bộ lần 1)
3. `episodes/ep003/animatic/timing.json` + `animatic/voice.py` (lời theo cảnh; chỉ sinh lại cảnh đổi chữ)
4. `episodes/ep003/design/c3/src/scenes.js` (`ANIM` + shot; trang `page.html?k=ANIM&r=anim`) + `design/c3/render.js` (`--from/--to`)
5. `episodes/ep003/audio_src/mix_full.py` + `animatic/mix-report.json` (nhạc style C đã duyệt)
6. `episodes/ep003/contract.json` + `checks/CONTRACT.md` (mục artefact, hợp đồng trang `window.CHECKS`)
7. `episodes/ep003/story/script.md` (S03.1 "T-bill" — A14)
8. `episodes/ep003/gates/C3.md` (chữ đã đổi, cho gói C6)

## 3. Việc treo
- **C5 (P3) — việc CHẶN từ checks lần 1** (`gates/C4.md` §C): A14 "T-bill" S03.1; trang dựng thêm hợp đồng `window.CHECKS` + `design/tokens.json` (mọi luật trang, S02/S07–S09/C07); render 1080p (F01/F04/F05/F06); phụ đề chia dòng/cue (F09); `out/package/description.md`, `artefacts.M3`, `out/rights.json` (F10–F12); `data.crosscheck` TB3MS vs DTB3 (S03/S04); `coverage` (S06). Sửa chỉ trong danh sách §6; chữ/lời người xem thấy đổi → gói C6.
- **C6:** lãi EE công bố 1/11/2026 (claim `ctx_ee_rate`); 3 thumbnail qua claim-risk; chữ đã đổi ở C3/C4.
- **Tổng kết tập:** đề xuất playbook — tách câu hỏi nghĩa (tắt tiếng) / khuyên (có lời), câu khuyên không dẫn dắt, hiệu lực bộ đo bằng đối chứng âm/dương (chủ dự án C3).
- **C4 áp ngay khi có quyết định:** đổi nhãn "Not a pick. What history did." → "Not a pick. Real rates, what-if bond." (claim-risk, REVIEWER C3); lời S06.6 không dùng nguyên câu "what history did".
- **`contract.json` còn thiếu** (C4/C5): `data.crosscheck` (TB3MS vs DTB3 trung bình ngày, S04), `coverage`, `sonification`, `artefacts`, `rights`; luật canh nhãn giả định từng khung chưa có trong khoá (issue #29 — S02 canh nhãn xuất hiện).
- **(đã xong ở P2)** Cho C3 (bắt buộc, lệnh chủ dự án 04/10): cần **ít nhất một ký hiệu mới** cho ý "gấp đôi / sức mua" — không lặp hình Tập 2 (V1 lưới ô chạy lại, V3 đường lãi so vạch, dãy núi TB3MS đều đã dùng cho cùng chuỗi TB3MS ở Tập 2). Ứng viên chưa có trong thư viện: bội số tiền "×2" như một vạch đích; sức mua của gấp đôi (giỏ hàng co/giãn). C3 thiết kế mới, kiểm cổng gốc.
- **Giả định "nếu khi đó đã có bảo đảm"** cho mọi cửa sổ trước 5/2005: nói bằng lời và hiện trên hình **ngay từ đầu (cold open, trước mọi số lịch sử)** (claim `ctx_hypothetical`); WRITER và C3 nhận làm luật của tập.
- ~~Khoá K của tập~~ — xong (K3.7).
- ~~Phối nhạc~~ — clip ≤ 60 s xong ở P2 (`review-c3/music-clip.*`). Ghi chú cũ: chưa làm ở P1 — engine Tập 2 `episodes/ep002/audio_src/mix.py` (style C, G-016 · chọn) cần mốc thời gian animatic/tempo map; P2 dựng clip phối ≤ 60 s trên table read + đo T2 (`toolkit/audio/d_music_selfsim.py`, tham khảo; Tập 2 19,7%).
- **Gói C3 phải liệt kê:** sửa ghi chú hình S05.5–S05.7 (§6.6: "52.3% overall" + "small sample · one era" cùng hiện với "0 of 17"); tên nhân vật Dana (ILLUSTRATIVE) là gu; đề xuất lời chỉ giữ 3.47, 3.53 lên hình (6/6 người đọc vấp).
- **P3/C6:** trước phát hành cập nhật lãi EE công bố **1/11/2026** (một claim `ctx_ee_rate`; kết quả lịch sử không đổi). Lời/hình luôn ghi "for bonds issued May–October 2026".
- Ghim dữ liệu August 2026 (chủ dự án C1); TB3MS 9/2026 = 3.94% không dùng.

## 4. Điểm dừng an toàn
- 2026-10-05 (P2): **P2 XONG.** C3 (#31) và C4 (qua vòng 1, issue C4) xong; checks lần 1 lưu `review-c4/checks-run1/`. **Dừng.** P3 bắt đầu khi PLAN ghi "P2 xong" (đã ghi). Tái lập animatic: `fetch.py --verify` → `model.py` → `claims.py` → `animatic/voice.py` (S02 sinh lại nếu mất take: ~0,8 k ký tự EL) → `design/c3/build_data.py` → server `python3 -m http.server 8765` ở gốc repo → `node design/c3/render.js ANIM --from a --to b` (4 đoạn) → `audio_src/mix_full.py` → ghép (lệnh ở ledger 02:20) → `animatic/artefacts.py`.
- 2026-10-05 (P2, C4): C3 xong; ý đồ C4 v2 commit. Đang: hiệu chuẩn (`review-c4/cal/`, 3 + 3 người đọc) → animatic (`animatic/voice.py` → `timing.json`; chỉ S02 sinh lại). Nếu mất container: `fetch.py --verify` → `model.py` → `claims.py` → `design/c3/build_data.py` → `design/c4/ctrl/build_ctrl.py` → `animatic/voice.py` (take S02 không commit; sinh lại tốn ~0,4 k ký tự EL).
- 2026-10-05 (P2): **gói C3 gửi (sau REVIEWER), DỪNG chờ chủ dự án** (3 câu). Nhánh làm việc `ccr-806b9e1b-ju4ok5` (= `ep003` + P2; `ep003` trên remote chưa cập nhật — đẩy/merge khi chủ dự án cho phép). Tái lập: `python3 episodes/ep003/data/fetch.py --verify && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/claims.py && python3 episodes/ep003/design/c3/build_data.py`; style frame: `python3 -m http.server 8765` ở gốc repo + `NODE_PATH=$(npm root -g) node episodes/ep003/design/c3/render.js KEY1 … [--r2] [--check]`; dải/mẫu: `python3 episodes/ep003/review-c3/make_c3.py [--round 2]`; checks: bản sao `git archive` + `python3 checks/py/run.py episodes/ep003 --only S01,S05 --first`.
- 2026-10-04 (4): **P1 XONG.** C2 qua vòng 1 (issue #28), phân loại nhịp #27, giao phiên K #29, table read 3 911 ký tự. **Dừng.** P2 bắt đầu khi PLAN ghi "P1 xong" (đã ghi): C3 không cần khoá K; C4 cần khoá K đã merge `main`. Tái lập: `python3 episodes/ep003/data/fetch.py --verify && python3 episodes/ep003/model/model.py && python3 episodes/ep003/story/check_script.py`.
- 2026-10-04 (3): C1 xong. Đang: WRITER (`story/WRITER-brief.md`). Nếu mất: giao lại WRITER cùng đầu bài → `python3 episodes/ep003/story/check_script.py` → kiểm mù C2 theo `gates/C2-intent.md`.
- 2026-10-04 17:50 (2): **gói C1 gửi (sau REVIEWER), issue [#26](https://github.com/HungQuach301/crux-lab/issues/26). DỪNG chờ chủ dự án** (3 câu). Sau khi trả lời: ghi `taste-ledger.md`, `AUTHORSHIP.md` (trên `ep003`) + ledger; giao WRITER (đầu bài `episode.md` §3 + luật tập: giả định trước 5/2005 nói bằng lời thường **trong cold open, trước mọi số lịch sử** (theo quyết định câu 2) + nhãn hình; không đặt 3.72% cạnh 3.53% mà không chú giải; mốc 17 tháng luôn kèm "mẫu ngắn" + tỉ lệ toàn kỳ) → C2.
- 2026-10-04 17:10 (1): hồ sơ + Việc 0 xong. Đang: REVIEWER soát ý đồ C1 → kiểm mù C1 (`review-c1/`, manifest T/G/titles). Nếu mất container: `python3 episodes/ep003/data/fetch.py --verify --retire3 && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/model.py --retire3`.

## 5. KPI tạm (cuối P2)
- Chủ dự án tham gia: **2** (C1, C3) + 1 chỉ dẫn ngoài cổng (lệnh K3.7 khi phiên đang chạy, không dừng chờ). Mục tiêu Tập 3: 3 + xác nhận tải.
- Vòng: C1 **1** · C2 **1** · C3 cổng gốc **2** (trượt vì câu khuyên → quyết định chủ dự án) · hiệu chuẩn **1** · C4 **1** (qua, không dự phòng).
- Lượt agent: **131** = P1 55 + P2 76 (nhạc 2: clip C3 + âm tạm toàn tập; REVIEWER 4: ý đồ C3, gói C3, ý đồ C4, báo cáo/issue C4; WRITER 1; người đọc mù C3 32 + hiệu chuẩn 6 + C4 26 = 64; người chấm độc lập C3 2 + hiệu chuẩn 1 + C4 2 = 5; render/checks chạy lệnh trực tiếp).
- Ký tự ElevenLabs: **4 733** = 3 911 (P1) + 822 (P2: S02 hai seed).
- Thời gian: P2 2026-10-04 23:40 UTC → gói C3 2026-10-05 ~00:55 → C3 trả lời → C4 qua ~02:45 → P2 xong.
- Token: không đọc được.

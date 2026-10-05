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
| C4 (TỰ ĐỘNG) | **ĐANG** — ý đồ v2 (sau REVIEWER) → hiệu chuẩn bộ đo khuyên → animatic → cổng gốc → checks đủ bộ lần 1 | `gates/C4-intent.md` | — |

## 2. Phiên sau đọc (P2 tiếp, sau trả lời C3: áp quyết định → C4)
1. `episodes/ep003/gates/C3.md` (gói, 3 câu + phương án A/B/C cho cổng gốc) + câu trả lời của chủ dự án (issue #31)
2. `episodes/ep003/gates/C3-intent.md` (ý đồ v2) và `gates/C3-tally-r2.md`
3. `episodes/ep003/story/script.md` + `story/beats.md` (C4 sửa S02.7/S08.4 nếu câu 1.2 duyệt)
4. `episodes/ep003/design/c3/src/scenes.js` (style frame, `?r=2` = nhãn vòng 2) + `design/c3/render.js`
5. `episodes/ep003/contract.json` + `checks/CONTRACT.md` (hàng `lock-vs-roll-replay`, mục artefact) — C4 cần `out/timeline.json`, `script.json`, stem…
6. `episodes/ep003/numbers.md`
7. `episodes/ep003/review-c3/music-clip.json` + `audio_src/mix_c3clip.py` (engine nhạc cho animatic)
8. `episodes/ep003/review-c2/table-read.json` (take theo hash chữ; chỉ sinh lại cảnh đổi chữ)

## 3. Việc treo
- **Hiệu chuẩn bộ đo khuyên (C4 §A):** không đạt (ÂM > 1/3 hoặc DƯƠNG < 2/3) → dừng, mở issue báo chủ dự án.
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
- 2026-10-05 (P2, C4): C3 xong; ý đồ C4 v2 commit. Đang: hiệu chuẩn (`review-c4/cal/`, 3 + 3 người đọc) → animatic (`animatic/voice.py` → `timing.json`; chỉ S02 sinh lại). Nếu mất container: `fetch.py --verify` → `model.py` → `claims.py` → `design/c3/build_data.py` → `design/c4/ctrl/build_ctrl.py` → `animatic/voice.py` (take S02 không commit; sinh lại tốn ~0,4 k ký tự EL).
- 2026-10-05 (P2): **gói C3 gửi (sau REVIEWER), DỪNG chờ chủ dự án** (3 câu). Nhánh làm việc `ccr-806b9e1b-ju4ok5` (= `ep003` + P2; `ep003` trên remote chưa cập nhật — đẩy/merge khi chủ dự án cho phép). Tái lập: `python3 episodes/ep003/data/fetch.py --verify && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/claims.py && python3 episodes/ep003/design/c3/build_data.py`; style frame: `python3 -m http.server 8765` ở gốc repo + `NODE_PATH=$(npm root -g) node episodes/ep003/design/c3/render.js KEY1 … [--r2] [--check]`; dải/mẫu: `python3 episodes/ep003/review-c3/make_c3.py [--round 2]`; checks: bản sao `git archive` + `python3 checks/py/run.py episodes/ep003 --only S01,S05 --first`.
- 2026-10-04 (4): **P1 XONG.** C2 qua vòng 1 (issue #28), phân loại nhịp #27, giao phiên K #29, table read 3 911 ký tự. **Dừng.** P2 bắt đầu khi PLAN ghi "P1 xong" (đã ghi): C3 không cần khoá K; C4 cần khoá K đã merge `main`. Tái lập: `python3 episodes/ep003/data/fetch.py --verify && python3 episodes/ep003/model/model.py && python3 episodes/ep003/story/check_script.py`.
- 2026-10-04 (3): C1 xong. Đang: WRITER (`story/WRITER-brief.md`). Nếu mất: giao lại WRITER cùng đầu bài → `python3 episodes/ep003/story/check_script.py` → kiểm mù C2 theo `gates/C2-intent.md`.
- 2026-10-04 17:50 (2): **gói C1 gửi (sau REVIEWER), issue [#26](https://github.com/HungQuach301/crux-lab/issues/26). DỪNG chờ chủ dự án** (3 câu). Sau khi trả lời: ghi `taste-ledger.md`, `AUTHORSHIP.md` (trên `ep003`) + ledger; giao WRITER (đầu bài `episode.md` §3 + luật tập: giả định trước 5/2005 nói bằng lời thường **trong cold open, trước mọi số lịch sử** (theo quyết định câu 2) + nhãn hình; không đặt 3.72% cạnh 3.53% mà không chú giải; mốc 17 tháng luôn kèm "mẫu ngắn" + tỉ lệ toàn kỳ) → C2.
- 2026-10-04 17:10 (1): hồ sơ + Việc 0 xong. Đang: REVIEWER soát ý đồ C1 → kiểm mù C1 (`review-c1/`, manifest T/G/titles). Nếu mất container: `python3 episodes/ep003/data/fetch.py --verify --retire3 && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/model.py --retire3`.

## 5. KPI tạm (giữa P2, trước C4)
- Chủ dự án tham gia: **2** (C1, C3). Lệnh K3.7 (05/10) đến khi phiên đang chạy, không phải lần dừng chờ.
- Vòng: C1 **1** · C2 **1** · C3 cổng gốc **2** (trượt vì câu khuyên; dự phòng không áp được → gói).
- Lượt agent: **95** = P1 55 + P2 40 (nhạc 1; REVIEWER 3: ý đồ C3, gói C3, ý đồ C4; WRITER 1; người đọc mù 32; người chấm độc lập 2).
- Ký tự ElevenLabs: **3 911** (P2 không sinh giọng mới; clip giọng/cold open cắt từ table read C2).
- Thời gian: P1 2026-10-04 16:40 UTC → P1 xong; P2 bắt đầu 2026-10-04 23:40 UTC → gói C3 2026-10-05.
- Token: không đọc được.

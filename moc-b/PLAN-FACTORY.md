# PLAN — phiên nhà máy (tiếp Mốc B: thư viện mẫu, một lệnh dựng, Shorts, LFS)

Chủ dự án chuyển phần này sang phiên riêng (D-006 bổ sung 2, 05/10/2026). Phiên đó **đọc file này**, `CHARTER.md`, `playbook/episode.md` §5, §6, §9, `playbook/story.md` §4–5 và `toolkit/visual-library/README.md`. Không đọc tập cũ, trừ các file được nêu dưới đây.

**Trần token đề xuất:** 0,6 triệu, gồm ≤ 2 agent con (REVIEWER + 1 kiểm độc lập); mỗi agent con ≈ 44 nghìn token cố định. **ElevenLabs:** ≈ 0,8 nghìn ký tự (demo S04).

## 1. Trạng thái (dở, trên `main` sau khi `moc-b` merge)
| File | Có gì | Chưa |
|---|---|---|
| `toolkit/factory/lib/engine.js` | Engine canvas 2D ngang 1920×1080 / dọc 1080×1920, ra 1080p hoặc 720p. Tự áp chuẩn và ghi log cho qc: sàn chữ tự nâng (40 px ngang, 56 px dọc, tính cả zoom), tương phản ≥ 4,5:1 (đổi màu → thêm nền), dời vào vùng an toàn, nhãn không đè (đẩy dọc, còn đè thì ghi collision), nhãn ILLUSTRATIVE và "US only · history, not a forecast" tự gắn theo cờ claim, đẩy máy chậm 1,5 %/cảnh để không khung nào đứng yên khi lời chạy. `E.CL(id)` và `{claimId}` trong chuỗi | **Chưa chạy lần nào** (chưa có page.html, chưa test) |
| `toolkit/factory/lib/templates.js` | 10 mẫu tham số hoá: `title`, `bignum`, `bars` (trục luôn từ 0), `line` (mức cố định đứng yên, phần vượt màu warn), `swarm` (Tập 3 "đàn chấm về đích" + V1), `paths` (KEY-1), `timeline` (vùng giả định gạch chéo), `method` (V7), `person`, `endcard`. Mọi mốc là giây tính từ đầu cảnh, do build.py giải từ "@từ" | Chưa chạy; vị trí cho khổ dọc mới ước |

Mã viết mới, chỉ lấy ý tưởng từ engine Tập 2–3 (`episodes/ep003/design/c3/src/engine.js`, `scenes.js`), không chép nguyên.

## 2. Việc còn lại (theo thứ tự)
1. **`toolkit/factory/page.html` + `render.js`**:
   - Playwright, mỗi worker một trang;
   - khung trung gian **JPEG q 0,95** thay cho RGBA base64 (đo trước/sau trên cùng cảnh ep003 1080p, ghi `moc-b/SPEED.md`);
   - render song song **chỉ đoạn đổi**: băm = đặc tả đoạn + mốc đã giải + băm mã mẫu + dữ liệu;
   - log khung mỗi 6 khung cho qc.
2. **`episodes/epNNN/episode.yaml` + `toolkit/factory/spec.py`** (kiểm đặc tả):
   - `format: lab|101` (thời lượng tối đa cứng, tối thiểu mềm cho 101: "không độn");
   - `midrolls` (lab 2, 101 1; ở ranh giới hồi, khoảng lặng ≥ 1 s; không trong 120 s đầu/cuối);
   - `scope: excerpt` bỏ qua luật thời lượng/mid-roll;
   - claim tồn tại trong `out/claims.json`;
   - `custom_symbols` ≤ 2 (vượt → ngoại lệ, hỏi chủ dự án);
   - `shorts` 2–3.
3. **`toolkit/factory/voice.py`**:
   - ElevenLabs `with-timestamps` (Eric `cjVigY5qzO86Huf0OWal`, `eleven_v3`, seed cố định), lời chuẩn hoá qua `toolkit/voice/normalize.js`;
   - **cache theo SHA-256 (văn bản nói + voice + model + seed)**;
   - căn ký tự → mốc từ.
4. **`toolkit/factory/build.py` + `toolkit/build.sh <episode.yaml>`**: kiểm đặc tả → giọng (cache) → giải "@từ" thành giây (hình không đi trước lời) → `timeline.json` + `captions.srt` → render song song đoạn đổi → mix (lời + nhạc tuỳ chọn, ducking, loudnorm 2 lượt −14 LUFS / ≤ −1 dBTP) → master (concat copy) → **3 phần 720p ≤ 90 MB** cắt ở ranh giới cảnh gần 1/3 và 2/3 → Shorts.
5. **Shorts** (`shorts:` trong yaml):
   - render lại các cảnh trong khoảng thời gian ở khổ dọc;
   - lời cắt từ master;
   - dòng móc trên đầu, thẻ cuối 1,5 s;
   - ≤ 60 s;
   - sàn chữ dọc 56 px;
   - vùng an toàn dọc;
   - ILLUSTRATIVE / history tự gắn.
6. **`toolkit/factory/qc.py`** (luật làm việc của bên dựng, không thay `checks/`), mỗi mục ĐẠT/TRƯỢT, ghi tên mục sát ngưỡng ±5 %:
   - sàn chữ;
   - tương phản;
   - vùng an toàn;
   - va chạm nhãn;
   - nhãn ILLUSTRATIVE / history;
   - trục từ 0;
   - `freezedetect` d=3 giao với khoảng có lời = 0;
   - mốc hình ≥ mốc từ;
   - loudness;
   - kích thước phần;
   - thời lượng Short;
   - luật `format`.
   Gửi K qua `checks-appeal.md`.
7. **Demo một lệnh:** `episodes/ep003/episode.yaml` (`scope: excerpt`, cảnh **S04 "The replay"**, 71 s, 785 ký tự lời; mẫu `swarm` trên `window.DATA.windows[].roll` với cổng `ctx_guarantee`; dữ liệu dựng bằng `fetch.py --verify → model.py → claims.py → design/c3/build_data.py`; lưu ý `model.py` cần `topics-r1/machine/retire-4/data/` có `TB3MS.csv`, `CPIAUCNS.csv`). Một Short S04.4–S04.7. Ghi thời gian, bảng qc.
8. **Git LFS** cho master trên nhánh `release-epNNN`: kiểm hạn mức LFS của tài khoản trước (không đọc được thì dừng ở thử nhỏ: demo master vài MB); đẩy, tải ngược, so SHA. Vượt hạn mức hoặc proxy chặn LFS → giữ cách phần 90 MB.
9. **Tốc độ render** trước/sau → `moc-b/SPEED.md`.

## 3. Điểm dừng an toàn
Sau mỗi việc ở §2: commit lên nhánh của phiên. Lệnh tái lập dữ liệu Tập 3 ở `episodes/ep003/PLAN.md` mục 4.

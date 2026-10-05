# C4 — Ý đồ: hiệu chuẩn bộ đo câu khuyên + cổng gốc animatic (ghi TRƯỚC khi chạy, commit trước; không sửa sau khi thấy kết quả)

Ngày 2026-10-05. **Bản 2 — sửa theo REVIEWER trước khi chạy** (1 CHẶN, 6 CHÍNH, 5 THAM KHẢO; bản 1 `b4a2ad8`). Nguồn thẩm quyền: quyết định C3 của chủ dự án (issue #31, ghi nguyên văn ở `ledger.md` 2026-10-05 và `taste-ledger.md` "Tập 3 · C3"), `quality-framework.md` v2 §4 (C4), §5. Bộ đo câu khuyên **mới** do chủ dự án đặt; phiên chỉ thực thi, không thêm tiêu chí. Nguyên văn trả lời: `gates/C4-blind.md`; gộp: `gates/C4-cal-tally.md`, `gates/C4-tally*.md`.

## A. Hiệu chuẩn bộ đo câu khuyên (trước C4; tiêu chí chủ dự án)

**Câu hỏi khuyên (nguyên văn chủ dự án):** *"Does this clip suggest the viewer should DO anything? If yes, what? If no, write 'no action'."*

**Rubric khuyên (ý chủ dự án, dịch cho người chấm; các ví dụ chỉ minh hoạ "chọn / mua / khoá / tránh"):** `advice = true` **chỉ khi** câu trả lời nêu một **hành động hướng tới người xem**: chọn / mua / khoá / tránh một sản phẩm hay lựa chọn tài chính (ví dụ "buy the bond", "lock in the rate", "keep rolling T-bills", "avoid cash", "move money into stocks/TIPS"). **Không tính:** "lịch sử cho thấy X" (mô tả kết quả), "tuỳ hoàn cảnh / it depends / compare your own situation", "no action", lời nhắc cách đọc số liệu.

**Dạng mẫu "clip có tiếng".** Người đọc agent không xem được video và không nghe được tiếng. "Clip có tiếng" được trao bằng **một PNG** gồm dải 6 khung (như cổng gốc, giữ chữ/số) **và**, ngay dưới dải, **nguyên văn lời đọc** của đúng khoảng thời gian đó (khối chữ "Narration heard during this clip: …"). Dải không lời (tắt tiếng) dùng cho câu hỏi nghĩa. Đây là cách phiên hiểu "có tiếng"; REVIEWER soát trước khi chạy.

**Đối chứng (dựng trước, từ thư viện hình v1; `engine.js` chép nguyên văn trừ đường dẫn tokens):**
- **ÂM (trung tính):** V1 "lưới ô chạy lại" — `toolkit/visual-library/code/h3/scenes.js` `K5`, chép nguyên văn (`design/c4/ctrl/`), dữ liệu dựng lại từ TB3MS ghim (1954-01…, cửa sổ 120 tháng, cờ "vượt 9%" theo công thức ở đầu `scenes.js`). Lời (viết trước, trung tính, không số mới ngoài năm 1954): *"We took the same ten-year loan and started it in every month since 1954. Each square is one of those replays, placed under the month it started."*
- **DƯƠNG:** cùng dải, cùng lời, thêm nhãn **"Lock it in now"** (tier `head`, 72 px @1080, nền `surface`) hiện ở cả 6 khung.

**Người đọc:** 3 agent mới (sonnet) cho mỗi đối chứng, mỗi agent một PNG hex (`packets.py deal`). Câu hỏi gửi (chuỗi `question` của manifest): vai đích Tập 3 + câu khuyên mới, không câu nào khác:
> You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account or short-term Treasury bills. The image shows six numbered frames, in order, from a short animated clip in a personal-finance video, and below them the narration heard during the clip. Look only at the image. Does this clip suggest the viewer should DO anything? If yes, what? If no, write 'no action'.

**Chấm:** agent độc lập mù tập (sonnet), gói nhãn ngẫu nhiên (`packets.py packet`), khoá nhãn commit trước khi chấm; chỉ chấm `advice` theo rubric trên (điểm nghĩa = 0, không dùng). **Gói người chấm (REVIEWER CHẶN 1):** `packets.py packet` tự chèn trường `scale` mang định nghĩa khuyên CŨ → ngay sau `packet`, `review-c4/fix_packet.py` thay `scale` bằng đúng câu `rules` của rubric đang dùng; lời giao người chấm ghim nguyên văn ở `review-c4/judge-prompt.md` (chỉ thay đường dẫn gói). SHA của cả hai và của gói sau khi thay ghi vào `inputs.json` của lượt. Áp cho hiệu chuẩn và mọi lượt C4. Vùng mơ hồ nêu trước (không thêm luật): dạng rào đón "consider locking in" — người chấm tự quyết theo rubric; phiên ghi lại các trường hợp này trong issue.

**Đếm (REVIEWER CHÍNH 3):** `deal --slots 1,2,3` cho mỗi đối chứng (đủ 3 + 3, không dừng sớm); kết quả **chỉ đọc cột `advice`** của `tally` (NEG: số người bị cờ ≤ 1; POS: ≥ 2). Cột `status`/`verdict` của `tally` trên bộ `cal` vô nghĩa (điểm nghĩa luôn 0) và không dùng.

**Vì sao V1 làm đối chứng âm (§6.4, ghi một dòng ledger):** V1 là ký hiệu mạnh nhất của thư viện, mang nghĩa mô tả ("chạy lại từ mọi tháng"), không có lựa chọn hai phía như V4 (V4 có tiền sử khuyên 1/3 ở Tập 2 và 1–2/2 ở C3 Tập 3), nên hợp với "clip trung tính". **Giới hạn (ghi trong issue):** V1 là khoản vay (Tập 2, ILLUSTRATIVE) trong khi vai người đọc là người gửi tiết kiệm → NEG ≤ 1/3 chủ yếu chứng minh người chấm phân biệt được nhãn mệnh lệnh; chưa chứng minh bộ đo không cờ quá tay trên nội dung tiết kiệm trung tính. Lời đối chứng do phiên viết (trung tính, mô tả) — ghi ledger.

**Tiêu chí hiệu lực (chủ dự án):** ÂM **≤ 1/3** bị cờ **và** DƯƠNG **≥ 2/3** bị cờ → bộ đo mới **áp tự động** cho C4. Không đạt một trong hai → **dừng, mở issue báo chủ dự án**; không chạy C4 với bộ đo chưa hiệu lực. Không dừng sớm ở hiệu chuẩn (đủ 3 + 3).

## B. Cổng C4 (TỰ ĐỘNG) — animatic 720p toàn tập

**Đầu vào:** animatic toàn tập 720p (hợp đồng hình C3 đã ký), giọng Eric `eleven_v3` theo cảnh (take table read C2 cho cảnh không đổi chữ — cắt theo ranh giới cảnh đo bằng ASR, không giãn; sinh lại chỉ cảnh đổi chữ: S02, S08 theo câu 1.2), âm tạm (nhạc style C, engine `audio_src/`). Nhãn "Not a pick. What history did." đổi thành **"Not a pick. Real rates, what-if bond."** (C3 câu 1, claim-risk). Mọi nhịp then chốt mang nhãn đối trọng vòng 2 của C3.

**Mẫu:** mỗi nhịp KEY-1…KEY-7 lấy khoảng thời gian của nhịp trên animatic (`edit/timing.json`, ranh giới câu của nhịp theo `beats.md`), hai dạng từ cùng khoảng:
- **dải tắt tiếng** (`strips.py`) → câu hỏi **NGHĨA** = câu 1–3 của C3 (bỏ câu 4 cũ), rubric "đúng nghĩa" = cột muted read `beats.md` (giống C3 r1, SHA rubric ghi khi dựng); chỉ nhịp loại 1;
- **dải + lời** (dạng ở mục A) → câu hỏi **KHUYÊN** mới; cả 7 nhịp (KEY-3 loại 2 chỉ kiểm khuyên). **Chữ lời** của khoảng = các câu của `script.md` có mốc bắt đầu (căn bằng ASR mức từ trên **chính audio lời của animatic**, `animatic/timing.json`) nằm trong khoảng nhịp — tức là lời người xem nghe trong khoảng đó, không lấy cả cảnh. **Giới hạn (ghi trong issue):** mất ngữ điệu, nhạc và nhịp; chữ nổi hơn tiếng. Câu hỏi khuyên C4 **trùng từng ký tự** với `review-c4/cal/manifest.json` (SHA ghi trong `inputs.json`).
- Câu hỏi NGHĨA bỏ câu 4 cũ (lời khuyên) — trái §5.3 nhưng theo quyết định (c) của chủ dự án ở C3 (đo khuyên tách riêng trên clip có lời).

**Đếm và gộp (REVIEWER CHÍNH 2):** hai manifest/khoá riêng: `review-c4/rN/mean/` (6 nhịp loại 1, `tally --classes`; rubric lượt nghĩa ghi "advice: always false, not judged here" — cờ khuyên tự phát ở lượt nghĩa **không tính**) và `review-c4/rN/adv/` (7 nhịp; chỉ đọc cột `advice`/`advice_beats`, bỏ `verdict`). Bảng gộp `gates/C4-tally.md` dựng bằng script ghi trước (`review-c4/combine.py`): nhịp loại 1 đạt = nghĩa PASS ∧ khuyên 0; cổng = ≥ 5/6 nhịp đạt ∧ không nhịp nào (gồm KEY-3) có khuyên; ±5% nêu tên.

**Người đọc:** agent mới mỗi (nhịp, dạng, lượt). Dừng sớm §5.6 áp **riêng cho mỗi dạng**: nghĩa — 2 người đầu cùng kết quả thì dừng, lệch thì người thứ 3, đạt khi ≥ 2/3 điểm 1; khuyên — 2 người đầu cùng không cờ thì đạt, có cờ ở bất kỳ người nào thì nhịp trượt khuyên ngay.

**Ngưỡng C4 (§4, giữ nguyên):** một nhịp loại 1 **đạt** khi nghĩa ≥ 2/3 **và** khuyên 0 (trên dải + lời). Cổng **qua** khi ≥ **80%** nhịp loại 1 đạt **và** không nhịp nào (kể cả KEY-3) có câu khuyên. Bảng phân loại `story/beats-class.json` SHA `2299ddf5…` (không đổi). 6 nhịp loại 1: 80% ⇒ cần ≥ 5/6 (4/6 = 67% trượt). Kết quả 5/6 = 83% nằm **trong ±5% quanh ngưỡng** (`tally` tự in cờ) → nêu tên trong issue.

**Vòng và dự phòng (chủ dự án + §4):** tối đa **2 vòng**.
- Nhịp còn cờ khuyên → sửa theo gợi ý (C) của gói C3 (bỏ "Which path ends with more?" ở KEY-1; bỏ hình Dana cầm phong bì khỏi KEY-1, giữ ở lời; KEY-4/5/7 cổng ×2 vẽ như **thước**, không như đích; KEY-6 bỏ cột "×2 dollars" bên trái) **và** thêm câu đối trọng trong lời ở cảnh đó (WRITER, giữ nghĩa, claim đủ; chỉ sinh lại cảnh đổi chữ).
- Nhịp trượt nghĩa → nhãn nghĩa (≤ ~8 từ, ≥ 40 px @1080, ≥ 1 s/3 từ).
- Sau vòng 2 vẫn trượt → **ngoại lệ** (§4 C4): render, ghi điểm hai vòng vào ledger và gói C6.
- Người đọc mới ở mỗi vòng; câu hỏi, rubric không đổi giữa các vòng. **Vòng 1 = animatic gốc.** Vòng 2: nhịp **đã sửa** (hình theo (C) và/hoặc lời đối trọng) kiểm lại **cả nghĩa lẫn khuyên**; nhịp không đổi giữ kết quả vòng 1. Câu đối trọng mới: chạy lại `check_script.py` + claim, chỉ sinh lại cảnh đổi chữ, liệt kê cho gói C6 (§6.5).

**Checks đủ bộ lần 1 (cuối C4):** bản sao `git archive` + LOCK `a20c6878…` khớp; `python3 checks/py/run.py episodes/ep003 --first`; báo cáo `out/checks/report.json` lưu vào `review-c4/checks-run1/`. Artefact còn thiếu ở animatic (stem cuối, gói phát hành…) ghi MISSING kèm lý do trong issue C4; không sửa luật.

**Issue:** `[Cổng C4 · tự động] Tập 3 — qua/ngoại lệ` ≤ 5 dòng (REVIEWER soát trước). Không chờ.

## C. Đề xuất cho tổng kết tập (không áp ở Tập 3 ngoài C4)
Đưa vào playbook: tách câu hỏi nghĩa (tắt tiếng) / câu hỏi khuyên (có lời); câu hỏi khuyên không dẫn dắt; hiệu lực bộ đo bằng đối chứng âm/dương trước khi dùng.

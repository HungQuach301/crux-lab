# Sổ tay chạy một tập (playbook v2, 04/10/2026)

Áp từ Tập 3 (`decisions/D-005.md`). Khung: `playbook/quality-framework.md` v2. Prompt mẫu: `playbook/prompts/`. Một tập chạy bằng một dòng: **"Chạy Tập N, phiên P1"** (máy đề xuất đề tài ở C1) hoặc **"Chạy Tập N, đề tài #k, phiên P1"** (rồi P2, P3).

## 1. Ba phiên ngắn

| Phiên | Cổng | Bắt đầu khi | Kết thúc khi | Chủ dự án |
|---|---|---|---|---|
| **P1** | C1 (GU) → C2 (TỰ ĐỘNG) → giao phiên K | Có đề tài #k do chủ dự án chỉ, **hoặc** `topics/queue.md` có ≥ 1 đề tài với hồ sơ đạt `topic-dossier.md` | C2 qua (hoặc qua bằng dự phòng); issue C2 + issue phân loại nhịp đã mở; danh sách claim gửi phiên K | 1 lần (C1) |
| **P2** | C3 (GU) → C4 (TỰ ĐỘNG) | PLAN ghi "P1 xong". C3 không cần khoá K; **C4 cần khoá K** của tập đã merge `main` | Animatic qua C4 (hoặc ngoại lệ); checks đủ bộ lần 1 | 1 lần (C3) |
| **P3** | C5 (TỰ ĐỘNG) → C6 (GU) → giao hàng | PLAN ghi "P2 xong" | Chủ dự án tải xong bản giao; nhánh `epNNN-delivery` xoá; tập merge `main` | 1 lần (C6) + xác nhận tải |

- **Chọn đề tài nằm trong C1** (D-005 bổ sung), không thêm lượt tham gia. Khi prompt không nêu #k, P1 lấy tối đa 3 ứng viên từ `topics/queue.md` có hồ sơ đạt chuẩn. Thứ tự ưu tiên: (1) trụ nội dung ít tập nhất trước (đếm tập đã merge `main`: tới Tập 2 là vay nợ 2, hưu trí 0, thuế 0); (2) `model.kind` có sẵn trong `checks/`. Mỗi ứng viên dựng một logline. Câu hỏi đề tài và câu hỏi logline gộp làm một câu trong gói C1, kèm khuyến nghị và lý do. Chủ dự án được chọn đề tài ngoài danh sách. Máy không tự chọn (D-004); xét lại khi có số đo trễ YouTube của ≥ 3 tập từ đề tài máy.
- Mỗi tập một nhánh `epNNN` (từ `main`). Chỉ P3 merge `epNNN` vào `main` (fetch trước; trong file dùng chung chỉ sửa phần của tập).
- **Bàn giao qua `episodes/epNNN/PLAN.md`.** Cuối mỗi phiên, PLAN có đủ năm mục: (1) bảng cổng và quyết định; (2) **"Phiên sau đọc"**: danh sách file có tên, tối đa ~8 file; (3) việc treo; (4) điểm dừng an toàn và lệnh chạy tiếp; (5) KPI tạm (§8).
- **Phiên sau chỉ đọc** `CHARTER.md`, `quality-framework.md`, file này, `PLAN.md`, `ledger.md` và các file trong mục (2). Không đọc nguyên văn kiểm mù (`gates/*-blind.md`). Không đọc tập cũ, trừ file thư viện hình được nêu tên.
- Trước mỗi gói GU và mỗi issue TỰ ĐỘNG: giao **REVIEWER** soát (`quality-framework.md` §7). Kết quả soát in kèm gói.

## 2. Mô hình và effort

| Việc | Model | Effort |
|---|---|---|
| Điều phối (P1, P2, P3) | Opus | Medium |
| WRITER (treatment, beat sheet, kịch bản, sửa kịch bản) | Opus | Medium |
| REVIEWER | Opus | Medium |
| Tổng kết tập | Opus | Medium |
| Người đọc kiểm mù, người chấm độc lập | Sonnet | (mặc định) |
| Render, checks, mã hoá, ghép tiếng, sinh giọng | (agent con hoặc lệnh trực tiếp) | Low |

## 3. Đầu bài WRITER (từ C2) — luật thêm vào đầu bài mỗi tập

1. **Từ khó cho ASR:** không dải năm có gạch nối ("1954-1980" → "from 1954 to 1980"). Không "minus" và không số âm đọc lên ("−1 point" → "1 point above"). Không ký hiệu (%, ±, →) trong chỗ phải đọc thành chữ. Số tiền đọc rõ (lessons E6).
2. **Claim-risk áp cho câu NÊU số.** Câu đó kèm đủ điều kiện của claim-risk (ví dụ hai thời kỳ + xấu nhất). Câu **nhắc lại** gọi bằng lời, không nêu lại số. Mỗi tỉ lệ một dạng cố định cả tập (lessons E5).
3. **Câu đối trọng:** mỗi kết luận có một câu chặn suy diễn "X an toàn hơn / tốt hơn" (ví dụ: "That is not a reason to pick either loan; it is what history did for this pair of rates"). Không mệnh lệnh với người xem (lessons E4).
4. **Mật độ số** đọc liền nhau chỉ là chỉ số Tham khảo, không phải đích. Đoạn có ≥ 3 số liền nhau thì đưa bớt lên hình.
5. **Đoạn phương pháp mẫu = 1 câu lời + thẻ phương pháp + mô tả** (thư viện hình V7).
6. Bảng nhịp có cột **loại nhịp**: loại 1 "hình tự mang ý" (kèm một câu "ý người xem phải đọc ra khi tắt tiếng") hoặc loại 2 "hình minh hoạ lời". Gợi ý hình lấy từ thư viện (`toolkit/visual-library/README.md`) trước khi đề xuất ký hiệu mới.
7. Gen được bảo vệ và gu đã chốt: chép từ `CHARTER.md` §5 và `taste-ledger.md` (G-007…G-016). Không chép kịch bản tập cũ.

## 4. Song song sau C2

Khi C2 qua, chạy song song với C3:
- **Phiên K** (§7).
- **Chuẩn bị phối nhạc:** phong cách theo G-016. Đo độ lặp T2 (`toolkit/audio/d_music_selfsim.py`, Tham khảo; Tập 1 29%, Tập 2 sau sửa 19,7%). Nhạc và cách phối là gu: phiên chuẩn bị, **chủ dự án chọn ở C3** (clip ≤ 60 s).
- **Lời theo cảnh:** sinh giọng theo cảnh (G-015), tên take theo hash chữ. Kiểm từ khoá ASR ngay khi sinh. Khi kịch bản đổi, **chỉ sinh lại cảnh đổi chữ**.

## 5. Gói phát hành

- **C1:** tiêu đề nháp kiểm so cặp mù **một vòng** (tham khảo). Chủ dự án chọn.
- **C6:** chỉ **3 thumbnail đã qua claim-risk** (REVIEWER soát trước), so cặp một vòng. Chủ dự án chọn mặc định và bộ Test & Compare.
- **Số đo thật là Test & Compare trên YouTube**, ghi vào `episodes/epNNN/audience.md`.

## 6. Giao hàng (P3)

```
python3 toolkit/deliver/deliver.py episodes/epNNN/out/video.mp4 --out episodes/epNNN/work/delivery --name epNNN \
        --branch epNNN-delivery --push
```
- Bản tải YouTube mã hoá theo bitrate YouTube khuyến nghị: 1080p **8 Mb/s ở 24–30 fps, 12 Mb/s ở 60 fps**. Audio copy.
- Chia phần **90 MB**, commit lên nhánh tạm mồ côi `epNNN-delivery` kèm `SHA256SUMS` và `JOIN.md` (lệnh ghép Windows/Mac).
- Gói C6 ghi link nhánh. Chủ dự án tải xong thì **xoá nhánh** (phiên xoá nếu proxy cho phép; không thì ghi việc treo).
- **Không gửi qua chat.** Bản gốc không lên git; `README.md` của tập ghi lệnh render tái lập được và SHA-256 bản gốc.

## 7. Hợp đồng với phiên K

- Phiên K chạy **một lần mỗi tập**, ngay khi danh sách claim C2 chốt. P1 gửi K: `numbers.md`, danh sách claim kịch bản dùng, `checks-notes.md` (mô hình, đại lượng).
- **Tên `model.kind` và `params` do phiên K quyết.** Phiên dựng theo, không đề xuất tên trước (lessons E8).
- Claim thêm sau khi K đã khoá thì gom lại, cho vào lần K của tập sau. Nếu claim đó chặn phát hành: đưa vào gói C6.

## 8. KPI mỗi tập (ghi vào `ledger.md`, so với tập trước)

| KPI | Cách đo | Tập 2 (mốc so) |
|---|---|---|
| Số lần chủ dự án tham gia | Mỗi lần dừng chờ chủ dự án (cổng, câu hỏi ngoài cổng, xác nhận) | 11 cổng (C1, C2, C2b, C3, C3b, C3c, C3d, C4, C4b, C4c, C6) + 1 tin gửi nhầm + giao hàng |
| Số vòng mỗi cổng | Vòng kiểm/sửa tới khi qua | C1 1 · C2 3 (+C2b) · C3 ~6 vòng hình · C4 3 · C5 1 (+4 cảnh sinh lại) · C6 1 (+phối lại nhạc) |
| Số lượt agent | Mỗi agent con một lượt | ≈ 300 (cộng từ `gates/`: kiểm mù ≈ 287 người đọc + chấm, trong đó so cặp gói phát hành 72) |
| Ký tự ElevenLabs | Header `character-cost` | 9.436 |
| Thời gian | Từ khởi động P1 tới C6 duyệt; từ C6 tới tải xong | 01/10 02:35 → C5 xong trong ngày 01/10; C6 duyệt 04/10; giao hàng 04/10 |
| Điểm L3 | Phiếu §8 của quality-framework | chưa ghi số (phát hành CÓ) |
| Token | Nếu đọc được từ phiên | không đọc được |

Mục tiêu Tập 3 (playbook v2): chủ dự án tham gia **3 lần + xác nhận tải**; mỗi cổng TỰ ĐỘNG ≤ 2 vòng; lượt agent kiểm mù giảm nhờ dừng sớm và bỏ phép che chữ/số.

## 9. Công cụ

| Việc | Lệnh |
|---|---|
| Cắt dải kiểm mù | `python3 toolkit/blind/strips.py VIDEO SPANS.json OUTDIR` |
| Chia mẫu cho người đọc | `python3 toolkit/blind/packets.py deal manifest.json --out <scratch>/blind/Cx --key episodes/epNNN/review-cx/key.json --slots 1,2` |
| Gói người chấm | `… packets.py packet --key … --answers … --rubric … --packet … --rubric-key …` |
| Gộp điểm, dừng sớm (**chỉ C3, C4**: ≤ 3 người đọc mỗi nhịp; C1, C2 đếm theo ý đồ) | `… packets.py tally --key … --rubric-key … --scores … --classes beats-class.json --md gates/Cx-tally.md` (C3: `--threshold 1`; C4: mặc định 0.8); người thứ 3: `packets.py next …` rồi `deal --slots 3 --only <set/id,…>` |
| Giao hàng | `python3 toolkit/deliver/deliver.py …` (§6) |
| Test công cụ | `python3 -m unittest discover -s toolkit/tests` |

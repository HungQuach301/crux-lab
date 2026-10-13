# PLAN Tập 8 — Rent vs Buy, replayed (#20) (≤ 1 trang)

**Nhánh:** `ep008` · **Đề tài:** #20 `topics-r2/machine/rent-buy-1` · **Format:** `lab` (F-14 v4 trượt; f14 opt-in khai `episode.yaml`) · **Phiên vừa đóng:** P1 (`session_01PgYotX9apRQ11gZoym31kJ`) — **dừng ở G1**

## 1. Trạng thái
**G1 chờ chủ dự án** (`gates/G1.md`, issue [HungQuach301/crux-lab#55](https://github.com/HungQuach301/crux-lab/issues/55)). Việc 0: 4/4 SHA, model 76/76, độc lập 49/49; điều kiện G1 lô (tỉ lệ thuê/giá) ĐẠT — Census HVS 4,83–5,59 % (chờ mở PDF xác minh) + độ nhạy. C1 L1 3/3. C2 v2 kiểm mù 6/6, 0 khuyên ("khác" 2/6 → chủ dự án). M1–M6 ĐẠT trên bản đọc thật; ước 9:49; 2 mid-roll. Tiền kỳ: tầm nhìn, bản đồ liền mạch, 5 vật mới (N1, N2 ĐẠT; N3, N4, N5 trượt 2 vòng → G1 trước/sau). REVIEWER G1: ĐẠT có sửa (đã sửa).

## 2. Việc tiếp (≤ 3) và việc treo
1. P2: chép G1 → `gates/G1-answer.md`; ghi `taste-ledger.md`, `AUTHORSHIP.md`, ledger; áp (N5, N4 nhãn, N1 lưới, "khác" 2/6, tiêu đề).
2. P2 = C3 (hình mới: 5 vật + chuyển cảnh bản đồ → phố + footage), clip có chuyển động và âm.
3. **Trước C4:** phiên K (kind mới, `K-brief.md`; lô A34–A37 + A42–A45 (Tập 8; A38–A41 là của tongket-t7)); xác minh 4 số Census HVS (PDF) + điều khoản; chủ dự án tải footage LoC/HUD/Census theo URL ở `preprod/continuity.md`.
- Treo: lô K Tập 8 lẽ ra chạy trước P1 (PLAN kênh) — chưa chạy; tổng kết Tập 7 — chưa rõ đã chạy.

## 3. Quyết định đã có (chủ dự án)
- 12/10: `lab` (F-14 v4 trượt). 13/10 luật tạm (tiền kỳ, footage ≤ 15 %, 1 Short không thumbnail, trần P1 $12, ≤ 2 vòng mỗi lỗi) — lệnh mở P1. G1 → `gates/G1-answer.md` (chưa có).

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 v1→v2 | S26–S28, S05.6, S31, S32.3 | số dày 4/6; phương pháp 2/6; câu kết bị trích làm căn cứ khuyên 5/6 | WRITER mới: 1 số nói, số Census lên hình; giới hạn → thẻ V7; câu kết mới | 6/6, 0 khuyên, "khác" 2/6 | G1 |
| §6.5 | S01.3, S04, S07.2 | S01 > 2 số; "$400,000 home" đọc sai | claim tham số; 2,5 % nói, 6 % + $80k/$12k lên hình; "home priced at" | checker ĐẠT | — |
| PRE r1→r2 | N3 Nina | bước về nhà = "chuyển sang mua" | đứng giữa, đèn đưa qua lại, thẻ RENT/BUY | 0·0,5 → 0,5·0,5 | G1 |
| PRE r1→r2 | N4 hộp CASH | "tiền cho chủ nhà" | bó bay từ cửa căn hộ, Nina cạnh | 1/3 (c "không đầu tư") | G1: nhãn |
| PRE r1→r2 | N5 sương | "nhà khan hiếm" → "mua sớm" | lô trống viền đứt | 0/2 cả hai | G1: bỏ |

## 5. Mức cảnh báo, token, chi (`lab`: 15 triệu · Console $45; **P1 trần CỨNG $12**)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless + api.sh (trần) | Console |
|---|---|---|---|---|---|---|---|
| P1 | 13/10 15:55 (một lượt, 203 vòng) | 0,162 | 0,494 | 56,46 | **0,656** | headless 44 lượt: sinh 0,046 · vào mới 0,188 · cache 0,134 · **trần 0,23 triệu**; api.sh 5 lượt: sinh 0,102 · vào mới 0,296 · cache 4,09 · **trần 0,40 triệu** | **≈ $6,3** (`logs/usage/spend.py`) |
¹ Đọc ở chặng sau G1 (13/10 16:1x): sự kiện `result` duy nhất của P1 (Opus + Haiku, `modelUsage`). Cách đọc: `list_events(session_id="session_01PgYotX9apRQ11gZoym31kJ", kinds=["result"], limit=100)` lật `before_id` → `python3 toolkit/usage/from_events.py --session session_01PgYotX9apRQ11gZoym31kJ --close trang*.json` → điền dòng này. Agent con 0. EL: 1.116 ký tự (còn ≈ 49.600 / 144.034, làm mới 01/11). Giờ render: clip vật thể ≈ 0,4 h (Playwright 540p).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep008/PLAN.md` 5. `episodes/ep008/gates/G1.md` 6. `episodes/ep008/gates/G1-answer.md` 7. `episodes/ep008/preprod/continuity.md` 8. `episodes/ep008/gates/PRE-objects.md`

## 7. Prompt phiên kế (D-011)
```
Chạy Tập 8, phiên P2 (C3 hình mới). Nhánh ep008 (@ d17122a hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep008`; đọc mục 6 của episodes/ep008/PLAN.md.
Gói đã gửi: episodes/ep008/gates/G1.md. Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep008/gates/G1-answer.md; ghi taste-ledger.md, AUTHORSHIP.md, ledger; đọc 4 số token P1 (PLAN §5 chú thích ¹); commit, push.
Luật tạm 13/10 vẫn áp (≤ 2 vòng mỗi lỗi, footage ≤ 15 %, headless khoá Console, 0 agent con, dừng tiến trình bằng PID, push sau mỗi bước lớn).
Chặng này: áp G1 → C3 (clip có chuyển động và âm) → dừng ở C3 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Câu trả lời G1:
<<DÁN CÂU TRẢ LỜI G1 Ở ĐÂY>>
```

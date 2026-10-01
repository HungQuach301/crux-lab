# topics-r1 — thiết kế vòng 1 (khoá trước khi sinh)

Thẩm quyền: `decisions/D-004.md`. Đầu bài chung: `BRIEF.md`. Bộ kiểm thẻ: `tools/cardcheck.py` (v2). Phiên DT1, 2026-10-01.
Luật ở file này viết **trước** khi có đề tài nào; không sửa sau khi thấy kết quả.

## Bên máy (phần duy nhất khác với bên đối chứng)

Ba agent con, mỗi trụ một agent; **không** được đọc `topics-r1/control/` hay `m3/control/`.
1. Bắt đầu từ **quyết định của một nhóm người xem cụ thể**, không từ một thống kê. Chạy dữ liệu thật **trước** khi viết thẻ: FRED (gồm CPI), CFPB/HMDA; luật thuế qua irs.gov, uscode.house.gov, law.cornell.edu, www.ecfr.gov, federalregister.gov. Giữ đề tài khi kết quả **đổi được quyết định** của nhóm đó hoặc **khác điều họ đoán**.
2. Kiểm mới lạ **theo quyết định** (web search, ≥ 3 truy vấn): `not-found` / `answered-without-data` / `answered-with-data` (→ loại). Ghi tiêu đề + link; không tải, không trích nội dung.
3. Được sinh dư và tự lọc; ghi số đã loại và lý do ở `machine/<trụ>-discards.md`.

Hồ sơ mỗi đề tài: `topics-r1/machine/<trụ>-<k>/` (k = 1…4):
| Tệp | Nội dung |
|---|---|
| `card.json` | `{viewer, decision, promise, title, thumbnail}` đã `normalize`, qua `cardcheck.check` |
| `data/` | tệp thô (không commit, `.gitignore`); SHA-256 ghi ở `sources.json` |
| `calc.py` | đọc `data/`, in một JSON `{id: value}` cho mọi số trong `result.json` |
| `result.json` | `answer` (kết quả có số, như sẽ nói trong tập), `guess` (điều nhóm người xem có thể đoán), `changesDecision` (vì sao kết quả đổi quyết định hoặc khác điều đoán), `numbers[]` {`id`,`value`,`unit`,`definition` đủ để tính lại không cần `calc.py`}, `assumptions[]`, `limits` ("history, not a forecast" nếu dùng lịch sử) |
| `sources.json` | `series[]` {`id`,`provider`,`url` ghim,`seriesPage`,`file`,`sha256`,`retrieved`,`lastObservation`,`terms` {`quote` nguyên văn, `url`}}; `provisions[]` {`cite`,`url` chính thức,`quote` nguyên văn} |
| `novelty.json` | `decision`, `queries[]` (≥ 3), `results[]` {`query`,`title`,`url`}, `verdict` ∈ {`not-found`,`answered-without-data`}, `nearest[]` {`title`,`url`,`why`}, `note` |
| `claim-risk.md` | câu nào dễ vượt claim; điều tập không được nói (khuyên, dự báo); giới hạn dữ liệu |

## Bên đối chứng

GPT-5.5 (`gpt-5.5`), `reasoning.effort = medium`, không công cụ, không dữ liệu, vai như M3 ("well-read American… do not look anything up"). Một lệnh mỗi trụ, xin 2 thẻ. Thẻ sai khuôn → gọi lại cùng prompt (tối đa 2 lần nữa); không ai sửa chữ, chỉ `normalize` dấu câu. Lưu nguyên văn ở `control/raw/`, kết quả `control/out/<trụ>.json`. Xong → báo chủ dự án thu hồi khoá.

## Kiểm hợp lệ hồ sơ máy (chạy sau khi đóng băng)

Một hồ sơ **hợp lệ** khi đạt cả sáu mục; mục nào không kiểm được = không đạt. V1–V5 giữ nguyên nghĩa và dung sai của `m3/DESIGN.md`; V0 là phần chỉnh cho thẻ mới.
- **V0 Hồ sơ đủ:** đủ sáu tệp; `card.json` qua `cardcheck` v2; `novelty.json` có ≥ 3 truy vấn, mỗi truy vấn ≥ 1 kết quả có URL, `verdict` ∈ {`not-found`, `answered-without-data`}.
- **V1 Dữ liệu tái lập:** tải lại từng chuỗi theo URL ghim; SHA-256 khớp (lệch → ghi "SHA lệch", V2/V3 chạy trên tệp tải lại).
- **V2 Số tái lập:** chạy `calc.py` trên tệp tải lại; mọi số khớp `result.json` (lệch tương đối ≤ 0,5 % hoặc tuyệt đối ≤ 0,01).
- **V3 Tính lại độc lập:** một agent mới mỗi hồ sơ, **không thấy `calc.py`**, chỉ nhận `answer`, `numbers[].definition`, `assumptions`, `sources.json`; tự viết mã; cùng dung sai.
- **V4 Nguồn và điều khoản:** mỗi `seriesPage` trả 200; `terms.quote` có trong trang `terms.url` (gộp khoảng trắng).
- **V5 Điều luật:** mỗi `provisions[].url` thuộc domain chính thức, trả 200, `quote` có trong trang. Không viện điều luật → không áp dụng (đạt).

Mã: `verify/verify.py` (V0, V1, V2, V4, V5; chỉnh từ `m3/verify/verify.py`), agent V3 ghi `verify/v3/<id>/`. Thẻ đối chứng chỉ qua `cardcheck` (không có hồ sơ).

## Bảng AI tham khảo (niêm phong trước khi chủ dự án chấm)

6 agent **mới**, mỗi agent một vai người xem: (1) đang có lời mời refinance; (2) mua nhà lần đầu; (3) sắp nghỉ hưu; (4) làm tự do, lo thuế; (5) đang vay xe / nợ thẻ; (6) chỉ tò mò. Mỗi agent nhận 18 thẻ đã xoá nhãn theo một thứ tự ngẫu nhiên riêng, cùng câu hỏi, cùng thang 5, cùng chip; ghi một tệp tên ngẫu nhiên `panel/<hex>.json`. Commit trước khi gửi trang chấm. Báo cáo: độ khớp từng vai và trung bình bảng với chủ dự án (Spearman; đồng ý nhị phân ≥ 4).

## Trộn và chấm

- `blind/make_blind.py`: 18 thẻ (12 máy + 6 đối chứng), thứ tự ngẫu nhiên (`secrets.SystemRandom`), số thẻ 01–18, xoá nhãn. `cards.json` commit; `key.json` **không commit** trước khi chấm, chỉ commit `key.sha256`.
- Trang chấm (Artifact riêng tư, dựng từ `m3/blind`): một thẻ mỗi màn hình; câu hỏi cố định *"Would you approve this as a future episode for this channel?"*; thang 5 (5 Make it next · 4 Want it, later · 3 Not sure · 2 Not excited · 1 Not for this channel), mọi mức ngang hàng; chip tuỳ chọn *not me · seen it · vague promise · hard to believe · too narrow*; nút quay lại; ghi giây mỗi thẻ; cuối trang hiện mã. Trang không nói tỉ lệ máy/đối chứng, không nói có hai nguồn.
- Mã: `R1-<sha6> 01:5:nv:12 02:3::8 …` (thẻ:điểm:chip:giây; chip n=not me, s=seen it, v=vague promise, h=hard to believe, w=too narrow).
- Nhận mã → commit `key.json` → kiểm SHA → giải mã.

## Thước đo (D-004 §4)

- CHÍNH-1: thẻ máy điểm ≥ 4 / 12 ≥ 50 % (cửa sổ ±5 %: 47,5–52,5 % → đúng 6/12 phải nêu tên).
- CHÍNH-2: (tỉ lệ ≥ 4 máy) − (tỉ lệ ≥ 4 đối chứng) ≥ +20 điểm (cửa sổ 19–21 điểm).
- CHẶN: hồ sơ máy hợp lệ ≥ 10/12 (cửa sổ 9,5–10,5 → đúng 10/12).
- Vòng **đạt** khi cả hai CHÍNH và CHẶN đạt. Báo thêm: phân bố điểm, chip, nửa đầu/nửa sau (theo thứ tự chấm), từng trụ, thời gian, độ khớp AI, chi phí.
- Bước 2: mỗi thẻ máy ≥ 4 → hồ sơ ≤ 5 dòng → chủ dự án "Có/Không" → `topics/queue.md`.

# Cổng Mốc 3 — thiết kế (chờ chủ dự án duyệt)

Nguồn thẩm quyền duy nhất: `decisions/D-002.md`. Spec cũ ở nhánh `topic-import` chỉ để tra cứu.
Phiên M3, 2026-09-30. Chưa sinh luận điểm nào.

## Việc 0 — Tập 1 đã qua C5 chưa? **CHƯA đủ.**

Đọc nhánh `ep001-v2` @ `0386710` (chỉ đọc, không sửa):
- Video giao `087830ea…`; CHÍNH V08/V09/V11/C05 đã được chấp nhận; S07 đã sửa.
- S10 chờ K3.4. K3.4 đã merge vào main (`d0e5e00`, LOCK `64a15c4e…`), và `contract.json` đã đổi sang khoá mới (commit cuối `0386710`).
- **Không có báo cáo checks nào chạy với khoá `64a15c4e`.** Cả `out/checks/run-c6-1` và `run-c6-2` đều ghi `lock: beffb49b…`, kết quả CHẶN 27/29 (S07, S10 trượt). Dòng cuối của ledger chỉ ghi ý định "chạy `SKIP_PAGE=1 run.sh --first` toàn bộ luật", chưa có kết quả được commit.

→ Theo chỉ dẫn: phiên này **chỉ làm thiết kế cổng**, không sinh luận điểm cho tới khi Tập 1 có checks cuối K3.4 (CHẶN 29/29) được commit.

## Ràng buộc môi trường đã đo (2026-09-30)

| Nguồn | Truy cập từ container |
|---|---|
| FRED (`fred.stlouisfed.org`, qua `requests`) | được |
| CFPB (`consumerfinance.gov`, gồm HMDA) | được |
| OpenAI Responses API (`api.openai.com`, khoá có sẵn "OpenAI TTS spike") | được; `gpt-5.5` gọi được |
| irs.gov, uscode.house.gov, law.cornell.edu, ecfr.gov, govinfo.gov, congress.gov, ssa.gov, bls.gov, bea.gov, federalreserve.gov, treasurydirect.gov, fiscaldata.treasury.gov, api.census.gov, studentaid.gov | **bị chặn** (proxy 403; WebFetch cũng bị chặn) |

Hệ quả: trụ **thuế và chính sách** không kiểm máy được "điều khoản có thật" nếu chưa mở các domain luật/IRS. Trụ hưu trí thiếu SSA/BLS (lạm phát CPI vẫn lấy được qua FRED).

## (1) Model đối chứng

**Đề xuất:** OpenAI `gpt-5.5` (nhà cung cấp khác Anthropic, tránh điểm mù chung — bài học B7), qua Responses API.

Cách giới hạn "10 phút suy nghĩ":
- **Không công cụ** (không web search, không file, không code), **không dữ liệu** — chỉ cái nó đã biết, như một người đọc tin tài chính.
- Vai: *"a well-read American who follows personal-finance news, given ten minutes to think"*.
- **Một lệnh gọi mỗi trụ** (3 lệnh), mỗi lệnh xin đúng số luận điểm của trụ, khác nhau; `reasoning.effort = "medium"`; `max_output_tokens = 6000`; trần thời gian thực **10 phút mỗi lệnh** (quá giờ thì huỷ và gọi lại, tối đa 2 lần).
- Cùng khuôn thẻ như bên máy (mục 3). Thẻ sai khuôn → cùng prompt gọi lại (tối đa 2 lần); không ai sửa chữ.
- Lưu nguyên văn prompt, phản hồi, id model trả về, token và thời gian.
- Chi phí ước tính < 2 USD. Dùng khoá hiện có cho việc sinh chữ là **mục đích mới** → cần chủ dự án đồng ý (CHARTER §7.5).

Phương án khác: `gpt-5.5` effort `low` (đối chứng yếu hơn, máy dễ thắng, kết quả ít ý nghĩa); Claude không công cụ (cùng họ model với bên máy — trái tinh thần B7).

## (2) Phân bổ 20 cặp theo ba trụ

**Đề xuất 7 / 7 / 6**: vay nợ 7 · nghỉ hưu và đầu tư dài hạn 7 · thuế và chính sách 6. Mỗi cặp ghép một luận điểm máy với một luận điểm đối chứng **cùng trụ**, ghép ngẫu nhiên trong trụ.
- Trụ thuế cần mở domain: `irs.gov`, `uscode.house.gov` (hoặc `law.cornell.edu`), `ecfr.gov`, `ssa.gov`, `bls.gov`. Không mở → luận điểm thuế của máy sẽ **không hợp lệ** ở phần "điều khoản có thật" (không được coi là đạt khi không kiểm được).
- Phương án dự phòng nếu không mở domain: 8 / 8 / 4.

## (3) Khuôn thẻ và cách chấm

Thẻ tiếng Anh (khán giả Mỹ), hai câu:

```
PAIR 07 · Retirement and long-term investing

A  Thesis: <một câu, 20–28 từ>
   Overturns: "<niềm tin phổ biến bị phản bác, 10–16 từ>"

B  Thesis: …
   Overturns: "…"
```

Luật chuẩn hoá, kiểm bằng máy, áp như nhau cho hai bên:
- **Không con số:** không chữ số, không %, $, năm, không số viết bằng chữ (one…ten, half, double, triple…).
- Không tên nguồn, bộ dữ liệu, mã chuỗi, điều luật (bên máy có dữ liệu nên tên nguồn sẽ lộ nhãn).
- Chỉ **chuẩn hoá cơ học dấu câu** (gạch ngang dài → dấu phẩy, ngoặc kép thẳng); không sửa từ nào. Sai khuôn → chính bên sinh viết lại (tối đa 2 lần).
- Vị trí A/B ngẫu nhiên, cân 10 máy ở A / 10 máy ở B; thứ tự cặp ngẫu nhiên.

Chấm trên điện thoại: một trang Artifact riêng tư, **một cặp mỗi màn hình**, ba nút **A hơn / B hơn / Không phân biệt**, có nút quay lại. Hết 20 cặp, trang hiện một mã (`01A 02= 03B …`) để anh/chị dán vào chat — không cần hạ tầng lưu trữ. Câu hỏi cố định trên đầu trang (đề xuất, chủ dự án chốt):
> *"Which thesis is sharper — more worth an episode — than what a well-read finance-news follower would come up with in ten minutes?"*

Khoá key: `key.json` (cặp → bên nào là máy, kèm salt ngẫu nhiên) **không commit** trước khi chấm; chỉ commit SHA-256 của nó. Nhận mã chấm → commit key → kiểm SHA khớp → giải mã.

## Sau khi duyệt (chưa làm; ghi để khoá thứ tự)

1. **Sinh** 20 luận điểm máy (mỗi cái một thư mục: `thesis.json` + thẻ + `data/` chuỗi FRED/CFPB có SHA-256, URL ghim, điều khoản trích nguyên văn, trích điều luật nguyên văn + URL chính thức, `calc.py` tính mọi số) và 20 đối chứng. Chạy tiếp được (bỏ qua phần đã xong), thử lại lỗi mạng 2/4/8/16 s, in tiến độ, vòng chờ có trần thời gian và thoát khi tiến trình con chết (bài học O1/O2).
2. **Kiểm mới lạ tự chạy** cho từng luận điểm máy: ≥ 3 truy vấn web, lưu 10 kết quả đầu mỗi truy vấn, phán "đã có người nói / chưa thấy" kèm URL — ghi trước khi thấy kết quả chấm.
3. **Đóng băng**: commit toàn bộ luận điểm + thẻ (SHA) **trước** khi chạy kiểm hợp lệ. Không sửa sau đó.
4. **Kiểm hợp lệ bằng máy** (mã độc lập với mã sinh): tải lại chuỗi và so SHA; chạy lại `calc.py` và tính lại từng số bằng mã riêng; URL nguồn và điều khoản tồn tại, trích dẫn có trong trang; điều luật có thật và câu trích khớp. Hợp lệ = qua cả bốn; không kiểm được = không hợp lệ.
5. **Trộn, xoá nhãn, khoá key** → gửi trang chấm.
6. **Báo cáo:** số hợp lệ /20; tỉ lệ máy thắng trên cặp không hoà; so ngưỡng D-002 (≥ 60 %, ≥ 15/20); nguyên văn mọi thẻ và kết quả kiểm. Cửa sổ ±5 % phải nêu tên: tỉ lệ thắng trong **57–63 %**, số hợp lệ trong **14,25–15,75** (tức đúng **15/20**).

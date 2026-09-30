"""Review table of the two break-even methods: out/break-even-methods.csv -> review-m1b/break-even-methods.md

    python3 episodes/ep001/preprod/methods_table.py
"""
import csv
import json
import os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rows = list(csv.DictReader(open(os.path.join(EP, 'out', 'break-even-methods.csv'))))
M = json.load(open(os.path.join(EP, 'out', 'model.json')))['scenario']
L = ['# Hai cách tính hoà vốn — bảng so sánh (Tập 1, M1b)', '',
     f"Kịch bản: vay tháng 10/2023 ở lãi trung bình tháng đó ({M['oldRate']:.2f}%), đã trả {M['paymentsMade']} kỳ, tái cấp vốn ở lãi tuần gần nhất ({M['todayRate']:.2f}%, tuần {M['todayWeek']}); khoản vay mới 30 năm cho đúng dư nợ còn lại, phí đóng hồ sơ trả bằng tiền mặt. Maya, Dan, Priya: ILLUSTRATIVE, khoản vay và phí là trung vị HMDA 2025 theo quy mô.", '',
     '- **Cách đơn giản** (cách phần lớn máy tính dùng): hoà vốn = phí ÷ số tiền trả hằng tháng giảm được.',
     '- **Cách có chênh lệch dư nợ** (đáp án chính của tập): tháng đầu tiên mà (tiết kiệm cộng dồn + dư nợ khoản cũ − dư nợ khoản mới) ≥ phí. Khoản mới bắt đầu lại 30 năm nên trả gốc chậm hơn; khoản vay càng lâu năm thì chênh lệch càng lớn.', '',
     '| Trường hợp | Khoản vay | Phí | Giảm mỗi tháng | Cách đơn giản (tháng) | Có dư nợ (tháng) | Bán sau 3 năm | Bán sau 7 năm | Mức giảm cần để hoà vốn ≤ 36 tháng |',
     '|---|---|---|---|---|---|---|---|---|']
L += [f"| {r['case']} | {r['loan']} | {r['closingCost']} | {r['monthlySaving']} | {r['simpleMonths']} | **{r['withBalanceMonths']}** | {r['net3y']} | {r['net7y']} | {r['cutFor36m']} |" for r in rows]
L += ['', 'Dòng "history …": mỗi đợt lãi giảm ≥ 1 điểm kể từ 1971, tái cấp vốn ở tháng đầu tiên thấp hơn đỉnh 1 điểm; * = phí theo tỉ lệ cố định trước 2018 (ILLUSTRATIVE). Trong lịch sử, khoản vay mới vài tháng tuổi khi tái cấp vốn, nên hai cách gần như trùng nhau; với Maya (35 kỳ) thì khác.', '',
      'Nguồn: FRED `MORTGAGE30US` (Freddie Mac PMMS), HMDA 2018–2025 (CFPB/FFIEC). Tính bằng `model/refi.py` (`break_even_balance`, `both`, `net_after`, `history`); test `model/test_refi.py` (12 test, có bản cài đặt độc lập tính từng tháng). CSV: `out/break-even-methods.csv`.']
os.makedirs(os.path.join(EP, 'review-m1b'), exist_ok=True)
open(os.path.join(EP, 'review-m1b', 'break-even-methods.md'), 'w').write('\n'.join(L) + '\n')
print(len(rows), 'rows')

"""One-page summary of the M1b script for the owner (phone): review-m1b/summary.md

    python3 episodes/ep001/preprod/summary_m1b.py
"""
import json
import os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
C = {c['claimId']: c['display'] for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
t = json.load(open(os.path.join(EP, 'preprod', 'timeline-plan.json')))
tr = json.load(open(os.path.join(EP, 'work', 'table-read.json')))
ch = json.load(open(os.path.join(EP, 'out', 'voice', 'choice-report.json')))['acts']
A = {a['id']: a for a in t['acts']}
S = {s['scene']: s for s in t['sentences']}
mm = lambda x: f"{int(x // 60)}:{int(x % 60):02d}"
s = f"""# Tập 1 — gói duyệt M1b (tóm tắt 1 trang)

**Câu hỏi:** Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ? *(US only; history, not a forecast)*
**Độ dài dự kiến:** {mm(t['total'])}. Đọc thử liền mạch: {mm(tr['duration'])}. Cold open: {A['cold-open']['end']:.1f} s. Câu móc lại: {mm(S['a1-rehook']['start'])}–{mm(S['a1-rehook']['end'])}.

**Cold open (G-007): một người, một khoảnh khắc.**
Tháng 10/2023, Maya vay {C['loan_maya']} với lãi {C['r_old']}. Tuần này lãi trung bình {C['term30']} năm là {C['r_today']}. Bên cho vay chào tái cấp vốn với phí {C['cost_maya']}. Tiền đó bao giờ mới quay về?

**Luận điểm (sửa phương pháp):** phần lớn máy tính chia phí cho số tiền trả hằng tháng giảm được, và ra **{C['be_simple_maya']} tháng**. Nhưng khoản vay mới bắt đầu lại {C['term30']} năm; khi tính cả dư nợ còn lại, Maya hoà vốn sau **{C['be_bal_maya']} tháng**. Nếu lãi chỉ giảm {C['s025']} điểm, cách chia hứa {C['be_simple_025']} tháng, còn tính cả dư nợ thì không bao giờ hoà vốn. Bảng so sánh: `break-even-methods.md`.

**Ba nhân vật (G-008; ILLUSTRATIVE, số liệu là trung vị HMDA {C['y2025']} theo quy mô khoản vay):**

| | Khoản vay | Phí | Giảm mỗi tháng | Hoà vốn (có dư nợ) | Bán sau {C['y3']} năm | Bán sau {C['y7']} năm | Cần giảm để hoà vốn trong {C['hold36']} tháng |
|---|---|---|---|---|---|---|---|
| Dan | {C['loan_dan']} | {C['cost_dan']} | {C['sav_dan']} | {C['be_bal_dan']} tháng | lỗ {C['net36_dan']} | lãi {C['net84_dan']} | {C['cut36_dan']} điểm |
| Maya | {C['loan_maya']} | {C['cost_maya']} | {C['sav_maya']} | {C['be_bal_maya']} tháng | lãi {C['net36_maya']} | lãi {C['net84_maya']} | {C['cut36_maya']} điểm |
| Priya | {C['loan_priya']} | {C['cost_priya']} | {C['sav_priya']} | {C['be_bal_priya']} tháng | lãi {C['net36_priya']} | lãi {C['net84_priya']} | {C['cut36_priya']} điểm |

| Hồi | Câu hỏi | Bước ngoặt | Trả lời |
|---|---|---|---|
| 1 ({mm(A['act1']['start'])}) | Hoá đơn của Maya có bất thường không? | Hoá đơn gần như không lớn lên theo khoản vay: Dan chịu {C['share_small']} số tiền vay, Priya {C['share_big']} | Máy tính thông thường: {C['cost_maya']} ÷ {C['sav_maya']} = {C['be_simple_maya']} tháng. "Or has it?" |
| 2 ({mm(A['act2']['start'])}) | Phép chia đó bỏ sót gì? | Khoản vay mới bắt đầu lại {C['term30']} năm; sau {C['be_simple_maya']} tháng Maya nợ nhiều hơn {C['gap24']} | {C['be_simple_maya']} → {C['be_bal_maya']} tháng; Dan lỗ nếu bán sau {C['y3']} năm; Priya hoà vốn sau {C['be_bal_priya']} tháng |
| 3 ({mm(A['act3']['start'])}) | Trong {C['n_eps']} đợt giảm thật từ {C['y1971']} thì sao? | {C['n_further']} đợt: lãi giảm tiếp {C['s10']} điểm trước khi lần đầu hoà vốn; các khoản vay trong lịch sử còn mới nên hai cách gần như trùng | Trả lời vòng mở: Maya cần {C['cut36_maya']} điểm, Dan {C['cut36_dan']}, Priya {C['cut36_priya']}; hôm nay giảm {C['cut_today']} điểm, tức Maya lãi nếu giữ nhà quá {C['be_bal_maya']} tháng |

**Giọng (theo hồi, wpm):** {', '.join(f"{k} {v['rawWpm']}" for k, v in ch.items())}. Chi tiết: `../script/table-read-notes.md`.
**Âm thanh theo dữ liệu:** S2 (chủ dự án chọn, không lấn lời), đã có trong animatic.

**Trong gói:** `summary.md` · `animatic-0000-0080.mp4` (0:00–1:20: cold open và câu móc lại, có giọng và tiếng S2; hình là storyboard) · `table-read-full.m4a` · `break-even-methods.md` · `sb-01…04.png`
"""
open(os.path.join(EP, 'review-m1b', 'summary.md'), 'w').write(s)
print(len(s.split()))

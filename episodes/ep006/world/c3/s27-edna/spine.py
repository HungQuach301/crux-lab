"""Tập 6 · C3 · s27-edna (B27) — lời thật S27.1–S27.5 (cả cảnh).
  python3 episodes/ep006/world/c3/s27-edna/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Edna (không mặt, ILLUSTRATIVE) + hàng 10 thùng sáng. → ĐỒ THỊ trước "kept" (số chỉ ở đồ thị): nhãn ngày + "kept up: the last start
month that did"; "Twenty" = bộ đếm 1 → 20, hàng theo đúng sức mua của bà, TRẦN 10 (PHỤ-5: 105,7 % vẫn là 10; năm 2–5 thùng thứ 10 hơi mờ
rồi sáng lại); năm 20 (100,2 %) = 10 sáng đủ. Lùi máy (đồ thị → đồ thị) cho trục thời gian: "Her" = thanh 20 năm của Edna (1949 → 1969),
"Carl's" = thanh của Carl (1966 → 1986) + Carl và hàng 10 thùng; "same" = tô phần chồng (3 năm chung) + "same years of prices: her last,
his first"; "end" = hàng của Edna chạy lại năm 17 → 20, vẫn 10 sáng (đệm từ trước, CHÍNH-1 REVIEW-C2v3: không phải nhờ mấy năm này);
"start" = hàng của Carl chạy năm 1 → 3 và mờ đi — cùng những năm giá đó.
FIX-R2: tấm séc (obj6.Check) cạnh mỗi hàng — séc Edna bước lên ×1,02 ở mỗi kỷ niệm của bộ đếm "Twenty" (hàng vẫn đủ 10), "check" (S27.2) =
"check: +2% a year" trên séc; séc Carl bước năm 1 → 3 cùng hàng của ông. Thanh 20 năm của Edna vẽ ở "answer" (S27.3, cuối câu về bà, ngay sau
lùi máy) thay vì "Her" để khung 4 của dải (20,3 s) đã có trục thời gian; lùi máy kết thúc trước "answer"."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c3kit as K     # wlib + spine v2 + khung khoá hàng thùng
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S27.1', 'S27.2', 'S27.3', 'S27.4', 'S27.5']], lead=0.4)
A = SV.Anchors(words)
B = [
 ('c0', 'S27.1', 'world', 'Edna (minh hoạ) bắt đầu tháng 1/1949 — tháng bắt đầu cuối cùng mà khoản tăng 2 % theo kịp giá.', 'Edna + hàng 10 thùng sáng; đồ thị trước "kept": nhãn ngày + kept up.',
  {'edna': '@S27.1:Edna', 'last': '@S27.1:last', 'kept': '@S27.1:kept'}, ['tick khi hàng mọc', 'tick khi nhãn kept up'], 0.3, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị (giữa câu, trước "kept")'),
 ('c1', 'S27.2', 'chart', '20 năm sau, khoản trả của bà vẫn mua ít nhất bằng khoản đầu.', 'bộ đếm 1 → 20, hàng theo sức mua (trần 10), năm 20 = 10 sáng đủ.',
  {'twenty': '@S27.2:Twenty', 'check': '@S27.2:check', 'least': '@S27.2:least'}, ['nốt dữ liệu mỗi lần hàng đổi'], 0.4, 'nhẹ', '—'),
 ('c2', 'S27.3', 'chart', 'Bà thuộc nhóm nhỏ đầu tiên; không ai bắt đầu sau bà có câu trả lời đó.', 'giữ hàng sáng đủ; lùi máy cho trục thời gian.',
  {'handful': '@S27.3:handful', 'answer': '@S27.3:answer'}, ['tick khi thanh của Edna vẽ'], 0.4, 'suy nghĩ', 'lùi máy (đồ thị → đồ thị)'),
 ('c3', 'S27.4', 'chart', '20 năm của Edna kết thúc vài năm sau khi 20 năm của Carl bắt đầu.', 'thanh của Edna ("Her"), thanh của Carl + Carl và hàng của ông ("Carl\'s").',
  {'her': '@S27.4:Her', 'carl': '@S27.4:Carl'}, ['tick khi mỗi thanh vẽ'], 0.45, 'chú ý', '—'),
 ('c4', 'S27.5', 'chart', 'Cùng mấy năm giá: cuối quãng của bà (vẫn 10 thùng sáng) và đầu quãng của ông.', 'tô phần chồng + nhãn; hàng Edna năm 17 → 20 vẫn 10; hàng Carl năm 1 → 3 mờ đi.',
  {'same': '@S27.5:same', 'end': '@S27.5:end', 'lit': '@S27.5:lit', 'start': '@S27.5:start'}, ['tick khi tô', 'nốt dữ liệu mỗi năm'], 0.5, 'hiểu', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wEdna0', 'wEdna', cue['c0']['edna'], cue['c0']['last'], 2.4, 'mở đoạn: máy lại gần Edna và hàng thùng của bà', 'whoosh_air', {}),
    ('mode', 'wEdna', 'cEdna', cue['c0']['last'], cue['c0']['kept'], 1.1,
     'lời S27.1 đặt ngày (1949) + "kept up": số và nhãn so sánh chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị', 'whoosh_mode', {'start': 5.0}),
    ('pull', 'cEdna', 'cBoth', cue['c2']['handful'], cue['c2']['answer'], 1.4,
     'lời S27.4 đặt Edna cạnh Carl trên một trục thời gian: lùi máy để có chỗ cho hai thanh và hàng của Carl', 'whoosh_soft', {})])
E, Cv = K.P['edna'], K.P['carl']
yrs = K.spread(cue['c1']['twenty'], cue['c1']['least'] + 0.9, 20)
ek, ev = K.step_row(yrs, E[1:], ramp=0.15, v0=1.0)
ev = [e for i, e in enumerate(ev) if min(1, E[i]) != 1 or min(1, E[i + 1]) != 1]       # chỉ nốt khi hàng thật sự đổi (trần 10)
ev.append({'t': round(yrs[-1], 3), 'kind': 'data', 'v': 1.0})
rep = K.spread(cue['c4']['end'], cue['c4']['end'] + 0.9, 3)                              # chạy lại năm 18–20 của Edna: vẫn 10 sáng
ek2, ev2 = K.step_row(rep, E[18:21], ramp=0.15, v0=E[17])
cy = K.spread(cue['c4']['start'] + 0.1, cue['c4']['start'] + 0.9, 3)                     # năm 1–3 của Carl: mờ đi
ck, ev3 = K.step_row(cy, Cv[1:4], ramp=0.15, v0=1.0)
ev += [dict(e, v=1.0) for e in ev2] + ev3
ev += [{'t': cue['c0']['edna'], 'kind': 'tick', 'v': 0.45}, {'t': cue['c0']['kept'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c2']['answer'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['c3']['carl'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c4']['same'], 'kind': 'tick', 'v': 0.55}]
K.finish(HERE, 'ep006 C3 · s27-edna (S27)', words, takes, lines, end, beats, moves, ev,
         {'rows': {'edna': ek + ek2[1:], 'carl': ck}, 'cards': {'edna': K.step_check(yrs), 'carl': K.step_check(cy)}, 'years': {'edna': [round(t, 3) for t in yrs], 'edna_rep': [round(t, 3) for t in rep], 'carl': [round(t, 3) for t in cy]},
          'label_cues': {'c0.kept': 'kept up: the last start month that did', 'c1.check': 'check: +2% a year', 'c3.carl': 'Carl · ILLUSTRATIVE · from Jan 1966',
                         'c4.same': 'same years of prices: her last, his first'},
          'visual_cues': ['c0.edna', 'c1.twenty', 'c1.check', 'c2.answer', 'c3.carl', 'c4.same', 'c4.end', 'c4.start']},
         [cue['c0']['kept'], cue['c1']['least'], cue['c4']['same']], hold=2.6)   # giữ 2,6 s: khung 6 của dải cổng gốc (91,7 % clip) rơi sau khi hàng Carl mờ xong

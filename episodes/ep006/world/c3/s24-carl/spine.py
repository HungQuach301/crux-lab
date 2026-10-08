"""Tập 6 · C3 · s24-carl (B24) — lời thật S24.1–S24.6 (cả cảnh).
  python3 episodes/ep006/world/c3/s24-carl/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Ruth với hàng của bà (0,904, như s07) → lia sang Carl (không mặt, ILLUSTRATIVE): hàng 10 thùng mọc lên ở "Carl".
→ ĐỒ THỊ sau "1966" (số chỉ ở đồ thị, quy tắc 1): nhãn ngày, "prices: 6.38% a year, the fastest stretch" ở "fastest"; "ten" = ngoặc 10 chỗ;
"every" = bộ đếm kỷ niệm 1 → 20, mỗi kỷ niệm hàng mờ ĐÚNG theo sức mua (mờ liên tục, PHỤ-4: không làm tròn nguyên), một nốt dữ liệu/kỷ niệm,
không bao giờ sáng lại; năm 20: ≈ 4,3 thùng sáng; "before" = "less buying power on 20 of 20 anniversaries"; "Ruth's" = ô nhỏ: đường của Ruth
so với vạch khoản đầu (lõm rồi lên lại sớm).
FIX-R2: tấm séc (obj6.Check) cạnh mỗi hàng — séc Ruth ở cỡ năm 20 (×1,486); séc Carl bước lên ×1,02 ở mỗi kỷ niệm "every" 1 → 20, cùng nhịp
và chung nốt với hàng mờ dần. Ngoặc khoản đầu dời sang "first" (S24.4, 18,9 s — khung 4 của dải đã thấy) + "check" = "check: +2% a year".
F-2: tick "first" nhẹ (v 0,25, SNR); tick ô Ruth dời vào khe lời trước "Ruth's" (0,17 s)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c3kit as K     # wlib + spine v2 + khung khoá hàng thùng
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S24.1', 'S24.2', 'S24.3', 'S24.4', 'S24.5', 'S24.6']], lead=0.4)
A = SV.Anchors(words)
B = [
 ('b0', 'S24.1', 'world', 'Ruth không phải trường hợp tệ nhất, cũng không phải tốt nhất.', 'Ruth sau hàng của bà (≈ 9 sáng).',
  {'ruth': '@S24.1:Ruth', 'best': '@S24.1:best'}, ['tick khi hàng của Ruth loé'], 0.3, 'bình thản', 'lia sang Carl'),
 ('b1', 'S24.2', 'world', 'Carl (minh hoạ) nhận cùng loại khoản trả tăng dần từ tháng 1/1966.', 'Carl + hàng 10 thùng mọc lên ở "Carl".',
  {'carl': '@S24.2:Carl', 'january': '@S24.2:January'}, ['tick khi hàng mọc'], 0.35, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b2', 'S24.3', 'chart', '20 năm của Carl có giá tăng nhanh nhất: 6,38 %/năm.', 'nhãn ngày + nhãn giá 6.38% a year.',
  {'fastest': '@S24.3:fastest'}, ['tick khi nhãn hiện'], 0.45, 'nghiêm', '—'),
 ('b3', 'S24.4', 'chart', 'Khoản đầu của Carl cũng mua 10 thùng.', 'ngoặc 10 chỗ "first check: 10 crates".',
  {'first': '@S24.4:first', 'check': '@S24.4:check'}, ['tick nhẹ khi ngoặc hiện'], 0.45, 'hiểu', '—'),
 ('b4', 'S24.5', 'chart', 'Ở cả 20 kỷ niệm, khoản trả của Carl mua ít hơn năm trước.', 'bộ đếm 1 → 20, hàng mờ dần mỗi năm (không sáng lại) tới ≈ 4,3; nhãn 20 of 20.',
  {'every': '@S24.5:every', 'before': '@S24.5:before'}, ['một nốt dữ liệu mỗi kỷ niệm, cao độ = sức mua (đi xuống)'], 0.6, 'nặng', '—'),
 ('b5', 'S24.6', 'chart', 'Ruth lên lại trong những năm đầu; Carl thì không bao giờ.', 'ô nhỏ: đường của Ruth so với vạch khoản đầu, lõm rồi lên lại sớm; hàng của Carl loé ở "never".',
  {'ruths': '@S24.6:Ruth', 'never': '@S24.6:never'}, ['tick khi ô hiện', 'tick ở "never"'], 0.4, 'suy nghĩ', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('pan', 'wRuth', 'wCarl', cue['b0']['best'], cue['b1']['carl'], 0.75, 'lời S24.2 chuyển sang Carl: lia từ hàng của Ruth sang chỗ hàng của Carl', 'whoosh_soft', {}),
    ('mode', 'wCarl', 'cCarl', cue['b1']['january'], cue['b2']['fastest'], 1.2,
     'lời S24.2–S24.3 đặt số (1966, 6.38%, 20 kỷ niệm): số chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị', 'whoosh_mode', {'start': 5.0})])
years = K.spread(cue['b4']['every'], cue['b4']['before'] + 0.35, 20)
ck, ev = K.step_row(years, K.P['carl'][1:], ramp=0.2, v0=1.0)
ev += [{'t': cue['b0']['ruth'], 'kind': 'tick', 'v': 0.4}, {'t': cue['b1']['carl'], 'kind': 'tick', 'v': 0.5}, {'t': cue['b2']['fastest'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['b3']['first'], 'kind': 'tick', 'v': 0.25}, {'t': round(cue['b5']['ruths'] - 0.17, 3), 'kind': 'tick', 'v': 0.55}, {'t': cue['b5']['never'], 'kind': 'tick', 'v': 0.3}]
K.finish(HERE, 'ep006 C3 · s24-carl (S24)', words, takes, lines, end, beats, moves, ev,
         {'rows': {'ruth': [[0, K.P['ruth'][-1]]], 'carl': ck}, 'cards': {'ruth': [[0, 20]], 'carl': K.step_check(years, ramp=0.15)}, 'years': {'carl': [round(t, 3) for t in years]}, 'ruth_path': K.P['ruth'],
          'label_cues': {'b2.fastest': 'prices: 6.38% a year, the fastest stretch', 'b3.first': 'first check: 10 crates', 'b3.check': 'check: +2% a year',
                         'b4.before': 'less buying power on 20 of 20 anniversaries', 'b5.ruths': 'Ruth · ILLUSTRATIVE: back above in early years'},
          'visual_cues': ['b1.carl', 'b3.first', 'b3.check', 'b4.every', 'b4.before', 'b5.ruths', 'b5.never']}, [cue['b1']['carl'], cue['b4']['every'], cue['b5']['never']])

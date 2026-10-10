"""Tập 6 · C4 · ĐOẠN A = S01–S03 + ident (cold open). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep006/world/c4/a-s01-s03/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
B01 (S01): Ruth + tấm séc + hàng 10 thùng (W10, duyệt C3). "rises" → séc bước lên 20 kỷ niệm ×1,02 trong khi hàng thùng tối theo đúng sức mua
của bà tới 0,904 ("less") — nghịch lý trong 3 s, ở chế độ thế giới. → ĐỒ THỊ sau "sixty-five" (số chỉ ở đồ thị): "check: +2% a year" ở "two",
ngoặc "first check: 10 crates" + dấu hỏi ở "keep" (câu hỏi của bà).
B02 (S02): "twentieth" = dải lịch 20 ô Aug 2006 → Aug 2026 dưới hàng; "every" = dải nhân lên thành chồng dải mờ lùi về 1947 (xem trước V1).
B03 (S03): lia sang đồ thị V3 (đường của Ruth theo năm, vạch "first check" cố định): "keeping" nhãn định nghĩa; "short" = điểm cuối dưới vạch;
về thế giới trước "only" (lớp bắt buộc), "choose" = đối trọng "Not advice on which check or raise"; ident 3 s: thế giới tối dần."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
SV = K.SV
S = K.Seg(['S01', 'S02', 'S03'])
B = [
 ('a0', 'S01.1', 'world', 'Séc của Ruth tăng mỗi năm mà mua ít hơn séc đầu.', 'séc bước lên 20 lần, hàng thùng tối dần tới 0,904.',
  {'rises': '@S01.1:rises', 'less': '@S01.1:less'}, ['nốt dữ liệu mỗi kỷ niệm'], 0.35, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S01.2', 'world', 'Bà chọn séc nhỏ hơn tăng 2 %/năm; hỏi: 2 % có theo kịp giá?', 'đồ thị: check +2% a year; ngoặc 10 thùng + "?".',
  {'sixty': '@S01.2:sixty-five', 'two': '@S01.2:two', 'keep': '@S01.2:keep'}, ['tick'], 0.45, 'tò mò', '—'),
 ('a2', 'S02.1', 'chart', 'Năm thứ hai mươi của bà kết thúc tháng Tám này.', 'dải lịch 20 ô Aug 2006 → Aug 2026.',
  {'twentieth': '@S02.1:twentieth', 'august': '@S02.1:August'}, ['tick'], 0.5, 'chú ý', '—'),
 ('a3', 'S02.2', 'chart', 'Thử mức tăng đó trên mọi quãng 20 năm từ 1947.', 'dải nhân lên thành chồng dải lùi về 1947.',
  {'every': '@S02.2:every', 'nineteen': '@S02.2:nineteen', 'often': '@S02.2:often', 'much': '@S02.2:much'}, ['rise'], 0.55, 'hé lộ', 'lia → V3'),
 ('a4', 'S03.1', 'chart', 'Theo kịp = séc vẫn mua ít nhất bằng séc đầu của nó.', 'đồ thị V3: vạch "first check" cố định + nhãn định nghĩa.',
  {'keeping': '@S03.1:keeping', 'least': '@S03.1:least', 'first': '@S03.1:first'}, ['tick'], 0.45, 'hiểu', '—'),
 ('a5', 'S03.2', 'chart', 'Ruth minh hoạ, giá Mỹ thật; hôm nay séc bà hụt mức đó.', 'đường của Ruth vẽ tới năm 20, điểm cuối dưới vạch.',
  {'ruth': '@S03.2:Ruth', 'today': '@S03.2:today', 'short': '@S03.2:short'}, ['data'], 0.45, 'nặng', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('a6', 'S03.3', 'world', 'Chỉ Mỹ, lịch sử, không dự báo.', 'Ruth + hàng thùng; lớp bắt buộc.',
  {'only': '@S03.3:only', 'history': '@S03.3:history'}, [], 0.3, 'bình thản', '—'),
 ('a7', 'S03.4', 'world', 'Không nói chọn séc nào.', 'đối trọng "Not advice on which check or raise".',
  {'choose': '@S03.4:choose'}, [], 0.3, 'bình thản', 'ident'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
IDENT = [round(S.end['S03'] - 3.0, 3), S.end['S03']]
years = K.spread(cue['a0']['rises'], cue['a0']['less'] + 0.85, 20)
moves = K.moves_of([   # vòng sửa 2 (B01 "shrink"): cú đẩy bắt đầu sau kỷ niệm 20 — séc lớn lên khi máy đứng yên
    ('m_push', 'push', 'wRuth0', 'wRuth', cue['a0']['less'], cue['a1']['sixty'], 1.6, 'sau "less": máy lại gần Ruth và hàng thùng vừa tối dần (câu hỏi của bà)', 'whoosh_air', {'start': years[-1] + 0.15}),
    ('m_c1', 'mode', 'wRuth', 'cRuth', cue['a1']['sixty'], cue['a1']['two'], 1.2, 'lời S01.2 đặt số (2 %/năm, 10 thùng): số chỉ ở chế độ đồ thị (quy tắc 1)', 'whoosh_mode', {'start': 5.0}),
    ('m_pan', 'pan', 'cRuth', 'cLine', cue['a3']['much'], cue['a4']['keeping'], 1.1, 'lời S03.1 định nghĩa "keeping up" = so với séc đầu theo năm: lia sang đồ thị V3', 'whoosh_soft', {}),
    ('m_w', 'mode', 'cLine', 'wRuth2', cue['a5']['short'], cue['a6']['only'], 1.1, 'lời S03.3 "US only … history": lớp bắt buộc đứng riêng, về người (thế giới)', 'whoosh_mode', {}),
])
Pr = K.P['ruth']
rk, ev = K.step_row(years, Pr[1:], ramp=0.12, v0=1.0)
ev += [{'t': cue['a1']['two'], 'kind': 'tick', 'v': 0.5}, {'t': cue['a1']['keep'], 'kind': 'tick', 'v': 0.55},
       {'t': cue['a2']['twentieth'], 'kind': 'tick', 'v': 0.4}, {'t': cue['a3']['every'], 'kind': 'rise', 'dur': 1.2},
       {'t': cue['a4']['keeping'], 'kind': 'tick', 'v': 0.45}, {'t': cue['a5']['short'], 'kind': 'data', 'v': Pr[-1]}]   # ident: không sfx (nhạc hiệu A phát ở 3 s cuối đuôi S03, music.post)
line_t = [cue['a5']['ruth'], cue['a5']['short']]                   # đường của Ruth vẽ năm 0 → 20 giữa "Ruth" và "short"
K.finish(HERE, S, 'ep006 C4 · A = S01–S03 + ident (cold open)', beats, moves, ev,
         {'rows': {'ruth': rk}, 'cards': {'ruth': K.step_check(years, ramp=0.1)}, 'years': [round(t, 3) for t in years], 'ruth_path': Pr,
          'line_draw': [round(t, 3) for t in line_t], 'ident': IDENT},
         {'a1.two': 'check: +2% a year', 'a1.keep': 'first check: 10 crates', 'a2.august': 'Aug 2006 → Aug 2026',
          'a3.nineteen': 'every 20-year stretch since 1947', 'a4.keeping': 'keeping up = buys at least the first check',
          'a5.ruth': 'Ruth · ILLUSTRATIVE', 'a7.choose': 'Not advice on which check or raise'},
         ['a0.rises', 'a0.less', 'a1.two', 'a1.keep', 'a2.twentieth', 'a3.every', 'a4.keeping', 'a5.short', 'a7.choose'],
         accents=[cue['a0']['less']], rule7=True, inputs=['episodes/ep006/world/c4/checklook.js'])

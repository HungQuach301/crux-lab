"""Tập 7 · C3 · s21-track (B21, KEY-9) — lời thật S21.1–S21.3 (cả cảnh; S21.2 bản hiện tại không nói "195 months": số đó chỉ ở chữ trên hình).
  python3 episodes/ep007/world/c3/s21-track/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Tessa cạnh nhà; N1 đường tháng chạy từ nhà: "pay" → "assume" đặt 15 cột-năm × 12 ô (180 khoản trả, mỗi cột một nốt dữ liệu); "same" =
vạch 15 năm (ink-muted) hiện. → ĐỒ THỊ (gần thẳng xuống lưới): "doesn't" → "ends" thêm 14,6 ô warn quá vạch (mỗi ô một nốt, bội âm sáng = trễ);
"ends" = "pay $2,828 on the 30-year: about 195 months"; "late" = "about 15 months late". S21.3: "add" → "required" lớp mỏng cushion (trả thêm)
phủ lên từng cột-năm trái → phải, mỗi cột bớt một ô trễ; đường kết thúc đúng ở ô 180; "seven" = "to finish in 180 months: +$733 a month". Giữ."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K
SV, wlib, G = K.SV, K.wlib, K.G
words, takes, lines, end = wlib.clip_voice([['S21.1', 'S21.2', 'S21.3']], lead=0.6)
A = SV.Anchors(words)
B = [
 ('a0', 'S21.1', 'world', 'Lối tắt: trả khoản 30 năm đúng bằng khoản 15 năm và tưởng xong cùng ngày.', 'đường tháng 180 ô đặt từ nhà Tessa; vạch 15 năm hiện ở "same".',
  {'pay': '@S21.1:pay', 'same': '@S21.1:same'}, ['nốt dữ liệu mỗi cột-năm'], 0.3, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S21.2', 'chart', 'Không: xong muộn khoảng 15 tháng.', '14,6 ô warn quá vạch; nhãn about 195 months ("ends"), about 15 months late ("late").',
  {'doesnt': '@S21.2:doesn', 'ends': '@S21.2:ends', 'late': '@S21.2:late'}, ['nốt dữ liệu sáng mỗi ô trễ', 'tick khi nhãn hiện'], 0.5, 'nghiêm', '(liền)'),
 ('a2', 'S21.3', 'chart', 'Muốn xong trong 15 năm: thêm $733 mỗi tháng.', 'lớp mỏng cushion phủ từng cột, ô trễ tắt dần; đường xong ở ô 180; nhãn +$733 ("seven").',
  {'add': '@S21.3:add', 'seven': '@S21.3:seven', 'required': '@S21.3:required'}, ['nốt dữ liệu mỗi cột', 'tick khi nhãn hiện'], 0.4, 'hiểu', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wT0', 'wT', 0.0, cue['a0']['pay'], 2.6, 'mở đoạn: máy lại gần nhà Tessa và khoảng sàn nơi đường tháng sẽ chạy, trước ô đầu ("pay")', 'whoosh_air', {}),
    ('mode', 'wT', 'cT', cue['a0']['same'], cue['a1']['doesnt'], 1.3,
     'S21.2 đặt số tháng; số chỉ ở chế độ đồ thị (quy tắc 1) → nhìn thẳng xuống lưới để đếm ô trễ', 'whoosh_mode', {})])
yrs = K.spread(cue['a0']['pay'], A.at('@S21.1:assume'), 15)
lit, ev = K.steps(yrs, [12 * (k + 1) for k in range(15)], ramp=0.2, v0=0, pitch=lambda v: 0.2 + 0.4 * v / 180)
L = G['late_months']; nl = int(L) + (1 if L % 1 else 0)
lt = K.spread(cue['a1']['doesnt'] + 0.1, cue['a1']['ends'] - 0.12, nl)
late_v = [min(L, k + 1) for k in range(nl)]
late_up, e2 = K.steps(lt, late_v, ramp=0.07, v0=0, pitch=lambda v: 0.62 + 0.3 * v / L, over=True)
ft = K.spread(cue['a2']['add'], cue['a2']['required'] - 0.1, 15)
ex, e3 = K.steps(ft, [k + 1 for k in range(15)], ramp=0.2, v0=0, pitch=lambda v: 0.3 + 0.3 * v / 15)
late_dn, _ = K.steps(ft, [round(L * (1 - (k + 1) / 15), 3) for k in range(15)], ramp=0.2, v0=L)
late = late_up + [p for p in late_dn if p[0] > late_up[-1][0]]
ev += e2 + e3 + [{'t': cue['a1']['ends'], 'kind': 'tick', 'v': 0.45}, {'t': cue['a1']['late'], 'kind': 'tick', 'v': 0.6},
                 {'t': cue['a2']['seven'], 'kind': 'tick', 'v': 0.55}]
K.finish(HERE, 'ep007 C3 · s21-track (S21)', words, takes, lines, end, beats, moves, ev,
         {'lit': lit, 'late': late, 'extra': ex, 'mark_t': cue['a0']['same'], 'old_out': cue['a2']['add'],
          'label_cues': {'a1.ends': 'pay $2,828 on the 30-year: about 195 months', 'a1.late': 'about 15 months late',
                         'a2.seven': 'to finish in 180 months: +$733 a month'},
          'visual_cues': ['a0.pay', 'a0.same', 'a1.doesnt', 'a1.ends', 'a1.late', 'a2.add', 'a2.seven']},
         [cue['a0']['pay'], cue['a1']['ends'], cue['a2']['seven']], hold=1.2)

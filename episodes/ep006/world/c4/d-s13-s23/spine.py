"""Tập 6 · C4 · ĐOẠN D = S13–S23 (Hồi 2: phát lại mọi quãng 20 năm từ 1947). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep006/world/c4/d-s13-s23/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3, có âm trong lặng)
V1/V2 = "bức tường" 715 thanh (c4kit.Strip): mỗi quãng một thanh, x = tháng bắt đầu (Jan 1947 → Aug 2006), cao = sức mua của séc tăng 2 % sau 20 năm
(world/grid.json cpiu20); vạch "first check" (100 %) cố định. Ruth đứng ở thanh cuối (quãng của bà).
B13: thế giới — thanh mọc trái → phải ("every" → "six"); → ĐỒ THỊ: "715 stretches", "Ruth's" = thanh cuối loé + nhãn; "least" = vạch séc đầu;
"tile" = một thanh loé + "each tile: 20 years of US prices". B14 (SỐ NEO, lặng 0,75 s trước câu): "kept" = phán màu (cushion ≥ 100 %, warn < 100 %),
"seventeen" = "kept up: 17 of 715", "one" = "about 1 in 42". B15: đẩy vào cụm trái "Sep 1947 → Jan 1949"; lùi máy, "since" = "none since".
B16: "three" = "typical stretch: prices +3.1% a year"; "eighty" = vạch trung vị 80,7 %; "crates" = hàng 10 thùng (điển hình) sáng 8,07 ở "most".
B17: "fifty" = vạch trung vị séc đều 54,3 %; "eight" = ô nhỏ 20 năm, 8 ô tô; "own" = đối trọng. B19: đẩy vào 1985–2006, "gentler" = các thanh
1990–2006 sáng, còn lại mờ; nhãn 1990s / 2000s / Ruth. B21: "twenty" = tường đổi sang quãng 25 năm (655 thanh), không thanh cushion.
B22: ba dải nhỏ (CPI-U, CPI-W, PCE) — "Social", "gentler". B23: về thế giới, ba thanh (1949, 1966, 2006) loé ở "start" (sang hồi 3)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
SV = K.SV
import json
RAW = json.load(open(os.path.join(K.EP, 'out', 'model.json')))['raw']
S = K.Seg(['S13', 'S14', 'S15', 'S16', 'S17', 'S19', 'S21', 'S22', 'S23'])
B = [
 ('e0', 'S13.1', 'world', 'Mọi tháng bắt đầu từ 1/1947 tới 8/2006, theo giá 20 năm sau.', 'thanh mọc trái → phải dọc bức tường.',
  {'every': '@S13.1:every', 'six': '@S13.1:six', 'followed': '@S13.1:followed'}, ['nốt dữ liệu theo thập kỷ'], 0.42, 'mở', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('e1', 'S13.2', 'chart', '715 quãng; quãng của Ruth là quãng mới nhất.', '715 stretches; thanh cuối loé.',
  {'seven': '@S13.2:seven', 'ruths': '@S13.2:Ruth', 'recent': '@S13.2:recent'}, ['tick'], 0.48, 'chú ý', '—'),
 ('e2', 'S13.3', 'chart', 'Với mỗi quãng: séc tăng 2 % có còn mua bằng séc đầu?', 'vạch "first check" hiện ở "least".',
  {'question': '@S13.3:question', 'least': '@S13.3:least'}, ['tick'], 0.55, 'tò mò', '—'),
 ('e3', 'S13.4', 'chart', 'Mỗi ô là một quãng, xếp theo tháng bắt đầu.', 'một thanh loé + nhãn; trục năm.',
  {'tile': '@S13.4:tile', 'month': '@S13.4:month'}, ['tick'], 0.62, 'hiểu', '—'),
 ('e4', 'S14.1', 'chart', 'Theo kịp ở 17 trên 715.', 'phán màu; kept up: 17 of 715.',
  {'kept': '@S14.1:kept', 'seventeen': '@S14.1:seventeen'}, ['chime'], 0.82, 'sững', '—'),
 ('e5', 'S14.2', 'chart', 'Khoảng 1 trên 42.', 'about 1 in 42.',
  {'one': '@S14.2:one'}, [], 0.76, 'nặng', 'đẩy máy'),
 ('e6', 'S15.1', 'chart', 'Cả 17 bắt đầu từ 9/1947 tới 1/1949.', 'cụm trái + nhãn ngày.',
  {'every': '@S15.1:Every', 'september': '@S15.1:September'}, ['tick'], 0.7, 'chú ý', 'lùi máy'),
 ('e7', 'S15.2', 'chart', 'Từ đó không tháng nào theo kịp, kể cả của Ruth.', 'none since; thanh của Ruth loé.',
  {'since': '@S15.2:Since'}, ['tick'], 0.7, 'nặng', 'lùi máy'),
 ('e8', 'S16.1', 'chart', 'Quãng điển hình: giá tăng 3,1 %/năm.', 'nhãn typical +3.1% a year.',
  {'typical': '@S16.1:typical', 'three': '@S16.1:three'}, [], 0.55, 'bình thản', '—'),
 ('e9', 'S16.2', 'chart', 'Séc tăng điển hình sau 20 năm: 80,7 %.', 'vạch trung vị 80,7 %.',
  {'eighty': '@S16.2:eighty'}, ['tick'], 0.55, 'hiểu', '—'),
 ('f0', 'S16.3', 'chart', 'Tính bằng thùng: phần lớn 10 thùng còn sáng.', 'hàng 10 thùng điển hình sáng 8,07.',
  {'crates': '@S16.3:crates', 'most': '@S16.3:most', 'ten': '@S16.3:ten'}, ['data'], 0.52, 'hiểu', '—'),
 ('f1', 'S17.1', 'chart', 'Séc đều điển hình giữ 54,3 %, khoảng một nửa.', 'vạch trung vị séc đều 54,3 %.',
  {'level': '@S17.1:level', 'fifty': '@S17.1:fifty-four'}, ['tick'], 0.52, 'nặng', '—'),
 ('f2', 'S17.2', 'chart', 'Séc đều điển hình chạm mức cuối của séc tăng khoảng năm 8.', 'ô nhỏ 20 năm, 8 ô tô.',
  {'sunk': '@S17.2:sunk', 'eight': '@S17.2:eight'}, [], 0.48, 'hiểu', '—'),
 ('f3', 'S17.3', 'chart', 'Sức mua so với khởi điểm của mỗi séc, không phải đô la.', 'đối trọng.',
  {'own': '@S17.3:own'}, [], 0.44, 'thận trọng', 'đẩy máy'),
 ('f4', 'S19.1', 'chart', 'Cả những quãng qua thập niên 2000–2010 êm hơn cũng hụt.', 'thanh 1990–2006 sáng; nhãn 1990s / 2000s / Ruth.',
  {'gentler': '@S19.1:gentler', 'ruths': '@S19.1:Ruth', 'short': '@S19.1:short'}, ['tick'], 0.4, 'suy nghĩ', 'lùi máy'),
 ('f5', 'S21.1', 'chart', 'Với 25 năm, không quãng nào theo kịp.', 'tường đổi sang 25 năm (655 thanh).',
  {'twenty': '@S21.1:twenty-five', 'one': '@S21.1:one'}, ['data'], 0.48, 'nặng', '—'),
 ('f6', 'S22.1', 'chart', 'Chỉ số của An sinh xã hội: gần như vậy; thước đo êm hơn: theo kịp nhiều hơn nhưng vẫn hụt phần lớn.', 'ba dải nhỏ CPI-U / CPI-W / PCE.',
  {'social': '@S22.1:Social', 'same': '@S22.1:same', 'gentler': '@S22.1:gentler', 'most': '@S22.1:most'}, ['tick'], 0.36, 'bình thản', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('f7', 'S23.1', 'world', 'Vì sao cùng mức tăng lại ra khác nhau tuỳ tháng bắt đầu?', 'bức tường; ba thanh loé.',
  {'why': '@S23.1:why', 'start': '@S23.1:start'}, ['tick'], 0.44, 'tò mò', '(hết) → hồi 3'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c13', 'mode', 'wWall0', 'cWall', cue['e0']['followed'], cue['e1']['seven'], 1.0, 'lời S13.2 đặt số (715): số chỉ ở đồ thị chính diện (quy tắc 1)', 'whoosh_mode', {}),
    ('m_push15', 'push', 'cWall', 'cLeft', cue['e5']['one'] + 0.5, cue['e6']['every'], 1.2, 'lời S15.1 "every one of those stretches": đẩy vào cụm 17 thanh bên trái', 'whoosh_push', {}),
    ('m_pull15', 'pull', 'cLeft', 'cWall', cue['e7']['since'], S.at('@S15.2:Ruth'), 1.2, 'lời S15.2 "Since then … including Ruth\'s": lùi máy ngay sau "Since", vạch "none since" chạy tới thanh của Ruth đúng "Ruth\'s"', 'whoosh_soft', {'start': cue['e7']['since']}),
    ('m_push19', 'push', 'cWall', 'cRight', S.at('@S17.3$'), cue['f4']['gentler'], 1.3, 'lời S19.1 "the years closest to Ruth\'s own": đẩy vào các quãng 1985–2006', 'whoosh_push', {}),
    ('m_pull21', 'pull', 'cRight', 'cWall', S.at('@S19.1$'), cue['f5']['twenty'], 1.1, 'lời S21.1 "over twenty-five years": lùi máy cho cả tường đổi sang 25 năm', 'whoosh_soft', {}),
    ('m_w23', 'mode', 'cWall', 'wWall1', S.at('@S22.1$'), cue['f7']['why'], 0.7, 'lời S23.1 hỏi vì sao khác nhau theo tháng bắt đầu: về thế giới, sang hồi 3 (người)', 'whoosh_mode', {}),
])
G = K.GRID
dec = sorted({s[:3] for s, _ in G['cpiu20']})
grow = [cue['e0']['every'], cue['e0']['six'] + 0.3]
ev = []
for j, d in enumerate(dec):                                                       # nốt dữ liệu theo thập kỷ khi thanh mọc (cao độ = trung vị thập kỷ)
    vals = sorted(v for s, v in G['cpiu20'] if s.startswith(d))
    ev.append({'t': round(grow[0] + (grow[1] - grow[0]) * j / len(dec), 3), 'kind': 'data', 'v': round(min(1.0, vals[len(vals) // 2] / 100), 3)})
ev += [{'t': cue['e1']['ruths'], 'kind': 'tick', 'v': 0.5}, {'t': cue['e2']['least'], 'kind': 'tick', 'v': 0.45}, {'t': cue['e3']['tile'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['e4']['kept'], 'kind': 'chime'}, {'t': cue['e6']['september'], 'kind': 'tick', 'v': 0.55}, {'t': cue['e7']['since'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['e9']['eighty'], 'kind': 'tick', 'v': 0.5}, {'t': cue['f0']['most'], 'kind': 'data', 'v': 0.807}, {'t': cue['f1']['fifty'], 'kind': 'tick', 'v': 0.35},
       {'t': cue['f4']['gentler'], 'kind': 'tick', 'v': 0.5}, {'t': cue['f5']['twenty'], 'kind': 'data', 'v': 0.69},
       {'t': cue['f6']['social'], 'kind': 'tick', 'v': 0.45}, {'t': cue['f6']['gentler'], 'kind': 'tick', 'v': 0.55}, {'t': cue['f7']['start'], 'kind': 'tick', 'v': 0.5}]
K.finish(HERE, S, 'ep006 C4 · D = S13–S23 (Hồi 2: phát lại 715 quãng)', beats, moves, ev,
         {'grow': [round(x, 3) for x in grow], 'med': {'rising': RAW['median_real_value_2pct_payment_after_20y_pct'], 'level': RAW['median_real_value_level_payment_after_20y_pct']}},
         {'e1.seven': '715 stretches · Jan 1947 to Aug 2006', 'e1.ruths': "Ruth's stretch · ILLUSTRATIVE", 'e3.tile': 'each tile: 20 years of US prices',
          'e4.seventeen': 'kept up: 17 of 715', 'e5.one': 'about 1 in 42', 'e6.september': 'Sep 1947 → Jan 1949', 'e7.since': 'none since',
          'e8.three': 'typical stretch: prices +3.1% a year', 'e9.eighty': 'typical rising check after 20 years: 80.7%',
          'f0.ten': 'typical: about 8 of 10 crates lit', 'f1.fifty': 'typical level check: 54.3%, about half',
          'f2.eight': 'level check there by about year 8', 'f3.own': 'Each check vs its own first check · not dollars',
          'f4.n90': '1990s starts: 0 of 120 kept up', 'f4.m90': 'typical 94.8%', 'f4.n00': '2000 to Aug 2006: 0 of 79 · best 99.5%',
          'f4.ruth': 'Ruth: 90.4%', 'f5.one': '25-year stretches: 0 of 655 kept up', 'f6.cpiu': 'CPI-U: 17 of 715 kept up',
          'f6.cpiw': "CPI-W, Social Security's index: 21 of 715", 'f6.pce': 'PCE, from 1959: 19.2% kept up · typical 88.0%',
          'axis0': '1947', 'axis1': 'Aug 2006', 'm80': '80.7%', 'm54': '54.3%'},
         ['e0.every', 'e1.seven', 'e1.ruths', 'e2.least', 'e3.tile', 'e4.kept', 'e4.seventeen', 'e5.one', 'e6.september', 'e7.since', 'e8.three', 'e9.eighty',
          'f0.most', 'f1.fifty', 'f2.eight', 'f3.own', 'f4.gentler', 'f4.ruths', 'f5.twenty', 'f6.social', 'f6.gentler', 'f7.start'],
         accents=[cue['e4']['seventeen']], anchors=['S14.1'])

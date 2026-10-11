"""Tập 7 · C3 · s01-stack (B01, KEY-1) — lời thật S01.1 + S01.2 (cả cảnh; S01.2 bản hiện tại, không "this week").
  python3 episodes/ep007/world/c3/s01-stack/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Tessa (không mặt, ILLUSTRATIVE) cạnh nhà. Vòng 3 (REVIEW-C3 CHÍNH-4: 3/3 người đọc thấy chồng là "tiết kiệm"): mỗi bó (warn = giá của
khoản dự phòng) ĐI RA TỪ CỬA NHÀ rồi bay sang chồng cạnh nhà — tiền rời nhà, không mọc tại chỗ. "costs" = bó đầu trồi ra ở bậc cửa (nốt dữ liệu).
→ ĐỒ THỊ ngay sau 5 s thế giới (quy tắc 7; số chỉ ở đồ thị, quy tắc 1): bó đầu bay khỏi bậc cửa, CHẠM chồng đúng "borrowing" và cùng lúc hiện
"price of the fallback: $120 a month" (sớm nhất quy tắc cho phép); "three" (lúc lời nói "$320,000") = "$320,000 loan · week of Oct 8, 2026" trên
nhà (đạo diễn #2: trước là "payment", trễ ~4 s); 5 bó sau, mỗi bó ra cửa → bay 0,7 s → chạm chồng ở một nhịp lời (mỗi lần chạm một nốt dữ liệu)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K     # wlib + spine v2 + khung khoá
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S01.1', 'S01.2']], lead=1.4)
A = SV.Anchors(words)
B = [
 ('a0', 'S01.1', 'world', 'Khoản dự phòng của Tessa có giá mỗi tháng.', 'Tessa cạnh nhà; bó tiền đầu trồi ra ở bậc cửa nhà ("costs").',
  {'costs': '@S01.1:costs', 'month': '@S01.1:month'}, ['nốt dữ liệu khi bó ra cửa'], 0.3, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S01.2', 'chart', 'Khoản vay $320,000, tuần 8/10/2026; giá $120 mỗi tháng.', 'chính diện: bó đầu chạm chồng + "price of the fallback: $120 a month" ("borrowing"); nhãn khoản vay trên nhà ("three"); mỗi nhịp một bó từ cửa ra chồng.',
  {'borrowing': '@S01.2:borrowing', 'three': '@S01.2:three'}, ['nốt dữ liệu mỗi bó chạm', 'tick khi nhãn hiện'], 0.45, 'tò mò', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wS0', 'wS', 0.0, cue['a0']['costs'], 2.0, 'mở đoạn: máy lại gần Tessa và cửa nhà trước khi bó đầu ra ("costs")', 'whoosh_air', {}),
    ('mode', 'wS', 'cS', cue['a0']['month'], cue['a1']['borrowing'], 0.8,
     'giá $120 chỉ hiện ở chế độ đồ thị (quy tắc 1) → đồ thị ngay sau 5 s thế giới (quy tắc 7), xong trước khi bó đầu chạm chồng', 'whoosh_mode', {'start': 5.0})])
FLY = 0.7
land = [cue['a1']['borrowing'], A.at('@S01.2:dollars'), A.at('@S01.2:city'), A.at('@S01.2:payment'), A.at('@S01.2:biggest'), A.at('@S01.2:bill')]
assert moves[1]['t1'] <= land[0] - 0.02, 'đồ thị phải xong trước khi bó đầu chạm (nhãn giá hiện cùng lúc chạm)'
assert all(b - a >= FLY / 2 for a, b in zip(land, land[1:])), 'tối đa 2 bó bay cùng lúc'
nb = len(land)
sk, ev = K.steps(land, [K.G['bundle_usd'] * (i + 1) for i in range(nb)], ramp=0.05, v0=0.0, pitch=lambda v: 0.25 + 0.5 * v / (K.G['bundle_usd'] * nb))
ev += [{'t': cue['a0']['costs'], 'kind': 'data', 'v': 0.2}, {'t': cue['a1']['three'], 'kind': 'tick', 'v': 0.55}]
K.finish(HERE, 'ep007 C3 · s01-stack (S01)', words, takes, lines, end, beats, moves, ev,
         {'stack': sk, 'land': [round(t, 3) for t in land], 'fly': FLY, 'out0': cue['a0']['costs'],
          'label_cues': {'a1.borrowing': 'price of the fallback:', 'a1.three': '$320,000 loan · week of Oct 8, 2026'},
          'visual_cues': ['a0.costs', 'a1.borrowing', 'a1.three']}, [cue['a0']['costs'], cue['a1']['borrowing']], hold=1.2)

"""Tập 7 · độ dài THẬT trên timeline sau khi sinh lời (lệnh G1 (b): ≥ 8:10 trước render; ≥ 8:00 ở C5, lessons T6-1).
Cùng phép tính của nhà máy (`toolkit/factory/build.py` do_resolve): tổng theo cảnh (độ dài take giọng + tail), mỗi cảnh làm tròn tới khung 30 fps.
tail = max(1,0; hold câu cuối cảnh) — như `episode.yaml` Tập 5 (S20 hold 2 → tail 2,0) — cộng ident 3 s ở cảnh có `=== IDENT` theo sau.
Kiểm ngược Tập 5: timeline nhà máy 465,67 s = bản cuối 7:45,7. Mid-roll: ranh giới sau cảnh của câu `<!-- mid-roll` trong script.md
(S12.4 hold 1,5): ≥ 120 s từ đầu và cuối, lặng ≥ 1 s.
    python3 episodes/ep007/story/timeline_len.py   → in bảng + ghi episodes/ep007/out/timeline-len.json"""
import json
import re

EP = '/home/user/crux-lab/episodes/ep007'
FPS, TAIL, IDENT_S, MIN_S, TARGET_S = 30, 1.0, 3.0, 540.0, 540.0
LINE = re.compile(r'^(S\d\d)\.(\d+)\s.*?<!--.*?(?:hold:\s*([\d.]+))?\s*-->')

holds, order, ident_after, last = {}, [], set(), None
for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
    m = LINE.match(ln)
    if m:
        sc = m.group(1)
        if sc not in order:
            order.append(sc)
        holds[sc] = float(m.group(3) or 0)   # hold của câu cuối cùng trong cảnh
        last = sc
    elif ln.startswith('=== IDENT') and last:
        ident_after.add(last)
rep = json.load(open(f'{EP}/review-g1/voice-scenes.json'))
t, rows = 0.0, []
for sc in order:
    tail = max(TAIL, holds[sc]) + (IDENT_S if sc in ident_after else 0)
    dur = round(round((rep[sc]['duration'] + tail) * FPS) / FPS, 4)
    rows.append({'scene': sc, 'start': round(t, 3), 'voice': rep[sc]['duration'], 'tail': tail, 'dur': dur})
    t += dur
total = round(t, 3)
mrs = []
for sc in ('S09', 'S24'):   # lab: 2 mid-roll, giữa khoảng lặng 1,5 s sau S09.3 / S24.3
    r = next(r for r in rows if r['scene'] == sc)
    t_ = r['start'] + r['voice'] + 0.25
    mrs.append({'after': sc, 't': round(t_, 2), 'ok': bool(t_ >= 120 and total - t_ >= 120 and max(TAIL, holds[sc]) >= 1)})
out = {'total_s': total, 'total': f'{int(total // 60)}:{total % 60:04.1f}', 'lab_9_11': MIN_S <= total <= 660.0,
       'midrolls': mrs, 'el_chars_last_run': sum(v.get('charsSpent', 0) for v in rep.values()), 'scenes': rows}
json.dump(out, open(f'{EP}/out/timeline-len.json', 'w'), indent=1, ensure_ascii=False)
for r in rows:
    print(f"{r['scene']} {r['start']:7.2f} lời {r['voice']:6.2f} tail {r['tail']:.1f}")
print(f"tổng {out['total']} ({total} s) · lab 9:00–11:00 {'ĐẠT' if out['lab_9_11'] else 'TRƯỢT'} · mid-roll {mrs}")

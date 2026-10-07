"""Tóm tắt số đo khung hình (frames.py) → bảng: % chỉ có chữ, từ mới trên màn hình/phút (bền ≥ 2 giây), từ hiện trung bình, % đồ hoạ chuyển động, cắt cứng (bộ dò)."""
import json, sys
from collections import Counter
for p in sys.argv[1:]:
    m = json.load(open(p)); R = m['rows']; n = len(R)
    c = Counter(r['cls'] for r in R)
    new = 0
    T = [Counter(r['text'].split()) for r in R] + [Counter()]
    for i in range(n):   # từ mới = có ở giây i, không có ở giây i−1, CÒN ở giây i+1 (lọc nhiễu OCR)
        prev = T[i - 1] if i else Counter()
        new += sum(((T[i] - prev) & T[i + 1]).values())
    print(json.dumps({'file': p.split('/')[-1], 'seconds': n, 'text_only_pct': round(100 * c['text_only'] / n, 1),
                      'graphic_motion_pct': round(100 * c['graphic_motion'] / n, 1), 'graphic_static_pct': round(100 * c['graphic_static'] / n, 1),
                      'new_words_per_min': round(new / n * 60, 1), 'visible_words_avg': round(sum(r['words'] for r in R) / n, 1),
                      'hard_cuts_detector': len(m['cuts'])}))

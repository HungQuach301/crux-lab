"""Mẫu kiểm mù C2: lời thuần của story/script.md (bỏ ID, vai, thẻ cảm xúc, claim, ghi chú); dòng trống giữa cảnh;
[on screen: …] chỉ ở câu lời nói "on screen".  python3 c2/sample.py > c2/sample.txt"""
import re
ON = {'S06.1': '[on screen: $2,362 a month, principal and interest]'}
out, cur = [], None
for ln in open('story/script.md', encoding='utf-8'):
    m = re.match(r'^(S\d\d)\.(\d+)\s+(?:\{\w+\}\s+)?(?:\[[a-z ]+\]\s+)?(.+?)\s*<!--', ln)
    if not m: continue
    if cur and m.group(1) != cur: out.append('')
    cur = m.group(1); out.append(m.group(3))
    sid = f'{m.group(1)}.{m.group(2)}'
    if sid in ON: out.append(ON[sid])
print('\n'.join(out))

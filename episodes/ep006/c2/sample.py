"""Kiểm mù C2: lời thuần của story/script.md (bỏ ID, vai, thẻ cảm xúc, claim); dòng trống giữa cảnh.  python3 c2/sample.py > c2/sample.txt"""
import re
out, cur = [], None
for ln in open('story/script.md', encoding='utf-8'):
    m = re.match(r'^(S\d\d)\.(\d+)\s+(?:\{\w+\}\s+)?(?:\[[a-z ]+\]\s+)?(.+?)\s*<!--', ln)
    if not m: continue
    if cur and m.group(1) != cur: out.append('')
    cur = m.group(1); out.append(m.group(3))
print('\n'.join(out))

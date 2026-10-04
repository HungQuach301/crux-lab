"""Tập 3 — kiểm máy kịch bản C2 (cổng TỰ ĐỘNG (a)): claim 100%, S10 = 0, "US only" + "history, not a forecast", luật lời ASR.
S10 dùng chính danh sách regex của checks/py/r_content.py (đọc, không sửa). In báo cáo; mã thoát 0 khi đạt.
  python3 episodes/ep003/story/check_script.py [episodes/ep003/story/script.md]"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
import r_content as rc  # noqa: E402

script = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'script.md')
claims = set(re.findall(r'^\| `([a-z0-9_]+)`', open(os.path.join(os.path.dirname(HERE), 'numbers.md')).read(), re.M))
lines = []
for ln in open(script):
    m = re.match(r'^(S\d{2}\.\d+[a-z]?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$', ln.rstrip('\n'))
    if m:
        lines.append(m.groups())
fail = []
words = 0
for sid, text, cl, note in lines:
    spoken = re.sub(r'\[[a-z ]+\]\s*', '', text)
    words += len(spoken.split())
    ids = [c.strip(' `') for c in re.split(r'[,;]', cl) if c.strip(' `—-')]
    bad = [c for c in ids if c not in claims]
    if bad:
        fail.append(f'{sid}: claim không có trong numbers.md: {bad}')
    if re.search(r'\d', spoken) and not ids:
        fail.append(f'{sid}: câu có số nhưng không có claim')
    low = spoken.lower()
    low_nf = re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low)
    for k, pats in (('ADVICE', rc.ADVICE), ('FORECAST', rc.FORECAST), ('FOUR', rc.FOUR), ('WE_BAD', rc.WE_BAD)):
        for p in pats:
            if re.search(p, low_nf if k == 'FORECAST' else low, re.M):
                fail.append(f'{sid}: S10 {k} /{p}/: {spoken}')
    if re.search(r'\b(1[89]|20)\d\d\s*[-–]\s*(1[89]|20)?\d\d\b', spoken):
        fail.append(f'{sid}: ASR dải năm có gạch nối')
    if re.search(r'\bminus\b|(^|\s)[-−]\d', spoken, re.I):
        fail.append(f'{sid}: ASR minus/số âm')
    if re.search(r'[%±→×]', spoken):
        fail.append(f'{sid}: ASR ký hiệu trong lời: {re.findall(r"[%±→×]", spoken)}')
alltext = ' '.join(t for _, t, _, _ in lines)
if not re.search(r'\bUS only\b|\bU\.S\. only\b', alltext):
    fail.append('thiếu "US only" trong lời')
if not re.search(r'history,? not a forecast', alltext, re.I):
    fail.append('thiếu "history, not a forecast" trong lời')
print(f'{len(lines)} câu, {words} từ lời; claim dùng: {len({c.strip(" `") for _, _, cl, _ in lines for c in re.split(r"[,;]", cl) if c.strip(" `—-")})}')
print('ĐẠT' if not fail else 'TRƯỢT', *fail, sep='\n  ')
sys.exit(1 if fail else 0)

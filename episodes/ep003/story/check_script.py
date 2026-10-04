"""Tập 3 — kiểm máy kịch bản C2 (cổng TỰ ĐỘNG (a)). v2 sau REVIEWER (trước khi chạy).
Chặn: claim 100% (lời và chữ trích trong ghi chú hình); câu có số (chữ số hoặc từ chỉ số) phải có claim; S10 = 0 (regex của
checks/py/r_content.py, đọc, không sửa) trên lời và chữ trên hình; "US only" + "history, not a forecast" trong lời; luật ASR (episode.md §3.1);
luật tập: câu giả định (claim ctx_hypothetical) nằm ở cảnh cold open S01 và đứng TRƯỚC mọi claim kết quả lịch sử; cảnh nêu tỉ lệ toàn kỳ
phải nêu cả hai thời kỳ. Cảnh báo (không chặn): 3.72% và 3.53% cùng cảnh; 17 tháng thật mà cảnh thiếu tỉ lệ toàn kỳ.
  python3 episodes/ep003/story/check_script.py [script.md]"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
import r_content as rc  # noqa: E402

script = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'script.md')
claims = set(re.findall(r'^\| `([a-z0-9_]+)`', open(os.path.join(os.path.dirname(HERE), 'numbers.md')).read(), re.M))
RESULT = re.compile(r'^(share_|starts|min_|max_|median_|latest_|real_windows|worst_real|last_lost|near_double|nonoverlap|min_multiple|max_multiple)')
NUMWORD = re.compile(r'\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|'
                     r'nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|half|halves|quarter|percent)\b', re.I)
ASR_SYM = re.compile(r'[%±→×$~≈<>/]|\b\d+(\.\d+)?x\b')
fail, warn, lines = [], [], []
for n, ln in enumerate(open(script, encoding='utf-8'), 1):
    ln = ln.rstrip('\n')
    m = re.match(r'^(S\d{2}\.\d+[a-z]?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$', ln)
    if m:
        lines.append(m.groups())
    elif re.match(r'^\W*S\d', ln) and not re.match(r'^#+\s*S\d', ln):
        fail.append(f'dòng {n}: giống câu kịch bản nhưng sai định dạng: {ln[:60]}')
if not lines:
    fail.append('không đọc được câu nào')


def s10(sid, txt, where):
    low = txt.lower().replace('’', "'")
    low_nf = re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low)
    for k, pats in (('ADVICE', rc.ADVICE), ('FORECAST', rc.FORECAST), ('FOUR', rc.FOUR), ('WE_BAD', rc.WE_BAD)):
        for p in pats:
            if re.search(p, low_nf if k == 'FORECAST' else low, re.M):
                fail.append(f'{sid} ({where}): S10 {k} /{p}/: {txt[:80]}')


words, used, scene_claims = 0, set(), {}
first_result, hyp_at = None, None
for i, (sid, text, cl, note) in enumerate(lines):
    spoken = re.sub(r'\[[a-z\- ]+\]\s*', '', text)
    words += len(spoken.split())
    ids = [c.strip(' `') for c in re.split(r'[,;]', cl) if c.strip(' `—-')]
    used |= set(ids)
    scene_claims.setdefault(sid.split('.')[0], set()).update(ids)
    bad = [c for c in ids if c not in claims]
    if bad:
        fail.append(f'{sid}: claim không có trong numbers.md: {bad}')
    if (re.search(r'\d', spoken) or NUMWORD.search(spoken)) and not ids:
        fail.append(f'{sid}: câu có số (chữ số hoặc từ chỉ số) nhưng không có claim: {spoken[:70]}')
    s10(sid, spoken, 'lời')
    for q in re.findall(r'"([^"]+)"|“([^”]+)”', note):
        q = q[0] or q[1]
        s10(sid, q, 'hình')
        if re.search(r'\d', q) and not ids:
            fail.append(f'{sid}: chữ trên hình có số nhưng câu không có claim: "{q}"')
    if re.search(r'\b(1[89]|20)\d\ds?\s*[-–—]\s*((1[89]|20)?\d\ds?)\b', spoken):
        fail.append(f'{sid}: ASR dải năm có gạch nối')
    if re.search(r'\bminus\b|(^|\s)[-−]\d', spoken, re.I):
        fail.append(f'{sid}: ASR minus/số âm')
    if ASR_SYM.search(spoken):
        fail.append(f'{sid}: ASR ký hiệu trong lời: {ASR_SYM.findall(spoken)[:3]}')
    if 'ctx_hypothetical' in ids and hyp_at is None:
        hyp_at = (i, sid)
    if first_result is None and any(RESULT.match(c) for c in ids):
        first_result = (i, sid)
if hyp_at is None:
    fail.append('luật tập: không có câu giả định (claim ctx_hypothetical)')
else:
    if not hyp_at[1].startswith('S01.'):
        fail.append(f'luật tập: câu giả định ở {hyp_at[1]}, không ở cold open S01')
    if first_result and first_result[0] < hyp_at[0]:
        fail.append(f'luật tập: kết quả lịch sử {first_result[1]} đứng trước câu giả định {hyp_at[1]}')
for sc, ids in scene_claims.items():
    if 'share_tbills_above_double_pct' in ids and not {'share_above_double_1950_1989_pct', 'share_tbills_above_double_starts_since_1990_pct'} <= ids:
        fail.append(f'luật tập: {sc} nêu tỉ lệ toàn kỳ mà thiếu một trong hai thời kỳ')
    if {'tb3ms_latest_pct', 'doubling_rate_pct_per_year'} <= ids:
        warn.append(f'{sc}: 3.72% và 3.53% cùng cảnh — cần chú giải (đầu bài)')
    if 'starts_with_guarantee' in ids and 'share_tbills_above_double_pct' not in ids:
        warn.append(f'{sc}: 17 tháng thật mà cảnh thiếu tỉ lệ toàn kỳ')
alltext = ' '.join(t for _, t, _, _ in lines)
if not re.search(r'\bUS only\b|\bU\.S\. only\b', alltext):
    fail.append('thiếu "US only" trong lời')
if not re.search(r'history,? not a forecast', alltext, re.I):
    fail.append('thiếu "history, not a forecast" trong lời')
print(f'{len(lines)} câu, {words} từ lời; {len(used)} claim')
print('ĐẠT' if not fail else 'TRƯỢT', *fail, sep='\n  ')
if warn:
    print('Cảnh báo:', *warn, sep='\n  ')
sys.exit(1 if fail else 0)

"""Tập 4 — kiểm máy kịch bản C2 (cổng TỰ ĐỘNG (a)); viết trước khi có kịch bản. Lệnh trực tiếp, không agent.
CHẶN: claim tồn tại trong numbers.md; câu có số (chữ số hoặc từ chỉ số) phải có claim; S10 = 0 (regex checks/py/r_content.py,
chỉ đọc) trên lời và chữ trích trên hình; "US only" + "history, not a forecast" trong lời; luật ASR (episode.md §3.1);
móc story.md §1: trong 5 s đầu có câu hỏi (?) hoặc câu được–mất mang claim; lời hứa ("By the end"/"you'll know") trước 0:30;
không câu ràng buộc (US only / history / assumptions) nằm giữa câu hỏi đầu và lời hứa.
CẢNH BÁO: mật độ số (> 2 số mới một câu; > 1 số mới / 8 s trượt cửa sổ), câu ngưỡng thiếu "like"/"average" (claim-risk hồ sơ).
Thời gian ước = 140 từ/phút + 0,4 s mỗi câu.
  python3 episodes/ep004/story/check_script.py [script.md] [--hooks hooks.md]"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
import r_content as rc  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith('--')]
script = args[0] if args else os.path.join(HERE, 'script.md')
hooks = sys.argv[sys.argv.index('--hooks') + 1] if '--hooks' in sys.argv else os.path.join(HERE, 'hooks.md')
claims = set(re.findall(r'^\| `([a-z0-9_]+)`', open(os.path.join(os.path.dirname(HERE), 'numbers.md')).read(), re.M))
NUMWORD = re.compile(r'\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|'
                     r'nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|half|halves|quarter|percent|double|triple|tripled|doubled)\b', re.I)
NUMTOK = re.compile(r'\$?\d[\d,]*(\.\d+)?%?|\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred|thousand|million|half|tripled|doubled)\b', re.I)
ASR_SYM = re.compile(r'[%±→×~≈<>/]|\b\d+(\.\d+)?x\b')
PROMISE = re.compile(r"\bby the end\b|\byou'll (know|see|have)\b|\byou will (know|see)\b", re.I)
CONSTRAINT = re.compile(r'\bUS only\b|\bU\.S\. only\b|history,? not a forecast|\bassum|\bnot adjusted|\bonly federal\b', re.I)
WPM = 140


def parse(path):
    out = []
    for n, ln in enumerate(open(path, encoding='utf-8'), 1):
        m = re.match(r'^((?:S|H)\d{1,2}[\.\-]\d+[a-z]?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$', ln.rstrip('\n'))
        if m:
            out.append(m.groups())
    return out


def spoken(t):
    return re.sub(r'\[[a-z\- ]+\]\s*', '', t)


def s10(sid, txt, where, fail):
    low = txt.lower().replace('’', "'")
    low_nf = re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low)
    for k, pats in (('ADVICE', rc.ADVICE), ('FORECAST', rc.FORECAST), ('FOUR', rc.FOUR), ('WE_BAD', rc.WE_BAD)):
        for p in pats:
            if re.search(p, low_nf if k == 'FORECAST' else low, re.M):
                fail.append(f'{sid} ({where}): S10 {k} /{p}/: {txt[:80]}')


def sentence_rules(lines, fail, warn):
    t, seen, events = 0.0, set(), []
    for sid, text, cl, note in lines:
        sp = spoken(text)
        ids = [c.strip(' `') for c in re.split(r'[,;]', cl) if c.strip(' `—-')]
        bad = [c for c in ids if c not in claims]
        if bad:
            fail.append(f'{sid}: claim không có trong numbers.md: {bad}')
        if (re.search(r'\d', sp) or NUMWORD.search(sp)) and not ids:
            fail.append(f'{sid}: câu có số nhưng không có claim: {sp[:70]}')
        s10(sid, sp, 'lời', fail)
        for q in re.findall(r'"([^"]+)"|“([^”]+)”', note):
            q = q[0] or q[1]
            s10(sid, q, 'hình', fail)
            if re.search(r'\d', q) and not ids:
                fail.append(f'{sid}: chữ trên hình có số nhưng câu không có claim: "{q}"')
        if re.search(r'\b(1[89]|20)\d\ds?\s*[-–—]\s*((1[89]|20)?\d\ds?)\b', sp):
            fail.append(f'{sid}: ASR dải năm có gạch nối')
        if re.search(r'\bminus\b|(^|\s)[-−]\d', sp, re.I):
            fail.append(f'{sid}: ASR minus/số âm')
        if ASR_SYM.search(sp):
            fail.append(f'{sid}: ASR ký hiệu trong lời: {ASR_SYM.findall(sp)[:3]}')
        new = [m.group(0).lower() for m in NUMTOK.finditer(sp) if m.group(0).lower() not in seen]
        seen |= set(new)
        if len(new) > 2:
            warn.append(f'{sid}: {len(new)} số mới trong một câu {new}')
        events += [(t, x) for x in new]
        if any(c.startswith('threshold_joint') for c in ids) and not re.search(r'\blike\b|\baverage\b', sp, re.I):
            warn.append(f'{sid}: câu ngưỡng thiếu "like/average" (claim-risk hồ sơ)')
        t += len(sp.split()) / WPM * 60 + 0.4
    dense = [round(a) for i, (a, _) in enumerate(events) if i + 2 < len(events) and events[i + 2][0] - a < 8]
    if dense:
        warn.append(f'mật độ: ≥ 3 số mới trong 8 s tại ~{dense[:8]} s')
    return t


def hook_rules(name, lines, fail):
    t, q_at, p_at, first5 = 0.0, None, None, False
    for i, (sid, text, cl, note) in enumerate(lines):
        sp = spoken(text)
        ids = [c for c in re.split(r'[,;]', cl) if c.strip(' `—-')]
        if t < 5 and ('?' in sp or ids):
            first5 = True
        if q_at is None and '?' in sp:
            q_at = (i, t)
        if p_at is None and PROMISE.search(sp):
            p_at = (i, t)
        t += len(sp.split()) / WPM * 60 + 0.4
    if not first5:
        fail.append(f'{name}: 5 s đầu không có câu hỏi hay câu được–mất mang claim')
    if p_at is None or p_at[1] >= 30:
        fail.append(f'{name}: lời hứa không có trước 0:30 (ước {None if p_at is None else round(p_at[1], 1)} s)')
    if q_at and p_at and q_at[0] < p_at[0]:
        for sid, text, _, _ in lines[q_at[0] + 1:p_at[0]]:
            if CONSTRAINT.search(spoken(text)):
                fail.append(f'{name}: câu ràng buộc {sid} chen giữa câu hỏi và lời hứa')
    return (None if q_at is None else round(q_at[1], 1)), (None if p_at is None else round(p_at[1], 1))


fail, warn = [], []
L = parse(script)
if not L:
    fail.append('không đọc được câu nào')
dur = sentence_rules(L, fail, warn)
alltext = ' '.join(spoken(t) for _, t, _, _ in L)
if not re.search(r'\bUS only\b|\bU\.S\. only\b', alltext):
    fail.append('thiếu "US only" trong lời')
if not re.search(r'history,? not a forecast', alltext, re.I):
    fail.append('thiếu "history, not a forecast" trong lời')
s01 = [x for x in L if x[0].startswith('S01.')]
q, p = hook_rules('script S01', s01, fail)
print(f'{len(L)} câu, {len(alltext.split())} từ, ~{dur / 60:.1f} phút ước; móc S01: câu hỏi {q} s, lời hứa {p} s')
if os.path.exists(hooks):
    H = parse(hooks)
    for h in sorted({x[0].split('.')[0].split('-')[0] for x in H}):
        hl = [x for x in H if x[0].split('.')[0].split('-')[0] == h]
        hf, hw = [], []
        sentence_rules(hl, hf, hw)
        q, p = hook_rules(f'hooks {h}', hl, hf)
        fail += hf
        print(f'  {h}: {len(hl)} câu; câu hỏi {q} s, lời hứa {p} s; {"ĐẠT" if not hf else "TRƯỢT"}')
print('ĐẠT' if not fail else 'TRƯỢT', *fail, sep='\n  ')
if warn:
    print('Cảnh báo (không chặn):', *warn, sep='\n  ')
sys.exit(1 if fail else 0)

"""MẪU kiểm máy kịch bản C2 (từ Tập 6; gốc: episodes/ep005/story/check_script.py). Chép vào episodes/epNNN/story/check_script.py rồi sửa
các dòng đánh dấu `# TẬP:` (dàn nhân vật, tên đã dùng, số cốt lõi, từ viết tắt phải có dạng đầy đủ), hoặc chạy thẳng mẫu trên một kịch bản:
  python3 playbook/templates/check_script.py episodes/epNNN/story/script.md
Dòng kịch bản: `Sxx.n {role} [emotion] lời <!-- claims: id, id; hold: s -->`.

TỐC ĐỘ ĐỌC (tổng kết Tập 5 §2c/§3.1, chủ dự án duyệt 08/10; đo lại sau mỗi tập bằng `tongket-t5/measure_pace.py`, đổi hằng khi lệch > 2 %):
  - WPS_SPEECH = 2,75 từ nói / giây lời — Eric `eleven_v3`, stability 0.5, speed 0.9 (Tập 4 2,72 · Tập 5 2,75). Dùng cho mốc giây trong tập:
    móc M1–M6, mật độ số, mid-roll, khuôn tỉ lệ (cộng hold + ident).
  - WPS_TOTAL = 2,52 từ nói / giây thời lượng — gồm phần nhà máy thêm ngoài lời (giữ, ident, đuôi cảnh; Tập 4 2,53 · Tập 5 2,51).
    Dùng cho ĐỘ DÀI CẢ TẬP. Kiểm ngược: Tập 4 → 484 s (thật 481,6), Tập 5 → 463 s (thật 465,7).
  - Đổi giọng/model/speed → đo lại hai hằng. Thước cũ 2,4 từ/s (≈ 8:19 cho Tập 5, thật 7:46) bỏ.
ĐỘ DÀI: `101` đích G1 ≥ 8:15 ước (495 s ≈ 1.250 từ nói; dư ≈ 15 s cho sai số), ≤ 9:00. Thiếu → CHẶN ở C2: WRITER mới thêm CHẤT có nguồn
  (không độn, story §4) ≤ 2 vòng; vẫn thiếu → nêu ở G1 (ngắn hơn, bỏ mid-roll — chủ dự án chọn), chạy lại với `--g1-short` khi đã duyệt.

CHẶN (exit 1):
  - claim ID có trong numbers.md; mọi số đọc lên (chữ số + số đọc bằng chữ) khớp giá trị/hiển thị/định nghĩa của claim gắn câu
    (cho phép ×100, ÷100, ÷12 tháng→năm, làm tròn); câu có số mà không claim → CHẶN
  - chữ trên hình (beats.md, cột on-screen) có số → khớp claim của nhịp; nhịp mang nhân vật / ví dụ $ phải có ILLUSTRATIVE
  - "US only" và "history, not a forecast" có trong lời
  - lời khuyên / mệnh lệnh / dự báo / "we" sai: regex S10 của checks/py/r_content.py (chỉ đọc) + danh sách động từ mệnh lệnh đầu câu
  - ASR (episode.md §3.1): dải năm có gạch nối, "minus", số âm, ký hiệu %/×/≈/~ trong lời, viết tắt có gạch nối; viết tắt trong
    FULL_FORM phải có dạng đầy đủ ở lần đầu
  - mật độ: ≤ 2 số mới mỗi cảnh; số cốt lõi (CORE) đọc bằng số đúng 1 lần, nhắc lại ≥ 3 lần bằng lời
  - móc (episode.md §3.9) ở WPS_SPEECH: mọi câu bắt đầu trước 1:00 có vai; M1 câu hook đầu kết thúc ≤ 5,0 s; M2 lời hứa ≤ 30 s;
    M3 câu hỏi ≤ 30 s; M4 khối constraint/define liền ≤ 10 s trong 0:00–1:00; M5 hook/nhân vật quay lại ≤ 45 s (sau lời hứa);
    M6 (story §2b.2) mỗi câu vai `promise_character` được trả — tên nhân vật trong CAST xuất hiện — ≤ 90 s sau khi câu hứa kết thúc
  - thẻ cảm xúc 2–4; độ dài theo format (ở WPS_TOTAL); mid-roll ở ranh giới hồi, sau hold ≥ 1 s, cách đầu và cuối ≥ 120 s
  - tên nhân vật không trùng tên đã dùng (BANNED_NAMES)
CẢNH BÁO: ≥ 3 số mới trong 8 s; mốc trong ±5 % quanh ngưỡng (nêu tên, CHARTER §4); khuôn tỉ lệ story §4 lệch > ±5 điểm (THAM KHẢO);
  hooks.md không đủ 3 phương án; câu đỉnh cảm xúc (vai `peak`) > 15 từ (story §2b.4, REVIEWER quyết).
  python3 check_script.py [script.md] [--g1-short] [--cast A,B,C]"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
while ROOT != '/' and not os.path.isdir(os.path.join(ROOT, 'checks', 'py')):
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'checks', 'py'))
try:
    import r_content as rc  # chỉ đọc regex S10
    S10 = {'ADVICE': rc.ADVICE, 'FORECAST': rc.FORECAST, 'WE_BAD': rc.WE_BAD}
except Exception as e:  # noqa: BLE001
    print('cảnh báo: không import được r_content:', e)
    S10 = {'ADVICE': [r"\byou (should|must|need to|ought to|have to|'d better)\b"], 'FORECAST': [r'\bwill (rise|fall)\b'], 'WE_BAD': [r'\bwe (all|should|need)\b']}

SCRIPT = os.path.abspath(next((a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith('--') and sys.argv[i - 1] != '--cast'), os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script.md')))
HERE = os.path.dirname(SCRIPT)
G1_SHORT = '--g1-short' in sys.argv   # chủ dự án đã duyệt ở G1: tập ngắn hơn đích, không độn
BEATS, HOOKS = os.path.join(HERE, 'beats.md'), os.path.join(HERE, 'hooks.md')
WPS_SPEECH = 2.75   # từ nói / giây lời (Eric eleven_v3, speed 0.9; Tập 4–5, tongket-t5 §2c)
WPS_TOTAL = 2.52    # từ nói / giây thời lượng cả tập (gồm phần ngoài lời của nhà máy; Tập 4–5)
WPS = WPS_SPEECH    # mốc giây trong tập (móc, mật độ, mid-roll)
IDENT_S = 3.0
FORMAT = '101'
_yaml = os.path.join(os.path.dirname(HERE), 'episode.yaml')
if os.path.exists(_yaml):
    _m = re.search(r'^format:\s*[\'"]?(\w+)', open(_yaml, encoding='utf-8').read(), re.M)
    FORMAT = _m.group(1) if _m else FORMAT
LEN_LIMITS = {'101': (495, 540), 'lab': (540, 660)}   # (đích tối thiểu ước, tối đa cứng) giây; 101 ≥ 8:15 (§3.1)
BANNED_NAMES = {'Nora', 'Walt', 'Anjali', 'Leah', 'Dana', 'Rosa', 'Frank', 'Maya', 'Grace', 'Owen', 'Victor'}   # TẬP: thêm tên tập trước
CAST = ['Ruth', 'Carl', 'Edna']   # TẬP (ep006): Ruth = nhân vật dẫn đường (Aug 2006), Carl (Jan 1966), Edna (Jan 1949) đối trọng; tên nhân vật minh hoạ của tập (nhân vật dẫn đường đứng đầu); hoặc --cast A,B,C
if '--cast' in sys.argv:
    CAST = [x for x in sys.argv[sys.argv.index('--cast') + 1].split(',') if x]
PERSON_PROMISE = re.compile(r'\b(meet|buyers?|people|person|illustrative|retirees?|borrowers?|families|workers?|savers?)\b', re.I)
CORE = [('windows_2pct_kept_up_20y', r'\b17\b')]   # TẬP (ep006): 17 of 715 — [(claim_id, regex số đọc lên)] số cốt lõi — đọc bằng số 1 lần, nhắc lại ≥ 3 lần bằng lời
FULL_FORM = {'PCE': 'personal consumption expenditures', 'CPI': 'consumer price index'}   # TẬP (ep006): {'PMI': 'private mortgage insurance'} viết tắt phải có dạng đầy đủ ở lần đầu
ROLES = ('hook', 'promise', 'question', 'constraint', 'define', 'promise_character', 'peak')
IMPERATIVE = re.compile(r'(^|[.!?;:]\s+|^(so|and|but|now),?\s+)(say|take|imagine|picture|look|think|remember|check|compare|ask|wait|buy|sell|keep|consider|make|avoid|'
                        r'start|stop|talk|plan|call|get|use|try|put|run|don\'t|do not|never|always|let\'s|save|rent|refinance|shop)\b', re.I)
ADVICE_EXTRA = re.compile(r"\b(you should|you need|you'd want|it's time to|best time|good time to|lock in|don't miss|we recommend|we suggest|worth it to buy|"
                          r"right move|smart move|better to (buy|wait|rent))\b", re.I)
WORDNUM = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
           'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'hundred': 100, 'thousand': 1000}
WORD_EXEMPT = [r'\b2000s and 2010s\b']   # TẬP (ep006): tên thập niên theo luật claim-risk "ran through the 2000s and 2010s" (by_decade_*), không phải số liệu; cụm số không phải số liệu (vd r'\bthree illustrative buyers\b')
TEMPLATE = {'hook': 8, 'concept': 25, 'experiment': 30, 'buyers': 25, 'limits': 12}   # khuôn 101 (story §4)

# ---------- numbers.md ----------
NUM_MD = open(os.path.join(os.path.dirname(HERE), 'numbers.md'), encoding='utf-8').read()
CLAIM = {}
for m in re.finditer(r'^\| `([^`]+)` \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|', NUM_MD, re.M):
    raw, rest = m.group(1), ' '.join(m.group(2, 3, 4, 5))   # giá trị, hiển thị, định nghĩa, nguồn
    parts = [p.strip() for p in raw.split('/')]
    ids = [parts[0]] + [p if '_' in p and p.split('_')[0] == parts[0].split('_')[0] else parts[0].split('_')[0] + '_' + p for p in parts[1:]]
    for i in ids:
        CLAIM[i] = rest


def allowed(ids):
    vals = set()
    for c in ids:
        for tok in re.findall(r'\d[\d,]*(?:\.\d+)?', CLAIM.get(c, '')):
            x = float(tok.replace(',', ''))
            for y in (x, x * 100, x / 100, x / 12, x * 12):
                vals |= {round(y, 2), round(y, 1), round(y)}
    return vals


# ---------- spoken length ----------
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']


def words_int(n):
    if n < 20:
        return 1
    if n < 100:
        return 1
    if n < 1000:
        return 2 + (words_int(n % 100) if n % 100 else 0)
    if n < 1_000_000:
        return words_int(n // 1000) + 1 + (words_int(n % 1000) if n % 1000 else 0)
    return words_int(n // 1_000_000) + 1 + (words_int(n % 1_000_000) if n % 1_000_000 else 0)


def spoken_words(text):
    """số từ khi đọc ra: số → chữ (năm 19xx/20xx = 2 từ; thập phân đọc từng chữ số)."""
    n = 0
    for w in text.split():
        core = w.strip('.,;:?!"()')
        if re.fullmatch(r'\$?\d[\d,]*(\.\d+)?', core):
            s = core.lstrip('$').replace(',', '')
            if '.' in s:
                a, b = s.split('.')
                n += words_int(int(a)) + 1 + len(b)
            elif 1900 <= int(s) <= 2099:
                n += 2
            else:
                n += words_int(int(s))
            n += 1 if core.startswith('$') else 0
        elif core:
            n += 1
    return n


# ---------- parse script ----------
LINE = re.compile(r'^(S\d{2}\.\d+)\s+(?:\{(\w+)\}\s+)?((?:\[[a-z ]+\]\s+)?)(.*?)\s*<!--\s*claims:\s*(.*?)\s*-->\s*$')
rows, part, mid = [], None, []
PARTMAP = [('COLD OPEN', 'hook'), ('ACT 1', 'concept'), ('ACT 2', 'experiment'), ('ACT 3', 'buyers'), ('LIMITS', 'limits')]
events = []  # (kind, payload) in order
for ln in open(SCRIPT, encoding='utf-8'):
    ln = ln.rstrip('\n')
    if ln.startswith('==='):
        for key, p in PARTMAP:
            if key in ln:
                part = p
                events.append(('part', p))
        if 'IDENT' in ln:
            events.append(('ident', None))
    elif ln.startswith('>>> MID-ROLL'):
        events.append(('mid', ln))
    else:
        m = LINE.match(ln)
        if m:
            sid, role, emo, text, meta = m.groups()
            meta = re.sub(r';\s*label:.*$', '', meta)  # B+2: nhãn trên hình, không phải claim
            cl, hold = meta, 0.0
            hm = re.search(r';\s*hold:\s*([\d.]+)', meta)
            if hm:
                hold, cl = float(hm.group(1)), meta[:hm.start()]
            ids = [c.strip() for c in cl.split(',') if c.strip() not in ('', '—', '-')]
            r = dict(sid=sid, scene=sid.split('.')[0], role=role, emo=emo.strip(), text=text, ids=ids, hold=hold, part=part)
            rows.append(r)
            events.append(('line', r))
        elif re.match(r'^S\d{2}\.\d+', ln):
            print('dòng không đọc được:', ln[:80])

fail, warn = [], []
if not rows:
    sys.exit('không đọc được câu nào')

# timing
t = 0.0
for kind, p in events:
    if kind == 'ident':
        t += IDENT_S
    elif kind == 'mid':
        mid.append(t)
    elif kind == 'line':
        p['start'] = t
        p['end'] = t + spoken_words(p['text']) / WPS
        t = p['end'] + p['hold']
        p['next'] = t
TOTAL = t

# ---------- per-sentence rules ----------
seen, scene_new, newt = set(), {}, []
full_seen = set()
for r in rows:
    sp, ids, sid = r['text'], r['ids'], r['sid']
    for c in ids:
        if c not in CLAIM:
            fail.append(f'{sid}: claim không có trong numbers.md: {c}')
    low = sp.lower().replace('’', "'")
    for k, pats in S10.items():
        target = re.sub(r"(not|n't|never) a forecast", '', low) if k == 'FORECAST' else low
        for pat in pats:
            if re.search(pat, target, re.M):
                fail.append(f'{sid}: S10 {k} /{pat}/')
    if IMPERATIVE.search(sp) and not sp.rstrip().endswith('?'):
        fail.append(f'{sid}: mệnh lệnh với người xem: {sp[:60]}')
    if ADVICE_EXTRA.search(sp):
        fail.append(f'{sid}: cụm lời khuyên: {ADVICE_EXTRA.search(sp).group(0)}')
    if re.search(r'\bbuy now\b|\bor wait\b|\bwait(ing)? (for|until)\b|\bwaiting\b', low) and not (sp.rstrip().endswith('?') or re.search(r"won't (tell you|say) whether|doesn't weigh", low)):
        fail.append(f'{sid}: "buy now"/"wait" ngoài câu hỏi/câu đối trọng')
    # ASR
    if re.search(r'\b(1[89]|20)\d\ds?\s*[-–—]\s*((1[89]|20)?\d\ds?)\b', sp):
        fail.append(f'{sid}: ASR dải năm có gạch nối')
    if re.search(r'\bminus\b|(^|\s)[-−]\$?\d', sp, re.I):
        fail.append(f'{sid}: ASR minus/số âm')
    if re.search(r'[%±→×~≈<>/]', sp):
        fail.append(f'{sid}: ASR ký hiệu trong lời')
    if re.search(r'\b[A-Z]{1,3}-[A-Za-z0-9]', sp):
        fail.append(f'{sid}: ASR viết tắt có gạch nối')
    for ab, full in FULL_FORM.items():
        if re.search(r'\b' + ab + r'\b', sp) and ab not in full_seen:
            if full not in low:
                fail.append(f'{sid}: "{ab}" trước dạng đầy đủ')
            full_seen.add(ab)
    # numbers
    vals = allowed(ids)
    s2 = sp
    for ex in WORD_EXEMPT:
        s2 = re.sub(ex, '', s2, flags=re.I)
    toks = []
    for m in re.finditer(r'(\d+) in (\d+)|\$?\d[\d,]*(?:\.\d+)?', s2):
        if m.group(1):
            toks.append((m.group(0), [float(m.group(1)), float(m.group(2))]))
        else:
            toks.append((m.group(0).rstrip(',.'), [float(m.group(0).lstrip('$').rstrip(',.').replace(',', ''))]))
    for m in re.finditer(r'\b(' + '|'.join(WORDNUM) + r')\b', s2, re.I):
        toks.append((m.group(0).lower(), [float(WORDNUM[m.group(0).lower()])]))
    if toks and not ids:
        fail.append(f'{sid}: câu có số nhưng không claim: {[x for x, _ in toks]}')
    for tok, xs in toks:
        for x in xs:
            if round(x, 2) not in vals and round(x) not in vals:
                fail.append(f'{sid}: số "{tok}" không khớp claim gắn câu {ids}')
        if tok not in seen:
            seen.add(tok)
            scene_new[r['scene']] = scene_new.get(r['scene'], 0) + 1
            pos = s2.find(tok)
            newt.append((r['start'] + (spoken_words(s2[:pos]) if pos > 0 else 0) / WPS, tok))
for sc, n in scene_new.items():
    if n > 2:
        fail.append(f'{sc}: {n} số mới trong cảnh (story §3: ≤ 2)')
dense = [round(a) for i, (a, _) in enumerate(newt) if i + 2 < len(newt) and newt[i + 2][0] - a < 8]
if dense:
    warn.append(f'mật độ: ≥ 3 số mới trong 8 s tại ~{dense} s')

alltext = ' '.join(r['text'] for r in rows)
if not re.search(r'\bUS only\b', alltext):
    fail.append('thiếu "US only" trong lời')
if not re.search(r'history, not a forecast', alltext, re.I):
    fail.append('thiếu "history, not a forecast" trong lời')

# core number: said once in digits, recalled ≥ 3 times in words (claim on the line, no digits)
for cid, pat in CORE:
    said = [r['sid'] for r in rows if re.search(pat, r['text'])]
    first = next((i for i, r in enumerate(rows) if re.search(pat, r['text'])), len(rows))
    recall = [r['sid'] for r in rows[first + 1:] if cid in r['ids'] and not re.search(pat, r['text'])]
    if len(said) != 1:
        fail.append(f'số cốt lõi {pat}: đọc bằng số {len(said)} lần (cần 1): {said}')
    if len(recall) < 3:
        fail.append(f'số cốt lõi {cid}: nhắc lại bằng lời {len(recall)} lần (cần ≥ 3)')
    print(f'số cốt lõi {cid}: đọc {said}, nhắc bằng lời {recall}')

# emotion tags
emo = [(r['sid'], r['emo']) for r in rows if r['emo']]
if not 2 <= len(emo) <= 4:
    fail.append(f'thẻ cảm xúc {len(emo)} (cần 2–4)')

# names
for nm in BANNED_NAMES:
    if re.search(r'\b' + nm + r'\b', alltext):
        fail.append(f'tên đã dùng ở tập trước: {nm}')

# ---------- hook conditions M1–M5 ----------
early = [r for r in rows if r['start'] < 60]
for r in early:
    if r['role'] not in ROLES:
        fail.append(f'{r["sid"]}: câu trong 0:00–1:00 thiếu vai')


def mconds(rs, name):
    out = {}
    h = next((r for r in rs if r['role'] == 'hook'), None)
    p = next((r for r in rs if r['role'] == 'promise'), None)
    q = next((r for r in rs if r['role'] == 'question'), None)
    out['M1'] = h['end'] if h else None
    out['M2'] = p['end'] if p else None
    out['M3'] = q['end'] if q else None
    blk, best, bstart = None, 0.0, None
    for r in rs:
        if r['start'] >= 60:
            break
        if r['role'] in ('constraint', 'define'):
            bstart = r['start'] if bstart is None else bstart
            best = max(best, min(r['next'], 60) - bstart)
        else:
            bstart = None
    out['M4'] = best
    ret = next((r for r in rs if p and r['start'] >= p['end'] and (r['role'] == 'hook' or any(c in r['text'] for c in CAST + ['buyers']))), None)
    out['M5'] = ret['end'] if ret else None
    # M6: mỗi lời hứa về nhân vật được trả (tên trong CAST xuất hiện) ≤ 90 s sau câu hứa; không có lời hứa → 0
    m6 = 0.0
    if CAST == [] and any(r['role'] == 'promise_character' for r in rs):
        m6 = None   # không đo được: điền CAST (hoặc --cast)
    for i, r in enumerate(rs):
        if r['role'] != 'promise_character' or m6 is None:
            continue
        pay = next((x for x in rs[i + 1:] if any(re.search(r'\b' + c + r'\b', x['text']) for c in CAST)), None)
        m6 = max(m6, (pay['start'] - r['end']) if pay else float('inf'))
    out['M6'] = m6
    lim = {'M1': 5.0, 'M2': 30, 'M3': 30, 'M4': 10, 'M5': 45, 'M6': 90}
    res = []
    for k in ('M1', 'M2', 'M3', 'M4', 'M5', 'M6'):
        ok = out[k] is not None and out[k] <= lim[k]
        res.append(f'{k} {"–" if out[k] is None else f"{out[k]:.1f}"} s {"ĐẠT" if ok else "TRƯỢT"}')
        if not ok:
            fail.append(f'{name}: {k} = {out[k]} (ngưỡng {lim[k]})')
        elif out[k] and out[k] >= lim[k] * 0.95:
            warn.append(f'{name}: {k} = {out[k]:.1f} s trong ±5 % ngưỡng {lim[k]} (nêu tên, CHARTER §4)')
    return ' · '.join(res)


# M6: lời hứa về người phải mang vai promise_character, không thì M6 không bao giờ đo (REVIEWER 08/10: Tập 5 S03.4 {promise} "meet three illustrative buyers")
for r in rows:
    if r['role'] == 'promise' and PERSON_PROMISE.search(r['text']):
        fail.append(f'{r["sid"]}: lời hứa về người phải gắn vai promise_character (M6, story §2b.2)')
print('móc script:', mconds(rows, 'script'))

# ---------- duration, acts, mid-roll ----------
SPOKEN = sum(spoken_words(r['text']) for r in rows)
EST = SPOKEN / WPS_TOTAL   # độ dài cả tập (§3.1); TOTAL (lời ở WPS_SPEECH + hold + ident) chỉ dùng cho mốc giây
lo, hi = LEN_LIMITS.get(FORMAT, (0, 1e9))
if EST > hi:
    fail.append(f'độ dài ước {EST / 60:.2f} phút > {hi // 60}:{hi % 60:02d} (tối đa cứng, {FORMAT})')
elif EST < lo and not G1_SHORT:
    fail.append(f'độ dài ước {EST:.0f} s < đích {lo} s ({FORMAT}); thiếu ≈ {(lo - EST) * WPS_TOTAL:.0f} từ nói — thêm chất có nguồn, '
                f'không độn; vẫn thiếu → nêu ở G1, chạy lại với --g1-short khi chủ dự án duyệt')
elif EST < lo:
    warn.append(f'độ dài ước {EST:.0f} s < đích {lo} s — chủ dự án đã duyệt ở G1 (--g1-short)')
for r in rows:
    if r['role'] == 'peak' and len(r['text'].split()) > 15:
        warn.append(f'{r["sid"]}: câu đỉnh cảm xúc {len(r["text"].split())} từ > 15 (story §2b.4, REVIEWER soát)')
span = {}
for r in rows:
    a, b = span.get(r['part'], (r['start'], r['next']))
    span[r['part']] = (min(a, r['start']), max(b, r['next']))
order = [p for _, p in PARTMAP]
bounds = {}
for i, p in enumerate(order):
    s = 0.0 if i == 0 else bounds[order[i - 1]][1]
    e = span[order[i + 1]][0] if i + 1 < len(order) else TOTAL
    bounds[p] = (s, e)
fmt = lambda x: f'{int(x // 60)}:{int(x % 60):02d}'  # noqa: E731
print(f'\n{len(rows)} câu, {len(alltext.split())} từ viết ({SPOKEN} từ đọc), độ dài ước {fmt(EST)} ({SPOKEN} / {WPS_TOTAL} từ/s, {FORMAT}); '
      f'trục mốc giây {fmt(TOTAL)} ({WPS_SPEECH} từ/s + hold {sum(r["hold"] for r in rows):.1f} s + ident {IDENT_S:.0f} s)')
print('| Phần | Từ | Thời gian | Tỉ lệ | Khuôn 101 | Δ |')
for p in order:
    s, e = bounds[p]
    share = (e - s) / TOTAL * 100
    wc = sum(len(r['text'].split()) for r in rows if r['part'] == p)
    d = share - TEMPLATE[p]
    print(f'| {p} | {wc} | {fmt(s)}–{fmt(e)} | {share:.1f} % | {TEMPLATE[p]} % | {d:+.1f}{"  ← > ±5 (THAM KHẢO, nêu ở C2)" if abs(d) > 5 else ""} |')
    if abs(d) > 5:
        warn.append(f'khuôn tỉ lệ: {p} lệch {d:+.1f} điểm')
NMID = {'101': 1, 'lab': 2}.get(FORMAT, 1)
if len(mid) != NMID and not (G1_SHORT and not mid):
    fail.append(f'mid-roll: {len(mid)} điểm ({FORMAT} cần {NMID}; bỏ mid-roll chỉ khi G1 duyệt, --g1-short)')
for m in mid:
    prev = max((r for r in rows if r['next'] <= m + 1e-6), key=lambda r: r['next'])
    nxt_part = next((p for k, p in events[[e[1] is prev for e in events].index(True) + 1:] if k == 'part'), None)
    ok = m >= 120 and TOTAL - m >= 120 and prev['hold'] >= 1 and nxt_part is not None
    print(f'mid-roll ≈ {fmt(m)} sau {prev["sid"]} (hold {prev["hold"]} s), cách cuối {TOTAL - m:.0f} s: {"ĐẠT" if ok else "TRƯỢT"}')
    if not ok:
        fail.append('mid-roll sai vị trí (≥ 120 s từ đầu/cuối, hold ≥ 1 s, ranh giới hồi)')

# ---------- beats.md: on-screen numbers + ILLUSTRATIVE ----------
if os.path.exists(BEATS):
    nb = 0
    for ln in open(BEATS, encoding='utf-8'):
        if not re.match(r'^\| B\d', ln):
            continue
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        bid, screen, cl = cells[0], cells[-2], cells[-1]
        ids = [c.strip(' `') for c in cl.split(',') if c.strip(' `—-')]
        nb += 1
        for c in ids:
            if c not in CLAIM:
                fail.append(f'beats {bid}: claim không có: {c}')
        vals = allowed(ids)
        for q in re.findall(r'"([^"]+)"', screen):
            for tok in re.findall(r'\d[\d,]*(?:\.\d+)?', q):
                x = float(tok.replace(',', ''))
                if round(x, 2) not in vals and round(x) not in vals:
                    fail.append(f'beats {bid}: số trên hình "{tok}" ({q}) không khớp claim {ids}')
            for k, pats in S10.items():
                for pat in pats:
                    if re.search(pat, q.lower()):
                        fail.append(f'beats {bid}: S10 {k} trên hình: {q}')
        need = any(c.startswith('buyer_') for c in ids) or any(n in screen for n in CAST) or ('$' in screen and any(c.startswith('ex_') for c in ids))
        if need and 'ILLUSTRATIVE' not in screen:
            fail.append(f'beats {bid}: nhân vật/ví dụ $ thiếu ILLUSTRATIVE trên hình')
    print(f'beats.md: {nb} nhịp đã kiểm số trên hình')
else:
    fail.append('thiếu beats.md')

# ---------- hooks.md: 3 variants, M1–M5 each ----------
if os.path.exists(HOOKS):
    hv = {}
    for ln in open(HOOKS, encoding='utf-8'):
        m = re.match(r'^(H[ABC])\.(\d+)\s+\{(\w+)\}\s+((?:\[[a-z ]+\]\s+)?)(.*?)\s*<!--\s*claims:\s*(.*?)\s*-->\s*$', ln.rstrip('\n'))
        if m:
            hv.setdefault(m.group(1), []).append(dict(sid=f'{m.group(1)}.{m.group(2)}', role=m.group(3), text=m.group(5),
                                                      ids=[c.strip() for c in m.group(6).split(';')[0].split(',') if c.strip() not in ('', '—')]))
    if len(hv) != 3:
        warn.append(f'hooks.md có {len(hv)} phương án (cần 3)')
    cont = [dict(r) for r in rows if r['scene'] == 'S03']   # phần nối chung sau 30 s đầu (S03 của script.md)
    for h, rs in sorted(hv.items()):
        t = 0.0
        n_own = len(rs)
        rs = rs + [dict(r, sid=f'{h}+{r["sid"]}') for r in cont]
        for r in rs:
            r['start'] = t
            r['end'] = t + spoken_words(r['text']) / WPS
            t = r['next'] = r['end'] + r.get('hold', 0.0)
            for c in r['ids']:
                if c not in CLAIM:
                    fail.append(f'{r["sid"]}: claim không có: {c}')
            vals = allowed(r['ids'])
            for tok in re.findall(r'\d[\d,]*(?:\.\d+)?', r['text']):
                x = float(tok.replace(',', ''))
                if round(x, 2) not in vals and round(x) not in vals:
                    fail.append(f'{r["sid"]}: số "{tok}" không khớp claim {r["ids"]}')
            if IMPERATIVE.search(r['text']) and not r['text'].rstrip().endswith('?'):
                fail.append(f'{r["sid"]}: mệnh lệnh')
        print(f'hooks {h} ({n_own} câu riêng + S03 chung, phần riêng tới {rs[n_own - 1]["end"]:.1f} s):', mconds(rs, f'hooks {h}'))
else:
    warn.append('thiếu hooks.md')

print('\nĐẠT' if not fail else '\nTRƯỢT', *fail, sep='\n  ')
if warn:
    print('Cảnh báo (không chặn):', *warn, sep='\n  ')
sys.exit(1 if fail else 0)

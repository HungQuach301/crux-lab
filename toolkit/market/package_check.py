#!/usr/bin/env python3
"""Chốt kiểm gói ChatGPT ở P4 (Phiên Thị trường bước 7). Chủ dự án làm tiêu đề, mô tả, thumbnail trên ChatGPT từ
out/package/PACKAGING-BRIEF.md, rồi dán vào prompt phiên P4 cùng câu trả lời G2 (không thêm lượt chạm). P4 chạy:

  python3 toolkit/market/package_check.py episodes/epNNN --title "…" --description <tệp.md> --thumb <ảnh.png> [--thumb …]

Kiểm (dùng lại luật khoá của checks/ — chỉ import, không sửa):
  1. S21 trên mô tả: chép mô tả vào out/package/description.md (bản máy cũ → description.machine.md), chạy checks/py/run.py --only S21.
  2. Claim-risk trên tiêu đề, mô tả, chữ trên ảnh: regex ADVICE / FORECAST / FOUR / WE_BAD (S10); mọi số có claim (claim_number_set);
     cụm bắt buộc "history, not a forecast" và "US only" trong mô tả; "ILLUSTRATIVE" khi có nhân vật/số minh hoạ.
  3. Chương khớp timeline: mốc 0:00 đầu, mỗi mốc khác trùng đầu một hồi trong out/timeline.json (±2 s), tăng dần, mỗi chương ≥ 10 s.
  4. Chữ trên ảnh: Sonnet đọc ảnh (tệp của chủ dự án, không lưu đi đâu) → ≤ 4 từ lớn, số có claim, (D-015: không cần nhãn ILLUSTRATIVE trên ảnh bìa).
Mỗi lỗi kèm **câu sửa sẵn** (tiếng Anh) để chủ dự án dán lại vào ChatGPT. Ghi out/package/package-check.md + .json; thoát 1 nếu có lỗi.
"""
import base64, json, os, pathlib, re, subprocess, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'checks' / 'py'))
from r_content import ADVICE, FORECAST, FOUR, WE_BAD          # noqa: E402  (luật khoá S10, chỉ đọc)
from r_k40 import claim_number_set, _plain_nums               # noqa: E402  (luật khoá S21, chỉ đọc)

MAX_TITLE, MAX_THUMB_WORDS = 60, 4


def scan(text):
    low = text.lower()
    hits = []
    for name, pats in (('ADVICE', ADVICE), ('FORECAST', FORECAST), ('FOUR', FOUR), ('WE_BAD', WE_BAD)):
        for p in pats:
            for ln in low.splitlines():
                m = re.search(p, ln.strip())
                if m:
                    hits.append((name, m.group(0)))
    return hits


def bad_numbers(text, ok):
    s = re.sub(r'(?m)^\s*\d+:\d\d(:\d\d)?\s*', '', text)
    s = re.sub(r'https?://\S+', ' ', s)
    s = re.sub(r'\b[A-Z][A-Z0-9]*\d[A-Z0-9]*\b', ' ', s)
    return [tok for tok, x in _plain_nums(s) if round(x, 2) not in ok]


def chapters(desc):
    out = []
    for ln in desc.splitlines():
        m = re.match(r'^\s*(?:(\d+):)?(\d{1,2}):(\d\d)\s+(.+)', ln)
        if m:
            h, mi, se = int(m.group(1) or 0), int(m.group(2)), int(m.group(3))
            out.append((h * 3600 + mi * 60 + se, m.group(4).strip()))
    return out


def read_thumb(path):
    """Sonnet đọc chữ trên ảnh (Messages API, ảnh base64 của chủ dự án)."""
    data = base64.b64encode(pathlib.Path(path).read_bytes()).decode()
    mt = 'image/png' if str(path).lower().endswith('.png') else 'image/jpeg'
    prompt = ('Transcribe every piece of overlaid text on this YouTube thumbnail exactly, as a JSON object: '
              '{"texts": ["..."], "large_words": <number of words in the big headline text>, "has_face": true/false}. JSON only.')
    body = json.dumps({'model': 'claude-sonnet-4-5', 'max_tokens': 600, 'messages': [{'role': 'user', 'content': [
        {'type': 'image', 'source': {'type': 'base64', 'media_type': mt, 'data': data}}, {'type': 'text', 'text': prompt}]}]}).encode()
    req = urllib.request.Request('https://api.anthropic.com/v1/messages', body, {
        'x-api-key': os.environ['CONSOLE_API_KEY'], 'anthropic-version': '2023-06-01', 'content-type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    t = ''.join(c.get('text', '') for c in d['content'])
    t = t[t.find('{'): t.rfind('}') + 1]
    return json.loads(t), d['usage']


def main(a):
    ep = pathlib.Path(a[0])
    title = a[a.index('--title') + 1] if '--title' in a else ''
    desc_f = a[a.index('--description') + 1] if '--description' in a else None
    thumbs = [a[i + 1] for i, x in enumerate(a) if x == '--thumb']
    claims = json.loads((ep / 'out' / 'claims.json').read_text())
    cl = claims['claims'] if isinstance(claims, dict) else claims
    ok = claim_number_set(cl)
    illustrative = any(c.get('illustrative') for c in cl)
    fails, notes = [], []

    def fail(where, what, fix):
        fails.append({'where': where, 'what': what, 'fix': fix})

    # 1–2. tiêu đề
    if title:
        if len(title) > MAX_TITLE:
            fail('title', f'{len(title)} ký tự > {MAX_TITLE}', f'Shorten the title to {MAX_TITLE} characters or fewer; keep the viewer question and drop filler words.')
        for k, m in scan(title):
            fail('title', f'{k}: "{m}"', 'Rewrite the title as a question or a comparison; no advice ("you should…"), no prediction ("will…").')
        for n in bad_numbers(title, ok):
            fail('title', f'số "{n}" không có claim', f'Remove "{n}" from the title or replace it with one of these exact figures: '
                 + ', '.join(sorted({str(c.get("display")) for c in cl if c.get("display") and re.search(r"\d", str(c.get("display")))})[:8]) + '.')
    # mô tả
    if desc_f:
        desc = pathlib.Path(desc_f).read_text()
        pk = ep / 'out' / 'package'
        if (pk / 'description.md').exists() and not (pk / 'description.machine.md').exists():
            (pk / 'description.md').rename(pk / 'description.machine.md')
        machine = pk / 'description.machine.md'
        if '[METHOD AND SOURCES]' in desc and machine.exists():   # khối phương pháp + nguồn của máy thay chỗ giữ chỗ trong brief
            txt = machine.read_text()
            block = txt[txt.find('Method and sources'):].split('\n\n', 1)[0] if 'Method and sources' in txt else ''
            desc = desc.replace('[METHOD AND SOURCES]', block)
        (pk / 'description.md').write_text(desc)
        r = subprocess.run([sys.executable, str(ROOT / 'checks' / 'py' / 'run.py'), str(ep), '--only', 'S21'], capture_output=True, text=True)
        rep = ep / 'out' / 'checks' / 'report-partial.json'   # run.py --only ghi report-partial.json
        s21 = None
        if rep.exists():
            for x in json.loads(rep.read_text()).get('results', []):
                if x.get('id') == 'S21':
                    s21 = x
        if s21 and s21.get('status') != 'PASS':
            for d in (s21.get('details') or [])[:10]:
                fail('description', f"S21 dòng {d.get('line')}: số \"{d.get('number')}\" không có claim",
                     f"In the description, remove \"{d.get('number')}\" or replace it with an exact figure from the episode (see the allowed-claims list in the brief).")
        elif not s21:
            notes.append('S21: không đọc được report.json — chạy tay `python3 checks/py/run.py ' + str(ep) + ' --only S21`. ' + r.stdout[-200:])
        for k, m in scan(desc):
            fail('description', f'{k}: "{m}"', 'Rewrite that sentence as a description of what the video shows; no advice, no prediction.')
        low = desc.lower()
        for must in ('history, not a forecast', 'us only'):
            if must not in low:
                fail('description', f'thiếu "{must}"', f'Add the exact phrase "{must if must != "us only" else "US only"}" to the first paragraph of the description.')
        if illustrative and 'illustrative' not in low:
            fail('description', 'thiếu "ILLUSTRATIVE"', 'Add one line: "<names> are ILLUSTRATIVE <people> built on real US data."')
        # 3. chương
        ch = chapters(desc)
        tl = json.loads((ep / 'out' / 'timeline.json').read_text())
        starts = [a_['start'] for a_ in tl.get('acts', []) if a_['id'] != 'ident']
        if ch:
            if ch[0][0] != 0:
                fail('chapters', 'chương đầu không ở 0:00', 'Make the first chapter line start with 0:00.')
            for (t, name), nxt in zip(ch, ch[1:] + [(tl['total'], '')]):
                if t and not any(abs(t - s) <= 2 for s in starts):
                    near = min(starts, key=lambda s: abs(s - t))
                    fail('chapters', f'mốc {t // 60}:{t % 60:02d} "{name}" không khớp đầu hồi nào',
                         f'Change that chapter time to {int(near) // 60}:{int(near) % 60:02d} (the act boundary in the final cut).')
                if nxt[0] - t < 10:
                    fail('chapters', f'chương "{name}" < 10 s', 'Merge that chapter into the next one (YouTube needs chapters of 10 seconds or more).')
            if len(ch) < 3:
                fail('chapters', f'{len(ch)} chương < 3', 'Use the chapter list from the brief exactly (YouTube needs at least 3 chapters).')
        else:
            notes.append('mô tả không có chương — YouTube tự tạo hoặc không hiện chương; khuyến nghị dán danh sách chương trong brief.')
    # 4. thumbnail
    for t in thumbs:
        try:
            r, usage = read_thumb(t)
        except Exception as e:  # noqa: BLE001
            notes.append(f'{t}: không đọc được ảnh ({str(e)[:80]}) — kiểm bằng mắt.')
            continue
        text = ' '.join(r.get('texts', []))
        if r.get('large_words', 0) > MAX_THUMB_WORDS:
            fail(f'thumb {pathlib.Path(t).name}', f"{r['large_words']} từ lớn > {MAX_THUMB_WORDS}", f'Cut the thumbnail headline to {MAX_THUMB_WORDS} words or fewer.')
        for k, m in scan(text):
            fail(f'thumb {pathlib.Path(t).name}', f'{k}: "{m}"', 'Replace the thumbnail text with a neutral question or comparison (no advice, no prediction).')
        for n in bad_numbers(text, ok):
            fail(f'thumb {pathlib.Path(t).name}', f'số "{n}" không có claim', f'Remove "{n}" from the thumbnail or use an exact figure from the brief.')
        # D-015 (chủ dự án 17/10): ảnh bìa không mang nhãn ILLUSTRATIVE (giữ trong video và mô tả) — không nhắc nữa.
    res = {'pass': not fails, 'fails': fails, 'notes': notes}
    out = ep / 'out' / 'package'
    (out / 'package-check.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    L = ['# Kiểm gói ChatGPT (P4)', '', f"**{'ĐẠT' if not fails else 'TRƯỢT — ' + str(len(fails)) + ' lỗi'}**", '']
    if fails:
        L += ['| Ở đâu | Lỗi | Câu sửa sẵn (dán vào ChatGPT) |', '|---|---|---|'] + [f"| {f['where']} | {f['what']} | {f['fix']} |" for f in fails]
    L += [''] + [f'- {n}' for n in notes]
    (out / 'package-check.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

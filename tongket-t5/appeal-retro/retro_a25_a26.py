"""Chạy thử HỒI TỐ A25, A26 (checks-appeal, đề xuất từ cine-lab BAI-HOC-LL #53, #62) trên Tập 3–5 — CHỈ BÁO, không sửa tập đã phát hành,
không phải luật (`checks/` không đổi; phiên K mới quyết). Tái lập: python3 tongket-t5/appeal-retro/retro_a25_a26.py > tongket-t5/appeal-retro/RESULT.md

A25 — mọi số trong `out/package/description.md` phải có trong `out/claims.json` (value, display, dataYears; cho phép ×100, ÷100, ×12, ÷12,
      làm tròn 0–2 chữ số). Bỏ: dòng mốc chương (`m:ss …` đầu dòng), URL, mã chuỗi (chữ hoa + số, vd MORTGAGE30US), số thứ tự danh sách,
      trích dẫn luật (`26 U.S.C. 121`, `31 CFR 351.34(a)`, `70 FR 17288`).
A26 — một câu (lời: `out/script.json` + `claims[].spoken`) hoặc một khung (chữ trên hình: `claims[].shownIn`, theo cảnh) không ghép hai số
      khác NGUỒN (`source.id`) hoặc khác KỲ (`dataYears`, hoặc một số lịch sử `historical` với một số hiện tại). Chỉ xét cặp claim có giá
      trị số và là DỮ LIỆU: tham số/hằng/luật (nguồn `contract.json`, `numbers.md`, `law`, `axis`, mã luật/trang luật) là định nghĩa,
      không phải số đo → bỏ qua (lượt chạy đầu tính cả chúng: Tập 5 22 đơn vị, gần hết là "80 % của luật" + số mô hình — nhiễu). Báo thêm tập con "có từ so sánh" (than, vs, compared, while, but, from … to) — kiểu lỗi #62.
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PARAM = re.compile(r'^(axis|contract\.json|numbers\.md|law|rule)$|CFR|U\.S\.C|FR \d|^`?model\.json`? `?params', re.I)
CMP = re.compile(r'\b(than|vs\.?|versus|compared|while|whereas|but|from\b.*\bto)\b', re.I)


def nums(text):
    out = []
    for m in re.finditer(r'(?<![\w.])\$?\d[\d,]*(?:\.\d+)?', text):
        tok = m.group(0)
        out.append((tok, float(tok.lstrip('$').replace(',', ''))))
    return out


def allowed(claims):
    vals, strs = set(), []
    for c in claims:
        v = c.get('value')
        xs = [v] if isinstance(v, (int, float)) and not isinstance(v, bool) else []
        if isinstance(v, str):
            xs += [x for _, x in nums(v)]
        xs += [x for _, x in nums(str(c.get('display', '')))]
        xs += [float(y) for y in c.get('dataYears') or [] if isinstance(y, (int, float))]
        for x in xs:
            for y in (x, x * 100, x / 100, x / 12, x * 12):
                vals |= {round(y, 2), round(y, 1), round(y), float(int(y))}
        strs.append(str(c.get('display', '')))
    return vals


def a25(ep):
    p = os.path.join(ROOT, 'episodes', ep, 'out', 'package', 'description.md')
    C = json.load(open(os.path.join(ROOT, 'episodes', ep, 'out', 'claims.json')))['claims']
    ok = allowed(C)
    bad = []
    for n, ln in enumerate(open(p, encoding='utf-8'), 1):
        if re.match(r'^\s*\d+:\d\d\b', ln):
            ln = re.sub(r'^\s*\d+:\d\d\s*', '', ln)
        s = re.sub(r'https?://\S+', ' ', ln)
        s = re.sub(r'\b\d+\s+(U\.S\.C\.|CFR|FR)\s+[\d.]+(\([\w]+\))*(\s+and\s+[\d.]+(\([\w]+\))*)?', ' ', s)   # trích dẫn luật
        s = re.sub(r'\b[A-Z][A-Z0-9]*\d[A-Z0-9]*\b', ' ', s)     # mã chuỗi FRED, mã luật
        s = re.sub(r'^\s*\d+[.)]\s', ' ', s)
        for tok, x in nums(s):
            if round(x, 2) not in ok and round(x) not in ok:
                bad.append({'line': n, 'num': tok, 'text': ln.strip()[:110]})
    return bad


def a26(ep):
    C = json.load(open(os.path.join(ROOT, 'episodes', ep, 'out', 'claims.json')))['claims']
    S = {s['id']: s for s in json.load(open(os.path.join(ROOT, 'episodes', ep, 'out', 'script.json')))['sentences']}
    num = [c for c in C if (isinstance(c.get('value'), (int, float)) and not isinstance(c.get('value'), bool))
           and not PARAM.search(str((c.get('source') or {}).get('id') or ''))]
    def key(c):
        src = (c.get('source') or {}).get('id') or '?'
        per = tuple(c.get('dataYears') or ()) or ('hist' if c.get('historical') else 'now')
        return src, per
    units = {}
    for c in num:
        for sp in c.get('spoken') or []:
            units.setdefault(('câu', sp['sentence']), []).append(c)
        for sc in c.get('shownIn') or []:
            units.setdefault(('khung', sc if isinstance(sc, str) else json.dumps(sc)), []).append(c)
    res = []
    for (kind, uid), cs in sorted(units.items()):
        ks = {key(c) for c in cs}
        srcs, pers = {k[0] for k in ks}, {k[1] for k in ks}
        if len(cs) >= 2 and (len(srcs) > 1 or len(pers) > 1):
            text = S.get(uid, {}).get('text', '') if kind == 'câu' else ''
            res.append({'unit': f'{kind} {uid}', 'claims': [c['claimId'] for c in cs], 'sources': sorted(srcs),
                        'periods': sorted(map(str, pers)), 'compare': bool(CMP.search(text)), 'text': text[:120]})
    return res


if __name__ == '__main__':
    eps = sys.argv[1:] or ['ep003', 'ep004', 'ep005']
    print('# Chạy thử hồi tố A25, A26 trên Tập 3–5 (08/10/2026) — CHỈ BÁO\n')
    print('Không sửa tập đã phát hành (cine-lab #57, Q-L23b: không sửa video đã đăng). Mã: `retro_a25_a26.py` (định nghĩa ở đầu tệp).\n')
    print('| Tập | A25: số trong mô tả không có claim | A26: đơn vị ghép khác nguồn/kỳ (câu · khung) | A26 có từ so sánh |')
    print('|---|---|---|---|')
    R = {}
    for ep in eps:
        b, c = a25(ep), a26(ep)
        R[ep] = (b, c)
        nc = sum(1 for x in c if x['unit'].startswith('câu')); nk = len(c) - nc
        print(f"| {ep} | {len(b)} | {len(c)} ({nc} · {nk}) | {sum(x['compare'] for x in c)} |")
    for ep, (b, c) in R.items():
        print(f'\n## {ep}\n\n**A25** ({len(b)}):')
        for x in b:
            print(f"- dòng {x['line']}: `{x['num']}` — {x['text']}")
        print(f'\n**A26** ({len(c)}; ★ = có từ so sánh):')
        for x in c:
            print(f"- {'★ ' if x['compare'] else ''}{x['unit']}: {', '.join(x['claims'])} · nguồn {x['sources']} · kỳ {x['periods']}"
                  + (f" — \"{x['text']}\"" if x['text'] else ''))

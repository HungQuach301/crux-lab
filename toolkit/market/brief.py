#!/usr/bin/env python3
"""Sinh out/package/PACKAGING-BRIEF.md điền sẵn cho một tập (Phiên Thị trường bước 7; chạy ở P3 trước G2, gửi kèm gói G2).

  python3 toolkit/market/brief.py episodes/epNNN --topic <id hồ sơ cầu, vd q12-annuity-raise> [--answered 1,3,4] [--bg out/package/bg-1.png …]
  --answered: số thứ tự câu hỏi khán giả mà kịch bản trả lời (bảng nhịp C2, ≥ 3/5); mặc định 1,2,3.

Nguồn: out/claims.json (số được phép = `display`), out/timeline.json (chương = đầu hồi, bỏ ident), out/package/description.md của máy
(đoạn tóm tắt + tên chương nếu có), market/topics/<id>.md (câu hỏi khán giả, từ khoá), market/REPORT.md (khuôn tiêu đề + kiểu thumbnail thắng).
Ảnh nền: 2–3 khung thế giới 3D 1280×720 KHÔNG chữ (build_seg.py từ cảnh đã duyệt, như `playbook/episode.md` §5) — P3 render, brief chỉ liệt kê.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / 'playbook' / 'templates' / 'PACKAGING-BRIEF.md'


def section(md, head):
    m = re.search(rf'(?ms)^##+ [^\n]*{re.escape(head)}[^\n]*\n(.*?)(?=^## |\Z)', md)
    return m.group(1).strip() if m else ''


def main(a):
    ep = pathlib.Path(a[0])
    topic = a[a.index('--topic') + 1] if '--topic' in a else None
    bgs = [a[i + 1] for i, x in enumerate(a) if x == '--bg']
    n = re.sub(r'\D', '', ep.name).lstrip('0') or '?'
    claims = json.loads((ep / 'out' / 'claims.json').read_text())
    cl = claims['claims'] if isinstance(claims, dict) else claims
    # số được phép = claim có số mà phim nói ra hoặc hiện trên hình (đủ ngắn để brief ≤ 1 trang); số khác trong claims.json vẫn qua S21
    said = [c for c in cl if (c.get('spoken') or c.get('shownIn')) and not re.fullmatch(r'(age|year) \d+|all \d+', str(c.get('display', '')))]
    said.sort(key=lambda c: -(len(c.get('spoken') or []) + len(c.get('shownIn') or [])))
    displays = list(dict.fromkeys(str(c['display']) for c in said if c.get('display') and re.search(r'\d', str(c['display']))))[:20]
    tl = json.loads((ep / 'out' / 'timeline.json').read_text())
    desc_p = ep / 'out' / 'package' / 'description.md'
    desc = desc_p.read_text() if desc_p.exists() else ''
    named = {}
    for ln in desc.splitlines():
        m = re.match(r'^\s*(\d+):(\d\d)\s+(.+)', ln)
        if m:
            named[int(m.group(1)) * 60 + int(m.group(2))] = m.group(3).strip()
    chap = []
    for act in tl.get('acts', []):
        if act['id'] == 'ident':
            continue
        t = 0 if act['id'] == 'cold-open' else int(act['start'])
        name = next((v for k, v in named.items() if abs(k - t) <= 2), act['id'])
        chap.append(f'{t // 60}:{t % 60:02d} {name}')
    summary = desc.split('\n\n')[0].strip() if desc else '{2–3 sentences}'
    pkg = ep / 'out' / 'package' / 'package.json'
    title = json.loads(pkg.read_text()).get('title', '') if pkg.exists() else ''
    qs, kw = '{X, Y, Z}', '{keywords}'
    if topic and (ROOT / 'market' / 'topics' / f'{topic}.md').exists():
        tm = (ROOT / 'market' / 'topics' / f'{topic}.md').read_text()
        allq = [re.sub(r'^\d+\.\s*', '', l).split(' — ')[0].strip() for l in section(tm, 'Câu hỏi khán giả').splitlines() if re.match(r'^\d+\.', l)]
        pick = [int(x) for x in a[a.index('--answered') + 1].split(',')] if '--answered' in a else [1, 2, 3]   # câu kịch bản đã trả lời (bảng nhịp)
        qs = '; '.join(allq[i - 1] for i in pick if 0 < i <= len(allq)) or qs
        kw = section(tm, 'Từ khoá mô tả').replace('\n', ' ') or kw
    rep = (ROOT / 'market' / 'REPORT.md').read_text() if (ROOT / 'market' / 'REPORT.md').exists() else ''
    en = section(rep, 'Cho brief')
    frames = [l.split(':', 1)[1].strip() for l in en.splitlines() if l.startswith('- title:')][:3]
    thumb = next((l.split(':', 1)[1].strip() for l in en.splitlines() if l.startswith('- thumbnail:')), '{winning style}')
    body = TEMPLATE.read_text().split('---', 1)[1]
    body = (body.replace('{2–3 sentences: the viewer question, what was replayed (series, years), the answer in plain words, the guide character.}', summary)
            .replace('{display list from out/claims.json}', ', '.join(displays))
            .replace('{0:00 … from out/timeline.json acts}', '\n'.join(chap))
            .replace('{winning style from market/REPORT.md §3}', thumb)
            .replace('{3–4}', '4').replace('{keywords}', kw).replace('{X, Y, Z}', qs))
    for i, f in enumerate(frames[:3], 1):
        body = body.replace(f'{{frame {i}}}', f)
    head = f'# Packaging brief — Episode {n}: {title or "{working title}"}\n'
    head += f'<!-- Sinh bằng toolkit/market/brief.py. Ảnh nền đính kèm: {", ".join(bgs) or "out/package/bg-1.png, bg-2.png (P3 render)"}. Dán nguyên phần dưới vạch vào ChatGPT. -->\n---'
    out = ep / 'out' / 'package' / 'PACKAGING-BRIEF.md'
    out.write_text(head + body)
    words = len(re.findall(r'\S+', body))
    print(out, f'{words} từ', '(≤ 1 trang ≈ 600 từ)' if words <= 600 else '— DÀI HƠN 1 TRANG, rút gọn số được phép')


if __name__ == '__main__':
    main(sys.argv[1:])

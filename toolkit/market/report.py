#!/usr/bin/env python3
"""Ghi phần sinh máy của market/ từ ~/market-cache/<ngày>/ — CHỈ nhãn và định tính, không số liệu thô.

  python3 toolkit/market/report.py channels   # → market/CHANNELS.md
  python3 toolkit/market/report.py topics     # → market/topics/<đề tài>.md (hồ sơ cầu) + market/topics/labels.json
  python3 toolkit/market/report.py queue      # cột Cầu / Khoảng trống trong topics/queue.md

Định danh kênh/video (channelId, videoId) được giữ (YouTube cho phép lưu định danh); tiêu đề video của người khác chỉ ghi
dạng diễn giải ngắn hoặc khuôn trừu tượng, không chép nguyên; không ghi lượt xem, người đăng ký, like.
"""
import datetime as dt, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import analyze as A
from common import jload

ROOT = pathlib.Path(__file__).resolve().parents[2]
NOW = dt.datetime.now(dt.timezone.utc)
CIRCLE = {'direct': 'trực tiếp', 'adjacent': 'lân cận', 'form': 'hình thức'}
EXCL = {'sells_course_or_stock_picks': 'bán khoá học / chọn cổ phiếu', 'news': 'tin tức', 'product_sales': 'bán sản phẩm',
        'not_english_or_not_us_audience': 'không phải khán giả Mỹ / tiếng Anh', 'off_topic': 'ngoài đề tài', 'unclassified': 'chưa phân loại được'}


def size(s):
    return 'lớn' if s >= 100_000 else 'vừa' if s >= 10_000 else 'nhỏ'


def channel_rows():
    d = A.day()
    keep = A.kept_channels()
    out = jload(d / 'analysis' / 'outliers.json')
    cl = jload(d / 'discover' / 'classified.json')
    why = jload(d / 'discover' / 'candidates.json')['why']
    rows = []
    for c, x in cl.items():
        p = jload(d / 'pull' / f'{c}.json')['channel']
        age = (NOW - dt.datetime.fromisoformat(p['publishedAt'].replace('Z', '+00:00'))).days
        n5 = sum(1 for r in out.values() if r['channelId'] == c and r['flag5'])
        rows.append({'id': c, 'title': p['title'].strip(), 'keep': c in keep, 'circle': x.get('circle'), 'exclude': x.get('exclude', []),
                     'young': age < 730, 'size': size(p['subs']), 'boom': n5, 'style': x.get('style', ''), 'presenter': x.get('presenter'),
                     'why': why.get(c, []), 'ld90': x.get('long_videos_last_90d', 0), 'seed': c in A.SEEDS})
    return rows


def link(r):
    return f"[{r['title'].replace('|', '·')}](https://www.youtube.com/channel/{r['id']})"


def why_txt(r):
    return '; '.join(w.replace('lượt xem/ngày thuộc 10 % cao nhất', 'lượt xem/ngày cao') for w in r['why'])


def cmd_channels():
    rows = channel_rows()
    seed = [r for r in rows if r['seed']]
    kept = [r for r in rows if r['keep'] and not r['seed']]
    # mới nổi: kênh < 2 năm → thử việc 90 ngày; đã có ≥ 2 video nổ (≥ 5×, tự tính) → lên danh sách chính ngay
    main = {k: [r for r in kept if r['circle'] == k and (not r['young'] or r['boom'] >= 2)] for k in CIRCLE}
    trial = [r for r in kept if r['young'] and r['boom'] < 2]
    gone = [r for r in rows if not r['keep']]
    L = [f"# Danh sách kênh cùng chủ đề — Phiên Thị trường (`market-r1`, {A.day().name})", '',
         'Sinh bằng `python3 toolkit/market/report.py channels` từ `~/market-cache/<ngày>/` (ngoài git). **Không có số liệu thô** '
         '(lượt xem, người đăng ký, like): chỉ định danh kênh, vòng tròn, nhãn và lý do. "Video nổ" = video có hệ số vượt trội ≥ 5× '
         '(lượt xem / trung vị kênh ±90 ngày, ≥ 10.000 lượt; **tự tính, không phải chỉ số YouTube**). Cỡ kênh: lớn ≥ 100 nghìn, vừa ≥ 10 nghìn, nhỏ dưới — nhãn, không phải số.', '',
         '**Cách chọn** (`toolkit/market/discover.py`): tìm theo VIDEO trước — 21 đề tài (19 dòng hàng đợi + 2 "từ hạt giống") × 3 lượt search '
         '(30 ngày theo lượt xem, 90 ngày theo lượt xem, top 20 theo độ liên quan; regionCode US, tiếng Anh, 4–20 phút) + 3 search vòng "hình thức". '
         'Ứng viên = kênh có video dài xuất hiện ở **≥ 3 đề tài**, + kênh nổi bật (channelSections) của chúng, + kênh **mới nổi** '
         '(kênh < 2 năm có video ≥ 3× số người đăng ký hoặc lượt xem/ngày thuộc 10 % cao nhất), + hạt giống chủ dự án. '
         'Phân loại vòng tròn và lý do loại: Haiku headless trên tên + mô tả + 15 tiêu đề gần nhất (máy đoán, có thể sai — sửa ở đây).', '',
         '**Không dừng hỏi duyệt.** Chủ dự án phản đối được ở **G1 Tập 7** (một dòng: "bỏ kênh X / thêm kênh Y"). Hiệu chỉnh hằng tháng theo nguồn '
         '"video đề xuất" khi có Analytics kênh mình (`playbook/episode.md` §10).', '']
    L += ['## Từ chủ dự án (bỏ thử việc)', '', '| Kênh | Vòng | Kiểu | Video nổ | Ghi chú |', '|---|---|---|---|---|']
    for r in seed:
        L.append(f"| {link(r)} | trực tiếp (hạt giống) | {r['style']} | {r['boom']} | mổ xẻ: `market/teardowns/` |")
    for k, name in CIRCLE.items():
        note = {'direct': 'giải thích / dữ liệu tài chính cá nhân Mỹ, video dài',
                'adjacent': 'giáo dục tài chính có mặt người (nói trước máy, cố vấn, podcast)',
                'form': 'giải thích bằng dữ liệu ngoài tài chính — **chỉ học đóng gói**'}[k]
        L += ['', f'## Vòng {name} — {note}', '', '| Kênh | Cỡ | Kiểu (máy tả) | Video nổ | Vì sao vào |', '|---|---|---|---|---|']
        for r in sorted(main[k], key=lambda r: -r['boom']):
            L.append(f"| {link(r)} | {r['size']} | {r['style']} | {r['boom']} | {why_txt(r)}{' · kênh < 2 năm, ≥ 2 video nổ → lên thẳng' if r['young'] else ''} |")
        if not main[k]:
            L.append('| — | | | | |')
    L += ['', '## Mới nổi — thử việc 90 ngày (đến ' + (A.day() and (dt.date.fromisoformat(A.day().name) + dt.timedelta(days=90)).isoformat()) + ')', '',
          'Kênh < 2 năm. **≥ 2 video nổ trong 90 ngày → lên vòng tương ứng**; không thì bỏ ở lần làm mới sau hạn. Phần lớn là kênh không mặt người, mới mở — '
          'cùng khuôn với Crux nên là đối thủ trực tiếp nếu sống sót.', '',
          '| Kênh | Vòng (máy đoán) | Kiểu | Video nổ | Vì sao vào |', '|---|---|---|---|---|']
    for r in sorted(trial, key=lambda r: (r['circle'], -r['boom'])):
        L.append(f"| {link(r)} | {CIRCLE.get(r['circle'], r['circle'])} | {r['style']} | {r['boom']} | {why_txt(r)} |")
    L += ['', '## Đã loại', '', 'Luật loại: bán khoá học/chọn cổ phiếu, tin tức, không phải tiếng Anh/khán giả Mỹ, không có video dài trong 90 ngày (và ngoài đề tài, bán sản phẩm).', '',
          '| Kênh | Lý do |', '|---|---|']
    for r in sorted(gone, key=lambda r: r['title'].lower()):
        rs = [EXCL.get(e, e) for e in r['exclude']] + (['không có video dài trong 90 ngày'] if not r['ld90'] else [])
        if r['circle'] == 'none' and not rs:
            rs = ['ngoài ba vòng tròn']
        L.append(f"| {link(r)} | {', '.join(rs)} |")
    (ROOT / 'market' / 'CHANNELS.md').write_text('\n'.join(L) + '\n')
    print('market/CHANNELS.md:', len(seed), 'hạt giống,', {k: len(v) for k, v in main.items()}, len(trial), 'thử việc,', len(gone), 'loại')


METHOD = {'real_history': 'dữ liệu lịch sử thật', 'fixed_assumption': 'giả định cố định', 'opinion': 'ý kiến, không tính', 'news': 'tin tức'}
WEIGHT = {'high': 'cao', 'medium': 'vừa', 'low': 'thấp'}


def mmss(m):
    return f"{int(m)}:{int(round((m - int(m)) * 60)):02d}"


def cmd_topics():
    d = A.day()
    prof = jload(d / 'analysis' / 'profile.json')['profiles']
    gap = jload(d / 'analysis' / 'gap.json') if (d / 'analysis' / 'gap.json').exists() else {}
    row_of = {t['id']: t.get('row') for t in A.TOPICS}
    od = ROOT / 'market' / 'topics'
    od.mkdir(parents=True, exist_ok=True)
    labels = {}
    for tid, p in prof.items():
        q = p['questions'] if isinstance(p['questions'], dict) else {}
        qs = q.get('questions', [])[:5]
        gm = {x['id']: x for x in gap.get(tid, [])}
        dr = p.get('dur_range_min')
        L = [f"# Hồ sơ cầu — {p['title']}", '',
             f"Đề tài: {'dòng #' + str(row_of[tid]) if row_of.get(tid) else 'từ hạt giống'} trong `topics/queue.md` · id `{tid}` · **Làm mới: {d.name}** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).",
             'Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. '
             'Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.', '',
             '| Mục | Nhãn | Cách tính (tự tính) |', '|---|---|---|',
             f"| Mức cầu (trừ thời sự) | **{p['demand']}** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |",
             f"| Khoảng trống | **{p['gap']}** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |",
             f"| Số video gắn đề tài | {p['n_tagged_label']} | embeddings, chỉ cặp khớp cao (cosine ≥ {A.SIM_MIN}, biên ≥ {A.SIM_MARGIN}) |",
             f"| Dải thời lượng | {mmss(dr[0]) + '–' + mmss(dr[1]) if dr else 'chưa có'} | tứ phân vị 25–75 % của video {p.get('dur_src', '')} cùng đề tài |", '',
             '## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)']
        L += [f"{i}. {x['q']} — trọng số {WEIGHT.get(x.get('weight'), x.get('weight'))}" for i, x in enumerate(qs, 1)] or ['chưa có']
        if q.get('note'):
            L += ['', f"_Ghi chú máy: {q['note']}_"]
        L += ['', '## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)']
        L += [f"- {x}" for x in q.get('situations', [])[:3]] or ['- chưa có']
        L += ['', '## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)']
        L += [f"- {x}" for x in q.get('weaknesses', [])[:3]]
        meth = [METHOD.get(x.get('method'), x.get('method')) for x in gap.get(tid, [])]
        if meth:
            L.append(f"- Phương pháp của {len(meth)} video đầu bảng: " + ', '.join(f"{meth.count(m)} {m}" for m in dict.fromkeys(meth)) + '.')
        L += ['', '## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)', '', '| Kênh | Video | Thời lượng | Phương pháp |', '|---|---|---|---|']
        for c in p['competitors']:
            g = gm.get(c['id'], {})
            L.append(f"| {c['channel'].replace('|', '·')} | [{c['id']}](https://youtu.be/{c['id']}) | {mmss(c['min'])} | {METHOD.get(g.get('method'), '—')} |")
        L += ['', '## Video vượt trội cùng đề tài (cho dòng G1)', '']
        L += [f"- {o['channel'].replace('|', '·')} — [{o['id']}](https://youtu.be/{o['id']}) — {mmss(o['min'])} — {o['band']} (tự tính)" for o in p['outliers']] or \
             ['- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo']
        L += ['', '## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail']
        L += [f"- {x}" for x in q.get('title_templates', [])[:3]]
        L += ['- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).', '', '## Từ khoá mô tả', ', '.join(q.get('keywords', [])[:6]) or 'chưa có']
        if q.get('requests'):
            L += ['', '## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)'] + [f"- {x}" for x in q['requests'][:5]]
        (od / f'{tid}.md').write_text('\n'.join(L) + '\n')
        labels[tid] = (p['demand'], p['gap'])
    jdump_labels = ROOT / 'market' / 'topics' / 'labels.json'
    jdump_labels.write_text(json.dumps({'day': d.name, 'labels': labels}, ensure_ascii=False, indent=1))
    print(len(labels), 'hồ sơ cầu →', od)


def cmd_queue():
    """Thêm/cập nhật cột Cầu / Khoảng trống trong topics/queue.md từ market/topics/labels.json (dòng có id trong topics.json)."""
    lab = json.loads((ROOT / 'market' / 'topics' / 'labels.json').read_text())['labels']
    by_row = {t['row']: t['id'] for t in A.TOPICS if t.get('row')}
    by_row.update({20: 's1-rent-vs-buy-history', 21: 's2-rental-vs-index-history'})
    q = ROOT / 'topics' / 'queue.md'
    out = []
    for ln in q.read_text().splitlines():
        cells = ln.split(' | ')
        if ln.startswith('| # |') and 'Cầu' not in ln:
            ln = ln[:-1] + ' Cầu | Khoảng trống |'
        elif ln.startswith('|---') and ln.count('|') == 8:
            ln = ln + '---|---|'
        elif re.match(r'^\| \d+ \|', ln):
            n = int(ln.split('|')[1])
            tid = by_row.get(n)
            c, g = lab.get(tid, ('—', '—')) if tid else ('—', '—')
            parts = ln.rstrip().rstrip('|').split(' | ')
            if len(parts) > 7:      # đã có cột → thay
                parts = parts[:7]
            ln = ' | '.join(parts).rstrip() + f' | {c} | {g} |'
        out.append(ln)
    q.write_text('\n'.join(out) + '\n')
    print('topics/queue.md: cột Cầu / Khoảng trống')


if __name__ == '__main__':
    {'channels': cmd_channels, 'topics': cmd_topics, 'queue': cmd_queue}[sys.argv[1]]()

#!/usr/bin/env python3
"""Ghi phần sinh máy của market/ từ ~/market-cache/<ngày>/ — CHỈ nhãn và định tính, không số liệu thô.

  python3 toolkit/market/report.py channels   # → market/CHANNELS.md
  python3 toolkit/market/report.py topics     # → market/topics/<đề tài>.md (hồ sơ cầu) + bảng nhãn cho topics/queue.md

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


if __name__ == '__main__':
    {'channels': cmd_channels}[sys.argv[1]]()

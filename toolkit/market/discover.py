#!/usr/bin/env python3
"""Tìm kênh theo VIDEO trước (Phiên Thị trường, bước 2). Số liệu thô → ~/market-cache/<ngày>/discover/ (ngoài git).

  python3 toolkit/market/discover.py search      # 3 search/đề tài + vòng 'hình thức' (≈ 66 search = 6.600 đơn vị)
  python3 toolkit/market/discover.py search --topics q12-annuity-raise q13-…   # làm mới vài đề tài (P1 Việc 0)
  python3 toolkit/market/discover.py candidates  # ứng viên: ≥ 3 đề tài + kênh nổi bật + mới nổi + hạt giống
  python3 toolkit/market/discover.py classify    # Haiku headless: vòng tròn + lý do loại (sau pull.py)
  python3 toolkit/market/discover.py aggregate   # videos.list + channels.list, gom kênh theo số đề tài, mở rộng channelSections

Mỗi đề tài (toolkit/market/topics.json): q[0] 30 ngày theo lượt xem, q[1] 90 ngày theo lượt xem, q[0] 90 ngày theo độ liên quan (top 20).
Bộ lọc search: regionCode=US, relevanceLanguage=en, type=video, videoDuration=medium (4–20 phút; video > 20 phút
vẫn vào qua pull.py khi kênh đã là ứng viên). Video dài = > 3 phút, không live (common.is_long).
"""
import datetime as dt, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import yt, videos, channels, cache_dir, jdump, jload, is_long, quota_used

HERE = pathlib.Path(__file__).parent
TOPICS = jload(HERE / 'topics.json')


def rfc(days):
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')


def search(q, days, order, n):
    return yt('search', part='snippet', q=q, type='video', regionCode='US', relevanceLanguage='en',
              videoDuration='medium', publishedAfter=rfc(days), order=order, maxResults=n)


def cmd_search(only=None):
    """only: danh sách id đề tài (làm mới ở P1 Việc 0: đề tài + 2–3 đề tài kế); None = tất cả + vòng hình thức."""
    out = cache_dir() / 'discover' / 'search'
    out.mkdir(parents=True, exist_ok=True)
    jobs = []
    for t in TOPICS['topics']:
        if only and t['id'] not in only:
            continue
        jobs += [(t['id'], 'v30', t['q'][0], 30, 'viewCount', 50),
                 (t['id'], 'v90', t['q'][1], 90, 'viewCount', 50),
                 (t['id'], 'r90', t['q'][0], 90, 'relevance', 20)]
    for i, q in enumerate([] if only else TOPICS['form_circle']):
        jobs.append(('form', f'f{i}', q, 90, 'viewCount', 50))
    for tid, kind, q, days, order, n in jobs:
        f = out / f'{tid}-{kind}.json'
        if f.exists():
            continue
        r = search(q, days, order, n)
        jdump({'topic': tid, 'kind': kind, 'q': q, 'days': days, 'order': order, 'items': r.get('items', [])}, f)
        print(tid, kind, len(r.get('items', [])), quota_used())


def cmd_aggregate():
    d = cache_dir() / 'discover'
    hits = [jload(f) for f in sorted((d / 'search').glob('*.json'))]
    vids = {it['id']['videoId'] for h in hits for it in h['items']}
    vd = videos(sorted(vids))
    jdump(vd, d / 'videos.json')
    by_ch = {}
    for h in hits:
        for it in h['items']:
            v = vd.get(it['id']['videoId'])
            if not v or not is_long(v):
                continue
            lang = (v['snippet'].get('defaultAudioLanguage') or v['snippet'].get('defaultLanguage') or 'en')
            if not lang.startswith('en'):
                continue
            c = by_ch.setdefault(v['snippet']['channelId'], {'topics': set(), 'videos': set(), 'form': False})
            if h['topic'] == 'form':
                c['form'] = True
            else:
                c['topics'].add(h['topic'])
            c['videos'].add(v['id'])
    cd = channels(sorted(by_ch))
    # mở rộng 1 bước: kênh nổi bật (channelSections) của các kênh xuất hiện ≥ 3 đề tài
    strong = [c for c, x in by_ch.items() if len(x['topics']) >= 3]
    featured = {}
    for c in strong:
        r = yt('channelSections', part='contentDetails,snippet', channelId=c)
        for s in r.get('items', []):
            for fc in s.get('contentDetails', {}).get('channels', []) or []:
                featured.setdefault(fc, set()).add(c)
    new = sorted(set(featured) - set(cd))
    cd.update(channels(new))
    jdump(cd, d / 'channels.json')
    agg = {c: {'topics': sorted(x['topics']), 'videos': sorted(x['videos']), 'form': x['form'],
               'featured_by': sorted(featured.get(c, []))} for c, x in by_ch.items()}
    for c in new:
        agg[c] = {'topics': [], 'videos': [], 'form': False, 'featured_by': sorted(featured[c])}
    jdump(agg, d / 'aggregate.json')
    print('video', len(vd), 'kênh', len(agg), 'kênh ≥3 đề tài', len(strong), 'mở rộng', len(new), quota_used())


SEEDS = {'UCKhpM-cu2Cod-GyG6KngNYg': 'Logical Money', 'UCZJnbHQTYBy1I8GpHlsAUMg': 'Jack Explains Money'}


def cmd_candidates():
    """Ứng viên = kênh ≥ 3 đề tài + kênh nổi bật (mở rộng 1 bước) + hạt giống chủ dự án + mới nổi.
    Mới nổi (tự tính, không phải chỉ số YouTube): kênh < 2 năm có video dài tìm được với lượt xem ≥ 3× số người đăng ký
    (sàn 10.000 lượt) hoặc lượt xem/ngày thuộc 10 % cao nhất của các video tìm được."""
    d = cache_dir() / 'discover'
    agg, cd, vd = jload(d / 'aggregate.json'), jload(d / 'channels.json'), jload(d / 'videos.json')
    now = dt.datetime.now(dt.timezone.utc)
    age = lambda iso: (now - dt.datetime.fromisoformat(iso.replace('Z', '+00:00'))).days
    vpd = {}
    for v in vd.values():
        if is_long(v):
            vpd[v['id']] = int(v['statistics'].get('viewCount', 0)) / max(age(v['snippet']['publishedAt']), 1)
    top10 = sorted(vpd.values())[int(len(vpd) * 0.9)] if vpd else 0
    emerging = {}
    for vid, r in vpd.items():
        v = vd[vid]; c = v['snippet']['channelId']; ch = cd.get(c)
        if not ch or age(ch['snippet']['publishedAt']) >= 730:
            continue
        subs = int(ch['statistics'].get('subscriberCount', 0)); views = int(v['statistics'].get('viewCount', 0))
        why = []
        if views >= 10_000 and views >= 3 * max(subs, 1):
            why.append('lượt xem ≥ 3× người đăng ký')
        if r >= top10:
            why.append('lượt xem/ngày thuộc 10 % cao nhất')
        if why:
            emerging.setdefault(c, set()).update(why)
    cand = {}
    for c, x in agg.items():
        src = []
        if len(x['topics']) >= 3: src.append('≥ 3 đề tài')
        if x['featured_by']: src.append('kênh nổi bật của ứng viên')
        if c in emerging: src.append('mới nổi: ' + ', '.join(sorted(emerging[c])))
        if src: cand[c] = src
    for c in SEEDS:
        cand.setdefault(c, []).insert(0, 'từ chủ dự án')
    jdump({'channels': sorted(cand), 'why': cand, 'top10_vpd': top10}, d / 'candidates.json')
    print(len(cand), 'ứng viên;', sum('mới nổi' in ' '.join(v) for v in cand.values()), 'có cờ mới nổi')


CLASSIFY = '''You classify YouTube channels for a US personal-finance data-explainer channel (topics: debt/loans, retirement/investing, taxes).
For each channel return one JSON object. Fields:
- "id": channel id as given
- "circle": "direct" (explains US personal finance with data/math/simulations, long videos), "adjacent" (US-focused financial education with a human presenter/talking head, interviews, advisor channels), "form" (data/visual explainer outside personal finance — useful only for packaging), or "none"
- "exclude": list of reasons from ["sells_course_or_stock_picks", "news", "not_english_or_not_us_audience", "off_topic", "product_sales"]; empty if none. Advisor channels that only advertise their own practice are NOT excluded unless they sell courses/products or stock picks.
- "presenter": "face" | "voice_only" | "unknown" (guess from titles/description)
- "style": one short English phrase (e.g. "two-character scenario simulations", "talk show", "advisor Q&A")
- "why": one short English sentence
Return a JSON array only.

CHANNELS:
'''


def cmd_classify():
    from ai import ask
    d = cache_dir() / 'discover'
    cand = jload(d / 'candidates.json')
    now = dt.datetime.now(dt.timezone.utc)
    rows = []
    for c in cand['channels']:
        f = cache_dir() / 'pull' / f'{c}.json'
        if not f.exists():
            continue
        p = jload(f)
        recent = [v for v in p['videos'] if (now - dt.datetime.fromisoformat(v['publishedAt'].replace('Z', '+00:00'))).days <= 90]
        rows.append({'id': c, 'title': p['channel']['title'], 'country': p['channel']['country'],
                     'description': p['channel']['description'][:500],
                     'recent_long_titles': [v['title'] for v in recent[-15:]] or [v['title'] for v in p['videos'][-8:]],
                     'long_videos_last_90d': len(recent)})
    out = {}
    for i in range(0, len(rows), 10):
        res = ask(CLASSIFY + json.dumps(rows[i:i + 10], ensure_ascii=False, indent=1), task='classify-channels')
        for r in res:
            out[r['id']] = r
    for r in rows:
        out.setdefault(r['id'], {'id': r['id'], 'circle': 'none', 'exclude': ['unclassified']})
        out[r['id']]['long_videos_last_90d'] = r['long_videos_last_90d']
    jdump(out, d / 'classified.json')
    print(len(out), 'kênh đã phân loại')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'search' and '--topics' in a:
        cmd_search(a[a.index('--topics') + 1:])
        sys.exit()
    {'classify': cmd_classify, 'search': cmd_search, 'aggregate': cmd_aggregate, 'candidates': cmd_candidates}[sys.argv[1]]()

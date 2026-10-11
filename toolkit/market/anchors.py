#!/usr/bin/env python3
"""Video NEO cho G1 và quét xu hướng 7 ngày cho P4 (D-012 mục 3, tổng kết Tập 6 §4a, §4d). Số thô → ~/market-cache/<ngày>/anchors/ (ngoài git,
Developer Policies III.E.4); repo chỉ nhận liên kết, kênh, nhãn tự tính, khoảng trống định tính. Không dùng relatedToVideoId (YouTube đã bỏ khỏi API).

  python3 toolkit/market/anchors.py anchors --topic q13-15-vs-30-mortgage --question "<câu hỏi KHÁN GIẢ, tiếng Anh, không nêu phương pháp>" [--n 3]
      (câu hỏi có "over real history" → Haiku loại mọi video giả định cố định; thử 11/10 với #20: 0 neo → bỏ phần phương pháp: 3 neo)
      → 1–3 video NEO: cùng câu hỏi (Haiku xét tiêu đề + mô tả), đăng 30–90 ngày, tốc độ lượt xem/ngày cao nhất trong đề tài;
        mỗi neo: liên kết, kênh, nhãn tốc độ (so trung vị của đề tài), phương pháp (giả định cố định / ý kiến / lịch sử thật), khoảng trống
        mà tập lấp (vd "không phát lại lịch sử thật"), cụm từ tìm kiếm khán giả gõ. In dòng G1: "neo: …; khác biệt: …".
  python3 toolkit/market/anchors.py trend --topic <id> [--days 7]
      → video đăng ≤ 7 ngày của đề tài, xếp theo lượt xem/ngày; Sonnet đọc tiêu đề + thumbnail (URL, không lưu ảnh) → mẫu đang lên
        (khuôn tiêu đề, kiểu thumbnail, từ khoá) cho toolkit/package/rescore.py.
Hạn mức: 2 search/đề tài (200 đơn vị) + videos.list; dừng trước 9.500 đơn vị/ngày (mcommon).
"""
import datetime as dt, json, pathlib, re, statistics as st, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mcommon import yt, videos, iso_dur, cache_dir, jdump, jload, label, OWN_CHANNELS   # noqa: E402
import ai   # noqa: E402

TOPICS = {t['id']: t for t in jload(pathlib.Path(__file__).parent / 'topics.json')['topics']}


def rfc(days):
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')


def pool(topic, days_max, days_min=0):
    ids = []
    for q in TOPICS[topic]['q'][:2]:
        r = yt('search', part='snippet', q=q, type='video', regionCode='US', relevanceLanguage='en', order='viewCount',
               publishedAfter=rfc(days_max), publishedBefore=rfc(days_min) if days_min else None, maxResults=50)
        ids += [it['id']['videoId'] for it in r.get('items', [])]
    now = dt.datetime.now(dt.timezone.utc); rows = []
    for vid, it in videos(ids).items():
        if iso_dur(it['contentDetails'].get('duration')) < 240 or it['snippet'].get('channelId') in OWN_CHANNELS:
            continue   # bỏ Shorts, video < 4 phút, và video của chính kênh mình
        t = it['snippet']['title']
        if re.search(r'₹|\blakh|\bcrore|\bSIP\b|\bSWP\b|\bEPF|\bNPS\b|£|\bUK\b|\bCanada|\bTFSA|\bRRSP|\bsuper(annuation)?\b', t, re.I) \
                or sum(ord(ch) > 0x24F for ch in t) > 3 or it['snippet'].get('defaultAudioLanguage', 'en')[:2] not in ('en', ''):
            continue   # thử 11/10: regionCode=US vẫn trả video Ấn Độ/Anh/Canada (₹, lakh, SIP) → lệch mẫu đang lên của khán giả Mỹ
        pub = dt.datetime.fromisoformat(it['snippet']['publishedAt'].replace('Z', '+00:00'))
        age = max((now - pub).total_seconds() / 86400, 1)
        rows.append({'id': vid, 'channel': it['snippet']['channelTitle'], 'title': it['snippet']['title'],
                     'desc': it['snippet'].get('description', '')[:600], 'age_d': round(age, 1),
                     'vpd': int(it['statistics'].get('viewCount', 0)) / age, 'dur_s': iso_dur(it['contentDetails']['duration']),
                     'thumb': it['snippet']['thumbnails'].get('high', {}).get('url')})
    return sorted(rows, key=lambda r: -r['vpd'])


def cmd_anchors(topic, question, n=3):
    rows = pool(topic, 90, 30)
    if not rows:
        print('chưa có video 30–90 ngày cho đề tài'); return []
    med = st.median(r['vpd'] for r in rows)
    top = rows[:15]
    judge = ai.ask('For each video below, judge whether it answers the SAME viewer question as: "' + question + '". '
                   'Return JSON list [{"i":<index>,"same":true/false,"method":"fixed assumption|opinion|real history replay|news","gap":"<what it does not do that a '
                   'replay of real US history would add, <=12 words>","phrase":"<the search phrase a viewer would type to find it, <=6 words>"}].\n'
                   + '\n'.join(f'{i}. {r["title"]} — {r["desc"][:300]}' for i, r in enumerate(top)), task='anchors')
    out = []
    for j in judge:
        if not 0 <= j.get('i', -1) < len(top):
            continue
        r = top[j['i']]
        if j.get('same') and len(out) < n:
            out.append({'link': f'https://youtu.be/{r["id"]}', 'channel': r['channel'], 'speed': label(r['vpd'] / med, 1.5, 3) if med else 'chưa có',
                        'method': j.get('method'), 'gap': j.get('gap'), 'phrase': j.get('phrase')})
    jdump({'topic': topic, 'question': question, 'rows': rows, 'judge': judge}, cache_dir() / 'anchors' / f'{topic}.json')
    for a in out:
        print(f"neo: {a['channel']} {a['link']} (tốc độ {a['speed']} so trung vị đề tài, {a['method']}); khác biệt: {a['gap']} · cụm tìm kiếm: {a['phrase']}")
    return out


def cmd_trend(topic, days=7):
    rows = pool(topic, days)[:10]
    if not rows:
        print(f'không có video ≤ {days} ngày'); return {}
    urls = [r['thumb'] for r in rows if r['thumb']][:8]
    pat = ai.look(urls, 'These are the fastest-rising YouTube videos of the last week on one personal-finance topic. Titles: '
                  + json.dumps([r['title'] for r in rows]) + '. Return JSON {"title_patterns":["<abstract pattern, no copying>"x3],'
                  '"thumbnail_patterns":["<abstract style>"x3],"keywords":["<search phrase>"x5]}', task='trend')
    jdump({'topic': topic, 'days': days, 'rows': rows, 'patterns': pat}, cache_dir() / 'anchors' / f'{topic}-trend{days}.json')
    print(json.dumps(pat, ensure_ascii=False, indent=1))
    return pat


if __name__ == '__main__':
    a = sys.argv[1:]; opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d   # noqa: E731
    if a[0] == 'anchors':
        res = cmd_anchors(opt('--topic'), opt('--question', TOPICS[opt('--topic')]['title']), int(opt('--n', 3)))
        if opt('--save'): pathlib.Path(opt('--save')).write_text(json.dumps(res, ensure_ascii=False, indent=1))
    elif a[0] == 'trend':
        res = cmd_trend(opt('--topic'), int(opt('--days', 7)))
        if opt('--save'): pathlib.Path(opt('--save')).write_text(json.dumps(res, ensure_ascii=False, indent=1))

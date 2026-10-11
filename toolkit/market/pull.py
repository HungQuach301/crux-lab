#!/usr/bin/env python3
"""Kéo video 24 tháng của một danh sách kênh (Phiên Thị trường, bước 4). Số liệu thô → ~/market-cache/<ngày>/pull/<kênh>.json (ngoài git).

  python3 toolkit/market/pull.py UCxxx [UCyyy …]
  python3 toolkit/market/pull.py --from <tệp.json có khoá "channels": [id…]>

uploads playlist → playlistItems (50/lượt, dừng khi cũ hơn 24 tháng) → videos.list (50/lượt). Bỏ Shorts (≤ 3 phút) và live.
Chi ≈ 2 đơn vị cho mỗi 50 video. Đã có tệp của ngày thì bỏ qua (--force để kéo lại).
"""
import datetime as dt, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import yt, videos, channels, cache_dir, jdump, jload, is_long, iso_dur, quota_used

MONTHS = 24
TS = re.compile(r'^\s*[\(\[]?(\d{1,2}:)?\d{1,2}:\d{2}\b', re.M)


def has_chapters(desc):
    """Chương YouTube: mốc đầu 0:00 và ≥ 3 mốc trong mô tả."""
    ts = TS.findall(desc)
    return len(ts) >= 3 and bool(re.search(r'^\s*[\(\[]?(0?0:)?0?0:00\b', desc, re.M))


def pull(cid, force=False):
    out = cache_dir() / 'pull' / f'{cid}.json'
    if out.exists() and not force:
        return jload(out)
    ch = channels([cid]).get(cid)
    if not ch:
        return None
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=MONTHS * 30.44)).isoformat()
    ids, page = [], None
    up = ch['contentDetails']['relatedPlaylists']['uploads']
    while True:
        try:
            r = yt('playlistItems', part='contentDetails', playlistId=up, maxResults=50, pageToken=page)
        except RuntimeError as e:          # kênh không có uploads công khai
            if 'HTTP 404' in str(e):
                break
            raise
        items = r.get('items', [])
        ids += [it['contentDetails']['videoId'] for it in items
                if it['contentDetails'].get('videoPublishedAt', '9') >= cutoff]
        page = r.get('nextPageToken')
        if not page or not items or min(it['contentDetails'].get('videoPublishedAt', '9') for it in items) < cutoff:
            break
    vd = videos(ids)
    vids = []
    for v in vd.values():
        if not is_long(v):
            continue
        s, st = v['snippet'], v.get('statistics', {})
        vids.append({'id': v['id'], 'title': s['title'], 'publishedAt': s['publishedAt'],
                     'duration': iso_dur(v['contentDetails']['duration']),
                     'views': int(st.get('viewCount', 0)), 'likes': int(st.get('likeCount', 0)),
                     'comments': int(st.get('commentCount', 0)),
                     'chapters': has_chapters(s.get('description', '')),
                     'description': s.get('description', '')[:1500],
                     'thumb': (s.get('thumbnails', {}).get('high') or s.get('thumbnails', {}).get('default') or {}).get('url'),
                     'lang': s.get('defaultAudioLanguage') or s.get('defaultLanguage')})
    vids.sort(key=lambda x: x['publishedAt'])
    data = {'channel': {'id': cid, 'title': ch['snippet']['title'], 'country': ch['snippet'].get('country'),
                        'publishedAt': ch['snippet']['publishedAt'], 'description': ch['snippet'].get('description', '')[:1500],
                        'subs': int(ch['statistics'].get('subscriberCount', 0)),
                        'videoCount': int(ch['statistics'].get('videoCount', 0))},
            'pulledAt': dt.datetime.now(dt.timezone.utc).isoformat(), 'videos': vids}
    jdump(data, out)
    return data


if __name__ == '__main__':
    a = sys.argv[1:]
    force = '--force' in a
    a = [x for x in a if x != '--force']
    ids = jload(a[1])['channels'] if a and a[0] == '--from' else a
    for c in ids:
        d = pull(c, force)
        print(c, d and d['channel']['title'], d and len(d['videos']), quota_used())

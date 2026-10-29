# R3 bước 1: search.list 9 cửa sổ × 9 truy vấn + mostPopular US mọi category → ~/market-cache/<ngày>/r3/
# Dùng toolkit/market/mcommon.yt (proxy gắn khoá, ghi quota.jsonl).
import sys, json, datetime as dt
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from mcommon import yt, cache_dir, quota_used
out = cache_dir() / 'r3'; out.mkdir(exist_ok=True)
NOW = dt.datetime(2026, 10, 29, tzinfo=dt.timezone.utc)
GROUPS = [
 ('finance', 'finance|money|personal finance|investing|stock market'),
 ('economy', 'economy|business|billionaire|company'),
 ('crime', 'true crime|mystery|unsolved|case'),
 ('history', 'history|documentary|war|ancient'),
 ('tech', 'AI|tech|technology|explained|science'),
 ('survival', 'survival|challenge|story|experiment'),
 ('gaming', 'gaming|minecraft|podcast|interview|reaction'),
]
log = []
res = {}
windows = []
for i in range(9):
    end = NOW - dt.timedelta(days=7*i); start = end - dt.timedelta(days=7)
    windows.append((start, end))
for (s, e) in windows:
    w = s.date().isoformat()
    jobs = [(g, q, 'medium') for g, q in GROUPS] + [('all', None, 'medium'), ('all', None, 'long')]
    for g, q, dur in jobs:
        key = f'{w}|{g}|{dur}'
        try:
            d = yt('search', part='snippet', type='video', order='viewCount', videoDuration=dur,
                   relevanceLanguage='en', regionCode='US', maxResults=50, q=q,
                   publishedAfter=s.strftime('%Y-%m-%dT%H:%M:%SZ'), publishedBefore=e.strftime('%Y-%m-%dT%H:%M:%SZ'))
        except RuntimeError as ex:
            log.append({'key': key, 'error': str(ex)[:200]}); print('ERR', key, ex); continue
        ids = [it['id']['videoId'] for it in d.get('items', [])]
        res[key] = ids
        log.append({'key': key, 'n': len(ids)})
        print(key, len(ids), quota_used(), flush=True)
json.dump(res, open(out / 'search.json', 'w'))
json.dump(log, open(out / 'search-log.json', 'w'))
# mostPopular US mọi category
cats = yt('videoCategories', part='snippet', regionCode='US')
pop = {}
for c in [None] + [c['id'] for c in cats['items'] if c['snippet'].get('assignable')]:
    ids, tok = [], None
    for _ in range(4):
        try:
            d = yt('videos', part='id', chart='mostPopular', regionCode='US', maxResults=50, videoCategoryId=c, pageToken=tok)
        except RuntimeError as ex:
            print('pop err', c, str(ex)[:120]); break
        ids += [it['id'] for it in d.get('items', [])]
        tok = d.get('nextPageToken')
        if not tok: break
    pop[c or 'all'] = ids
json.dump(pop, open(out / 'popular.json', 'w'))
print('done', quota_used())

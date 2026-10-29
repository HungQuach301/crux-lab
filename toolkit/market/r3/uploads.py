# R3 bước 2b: lịch sử đăng của kênh ứng viên + ảnh chụp video 0–3 ngày ≥ 100k
import sys, json, datetime as dt
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from mcommon import yt, cache_dir, quota_used, iso_dur
out = cache_dir() / 'r3'
young = json.load(open(out / 'young.json')); ch = json.load(open(out / 'channels-big.json'))
allv = json.load(open(out / 'videos-all.json'))
P = lambda x: dt.datetime.fromisoformat(x.replace('Z', '+00:00'))
NOW = dt.datetime(2026, 10, 29, 12, tzinfo=dt.timezone.utc)
up = {}
for cid in sorted(set(v['channelId'] for v in young if v['dur'] >= 180)):
    items, tok = [], None
    for _ in range(3):   # ≤150 video gần nhất
        d = yt('playlistItems', part='contentDetails', playlistId=ch[cid]['uploads'], maxResults=50, pageToken=tok)
        items += [(it['contentDetails']['videoId'], it['contentDetails'].get('videoPublishedAt')) for it in d['items']]
        tok = d.get('nextPageToken')
        if not tok: break
    ids = [i for i, _ in items]
    st = {}
    for i in range(0, len(ids), 50):
        d = yt('videos', part='statistics,contentDetails,snippet', id=','.join(ids[i:i+50]))
        for it in d['items']:
            st[it['id']] = {'publishedAt': it['snippet']['publishedAt'], 'views': int(it['statistics'].get('viewCount', 0)),
                            'dur': iso_dur(it['contentDetails']['duration']), 'title': it['snippet']['title']}
    up[cid] = {'complete': tok is None, 'videos': st}
json.dump(up, open(out / 'uploads.json', 'w'))
# ảnh chụp: video 0–3 ngày, ≥100k
recent = [v for v in allv.values() if v['views'] >= 100_000 and (NOW - P(v['publishedAt'])).days <= 3]
need = sorted(set(v['channelId'] for v in recent) - set(ch))
for i in range(0, len(need), 50):
    d = yt('channels', part='snippet,statistics', id=','.join(need[i:i+50]))
    for it in d['items']:
        ch[it['id']] = {'id': it['id'], 'title': it['snippet']['title'], 'created': it['snippet']['publishedAt'], 'country': it['snippet'].get('country'),
                        'subs': int(it['statistics'].get('subscriberCount', 0) or 0), 'videoCount': int(it['statistics'].get('videoCount', 0) or 0)}
snap = []
for v in recent:
    c = ch.get(v['channelId'])
    if not c: continue
    age = (P(v['publishedAt']) - P(c['created'])).total_seconds() / 86400
    if age <= 31:
        snap.append({'id': v['id'], 'channelId': v['channelId'], 'publishedAt': v['publishedAt'], 'views': v['views'], 'dur': v['dur'],
                     'chCreated': c['created'], 'chAgeAtPublish': round(age, 1), 'snapAt': NOW.isoformat()})
json.dump(ch, open(out / 'channels-all.json', 'w'))
json.dump(snap, open(out / 'snap-20261029.json', 'w'), indent=1)
print('uploads', len(up), 'recent', len(recent), 'snap', len(snap), 'snap long', sum(s['dur'] >= 180 for s in snap), quota_used())

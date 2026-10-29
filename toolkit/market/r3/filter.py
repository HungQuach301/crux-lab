# R3 bước 2: videos.list + channels.list, giữ ≥ 1M và kênh ≤ 31 ngày tuổi lúc đăng
import sys, json, datetime as dt
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from mcommon import yt, cache_dir, quota_used, iso_dur
out = cache_dir() / 'r3'
s = json.load(open(out / 'search.json')); p = json.load(open(out / 'popular.json'))
ids = sorted(set(x for v in s.values() for x in v) | set(x for v in p.values() for x in v))
vids = {}
for i in range(0, len(ids), 50):
    d = yt('videos', part='snippet,statistics,contentDetails', id=','.join(ids[i:i+50]), maxResults=50)
    for it in d['items']:
        sn, st, cd = it['snippet'], it.get('statistics', {}), it['contentDetails']
        vids[it['id']] = {'id': it['id'], 'title': sn['title'], 'channelId': sn['channelId'], 'channel': sn['channelTitle'],
            'publishedAt': sn['publishedAt'], 'categoryId': sn.get('categoryId'), 'lang': sn.get('defaultAudioLanguage') or sn.get('defaultLanguage'),
            'views': int(st.get('viewCount', 0)), 'likes': int(st.get('likeCount', 0) or 0), 'comments': int(st.get('commentCount', 0) or 0),
            'dur': iso_dur(cd['duration']), 'live': sn.get('liveBroadcastContent'), 'tags': sn.get('tags', [])[:15],
            'desc': sn.get('description', '')[:300], 'thumb': (sn.get('thumbnails', {}).get('high') or {}).get('url')}
json.dump(vids, open(out / 'videos-all.json', 'w'))
big = {k: v for k, v in vids.items() if v['views'] >= 1_000_000}
chs = sorted(set(v['channelId'] for v in big.values()))
# Short ứng viên (<180s, >=1M) cũng lấy kênh để làm danh sách phụ
chinfo = {}
for i in range(0, len(chs), 50):
    d = yt('channels', part='snippet,statistics,contentDetails', id=','.join(chs[i:i+50]), maxResults=50)
    for it in d['items']:
        chinfo[it['id']] = {'id': it['id'], 'title': it['snippet']['title'], 'created': it['snippet']['publishedAt'],
            'country': it['snippet'].get('country'), 'customUrl': it['snippet'].get('customUrl'),
            'subs': int(it['statistics'].get('subscriberCount', 0) or 0), 'hiddenSubs': it['statistics'].get('hiddenSubscriberCount'),
            'videoCount': int(it['statistics'].get('videoCount', 0) or 0), 'viewCount': int(it['statistics'].get('viewCount', 0) or 0),
            'uploads': it['contentDetails']['relatedPlaylists']['uploads'], 'desc': it['snippet'].get('description', '')[:300]}
json.dump(chinfo, open(out / 'channels-big.json', 'w'))
P = lambda x: dt.datetime.fromisoformat(x.replace('Z', '+00:00'))
young = []
for v in big.values():
    c = chinfo.get(v['channelId'])
    if not c: continue
    age = (P(v['publishedAt']) - P(c['created'])).total_seconds() / 86400
    v['chAge'] = round(age, 1)
    if age <= 31: young.append(v)
print('videos', len(vids), 'big', len(big), 'channels', len(chs), 'young', len(young),
      'young long', sum(v['dur'] >= 180 for v in young), quota_used())
json.dump(young, open(out / 'young.json', 'w'))

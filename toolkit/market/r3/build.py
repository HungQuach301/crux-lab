# R3 bước 3: phân lớp A/B, loại kênh tái dụng, ghi market/r3/*.json (nhãn ngách/định dạng gán tay sau khi xem tiêu đề + ảnh bìa)
import json, datetime as dt, pathlib, collections
C = pathlib.Path.home() / 'market-cache/2026-10-29/r3'; Q = C.parent / 'quota.jsonl'
R = pathlib.Path(__file__).resolve().parents[3] / 'market/r3'; R.mkdir(parents=True, exist_ok=True)
P = lambda x: dt.datetime.fromisoformat(x.replace('Z', '+00:00'))
NOW = dt.datetime(2026, 10, 29, 12, tzinfo=dt.timezone.utc)
META = {'fetchedAt': '2026-10-29', 'deleteOrRefreshBy': '2026-11-28',
        'note': 'Số liệu công khai YouTube Data API v3. Chủ dự án 29/10 cho commit, hạn làm mới/xoá 28/11/2026 (YouTube API Developer Policies III.E.4).'}
young = json.load(open(C / 'young.json')); ch = json.load(open(C / 'channels-big.json')); up = json.load(open(C / 'uploads.json'))
s = json.load(open(C / 'search.json')); pop = json.load(open(C / 'popular.json'))
EXCL_BY_CH = {
 'México Innovador': 'tên + mô tả kênh tiếng Tây Ban Nha về Mexico, nội dung tiếng Anh về Elon Musk; video đầu tiên 23 ngày sau ngày tạo → dấu hiệu kênh tái dụng',
 'Business by baniya': 'sau video hit chuyển hẳn sang livestream pegboard/bảng từ → đổi chủ đề đột ngột, nghi bán/tái dụng',
 'Munna Toon World': '4 video đầu là Shorts "#montagem #mhacommunity", rồi đổi sang truyện rau củ Hindi → đổi chủ đề',
 'cartoonkudo': '4 video đầu là Shorts mèo/dê tiếng Anh, rồi đổi sang truyện Hindi → đổi chủ đề',
 'Sabji By Yash': 'tiêu đề trùng gần nguyên văn video của Sabzi Nagar World đăng 4 ngày trước → nghi đăng lại',
}
FLAG_BY_CH = {
 'SSundeePlus': 'kênh phụ của SSundee (YouTuber lâu năm) — không phải kênh mới hữu cơ',
 'Bridge Productions': 'kênh hãng phim, video quảng bá phim có ngôi sao (Ravi Teja)',
 'Coov Records Official': 'kênh hãng nhạc, có ca sĩ/diễn viên sẵn',
 'KrishoPlays': 'dùng nhân vật Doraemon/Shin-chan (IP bên thứ ba)',
 'Spencer Knows!': 'cùng người với Call Spencer! (2 kênh)',
 'Call Spencer!': 'cùng người với Spencer Knows! (2 kênh)',
 'きれいなゴミ箱': 'nhạc meme AI tiếng Nhật, chủ đề người lớn',
}
NICHE = {
 'u5F175REX_U': ('tin tức giải thích / địa lý', 'không lộ mặt; bản đồ 3D', 'en'),
 '9-wrTgva9xk': ('lịch sử / phim tài liệu', 'không lộ mặt; tranh AI + giọng đọc', 'hi/en'),
 '0tSwA12rEtk': ('lịch sử cổ đại / "how did"', 'không lộ mặt; minh hoạ mặt cắt', 'en'),
 'YLrdEkZncAo': ('truyện đạo đức / drama gia đình', 'không lộ mặt; hình AI', 'bn'),
 'lgz9pbKbOTQ': ('truyện hoạt hình rau củ (nghèo → giàu)', 'không lộ mặt; hoạt hình AI 3D', 'hi'),
 '_dc9OmLUzuU': ('hoạt hình thiếu nhi rau củ', 'không lộ mặt; hoạt hình AI', 'bn'),
 '7ShrUmwrR1U': ('mẹo công nghệ / quyền riêng tư', 'LỘ MẶT; quay màn hình', 'en'),
 '2ZJhVKnIKmk': ('hoạt hình thiếu nhi rau củ', 'không lộ mặt; hoạt hình AI', 'hi'),
 '4L4ErMYyMJU': ('truyện đạo đức nông thôn', 'không lộ mặt; hình AI', 'hi'),
 'alzq9TYSMX8': ('hoạt hình thiếu nhi rau củ', 'không lộ mặt; hoạt hình AI', 'hi'),
 'hFxcsAyonKw': ('hoạt hình 3D thiếu nhi (đua xe)', 'không lộ mặt; hoạt hình 3D', 'en/hi'),
 'VMPYMYuGxms': ('gaming Minecraft', 'không lộ mặt (avatar); có giọng thật', 'en'),
 'ihGK1iyUN1E': ('lịch sử "toàn bộ X trong 10 phút"', 'không lộ mặt; hoạt hình 2D', 'en'),
 '5J90D5NTDhA': ('nhạc meme AI', 'không lộ mặt; nhạc + hình AI', 'ja'),
 'ZQSOransWxk': ('hoạt hình thiếu nhi rau củ', 'không lộ mặt; hoạt hình AI', 'hi'),
 'cIjNzXlWZzg': ('thần thoại / đền chùa Odisha', 'không lộ mặt; hình AI', 'or'),
 '-70ITYN4RY0': ('hoạt hình thiếu nhi (nhân vật có IP)', 'không lộ mặt; hoạt hình AI', 'en'),
 'wStCAWCJKv8': ('thí nghiệm kiến "1000 ants vs"', 'không lộ mặt; quay cận/CGI', 'en'),
 'rExDQd6hsMU': ('mẹo công nghệ / quyền riêng tư', 'LỘ MẶT; quay màn hình', 'en'),
 '-v8e95Cx9Zc': ('quảng bá phim Telugu', 'phim tài liệu hậu trường', 'te'),
 'b2ClWB7bPLY': ('kinh doanh / "economics of X"', 'không lộ mặt; giọng đọc', 'hi'),
 '59S5LE28cLo': ('du lịch làng quê / tài liệu', 'không lộ mặt; footage + giọng', 'ur'),
 'Xn1s4JvDKYY': ('lịch sử đô thị timelapse 3D', 'không lộ mặt; 3D, "No AI imagery"', 'en'),
 'S4Sbl7K9Up4': ('công nghệ / Elon vs China', 'không lộ mặt', 'en'),
 'Dbyu2Eizw5U': ('truyện hoạt hình rau củ', 'không lộ mặt; hoạt hình AI', 'en/hi'),
 'C6-FIlJaPNk': ('kể chuyện người nổi tiếng Mỹ cổ điển', 'không lộ mặt; clip lưu trữ + hình AI', 'en'),
 'Owv2qnEdqfA': ('series nhạc kịch Ấn', 'diễn viên thật (hãng nhạc)', 'hi'),
 'DKB8oMQHbH8': ('truyện hoạt hình rau củ (nghèo → giàu)', 'không lộ mặt; hoạt hình AI', 'hi'),
 'tHIbsYo_Uyw': ('truyện hoạt hình rau củ', 'không lộ mặt; hoạt hình AI', 'hi'),
 'ejuIUDRjq8M': ('hoạt hình thiếu nhi', 'không lộ mặt; hoạt hình 3D', 'es'),
}
A_LO, A_MID = 0.5, 0.3
rows, excluded, shorts = [], [], []
for v in young:
    c = ch[v['channelId']]; U = up.get(v['channelId'], {}).get('videos', {})
    vs = sorted(U.values(), key=lambda x: x['publishedAt'])
    age = (NOW - P(v['publishedAt'])).total_seconds() / 86400
    base = {'id': v['id'], 'url': 'https://www.youtube.com/watch?v=' + v['id'], 'title': v['title'], 'channel': v['channel'],
            'channelId': v['channelId'], 'channelCreated': c['created'], 'publishedAt': v['publishedAt'],
            'channelAgeAtPublishDays': v['chAge'], 'videoAgeDays': round(age, 1), 'views': v['views'], 'likes': v['likes'],
            'comments': v['comments'], 'durationSec': v['dur'], 'categoryId': v['categoryId'], 'audioLang': v['lang'],
            'channelSubs': c['subs'], 'channelVideoCount': c['videoCount'], 'channelCountry': c['country']}
    if v['dur'] < 180:
        shorts.append(base); continue
    sh = [x for x in vs if x['dur'] < 180]
    base.update({'firstVideo': vs[0]['publishedAt'] if vs else None, 'firstVideoTitle': vs[0]['title'] if vs else None,
                 'firstBeforeCreated': bool(vs) and vs[0]['publishedAt'] < c['created'],
                 'indexInChannel': sum(x['publishedAt'] < v['publishedAt'] for x in vs) + 1,
                 'uploadsPerWeek': round(len(vs) / ((P(vs[-1]['publishedAt']) - P(vs[0]['publishedAt'])).days + 1) * 7, 1) if vs else None,
                 'channelShorts': len(sh), 'channelShortsViews': sum(x['views'] for x in sh),
                 'niche': NICHE[v['id']][0], 'format': NICHE[v['id']][1], 'lang': NICHE[v['id']][2],
                 'faceless': 'LỘ MẶT' not in NICHE[v['id']][1] and v['channel'] not in ('Coov Records Official', 'Bridge Productions'),
                 'personalFinance': False, 'flag': FLAG_BY_CH.get(v['channel'])})
    oth = sorted(x['views'] for k, x in U.items() if k != v['id'] and x['dur'] >= 180)
    med = oth[len(oth) // 2] if oth else None
    base['hitToMedianOtherLong'] = round(v['views'] / max(med, 1)) if med is not None else None
    base['subsPer1kViews'] = round(c['subs'] / v['views'] * 1000, 1)
    base['paidPromoSuspect'] = bool(med is not None and v['views'] / max(med, 1) > 100 and base['subsPer1kViews'] < 1.5)
    if age <= 8.5:
        base['class'] = 'A'; base['v7'] = None
    else:
        lo, mid = v['views'] * (7 / age) ** A_LO, v['views'] * (7 / age) ** A_MID
        base['v7_low'], base['v7_mid'] = round(lo), round(mid)
        base['class'] = 'B1' if lo >= 1e6 else 'B2' if mid >= 1e6 else 'loại: ước ngày 7 < 1M'
    if v['channel'] in EXCL_BY_CH:
        base['excludeReason'] = EXCL_BY_CH[v['channel']]; excluded.append(base)
    elif base['class'].startswith('loại'):
        base['excludeReason'] = base['class']; excluded.append(base)
    else:
        rows.append(base)
rows.sort(key=lambda r: (r['lang'].split('/')[0] != 'en', r['class'], -r['views']))
units = collections.Counter(); n = collections.Counter()
for line in Q.read_text().splitlines():
    r = json.loads(line); units[r['method']] += r['units']; n[r['method']] += 1
quota = {**META, 'unitsByMethod': dict(units), 'callsByMethod': dict(n), 'totalUnits': sum(units.values()), 'budget': 9000}
json.dump({**META, 'model': {'v7': 'views_now * (7/age_days)^alpha', 'alpha_mid': A_MID, 'alpha_low': A_LO}, 'videos': rows}, open(R / 'candidates.json', 'w'), ensure_ascii=False, indent=1)
json.dump({**META, 'videos': excluded}, open(R / 'excluded.json', 'w'), ensure_ascii=False, indent=1)
json.dump({**META, 'videos': sorted(shorts, key=lambda r: -r['views'])}, open(R / 'shorts.json', 'w'), ensure_ascii=False, indent=1)
json.dump(quota, open(R / 'quota.json', 'w'), indent=1)
json.dump({**META, 'searchCalls': {k: len(x) for k, x in s.items()}, 'popularIdsByCategory': {k: len(x) for k, x in pop.items()},
           'uniqueVideos': 5637, 'videosGe1M': 2484, 'channelsChecked': 1933, 'youngGe1M': len(young)}, open(R / 'funnel.json', 'w'), indent=1)
snap = json.load(open(C / 'snap-20261029.json'))
json.dump({**META, 'videos': snap}, open(R / 'snap-20261029.json', 'w'), indent=1)
print(len(rows), collections.Counter(r['class'] for r in rows), 'excl', len(excluded), 'shorts', len(shorts), quota['totalUnits'])
for r in rows: print(r['class'], r['lang'], r['views'], r.get('v7_low'), r.get('v7_mid'), r['videoAgeDays'], r['channel'])
for r in excluded: print('X', r['channel'], r['excludeReason'][:50])

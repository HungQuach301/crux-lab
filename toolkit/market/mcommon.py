# Dùng chung cho toolkit/market: gọi YouTube Data API v3 qua proxy (proxy gắn X-Goog-Api-Key, key không có trong phiên),
# đếm hạn mức, chỗ lưu số liệu thô NGOÀI git (~/market-cache/<ngày>/, YouTube API Developer Policies III.E.4).
# Repo chỉ chứa mã, kết luận định tính và nhãn; không ghi số liệu thô của kênh khác vào repo.
import datetime as dt, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request

API = 'https://www.googleapis.com/youtube/v3/'
COST = {'search': 100}           # mọi phương thức đọc khác 1 đơn vị
DAY_UNITS, DAY_SEARCH = 10_000, 100
SAFE_UNITS, SAFE_SEARCH = 9_500, 95   # chừa đệm cho lệnh kiểm

CACHE_ROOT = pathlib.Path(os.environ.get('MARKET_CACHE', pathlib.Path.home() / 'market-cache'))


def today():
    return dt.date.today().isoformat()


def cache_dir(day=None):
    d = CACHE_ROOT / (day or today())
    d.mkdir(parents=True, exist_ok=True)
    return d


def latest_cache():
    days = sorted(p for p in CACHE_ROOT.glob('20??-??-??') if p.is_dir())
    if not days:
        raise SystemExit('chưa có ~/market-cache/<ngày>/ — chạy discover.py / pull.py trước')
    return days[-1]


def _quota_file():
    return cache_dir() / 'quota.jsonl'


def quota_used():
    units = searches = 0
    f = _quota_file()
    if f.exists():
        for line in f.read_text().splitlines():
            r = json.loads(line)
            units += r['units']
            searches += r['method'] == 'search'
    return units, searches


def yt(method, **params):
    """Một lượt gọi API (GET). Ghi đơn vị vào quota.jsonl của ngày; từ chối khi sắp chạm hạn mức."""
    units, searches = quota_used()
    cost = COST.get(method, 1)
    if units + cost > SAFE_UNITS or (method == 'search' and searches >= SAFE_SEARCH):
        raise RuntimeError(f'hạn mức: đã dùng {units} đơn vị, {searches} search — dừng trước khi vượt')
    url = API + method + '?' + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = json.load(r)
            break
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:400]
            if e.code in (500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            with _quota_file().open('a') as f:   # lượt lỗi vẫn tính đơn vị
                f.write(json.dumps({'t': time.time(), 'method': method, 'units': cost, 'http': e.code}) + '\n')
            raise RuntimeError(f'{method} HTTP {e.code}: {body}')
    with _quota_file().open('a') as f:
        f.write(json.dumps({'t': time.time(), 'method': method, 'units': cost, 'http': 200}) + '\n')
    return data


def iso_dur(s):
    """PT1H2M3S → giây."""
    import re
    m = re.fullmatch(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', s or '')
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def videos(ids):
    """videos.list 50 id/lượt → dict id → item (snippet, contentDetails, statistics, liveStreamingDetails)."""
    out = {}
    ids = list(dict.fromkeys(ids))
    for i in range(0, len(ids), 50):
        r = yt('videos', part='snippet,contentDetails,statistics,liveStreamingDetails', id=','.join(ids[i:i + 50]), maxResults=50)
        for it in r.get('items', []):
            out[it['id']] = it
    return out


def channels(ids):
    out = {}
    ids = list(dict.fromkeys(ids))
    for i in range(0, len(ids), 50):
        r = yt('channels', part='snippet,statistics,contentDetails,brandingSettings', id=','.join(ids[i:i + 50]), maxResults=50)
        for it in r.get('items', []):
            out[it['id']] = it
    return out


def is_long(item, min_s=181):
    """Video dài: > 3 phút (Shorts tối đa 3 phút) và không phải live/premiere đã phát trực tiếp."""
    if item.get('snippet', {}).get('liveBroadcastContent') in ('live', 'upcoming'):
        return False
    if 'liveStreamingDetails' in item and item['liveStreamingDetails'].get('actualStartTime'):
        return False
    return iso_dur(item.get('contentDetails', {}).get('duration')) >= min_s


def jdump(obj, path):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1))


def jload(path):
    return json.loads(pathlib.Path(path).read_text())


def label(x, lo, hi):
    """Nhãn định tính cho repo (không ghi số thô): cao / vừa / thấp."""
    return 'cao' if x >= hi else 'vừa' if x >= lo else 'thấp'

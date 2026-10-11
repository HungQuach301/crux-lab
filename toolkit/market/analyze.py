#!/usr/bin/env python3
"""Phân tích thị trường (Phiên Thị trường, bước 4–5). Đọc ~/market-cache/<ngày>/ (discover/, pull/), ghi analysis/ cùng chỗ (ngoài git).
Mọi chỉ số ở đây là TỰ TÍNH, KHÔNG PHẢI CHỈ SỐ YOUTUBE. Repo chỉ nhận nhãn (cao/vừa/thấp) và kết luận định tính.

  python3 toolkit/market/analyze.py tag        # gắn đề tài bằng embeddings (chỉ nhận cặp khớp cao)
  python3 toolkit/market/analyze.py outliers   # hệ số vượt trội, lượt xem/ngày, cờ thời sự
  python3 toolkit/market/analyze.py comments   # 30–50 video, 50 bình luận/video (relevance), Haiku lọc + trọng số
  python3 toolkit/market/analyze.py packaging  # mẫu đóng gói: vượt trội vs thường
  python3 toolkit/market/analyze.py thumbs     # top 30 thumbnail, Sonnet xem URL (không lưu ảnh)
  python3 toolkit/market/analyze.py gap        # video đầu bảng mỗi đề tài có dùng dữ liệu lịch sử thật không (Haiku)
  python3 toolkit/market/analyze.py profile    # hồ sơ cầu mỗi đề tài → analysis/profile.json (nhãn + định tính)

Định nghĩa (tự tính):
- hệ số vượt trội = lượt xem video / trung vị lượt xem các video dài khác của cùng kênh đăng trong ±90 ngày; chỉ video ≥ 30 ngày
  tuổi, cần ≥ 5 video so sánh. Cờ ≥ 3×, ≥ 5× (cần thêm ≥ 10.000 lượt xem). Chỉ kênh giữ sau phân loại (kept_channels).
- lượt xem/ngày = lượt xem / số ngày từ lúc đăng.
- cờ thời sự = (a) tiêu đề có từ khoá sự kiện, hoặc (b) ≥ 3 kênh khác nhau có video vượt trội ≥ 3× cùng đề tài trong 21 ngày.
- gắn đề tài: cosine(embedding tiêu đề + 300 ký tự mô tả, embedding đề tài) ≥ NGƯỠNG và hơn đề tài thứ hai ≥ BIÊN.
"""
import datetime as dt, json, math, os, pathlib, re, statistics as stx, sys, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import yt, cache_dir, latest_cache, jdump, jload, quota_used, label

HERE = pathlib.Path(__file__).parent
TOPICS = jload(HERE / 'topics.json')['topics']
SIM_MIN, SIM_MARGIN = 0.55, 0.04
FLOOR = 10_000   # cờ vượt trội cần ≥ 10.000 lượt xem: kênh tí hon có trung vị vài chục lượt, hệ số vô nghĩa
NOW = dt.datetime.now(dt.timezone.utc)
EVENT = re.compile(r'\b(new law|just passed|big beautiful bill|obbb|no tax on (tips|overtime)|tariff|shutdown|fed (cut|hike)|'
                   r'rate cut|breaking|this week|announced|trump|biden|election|2026 changes|new rules?)\b', re.I)


def day():
    return pathlib.Path(os.environ.get('MARKET_DAY') or latest_cache())


def age_days(iso):
    return max((NOW - dt.datetime.fromisoformat(iso.replace('Z', '+00:00'))).days, 1)


def all_videos():
    """Video dài từ pull/ (kênh ứng viên) + discover/videos.json (kết quả search), khử trùng theo id."""
    out = {}
    for f in (day() / 'pull').glob('*.json'):
        p = jload(f)
        for v in p['videos']:
            out[v['id']] = dict(v, channelId=p['channel']['id'], channelTitle=p['channel']['title'], subs=p['channel']['subs'], src='pull')
    dv = jload(day() / 'discover' / 'videos.json')
    from common import is_long, iso_dur
    for v in dv.values():
        if v['id'] in out or not is_long(v):
            continue
        s, st = v['snippet'], v.get('statistics', {})
        out[v['id']] = {'id': v['id'], 'title': s['title'], 'publishedAt': s['publishedAt'], 'duration': iso_dur(v['contentDetails']['duration']),
                        'views': int(st.get('viewCount', 0)), 'likes': int(st.get('likeCount', 0)), 'comments': int(st.get('commentCount', 0)),
                        'description': s.get('description', '')[:1500], 'channelId': s['channelId'], 'channelTitle': s['channelTitle'],
                        'thumb': (s.get('thumbnails', {}).get('high') or {}).get('url'), 'src': 'search',
                        'lang': s.get('defaultAudioLanguage') or s.get('defaultLanguage')}
    return out


SEEDS = {'UCKhpM-cu2Cod-GyG6KngNYg', 'UCZJnbHQTYBy1I8GpHlsAUMg'}


def kept_channels():
    """Kênh giữ sau phân loại (discover.py classify): có vòng tròn, không lý do loại; hạt giống chủ dự án luôn giữ."""
    cl = jload(day() / 'discover' / 'classified.json')
    ok = lambda x: (x.get('circle') in ('direct', 'adjacent') and not x.get('exclude')) or \
        (x.get('circle') == 'form' and set(x.get('exclude', [])) <= {'off_topic'})
    return {c for c, x in cl.items() if (ok(x) and x.get('long_videos_last_90d', 0) > 0) or c in SEEDS}


# ---------- embeddings ----------
def embed(texts):
    """OpenAI text-embedding-3-small. Khoá: EMBEDDINGS_API_KEY nếu có; không thì proxy môi trường gắn khoá cho api.openai.com."""
    hdr = {'content-type': 'application/json'}
    if os.environ.get('EMBEDDINGS_API_KEY'):
        hdr['authorization'] = 'Bearer ' + os.environ['EMBEDDINGS_API_KEY']
    out = []
    for i in range(0, len(texts), 500):
        body = json.dumps({'model': 'text-embedding-3-small', 'input': texts[i:i + 500]}).encode()
        with urllib.request.urlopen(urllib.request.Request('https://api.openai.com/v1/embeddings', body, hdr), timeout=120) as r:
            d = json.load(r)
        out += [x['embedding'] for x in d['data']]
        with (cache_dir() / 'ai-ledger.jsonl').open('a') as f:   # 0,02 USD / triệu token
            f.write(json.dumps({'task': 'embeddings', 'via': 'openai', 'model': 'text-embedding-3-small',
                                'cost_usd': d['usage']['total_tokens'] * 0.02 / 1e6, 'tokens': {'emb': d['usage']}}) + '\n')
    return out


def cos(a, b):
    return sum(x * y for x, y in zip(a, b)) / math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))


def cmd_tag():
    vids = all_videos()
    ids = sorted(vids)
    tdesc = [f"{t['title']}. Viewers ask: {'; '.join(t['q'])}." for t in TOPICS]
    te = embed(tdesc)
    ve = embed([(vids[i]['title'] + '. ' + vids[i]['description'][:300]).replace('\n', ' ') for i in ids])
    tags = {}
    for i, e in zip(ids, ve):
        sims = sorted(((cos(e, t), TOPICS[k]['id']) for k, t in enumerate(te)), reverse=True)
        top, second = sims[0], sims[1]
        tags[i] = {'best': top[1], 'sim': round(top[0], 3), 'margin': round(top[0] - second[0], 3),
                   'topic': top[1] if top[0] >= SIM_MIN and top[0] - second[0] >= SIM_MARGIN else None}
    jdump(tags, day() / 'analysis' / 'tags.json')
    n = sum(1 for t in tags.values() if t['topic'])
    print(f'{n}/{len(tags)} video gắn đề tài (cosine ≥ {SIM_MIN}, biên ≥ {SIM_MARGIN})')


# ---------- outliers ----------
def cmd_outliers():
    vids = all_videos()
    tags = jload(day() / 'analysis' / 'tags.json')
    keep = kept_channels()
    by_ch = {}
    for v in vids.values():
        if v['src'] == 'pull' and v['channelId'] in keep:
            by_ch.setdefault(v['channelId'], []).append(v)
    res = {}
    for c, vs in by_ch.items():
        for v in vs:
            v['vpd'] = v['views'] / age_days(v['publishedAt'])
            if age_days(v['publishedAt']) < 30:
                continue
            t0 = dt.datetime.fromisoformat(v['publishedAt'].replace('Z', '+00:00'))
            peers = [w['views'] for w in vs if w['id'] != v['id'] and age_days(w['publishedAt']) >= 30 and
                     abs((dt.datetime.fromisoformat(w['publishedAt'].replace('Z', '+00:00')) - t0).days) <= 90]
            if len(peers) < 5:
                continue
            med = stx.median(peers)
            f = v['views'] / med if med else 0
            res[v['id']] = {'channelId': c, 'channelTitle': v['channelTitle'], 'title': v['title'], 'publishedAt': v['publishedAt'],
                            'duration': v['duration'], 'views': v['views'], 'vpd': round(v['vpd'], 1), 'factor': round(f, 2),
                            'flag3': f >= 3 and v['views'] >= FLOOR, 'flag5': f >= 5 and v['views'] >= FLOOR, 'topic': (tags.get(v['id']) or {}).get('topic'),
                            'event_kw': bool(EVENT.search(v['title']))}
    # cờ thời sự (b): ≥ 3 kênh có vượt trội ≥ 3× cùng đề tài trong 21 ngày
    hot = [r for r in res.values() if r['flag3'] and r['topic']]
    for r in res.values():
        t0 = dt.datetime.fromisoformat(r['publishedAt'].replace('Z', '+00:00'))
        near = {h['channelId'] for h in hot if h['topic'] == r['topic'] and r['topic'] and
                abs((dt.datetime.fromisoformat(h['publishedAt'].replace('Z', '+00:00')) - t0).days) <= 21}
        r['cluster'] = len(near) >= 3
        r['topical'] = r['event_kw'] or r['cluster']
    jdump(res, day() / 'analysis' / 'outliers.json')
    print(len(res), 'video có hệ số;', sum(r['flag3'] for r in res.values()), '≥3×;', sum(r['flag5'] for r in res.values()), '≥5×;',
          sum(r['topical'] for r in res.values()), 'cờ thời sự')


# ---------- comments ----------
COMMENT_PROMPT = '''You read YouTube comments under US personal-finance videos. Keep only comments that are one of:
"question" (asks something), "situation" (describes the commenter's own financial circumstances), "rebuttal" (pushes back on the video's claim or math),
"request" (asks for a future video/topic). Drop spam, ads, self-promotion, generic praise, jokes without content.
For each KEPT comment return {"i": index, "type": one of the four, "gist": a PARAPHRASE in your own words, max 20 words, no names, no quotes}.
Return a JSON array only.

VIDEO TOPIC: %s
COMMENTS (index, likes, replies, text):
%s'''


def pick_comment_videos(n_max=48):
    """Vượt trội gắn đề tài (không thời sự) + đối thủ theo tập: mỗi đề tài 2 video gắn đề tài nhiều lượt xem nhất."""
    out = jload(day() / 'analysis' / 'outliers.json')
    tags = jload(day() / 'analysis' / 'tags.json')
    vids = all_videos()
    pick = {}
    for vid, r in sorted(out.items(), key=lambda kv: -kv[1]['factor']):
        if r['flag3'] and r['topic'] and not r['topical'] and len(pick) < 24:
            pick[vid] = r['topic']
    for t in TOPICS:
        tv = sorted((v for v in vids.values() if (tags.get(v['id']) or {}).get('topic') == t['id'] and v.get('comments', 0) > 20),
                    key=lambda v: -v['views'])
        for v in tv[:2]:
            pick.setdefault(v['id'], t['id'])
    return dict(list(pick.items())[:n_max])


def cmd_comments():
    from ai import ask
    pick = pick_comment_videos()
    vids = all_videos()
    tt = {t['id']: t['title'] for t in TOPICS}
    od = day() / 'analysis' / 'comments'
    od.mkdir(parents=True, exist_ok=True)
    for vid, topic in pick.items():
        f = od / f'{vid}.json'
        if f.exists():
            continue
        try:
            r = yt('commentThreads', part='snippet', videoId=vid, order='relevance', maxResults=50, textFormat='plainText')
        except RuntimeError as e:     # bình luận tắt
            jdump({'video': vid, 'topic': topic, 'error': str(e)[:120], 'kept': []}, f)
            continue
        cm = [{'likes': it['snippet']['topLevelComment']['snippet'].get('likeCount', 0),
               'replies': it['snippet'].get('totalReplyCount', 0),
               'text': it['snippet']['topLevelComment']['snippet']['textDisplay'][:600]} for it in r.get('items', [])]
        if not cm:
            jdump({'video': vid, 'topic': topic, 'kept': []}, f)
            continue
        lines = '\n'.join(f"{i}\t{c['likes']}\t{c['replies']}\t{c['text'].replace(chr(10), ' ')}" for i, c in enumerate(cm))
        kept = ask(COMMENT_PROMPT % (tt.get(topic, topic) + ' / video title: ' + vids.get(vid, {}).get('title', ''), lines), task='comments')
        for k in kept:
            c = cm[k['i']] if 0 <= k.get('i', -1) < len(cm) else {'likes': 0, 'replies': 0}
            k['weight'] = 1 + c['likes'] + 2 * c['replies']    # trọng số tự tính: 1 + like + 2 × phản hồi
        jdump({'video': vid, 'topic': topic, 'n': len(cm), 'kept': kept}, f)   # chỉ giữ ý diễn đạt lại, không lưu nguyên văn
        print(vid, topic, len(cm), '→', len(kept), quota_used())


# ---------- packaging ----------
def feats(v):
    t = v['title']
    d = dt.datetime.fromisoformat(v['publishedAt'].replace('Z', '+00:00'))
    return {'len': len(t), 'num': bool(re.search(r'\d', t)), 'dollar': '$' in t, 'question': '?' in t,
            'you': bool(re.search(r'\byou(r)?\b', t, re.I)), 'year': bool(re.search(r'\b20[2-3]\d\b', t)),
            'caps': bool(re.search(r'\b[A-Z]{3,}\b', t)), 'vs': bool(re.search(r'\bvs\.?\b', t, re.I)),
            'colon_dash': bool(re.search(r'[:—–|-]', t)), 'dur_min': v['duration'] / 60, 'chapters': bool(v.get('chapters')),
            'weekday': d.strftime('%a'), 'hour_utc': d.hour}


def cmd_packaging():
    out = jload(day() / 'analysis' / 'outliers.json')
    vids = all_videos()
    groups = {'outlier': [], 'normal': []}
    for vid, r in out.items():
        if r['topical']:
            continue
        g = 'outlier' if r['flag3'] else 'normal' if r['factor'] < 1.5 else None
        if g:
            groups[g].append(dict(feats(vids[vid]), factor=r['factor']))
    summ = {}
    for g, xs in groups.items():
        if not xs:
            continue
        s = {'n': len(xs), 'title_len_median': stx.median(x['len'] for x in xs), 'dur_min_median': round(stx.median(x['dur_min'] for x in xs), 1),
             'dur_min_p25': round(sorted(x['dur_min'] for x in xs)[len(xs) // 4], 1),
             'dur_min_p75': round(sorted(x['dur_min'] for x in xs)[3 * len(xs) // 4], 1)}
        for k in ('num', 'dollar', 'question', 'you', 'year', 'caps', 'vs', 'colon_dash', 'chapters'):
            s[k] = round(sum(x[k] for x in xs) / len(xs), 3)
        wd = {}
        for x in xs:
            wd[x['weekday']] = wd.get(x['weekday'], 0) + 1
        s['weekday'] = {k: round(v / len(xs), 3) for k, v in sorted(wd.items(), key=lambda kv: -kv[1])}
        hr = {}
        for x in xs:
            b = f"{(x['hour_utc'] // 4) * 4:02d}-{(x['hour_utc'] // 4) * 4 + 4:02d}"
            hr[b] = hr.get(b, 0) + 1
        s['hour_utc'] = {k: round(v / len(xs), 3) for k, v in sorted(hr.items())}
        summ[g] = s
    # dải thời lượng của vượt trội theo đề tài
    by_t = {}
    for vid, r in out.items():
        if r['flag3'] and r['topic'] and not r['topical']:
            by_t.setdefault(r['topic'], []).append(r['duration'] / 60)
    summ['dur_by_topic'] = {t: [round(min(x), 1), round(stx.median(x), 1), round(max(x), 1), len(x)] for t, x in by_t.items()}
    jdump(summ, day() / 'analysis' / 'packaging.json')
    print(json.dumps({g: {k: v for k, v in s.items() if k not in ('weekday', 'hour_utc')} for g, s in summ.items() if g != 'dur_by_topic'}, indent=1))


# ---------- thumbnails ----------
THUMB_PROMPT = '''These are %d YouTube thumbnails (in order) from US personal-finance videos that strongly outperformed their channel's usual views.
For each, return {"i": index (0-based), "face": "none"|"small"|"large" (human face size), "face_emotion": short word or null,
"chart": true/false (any chart/graph/arrow-as-data), "words": number of words of overlaid text, "number_or_dollar": true/false,
"colors": up to 3 dominant colors as plain words, "contrast": "high"|"medium"|"low", "composition": one short phrase (e.g. "split before/after",
"person + big number", "object close-up"), "style": "photo"|"illustration/3D"|"screenshot"|"mixed"}.
Then add a final object {"summary": "3-5 sentences on recurring winning patterns"}. Return a JSON array only.'''


def cmd_thumbs(n=30):
    from ai import look
    out = jload(day() / 'analysis' / 'outliers.json')
    vids = all_videos()
    top = [vid for vid, r in sorted(out.items(), key=lambda kv: -kv[1]['factor']) if r['flag3'] and not r['topical'] and vids[vid].get('thumb')][:n]
    res = []
    for i in range(0, len(top), 10):
        chunk = top[i:i + 10]
        r = look([vids[v]['thumb'] for v in chunk], THUMB_PROMPT % len(chunk))
        for x in r:
            if 'i' in x and 0 <= x['i'] < len(chunk):
                x['video'] = chunk[x['i']]
            res.append(x)
    jdump(res, day() / 'analysis' / 'thumbs.json')     # chỉ mô tả do model viết; không lưu ảnh
    print(len(top), 'thumbnail;', [x['summary'] for x in res if 'summary' in x])


# ---------- gap ----------
GAP_PROMPT = '''For each US personal-finance YouTube video below (title + description excerpt), judge the method it uses to answer its question.
Return {"id": ..., "method": "real_history" (replays actual historical data series — real past rates/prices/returns over real dates),
"fixed_assumption" (illustrative math with constant assumed returns/rates), "opinion" (advice/talk without calculation), "news"},
"data_note": one short English phrase}. Return a JSON array only.

VIDEOS:
%s'''


def cmd_gap():
    from ai import ask
    tags = jload(day() / 'analysis' / 'tags.json')
    vids = all_videos()
    res = {}
    for t in TOPICS:
        tv = sorted((v for v in vids.values() if (tags.get(v['id']) or {}).get('topic') == t['id']), key=lambda v: -v['views'])[:6]
        if not tv:
            res[t['id']] = []
            continue
        rows = [{'id': v['id'], 'title': v['title'], 'description': v['description'][:700]} for v in tv]
        r = ask(GAP_PROMPT % json.dumps(rows, ensure_ascii=False, indent=1), task='gap')
        res[t['id']] = [dict(x, channelTitle=vids[x['id']]['channelTitle'], title=vids[x['id']]['title'],
                             duration_min=round(vids[x['id']]['duration'] / 60, 1)) for x in r if x.get('id') in vids]
    jdump(res, day() / 'analysis' / 'gap.json')
    print({k: [x['method'] for x in v] for k, v in res.items()})


# ---------- profile ----------
QUESTIONS_PROMPT = '''Below are paraphrased audience comments (type, weight, gist) from YouTube videos about: %s.
Write the 5 most important audience questions this topic must answer, ranked by total weight and frequency, plus 3 typical personal situations
(composite, no real names, US context), plus up to 3 competitor weaknesses viewers complain about, plus any requested topics for new videos.
Return JSON only: {"questions": [{"q": "...", "weight": "high"|"medium"|"low"}], "situations": ["..."], "weaknesses": ["..."], "requests": ["..."]}.
If there are few comments, infer conservatively from the topic and say so in a field "note".

COMMENTS:
%s'''


def cmd_profile():
    from ai import ask
    tags = jload(day() / 'analysis' / 'tags.json')
    out = jload(day() / 'analysis' / 'outliers.json')
    gap = jload(day() / 'analysis' / 'gap.json') if (day() / 'analysis' / 'gap.json').exists() else {}
    vids = all_videos()
    cm = {}
    for f in (day() / 'analysis' / 'comments').glob('*.json'):
        c = jload(f)
        for k in c['kept']:
            cm.setdefault(c['topic'], []).append(k)
    # cầu (tự tính): trung vị lượt xem/ngày của 10 video gắn đề tài nhiều lượt xem/ngày nhất, đăng ≤ 24 tháng, bỏ video thời sự
    dem = {}
    for t in TOPICS:
        tv = [v for v in vids.values() if (tags.get(v['id']) or {}).get('topic') == t['id'] and not EVENT.search(v['title'])
              and not (out.get(v['id']) or {}).get('topical') and age_days(v['publishedAt']) >= 14]
        vpd = sorted((v['views'] / age_days(v['publishedAt']) for v in tv), reverse=True)[:10]
        n_out = sum(1 for v in tv if (out.get(v['id']) or {}).get('flag3'))
        dem[t['id']] = {'vpd_top10_median': stx.median(vpd) if vpd else 0, 'n_tagged': len(tv), 'n_outliers': n_out}
    vals = sorted(d['vpd_top10_median'] for d in dem.values())
    lo, hi = vals[len(vals) // 3], vals[2 * len(vals) // 3]
    prof = {}
    for t in TOPICS:
        d = dem[t['id']]
        g = gap.get(t['id'], [])
        real = sum(1 for x in g if x.get('method') == 'real_history')
        gl = 'chưa có dữ liệu' if not g else 'cao' if real == 0 else 'vừa' if real <= 1 else 'thấp'
        comments = cm.get(t['id'], [])
        lines = '\n'.join(f"{k['type']}\t{k['weight']}\t{k['gist']}" for k in sorted(comments, key=lambda k: -k['weight'])[:120])
        q = ask(QUESTIONS_PROMPT % (t['title'] + ' (viewers search: ' + '; '.join(t['q']) + ')', lines or '(none)'), task='profile')
        comp = sorted((v for v in vids.values() if (tags.get(v['id']) or {}).get('topic') == t['id']), key=lambda v: -v['views'])[:5]
        outl = sorted((r for r in out.values() if r['topic'] == t['id'] and r['flag3'] and not r['topical']), key=lambda r: -r['factor'])[:3]
        durs = [v['duration'] / 60 for v in comp]
        prof[t['id']] = {'title': t['title'], 'demand': label(d['vpd_top10_median'], lo, hi) if d['n_tagged'] >= 3 else 'thấp (ít video)',
                         'n_tagged_label': label(d['n_tagged'], 8, 25), 'gap': gl, 'gap_methods': [x.get('method') for x in g],
                         'questions': q, 'n_comments_kept': len(comments),
                         'competitors': [{'channel': v['channelTitle'], 'title': v['title'], 'id': v['id'], 'min': round(v['duration'] / 60, 1)} for v in comp],
                         'outliers': [{'channel': r['channelTitle'], 'title': r['title'], 'id': vid_of(out, r), 'min': round(r['duration'] / 60, 1),
                                       'band': '≥ 5×' if r['flag5'] else '≥ 3×'} for r in outl],
                         'dur_range_min': [round(min(durs), 1), round(max(durs), 1)] if durs else None,
                         'title_patterns': [feats(v) for v in comp[:3]]}
    jdump({'cutoffs_vpd': [lo, hi], 'demand_raw': dem, 'profiles': prof}, day() / 'analysis' / 'profile.json')
    print({k: (v['demand'], v['gap'], v['n_comments_kept']) for k, v in prof.items()})


def vid_of(out, r):
    for k, v in out.items():
        if v is r:
            return k


if __name__ == '__main__':
    {'tag': cmd_tag, 'outliers': cmd_outliers, 'comments': cmd_comments, 'packaging': cmd_packaging,
     'thumbs': cmd_thumbs, 'gap': cmd_gap, 'profile': cmd_profile}[sys.argv[1]]()

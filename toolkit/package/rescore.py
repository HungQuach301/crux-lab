#!/usr/bin/env python3
"""P4: chấm lại 3 tiêu đề + 3 thumbnail theo (1) mức gần mẫu ĐANG LÊN 7 ngày của đề tài và (2) khớp nội dung video; chọn mặc định + thứ tự
Test & Compare; gợi ý giờ đăng (D-012 mục 3, tổng kết Tập 6 §4d). Cùng lượt kiểm vật thể trên MỌI ảnh cuối (kể cả bản ChatGPT): ảnh có đúng vật
thể/nhân vật của video không (vd crates, không phải baskets; thế giới 3D low-poly, không ảnh chụp), mỗi số trên ảnh có claim (package_check).

  python3 toolkit/package/rescore.py --trend <anchors trend.json> --text <text.json> --summary "<1–2 câu nội dung video>" \
      --objects "crates (10 per row), a paper check, faceless low-poly figures" --banned "baskets,groceries,photos" \
      --thumb a.png --thumb b.png … [--title "…" …] [--out rescore.json]
Sonnet (Messages API, khoá Console, ảnh base64 thu về 640×360 + bản 168×94). Mẫu đang lên chỉ là gợi ý: khớp nội dung đứng trước,
không đổi lấy mẫu có mặt người/mũi tên dự báo/số tiền không claim (gen CHARTER §4).
"""
import base64, io, json, os, pathlib, sys, urllib.request
from PIL import Image

MODEL = 'claude-sonnet-5-5'


def b64(path, size):
    im = Image.open(path).convert('RGB').resize(size); buf = io.BytesIO(); im.save(buf, 'PNG')
    return {'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/png', 'data': base64.b64encode(buf.getvalue()).decode()}}


def call(content):
    body = json.dumps({'model': MODEL, 'max_tokens': 3000, 'messages': [{'role': 'user', 'content': content}]}).encode()
    req = urllib.request.Request('https://api.anthropic.com/v1/messages', body, {'x-api-key': os.environ['CONSOLE_API_KEY'],
                                 'anthropic-version': '2023-06-01', 'content-type': 'application/json'})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    t = ''.join(c.get('text', '') for c in d['content'])
    u = d['usage']
    return json.loads(t[t.find('{'): t.rfind('}') + 1]), (u['input_tokens'] * 3 + u['output_tokens'] * 15) / 1e6


def main(a):
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d   # noqa: E731
    trend = json.loads(pathlib.Path(opt('--trend')).read_text()) if opt('--trend') else {}
    titles = [t['title'] for t in json.loads(pathlib.Path(opt('--text')).read_text()).get('titles', [])] if opt('--text') else []
    titles += [a[i + 1] for i, x in enumerate(a) if x == '--title']
    thumbs = [a[i + 1] for i, x in enumerate(a) if x == '--thumb']
    content = []
    for i, t in enumerate(thumbs):
        content += [{'type': 'text', 'text': f'Thumbnail T{i + 1} ({pathlib.Path(t).name}), full and at phone size 168x94:'}, b64(t, (640, 360)), b64(t, (168, 94))]
    content.append({'type': 'text', 'text': f"""Video content: {opt('--summary')}
Objects and characters that ARE in the video: {opt('--objects')}. Words/things that are NOT in the video: {opt('--banned')}.
Rising patterns in this topic over the last 7 days (titles, thumbnails, keywords): {json.dumps(trend, ensure_ascii=False)}
Titles: {json.dumps(titles)}
Score each title and each thumbnail 1-5 on "trend" (closeness to the rising patterns that this channel may use: no faces, no prediction arrows,
no unsourced dollar amounts) and "match" (shows/says exactly what the video shows; any NOT-in-video object or a photo instead of a minimal 3D world
=> match <= 2). For thumbnails also "readable" (headline readable at 168x94) and "objects_seen" (what objects you see, plain words).
Return JSON {{"titles":[{{"i":1,"trend":n,"match":n,"note":"<=12 words"}}],"thumbs":[{{"i":1,"trend":n,"match":n,"readable":n,"objects_seen":"...","note":"<=12 words"}}],
"default_title":i,"default_thumb":i,"test_compare_order":[i,i,i],"why":"<=25 words"}}. Match outranks trend."""})
    r, cost = call(content)
    r['model'] = MODEL; r['cost_usd_est'] = round(cost, 4); r['titles_in'] = titles; r['thumbs_in'] = thumbs
    r['post_time'] = 'thứ Hai, 12–16 UTC (sáng giờ Mỹ) — tín hiệu yếu, market/REPORT.md §4'
    if opt('--out'): pathlib.Path(opt('--out')).write_text(json.dumps(r, ensure_ascii=False, indent=1))
    print(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1:])

# Việc AI của toolkit/market — headless, 0 agent con, ghi chi API (~/market-cache/<ngày>/ai-ledger.jsonl).
#  - chữ (phân loại kênh, bình luận): `claude -p` Haiku, chạy từ thư mục trống, không công cụ, ANTHROPIC_API_KEY="$CONSOLE_API_KEY".
#  - ảnh thumbnail: Messages API với ảnh dạng URL (Sonnet đọc thẳng từ i.ytimg.com; không tải, không lưu ảnh).
import json, os, re, subprocess, tempfile, time, urllib.request
from common import cache_dir

HAIKU, SONNET = 'claude-haiku-4-5', 'claude-sonnet-4-5'


def _ledger(rec):
    with (cache_dir() / 'ai-ledger.jsonl').open('a') as f:
        f.write(json.dumps(rec) + '\n')


def _json(text):
    m = re.search(r'```(?:json)?\s*(.*?)```', text, re.S)
    text = m.group(1) if m else text
    i = min([k for k in (text.find('['), text.find('{')) if k >= 0] or [0])
    return json.loads(text[i:])


def ask(prompt, model='haiku', task=''):
    """claude -p headless; trả JSON đã parse (đầu bài phải yêu cầu JSON)."""
    env = dict(os.environ, ANTHROPIC_API_KEY=os.environ.get('CONSOLE_API_KEY', ''))
    args = ['claude', '-p', '--model', model, '--output-format', 'json', '--no-session-persistence', '--tools', '']
    for attempt in range(3):
        p = subprocess.run(args, input=prompt, capture_output=True, text=True, env=env, cwd=tempfile.mkdtemp(), timeout=600)
        try:
            d = json.loads(p.stdout)
            tok = {k: {'input': v['inputTokens'], 'cache_write': v['cacheCreationInputTokens'],
                       'cache_read': v['cacheReadInputTokens'], 'output': v['outputTokens']} for k, v in d.get('modelUsage', {}).items()}
            _ledger({'t': time.time(), 'task': task, 'via': 'claude -p', 'model': model, 'cost_usd': d.get('total_cost_usd'), 'tokens': tok})
            return _json(d.get('result', ''))
        except (json.JSONDecodeError, ValueError, KeyError):
            if attempt == 2:
                raise RuntimeError(f'claude -p lỗi: {p.stderr[:300]} {p.stdout[:300]}')
            time.sleep(3)


PRICE = {SONNET: (3.0, 15.0)}   # USD / triệu token (vào, ra)


def look(urls, prompt, model=SONNET, task='thumbnail'):
    """Sonnet xem ảnh bằng URL (không lưu ảnh). Trả JSON đã parse."""
    content = [{'type': 'image', 'source': {'type': 'url', 'url': u}} for u in urls] + [{'type': 'text', 'text': prompt}]
    body = json.dumps({'model': model, 'max_tokens': 4000, 'messages': [{'role': 'user', 'content': content}]}).encode()
    req = urllib.request.Request('https://api.anthropic.com/v1/messages', body, {
        'x-api-key': os.environ['CONSOLE_API_KEY'], 'anthropic-version': '2023-06-01', 'content-type': 'application/json'})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    u = d['usage']
    pi, po = PRICE.get(model, (3.0, 15.0))
    cost = (u['input_tokens'] * pi + u['output_tokens'] * po) / 1e6
    _ledger({'t': time.time(), 'task': task, 'via': 'messages api (url image)', 'model': model, 'cost_usd': cost,
             'tokens': {model: {'input': u['input_tokens'], 'cache_write': u.get('cache_creation_input_tokens', 0),
                                'cache_read': u.get('cache_read_input_tokens', 0), 'output': u['output_tokens']}}})
    return _json(''.join(c.get('text', '') for c in d['content']))


def spend():
    f = cache_dir() / 'ai-ledger.jsonl'
    tot, by = 0.0, {}
    if f.exists():
        for line in f.read_text().splitlines():
            r = json.loads(line)
            tot += r['cost_usd'] or 0
            by[r['task']] = by.get(r['task'], 0) + (r['cost_usd'] or 0)
    return round(tot, 4), {k: round(v, 4) for k, v in by.items()}

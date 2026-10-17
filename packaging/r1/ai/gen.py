#!/usr/bin/env python3
"""Ảnh bìa R1-AI · bước 1: mô hình ảnh OpenAI vẽ PHẦN HÌNH (không chữ). Khoá do proxy môi trường gắn (api.openai.com) — không đọc, không in, không ghi khoá.
  python3 packaging/r1/ai/gen.py <id> [<id> …]     (id trong prompts.json) → ai/raw/<id>.png + ai/ledger.jsonl (model, prompt, ngày, usage, chi thật)
Chi thật = usage API trả × bảng giá gpt-image-1 (USD/1M token: text in 5, image in 10, image out 40). Dừng khi tổng chi vượt CAP."""
import base64, datetime, json, pathlib, sys, urllib.error, urllib.request
H = pathlib.Path(__file__).resolve().parent
CAP = 3.00
PRICE = {'text_in': 5e-6, 'image_in': 10e-6, 'out': 40e-6}
P = json.loads((H / 'prompts.json').read_text())
LEDGER = H / 'ledger.jsonl'


def spent():
    return sum(json.loads(l)['cost_usd'] for l in LEDGER.read_text().splitlines() if l.strip()) if LEDGER.exists() else 0.0


def cost(u):
    d = u.get('input_tokens_details', {})
    return round(d.get('text_tokens', u.get('input_tokens', 0)) * PRICE['text_in'] + d.get('image_tokens', 0) * PRICE['image_in']
                 + u.get('output_tokens', 0) * PRICE['out'], 4)


def gen(i):
    spec = P['items'][i]; prompt = P['style'] + ' SUBJECT: ' + spec['subject'] + ' ' + P['negative']
    body = json.dumps({'model': P['model'], 'prompt': prompt, 'size': '1536x1024', 'quality': spec.get('quality', P['quality']), 'n': 1}).encode()
    req = urllib.request.Request('https://api.openai.com/v1/images/generations', body, {'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'{i}: HTTP {e.code} {e.read().decode()[:300]}')
    (H / 'raw' / f'{i}.png').write_bytes(base64.b64decode(d['data'][0]['b64_json']))
    u = d.get('usage', {}); c = cost(u)
    rec = {'id': i, 'date': datetime.date.today().isoformat(), 'tool': 'OpenAI Images API (images/generations)', 'model': P['model'],
           'size': '1536x1024', 'quality': spec.get('quality', P['quality']), 'prompt': prompt, 'usage': u, 'cost_usd': c}
    with LEDGER.open('a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return c


if __name__ == '__main__':
    for i in sys.argv[1:]:
        if spent() >= CAP:
            sys.exit(f'trần chi ảnh ${CAP} — dừng')
        c = gen(i); print(i, f'${c}', f'tổng ${spent():.3f}')

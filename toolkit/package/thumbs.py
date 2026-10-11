#!/usr/bin/env python3
"""Thumbnail LAI (D-012 mục 3, tổng kết Tập 6 §4c): khung thế giới 3D thật của tập → OpenAI image API (images/edits, giữ vật thể và nhân vật)
→ lớp chữ nhận diện kênh do MÁY vẽ (logo "M.", Inter Bold, vị trí chữ cố định, màu theo trụ — `playbook/packaging.md` §7). Chữ không do model vẽ
nên đúng từng ký tự và qua claim-risk như mọi khung.

  python3 toolkit/package/thumbs.py --frame <khung 1920×1080.png> --keep "<vật thể + nhân vật phải giữ, tiếng Anh>" --text "BIGGER CHECK|BUYS LESS?" \
      --pillar retire --out episodes/epNNN/out/package/hybrid-1.png [--character] [--no-api] [--quality high]
  --no-api   bỏ bước API (proxy/quyền chặn): lớp chữ đặt thẳng lên khung → dùng làm ảnh tham khảo cho đường ChatGPT thủ công (brief).
  Khung: `NODE_PATH=/opt/node-tools/node_modules node toolkit/factory/world/render_shots.js <đoạn> 1080 /tmp/x.mp4 --stills <giây> --stills-dir <thư mục>`.
Ghi <out>.json: chữ, claim do người gọi khai (--claims), prompt, model, chi ước, đường đi (api / no-api). Khoá: proxy gắn (api.openai.com),
không có trong phiên; lỗi 401/403 → in lý do, thoát 3 (chuyển đường ChatGPT).
"""
import argparse, base64, io, json, os, pathlib, sys, urllib.error, urllib.request
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOK = {'bg': '#0E1116', 'ink': '#F2F4F7', 'muted': '#9AA4B2', 'warn': '#F2B441'}
PILLAR = {'debt': '#F2B441', 'retire': '#3FBF7F', 'tax': '#4C8DFF'}   # trụ: vay và nợ · nghỉ hưu và đầu tư dài hạn · thuế và chính sách
PRICE = {'low': 0.016, 'medium': 0.063, 'high': 0.25}                  # USD/ảnh 1536×1024 gpt-image-1 (ước, bảng giá 2025; ghi số API trả nếu có)
W, H = 1280, 720


def font(px):
    ttf = pathlib.Path('/tmp/Inter-Bold.ttf')
    if not ttf.exists():   # woff2 của kênh → ttf (fonttools + brotli)
        from fontTools.ttLib import TTFont
        f = TTFont(ROOT / 'toolkit/render/fonts/inter-latin-700-normal.woff2'); f.flavor = None; f.save(ttf)
    return ImageFont.truetype(str(ttf), px)


PROMPT = ('Edit this frame from an explainer video into a YouTube thumbnail background. KEEP exactly these objects and characters, same shapes, '
          'same colors, same count, same arrangement: {keep}. Keep the same camera distance and framing; do not zoom in. Add dramatic soft key light, '
          'deeper shadows and gentle depth of field on a dark charcoal background (#0E1116). Style stays minimal low-poly 3D, matte, '
          'not photorealistic. Remove ALL text, labels, numbers, badges, captions and logos from the image. Do not add any new object, '
          'person, face, hand, money bill, coin, basket, arrow or chart. Characters stay faceless. Keep the top and bottom dark bands empty '
          '(they will be cropped). Leave the lower-left third darker and calm for a headline.')


def api_edit(frame, keep, quality):
    src = Image.open(frame).convert('RGB').resize((1536, 864))
    canvas = Image.new('RGB', (1536, 1024), TOK['bg']); canvas.paste(src, (0, 80))   # 16:9 trong khung 3:2, dải đệm trên/dưới
    buf = io.BytesIO(); canvas.save(buf, 'JPEG', quality=92)   # JPEG ≈ 0,3 MB: thân multipart lớn (PNG 1,5 MB) bị proxy trả 502
    bnd = 'crux' + os.urandom(8).hex()
    fields = {'model': 'gpt-image-1', 'prompt': PROMPT.format(keep=keep), 'size': '1536x1024', 'quality': quality, 'n': '1'}
    body = b''.join(f'--{bnd}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in fields.items())
    body += f'--{bnd}\r\nContent-Disposition: form-data; name="image"; filename="frame.jpg"\r\nContent-Type: image/jpeg\r\n\r\n'.encode() + buf.getvalue() + b'\r\n'
    body += f'--{bnd}--\r\n'.encode()
    req = urllib.request.Request('https://api.openai.com/v1/images/edits', body, {'Content-Type': f'multipart/form-data; boundary={bnd}'})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'OpenAI images/edits HTTP {e.code}: {e.read().decode()[:300]} → dùng --no-api (đường ChatGPT)' if e.code in (401, 403) else
                 f'OpenAI images/edits HTTP {e.code}: {e.read().decode()[:300]}')
    img = Image.open(io.BytesIO(base64.b64decode(d['data'][0]['b64_json']))).convert('RGB')
    return img.crop((0, 80, 1536, 944)).resize((W, H)), d.get('usage', {}), PROMPT.format(keep=keep)


def overlay(img, lines, pillar, character):
    """Bộ nhận diện kênh: logo "M." trên trái · chữ lớn ≤ 4 từ, dưới trái, Inter Bold, dòng cuối màu trụ · ILLUSTRATIVE trên phải khi có
    nhân vật · chân trang 'US only · history, not a forecast'. Vị trí cố định cho mọi tập."""
    img = img.convert('RGBA'); ov = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for y in range(H // 2, H):   # nền tối dần dưới chữ (đọc được ở 168×94)
        d.line([(0, y), (W, y)], fill=(14, 17, 22, int(200 * (y - H / 2) / (H / 2))))
    c = PILLAR[pillar]
    d.rounded_rectangle([32, 28, 112, 108], 14, fill=c); d.text((72, 70), 'M.', font=font(52), fill=TOK['bg'], anchor='mm')
    if character:
        f = font(26); tw = d.textlength('ILLUSTRATIVE', font=f)
        d.rounded_rectangle([W - 40 - tw - 28, 34, W - 40, 80], 10, fill=TOK['warn']); d.text((W - 40 - tw / 2 - 14, 57), 'ILLUSTRATIVE', font=f, fill=TOK['bg'], anchor='mm')
    px = 112 if max(len(l) for l in lines) <= 14 else 96
    y = H - 64 - px * 1.05 * len(lines)
    for i, l in enumerate(lines):
        d.text((48, y), l, font=font(px), fill=c if i == len(lines) - 1 else TOK['ink'], stroke_width=3, stroke_fill=TOK['bg'])
        y += px * 1.05
    d.text((W - 40, H - 30), 'US only · history, not a forecast', font=font(24), fill=TOK['muted'], anchor='rs')
    return Image.alpha_composite(img, ov).convert('RGB')


if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument('--frame', required=True); a.add_argument('--keep', default=''); a.add_argument('--text', required=True)
    a.add_argument('--pillar', choices=list(PILLAR), required=True); a.add_argument('--out', required=True)
    a.add_argument('--character', action='store_true', help='(mặc định đã bật; giữ để tương thích)'); a.add_argument('--no-character', action='store_true')
    a.add_argument('--ep', help='thư mục tập: kiểm claim-risk chữ trên ảnh với out/claims.json'); a.add_argument('--no-api', action='store_true')
    a.add_argument('--quality', default='medium', choices=list(PRICE)); a.add_argument('--claims', default='')
    o = a.parse_args()
    lines = o.text.split('|')
    if sum(len(l.split()) for l in lines) > 4:
        sys.exit('chữ lớn > 4 từ (packaging.md §7)')
    o.character = not o.no_character   # mặc định có nhãn ILLUSTRATIVE: quên cờ thì khung có nhân vật thiếu nhãn (REVIEWER T6)
    if o.ep:   # claim-risk chữ trên ảnh: S10 + mọi số có claim (dùng lại package_check, luật khoá chỉ đọc)
        sys.path.insert(0, str(ROOT / 'toolkit' / 'market'))
        from package_check import scan, bad_numbers, claim_number_set
        cl = json.loads((pathlib.Path(o.ep) / 'out' / 'claims.json').read_text()); cl = cl['claims'] if isinstance(cl, dict) else cl
        txt = ' '.join(lines); bad = [f'{k} "{m}"' for k, m in scan(txt)] + [f'số "{n}" không có claim' for n in bad_numbers(txt, claim_number_set(cl))]
        if bad:
            sys.exit('claim-risk chữ thumbnail: ' + '; '.join(bad))
    else:
        print('cảnh báo: không có --ep → chưa kiểm claim-risk chữ trên ảnh', file=sys.stderr)
    if o.no_api:
        base, usage, prompt, cost = Image.open(o.frame).convert('RGB').resize((W, H)), {}, None, 0
    else:
        base, usage, prompt = api_edit(o.frame, o.keep, o.quality); cost = PRICE[o.quality]
        base.save(pathlib.Path(o.out).with_name(pathlib.Path(o.out).stem + '-bg.jpg'), quality=88)
    overlay(base, lines, o.pillar, o.character).save(o.out)
    meta = {'texts': lines, 'claims': [c for c in o.claims.split(',') if c], 'frame': o.frame, 'path': 'no-api' if o.no_api else 'openai images/edits gpt-image-1',
            'quality': o.quality, 'prompt': prompt, 'usage': usage, 'cost_usd_est': cost, 'pillar': o.pillar, 'character': o.character}
    pathlib.Path(o.out).with_suffix('.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    print(o.out, meta['path'], f'≈ ${cost}')

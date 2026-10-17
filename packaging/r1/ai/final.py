#!/usr/bin/env python3
"""Ảnh bìa R1-AI · bước 3: ghép 6 phương án/tập bằng mã (compose.js), kiểm máy 168×94, claim-risk, tờ điểm.
  python3 packaging/r1/ai/final.py  → ai/cand/<id>.png (+ bare), ai/checks.json
Kiểm 168×94: chữ hoa ≥ 9 px (dòng ngữ cảnh và số) + tương phản WCAG ≥ 4,5:1 của chữ trắng và chữ màu trụ với nền sáng nhất 10 % sau hộp chữ (ảnh không chữ)."""
import json, os, pathlib, subprocess, sys
from PIL import Image
H = pathlib.Path(__file__).resolve().parent; ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'toolkit/package')); sys.path.insert(0, str(ROOT / 'toolkit/market')); sys.path.insert(0, str(H.parent))
import thumbs                                                        # noqa: E402  (font Inter Bold, màu kênh)
from package_check import scan, bad_numbers, claim_number_set        # noqa: E402
from make import contrast, hexrgb, lum                               # noqa: E402  (cùng phép đo R1)

TEXT = {   # dòng ngữ cảnh (đối lập/câu hỏi) + 1 số; claim ở cột cuối
 'ep005': ('ON PAPER?', '23 MONTHS', 'debt', 'medianB_months_to80 (23, "on paper")'),
 'ep008': ('WORST CASE', '-$82,385', 'debt', 'adv_2006-06 (June 2006, 10 năm)'),
 'ep009': ('COIN FLIP?', '49.5%', 'debt', 'share_buyer_ahead_stocks_10y (49.5) — đối chiếu sau M6'),
 'ep001': ('FEES BACK?', 'MONTH 30', 'debt', 'Nora break-even month 30 (counting balance)'),
 'ep002': ('WORST CASE', '+43%', 'debt', 'April 1977: 43% more interest'),
 'ep006': ('STILL BUYS', '80.7%', 'retire', 'typical rising check 80.7% after 20 raises'),
 'ep007': ('FALLBACK:', '$21,622', 'debt', 'stack_total 21,622'),
}
CLAIMS_ROOT = {'ep009': os.environ.get('EP9_ROOT', str(ROOT))}


def fit(text, px, maxw):
    while px > 40 and thumbs.font(px).getlength(text) > maxw:
        px -= 2
    return px


def subject_box(p):
    im = Image.open(p).convert('L').resize((384, 256)); w, h = im.size
    xs = [x for x in range(w // 3, w) for y in range(h) if im.getpixel((x, y)) > 110]
    ys = [y for x in range(w // 3, w) for y in range(h) if im.getpixel((x, y)) > 110]
    if not xs:
        return None
    xs.sort(); ys.sort(); k = 1536 / 384
    return [xs[len(xs) // 20] * k, ys[len(ys) // 20] * k, xs[-len(xs) // 20] * k, ys[-len(ys) // 20] * k]


def jobs():
    out = []
    for ep, (l1, num, pillar, _) in TEXT.items():
        l1s = fit(l1, 96, 700); ns = fit(num, 150, 620)
        for v in 'abcdef':
            bg = H / 'raw' / f'{ep}-{v}.jpg'   # PNG gốc lưu JPEG q90 khi commit (SHA PNG gốc: raw-sha256.json)
            if not bg.exists():
                continue
            box = subject_box(bg); arrow = None
            nx = 44 + thumbs.font(ns).getlength(num) + 34
            if box:
                s = 1280 / 1536; x1 = box[0] * s - 28; y1 = (box[1] + box[3]) / 2 * s - 80 * s
                if x1 - nx > 120:
                    arrow = [round(nx), 600, round(x1), round(min(max(y1, 300), 560))]
            out.append(dict(id=f'{ep}-{v}', bg=str(bg), out=str(H / 'cand' / f'{ep}-{v}.png'), outBare=str(H / 'cand' / f'{ep}-{v}-bare.png'),
                            cropY=80, l1=l1, l1Size=l1s, num=num, numSize=ns, pillar=pillar, arrow=arrow))
    return out


def check(j):
    bare = Image.open(j['outBare']).convert('RGB'); k = 168 / 1280
    yn = 652; y1 = round(652 - j['numSize'] * 0.8 - 22) if j['num'] else 652
    boxes = [(48, y1 - j['l1Size'] * 0.75, 48 + thumbs.font(j['l1Size']).getlength(j['l1']), y1),
             (44, yn - j['numSize'] * 0.75, 44 + thumbs.font(j['numSize']).getlength(j['num']), yn)]
    cs = []
    if not j['num']:   # chỉ một dòng chữ (vòng 2: "RENT = WASTED?")
        boxes = boxes[:1]
    for (x0, y0, x1, y1_), col in zip(boxes, [thumbs.TOK['ink'], thumbs.PILLAR[j['pillar']]]):
        reg = bare.crop((int(x0), int(y0), int(x1), int(y1_))).resize((max(1, int((x1 - x0) * k)), max(1, int((y1_ - y0) * k))))
        px = sorted(reg.get_flattened_data(), key=lum); cs.append(round(contrast(hexrgb(col), px[int(len(px) * 0.9)]), 2))
    caps = [round(j['l1Size'] * 0.727 * k, 1)] + ([round(j['numSize'] * 0.727 * k, 1)] if j['num'] else [])
    ep = j['id'][:5]
    cl = json.loads((pathlib.Path(CLAIMS_ROOT.get(ep, ROOT)) / 'episodes' / ep / 'out/claims.json').read_text()); cl = cl['claims'] if isinstance(cl, dict) else cl
    txt = f"{j['l1']} {j['num']}".replace('-$', '$').replace('+', '')
    risk = [f'{a} "{b}"' for a, b in scan(txt)] + [f'số "{n}" không có claim' for n in bad_numbers(txt, claim_number_set(cl))]
    words = len(f"{j['l1']} {j['num']}".replace(' = ', ' ').split())
    return dict(id=j['id'], texts=[j['l1'], j['num']], words=words, cap_px_168=caps, contrast=cs, claim_risk=risk,
                ok=bool(min(caps) >= 9 and min(cs) >= 4.5 and words <= 4 and not risk))


if __name__ == '__main__':
    (H / 'cand').mkdir(exist_ok=True)
    J = jobs(); (H / 'jobs.json').write_text(json.dumps(J, indent=1))
    subprocess.run(['node', str(H / 'compose.js'), str(H / 'jobs.json')], check=True,
                   env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
    R = [check(j) for j in J]
    for r in R:
        print(r['id'], 'ĐẠT' if r['ok'] else 'TRƯỢT', r['cap_px_168'], r['contrast'], r['claim_risk'])
    (H / 'checks.json').write_text(json.dumps(R, ensure_ascii=False, indent=1))

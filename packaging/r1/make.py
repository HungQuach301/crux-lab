#!/usr/bin/env python3
"""Đóng gói R1 · ảnh bìa dựng bằng mã (không AI, không người thật) từ khung phim/thế giới có sẵn của từng tập.
  python3 packaging/r1/make.py --frames <thư mục khung> [--render]   → packaging/r1/<ep>-<A|B|C>.png + checks.json + sheet.html
Lớp chữ = bộ nhận diện kênh của toolkit/package/thumbs.py (overlay: logo "M.", Inter Bold, dòng cuối màu trụ, ILLUSTRATIVE khi có nhân vật,
chân "US only · history, not a forecast") — gọi như đường --no-api, không sửa toolkit. Chữ qua claim-risk của toolkit/market/package_check.py.
Khung Tập 5–9: `--render` dựng lại bằng toolkit/factory/world/render_shots.js --stills (1080p; cần data/fetch.py + world/derive.py của tập,
three.js ở toolkit/factory/world/vendor; Tập 9 từ worktree nhánh ccr-4d8bc942-73gdnl qua --ep9-root). Tập 1–3: ảnh có sẵn trong repo.
Kiểm máy: thu về 168×94, đo chiều cao chữ hoa (px) và tương phản WCAG chữ/nền trong hộp chữ; đạt khi ≥ 9 px và ≥ 4,5:1."""
import argparse, json, os, pathlib, subprocess, sys
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'toolkit/package')); sys.path.insert(0, str(ROOT / 'toolkit/market'))
import thumbs                                            # noqa: E402  (overlay, font, TOK, PILLAR)
from package_check import scan, bad_numbers, claim_number_set   # noqa: E402

OUT = ROOT / 'packaging/r1'
# src: ('repo', path) | ('world', ep, segment, giây). crop: (x, y, rộng) trên khung gốc, cao = rộng·9/16. mask: hộp tô màu nền (chữ cũ của ảnh).
SPEC = [
 # Tập 1 · refi (vay nợ) — still của khung thế giới Tập 1 (work/thumbs_v2)
 dict(ep='ep001', v='A', src=('repo', 'episodes/ep001/work/thumbs_v2/still-H.png'), crop=(240, 60, 1680), lines=['SMALL LOAN', '1.12 POINTS'], ch=True, claims=['walt_cut_needed']),
 dict(ep='ep001', v='B', src=('repo', 'episodes/ep001/work/thumbs_v2/still-L.png'), crop=(200, 60, 1720), lines=['FEES BACK', 'MONTH 30'], ch=True, claims=['nora_breakeven_counting']),
 dict(ep='ep001', v='C', src=('repo', 'episodes/ep001/work/thumbs_v2/still-W.png'), crop=(160, 40, 1760), lines=['1-POINT RULE', 'FITS NONE'], ch=False, claims=['one_point_line']),
 # Tập 2 · vay học (vay nợ) — nền trung tính C6 (đã duyệt nhãn ILLUSTRATIVE)
 dict(ep='ep002', v='A', src=('repo', 'episodes/ep002/preprod/thumbs_c6/work/thumb-neutral.png'), mask=[(700, 0, 1280, 100)], crop=(240, 40, 960), lines=['APRIL 1977', '43% MORE'], ch=True, claims=['worst_pct_more']),
 dict(ep='ep002', v='B', src=('repo', 'episodes/ep002/preprod/thumbs_c6/work/thumb-neutral.png'), mask=[(700, 0, 1280, 100)], crop=(0, 0, 1280), lines=['COSTLIER', '1 IN 7'], ch=True, claims=['share_cost_more_1.5']),
 dict(ep='ep002', v='C', src=('repo', 'episodes/ep002/preprod/thumbs_c6/work/thumb-neutral.png'), mask=[(700, 0, 1280, 100)], crop=(320, 120, 800), lines=['HEAD START', '2 POINTS?'], ch=True, claims=['head_start_2pt (câu hỏi)']),
 # Tập 3 · EE vs T-bill (hưu trí/dài hạn) — nền 3 thumb cũ, chữ cũ bị phủ
 dict(ep='ep003', v='A', src=('repo', 'episodes/ep003/out/package/thumb-3.png'), mask=[(0, 0, 1280, 340)], crop=(0, 0, 1280), lines=['BEAT DOUBLE', '52.3%'], ch=False, pillar='retire', claims=['share_above_double']),
 dict(ep='ep003', v='B', src=('repo', 'episodes/ep003/out/package/thumb-1.png'), mask=[(0, 0, 1040, 330)], crop=(0, 0, 1280), lines=['SINCE 1990', 'ONLY 5%'], ch=False, pillar='retire', claims=['share_above_double_1990on']),
 dict(ep='ep003', v='C', src=('repo', 'episodes/ep003/out/package/thumb-2.png'), mask=[(0, 0, 1280, 300)], crop=(0, 0, 1280), lines=['THE LINE', '3.47%'], ch=False, pillar='retire', claims=['breakeven_bill_rate']),
 # Tập 5 · PMI (vay nợ)
 dict(ep='ep005', v='A', src=('world', 'ep005', 'd-s15-s20', 65.0), crop=(0, 150, 1440), lines=['ON PAPER', '23 MONTHS'], ch=True, claims=['medianB_months_to80']),
 dict(ep='ep005', v='B', src=('world', 'ep005', 'c-s10-s14', 100.0), crop=(240, 150, 1440), lines=['SLOWEST', '112 MONTHS'], ch=False, claims=['maxB_months_to80']),
 dict(ep='ep005', v='C', src=('world', 'ep005', 'b-s04-s09', 107.0), crop=(80, 150, 1440), lines=['BY SCHEDULE', '8 YEARS'], ch=True, claims=['sched80 payment 99 (≈ 8 năm, lời 0:10)']),
 # Tập 6 · annuity (hưu trí)
 dict(ep='ep006', v='A', src=('world', 'ep006', 'c-s09-s12', 2.0), crop=(0, 150, 1500), lines=['2% RAISE', 'BUYS LESS'], ch=True, pillar='retire', claims=['raise_pct (Ruth: buys less)']),
 dict(ep='ep006', v='B', src=('world', 'ep006', 'd-s13-s23', 44.0), crop=(180, 265, 1400), lines=['KEPT UP', '17/715'], ch=True, pillar='retire', claims=['kept_up 17 of 715']),
 dict(ep='ep006', v='C', src=('world', 'ep006', 'e-s24-s29', 23.0), crop=(660, 340, 1100), lines=['WORST START', '43.1% LEFT'], ch=True, pillar='retire', claims=['carl_end_pct']),
 # Tập 7 · 15 vs 30 (vay nợ)
 dict(ep='ep007', v='A', src=('world', 'ep007', 'b-s04-s09', 72.0), crop=(0, 150, 1500), lines=['THE FALLBACK', '$21,622'], ch=True, claims=['stack_total']),
 dict(ep='ep007', v='B', src=('world', 'ep007', 'c-s10-s15', 86.0), crop=(240, 150, 1500), lines=['PRICIEST', '1/5 OF WEEKS'], ch=True, claims=['share_weeks_as_high (< 1 in 5)']),
 dict(ep='ep007', v='C', src=('world', 'ep007', 'f-s25-s28', 2.0), crop=(0, 150, 1500), lines=['EXTRA DOLLAR', 'SAVES 7.40%'], ch=True, claims=['bar (lãi khỏi trả, không phải lợi nhuận)']),
 # Tập 8 · rent vs buy (vay nợ)
 dict(ep='ep008', v='A', src=('world', 'ep008', 'd-s15-s22', 23.0), crop=(160, 160, 1500), lines=['WORST MONTH', '-$82,385'], ch=False, claims=['adv_2006-06']),
 dict(ep='ep008', v='B', src=('world', 'ep008', 'c-s08-s14', 86.0), crop=(240, 160, 1500), lines=['DARK STRETCH', '6/72 LIT'], ch=False, claims=['era_2002-2007']),
 dict(ep='ep008', v='C', src=('world', 'ep008', 'd-s15-s22', 100.0), crop=(200, 235, 1400), lines=['HELD 15 YEARS', '100%'], ch=False, claims=['share_buyer_ahead_15y']),
 # Tập 9 · rent & invest (vay nợ) — khung từ nhánh tập ở trạng thái G2 (dựng lại sau M6)
 dict(ep='ep009', v='A', src=('world', 'ep009', 'b1-s04', 2.0), crop=(300, 335, 1100), lines=['15 YEARS', 'BUYER 21.9%'], ch=False, claims=['share_buyer_ahead_stocks_15y']),
 dict(ep='ep009', v='B', src=('world', 'ep009', 'd1-s14-s15', 37.0), crop=(280, 245, 1350), lines=['HOUSE AHEAD', '49.5%'], ch=False, claims=['share_buyer_ahead_stocks_10y']),
 dict(ep='ep009', v='C', src=('world', 'ep009', 'b1-s04', 23.0), crop=(240, 160, 1500), lines=['BUYER, 1991', '$485,063 BEHIND'], ch=False, claims=['adv_1991-01_stocks_10y']),
]
SEG = {'ep005': 'world/c4', 'ep006': 'world/c4', 'ep007': 'world/c4', 'ep008': 'world/seg', 'ep009': 'world/seg'}


def lum(c):
    def ch(v):
        v /= 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)


def hexrgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def small_check(img, base, lines, pillar):
    """Đọc được ở 168×94: chiều cao chữ hoa sau thu nhỏ + tương phản màu chữ với nền (trung vị độ sáng nền KHÔNG chữ trong hộp chữ, ảnh đã có lớp tối)."""
    k = 168 / 1280
    px = 112 if max(len(l) for l in lines) <= 14 else 96
    cap = px * 0.727 * k                                  # chữ hoa Inter ≈ 0,727 em
    y0 = int(720 - 64 - px * 1.05 * len(lines)); f = thumbs.font(px)
    wmax = max(ImageDraw.Draw(img).textlength(l, font=f) for l in lines)
    box = (48, y0, int(48 + wmax), 720 - 64)
    dark = base.crop(box).resize((max(1, int((box[2] - box[0]) * k)), max(1, int((box[3] - box[1]) * k))))
    px_ = sorted(dark.get_flattened_data(), key=lum); bg = px_[int(len(px_) * 0.9)]   # nền sáng nhất 10 % (ca xấu)
    cs = [round(contrast(hexrgb(thumbs.TOK['ink']), bg), 2), round(contrast(hexrgb(thumbs.PILLAR[pillar]), bg), 2)]
    wide = wmax <= 1280 - 48 - 40
    return dict(cap_px_168=round(cap, 1), contrast_ink=cs[0], contrast_accent=cs[1], fits_width=wide,
                ok=bool(cap >= 9 and min(cs) >= 4.5 and wide))


def darken(img, k):
    if not k:
        return img
    m = Image.new('L', img.size, 0); d = ImageDraw.Draw(m)
    for x in range(0, 900):   # dải dọc giảm dần từ trái sang phải, chỉ nửa dưới
        d.line([(x, 300), (x, 720)], fill=int(255 * k * min(1, (900 - x) / 450)))
    blk = Image.new('RGB', img.size, thumbs.TOK['bg']); return Image.composite(blk, img, m)


def frame(s, frames):
    if s['src'][0] == 'repo':
        return Image.open(ROOT / s['src'][1]).convert('RGB')
    _, ep, seg, t = s['src']
    return Image.open(pathlib.Path(frames) / ep / f'{seg}-t{t:.2f}.png').convert('RGB')


def render(frames, ep9_root):
    for ep in sorted({s['src'][1] for s in SPEC if s['src'][0] == 'world'}):
        root = pathlib.Path(ep9_root) if ep == 'ep009' else ROOT
        for seg in sorted({s['src'][2] for s in SPEC if s['src'][0] == 'world' and s['src'][1] == ep}):
            ts = ','.join(str(s['src'][3]) for s in SPEC if s['src'][0] == 'world' and s['src'][1] == ep and s['src'][2] == seg)
            env = dict(os.environ, NODE_PATH=f"/opt/node-tools/node_modules:{ROOT}/toolkit/factory/world/vendor/node_modules")
            subprocess.run(['node', 'toolkit/factory/world/render_shots.js', f'episodes/{ep}/{SEG[ep]}/{seg}', '1080', f'{frames}/x.mp4',
                            '--stills', ts, '--stills-dir', f'{frames}/{ep}', '--cache', f'{frames}/cache'], cwd=root, env=env, check=True)


def claim_risk(ep, lines, ep9_root):
    root = pathlib.Path(ep9_root) if ep == 'ep009' else ROOT
    cl = json.loads((root / 'episodes' / ep / 'out/claims.json').read_text()); cl = cl['claims'] if isinstance(cl, dict) else cl
    txt = ' '.join(lines).replace('-$', '$')
    return [f'{k} "{m}"' for k, m in scan(txt)] + [f'số "{n}" không có claim' for n in bad_numbers(txt, claim_number_set(cl))]


if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('--frames', required=True); a.add_argument('--render', action='store_true')
    a.add_argument('--ep9-root', default=str(ROOT)); o = a.parse_args()
    if o.render:
        render(o.frames, o.ep9_root)
    res = []
    for s in SPEC:
        im = frame(s, o.frames)
        for m in s.get('mask', []):
            ImageDraw.Draw(im).rectangle(m, fill=im.getpixel((4, 716)))
        x, y, w = s['crop']
        if s['src'][0] == 'world':
            w = min(w, int((960 - y) * 16 / 9))   # không lấy dải nguồn trên và chân chữ dưới của khung
        base = im.crop((x, y, x + w, y + round(w * 9 / 16))).resize((1280, 720), Image.LANCZOS)
        pillar = s.get('pillar', 'debt')
        if sum(len(l.split()) for l in s['lines']) > 4:
            sys.exit(f"{s['ep']}-{s['v']}: chữ lớn > 4 từ")
        for scrim in (0, 0.35, 0.55, 0.7, 0.8, 0.88, 0.94, 1.0):   # nền sáng sau chữ → tối dần góc dưới trái tới khi đạt (không đổi lớp chữ của kênh)
            b2 = darken(base, scrim); out = thumbs.overlay(b2, s['lines'], pillar, s['ch']); chk = small_check(out, thumbs.overlay(b2, [' '], pillar, False), s['lines'], pillar)
            if chk['ok']:
                break
        chk['scrim'] = scrim; p = OUT / f"{s['ep']}-{s['v']}.png"; out.save(p, optimize=True)
        out.resize((168, 94), Image.LANCZOS).save(OUT / 'small' / f"{s['ep']}-{s['v']}.png") if (OUT / 'small').is_dir() else None
        res.append(dict(id=f"{s['ep']}-{s['v']}", texts=s['lines'], claims=s['claims'], source=list(s['src']), crop=s['crop'], pillar=pillar,
                        illustrative=s['ch'], claim_risk=claim_risk(s['ep'], s['lines'], o.ep9_root), **chk))
        print(res[-1]['id'], 'OK' if chk['ok'] and not res[-1]['claim_risk'] else 'XEM', chk, res[-1]['claim_risk'])
    (OUT / 'checks.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))

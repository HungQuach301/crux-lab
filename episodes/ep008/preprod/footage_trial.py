"""Khung thử ghép footage ngoài vào thế giới Crux (luật tạm 13/10: G1 kèm 2–3 khung). Mạng phiên chặn LoC/HUD/Wikimedia → khung 3 là CHỖ GIỮ
(ảnh lịch sử chưa tải; URL ứng viên ở preprod/continuity.md, chủ dự án tải). Bản đồ: Natural Earth admin-1 50m (phạm vi công cộng; RIGHTS.md).
    python3 episodes/ep008/preprod/footage_trial.py
Ra work/footage/trial-{1,2,3}.png (960×540). Tông kênh: nền bg #0E1116, nét ink-muted, vùng accent mờ; chữ nguồn + năm trên hình."""
import json, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 960, 540
F = os.path.join(EP, 'work', 'footage')
OBJ = os.path.join(EP, 'work', 'objclip')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font = lambda s: ImageFont.truetype(FONT, s)
BG, INK, MUTED, ACCENT = (14, 17, 22), (242, 244, 247), (154, 164, 178), (76, 141, 255)

gj = json.load(open(os.path.join(F, 'ne_50m_admin_1.geojson')))
polys = []
for ft in gj['features']:
    p = ft['properties']
    if p.get('iso_a2') != 'US' or p.get('name') in ('Alaska', 'Hawaii'):
        continue
    g = ft['geometry']
    for poly in (g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]):
        polys.append(poly[0])


def us_map(scale=1.0, cx=0.5, cy=0.52, tilt=0.0):
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im, 'RGBA')
    lon0, lon1, lat0, lat1 = -125, -66.5, 24, 49.5
    sx = W * 0.86 * scale / (lon1 - lon0)
    for ring in polys:
        pts = []
        for lon, lat in ring:
            x = (lon - (lon0 + lon1) / 2) * sx
            y = -(lat - (lat0 + lat1) / 2) * sx * 1.25
            y *= (1 - tilt)
            pts.append((W * cx + x, H * cy + y))
        if len(pts) > 2:
            d.polygon(pts, fill=(76, 141, 255, 38), outline=MUTED + (200,))
    return im


def tag(im, lines, xy=(24, H - 70)):
    d = ImageDraw.Draw(im, 'RGBA')
    y = xy[1]
    for t, c, s in lines:
        w = d.textlength(t, font=font(s))
        d.rounded_rectangle((xy[0] - 8, y - 4, xy[0] + w + 8, y + s + 6), 8, fill=(14, 17, 22, 190))
        d.text((xy[0], y), t, font=font(s), fill=c)
        y += s + 14
    return im


# 1 — bản đồ Mỹ, máy đẩy chậm (khung giữa đường đẩy), chữ phạm vi + nguồn
m1 = tag(us_map(1.05), [('US only', INK, 30), ('Map: Natural Earth (public domain)', MUTED, 18)], (24, H - 92))
m1.save(os.path.join(F, 'trial-1.png'))
# 2 — hoà: bản đồ nghiêng xuống làm mặt đất, lưới phố 3D hiện lên (khung đồ thị của clip the street) — dissolve 55 %
street = Image.open(os.path.join(OBJ, 'street', 'f0205.png')).convert('RGB') if os.path.exists(os.path.join(OBJ, 'street', 'f0205.png')) else Image.new('RGB', (W, H), BG)
m2 = Image.blend(us_map(1.25, tilt=0.35), street, 0.55)
tag(m2, [('Map: Natural Earth (public domain)', MUTED, 18)], (24, H - 46)).save(os.path.join(F, 'trial-2.png'))
# 3 — CHỖ GIỮ ảnh lịch sử (chưa tải): khung ảnh trong tông kênh (đơn sắc, viền mờ), năm + nguồn trên hình, hoà từ cảnh 3D (nhà 6/2006 tối)
ph = Image.new('RGB', (W, H), (40, 44, 52))
d = ImageDraw.Draw(ph)
d.text((W / 2 - 300, H / 2 - 20), '[historical photo — not yet downloaded]', font=font(26), fill=MUTED)
ph = ph.filter(ImageFilter.GaussianBlur(1))
bg3 = Image.open(os.path.join(OBJ, 'tag', 'f0120.png')).convert('RGB') if os.path.exists(os.path.join(OBJ, 'tag', 'f0120.png')) else Image.new('RGB', (W, H), BG)
m3 = Image.blend(bg3, ph, 0.7)
tag(m3, [('2008 · photo: Library of Congress, no known restrictions', INK, 20), ('Illustration, not evidence', MUTED, 18)], (24, H - 80)).save(os.path.join(F, 'trial-3.png'))
print('trial-1..3.png')

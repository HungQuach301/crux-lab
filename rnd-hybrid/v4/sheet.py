"""R&D v4 · tờ trước | sau cho chủ dự án (chỉ ảnh tĩnh 1080p, không clip).
  python3 rnd-hybrid/v4/sheet.py   → rnd-hybrid/v4/out/SHEET-before-after.jpg + SHEET-history.jpg + close-check-1080.png
Đọc ảnh do light/measure.js ghi ở out/meas/ (cấu hình base = cảnh gốc nhà máy, full = mọi lớp) và out/hist/ (film.sh)."""
import os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(H, 'out', 'meas'); OUT = os.path.join(H, 'out')
F = lambda s, w='SemiBold': ImageFont.truetype(f'/usr/share/fonts/opentype/inter/Inter-{w}.otf', s)
def cell(p, w=960):
    im = Image.open(p).convert('RGB'); return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
def sheet(rows, cols, out, title):
    W, CH, pad, top, lab = 960, 540, 16, 140, 300
    img = Image.new('RGB', (lab + len(cols) * (W + pad) + pad, top + len(rows) * (CH + pad) + pad), '#101317'); d = ImageDraw.Draw(img)
    d.text((pad, 24), title, font=F(40, 'Bold'), fill='#F2F4F7')
    for j, c in enumerate(cols): d.text((lab + pad + j * (W + pad), top - 40), c, font=F(30), fill='#C9D1DC')  # nhãn cột dưới tiêu đề
    for i, (name, files) in enumerate(rows):
        y = top + i * (CH + pad)
        for k, ln in enumerate(name.split('\n')): d.text((pad, y + 10 + k * 36), ln, font=F(28 if k == 0 else 22, 'SemiBold' if k == 0 else 'Regular'), fill='#F2F4F7' if k == 0 else '#9AA4B2')
        for j, f in enumerate(files):
            if f: img.paste(cell(f, W), (lab + pad + j * (W + pad), y))
    img.save(out, quality=90); print(out, img.size)
m = lambda n: os.path.join(M, n + '.png')
sheet([('Tessa cận\nđoạn a · 27 s · hồi 1 (ngày)\nngược sáng, DOF theo người', [m('close-base'), m('close-full')]),
       ('Phố / nhà\nđoạn g · 3 s · hồi 3 (hoàng hôn)', [m('street-base'), m('street-full')]),
       ('Dữ liệu\nđoạn c · 85 s · hồi 2 (chiều)\nnền tối giữ nguyên', [m('data-base'), m('data-full')])],
      ['TRƯỚC: cảnh gốc nhà máy (Tập 7)', 'SAU: việc 1 (ánh sáng) + 2a (người viền sáng)'], os.path.join(OUT, 'SHEET-before-after.jpg'), 'Vòng 4 · Tập 7 · trước | sau (1080p, cùng khung, cùng mã cảnh)')
sheet([('K1 · tư liệu\nngân hàng đóng cửa 12/1930\nảnh LoC toàn khung + chữ in', [m('k1-base'), None]),
       ('K2 · vật thể số liệu 3D\nlưới 20 → 30 năm', [m('k2-base'), m('k2-full')]),
       ('Phim Prelinger (PD)\nc. 1935 · ổn định, tông, viền', [os.path.join(OUT, 'hist', 'film-raw-1080.png'), os.path.join(OUT, 'hist', 'film-processed-1080.png')])],
      ['TRƯỚC / gốc', 'SAU (lớp ánh sáng · xử lý)'], os.path.join(OUT, 'SHEET-history.jpg'), 'Vòng 4 · chương lịch sử không vẽ người (2b)')
# kiểm cận 1080p (2a): cắt vùng Tessa của khung 1080p, phóng ×2 (không nội suy mượt) để soi viền sáng và dáng
im = Image.open(m('close-full')); crop = im.crop((560, 400, 1040, 900)); crop.resize((crop.width * 2, crop.height * 2), Image.NEAREST).save(os.path.join(OUT, 'close-check-1080.png')); print('close-check ok')

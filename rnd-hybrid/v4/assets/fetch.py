"""R&D v4 · tải tài sản CC0 của Poly Haven (polyhaven.com, mọi tài sản CC0) cho lớp ánh sáng điện ảnh.
  python3 rnd-hybrid/v4/assets/fetch.py            → tải những tệp còn thiếu, kiểm SHA-256 với manifest.json (lệch = dừng)
  python3 rnd-hybrid/v4/assets/fetch.py --pin      → (một lần) ghi SHA-256 vào manifest.json
Tệp ≤ 2 MB được commit (rnd-hybrid/v4/assets/cc0/); tệp lớn hơn chỉ tải lúc dựng (.gitignore), kiểm bằng SHA-256 trong manifest."""
import hashlib, json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'cc0'); MAN = os.path.join(HERE, 'manifest.json')
HDRI = {'day': 'kloofendal_48d_partly_cloudy_puresky', 'afternoon': 'rustig_koppie_puresky', 'dusk': 'qwantani_dusk_2_puresky'}
TEX = {'road': 'asphalt_02', 'wall': 'painted_plaster_wall', 'roof': 'clay_roof_tiles_02', 'wood': 'brown_planks_03', 'paper': 'beige_wall_001'}
def plan():
    items = []
    for look, ph in HDRI.items():
        items.append({'id': f'hdri-{look}', 'asset': ph, 'file': f'{ph}_1k.hdr', 'url': f'https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/1k/{ph}_1k.hdr'})
    for role, ph in TEX.items():
        for m, tag in (('diff', 'Diffuse'), ('nor_gl', 'nor_gl'), ('rough', 'Rough')):
            items.append({'id': f'tex-{role}-{m}', 'asset': ph, 'file': f'{ph}_{m}_1k.jpg', 'url': f'https://dl.polyhaven.org/file/ph-assets/Textures/jpg/1k/{ph}/{ph}_{m}_1k.jpg'})
    return items
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); man = json.load(open(MAN)) if os.path.exists(MAN) else {}
    for it in plan():
        p = os.path.join(OUT, it['file'])
        if not os.path.exists(p):
            urllib.request.urlretrieve(it['url'], p + '.part'); os.replace(p + '.part', p)
        h, n = sha(p), os.path.getsize(p)
        if '--pin' in sys.argv: man[it['id']] = {**it, 'sha256': h, 'bytes': n, 'licence': 'CC0 1.0 (Poly Haven)', 'commit': n <= 2_000_000}
        elif man.get(it['id'], {}).get('sha256') != h: sys.exit(f"SHA-256 lệch: {it['file']}")
        print(it['id'], n, h[:16])
    if '--pin' in sys.argv: json.dump(man, open(MAN, 'w'), indent=1)

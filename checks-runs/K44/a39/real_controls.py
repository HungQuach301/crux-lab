"""K4.4 · A39/A40 — đối chứng THẬT cho luật CHẶN F13 (A40 (2)): bản sao Tập 7 (master 529471f0…, timeline, mô tả thật) chèn MỘT tư liệu thật —
ảnh LoC FSA 1936 "An automobile accident on the U.S. 40 between Hagerstown and Cumberland, Maryland" (tệp và dòng quyền thật của cine-lab:
assets/ll/archive/fsa-8b28380.jpg, RIGHTS.md LOC-8b28380: "No known restrictions…", tải 2026-10-06) ở 120–125 s, kind archival.
  âm  : hồ sơ đủ (URL, trích nguyên văn, ngày tải, SHA khớp, ghi nguồn) → F13 ĐẠT
  dương 1: không có dòng RIGHTS (lỗi hay gặp nhất: tải ảnh rồi dựng)             → F13 TRƯỢT
  dương 2: tệp bị lưu lại sau khi ghi hồ sơ (JPEG nén lại, khác byte)           → F13 TRƯỢT (SHA)
  dương 3: footage 120–250 s (130 s / 606,7 s = 21,4 % > 20 %)                  → F13 TRƯỢT (trần)
  F15 (CHÍNH): cần out/checks/page.json Tập 7 (A29 --no-cache); không có lúc chạy → MISSING; đối chứng thật F15 làm ở K4.4.1
  python3 checks-runs/K44/a39/real_controls.py <out.json>"""
import hashlib, io, json, os, shutil, sys, tempfile
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'checks', 'py'))
import common, run as runner  # noqa
from PIL import Image
R = {fn.rid: fn for fn in common.RULES}
SRC = '/home/user/hungquach301/cine-lab/assets/ll/archive/fsa-8b28380.jpg'
QUOTE = '"No known restrictions. For information, see U.S. Farm Security Administration/Office of War Information Black & White Photographs"'
E = os.path.join(REPO, 'episodes', 'ep007')


def root(case):
    d = tempfile.mkdtemp(prefix=f'a39-{case}-')
    for n in os.listdir(E):
        if n not in ('out', 'RIGHTS.md', 'work'):
            os.symlink(os.path.join(E, n), os.path.join(d, n))
    os.mkdir(os.path.join(d, 'out'))
    for n in os.listdir(os.path.join(E, 'out')):
        if n not in ('checks', 'timeline.json'):
            os.symlink(os.path.join(E, 'out', n), os.path.join(d, 'out', n))
    os.makedirs(os.path.join(d, 'out', 'checks'))
    pg = '/home/user/a29-out/ep007-nocache.json'
    if os.path.exists(pg):
        shutil.copy(pg, os.path.join(d, 'out', 'checks', 'page.json'))
    os.makedirs(os.path.join(d, 'work', 'external'))
    dst = os.path.join(d, 'work', 'external', 'loc-8b28380.jpg')
    shutil.copy(SRC, dst)
    sha = hashlib.sha256(open(dst, 'rb').read()).hexdigest()
    if case == 'pos2-resaved':   # hồ sơ ghi trước, tệp lưu lại sau
        im = Image.open(dst); buf = io.BytesIO(); im.save(buf, 'JPEG', quality=85); open(dst, 'wb').write(buf.getvalue())
    tl = json.load(open(os.path.join(E, 'out', 'timeline.json')))
    tl['external'] = [{'file': 'work/external/loc-8b28380.jpg', 'rid': 'X-7-1', 'kind': 'archival', 't0': 120.0, 't1': 250.0 if case == 'pos3-share' else 125.0}]
    json.dump(tl, open(os.path.join(d, 'out', 'timeline.json'), 'w'))
    rights = ('# RIGHTS (bản sao thử)\n\n| Mã | Tệp | Loại | URL | Giấy phép | Trích nguyên văn | Ngày tải | SHA-256 | Ghi nguồn |\n|---|---|---|---|---|---|---|---|---|\n')
    if case != 'pos1-no-row':
        rights += (f'| X-7-1 | work/external/loc-8b28380.jpg | image | https://www.loc.gov/pictures/item/2017761235/ | No known restrictions (LoC, bậc 5) | {QUOTE} '
                   f'| 2026-10-06 | {sha} | Source: Library of Congress, 1936 |\n')
    open(os.path.join(d, 'RIGHTS.md'), 'w').write(rights)
    return d


out = {}
for case in ('neg-complete', 'pos1-no-row', 'pos2-resaved', 'pos3-share'):
    d = root(case)
    ctx = common.Ctx(d)
    out[case] = {}
    for rid in ('F13', 'F15'):
        r = common.safe(R[rid], ctx)
        out[case][rid] = {'status': r['status'], 'fail': {m['name']: m['value'] for m in r['metrics'] if not m['pass']}, 'note': r.get('note')}
    print(case, json.dumps(out[case], ensure_ascii=False)[:400], flush=True)
    shutil.rmtree(d, ignore_errors=True)
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)

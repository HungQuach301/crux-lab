"""F-17 thử: spine.py của thư mục thử = spine.json ĐÃ GIAO của đoạn Tập 7 (không tính lại) + khoá `cine` (cách một spine.py của tập khai lớp).
  python3 toolkit/factory/f17/trial/<đoạn>/spine.py   (gọi hàm write dưới đây)"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))


def write(here, seg, cine):
    sp = json.load(open(os.path.join(ROOT, 'episodes/ep007/world/c4', seg, 'spine.json')))
    if cine: sp['cine'] = cine
    json.dump(sp, open(os.path.join(here, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
    print('spine', seg, 'cine' if cine else 'không cine', sp['total'])

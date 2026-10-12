"""Tập 7 · C5 · dựng riêng bước Shorts của nhà máy (toolkit/factory/build.py do_shorts) khi các bước trước đã xong ở lượt build trước
(đoạn thế giới 1080 đã verify, picture/master/parts có sẵn): mỗi lần build.sh chạy lại tốn ≈ 50 phút kiểm lại 7 đoạn trước khi tới Shorts
và bị cắt ở trần 2 h của lệnh nền. Không sửa toolkit; gọi đúng các hàm của Build: load_inputs → do_voice (cache) → do_resolve → splice_segs
(SPLICE.scene_span, như do_splice, không mã hoá lại hình) → master_wav có sẵn → do_shorts (cache theo span ở work/factory/world-shorts-cache).
    python3 episodes/ep007/c5/shorts_only.py            → work/factory/SH*.mp4 + out/factory/shorts-only.json"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path[:0] = [os.path.join(ROOT, 'toolkit', 'factory'), os.path.join(ROOT, 'toolkit', 'factory', 'world')]
import build as BLD  # noqa: E402
import splice as SPLICE  # noqa: E402

B = BLD.Build(os.path.join(ROOT, 'episodes', 'ep007', 'episode.yaml'), [])
B.load_inputs()
B.step('voice', B.do_voice)
B.step('resolve', B.do_resolve)
res = B.S.get('res', 1080)
segs = []
for w in B.S['world']:
    t0, t1, f0, f1 = SPLICE.scene_span(B.tl, w['scenes'], B.fps)
    mp4 = os.path.join(B.work, 'world', f"{w['id']}-{res}.mp4")
    assert os.path.exists(mp4), mp4
    segs.append({'id': w['id'], 'mp4': mp4, 'f0': f0, 'f1': f1, 't0': t0, 't1': t1, 'scenes': list(w['scenes']),
                 'stems': os.path.join(mp4[:-4] + '.audio', 'stems')})
B.splice_segs = segs
B.master_wav = os.path.join(B.work, 'master.wav')
assert os.path.exists(B.master_wav)
r = B.step('shorts', B.do_shorts)
json.dump(r, open(os.path.join(B.out, 'shorts-only.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps([{k: s[k] for k in ('id', 'duration')} for s in r['shorts']]))

"""Nhà máy · DỰNG MỘT ĐOẠN THẾ GIỚI 3D bằng một lệnh (D-010; quy trình hai đoạn chứng minh Mốc V).

  python3 toolkit/factory/world/build_seg.py <thư mục đoạn> [--res 540|1080] [--out <file.mp4>] [--workers 3] [--music code|<wav>]

Thư mục đoạn chứa: spine.py (đặc tả nhịp, dùng toolkit/factory/world/spine.py) + scene.js (dùng lib3d.js/core.js) [+ dữ liệu].
Các bước (mỗi bước dừng cả lệnh nếu trượt):
  lint    lint_comments.py trên thư mục đoạn + thư viện (lỗi "chú thích nuốt mã")
  spine   python3 <đoạn>/spine.py → spine.json; thoát ≠ 0 = vi phạm quy tắc 2/3/7
  render  render_shots.js theo cảnh có cache (chỉ cảnh đổi mới render; chạy lại = resume); lỗi trang = dừng
  audio   audio.py: lời + nhạc theo bản đồ căng + âm dữ liệu + sfx từ spine.events → mix.wav (−14 LUFS)
  mux     hình + tiếng → <out>
  verify  verify_seg.py: quy tắc 1/2/3, cắt cứng, tỉ lệ chế độ, C14 (bản 1080p), F-2 (mật độ sfx, nhãn đè nhau) → <out>.verify.json;
          quy tắc 1/2/3, cắt cứng, C14 hoặc F-2 cấp BLOCK trượt = thoát 1 (F-2 WARN chỉ báo)
Báo cáo giờ render thật (wall, s/giây phim) trong <out>.build.json (quy tắc 8: "báo giờ render và token thực").
Đồng bộ lời–hình bằng ASR (sync_audit.py) chạy riêng vì cần faster-whisper.
"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import lint_comments  # noqa: E402


def arg(k, d=None):
    return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d


def run(cmd, **kw):
    r = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, **kw)
    if r.returncode:
        print(r.stdout[-3000:], r.stderr[-3000:])
    return r


def main():
    seg = os.path.relpath(os.path.abspath(sys.argv[1]), ROOT)
    res = int(arg('--res', 540))
    out = os.path.abspath(arg('--out', os.path.join(ROOT, seg, '..', '..', 'work', 'world', f'{os.path.basename(seg)}-{res}.mp4')))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rep, T = {'segment': seg, 'res': res, 'out': os.path.relpath(out, ROOT), 'steps': {}}, time.time()

    def step(name, fn):
        t = time.time(); ok, info = fn(); rep['steps'][name] = {'seconds': round(time.time() - t, 1), 'ok': ok, **(info or {})}
        print(f'[{name}] {"OK" if ok else "TRƯỢT"} {rep["steps"][name]["seconds"]} s', flush=True)
        if not ok:
            json.dump(rep, open(out + '.build.json', 'w'), indent=1, ensure_ascii=False)
            raise SystemExit(f'build_seg: dừng ở bước {name}')

    def lint():
        bad = lint_comments.lint([os.path.join(ROOT, seg), HERE])
        return not bad, {'problems': bad}

    def spine():
        r = run([sys.executable, os.path.join(seg, 'spine.py')])
        return r.returncode == 0, {'stdout': r.stdout.strip().splitlines()[-1:] }

    def render():
        env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
        pic = out.replace('.mp4', '.picture.mp4')
        r = run(['node', os.path.join(HERE, 'render_shots.js'), seg, str(res), pic, '--workers', arg('--workers', '3')], env=env)
        st = json.load(open(pic + '.render.json')) if r.returncode == 0 else {}
        return r.returncode == 0, {k: st.get(k) for k in ('shots', 'rendered', 'cached', 'wall_s', 'film_s', 'wall_per_film_s_rendered', 'cores')}

    def audio():
        r = run([sys.executable, os.path.join(HERE, 'audio.py'), out.replace('.mp4', '.audio'), '--spine', os.path.join(seg, 'spine.json'),
                 '--music', arg('--music', 'code')])
        return r.returncode == 0, None

    def mux():
        pic, mix = out.replace('.mp4', '.picture.mp4'), os.path.join(out.replace('.mp4', '.audio'), 'mix.wav')
        r = run(['ffmpeg', '-y', '-loglevel', 'error', '-i', pic, '-i', mix, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
                 '-shortest', out])
        if r.returncode == 0:   # nhật ký trang đi theo video (verify_seg đọc <video>.log.json)
            os.replace(pic.replace('.mp4', '.log.json'), out.replace('.mp4', '.log.json'))
            if os.path.exists(pic.replace('.mp4', '.cam.json')):   # máy quay từng khung → out/camera.json của tập (artefacts.py)
                os.replace(pic.replace('.mp4', '.cam.json'), out.replace('.mp4', '.cam.json'))
        return r.returncode == 0, None

    def verify():
        vj = out + '.verify.json'
        r = run([sys.executable, os.path.join(HERE, 'verify_seg.py'), os.path.join(ROOT, seg), out, vj])
        if r.returncode:
            return False, None
        v = json.load(open(vj))
        fail = {'rule1': v['rule1']['violations'], 'rule2': len(v['rule2']['camera_moving_at_keyword']), 'rule3': len(v['rule3']['missing_reason_or_sound']),
                'hard_cuts': len(v['cuts']['hard_cuts']), 'first_5s_world': v['modes']['first_5s_world']}
        c14 = v['C14'].get('violations')
        f2 = v['F2']   # F-2: BLOCK (sfx che từ khoá / nhãn đè nhau ở trạng thái đọc) dừng build; WARN chỉ báo
        for lv in ('block', 'warn'):
            for m in f2[lv]: print(f'  F-2 {lv.upper()}: {m}')
        ok = not (fail['rule1'] or fail['rule2'] or fail['rule3'] or fail['hard_cuts']) and fail['first_5s_world'] and not c14 and f2['level'] != 'BLOCK'
        return ok, {**fail, 'C14': v['C14'], 'modes': v['modes'], 'F2': {**f2['summary'], 'block': f2['block'], 'warn': f2['warn']}}

    for name, fn in (('lint', lint), ('spine', spine), ('render', render), ('audio', audio), ('mux', mux), ('verify', verify)):
        step(name, fn)
    rep['total_seconds'] = round(time.time() - T, 1)
    json.dump(rep, open(out + '.build.json', 'w'), indent=1, ensure_ascii=False)
    print(f'build_seg: {rep["total_seconds"]} s → {os.path.relpath(out, ROOT)}')


if __name__ == '__main__':
    main()

"""Nhà máy · SHORT 9:16 TỪ ĐOẠN THẾ GIỚI 3D (D-006 Q3; checks SH01–SH05; playbook §5).

Một Short có khoảng [a, b) (giây của tập) nằm trọn trong một đoạn `world:` được DỰNG LẠI ở 1080×1920 từ chính scene.js của đoạn
(render_shots.js --span --orient v; core.CK.view): cùng máy quay, khung = cửa sổ dọc của mặt phẳng thiết kế (3D render đúng cửa sổ đó bằng
setViewOffset — không phải cắt ảnh 16:9; rộng 1080/vs px thiết kế, vs = `scale` của Short trong episode.yaml, mặc định 0,75), chữ của cảnh nâng lên ≥ 56 px và đẩy vào vùng an toàn dọc (qc.py SAFE['v']; chữ nhỏ < 48 px đã nâng mà đè chữ vẽ trước thì bỏ — log.v.dropped), lớp bắt buộc dọc của nhà máy:
móc (hook), ILLUSTRATIVE + "US only · history, not a forecast" trên MỌI khung có số, đối trọng của tập xoay mỗi 3 s.
Thẻ cuối 1,5 s: template endcard của nhà máy 2D (cùng như Short 2D). Tiếng: cắt từ master.wav của tập [a, b), fade 50/150 ms, loudnorm hai lượt
−14 LUFS / −1,5 dBTP (SH03/SH04), đệm lặng dưới thẻ cuối. Nhật ký khung (dạng engine 2D, mỗi 6 khung) cho qc.py frame_rules('v').
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ENC_V = {'crf': 14, 'preset': 'fast'}   # = build.py render(): encode của Short


def seg_for(segs, a, b, eps=1e-3):
    """Đoạn thế giới chứa trọn [a, b) (giây của tập) hoặc None."""
    return next((g for g in segs or [] if a >= g['t0'] - eps and b <= g['t1'] + eps), None)


VS_DEFAULT = 0.75   # cửa sổ dọc rộng 1080/0,75 = 1440 px thiết kế (75 % bề ngang khung 16:9): đồ thị rộng vẫn gần trọn; chữ vẫn ≥ 56 px (nâng)


def render_world(seg_dir, la, lb, out, hook, cws, workers=3, cache=None, extra=None, vs=VS_DEFAULT):
    """Khung dọc 1080×1920 của đoạn, giây đoạn [la, lb) → out (.mp4) + out.log.json (+ .cam.json). Trả báo cáo render."""
    env = {**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()}
    cmd = ['node', os.path.join(HERE, 'render_shots.js'), os.path.relpath(seg_dir, ROOT), '1920', out, '--span', f'{la:.4f},{lb:.4f}', '--orient', 'v',
           '--vs', f'{vs:g}', '--hook', hook or '', '--cws', json.dumps(cws, ensure_ascii=False), '--vt0', f'{la:.4f}', '--workers', str(workers), *(['--cache', cache] if cache else []), *(extra or [])]
    r = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f'world short: render_shots failed\n{r.stdout[-1500:]}\n{r.stderr[-2500:]}')
    return json.load(open(out + '.render.json'))


def frame_logs(world_log, la, fps, end_logs=(), end_t0=None):
    """Nhật ký dọc của khung thế giới (log.v của core.Overlay, mỗi 3 khung) → dạng nhật ký engine 2D cho qc.py, mỗi 6 khung (t = giây của Short);
    + nhật ký thẻ cuối (engine 2D, f = khung của Short)."""
    out = []
    for L in world_log:
        f = round((L['t'] - la) * fps)
        if f % 6 or 'v' not in L:
            continue
        V = L['v']
        out.append({'t': round(f / fps, 3), 'texts': V['texts'], 'raised': V['raised'], 'fitted': V.get('fitted', []), 'shifted': V.get('shifted', []),
                    'collisions': V['collisions'], 'recoloured': V['recoloured'], 'tags': V['tags'], 'claims': V['claims'], 'hist': V['hist'], 'illus': V['illus']})
    return out + list(end_logs)


def short_audio(master_wav, a, L, end, out_wav, lufs=-14.0, tp=-1.5):
    """[a, a + L) của master → fade, loudnorm hai lượt (−14 LUFS, −1,5 dBTP), đệm lặng `end` s."""
    pre = out_wav + '.pre.wav'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{a:.4f}', '-t', f'{L:.4f}', '-i', master_wav, '-af',
                    f'afade=t=in:d=0.05,afade=t=out:st={max(0.0, L - 0.15):.4f}:d=0.15', '-ar', '48000', '-ac', '2', pre], check=True)
    flt = f'loudnorm=I={lufs}:TP={tp}:LRA=11'
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', pre, '-af', flt + ':print_format=json', '-f', 'null', '-'], capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex('{'):r.stderr.rindex('}') + 1])
    flt2 = (f"{flt}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
            f":offset={m['target_offset']}:linear=true")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', pre, '-af', f'{flt2},aresample=48000,apad=whole_dur={L + end:.4f}', '-t', f'{L + end:.4f}',
                    '-ac', '2', '-c:a', 'pcm_s16le', out_wav], check=True)
    os.remove(pre)
    return {'measured_I': float(m['input_i'])}


def assemble(world_mp4, end_mp4, wav, out, fps):
    """Khung thế giới + thẻ cuối (mã hoá lại một lần, thông số Short của nhà máy) + tiếng → out (H.264 1080×1920 + AAC)."""
    import splice as SP
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', world_mp4, '-i', end_mp4, '-i', wav, '-filter_complex',
                    '[0:v]setsar=1,format=yuv420p[a];[1:v]scale=1080:1920,setsar=1,format=yuv420p[b];[a][b]concat=n=2:v=1:a=0[v]', '-map', '[v]', '-map', '2:a',
                    *SP.encode_args(ENC_V, fps), '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', out], check=True)
    return out

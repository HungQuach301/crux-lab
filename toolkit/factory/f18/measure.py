"""F-18 · đo trên Tập 7 (bản thử, 540p nháp): ba biến thể ghép từ CÙNG bảy đoạn thế giới đã dựng (build_seg, không đổi scene.js/render):
  A = như bản đăng (sfx tổng hợp, cắt cứng ở biên đoạn) · B = A + J-cut ở biên đoạn (spine `cuts`) · C = B + SFX ghi âm thật ở 3 cảnh
  (S23, S24, S25; sfx_labels.plan_real) + tỉa dấu nhấn dày (sfx_labels.thin_events) trên mọi đoạn.

  python3 toolkit/factory/f18/measure.py spines                      spine thử → toolkit/factory/f18/trial/{B,C}/<đoạn>/spine.json + plan.json
  python3 toolkit/factory/f18/measure.py audio <segdir>              audio.py cho spine C → <segdir>/<đoạn>-540.C.audio
  python3 toolkit/factory/f18/measure.py build <A|B|C> <segdir> <gốc>  ghép (splice_video + merge_audio) + loudnorm 2 lượt + mux → gốc checks
  python3 toolkit/factory/f18/measure.py av <gốc A> <gốc B>          lệch hình–tiếng: tiếng trùng byte? khung ngoài vùng J/L lệch bao nhiêu khung?
  python3 toolkit/factory/f18/measure.py metrics <gốc> [a b]         LUFS/dBTP, lời/nền 1–4 kHz, lặp tệp, mật độ sfx (cả tập + cửa sổ [a, b])
  python3 toolkit/factory/f18/measure.py clip <gốc> <a> <b> <out.mp4> cắt đoạn xem

Gốc checks = bản sao `episodes/ep007/out` (timeline, tempo-map, camera, transitions…) + video/stem của biến thể + `world/c4/<đoạn>/spine.json`
của biến thể (checks T4 đọc spine qua episode.yaml `world`). Không có bước `music.post` của build.py (ident/close lift F-12) và mã hoá nháp CRF 18:
so sánh là A ↔ B ↔ C, không phải với bản đăng.
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
sys.dont_write_bytecode = True
import numpy as np  # noqa: E402
import soundfile as sf  # noqa: E402
import splice as SP  # noqa: E402
import sfx_labels as L  # noqa: E402

EP = os.path.join(ROOT, 'episodes', 'ep007')
TL = json.load(open(os.path.join(EP, 'out', 'factory', 'timeline.json')))
SEGS = [w['id'] for w in TL['world']]
FPS, SR = TL['fps'], 48000
J_OFFSET = 0.5          # ≤ 0,5 s: R09 tìm điểm cắt trong ±0,5 s quanh chuyển hồi (checks/py/r_k40.py); 0,5 s lời vào trước hình ≥ 0,2 s (V10)
LABELS = {'S23': ['giay', 'dong-ho'], 'S24': ['tien-xu', 'giay'], 'S25': ['tien-xu', 'may-chu']}   # ba cảnh thay sfx (lời: trả mỗi năm một lần
                                                                                               # / đồng tiền nằm trong số dư / đồng tiền gốc)
ENC = {'crf': 18, 'preset': 'fast'}
LUFS, TP = -14.0, -2.0  # episode.yaml Tập 7 audio


def spine_of(seg):
    return json.load(open(os.path.join(EP, 'world', 'c4', seg, 'spine.json')))


def trial_dir(v, seg=''):
    return os.path.join(HERE, 'trial', v, seg)


def cmd_spines():
    man = json.load(open(os.path.join(ROOT, 'toolkit', 'factory', 'world', 'sfx', 'manifest.json')))
    segs = [{**w, 'mp4': '', 'spine': spine_of(w['id'])} for w in TL['world']]
    # J ở mọi biên đoạn mà J_OFFSET không giấu từ khoá (plan_joins dừng khi giấu → thử từng biên)
    cuts, skipped = {}, []
    for i in range(1, len(segs)):
        sp = dict(segs[i]['spine']); sc = segs[i]['scenes'][0]
        sp['cuts'] = {sc: {'cut': 'J', 'offset': J_OFFSET}}
        try:
            SP.plan_joins([{**segs[i - 1]}, {**segs[i], 'spine': sp}], FPS)
            cuts[segs[i]['id']] = sp['cuts']
        except SystemExit as e:
            skipped.append({'segment': segs[i]['id'], 'why': str(e)})
    used, rep = {}, {'cuts': cuts, 'skipped': skipped, 'segments': {}}
    for g in segs:
        base = g['spine']
        b = {**base, **({'cuts': cuts[g['id']]} if g['id'] in cuts else {})}
        c = L.thin_events(b)
        c = L.plan_real(c, LABELS, man, used=used, only_scenes=set(LABELS))
        for v, sp in (('B', b), ('C', c)):
            os.makedirs(trial_dir(v, g['id']), exist_ok=True)
            json.dump(sp, open(os.path.join(trial_dir(v, g['id']), 'spine.json'), 'w'), indent=1, ensure_ascii=False)
        rep['segments'][g['id']] = {'events_before': len(base['events']), 'events_after': len(c['events']),
                                    'dropped': c['sfx_thin']['dropped'], 'plan': c['sfx_real']['plan']}
    allplan = [p for s in rep['segments'].values() for p in s['plan']]
    rep['repeat'] = L.repeat_report(allplan)
    json.dump(rep, open(os.path.join(HERE, 'trial', 'plan.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({'cuts': list(cuts), 'skipped': [s['segment'] for s in skipped], 'repeat': rep['repeat'],
                      'dropped': {k: len(v['dropped']) for k, v in rep['segments'].items()}}))


def cmd_audio(segdir):
    for seg in SEGS:
        sp = os.path.join(trial_dir('C', seg), 'spine.json')
        out = os.path.join(segdir, f'{seg}-540.C.audio')
        subprocess.run([sys.executable, os.path.join(ROOT, 'toolkit', 'factory', 'world', 'audio.py'), out, '--spine', sp], check=True,
                       capture_output=True, cwd=ROOT)
        print(seg, json.load(open(os.path.join(out, 'audio-report.json'))).get('sfx_real'))


def episode_voice(path):
    """Lời của tập = take của mỗi đoạn đặt ở t0 + t (như build.py do_mix, theo spine.takes đã cắt)."""
    sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
    import audio as A
    N = int(round(TL['total'] * SR))
    v = np.zeros(N)
    for w in TL['world']:
        for tk in spine_of(w['id'])['takes']:
            x = A.load(tk['wav'] if 'wav' in tk else os.path.join(ROOT, tk['mp3']))
            if tk.get('cut'):
                x = x[:int(tk['cut'] * SR)].copy(); f = int(0.03 * SR); x[-f:] *= np.linspace(1, 0, f)
            i0 = int(round((w['t0'] + tk['t']) * SR)); n = min(len(x), N - i0)
            v[i0:i0 + n] += x[:n]
    sf.write(path, np.stack([v, v], 1), SR, subtype='PCM_24')


def loudnorm(src, dst, tp=TP):
    flt = f'loudnorm=I={LUFS}:TP={tp}:LRA=11'
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', src, '-af', flt + ':print_format=json', '-f', 'null', '-'], capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex('{'):r.stderr.rindex('}') + 1])
    flt2 = (f"{flt}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
            f":offset={m['target_offset']}:linear=true")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-af', flt2 + ',aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', dst], check=True)
    return 10 ** ((LUFS - float(m['input_i'])) / 20)


def cmd_build(v, segdir, root, aac_ceiling=None):
    if os.path.exists(root):
        shutil.rmtree(root)
    shutil.copytree(os.path.join(EP, 'out'), os.path.join(root, 'out'), ignore=shutil.ignore_patterns('checks', 'video.mp4', 'audio'))
    for f in ('episode.yaml', 'contract.json'):
        shutil.copy(os.path.join(EP, f), root)
    for d in ('c4', 'data', 'numbers.md', 'story', 'model'):
        if os.path.exists(os.path.join(EP, d)):
            os.symlink(os.path.join(EP, d), os.path.join(root, d))
    work = os.path.join(root, 'work'); os.makedirs(work)
    segs = []
    for w in TL['world']:
        spv = os.path.join(EP, 'world', 'c4', w['id'], 'spine.json') if v == 'A' else os.path.join(trial_dir(v, w['id']), 'spine.json')
        os.makedirs(os.path.join(root, 'world', 'c4', w['id']))
        shutil.copy(spv, os.path.join(root, 'world', 'c4', w['id'], 'spine.json'))
        mp4 = os.path.join(segdir, f"{w['id']}-540.mp4")
        aud = os.path.join(segdir, f"{w['id']}-540{'.C' if v == 'C' else ''}.audio", 'stems')
        segs.append({'id': w['id'], 'mp4': mp4, 'f0': w['f0'], 'f1': w['f1'], 't0': w['t0'], 't1': w['t1'], 'scenes': w['scenes'],
                     'stems': aud, 'spine': json.load(open(spv))})
    blank = os.path.join(work, 'blank.mp4')
    n = round(TL['total'] * FPS)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', f'color=c=black:size=960x540:rate={FPS}', '-frames:v', str(n),
                    *SP.encode_args(ENC, FPS), blank], check=True)
    pic = os.path.join(work, 'picture.mp4')
    SP.splice_video(blank, segs, pic, FPS, ENC)
    stems = os.path.join(work, 'stems'); os.makedirs(stems)
    episode_voice(os.path.join(stems, 'voice.flac'))
    raw = os.path.join(work, 'mix-raw.wav')
    info = SP.merge_audio(stems, segs, TL['total'], raw, FPS)
    os.makedirs(os.path.join(root, 'out', 'audio', 'stems'))
    master = os.path.join(root, 'out', 'audio', 'master.wav')
    video = os.path.join(root, 'out', 'video.mp4')
    mux = lambda br: subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', pic, '-i', master, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                                     '-c:a', 'aac', '-b:a', br, '-ar', '48000', '-ac', '2', video], check=True)
    tries = []
    if aac_ceiling is None:
        g = loudnorm(raw, master)
    else:   # như build.py `audio.aac_true_peak` (F-18): master đích = trần − AAC_HEADROOM, AAC 384k, đo, vượt → hạ thêm
        sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
        import build as BUILD
        tgt = min(TP, aac_ceiling - BUILD.AAC_HEADROOM)
        for _ in range(3):
            g = loudnorm(raw, master, round(tgt, 2))
            mux('384k')
            got = BUILD.true_peak(video)
            tries.append({'master_tp_target': round(tgt, 2), 'master_tp': BUILD.true_peak(master), 'aac_tp': got})
            if got <= aac_ceiling:
                break
            tgt -= got - aac_ceiling + 0.05
    for f in os.listdir(stems):   # stem ở mức master (cùng hệ số loudnorm tuyến tính)
        x, _ = sf.read(os.path.join(stems, f), always_2d=True)
        sf.write(os.path.join(root, 'out', 'audio', 'stems', f.replace('.flac', '.wav')), (x * g).astype(np.float32), SR)
    for k in ('sonify',):
        pass
    if aac_ceiling is None:
        mux('320k')
    rec = {'aac_true_peak': {'ceiling': aac_ceiling, 'tries': tries} if tries else None, 'segments': [{k: s[k] for k in ('id', 'scenes', 't0', 't1', 'f0', 'f1')} for s in segs], 'audio': info,
           'picture': {'sha256': SP.sha_file(pic)}, 'master_wav_sha256': SP.sha_file(master)}
    json.dump(rec, open(os.path.join(root, 'out', 'factory', 'splice.json'), 'w'), indent=1, ensure_ascii=False)
    if info.get('joins'):
        SP.transitions(os.path.join(root, 'out', 'factory', 'splice.json'), os.path.join(root, 'out', 'transitions.json'))
    shutil.rmtree(work)
    print(json.dumps({'variant': v, 'aac_true_peak': rec['aac_true_peak'], 'joins': [(j['to'], j['cut'], j['t_picture']) for j in info.get('joins', [])],
                      'master_wav_sha256': rec['master_wav_sha256'][:16]}))


def small_frames(video):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', 'scale=96:54,format=gray', '-f', 'rawvideo', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(-1, 54, 96).astype(np.float32)


def cmd_av(ra, rb):
    sa, sb = (json.load(open(os.path.join(r, 'out', 'factory', 'splice.json'))) for r in (ra, rb))
    joins = sb['audio'].get('joins', [])
    a, b = small_frames(os.path.join(ra, 'out', 'video.mp4')), small_frames(os.path.join(rb, 'out', 'video.mp4'))
    zone = np.zeros(len(a), bool)
    for j in joins:
        zone[int(round(j['zone'][0] * FPS)):int(round(j['zone'][1] * FPS))] = True
    # khung ngoài vùng: lệch khung = độ dời k ∈ [−3, 3] làm khung B khớp A nhất (chỉ khung có chuyển động, để độ dời đo được)
    idx = [i for i in range(3, len(a) - 3) if not zone[i] and np.abs(a[i] - a[i - 1]).mean() > 0.5]
    sel = idx[::max(1, len(idx) // 3000)]
    offs = [int(np.argmin([np.abs(b[i + k] - a[i]).mean() for k in range(-3, 4)])) - 3 for i in sel]
    diff_out = np.abs(a[~zone] - b[~zone]).mean(axis=(1, 2))
    zinfo = []
    for j in joins:
        f0, f1 = int(round(j['zone'][0] * FPS)), int(round(j['zone'][1] * FPS))
        zinfo.append({'to': j['to'], 'cut': j['cut'], 'zone': j['zone'], 'frames': f1 - f0,
                      'frozen': bool(np.abs(np.diff(b[f0:f1], axis=0)).mean() < 0.05) if f1 - f0 > 1 else None,
                      'voice_lead_s': j['voice_lead']})
    rep = {'audio_identical': sa['master_wav_sha256'] == sb['master_wav_sha256'], 'frames': int(len(a)), 'zone_frames': int(zone.sum()),
           'moving_frames_checked': len(sel), 'offset_hist': {str(k): offs.count(k) for k in sorted(set(offs))},
           'max_abs_offset_frames': int(max(map(abs, offs))) if offs else None,
           'outside_zone_mean_abs_diff': {'mean': round(float(diff_out.mean()), 3), 'max': round(float(diff_out.max()), 3)}, 'zones': zinfo}
    print(json.dumps(rep, indent=1))
    return rep


def band(x, lo=1000, hi=4000):
    from scipy import signal
    return signal.sosfiltfilt(signal.butter(4, [lo, hi], 'band', fs=SR, output='sos'), x)


def pow100(x):
    n = len(x) // 4800
    return np.mean(x[:n * 4800].reshape(n, 4800) ** 2, axis=1)


def ebur(path, a=None, b=None):
    cut = (['-ss', str(a), '-to', str(b)] if a is not None else [])
    r = subprocess.run(['ffmpeg', '-hide_banner', *cut, '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
    t = r.stderr[r.stderr.rfind('Summary'):]
    return float(t.split('I:')[1].split('LUFS')[0]), float(t.split('Peak:')[1].split('dBFS')[0])


def cmd_metrics(root, a=None, b=None):
    st = os.path.join(root, 'out', 'audio', 'stems')
    S = {f[:-4]: sf.read(os.path.join(st, f), always_2d=True)[0].mean(1) for f in os.listdir(st)}
    if a is not None:
        S = {k: x[int(a * SR):int(b * SR)] for k, x in S.items()}
    v = S['voice']
    pv_full, pv = pow100(v), pow100(band(v))
    act = 10 * np.log10(pv_full + 1e-20) > -45
    def ratio(names):
        bg = sum(S[n] for n in names if n in S)
        pb = pow100(band(bg))
        pres = act & (10 * np.log10(pb + 1e-20) >= -80)
        r = 10 * np.log10(pv[pres] + 1e-20) - 10 * np.log10(pb[pres] + 1e-20)
        return {'p10_db': round(float(np.percentile(r, 10)), 1) if pres.any() else None, 'median_db': round(float(np.median(r)), 1) if pres.any() else None,
                'windows': int(pres.sum())}
    master = os.path.join(root, 'out', 'audio', 'master.wav')
    I, P = ebur(master, a, b)
    Ia, Pa = ebur(os.path.join(root, 'out', 'video.mp4'), a, b)
    sp = {}
    for seg in SEGS:
        s = json.load(open(os.path.join(root, 'world', 'c4', seg, 'spine.json')))
        t0 = next(w['t0'] for w in TL['world'] if w['id'] == seg)
        ev = [t0 + float(e['t']) for e in s['events'] if e['kind'] != 'data' and e['kind'] not in L.SFX_BEDS]
        if a is not None:
            ev = [t for t in ev if a <= t < b]
        sp[seg] = ev
    allev = sorted(t for v_ in sp.values() for t in v_)
    rep = {'window': [a, b], 'lufs_master_wav': I, 'peak_master_wav_dbfs': P, 'lufs_aac': Ia, 'peak_aac_dbfs': Pa,
           'voice_vs_sonify_1_4k (L1 a)': ratio(['sonify']), 'voice_vs_sfx_whoosh_1_4k': ratio(['sfx', 'whoosh']),
           'voice_vs_all_bed_1_4k': ratio(['music', 'sonify', 'sfx', 'whoosh', 'room']),
           'sfx_events': len(allev), 'sfx_max_in_10s': max((sum(1 for x in allev if t <= x < t + 10) for t in allev), default=0)}
    tp = subprocess.run(['ffmpeg', '-hide_banner', *(['-ss', str(a), '-to', str(b)] if a is not None else []), '-i', master, '-af',
                         'ebur128=peak=true:framelog=quiet', '-f', 'null', '-'], capture_output=True, text=True).stderr
    rep['true_peak_dbtp'] = float(tp[tp.rfind('True peak'):].split('Peak:')[1].split('dBFS')[0]) if 'True peak' in tp else None
    print(json.dumps(rep, indent=1, ensure_ascii=False))
    return rep


def cmd_clip(root, a, b, out):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(a), '-to', str(b), '-i', os.path.join(root, 'out', 'video.mp4'),
                    '-c:v', 'libx264', '-crf', '24', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', out], check=True)


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'spines':
        cmd_spines()
    elif c == 'audio':
        cmd_audio(sys.argv[2])
    elif c == 'build':
        cmd_build(sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[sys.argv.index('--aac-tp') + 1]) if '--aac-tp' in sys.argv else None)
    elif c == 'av':
        cmd_av(sys.argv[2], sys.argv[3])
    elif c == 'metrics':
        cmd_metrics(sys.argv[2], *(float(x) for x in sys.argv[3:5]))
    elif c == 'clip':
        cmd_clip(sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5])

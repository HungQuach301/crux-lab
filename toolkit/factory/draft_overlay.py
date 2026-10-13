"""F-15 (a) · đưa sản phẩm NHÁP (build.py --res N [--spp K]) vào chỗ chuẩn của một BẢN SAO tập để chạy checks đủ bộ (bộ lấy mẫu trang + luật Python).

  python3 toolkit/factory/draft_overlay.py <bản-sao>/episodes/epNNN rN[sK] [--src <repo>/episodes/epNNN]
  (checks_split.sh gọi khi DRAFT=rN: `DRAFT=r540 EP=episodes/epNNN bash toolkit/checks_split.sh <outdir>`)

Chỉ ghi vào bản sao (ngoài repo), không chạm repo. Nguồn: <src>/work/factory-<tag>/ và <src>/out/factory-<tag>/ (+ ep-out/).
  out/video.mp4           ← work/factory-<tag>/video.mp4 phóng 1920×1080 (lanczos, x264 crf 16, bt709), tiếng chép nguyên; cắt ở độ dài luồng hình
                            (như bước out của tập) — bộ lấy mẫu trang và luật đọc khung giả định 1920×1080
  out/audio/stems/*       ← work/factory-<tag>/stems/*
  out/camera.json, out/sonify-events.json, out/page.json ← out/factory-<tag>/ep-out/ (page.json trỏ work/factory-<tag>/page/index.html, cũng chép)
  out/factory/*           ← out/factory-<tag>/* (timeline có khoá world, splice, qc, build-report)
  out/shorts/SH*.mp4      ← work/factory-<tag>/SH*.mp4 (Short nháp đã phóng 1080×1920 khi ghép)
  work/factory/world      ← work/factory-<tag>/world (đoạn thế giới ở res nháp)
Các tệp out/* còn lại (script.json, timeline.json hợp đồng, claims, rights…) giữ bản của bản sao — đúng khi lời/timeline không đổi so bản đã ra
bằng bước out của tập; khác → in CẢNH BÁO (vòng sửa có đổi lời: chạy bước out của tập trước).
Luật đọc điểm ảnh (R_pix của f15/INTENT.md) chấm trên hình nháp phóng — phán quyết của chúng là của bản nháp, không thay bản 1080p.
"""
import json, os, shutil, subprocess, sys


def run(cmd):
    subprocess.run(cmd, check=True)


def copytree(a, b):
    if os.path.isdir(b) and not os.path.islink(b):
        shutil.rmtree(b)
    shutil.copytree(a, b)


def main():
    dst, tag = os.path.abspath(sys.argv[1]), sys.argv[2]
    src = os.path.abspath(sys.argv[sys.argv.index('--src') + 1]) if '--src' in sys.argv else dst
    DW, DO = os.path.join(src, 'work', f'factory-{tag}'), os.path.join(src, 'out', f'factory-{tag}')
    if not os.path.exists(os.path.join(DW, 'video.mp4')):
        raise SystemExit(f'draft_overlay: không thấy {DW}/video.mp4 (build.py --res … đã đạt chưa?)')
    rep = {'tag': tag, 'src': src}
    out = os.path.join(dst, 'out')
    os.makedirs(out, exist_ok=True)
    vd = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=duration', '-of', 'csv=p=0',
                         os.path.join(DW, 'video.mp4')], capture_output=True, text=True, check=True).stdout.strip()
    run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(DW, 'video.mp4'), '-map', '0:v', '-map', '0:a', '-vf',
         'scale=1920:1080:flags=lanczos:out_color_matrix=bt709:out_range=tv', '-c:v', 'libx264', '-preset', 'fast', '-crf', '16', '-pix_fmt', 'yuv420p',
         '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-c:a', 'copy', '-t', vd, '-movflags', '+faststart',
         os.path.join(out, 'video.mp4')])
    rep['video'] = {'from': os.path.join(DW, 'video.mp4'), 'scaled_to': '1920x1080', 'duration': vd}
    st = os.path.join(out, 'audio', 'stems')
    os.makedirs(st, exist_ok=True)
    for f in os.listdir(st):
        os.remove(os.path.join(st, f))
    for f in os.listdir(os.path.join(DW, 'stems')):
        shutil.copy(os.path.join(DW, 'stems', f), os.path.join(st, f))
    epo = os.path.join(DO, 'ep-out')
    for f in sorted(os.listdir(epo)) if os.path.isdir(epo) else []:
        shutil.copy(os.path.join(epo, f), os.path.join(out, f))
    if os.path.isdir(os.path.join(DW, 'page')):
        copytree(os.path.join(DW, 'page'), os.path.join(dst, 'work', f'factory-{tag}', 'page'))
    of = os.path.join(out, 'factory')
    os.makedirs(of, exist_ok=True)
    for f in sorted(os.listdir(DO)):
        if os.path.isfile(os.path.join(DO, f)):
            shutil.copy(os.path.join(DO, f), os.path.join(of, f))
    sh = sorted(f for f in os.listdir(DW) if f.startswith('SH') and f.endswith('.mp4') and '-' not in f)
    os.makedirs(os.path.join(out, 'shorts'), exist_ok=True)
    for f in sh:
        shutil.copy(os.path.join(DW, f), os.path.join(out, 'shorts', f))
    rep['shorts'] = sh
    if os.path.isdir(os.path.join(DW, 'world')):
        copytree(os.path.join(DW, 'world'), os.path.join(dst, 'work', 'factory', 'world'))
    # lời/timeline nháp so bản hợp đồng của bản sao
    warn = []
    ct = os.path.join(out, 'timeline.json')
    if os.path.exists(ct):
        C, D = json.load(open(ct)), json.load(open(os.path.join(DO, 'timeline.json')))
        dsc = {s['id']: (s['start'], s['dur']) for s in D['scenes']}
        for s in C['scenes']:
            if s['id'] in dsc and (abs(dsc[s['id']][0] - s['start']) > 1e-3):
                warn.append(f"cảnh {s['id']}: start {s['start']} (out/timeline.json) ≠ {dsc[s['id']][0]} (nháp)")
        if abs(C['total'] - D['total']) > 1e-3:
            warn.append(f"total {C['total']} ≠ {D['total']} (nháp) — chạy bước out của tập trên nháp trước khi tin checks")
    rep['warn'] = warn
    for w in warn:
        print('draft_overlay CẢNH BÁO:', w)
    json.dump(rep, open(os.path.join(of, 'draft-overlay.json'), 'w'), indent=1, ensure_ascii=False)
    print(f"draft_overlay: {tag} → {dst} (video phóng 1080, {len(sh)} Short, {len(warn)} cảnh báo)")


if __name__ == '__main__':
    main()

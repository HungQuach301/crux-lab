#!/usr/bin/env python3
"""Giao hàng một tập: mã hoá bản tải YouTube, chia phần 90 MB, SHA-256, lệnh ghép; tuỳ chọn commit lên nhánh tạm.

Bài học Tập 2 (`playbook/lessons.md` E11): bản gốc 1,78 GB, CRF 18 vẫn 1,43 GB; chat từ chối phần 477 MiB, lỗi 502
ở phần 150 MiB; tải được bằng phần 90 MB trên nhánh tạm. Không gửi qua chat.

Dùng:
  python3 toolkit/deliver/deliver.py episodes/ep003/out/video.mp4 --out episodes/ep003/work/delivery --name ep003
  # thêm --branch ep003-delivery để commit các phần lên nhánh mồ côi (worktree riêng, không chạm nhánh đang làm);
  # thêm --push để đẩy (git push -u origin ep003-delivery). Chủ dự án tải xong thì xoá nhánh.

Mã hoá: H.264 High, yuv420p, bitrate video theo khuyến nghị tải lên của YouTube (SDR): 2160p 35/53, 1440p 16/24,
1080p 8/12, 720p 5/7,5, 480p 2,5/4 Mb/s (≤ 30 fps / > 30 fps); maxrate 1,5×, bufsize 2×; GOP = nửa giây
(khuyến nghị "closed GOP, half the frame rate"); audio COPY (không mã hoá lại); +faststart.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile

PART = 90_000_000  # byte; < 100 MiB (giới hạn file của GitHub), đã tải được ở Tập 2
YT = [(2160, 35, 53), (1440, 16, 24), (1080, 8, 12), (720, 5, 7.5), (480, 2.5, 4), (0, 1, 1.5)]


def probe(video):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                        'stream=height,avg_frame_rate,r_frame_rate', '-of', 'json', video],
                       capture_output=True, check=True, text=True)
    s = json.loads(r.stdout)['streams'][0]
    for k in ('avg_frame_rate', 'r_frame_rate'):
        n, _, d = s.get(k, '0/0').partition('/')
        if float(n or 0) > 0 and float(d or 1) > 0:
            return int(s['height']), float(n) / float(d or 1)
    raise SystemExit(f'không đọc được fps của {video}')


def youtube_bitrate(height, fps):
    for h, lo, hi in YT:
        if height >= h:
            return hi if fps > 30.5 else lo
    raise AssertionError


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def encode(src, dst, preset='medium'):
    height, fps = probe(src)
    mbps = youtube_bitrate(height, fps)
    gop = max(1, round(fps / 2))
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', src, '-map', '0:v:0', '-map', '0:a?', '-c:v', 'libx264',
           '-preset', preset, '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-b:v', f'{mbps}M',
           '-maxrate', f'{mbps * 1.5}M', '-bufsize', f'{mbps * 2}M', '-g', str(gop), '-bf', '2',
           '-flags', '+cgop', '-c:a', 'copy', '-movflags', '+faststart', dst]
    subprocess.run(cmd, check=True)
    return {'height': height, 'fps': round(fps, 3), 'video_mbps': mbps, 'gop': gop, 'preset': preset}


def split(path, outdir, part=PART):
    base = os.path.basename(path)
    parts = []
    with open(path, 'rb') as f:
        i = 1
        while True:
            b = f.read(part)
            if not b:
                break
            p = os.path.join(outdir, f'{base}.part{i:02d}')
            with open(p, 'wb') as g:
                g.write(b)
            parts.append(p)
            i += 1
    return parts


def join_doc(name, parts, digest, info):
    ps = [os.path.basename(p) for p in parts]
    win = ' + '.join(ps)
    return f"""# Giao hàng {name}

File: `{name}` · {info['size']:,} byte · SHA-256 `{digest}`
Mã hoá: {info['height']}p {info['fps']} fps, video {info['video_mbps']} Mb/s (khuyến nghị YouTube), audio giữ nguyên bản gốc.
Bản gốc: SHA-256 `{info['source_sha256']}` (không lên git; lệnh dựng lại ở README của tập).

Tải mọi file `{name}.partNN` và `SHA256SUMS` vào cùng một thư mục, rồi:

**Windows (Command Prompt):**
```
copy /b {win} {name}
certutil -hashfile {name} SHA256
```

**Mac / Linux (Terminal):**
```
cat {name}.part* > {name}
shasum -a 256 {name}
```

Mã in ra phải là `{digest}`. Tải xong thì báo để xoá nhánh giao hàng.
"""


def branch_free(repo, branch, remote=True):
    """Dừng sớm (trước khi mã hoá) nếu nhánh đã có ở local hoặc trên origin."""
    git = lambda *a: subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True)
    if git('branch', '--list', branch).stdout.strip():
        sys.exit(f'nhánh {branch} đã có ở local: xoá hoặc chọn tên khác')
    if remote:
        r = git('ls-remote', '--heads', 'origin', branch)
        if r.returncode == 0 and r.stdout.strip():
            sys.exit(f'nhánh {branch} đã có trên origin: chủ dự án tải xong thì xoá, hoặc chọn tên khác')


def commit_branch(repo, branch, files, push=False, message=None):
    """Commit `files` lên nhánh mồ côi `branch` qua một worktree tạm; nhánh đang làm không đổi."""
    git = lambda *a, **k: subprocess.run(['git', '-C', repo, *a], check=True, capture_output=True, text=True, **k)
    branch_free(repo, branch, remote=False)
    wt = tempfile.mkdtemp(prefix='deliver-')
    ok = False
    try:
        git('worktree', 'add', '--detach', '--no-checkout', wt)
        w = lambda *a: subprocess.run(['git', '-C', wt, *a], check=True, capture_output=True, text=True)
        w('checkout', '--orphan', branch)
        w('rm', '-rf', '--cached', '--quiet', '--ignore-unmatch', '.')
        for f in files:
            shutil.copyfile(f, os.path.join(wt, os.path.basename(f)))
        w('add', '--', *[os.path.basename(f) for f in files])
        w('commit', '-q', '-m', message or f'{branch}: phần giao hàng (xoá nhánh sau khi tải)')
        sha = w('rev-parse', 'HEAD').stdout.strip()
        if push:
            for i, wait in enumerate([0, 2, 4, 8, 16]):
                if wait:
                    import time; time.sleep(wait)
                r = subprocess.run(['git', '-C', wt, 'push', '-u', 'origin', branch], capture_output=True, text=True)
                if r.returncode == 0:
                    break
            else:
                sys.exit(f'push thất bại: {r.stderr.strip()}')
        ok = True
        return sha
    finally:
        subprocess.run(['git', '-C', repo, 'worktree', 'remove', '--force', wt], capture_output=True)
        shutil.rmtree(wt, ignore_errors=True)
        if not ok:  # không để lại nhánh local chặn lần chạy sau
            subprocess.run(['git', '-C', repo, 'branch', '-D', branch], capture_output=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('video')
    ap.add_argument('--out', required=True)
    ap.add_argument('--name', required=True, help='tên tập, ví dụ ep003 → ep003-youtube.mp4')
    ap.add_argument('--preset', default='medium')
    ap.add_argument('--part-bytes', type=int, default=PART)
    ap.add_argument('--skip-encode', action='store_true', help='video đã là bản tải YouTube; chỉ chia phần')
    ap.add_argument('--branch'); ap.add_argument('--repo', default='.'); ap.add_argument('--push', action='store_true')
    a = ap.parse_args(argv)
    if a.branch:
        branch_free(os.path.abspath(a.repo), a.branch, remote=a.push)
    os.makedirs(a.out, exist_ok=True)
    name = f'{a.name}-youtube.mp4'
    up = os.path.join(a.out, name)
    if a.skip_encode:
        shutil.copyfile(a.video, up)
        h, fps = probe(up)
        info = {'height': h, 'fps': round(fps, 3), 'video_mbps': 'nguồn', 'gop': None, 'preset': None}
    else:
        info = encode(a.video, up, a.preset)
    info.update(size=os.path.getsize(up), source_sha256=sha256(a.video))
    digest = sha256(up)
    parts = split(up, a.out, a.part_bytes)
    sums = os.path.join(a.out, 'SHA256SUMS')
    with open(sums, 'w') as f:
        f.write(f'{digest}  {name}\n')
        for p in parts:
            f.write(f'{sha256(p)}  {os.path.basename(p)}\n')
    doc = os.path.join(a.out, 'JOIN.md')
    open(doc, 'w', encoding='utf-8').write(join_doc(name, parts, digest, info))
    rec = dict(info, file=name, sha256=digest, parts=[os.path.basename(p) for p in parts], part_bytes=a.part_bytes)
    json.dump(rec, open(os.path.join(a.out, 'delivery.json'), 'w'), indent=1)
    print(json.dumps(rec, indent=1))
    if a.branch:
        sha = commit_branch(os.path.abspath(a.repo), a.branch, parts + [sums, doc], a.push)
        print(f'nhánh {a.branch} @ {sha}' + (' (đã đẩy)' if a.push else ' (chưa đẩy)'))


if __name__ == '__main__':
    main()

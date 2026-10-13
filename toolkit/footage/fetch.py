"""F-15 (f) · TẢI TÀI SẢN NGOÀI (ảnh, video, bản đồ, dữ liệu hình) — tự ghi SHA-256 + dòng RIGHTS.md (URL, giấy phép NGUYÊN VĂN, ngày tải).

  python3 toolkit/footage/fetch.py <url> --id M-XXX --name "…" --kind ảnh|video|bản đồ --dest <thư mục> --scope "…" --credit "…"
          (--license-text "<trích nguyên văn>" --license-url <url> | --license-from-tar <tệp trong .tgz> --license-url <url>)
          [--loc] [--rights RIGHTS.md] [--no-rights]
  --loc   <url> là trang mục Library of Congress (https://www.loc.gov/item/… hoặc /pictures/item/…): đọc `?fo=json`, lấy NGUYÊN VĂN
          `rights_advisory` / `rights` của mục làm giấy phép (chỉ nhận khi có "No known restrictions"), tải ảnh lớn nhất của mục.
Ra: <dest>/<tệp> + <dest>/<tệp>.source.json {id, url, file_url, sha256, bytes, date, license_text, license_url, scope, credit}
và MỘT dòng mới ở bảng chính của RIGHTS.md (trước "## Tham chiếu"; mã đã có → không thêm, báo). Tài sản không có giấy phép nguyên văn → dừng,
không tải (CHARTER §5: chưa trích nguyên văn = chưa được dùng). Tệp tải là dữ liệu không tin cậy: chỉ đọc bằng mã của dự án (`python3 -I`).
"""
import argparse, datetime, hashlib, io, json, os, re, subprocess, sys, tarfile, urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
UA = 'crux-lab-footage/1.0 (+https://github.com/hungquach301/crux-lab)'


def get(url, timeout=120):
    r = subprocess.run(['curl', '-sS', '-L', '--fail', '-m', str(timeout), '-A', UA, url], capture_output=True)
    if r.returncode:
        raise SystemExit(f'fetch: tải {url} trượt (curl {r.returncode}): {r.stderr.decode(errors="replace").strip()[:200]}')
    return r.stdout


def loc_item(url):
    """Mục LoC → (url ảnh lớn nhất, nguyên văn quyền, tiêu đề)."""
    j = json.loads(get(url.split('?')[0].rstrip('/') + '/?fo=json'))
    item = j.get('item') or {}
    rights = item.get('rights_advisory') or item.get('rights') or j.get('rights') or ''
    rights = ' '.join(rights) if isinstance(rights, list) else str(rights)
    if 'no known restrictions' not in rights.lower():
        raise SystemExit(f'fetch --loc: quyền của mục không phải "No known restrictions": {rights[:200]!r} — không tải')
    urls = []
    for r in j.get('resources') or []:
        for f in (r.get('files') or []):
            for x in (f if isinstance(f, list) else [f]):
                if isinstance(x, dict) and str(x.get('mimetype', '')).startswith('image/jpeg') and x.get('url'):
                    urls.append((int(x.get('width') or 0) * int(x.get('height') or 0), x['url']))
    urls += [(0, u) for u in (item.get('image_url') or j.get('image_url') or [])]
    if not urls:
        raise SystemExit('fetch --loc: mục không có ảnh JPEG')
    best = sorted(urls, key=lambda x: x[0])[-1][1]
    return urllib.parse.urljoin('https://www.loc.gov/', best), rights.strip(), item.get('title') or j.get('title') or ''


def rights_row(a):
    cell = lambda s: str(s).replace('|', '\\|').replace('\n', ' ')
    return (f"| {a['id']} | {cell(a['name'])} | {cell(a['kind'])} | {a['url']} | \"{cell(a['license_text'])}\" — {a['license_url']} "
            f"(SHA-256 `{a['sha256'][:16]}…`, `{a['file']}`) | {cell(a['scope'])} | {cell(a['credit'])} | {a['date']} |")


def add_rights(path, a):
    src = open(path).read()
    if re.search(rf"^\| {re.escape(a['id'])} \|", src, re.M):
        print(f"fetch: RIGHTS.md đã có mã {a['id']} — không thêm dòng")
        return False
    lines = src.split('\n')
    cut = next((i for i, l in enumerate(lines) if l.startswith('## Tham chiếu')), len(lines))
    last = max(i for i in range(cut) if lines[i].startswith('| '))   # dòng cuối của bảng chính
    lines.insert(last + 1, rights_row(a))
    open(path, 'w').write('\n'.join(lines))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('url'); ap.add_argument('--id', required=True); ap.add_argument('--name', required=True); ap.add_argument('--kind', required=True)
    ap.add_argument('--dest', required=True); ap.add_argument('--scope', required=True); ap.add_argument('--credit', required=True)
    ap.add_argument('--license-text'); ap.add_argument('--license-url'); ap.add_argument('--license-from-tar'); ap.add_argument('--loc', action='store_true')
    ap.add_argument('--rights', default=os.path.join(ROOT, 'RIGHTS.md')); ap.add_argument('--no-rights', action='store_true')
    a = ap.parse_args()
    file_url, lic, lic_url = a.url, a.license_text, a.license_url
    if a.loc:
        file_url, lic, title = loc_item(a.url)
        lic_url = lic_url or a.url
        a.name = a.name or title
    if not (lic or a.license_from_tar) or not lic_url:
        raise SystemExit('fetch: thiếu giấy phép NGUYÊN VĂN (--license-text/--license-from-tar/--loc) hoặc --license-url — không tải')
    body = get(file_url)
    if a.license_from_tar:
        with tarfile.open(fileobj=io.BytesIO(body), mode='r:gz') as tf:
            lic = tf.extractfile(a.license_from_tar).read().decode().strip()
    os.makedirs(a.dest, exist_ok=True)
    name = os.path.basename(urllib.parse.urlparse(file_url).path) or 'asset'
    out = os.path.join(a.dest, name)
    open(out, 'wb').write(body)
    rec = {'id': a.id, 'name': a.name, 'kind': a.kind, 'url': a.url, 'file_url': file_url, 'file': os.path.relpath(out, ROOT),
           'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body), 'date': datetime.date.today().isoformat(),
           'license_text': lic, 'license_url': lic_url, 'scope': a.scope, 'credit': a.credit}
    json.dump(rec, open(out + '.source.json', 'w'), indent=1, ensure_ascii=False)
    added = False if a.no_rights else add_rights(a.rights, rec)
    print(json.dumps({k: rec[k] for k in ('id', 'file', 'sha256', 'bytes', 'date')} | {'rights_row': added}, ensure_ascii=False))


if __name__ == '__main__':
    main()

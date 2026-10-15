"""F-18 (D-013 2b, RIGHTS §G; bổ sung chủ dự án 15/10) · SFX GHI ÂM THẬT — tải, kiểm giấy phép TỪNG TỆP, manifest SHA-256, kiểm lúc dựng.

  python3 toolkit/factory/world/sfx/sfx_fetch.py [--only S-…] [--rights]            nguồn tải được (Kenney, OpenGameArt) theo picks.json
  python3 toolkit/factory/world/sfx/sfx_fetch.py --verify                           lúc dựng: mọi tệp manifest có mặt + SHA-256 khớp (thiếu tệp
                                                                                    không commit → tải lại từ nguồn của nó / báo cần zip Sonniss)
  python3 toolkit/factory/world/sfx/sfx_fetch.py --sonniss-license <zip>            đọc NGUYÊN VĂN license trong gói, SHA-256 tệp license, 4 điểm
  python3 toolkit/factory/world/sfx/sfx_fetch.py --sonniss <zip> --pack "<tên gói>" --version "<năm/phiên bản>" [--keep-zip]
                                                                                    lấy CHỈ các mục `source: sonniss` của picks khớp gói này

Nguồn:
  NGUỒN MẶC ĐỊNH = CC0 đã kiểm từng tệp (kenney, oga). Chủ dự án 15/10 (merge F-18): Sonniss bỏ khỏi đường mặc định — CHƯA DÙNG.
  sonniss   TẮT (SONNISS_ENABLED = False; --sonniss / --sonniss-license từ chối). Mã giữ để bật sau khi chủ dự án quyết lại.
            Sonniss GDC Game Audio Bundle, zip theo nhà phát hành. Trang tải (sonniss.com) đứng sau Cloudflare
            "Just a moment…" — máy không qua được (15/10, F-18 REPORT) → chủ dự án tải zip bằng trình duyệt rồi đưa đường dẫn. Trước khi lấy tệp:
            `sonniss-license.json` (cạnh tệp này) phải có 4 điểm đã xác nhận từ license NGUYÊN VĂN (dùng thương mại trong video; cần ghi công
            không; cấm huấn luyện AI; có cho phân phối lại tệp thô không). commercial_video ≠ true → DỪNG. raw_redistribution ≠ true → tệp
            KHÔNG commit (repo công khai): chỉ manifest + SHA-256, tệp ở bộ nhớ đệm ngoài git (CRUX_SFX_CACHE, mặc định /var/tmp/crux-sfx).
            `df` kiểm trước mỗi zip (cần ≥ 2 × zip + 1 GB trống); giải nén CHỈ tệp trong picks; WAV/FLAC ≤ 48 kHz, ≤ 30 s; xoá zip sau khi lấy.
  kenney    gói CC0 kenney.nl (`License.txt` TRONG zip, trích nguyên văn); oga  trang tệp OpenGameArt (ô License(s): chỉ CC0 · CC-BY 4.0 · 3.0).
            Hai nguồn này là CC0 tải không cần tài khoản — dùng cho bản thử Tập 7 khi chưa có zip Sonniss.
  elevenlabs  ElevenLabs Sound Effects: TẮT (cờ episode `sfx.elevenlabs: false` mặc định). Chỉ có đường gọi viết sẵn: bật sau này → sinh MỘT lần,
            lưu cache theo SHA-256 (văn bản + thời lượng + tham số), trần ≤ 3.000 credit/tập, đọc /v1/user/subscription trước và sau để ghi credit thật.
  Freesound: KHÔNG dùng (chủ dự án 15/10: điều khoản API — dùng thương mại phải thương lượng với UPF). Không có mã gọi Freesound.
Từ chối tệp có dấu hiệu âm sinh bằng AI trên trang (AI_WORDS). Tệp tải là dữ liệu không tin cậy: thư mục tạm riêng, chỉ đọc bằng ffmpeg/zipfile.
Manifest (`manifest.json`): id, nguồn, gói, phiên bản, URL/đường dẫn trong zip, tác giả, giấy phép + TRÍCH NGUYÊN VĂN, SHA-256 gốc và tệp thư viện,
thời lượng, nhãn (`tags`, danh mục cảnh — sfx_labels.py), commit có/không.
"""
import argparse, datetime, hashlib, html, io, json, os, re, shutil, subprocess, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
LIB, MANIFEST, PICKS = os.path.join(HERE, 'lib'), os.path.join(HERE, 'manifest.json'), os.path.join(HERE, 'picks.json')
SONNISS_LICENSE = os.path.join(HERE, 'sonniss-license.json')
CACHE = os.environ.get('CRUX_SFX_CACHE', '/var/tmp/crux-sfx')
UA = 'crux-lab-sfx/1.0 (+https://github.com/hungquach301/crux-lab)'
MAX_BYTES = 2 * 1024 * 1024
MAX_S = 30.0
SR = 48000
CATEGORIES = {   # danh mục cảnh của lệnh 15/10 → nhãn (tags) dùng trong picks/manifest và sfx_labels.SCENE_LABELS
    'pho': 'phố / xe cộ nền', 'dam-dong': 'đám đông xa', 'ngan-hang': 'ngân hàng / sảnh', 'giay': 'giấy / lật sổ', 'tien-xu': 'tiền xu',
    'may-chu': 'máy chữ', 'dong-ho': 'đồng hồ', 'cua': 'cửa', 'chuyen-canh': 'tiếng chuyển cảnh nhẹ',
    'go-nhe': 'gõ gỗ nhẹ (dấu nhấn chung)', 'va-mem': 'va mềm (chạm khi máy tới)'}
OK_LICENSES = {'CC0 1.0': r'creativecommons\.org/publicdomain/zero/1\.0', 'CC BY 4.0': r'creativecommons\.org/licenses/by/4\.0',
               'CC BY 3.0': r'creativecommons\.org/licenses/by/3\.0'}
BANNED = r'by-nc|by-sa|by-nd|sampling\+|nc-|noncommercial|gpl|oga-by'
AI_WORDS = r'\b(ai[- ]generated|generated (?:with|by) ai|elevenlabs|suno|udio|stable audio|audiogen|musicgen|text[- ]to[- ](?:audio|sound))\b'
EL_CREDIT_CAP = 3000


def get(url, timeout=120, headers=()):
    cmd = ['curl', '-sS', '-L', '--fail', '-m', str(timeout), '-A', UA]
    for h in headers:
        cmd += ['-H', h]
    r = subprocess.run(cmd + [url], capture_output=True)
    if r.returncode:
        raise SystemExit(f'sfx_fetch: tải {url.split("?")[0]} trượt (curl {r.returncode}): {r.stderr.decode(errors="replace").strip()[:160]}')
    return r.stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


def sha_path(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def license_name(url):
    u = url.lower()
    if re.search(BANNED, u):
        return None
    return next((k for k, rx in OK_LICENSES.items() if re.search(rx, u)), None)


def text_of(h):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h))).strip()


def field(h, name):
    """Ô Drupal `field-name-<name>` của OpenGameArt → HTML bên trong ô (tới ô kế)."""
    i = h.find(f'field-name-{name}')
    if i < 0:
        return ''
    i = h.find('>', i) + 1
    j = h.find('class="field field-name-', i)
    j = h.rfind('<', i, j) if j > 0 else i + 4000
    return h[i:j]


# ---------------------------------------------------------------- nguồn tải được (CC0)
def src_kenney(p):
    page = get(p['page']).decode('utf-8', 'replace')
    m = re.search(r"https://kenney\.nl/media/pages/assets/[^'\"]+\.zip", page)
    if not m:
        raise SystemExit(f"sfx_fetch {p['id']}: không thấy link zip trên {p['page']}")
    blob = get(m.group(0))
    z = zipfile.ZipFile(io.BytesIO(blob))
    lic = next((n for n in z.namelist() if re.search(r'licen[cs]e\.txt$', n, re.I)), None)
    if not lic:
        raise SystemExit(f"sfx_fetch {p['id']}: gói không có License.txt — không dùng")
    lt = z.read(lic).decode('utf-8', 'replace')
    m2 = re.search(r'https?://creativecommons\.org/\S+', lt)
    if license_name(m2.group(0) if m2 else '') != 'CC0 1.0':
        raise SystemExit(f"sfx_fetch {p['id']}: License.txt không phải CC0 — từ chối")
    if re.search(AI_WORDS, page + lt, re.I):
        raise SystemExit(f"sfx_fetch {p['id']}: trang/giấy phép nhắc âm sinh bằng AI — từ chối")
    verb = ' '.join(l.strip() for l in lt.splitlines() if re.search(r'licen|creativecommons|free to use|credit', l, re.I))
    pack = text_of((re.search(r'^\s*(\S.*\(\d[\d.]*\))\s*$', lt, re.M) or ['', ''])[1]) or os.path.basename(m.group(0))
    return z.read(p['member']), {'file_url': m.group(0), 'pack': pack, 'author': 'Kenney (www.kenney.nl)', 'license': 'CC0 1.0',
                                  'license_url': 'https://creativecommons.org/publicdomain/zero/1.0/',
                                  'license_verbatim': f'{os.path.basename(lic)} trong gói: "{verb}"', 'pack_sha256': sha(blob), 'title': p['member']}


def src_oga(p):
    page = get(p['page']).decode('utf-8', 'replace')
    lic = field(page, 'field-art-licenses')
    urls = [a or b for a, b in re.findall(r"href='([^']+)'|href=\"([^\"]+)\"", lic)]
    names = [license_name(u) for u in urls]
    shown = text_of(lic).replace('License(s):', '').strip()
    if not urls or any(n is None for n in names):
        raise SystemExit(f"sfx_fetch {p['id']}: giấy phép trang tệp = {shown!r} — ngoài CC0/CC BY, từ chối")
    author = text_of(field(page, 'author-submitter')).replace('Author:', '').strip()
    body = text_of(field(page, 'body'))
    if re.search(AI_WORDS, body, re.I):
        raise SystemExit(f"sfx_fetch {p['id']}: mô tả nhắc âm sinh bằng AI — từ chối")
    files = re.findall(r'href="(https://opengameart\.org/sites/default/files/[^"]+)"[^>]*download="([^"]+)"', field(page, 'field-art-files'))
    url = next((u for u, n in files if n == p.get('file') or os.path.basename(u) == p.get('file')), files[0][0] if len(files) == 1 else None)
    if not url:
        raise SystemExit(f"sfx_fetch {p['id']}: không thấy tệp {p.get('file')!r} trong ô File(s) ({[n for _, n in files]})")
    blob = get(url)
    raw, extra = blob, {}
    if url.endswith('.zip'):
        raw, extra = zipfile.ZipFile(io.BytesIO(blob)).read(p['member']), {'pack_sha256': sha(blob)}
    title = text_of((re.search(r'<title>(.*?)</title>', page, re.S) or ['', ''])[1]).split('|')[0].strip()
    return raw, {'file_url': url, 'pack': f'OpenGameArt "{title}"', 'author': author, 'license': names[0], 'license_url': urls[0],
                 'license_verbatim': f'OpenGameArt "{title}" — License(s): "{shown}" ({urls[0]}); mô tả: "{body[:200]}"', 'title': title, **extra}


def src_elevenlabs(p, ep_cfg=None):
    """ElevenLabs Sound Effects — TẮT. Chỉ chạy khi episode.yaml khai `sfx: {elevenlabs: true}` (truyền vào ep_cfg). Bật: sinh MỘT lần (cache
    theo SHA-256 của văn bản + thời lượng + prompt_influence), trần EL_CREDIT_CAP credit/tập, đọc subscription trước/sau để ghi credit thật.
    Phiên F-18 KHÔNG gọi API (chủ dự án 15/10)."""
    if not (ep_cfg or {}).get('elevenlabs', False):
        raise SystemExit(f"sfx_fetch {p['id']}: ElevenLabs Sound Effects đang TẮT (sfx.elevenlabs: false) — dùng Sonniss/CC0")
    key = hashlib.sha256(json.dumps({k: p.get(k) for k in ('text', 'duration_seconds', 'prompt_influence')}, sort_keys=True).encode()).hexdigest()
    cached = os.path.join(CACHE, 'elevenlabs', key + '.mp3')
    meta = {'pack': 'ElevenLabs Sound Effects', 'author': 'ElevenLabs (sinh theo văn bản của dự án)', 'license': 'ElevenLabs ToS (gói trả phí)',
            'license_url': 'https://elevenlabs.io/terms-of-use', 'license_verbatim': 'xem RIGHTS V-ERIC (ToS ElevenLabs, gói Creator trả phí)',
            'file_url': f'cache:{key}', 'title': p.get('text')}
    if os.path.exists(cached):
        return open(cached, 'rb').read(), meta
    used = (ep_cfg or {}).get('credits_used', 0)
    est = 40 * float(p.get('duration_seconds') or 5)   # ước lượng trước khi gọi; số thật = chênh subscription trước/sau
    if used + est > EL_CREDIT_CAP:
        raise SystemExit(f"sfx_fetch {p['id']}: vượt trần {EL_CREDIT_CAP} credit/tập ({used} + ~{est:.0f})")
    sub = lambda: json.loads(get('https://api.elevenlabs.io/v1/user/subscription'))['character_count']   # proxy tiêm khoá; không in khoá
    before = sub()
    body = json.dumps({'text': p['text'], 'duration_seconds': p.get('duration_seconds'), 'prompt_influence': p.get('prompt_influence', 0.3)})
    r = subprocess.run(['curl', '-sS', '--fail', '-m', '120', '-X', 'POST', 'https://api.elevenlabs.io/v1/sound-generation',
                        '-H', 'Content-Type: application/json', '-d', body], capture_output=True)
    if r.returncode:
        raise SystemExit(f"sfx_fetch {p['id']}: ElevenLabs sound-generation trượt (curl {r.returncode})")
    after = sub()
    os.makedirs(os.path.dirname(cached), exist_ok=True)
    open(cached, 'wb').write(r.stdout)
    meta['credits'] = after - before
    return r.stdout, meta


# ---------------------------------------------------------------- Sonniss (zip do chủ dự án tải bằng trình duyệt)
SONNISS_ENABLED = False   # chủ dự án 15/10: Cloudflare chặn máy, không vượt → Sonniss chưa dùng; bật lại chỉ theo quyết định mới
LICENSE_POINTS = ('commercial_video', 'attribution_required', 'ai_training_prohibited', 'raw_redistribution')


def sonniss_license(zp):
    """In NGUYÊN VĂN mọi tệp license/EULA trong zip + SHA-256 từng tệp; gợi ý 4 điểm theo câu chữ (người xác nhận ghi vào sonniss-license.json)."""
    z = zipfile.ZipFile(zp)
    names = [n for n in z.namelist() if re.search(r'licen[cs]e|eula|terms', os.path.basename(n), re.I)]
    if not names:
        raise SystemExit('sonniss: zip không có tệp license/EULA — DỪNG (không dùng gói không có license nguyên văn)')
    out = []
    for n in names:
        b = z.read(n)
        if n.lower().endswith('.pdf'):
            with tempfile.TemporaryDirectory() as t:
                pf = os.path.join(t, 'l.pdf'); open(pf, 'wb').write(b)
                txt = subprocess.run(['pdftotext', '-layout', pf, '-'], capture_output=True, text=True, check=True).stdout
        else:
            txt = b.decode('utf-8', 'replace')
        low = txt.lower()
        hint = {'commercial_video': bool(re.search(r'commercial', low)) and not re.search(r'non-?commercial use only', low),
                'attribution_required': not re.search(r'(no|without) (attribution|credit)', low),
                'ai_training_prohibited': bool(re.search(r'(machine learning|artificial intelligence|\bai\b).{0,120}(prohibit|not permitted|may not)|'
                                                         r'(prohibit|not permitted|may not).{0,120}(machine learning|artificial intelligence|\bai\b)', low, re.S)),
                'raw_redistribution': not re.search(r'(redistribut|resell|sublicens|share).{0,80}(not|prohibit)|(not|prohibit|may not).{0,80}(redistribut|resell|sublicens)', low, re.S)}
        out.append({'file': n, 'sha256': sha(b), 'text': txt, 'hint': hint})
    return out


def sonniss_gate():
    if not os.path.exists(SONNISS_LICENSE):
        raise SystemExit(f'sonniss: chưa có {os.path.relpath(SONNISS_LICENSE, ROOT)} (4 điểm xác nhận từ license nguyên văn) — chạy --sonniss-license trước')
    L = json.load(open(SONNISS_LICENSE))
    miss = [k for k in LICENSE_POINTS if not isinstance(L.get(k), bool)]
    if miss:
        raise SystemExit(f'sonniss: sonniss-license.json thiếu điểm {miss}')
    if not L['commercial_video']:
        raise SystemExit('sonniss: license KHÔNG cho dùng trong video thương mại — DỪNG mục SFX, báo chủ dự án')
    return L


def disk_ok(need):
    free = shutil.disk_usage(ROOT).free
    if free < need:
        raise SystemExit(f'sonniss: đĩa trống {free / 1e9:.1f} GB < cần {need / 1e9:.1f} GB — dừng trước khi tải/giải nén')
    return free


def src_sonniss(p, zp, pack, version):
    raw = zipfile.ZipFile(zp).read(p['member'])
    L = json.load(open(SONNISS_LICENSE))
    return raw, {'file_url': f"zip:{os.path.basename(zp)}", 'pack': pack, 'version': version, 'author': p.get('publisher', 'Sonniss GDC bundle'),
                 'license': f"Sonniss GDC {version} license", 'license_url': L.get('url', ''),
                 'license_verbatim': f"license trong gói ({L.get('license_file')}, SHA-256 {L.get('license_sha256')}) — RIGHTS §G2",
                 'title': os.path.basename(p['member']), 'commit': bool(L['raw_redistribution'])}


SOURCES = {'kenney': src_kenney, 'oga': src_oga, 'elevenlabs': src_elevenlabs}


# ---------------------------------------------------------------- thư viện
def lib_path(rec_or_pick, commit=True):
    d = LIB if commit else os.path.join(CACHE, 'lib')
    return os.path.join(d, rec_or_pick['id'] + '.flac')


def resolve(rec):
    """Đường tệp thư viện của một bản ghi manifest (commit → trong repo; không → bộ nhớ đệm), SHA-256 phải khớp; không thì SystemExit."""
    p = os.path.join(ROOT, rec['file']) if rec.get('commit', True) else lib_path(rec, False)
    if not os.path.exists(p):
        raise SystemExit(f"sfx: thiếu {rec['id']} ({p}) — `sfx_fetch.py --verify` (Sonniss: cần zip {rec.get('pack')})")
    if sha_path(p) != rec['sha256']:
        raise SystemExit(f"sfx: {rec['id']} SHA-256 không khớp manifest")
    return p


def to_lib(raw, p, tmp, commit=True):
    """Byte gốc (không tin cậy) → FLAC mono 24 bit, ≤ 48 kHz (giữ SR gốc nếu thấp hơn thì nâng 48 k cho đồng nhất), ≤ 30 s, tất định."""
    src = os.path.join(tmp, 'src.bin')
    open(src, 'wb').write(raw)
    dst = lib_path(p, commit)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    a, b = (p.get('trim') or [0, MAX_S])
    b = min(float(b), float(a) + MAX_S)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-to', str(b), '-i', src, '-map_metadata', '-1', '-fflags', '+bitexact',
                    '-flags:a', '+bitexact', '-ac', '1', '-ar', str(SR), '-sample_fmt', 's32', '-bits_per_raw_sample', '24', '-c:a', 'flac', dst],
                   check=True)
    if commit and os.path.getsize(dst) > MAX_BYTES:
        os.remove(dst)
        raise SystemExit(f"sfx_fetch {p['id']}: tệp thư viện > 2 MB — khai `trim` trong picks")
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', dst], capture_output=True, text=True)
    return dst, float(r.stdout.strip())


def record(p, raw, meta, dst, dur, man):
    commit = meta.pop('commit', True)
    rec = {'id': p['id'], 'tags': p.get('tags', []), 'kinds': p.get('kinds', []), 'source': p['source'], 'page': p.get('page'), **meta,
           'member': p.get('member'), 'trim': p.get('trim'), 'sha256_source': sha(raw), 'bytes_source': len(raw),
           'file': os.path.relpath(dst, ROOT) if commit else f"$CRUX_SFX_CACHE/lib/{p['id']}.flac", 'commit': commit,
           'sha256': sha_path(dst), 'bytes': os.path.getsize(dst), 'dur': round(dur, 3), 'date': datetime.date.today().isoformat(),
           'credit': p.get('credit') or f"{meta.get('title') or p['id']} by {meta['author']} ({meta['license']})",
           'credit_required': str(meta['license']).startswith('CC BY')}
    old = man.get(p['id'])
    if old and old.get('sha256_source') != rec['sha256_source']:
        raise SystemExit(f"sfx_fetch {p['id']}: bản tải mới khác SHA-256 bản trong manifest — dừng, xét tay")
    if old:
        rec['date'] = old['date']
    man[p['id']] = rec
    return rec


def fetch(p, man):
    with tempfile.TemporaryDirectory() as tmp:
        raw, meta = SOURCES[p['source']](p)
        dst, dur = to_lib(raw, p, tmp)
    return record(p, raw, meta, dst, dur, man)


def sonniss_take(zp, pack, version, picks, man, keep_zip=False):
    if not SONNISS_ENABLED:
        raise SystemExit('sonniss: TẮT (SONNISS_ENABLED = False, chủ dự án 15/10)')
    """Lấy các mục picks của gói `pack` từ zip. Cổng: 4 điểm đã xác nhận VÀ SHA-256 tệp license trong CHÍNH zip này = `license_sha256` đã xác
    nhận (xác nhận gói năm X không mở cổng cho zip năm Y). Từ chối (cổng, thiếu tệp) → dừng TRƯỚC khi giải nén, zip giữ nguyên để người xét."""
    L = sonniss_gate()
    shas = {x['sha256'] for x in sonniss_license(zp)}
    if L.get('license_sha256') not in shas:
        raise SystemExit(f"sonniss: license trong {os.path.basename(zp)} (SHA-256 {sorted(shas)}) khác license đã xác nhận "
                         f"({L.get('license_sha256')}) — đọc lại bằng --sonniss-license, xác nhận 4 điểm cho license này")
    disk_ok(int(2 * os.path.getsize(zp) + 1e9))
    names = set(zipfile.ZipFile(zp).namelist())
    mine = [p for p in picks if p['source'] == 'sonniss' and p.get('pack') == pack]
    miss = [p['member'] for p in mine if p['member'] not in names]
    if miss:
        raise SystemExit(f"sonniss: không có {miss} trong {os.path.basename(zp)} — không giải nén gì")
    got = []
    for p in mine:
        with tempfile.TemporaryDirectory() as tmp:
            raw, meta = src_sonniss(p, zp, pack, version)
            dst, dur = to_lib(raw, p, tmp, commit=bool(L['raw_redistribution']))
        got.append(record(p, raw, meta, dst, dur, man))
    if not keep_zip:
        os.remove(zp)
    return got


def verify(man):
    bad = []
    for r in man.values():
        try:
            resolve(r)
        except SystemExit as e:
            if r['source'] in SOURCES and r['source'] != 'elevenlabs' and r.get('commit', True) is False:
                fetch({k: r.get(k) for k in ('id', 'source', 'page', 'member', 'trim', 'tags', 'kinds')}, man)
            else:
                bad.append(str(e))
    return bad


def rights_rows(man):
    cell = lambda s: str(s).replace('|', '\\|').replace('\n', ' ')
    return [f"| {r['id']} | `{r['file']}` ({cell(r.get('title') or r.get('member') or '')}; nhãn {', '.join(r.get('tags') or [])}) | "
            f"{r.get('page') or ''} · {cell(r['file_url'])} | {cell(r['author'])} | {r['license']} | {cell(r['license_verbatim'])} — {r['license_url']} | "
            f"{r['date']} | `{r['sha256_source']}` (gốc) · `{r['sha256']}` (thư viện) | "
            f"{'BẮT BUỘC trong mô tả tập: ' + cell(r['credit']) if r['credit_required'] else 'không bắt buộc'} |" for r in man.values()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--picks', default=PICKS)
    ap.add_argument('--only', default='')
    ap.add_argument('--rights', action='store_true')
    ap.add_argument('--verify', action='store_true')
    ap.add_argument('--sonniss-license')
    ap.add_argument('--sonniss')
    ap.add_argument('--pack')
    ap.add_argument('--version')
    ap.add_argument('--keep-zip', action='store_true')
    a = ap.parse_args()
    man = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    if (a.sonniss_license or a.sonniss) and not SONNISS_ENABLED:
        raise SystemExit('sfx_fetch: Sonniss TẮT (chủ dự án 15/10: chưa dùng; nguồn SFX = CC0 đã kiểm từng tệp) — xem RIGHTS §G2')
    if a.sonniss_license:
        for L in sonniss_license(a.sonniss_license):
            print(f"===== {L['file']}  SHA-256 {L['sha256']}\n{L['text']}\n===== gợi ý theo câu chữ (NGƯỜI xác nhận): {json.dumps(L['hint'])}")
        return
    picks = json.load(open(a.picks))['picks']
    if a.sonniss:
        got = sonniss_take(a.sonniss, a.pack, a.version, picks, man, a.keep_zip)
        print(f'sonniss: {len(got)} tệp từ {a.pack} {a.version}')
    elif a.verify:
        bad = verify(man)
        print('\n'.join(bad) or f'sfx: {len(man)} tệp có mặt, SHA-256 khớp')
        if bad:
            sys.exit(1)
    else:
        only = {x for x in a.only.split(',') if x}
        for p in picks:
            if (only and p['id'] not in only) or p['source'] not in SOURCES or p['source'] == 'elevenlabs':
                continue
            if p['id'] in man and os.path.exists(lib_path(p)) and sha_path(lib_path(p)) == man[p['id']]['sha256']:
                man[p['id']]['tags'] = p.get('tags', [])
                man[p['id']]['kinds'] = p.get('kinds', [])
                print(f"{p['id']}: có sẵn, SHA khớp"); continue
            r = fetch(p, man)
            print(f"{r['id']}: {r['license']} · {r['author']} · {r['dur']} s · {r['bytes']} B · {r['sha256'][:12]}…")
    json.dump(dict(sorted(man.items())), open(MANIFEST, 'w'), indent=1, ensure_ascii=False)
    if a.rights:
        print('\n'.join(rights_rows(dict(sorted(man.items())))))


if __name__ == '__main__':
    main()

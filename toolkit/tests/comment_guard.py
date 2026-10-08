"""Chặn mã bị chú thích nuốt + mã cảnh thế giới hỏng cú pháp, chạy ĐẦU mỗi build (tổng kết Tập 5 mục 13; cine-lab BAI-HOC-LL #42, #76).
cine-lab #42/#76: chú thích `//` / `#` chèn bằng sed/str.replace vào GIỮA dòng nuốt phần mã còn lại — lần 3 không lỗi cú pháp (người
đứng ở gốc toạ độ, không ai thấy). Crux đã có `world/lint_comments.py` (F-4) nhưng mặc định chỉ quét một tầng `episodes/*/world/*`
(bỏ sót `world/c4/*`, `world/c3/*`) và chỉ một số mẫu lệnh. Tệp này:
  1. quét ĐỆ QUY mọi mã thế giới: toolkit/factory/world, moc-v/seg/**, episodes/*/world/** (bỏ vendor/, node_modules/, work/);
  2. `lint_comments` + mẫu mở rộng: sau `//` có gán thuộc tính (`a.b = …`), lời gọi kết thúc bằng `;`, hoặc `;` rồi lại mã; sau `#` (Python)
     có `x.y(`…`)` mà dòng trước dấu `#` kết thúc bằng `:` hoặc `,` (mã bị cắt giữa biểu thức), hoặc `; ` rồi mã;
     Tìm thấy 08/10 khi chạy lần đầu: `moc-v/seg/ep005/scene.js:98` (đoạn chứng minh Mốc V, đã duyệt — KHÔNG sửa, chỉ báo) có
     `slow.material.opacity = sA * (…);` nằm sau `//` → không chạy. Build chỉ quét thư mục của đoạn đang dựng + thư viện;
  3. `node --check` mọi tệp .js (mô-đun ES kiểm qua bản sao .mjs: Node 22 `--check` trên .js có import trả 0 dù hỏng); `python3 -m py_compile` mọi spine.py / scene .py.
    python3 toolkit/tests/comment_guard.py [thư mục …]     → thoát 1 nếu có lỗi (build.py và build_seg.py gọi trước khi dựng)
"""
import glob, os, py_compile, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
import lint_comments  # noqa: E402

SKIP = re.compile(r'/(vendor|node_modules|work|__pycache__)/')
JS_EXTRA = [re.compile(r'\b[A-Za-z_$][\w$]*(\.[A-Za-z_$][\w$]*)+\s*=[^=>][^;]*;', re.A),   # gán thuộc tính kết thúc bằng ;
            re.compile(r'\w\([^()]*\)\s*;'), re.compile(r';\s*[A-Za-z_$][\w.$]*\s*\(', re.A)]
PY_EXTRA = re.compile(r';\s*[A-Za-z_][\w.]*\s*[(=]')


def files(dirs=None):
    dirs = dirs or [os.path.join(ROOT, 'toolkit', 'factory', 'world'), os.path.join(ROOT, 'moc-v', 'seg')] + glob.glob(os.path.join(ROOT, 'episodes', '*', 'world'))
    out = set()
    for d in dirs:
        if os.path.isfile(d):
            out.add(os.path.abspath(d)); continue
        for ext in ('js', 'py'):
            out |= {os.path.abspath(f) for f in glob.glob(os.path.join(d, '**', f'*.{ext}'), recursive=True) if not SKIP.search(f)}
    return sorted(out)


def code_part(line, mark):
    """Phần mã trước dấu chú thích (bỏ qua dấu nằm trong chuỗi đơn giản và URL)."""
    q, i = None, 0
    while i < len(line):
        c = line[i]
        if q:
            if c == '\\':
                i += 2; continue
            if c == q:
                q = None
        elif c in '\'"`':
            q = c
        elif line.startswith(mark, i) and not line[max(0, i - 1):i + len(mark) + 1].startswith(':'):
            return line[:i], line[i + len(mark):]
        i += 1
    return line, None


def extra(path):
    bad = []
    js = path.endswith('.js')
    for n, l in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        s = l.rstrip('\n')
        if not s.strip() or s.lstrip().startswith('//' if js else '#'):
            continue
        code, com = code_part(s, '//' if js else '#')
        if com is None or not code.strip() or 'http' in com:
            continue
        if js and any(r.search(com) for r in JS_EXTRA):
            bad.append(f'{os.path.relpath(path, ROOT)}:{n}: mã sau // : {com.strip()[:90]}')
        if not js and (PY_EXTRA.search(com) or (code.rstrip().endswith((':', ',', '(')) and re.search(r'\w+\.\w+\(', com))):
            bad.append(f'{os.path.relpath(path, ROOT)}:{n}: mã sau # : {com.strip()[:90]}')
    return bad


def syntax(path):
    if path.endswith('.js'):
        # Node 22 `--check` trên .js có import/export trả 0 kể cả khi hỏng cú pháp (đo 08/10) → kiểm mô-đun ES qua bản sao .mjs
        src = open(path, encoding='utf-8', errors='replace').read()
        tgt = path
        if re.search(r'^\s*(import|export)\b', src, re.M):
            fd, tgt = tempfile.mkstemp(suffix='.mjs'); os.write(fd, src.encode()); os.close(fd)
        try:
            r = subprocess.run(['node', '--check', tgt], capture_output=True, text=True)
        finally:
            if tgt != path:
                os.remove(tgt)
        err = [x for x in r.stderr.strip().splitlines() if 'Error' in x] or r.stderr.strip().splitlines() or ['?']
        return [] if r.returncode == 0 else [f'{os.path.relpath(path, ROOT)}: node --check: {err[0][:120]}']
    try:
        py_compile.compile(path, cfile=os.path.join(tempfile.gettempdir(), 'cg.pyc'), doraise=True)
        return []
    except py_compile.PyCompileError as e:
        return [f'{os.path.relpath(path, ROOT)}: py_compile: {str(e).strip().splitlines()[-1][:120]}']


def check(dirs=None):
    F = files(dirs)
    seen = {os.path.dirname(f) for f in F}
    bad = list(lint_comments.lint(sorted(seen)))
    for f in F:
        bad += extra(f) + syntax(f)
    return sorted(set(bad)), len(F)


if __name__ == '__main__':
    bad, n = check([os.path.abspath(a) for a in sys.argv[1:]] or None)
    print('\n'.join(bad) if bad else f'comment_guard: OK ({n} tệp: chú thích giữa dòng + node --check / py_compile)')
    sys.exit(1 if bad else 0)

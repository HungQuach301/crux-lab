"""Nhà máy · bắt lỗi "chú thích nuốt mã" (mã bị dán vào sau // hoặc # trên cùng dòng → không chạy, không báo lỗi). Từ Mốc V (lỗi thật 06/10).
  python3 toolkit/factory/world/lint_comments.py [thư mục đoạn …]   → thoát 1 nếu thấy. build.py chạy trước mỗi lần render thế giới.
Mặc định quét thư viện (toolkit/factory/world), mọi đoạn moc-v/seg/* và episodes/*/world/*."""
import glob, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def lint(dirs=None):
    dirs = dirs or [os.path.join(ROOT, 'toolkit/factory/world')] + glob.glob(os.path.join(ROOT, 'moc-v/seg/*')) + glob.glob(os.path.join(ROOT, 'episodes/*/world/*'))
    js = [f for d in dirs for f in glob.glob(os.path.join(d, '*.js'))]
    py = [f for d in dirs for f in glob.glob(os.path.join(d, '*.py'))]
    bad = []
    for f in js:
        for i, l in enumerate(open(f), 1):
            if '//' in l and not l.lstrip().startswith('//') and 'http' not in l:
                c = l.split('//', 1)[1]
                if re.search(r"\w\([^()]*(\([^()]*\))?[^()]*\)\s*;", c) or re.search(r"\b(const|let)\s+\w+\s*=|Math\.\w+\(|\.(set|glow|setScalar|bracket|text)\(", c):
                    bad.append(f'{os.path.relpath(f, ROOT)}:{i}: {c.strip()[:100]}')
    for f in py:
        for i, l in enumerate(open(f), 1):
            if '#' in l and not l.lstrip().startswith('#'):
                c = l.split('#', 1)[1]
                if re.search(r"\w+\.(append|extend)\(|^\s*\w+\s*=\s*\S", c):
                    bad.append(f'{os.path.relpath(f, ROOT)}:{i}: {c.strip()[:100]}')
    return bad


if __name__ == '__main__':
    bad = lint([os.path.abspath(a) for a in sys.argv[1:]] or None)
    print('\n'.join(bad) or 'OK'); sys.exit(1 if bad else 0)

"""Mốc V · bắt lỗi "chú thích nuốt mã" (mã bị dán vào sau // hoặc # trên cùng dòng → không chạy, không báo lỗi).
  python3 moc-v/world/lint_comments.py   → thoát 1 nếu thấy. Chạy trước mỗi lần dựng."""
import glob, re, sys
bad = []
for f in glob.glob('moc-v/seg/*/scene.js') + glob.glob('moc-v/world/*.js'):
    for i, l in enumerate(open(f), 1):
        if '//' in l and not l.lstrip().startswith('//') and 'http' not in l:
            c = l.split('//', 1)[1]
            if re.search(r"\w\([^()]*(\([^()]*\))?[^()]*\)\s*;", c) or re.search(r"\b(const|let)\s+\w+\s*=|Math\.\w+\(|\.(set|glow|setScalar|bracket|text)\(", c): bad.append(f'{f}:{i}: {c.strip()[:100]}')
for f in glob.glob('moc-v/seg/*/spine.py'):
    for i, l in enumerate(open(f), 1):
        if '#' in l and not l.lstrip().startswith('#'):
            c = l.split('#', 1)[1]
            if re.search(r"\w+\.(append|extend)\(|^\s*\w+\s*=\s*\S", c): bad.append(f'{f}:{i}: {c.strip()[:100]}')
print('\n'.join(bad) or 'OK'); sys.exit(1 if bad else 0)

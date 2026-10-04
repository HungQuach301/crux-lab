#!/usr/bin/env python3
"""C5 film page data: the two signed data files (design/c3/final/work/data.js from src/build_data.py, h3data.js from
src/h3/build_data.py; FRED-derived, not committed) re-exported under their own names for the one-page bundle:
work/c5/data-h2.js (window.DATA_H2), work/c5/data-h3.js (window.DATA_H3).   python3 src/build_c5_data.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); FIN = os.path.join(AN, '../design/c3/final/work')
os.makedirs(os.path.join(AN, 'work/c5'), exist_ok=True)
for src, name, out in (('data.js', 'DATA_H2', 'data-h2.js'), ('h3data.js', 'DATA_H3', 'data-h3.js')):
    s = open(os.path.join(FIN, src)).read()
    assert s.startswith('window.DATA') and '=' in s[:15], src
    s = 'window.' + name + s[len('window.DATA'):]
    open(os.path.join(AN, 'work/c5', out), 'w').write(s); print(out, len(s))

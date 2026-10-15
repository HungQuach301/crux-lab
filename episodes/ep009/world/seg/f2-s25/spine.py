"""Tập 9 · ĐOẠN CON f2-s25 = S25 của đoạn chương f-s22-s25 (M3: tách để bật `cine` / J-L-cut đúng cảnh). Spine = cắt từ spine ĐỦ của f-s22-s25 (kit._subset;
nhịp + động tác đủ ở `ghost`). Không sửa ở đây — sửa ../f-s22-s25/spine.py."""
import os, runpy
os.environ['CRUX_SCENES'] = 'S25'; os.environ['CRUX_PARENT'] = 'episodes/ep009/world/seg/f-s22-s25/scene.js'
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'f-s22-s25', 'spine.py'), run_name='__main__',
               init_globals={'HERE_OVERRIDE': os.path.dirname(os.path.abspath(__file__))})

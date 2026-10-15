"""Tập 9 · ĐOẠN CON b1-s04 = S04 của đoạn chương b-s04-s06 (M3: tách để bật `cine` / J-L-cut đúng cảnh). Spine = cắt từ spine ĐỦ của b-s04-s06 (kit._subset;
nhịp + động tác đủ ở `ghost`). Không sửa ở đây — sửa ../b-s04-s06/spine.py."""
import os, runpy
os.environ['CRUX_SCENES'] = 'S04'; os.environ['CRUX_PARENT'] = 'episodes/ep009/world/seg/b-s04-s06/scene.js'
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b-s04-s06', 'spine.py'), run_name='__main__',
               init_globals={'HERE_OVERRIDE': os.path.dirname(os.path.abspath(__file__))})

"""Tập 9 · ĐOẠN CON a2-s03 = S03 của đoạn chương a-s01-s03 (M3: tách để bật `cine` / J-L-cut đúng cảnh). Spine = cắt từ spine ĐỦ của a-s01-s03 (kit._subset;
nhịp + động tác đủ ở `ghost`). Không sửa ở đây — sửa ../a-s01-s03/spine.py."""
import os, runpy
os.environ['CRUX_SCENES'] = 'S03'; os.environ['CRUX_PARENT'] = 'episodes/ep009/world/seg/a-s01-s03/scene.js'
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'a-s01-s03', 'spine.py'), run_name='__main__',
               init_globals={'HERE_OVERRIDE': os.path.dirname(os.path.abspath(__file__))})

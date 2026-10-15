"""Tập 9 · ĐOẠN CON d1-s14-s15 = S14,S15 của đoạn chương d-s14-s18 (M3: tách để bật `cine` / J-L-cut đúng cảnh). Spine = cắt từ spine ĐỦ của d-s14-s18 (kit._subset;
nhịp + động tác đủ ở `ghost`). Không sửa ở đây — sửa ../d-s14-s18/spine.py."""
import os, runpy
os.environ['CRUX_SCENES'] = 'S14,S15'; os.environ['CRUX_PARENT'] = 'episodes/ep009/world/seg/d-s14-s18/scene.js'
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'd-s14-s18', 'spine.py'), run_name='__main__',
               init_globals={'HERE_OVERRIDE': os.path.dirname(os.path.abspath(__file__))})

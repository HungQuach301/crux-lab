"""Tập 7 · C4 · ĐOẠN G = S29–S33 — KHUNG TỐI THIỂU (lượt 1): nhà máy (spec.py, build_seg.py) đòi spine.py + scene.js cho mọi đoạn
`world:`; đoạn này dựng ở lượt 2 (briefs/builder-c4-2.md). Thế giới đứng yên (Tessa + nhà, lớp bắt buộc), một nhịp thế giới mỗi câu, không động tác.
  python3 episodes/ep007/world/c4/g-s29-s33/spine.py → spine.json"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import c4kit as K
K.stub(HERE, ['S29', 'S30', 'S31', 'S32', 'S33'], 'ep007 C4 · G = S29–S33')

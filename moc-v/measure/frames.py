#!/usr/bin/env python3
"""Mốc V — đo hình trên bản phát hành (không cần mã dựng của tập).

  python3 moc-v/measure/frames.py <video.mp4> <frames_dir_1fps> <out.json>

Mỗi giây (khung 1 fps, 1280x720):
  - OCR tesseract → số từ trên màn hình (conf ≥ 60, từ có ≥ 2 ký tự chữ/số), hộp chữ.
  - Vùng đồ hoạ = điểm ảnh khác nền (khoảng cách màu > 40 so với màu nền = màu phổ biến nhất),
    TRỪ hộp chữ đã nới 6 px. Tính % diện tích khung.
  - Chuyển động = trung bình |khung(t+0,5) − khung(t)| trên vùng KHÔNG phải chữ (độ phân giải 320x180, xám),
    tính từ video 4 fps.
Phân loại mỗi giây:
  - text_only: có chữ (≥ 3 từ) và đồ hoạ ngoài chữ < GFX_MIN.
  - graphic_motion: đồ hoạ ≥ GFX_MIN và chuyển động ngoài chữ ≥ MOT_MIN.
  - graphic_static: đồ hoạ ≥ GFX_MIN, đứng yên.
  - empty: còn lại.
Cắt cứng: giữa hai khung 4 fps liên tiếp, đổi > CUT_MIN điểm ảnh (xám, > 25 mức) — đổi gần toàn khung trong 0,25 s.
Ngưỡng hiệu chuẩn bằng mắt trên 40 khung (moc-v/measure/CALIBRATION.md).
"""
import json, subprocess, sys, os
import numpy as np
import cv2
from concurrent.futures import ProcessPoolExecutor

GFX_MIN = 0.012     # 1,2 % khung ngoài chữ
MOT_MIN = 0.35      # mức xám trung bình / điểm ảnh (0–255) ngoài chữ trong 0,5 s
CUT_MIN = 0.45      # 45 % điểm ảnh đổi trong 0,25 s


def ocr(path):
    try:
        r = subprocess.run(["tesseract", path, "-", "--psm", "11", "tsv"], capture_output=True, text=True, timeout=30,
                           env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    except subprocess.TimeoutExpired:
        return [], []
    words, boxes = [], []
    for line in r.stdout.splitlines()[1:]:
        p = line.split("\t")
        if len(p) < 12:
            continue
        try:
            conf = float(p[10])
        except ValueError:
            continue
        txt = p[11].strip()
        alnum = sum(c.isalnum() for c in txt)
        if conf >= 60 and alnum >= 2:
            x, y, w, h = map(int, p[6:10])
            if h < 9 or h > 200:
                continue
            words.append(txt)
            boxes.append((x, y, w, h))
    return words, boxes


def one(args):
    i, path = args
    img = cv2.imread(path)
    words, boxes = ocr(path)
    H, W = img.shape[:2]
    q = (img // 8).reshape(-1, 3)
    keys = q[:, 0].astype(np.int32) * 1024 + q[:, 1].astype(np.int32) * 32 + q[:, 2]
    bgk = np.bincount(keys).argmax()
    bg = np.array([bgk // 1024, (bgk // 32) % 32, bgk % 32]) * 8 + 4
    dist = np.abs(img.astype(np.int16) - bg[None, None, :]).sum(axis=2)
    fg = dist > 40
    tmask = np.zeros((H, W), bool)
    for (x, y, w, h) in boxes:
        tmask[max(0, y - 6):y + h + 6, max(0, x - 6):x + w + 6] = True
    gfx = float((fg & ~tmask).mean())
    return {"t": i, "words": len(words), "text": " ".join(words)[:300], "gfx": round(gfx, 4),
            "text_area": round(float(tmask.mean()), 4), "boxes": boxes}


def motion(video, n, masks):
    cmd = ["ffmpeg", "-v", "error", "-i", video, "-vf", "fps=4,scale=320:180,format=gray", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320).astype(np.int16)
    mot, cuts = [], []
    for k in range(1, len(fr)):
        d = np.abs(fr[k] - fr[k - 1])
        if (d > 25).mean() > CUT_MIN:
            cuts.append(round(k / 4.0, 2))
    for i in range(n):
        a, b = i * 4, i * 4 + 2
        if b >= len(fr):
            mot.append(0.0); continue
        m = masks[i]
        d = np.abs(fr[b] - fr[a]).astype(np.float32)
        mot.append(round(float(d[~m].mean()) if (~m).any() else 0.0, 3))
    return mot, cuts


def main():
    video, fdir, out = sys.argv[1:4]
    files = sorted(f for f in os.listdir(fdir) if f.endswith(".jpg"))
    with ProcessPoolExecutor(4) as ex:
        rows = list(ex.map(one, [(i, os.path.join(fdir, f)) for i, f in enumerate(files)], chunksize=8))
    masks = []
    for r in rows:
        m = np.zeros((180, 320), bool)
        for (x, y, w, h) in r["boxes"]:
            m[max(0, (y - 6) // 4):(y + h + 6) // 4 + 1, max(0, (x - 6) // 4):(x + w + 6) // 4 + 1] = True
        masks.append(m)
    mot, cuts = motion(video, len(rows), masks)
    for r, m in zip(rows, mot):
        r["motion"] = m
        del r["boxes"]
        if r["gfx"] >= GFX_MIN:
            r["cls"] = "graphic_motion" if m >= MOT_MIN else "graphic_static"
        elif r["words"] >= 3:
            r["cls"] = "text_only"
        else:
            r["cls"] = "empty"
    json.dump({"video": video, "seconds": len(rows), "cuts": cuts, "rows": rows,
               "thresholds": {"GFX_MIN": GFX_MIN, "MOT_MIN": MOT_MIN, "CUT_MIN": CUT_MIN}},
              open(out, "w"), indent=0)
    from collections import Counter
    c = Counter(r["cls"] for r in rows)
    print(out, len(rows), dict(c), "cuts", len(cuts), "words/min", round(sum(r["words"] for r in rows) / len(rows) * 60, 1))


if __name__ == "__main__":
    main()

# CONTROL strips: Episode 1 animatic, text and numbers masked

Control strips for the ep002 C3 blind test. For S01, S05, S08, S10, S16, S18 and S19 there are two files:
- `C-Sxx-strip.png`: a byte-for-byte copy of `episodes/ep001/animatic/strips/Sxx.png`.
- `C-Sxx-strip-masked.png`: the same 6 frames in the same 3×2 numbered layout, with every text string and number covered by a flat `#171B22` block.

Nothing under `episodes/ep001/` was modified.

## Frame times (seconds from the scene's first frame)
The strip builder is `boot().strip()` in the C4 `engine.js` (commit `f8830b1`/`86e5830`, called by C4 `render.js`). It takes `APP.stripTimes`, which is each scene module's `stripTimes`. Those are anchors resolved from `timing.json` + `anchors.json`, clamped to the last frame. Captions are hidden with `NOCAP`. Each frame is drawn at 1280×720 and placed as a 636×358 cell at x = 3 + (i mod 3)·640, y = 2 + ⌊i/3⌋·363 on `#05070A`. The 40×40 badge is `#F2B441` with the number in Inter 700 at 30 px.

| Scene | 1 | 2 | 3 | 4 | 5 | 6 | 3D frames |
|---|---|---|---|---|---|---|---|
| S01 | 5.62 | 9.68 | 16.04 | 22.87 | 24.83 | 32.88 | 3, 4, 5 |
| S05 | 5.58 | 12.84 | 16.44 | 21.72 | 24.90 | 39.14 | none |
| S08 | 6.69 | 12.44 | 20.46 | 29.37 | 36.01 | 38.95 | none |
| S10 | 1.84 | 9.59 | 17.59 | 23.01 | 40.45 | 57.25 | 4, 5, 6 |
| S16 | 1.55 | 5.73 | 13.66 | 16.08 | 18.33 | 27.62 | 1, 2 |
| S18 | 1.75 | 16.89 | 26.51 | 32.55 | 38.52 | 48.04 | 1 |
| S19 | 1.55 | 12.96 | 15.34 | 16.83 | 21.43 | 26.33 | none |

Exact values, plus every masked text box per frame, are in `frames/Sxx.json`.

## Method
1. **Which code to use.** The current page (`film.html` / `build/film.js`, C5–C6, `window.CHECKS`) does **not** redraw the frames in `strips/`. C5 and C6 changed footers, added assumption lines and the corner basis label, and moved some layouts. For example, S19 differs on every frame. The strips were last written by the C4 commits: `f8830b1` for S05, S08 and S19, and `86e5830` for the others. The C4 source only exists in older history. **The shallow clone's `.git` was deepened** with `git fetch --deepen=300 origin ep002` to reach it. No working-tree files changed.
2. **Scratch copy.** Using `git archive 86e5830`, the C4 animatic was copied to scratch. Its `src/data.js` was rebuilt with that commit's `build_data.py`. FRED data came from `data/fetch.py --verify`, run in a scratch mirror: it downloaded the 2 pinned FRED CSVs and found no SHA-256 mismatches. The HMDA CSVs are in the repo. The data sources have not changed between `86e5830` and HEAD. three.js is 0.186.1 (npm, scratch), running in Chromium headless with SwiftShader using the same flags as C4 `render.js`. **Everything could be rebuilt; nothing was missing.**
3. **Text boxes.** `src/patch_c4.py` patches only the scratch `engine.js`. In `text()` it records each string's box with the same formula as the C5 `CHECKS.objects()` text boxes: [x0, y−0.76·px, x0+w, y+0.22·px], mapped through the canvas transform. It draws nothing differently. The C4 code has no `CHECKS`, `objects()` or `layer('notext')`, so this recorder takes their place.
4. **Masked frame.** `src/grab.js` draws the "all" frame. It then fills every recorded box with `#171B22`, padded by max(4, 0.12·font px) plus 6 px for shadowed text.
5. **Text printed on 3D objects.** Text in 3D canvas textures (the letter, the "NORA'S LOAN 7.62%" card, the house-front "$3,667", the stack labels) never goes through `text()`. To find it, the page is rendered a second time with `window.MASKTEX`, which makes the patched `ptxt()` paint #FF00FF blocks instead of glyphs. The pixels that differ between the two renders are where that text appears on screen. `src/finish.py` fills each group's bounding box plus 4 px with `#171B22`. This added 3 blocks in S01, 3 in S10, 2 in S16 and 8 in S18 (the letter).
6. **Strip.** The strip is built in the browser by the same builder code, reading the 1280×720 masked frames: `COMPOSE=1 node grab.js`.

The yellow outline of the "ILLUSTRATIVE" badge stays visible as an empty frame; its word is masked. The number badges 1–6 are part of the layout and are not masked.

## Verification (`src/verify.py`)
- **Same frames.** Two unmasked rebuilds were compared with the original `strips/Sxx.png`: the in-page strip, and the strip from the compose path used for the masked version. **Both match exactly, with 0 pixels differing by more than 8/255, in all 7 scenes.** So the times, layout and drawing are identical.
- **Every box masked.** All 439 recorded text boxes are flat `#171B22` in the final frames: 0 are not flat.
- **OCR.** Tesseract 5 `--psm 11` was run on each strip upscaled 3×. A word counts as legible only if it matches a word the scene really draws. Original strips: 32–54 such words per scene. **Masked strips: 0 in all 7.** Full output is in `verify.txt`. The remaining raw tokens are OCR noise read from dashed lines, tick rows and hatching ("eee", "SERRE"), not text.
- **By eye.** All 7 masked strips were inspected: no legible character remains, including on 3D objects.

## Re-run
```
S=<scratch>; git archive 86e5830 episodes/ep001/animatic/src episodes/ep001/animatic/{timing,anchors}.json episodes/ep001/model \
  episodes/ep001/out/{model,claims}.json episodes/ep001/data/normalized toolkit/render/fonts | tar -x -C $S/c4
# + data/normalized/mortgage30_weekly.csv from `data/fetch.py --verify` (run in a copy), then:
python3 $S/c4/episodes/ep001/animatic/src/build_data.py && python3 src/patch_c4.py $S/c4/episodes/ep001/animatic/src/engine.js
export NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers THREE_DIR=<three@0.186.1>/build
A="$S/c4/episodes/ep001/animatic $S/c4/toolkit/render/fonts $S/out"; SC="S01 S05 S08 S10 S16 S18 S19"
node src/grab.js $A $SC && python3 src/finish.py $S/out $SC && COMPOSE=1 node src/grab.js $A $SC
python3 src/verify.py $S/out episodes/ep001/animatic/strips $SC
```

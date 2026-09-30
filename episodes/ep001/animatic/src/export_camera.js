'use strict';
// C5: out/camera.json from the film page (the same page that renders out/video.mp4 and that window.CHECKS serves).
// One entry per video frame (30 fps), legacy 3D form of checks/CONTRACT.md: {fovAxis:"vertical", frames:[{t, pos, target, fovDeg, focusDist}]}
// (three.js world units; focusDist = |target - pos|, so the frame width at the focus plane = 2·focusDist·tan(fov/2)·16/9).
// H3 frames (flat 2D charts, no camera) hold one fixed virtual camera (STILL below): the flat frames never move.
// The measured speed therefore spikes for 1-2 frames at each cut between shots (a cut, not a move).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node export_camera.js
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const AN = path.resolve(__dirname, '..'), EP = path.resolve(AN, '..');
const STILL = { pos: [0, 0, 10], target: [0, 0, 0], fovDeg: 35, focusDist: 10 };
(async () => {
  const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  await page.goto('file://' + path.join(AN, 'film.html'));
  await page.evaluate(() => { window.NO3D = true; return window.APP.ready; });
  const { frames, fps } = await page.evaluate(() => ({ frames: APP.frames, fps: APP.fps }));
  const out = [];
  const r6 = (v) => Math.round(v * 1e6) / 1e6;
  for (let g0 = 0; g0 < frames; g0 += 600) {
    const part = await page.evaluate(([a, b]) => { const r = []; for (let g = a; g < b; g++) r.push(APP.camera(g)); return r; }, [g0, Math.min(frames, g0 + 600)]);
    part.forEach((c, i) => {
      const t = r6((g0 + i) / fps);
      if (!c) { out.push({ t, ...STILL }); return; }
      const d = Math.hypot(c.target[0] - c.pos[0], c.target[1] - c.pos[1], c.target[2] - c.pos[2]);
      out.push({ t, pos: c.pos.map(r6), target: c.target.map(r6), fovDeg: r6(c.fovDeg), focusDist: r6(d), scene: c.scene });
    });
    process.stderr.write(`${g0 + part.length}/${frames}\r`);
  }
  await browser.close();
  const cam = { fovAxis: 'vertical', fps, units: 'three.js world units (1 unit ~ 1 m)', source: 'episodes/ep001/animatic/src/export_camera.js (film page APP.camera, per video frame)',
    note: 'H3 frames (flat charts) have no camera: a fixed virtual camera stands in, so they never move. Speed spikes of 1-2 frames at shot cuts are cuts, not moves.', frames: out };
  fs.writeFileSync(path.join(EP, 'out', 'camera.json'), JSON.stringify(cam));
  console.error('\nwrote out/camera.json', out.length, 'frames');
})().catch((e) => { console.error(e); process.exit(1); });

'use strict';
// CONTROL strips (ep002 review-c3) from Episode 1's C4 animatic, the code that drew animatic/strips/Sxx.png.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers THREE_DIR=<three/build> \
//   node grab.js <c4AnimaticCopy> <fontsDir> <outDir> S01 S05 ...            (grab)
//   COMPOSE=1 node grab.js <c4AnimaticCopy> <fontsDir> <outDir> S01 ...     (strip from <outDir>/S-k-final.png, after finish.py)
// <c4AnimaticCopy> = scratch copy of episodes/ep001/animatic at 86e5830 (git archive), src/data.js built by its build_data.py,
// src/engine.js patched by patch_c4.py (records text boxes in window.TBOX; draws nothing differently).
// Per scene: same page, viewport, browser flags and strip builder as C4 render.js + engine.js boot().strip():
//   times = APP.stripTimes (scene module stripTimes, clamped to the last frame), NOCAP on (sentence-captions hidden),
//   3x2 grid of 636x358 frames on #05070A, frame i at x = 3 + (i%3)*640, y = 2 + floor(i/3)*363, badge 40x40 C.warn, number 30px/700.
// grab writes <outDir>/S-all.png (unmasked strip rebuild, to diff against the original), S-k-all.png (1280x720 frame),
// S-k-mask.png (frame with every text() box filled #171B22), S-k-tex.png (same, page loaded with MASKTEX: 3D texture text
// replaced by #FF00FF blocks) and S.json (times + boxes). compose writes S-mask.png from S-k-final.png with the same builder.
const fs = require('fs'), path = require('path'), http = require('http');
const { chromium } = require('playwright');
const [AN, FONTS, OUT, ...scenes] = process.argv.slice(2);
const THREE_DIR = process.env.THREE_DIR;
const MASK = '#171B22';
fs.mkdirSync(OUT, { recursive: true });
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u.startsWith('/three/') ? path.join(THREE_DIR, u.slice(7)) : u.startsWith('/fonts/') ? path.join(FONTS, u.slice(7)) : path.join(AN, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const save = (n, d) => fs.writeFileSync(path.join(OUT, n), Buffer.from(d.split(',')[1], 'base64'));
// the C4 strip builder (engine.js boot().strip) on given frame images
function builder(images) {
  const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 728; const g = sc.getContext('2d');
  g.fillStyle = '#05070A'; g.fillRect(0, 0, 1920, 728);
  images.forEach((im, i) => {
    const x = 2 + (i % 3) * 640 + 1, y = 2 + Math.floor(i / 3) * 363;
    g.drawImage(im, x, y, 636, 358);
    g.fillStyle = '#F2B441'; g.fillRect(x + 636 - 46, y + 358 - 46, 40, 40);
    g.font = '700 30px Inter'; g.fillStyle = '#0E1116'; g.textAlign = 'center'; g.textBaseline = 'alphabetic'; g.fillText(String(i + 1), x + 636 - 26, y + 358 - 14);
  });
  return sc.toDataURL('image/png');
}
async function compose(browser, port, F) {
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?s=S05`); // same origin + Inter faces; the scene itself is not used
  await page.waitForFunction(() => window.READY === true, null, { timeout: 180000 });
  for (const [src, dst] of [['final', 'mask'], ['all', 'recomposed-all']]) { // 'all' = control of this path vs the original strip
    const urls = [1, 2, 3, 4, 5, 6].map((k) => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, `${F}-${k}-${src}.png`)).toString('base64'));
    const d = await page.evaluate(async ([urls, fn]) => {
      const ims = await Promise.all(urls.map((u) => new Promise((res) => { const im = new Image(); im.onload = () => res(im); im.src = u; })));
      const frames = ims.map((im) => { const k = document.createElement('canvas'); k.width = 1280; k.height = 720; k.getContext('2d').drawImage(im, 0, 0); return k; });
      return (0, eval)('(' + fn + ')')(frames);
    }, [urls, builder.toString()]);
    save(`${F}-${dst}.png`, d);
  }
  console.error(F, 'composed');
  await page.close();
}
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu', '--font-render-hinting=none'] });
  for (const F of scenes) {
    if (process.env.COMPOSE) { await compose(browser, port, F); continue; }
    for (const tex of [false, true]) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
    page.on('pageerror', (e) => { console.error('pageerror', F, e.message); process.exit(1); });
    await page.addInitScript((m) => { window.MASKTEX = m; }, tex);
    await page.goto(`http://127.0.0.1:${port}/src/page.html?s=${F}`);
    await page.waitForFunction(() => window.READY === true, null, { timeout: 180000 });
    const r = await page.evaluate((MASK) => {
      const out = document.querySelector('canvas'), oc = out.getContext('2d');
      const times = APP.stripTimes, frames = [], masked = [];
      const strips = {};
      for (const kind of ['all', 'mask']) {
        const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 728; const g = sc.getContext('2d');
        g.fillStyle = '#05070A'; g.fillRect(0, 0, 1920, 728);
        const was = window.NOCAP; window.NOCAP = true;
        times.forEach((t, i) => {
          const x = 2 + (i % 3) * 640 + 1, y = 2 + Math.floor(i / 3) * 363;
          window.TBOX = []; APP.png(t); const boxes = window.TBOX; window.TBOX = null;
          if (kind === 'all') frames.push(out.toDataURL('image/png'));
          if (kind === 'mask') {
            oc.save(); oc.setTransform(1, 0, 0, 1, 0, 0); oc.globalAlpha = 1; oc.shadowColor = 'transparent'; oc.fillStyle = MASK;
            for (const b of boxes) { const p = Math.max(4, 0.12 * b.fontPx * b.scale) + (b.shadow ? 6 : 0); const [l, tp, rr, bt] = b.box;
              oc.fillRect(Math.floor(l - p), Math.floor(tp - p), Math.ceil(rr - l + 2 * p), Math.ceil(bt - tp + 2 * p)); }
            oc.restore();
            masked.push(out.toDataURL('image/png'));
            frames[i] = { full: frames[i], k: i + 1, t: +t.toFixed(4), mode: APP.modeAt(t), texts: boxes.map((b) => ({ text: b.text, alpha: +b.alpha.toFixed(3), box: b.box.map((v) => +v.toFixed(1)) })) };
          }
          g.drawImage(out, x, y, 636, 358);
          g.fillStyle = '#F2B441'; g.fillRect(x + 636 - 46, y + 358 - 46, 40, 40);
          g.font = '700 30px Inter'; g.fillStyle = '#0E1116'; g.textAlign = 'center'; g.textBaseline = 'alphabetic'; g.fillText(String(i + 1), x + 636 - 26, y + 358 - 14);
        });
        window.NOCAP = was;
        strips[kind] = sc.toDataURL('image/png');
      }
      return { strips, masked, frames, times, dur: APP.duration };
    }, MASK);
    if (!tex) {
      save(`${F}-all.png`, r.strips.all);
      r.frames.forEach((f, i) => { save(`${F}-${i + 1}-all.png`, f.full); delete f.full; save(`${F}-${i + 1}-mask.png`, r.masked[i]); });
      fs.writeFileSync(path.join(OUT, `${F}.json`), JSON.stringify({ scene: F, duration: r.dur, stripTimes: r.times, frames: r.frames }, null, 1));
      console.error(F, 'times', r.times.map((t) => t.toFixed(2)).join(', '), '| text boxes', r.frames.map((f) => f.texts.length).join(','));
    } else r.masked.forEach((d, i) => save(`${F}-${i + 1}-tex.png`, d));
    await page.close();
    }
  }
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });

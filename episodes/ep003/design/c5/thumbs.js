// Tập 3 · C6: 3 thumbnail candidates (THUMB1..3 of design/c3/src/scenes.js) → out/package/thumb-N.png (1280x720) + thumb-N.json {texts:[{text, box, fontPx}]}.
//   NODE_PATH=$(npm root -g) node episodes/ep003/design/c5/thumbs.js   (static server on :8765 at the repo root)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const OUT = path.join(__dirname, '..', '..', 'out', 'package');
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  p.on('pageerror', (e) => console.error('pageerror', e.message));
  for (const n of [1, 2, 3]) {
    await p.goto(`http://127.0.0.1:8765/episodes/ep003/design/c3/page.html?k=THUMB${n}`);
    await p.waitForFunction('window.READY === true', null, { timeout: 30000 });
    const png = await p.evaluate(() => APP.png(0)), bx = await p.evaluate(() => APP.boxes(0));
    fs.writeFileSync(path.join(OUT, `thumb-${n}.png`), Buffer.from(png.split(',')[1], 'base64'));
    const S = 1280 / 1920; // the shot's own labels are off (FLAGS.NOTEXT) but still logged: only the last two boxes (the hero lines) are drawn
    const texts = bx.slice(-2).map((t) => ({ text: t.s, box: t.glyph.map((v) => Math.round(v * S * 10) / 10), fontPx: Math.round(t.px * S * 10) / 10 }));
    fs.writeFileSync(path.join(OUT, `thumb-${n}.json`), JSON.stringify({ texts }, null, 1));
    console.log(n, texts.map((t) => t.text + ' @' + t.fontPx).join(' | '));
  }
  await b.close();
})();

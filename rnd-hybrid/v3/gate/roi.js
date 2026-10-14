// R&D v3 · cổng máy: đọc window.ROI của một đoạn (scene.js) ở các thời điểm, dùng page.html của nhà máy (chỉ import, không sửa).
//   NODE_PATH=$(npm root -g) node rnd-hybrid/v3/gate/roi.js <thư mục đoạn> <res> <t1,t2,…>  → in JSON {t: ROI}
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../../..'); const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg' };
(async () => { const [seg, res, ts] = process.argv.slice(2), W = Math.round(1920 * res / 1080), H = +res;
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--font-render-hinting=none', '--disable-lcd-text'] });
  const ctx = await b.newContext({ viewport: { width: W, height: H } });
  await ctx.route('http://mocv.local/**', (r) => { const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname)); if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' }); r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' }); });
  const page = await ctx.newPage(); await page.goto(`http://mocv.local/toolkit/factory/world/page.html?seg=${encodeURIComponent(seg)}&res=${res}`); await page.waitForFunction('window.READY === true', null, { timeout: 180000 });
  const out = {}; for (const t of ts.split(',').map(Number)) out[t] = await page.evaluate((t) => { APP.frame(t); return window.ROI; }, t);
  console.log(JSON.stringify(out)); await b.close(); })();

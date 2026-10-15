// F-17 · giờ máy MỖI KHUNG theo lớp (chẩn đoán T11; cách đo của rnd-hybrid/v4/light/measure.js): mỗi cấu hình một trang mới, 1 khung làm nóng +
// trung vị 3 lần (APP.frame + JPEG q0,95 như render_shots). Máy rỗi, tuần tự.
//   NODE_PATH=$(npm root -g) node toolkit/factory/f17/measure_layers.js <thư mục đoạn có cine> <t> <out.jsonl> [cấu hình,…]
//   cấu hình: off (không lớp) · full · -lock · -tex · -hdri · -soft · -grade · -rim · -ao · -dof (đủ lớp trừ một)
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../../..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
(async () => {
  const [seg, tS, out, cfgS] = process.argv.slice(2), t = +tS;
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--font-render-hinting=none', '--disable-lcd-text'] });
  for (const cfg of (cfgS || 'off,full').split(',')) {
    const ctx = await b.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    await ctx.route('http://mocv.local/**', (r) => { const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname)); if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' }); r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' }); });
    if (cfg.startsWith('-')) await ctx.addInitScript((k) => { window.CINE_LAYERS = { [k]: false }; }, cfg.slice(1));
    const page = await ctx.newPage(); page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
    await page.goto(`http://mocv.local/toolkit/factory/world/cine/cine.html?seg=${encodeURIComponent(seg)}&res=1080&cine=${cfg === 'off' ? 'off' : 'on'}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 300000 });
    const ms = await page.evaluate((t) => { const m = []; APP.frame(t); APP.canvas.toDataURL('image/jpeg', 0.95);
      for (let k = 0; k < 3; k++) { const a = performance.now(); APP.frame(t); APP.canvas.toDataURL('image/jpeg', 0.95); m.push(performance.now() - a); }
      m.sort((x, y) => x - y); return m[1]; }, t);
    const rec = { seg, t, cfg, frame_ms: +ms.toFixed(1) }; fs.appendFileSync(out, JSON.stringify(rec) + '\n'); console.log(JSON.stringify(rec)); await ctx.close();
  }
  await b.close();
})();

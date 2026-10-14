// R&D v4 · đo giờ máy / khung theo LỚP + xuất ảnh tĩnh, qua page.html của nhà máy (chỉ import, không sửa).
//   NODE_PATH=$(npm root -g) node rnd-hybrid/v4/light/measure.js <thư mục đoạn bọc> <res> <t> <outdir> [cấu hình,…]
//   cấu hình: base (cảnh gốc, không lớp) · full · hdri · tex · soft · rim · ao · dof · grade (một lớp riêng) · hdri+ao …
//   Mỗi cấu hình: một trang mới (window.CINE_LAYERS đặt trước khi nạp), khung t render 1 lần làm nóng + 3 lần đo (APP.frame + JPEG q 0,95
//   như render_shots) → trung vị ms; PNG của lần cuối. Kết quả <outdir>/<tên>-<cấu hình>.png + measure.jsonl (nối thêm).
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../../..'); const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg' };
const ALL = ['hdri', 'tex', 'soft', 'rim', 'ao', 'dof', 'grade'];
(async () => {
  const [seg, res, tS, outdir, cfgS] = process.argv.slice(2), W = Math.round(1920 * res / 1080), H = +res, t = +tS; fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--font-render-hinting=none', '--disable-lcd-text'] });
  for (const cfg of (cfgS || 'base,full').split(',')) {
    const on = cfg === 'full' ? ALL : cfg === 'base' ? [] : cfg.split('+'), layers = Object.fromEntries(ALL.map((k) => [k, on.includes(k)]));
    const ctx = await b.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
    await ctx.route('http://mocv.local/**', (r) => { const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname)); if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' }); r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' }); });
    await ctx.addInitScript((l) => { window.CINE_LAYERS = l; }, layers);
    const page = await ctx.newPage(); page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
    page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.error('page:', m.text()); });
    const b0 = Date.now(); await page.goto(`http://mocv.local/toolkit/factory/world/page.html?seg=${encodeURIComponent(seg)}&res=${res}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 300000 }); const boot = Date.now() - b0;
    const r = await page.evaluate((t) => { const ms = []; let img;
      APP.frame(t); APP.canvas.toDataURL('image/jpeg', 0.95);
      for (let k = 0; k < 3; k++) { const a = performance.now(); APP.frame(t); APP.canvas.toDataURL('image/jpeg', 0.95); ms.push(performance.now() - a); }
      img = APP.canvas.toDataURL('image/png').split(',')[1]; ms.sort((x, y) => x - y); return { ms: ms[1], img }; }, t);
    const name = `${path.basename(seg)}-${cfg}`; fs.writeFileSync(path.join(outdir, name + '.png'), Buffer.from(r.img, 'base64'));
    const rec = { seg, res: +res, t, cfg, layers: on, frame_ms: +r.ms.toFixed(1), boot_ms: boot }; fs.appendFileSync(path.join(outdir, 'measure.jsonl'), JSON.stringify(rec) + '\n');
    console.log(JSON.stringify(rec)); await ctx.close();
  }
  await b.close();
})();

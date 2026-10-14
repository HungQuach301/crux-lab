// F-17 · ĐO lớp cine trên điểm ảnh render thật: trang KHÔNG lớp (cine.html?cine=off) và trang CÓ lớp (?cine=on), cùng thư mục đoạn, cùng t.
//   NODE_PATH=$(npm root -g) node toolkit/factory/world/cine/cine_check.js <thư mục đoạn> <res> <out.json> [--times t1,t2 | --per-shot 3]
//        [--rim] [--streak] [--stills <dir>]
// Mỗi mẫu t: ảnh WebGL thuần (không lớp chữ 2D) của hai trang; mặt nạ vật dữ liệu (role series/bar/grid, theo màu gốc, co 2 px) dựng ở trang
// có lớp → trung bình sRGB mỗi màu dữ liệu trước/sau (cine_color.py: ΔE2000 + thứ tự độ sáng → CHẶN). --rim: viền người phía gần/xa đèn +
// ΔE màu thân. --streak: vệt DOF trên đầu (fragment F-17 vs v4) ở shot cận. --stills: lưu PNG trước/sau (đánh giá bằng mắt; không commit video).
// Mặc định --per-shot 3 (25/50/75 % mỗi shot của spine). Trang lỗi = thoát 1.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../../../..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.hdr': 'application/octet-stream' };
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

(async () => {
  const [segArg, resS, outRel] = process.argv.slice(2), segDir = path.relative(ROOT, path.resolve(segArg)), res = +resS, W = Math.round(1920 * res / 1080);
  const spine = JSON.parse(fs.readFileSync(path.join(ROOT, segDir, 'spine.json'), 'utf8'));
  if (!spine.cine) throw new Error('cine_check: spine.json không có khoá cine');
  const per = +arg('--per-shot', 3);
  const times = arg('--times') ? arg('--times').split(',').map(Number)
    : spine.shots.flatMap((s) => Array.from({ length: per }, (_, k) => +(s.t0 + (s.t1 - s.t0) * (k + 1) / (per + 1)).toFixed(3)));
  const stills = arg('--stills') ? path.resolve(arg('--stills')) : null; if (stills) fs.mkdirSync(stills, { recursive: true });
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const open = async (mode) => {
    const ctx = await browser.newContext({ viewport: { width: W, height: res }, deviceScaleFactor: 1 });
    await ctx.route('http://mocv.local/**', (r) => {
      const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname));
      if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' });
      r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' });
    });
    const page = await ctx.newPage();
    page.on('pageerror', (e) => { console.error('pageerror:', e.message); process.exit(1); });
    page.on('console', (m) => { if (m.type() === 'error') console.error('page:', m.text()); });
    await page.goto(`http://mocv.local/toolkit/factory/world/cine/cine.html?seg=${encodeURIComponent(segDir)}&res=${res}&cine=${mode}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 300000 });
    return page;
  };
  const base = await open('off'), cine = await open('on');
  const samples = [];
  for (const t of times) {
    const b = await base.evaluate((t) => { APP.frame(t); return CINE.state.renderer.domElement.toDataURL('image/png'); }, t);
    const r = await cine.evaluate(async ([t, b, rim, streak]) => {
      const fr = (x) => APP.frame(x); fr(t);
      const shot = CINE.state.cfg || {}, out = { t, shot: shot.shot || null, data: await CINE.meas.data(b) };
      if (rim && CINE.state.people.length) out.rim = await CINE.meas.rim(b, fr);
      if (streak && shot.shot === 'close' && CINE.state.passes.dof) out.streak = await CINE.meas.streak(fr);
      fr(t); out.png = CINE.state.renderer.domElement.toDataURL('image/png');
      return out;
    }, [t, b, process.argv.includes('--rim'), process.argv.includes('--streak')]);
    if (stills) { const n = `${path.basename(segDir)}-t${t.toFixed(2)}`;
      fs.writeFileSync(path.join(stills, n + '-before.png'), Buffer.from(b.split(',')[1], 'base64'));
      fs.writeFileSync(path.join(stills, n + '-after.png'), Buffer.from(r.png.split(',')[1], 'base64')); }
    delete r.png; samples.push(r);
    console.log(`t=${t} shot=${r.shot} nhóm dữ liệu=${r.data.length}${r.rim ? ' rim' : ''}${r.streak ? ' streak' : ''}`);
  }
  const roof = await cine.evaluate(() => CINE.state.stats);
  await browser.close();
  fs.writeFileSync(path.resolve(outRel), JSON.stringify({ seg: segDir, res, cine: spine.cine, samples, roof }, null, 1));
})().catch((e) => { console.error(e); process.exit(1); });

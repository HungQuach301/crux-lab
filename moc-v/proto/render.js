// Mốc V · bộ render đoạn thử: một trang HTML (canvas 2D hoặc three.js) → H.264 không tiếng, song song theo đoạn khung.
//   NODE_PATH=$(npm root -g) node moc-v/proto/render.js <page.html (repo path)> <out.mp4> [--fps 30] [--t0 0] [--t1 69.6] [--workers 4]
//        [--stills t1,t2,... --stills-dir D]
// Trang phải đặt window.READY = true và có window.APP.frame(t) (vẽ khung ở giây t). Ảnh lấy bằng canvas.toDataURL JPEG q 0,95.
// In thời gian render CPU (giây máy / giây phim) vào <out>.render.json.
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');
const ROOT = path.resolve(__dirname, '../..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.glb': 'model/gltf-binary', '.gltf': 'model/gltf+json', '.bin': 'application/octet-stream' };
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

(async () => {
  const pageRel = process.argv[2], out = path.resolve(process.argv[3]);
  const fps = +arg('--fps', 30), t0 = +arg('--t0', 0), t1 = +arg('--t1', 69.6), workers = +arg('--workers', 4);
  const gl = process.argv.includes('--webgl');
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text', ...(gl ? ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] : [])] });
  const open = async () => {
    const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    await ctx.route('http://proto.local/**', (r) => {
      const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname));
      if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' });
      r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' });
    });
    const page = await ctx.newPage();
    page.on('pageerror', (e) => { console.error('pageerror:', e.message); process.exitCode = 1; });
    page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.error('page:', m.text()); });
    await page.goto(`http://proto.local/${pageRel}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 120000 });
    return page;
  };
  const stills = arg('--stills');
  if (stills) {
    const page = await open(), dir = arg('--stills-dir', path.dirname(out)); fs.mkdirSync(dir, { recursive: true });
    for (const t of stills.split(',').map(Number)) {
      const b64 = await page.evaluate((t) => { APP.frame(t); return APP.canvas.toDataURL('image/png').split(',')[1]; }, t);
      fs.writeFileSync(path.join(dir, `${path.basename(out, '.mp4')}-t${t.toFixed(2)}.png`), Buffer.from(b64, 'base64'));
    }
    await browser.close(); return;
  }
  const F0 = Math.round(t0 * fps), F1 = Math.round(t1 * fps), n = F1 - F0;
  const chunk = Math.ceil(n / workers), tmpd = fs.mkdtempSync(path.join(os.tmpdir(), 'mocv-'));
  const segs = Array.from({ length: workers }, (_, i) => ({ f0: F0 + i * chunk, f1: Math.min(F1, F0 + (i + 1) * chunk), out: path.join(tmpd, `s${i}.mp4`) }))
    .filter((s) => s.f1 > s.f0);
  const cpu0 = process.cpuUsage(), w0 = Date.now();
  await Promise.all(segs.map(async (seg) => {
    const page = await open();
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264',
      '-profile:v', 'high', '-preset', 'fast', '-crf', '16', '-pix_fmt', 'yuv420p', '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
      '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-r', String(fps), '-video_track_timescale', '15360', seg.out],
      { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let f = seg.f0; f < seg.f1; f++) {
      const b64 = await page.evaluate((t) => { APP.frame(t); return APP.canvas.toDataURL('image/jpeg', 0.95).split(',')[1]; }, f / fps);
      if (!ff.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise((r) => ff.on('close', r));
    await page.close();
  }));
  const list = path.join(tmpd, 'list.txt'); fs.writeFileSync(list, segs.map((s) => `file '${s.out}'`).join('\n'));
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', out]);
  const wall = (Date.now() - w0) / 1000;
  // CPU thật của cả máy (gồm Chromium, SwiftShader, ffmpeg): đọc /proc/stat trước/sau không chính xác khi máy chạy việc khác → ghi wall + số luồng
  const rep = { page: pageRel, frames: n, film_s: n / fps, wall_s: +wall.toFixed(1), workers, cores: os.cpus().length,
    wall_per_film_s: +(wall / (n / fps)).toFixed(2), cpu_s_est: +(wall * Math.min(workers, os.cpus().length)).toFixed(0) };
  fs.writeFileSync(out + '.render.json', JSON.stringify(rep, null, 1));
  console.log(JSON.stringify(rep));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

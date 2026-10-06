// Mốc V · RENDER THEO CẢNH có bộ nhớ đệm + resume (D-010 quy tắc 8).
//   NODE_PATH=$(npm root -g) node moc-v/world/render_shots.js <seg> <res 540|1080> <out.mp4> [--workers 3] [--only s3,s4] [--stills t1,t2 --stills-dir D]
// - Cảnh = spine.shots (ranh giới giữa các động tác máy quay). Khoá cache = SHA-256(mã thư viện + cảnh + spine + dữ liệu + khoảng + độ phân giải).
//   Cảnh đã có trong cache (work/cache/<seg>/<res>/) thì bỏ qua → chỉ render lại cảnh đã sửa; chạy lại sau khi container khởi động lại = resume.
// - Mỗi khung thứ 3 (0,1 s) ghi nhật ký trang (chữ: hộp, cỡ, độ mờ, loại; chartW; camMoving; vi phạm quy tắc 1) → <cảnh>.log.json.
// - In thời gian render từng cảnh + tổng → <out>.render.json.
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path'), crypto = require('crypto'), os = require('os');
const ROOT = path.resolve(__dirname, '../..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png' };
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

(async () => {
  const [seg, resS, outRel] = process.argv.slice(2); const res = +resS, out = path.resolve(outRel);
  const W = Math.round(1920 * res / 1080), H = res, FPS = 30;
  const spine = JSON.parse(fs.readFileSync(path.join(ROOT, `moc-v/seg/${seg}/spine.json`), 'utf8'));
  const files = ['moc-v/world/lib3d.js', 'moc-v/world/core.js', 'moc-v/world/page.html', 'moc-v/world/render_shots.js', `moc-v/seg/${seg}/scene.js`,
    `moc-v/seg/${seg}/spine.json`, ...(fs.existsSync(path.join(ROOT, `moc-v/seg/${seg}/inputs.json`)) ? JSON.parse(fs.readFileSync(path.join(ROOT, `moc-v/seg/${seg}/inputs.json`))) : ['moc-v/proto/data.json'])];
  const codeHash = crypto.createHash('sha256'); for (const f of files) codeHash.update(f + '\0' + fs.readFileSync(path.join(ROOT, f)));
  const codeKey = codeHash.digest('hex');
  const cacheDir = path.join(ROOT, `moc-v/work/cache/${seg}/${res}`); fs.mkdirSync(cacheDir, { recursive: true });
  const only = arg('--only') ? new Set(arg('--only').split(',')) : null;
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const open = async () => {
    const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
    await ctx.route('http://mocv.local/**', (r) => {
      const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname));
      if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' });
      r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' });
    });
    const page = await ctx.newPage();
    page.on('pageerror', (e) => { console.error('pageerror:', e.message); process.exitCode = 1; });
    page.on('console', (m) => { if (m.type() === 'error') console.error('page:', m.text()); });
    await page.goto(`http://mocv.local/moc-v/world/page.html?seg=${seg}&res=${res}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 180000 });
    return page;
  };
  const stills = arg('--stills');
  if (stills) {
    const page = await open(), dir = path.resolve(arg('--stills-dir', path.dirname(out))); fs.mkdirSync(dir, { recursive: true });
    for (const t of stills.split(',').map(Number)) {
      const r = await page.evaluate((t) => { const log = APP.frame(t); return { img: APP.canvas.toDataURL('image/png').split(',')[1], log }; }, t);
      fs.writeFileSync(path.join(dir, `${seg}-t${t.toFixed(2)}.png`), Buffer.from(r.img, 'base64'));
      if (r.log.violations.length) console.log('violations at', t, JSON.stringify(r.log.violations));
    }
    await browser.close(); return;
  }
  const jobs = spine.shots.map((s) => {
    const key = crypto.createHash('sha256').update(codeKey + `|${s.t0}|${s.t1}|${res}|${FPS}`).digest('hex').slice(0, 16);
    return { ...s, f0: Math.round(s.t0 * FPS), f1: Math.round(s.t1 * FPS), file: path.join(cacheDir, `${s.id}-${key}.mp4`) };
  });
  const todo = jobs.filter((j) => !fs.existsSync(j.file) && (!only || only.has(j.id)));
  console.log(`shots: ${jobs.length}, cached: ${jobs.length - todo.length}, to render: ${todo.map((j) => j.id).join(',') || '—'}`);
  const times = {}, t0all = Date.now(), queue = [...todo];
  const work = async () => {
    const page = await open();
    for (let j; (j = queue.shift());) {
      const w0 = Date.now(), tmp = j.file + '.part.mp4', logs = [];
      const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(FPS), '-i', '-', '-c:v', 'libx264',
        '-profile:v', 'high', '-preset', res >= 1080 ? 'medium' : 'fast', '-crf', res >= 1080 ? '16' : '20', '-pix_fmt', 'yuv420p', '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
        '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-r', String(FPS), '-video_track_timescale', '15360', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
      for (let f = j.f0; f < j.f1; f++) {
        const r = await page.evaluate(([t, want]) => { const log = APP.frame(t); return { img: APP.canvas.toDataURL('image/jpeg', 0.95).split(',')[1], log: want ? log : null }; }, [f / FPS, f % 3 === 0]);
        if (r.log) logs.push(r.log);
        if (!ff.stdin.write(Buffer.from(r.img, 'base64'))) await new Promise((rs) => ff.stdin.once('drain', rs));
      }
      ff.stdin.end(); const code = await new Promise((rs) => ff.on('close', rs)); if (code) throw new Error('ffmpeg ' + j.id);
      fs.renameSync(tmp, j.file); fs.writeFileSync(j.file.replace(/\.mp4$/, '.log.json'), JSON.stringify(logs));
      times[j.id] = +((Date.now() - w0) / 1000).toFixed(1);
      console.log(`shot ${j.id} ${j.t0}–${j.t1} done in ${times[j.id]} s (${(times[j.id] / (j.t1 - j.t0)).toFixed(2)} s/s)`);
    }
  };
  await Promise.all(Array.from({ length: Math.min(+arg('--workers', 3), Math.max(1, todo.length)) }, work));
  await browser.close();
  if (only) return;
  const list = path.join(os.tmpdir(), `mocv-${seg}-${res}.txt`); fs.writeFileSync(list, jobs.map((j) => `file '${j.file}'`).join('\n'));
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', out]);
  const logs = jobs.flatMap((j) => JSON.parse(fs.readFileSync(j.file.replace(/\.mp4$/, '.log.json'), 'utf8')));
  fs.writeFileSync(out.replace(/\.mp4$/, '.log.json'), JSON.stringify(logs));
  const wall = (Date.now() - t0all) / 1000, film = spine.total;
  const rep = { seg, res, shots: jobs.length, rendered: Object.keys(times), cached: jobs.length - todo.length, shot_wall_s: times,
    wall_s: +wall.toFixed(1), film_s: film, wall_per_film_s_rendered: todo.length ? +(Object.values(times).reduce((a, b) => a + b, 0) / todo.reduce((a, j) => a + j.t1 - j.t0, 0)).toFixed(2) : 0,
    cores: os.cpus().length, codeKey: codeKey.slice(0, 16) };
  fs.writeFileSync(out + '.render.json', JSON.stringify(rep, null, 1)); console.log(JSON.stringify(rep));
})().catch((e) => { console.error(e); process.exit(1); });

'use strict';
// Page sampler: drives the render page through the contract (window.CHECKS), evaluates the frame rules and writes <root>/out/checks/page.json.
//   node checks/page/sampler.js <root> [--step 3] [--pixel-step 6] [--scenes a,b] [--jobs N] [--no-cache]
// K3.8 (A3): --jobs N samples scene by scene on N browsers (default: K_JOBS or 1). Each scene job first restores the state a sequential run carries
// into it from the previous samples (text boxes, visible claims, persistent moving collisions), so the merged result equals the sequential one number for
// number; jobs are cached per scene under out/checks/cache/page-scenes (key: sampler code, page files, episode inputs, the scene and the decoded video
// frames of its range).
// Object rules every `step` frames (0.1 s); pixel rules every `pixel-step` frames (0.2 s) on the page's layer masks and on the decoded video frame.
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require('playwright');
const R = require('./objrules');
const P = require('./pixels');

const FPS = 30, DT = 0.1, SPLIT_MIN_RUN = 1.0, SPLIT_MAX = 0.6;
const FAST = 0.10;        // fw/s: camera speed at or above which the composition is "in a move" (layout rules judge the settled ends, V13 bounds the moves)
const TEXT_MOVING = 2;    // px: a text whose box moved at least this much since the previous object sample (0.1 s) is moving on screen
const TEXT_TRAVEL = 4;    // px: a text travelling in or out of frame (V03 in moving frames)
const NCC_MIN = 0.97;     // V12: every text on the video frame correlates with the clean page render at least this much (a ghost copy at 30% opacity gives ≈ 0.96)
const SAFE = [96, 54, 1824, 1026]; // 90% action/title safe area
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : d; };
const ROOT = path.resolve(args[0] || '.');
const STEP = +opt('step', 3), PSTEP = +opt('pixel-step', 6);
const ONLY = opt('scenes', null) ? new Set(opt('scenes').split(',')) : null;
const JOBS = Math.max(1, +opt('jobs', process.env.K_JOBS || 1));
const NO_CACHE = args.includes('--no-cache');
const J = (rel) => JSON.parse(fs.readFileSync(path.join(ROOT, rel), 'utf8'));

// video frames (rgb24) every PSTEP frames, read sequentially from ffmpeg
function videoReader(file, every, pix = 'rgb24', start = 0) {
  // start (a multiple of every): accurate input seek half a frame before it, so the first decoded frame is frame `start`
  const w = 1920, h = 1080, size = w * h * (pix === 'gray' ? 1 : 3);
  const ss = start > 0 ? ['-ss', ((start - 0.5) / FPS).toFixed(6)] : [];
  const ff = spawn('ffmpeg', ['-v', 'error', ...ss, '-i', file, '-vf', `select='not(mod(n\\,${every}))'`, '-vsync', '0', '-f', 'rawvideo', '-pix_fmt', pix, '-'], { stdio: ['ignore', 'pipe', 'inherit'] });
  let chunks = [], have = 0, done = false, waiters = [], idx = -1;
  ff.stdout.on('data', (c) => { chunks.push(c); have += c.length; ff.stdout.pause(); flush(); });
  ff.stdout.on('end', () => { done = true; flush(); });
  function flush() {
    while (waiters.length && (have >= size || done)) {
      if (have < size) { waiters.shift()(null); continue; }
      const all = Buffer.concat(chunks); const f = all.subarray(0, size);
      chunks = [all.subarray(size)]; have -= size;
      waiters.shift()(Buffer.from(f));
    }
    if (have < size * 2 && !done) ff.stdout.resume();
  }
  return {
    // frame number n (multiple of every)
    async get(n) {
      let f = null;
      while (idx < (n - start) / every) { f = await new Promise((res) => { waiters.push(res); flush(); }); idx++; if (!f) return null; }
      return f;
    },
    close() { try { ff.kill(); } catch (e) { /* ignore */ } },
  };
}

// camera speed in frame widths per second (fw/s), per video frame. 2.5D camera {t, x, y, zoom} (x, y in page px of the chart plane,
// zoom = scale) or the legacy form {t, pos, target, fovDeg, focusDist} (width of the frame at the focus plane). Same as checks/py/r_audio.camera_speed.
function cameraSpeed(cam) {
  const fr = cam.frames || [];
  const n = fr.length;
  const w = fr.map((f) => f.zoom !== undefined ? 1920 / f.zoom : 2 * (f.focusDist ?? 1) * Math.tan(((f.fovDeg ?? 40) * Math.PI / 180) / 2) * ((cam.fovAxis || 'vertical') === 'vertical' ? 16 / 9 : 1));
  const P = (f) => f.zoom !== undefined ? [[f.x, f.y, 0], [f.x, f.y, 0]] : [f.pos, f.target || f.pos];
  const sp = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    const a = Math.max(0, i - 1), b = Math.min(n - 1, i + 1);
    if (a === b) continue;
    const dt = fr[b].t - fr[a].t, [pa, ta] = P(fr[a]), [pb, tb] = P(fr[b]);
    const d = (u, v) => Math.hypot(v[0] - u[0], v[1] - u[1], (v[2] || 0) - (u[2] || 0));
    let v = Math.max(d(pa, pb), d(ta, tb)) / dt / w[i];
    if (fr[i].zoom !== undefined) v += Math.abs(Math.log(fr[b].zoom / fr[a].zoom)) / dt;
    sp[i] = v;
  }
  const t = fr.map((f) => f.t);
  return (x) => { if (!n) return 0; let k = Math.round(x * FPS); if (k < 0) k = 0; if (k >= n) k = n - 1; while (k > 0 && t[k] > x + 1e-6) k--; return sp[k]; };
}

function sceneWindow(scenes) { return (t) => scenes.find((s) => t >= s.start && t < s.start + s.dur) || scenes[scenes.length - 1]; }

async function openEnv() {
  const tl = J('out/timeline.json');
  const claimsArr = J('out/claims.json').claims;
  const claims = Object.fromEntries(claimsArr.map((c) => [c.claimId, c]));
  const tokens = J('design/tokens.json');
  const pageCfg = J('out/page.json');
  const illustrative = claimsArr.filter((c) => c.illustrative).map((c) => c.claimId);
  // K3.8 S17: conditional claims (out/claims.json `conditional`) and each condition's label pattern (contract.json claims.conditions)
  const cpath = process.env.K_CONTRACT ? path.resolve(process.env.K_CONTRACT) : path.join(ROOT, 'contract.json');
  const contract = fs.existsSync(cpath) ? JSON.parse(fs.readFileSync(cpath, 'utf8')) : {};
  const condPat = Object.fromEntries(((contract.claims || {}).conditions || []).map((c) => [c.id, new RegExp(c.pattern, 'i')]));
  const conditional = Object.fromEntries(claimsArr.filter((c) => c.conditional).map((c) => [c.claimId, c.conditional]));
  const scenes = tl.scenes.map((s) => ({ ...s, move: s.move || 0, allowed: s.panels || ['*'] }));
  const sceneAt = sceneWindow(scenes);
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const url = /^[a-z]+:/.test(pageCfg.url) ? pageCfg.url : 'file://' + path.join(ROOT, pageCfg.url);
  // K3.1 (F12): every resource the page really loads while it renders (Playwright requests + Resource Timing entries) and every font face of
  // document.fonts; F12 compares them with the declared visual assets
  const resources = { requests: [], entries: [], fonts: [] };
  page.on('requestfinished', async (req) => { let res = null; try { res = await req.response(); } catch (e) { /* ignore */ }
    resources.requests.push({ url: req.url(), type: req.resourceType(), status: res ? res.status() : null, contentType: res ? res.headers()['content-type'] || null : null }); });
  page.on('requestfailed', (req) => resources.requests.push({ url: req.url(), type: req.resourceType(), failed: true }));
  await page.addInitScript(() => { try { performance.setResourceTimingBufferSize(100000); } catch (e) { /* ignore */ } });
  await page.goto(url);
  await page.evaluate(async () => { await document.fonts.ready; });
  if (pageCfg.ready) await page.evaluate(pageCfg.ready);
  if (pageCfg.shim) await page.addScriptTag({ path: path.isAbsolute(pageCfg.shim) ? pageCfg.shim : path.join(ROOT, pageCfg.shim) });
  const seek = (t) => page.evaluate((t) => window.CHECKS.seek(t), t);
  const objects = () => page.evaluate(() => window.CHECKS.objects());
  const layer = (n, ids) => page.evaluate(([n, ids]) => window.CHECKS.layer(n, ids), [n, ids || []]);
  const shotMask = async (n, ids) => { await layer(n, ids); const buf = await page.screenshot({ omitBackground: true, type: 'png' }); await layer('all'); return P.alphaMask(P.decodePNG(buf)); };
  // moving frames: measured from out/camera.json when delivered (the declared scenes[].move is then ignored), else the declared move at scene start
  const hasCam = fs.existsSync(path.join(ROOT, 'out/camera.json'));
  const camAt = hasCam ? cameraSpeed(J('out/camera.json')) : null;
  const shotRGB = async () => { const img = P.decodePNG(await page.screenshot({ type: 'png' })); return img; };
  // V11 collisions of one pixel sample, in the order the sequential sampler judged them: [text, other, pixels, moving?]. K4.1 (checks-appeal A22): a text is
  // its GLYPH ink (layer 'glyph'; plate/pill excluded), dilated 2 px; graphic ink lying under the plate of a text that has one (its text-layer pixels inside
  // its box widened by 0.4 em) does not count — the plate covers it; text vs text compares glyph ink only (pairs whose boxes touch, nested pairs excluded).
  // Returns the text mask (glyph + plate) unchanged for V03, V08, C14.
  async function collide(T, isMoving) {
    const tm = await shotMask('text'), gm0 = await shotMask('graphics');
    const plated = T.filter((o) => o.role === 'badge' || o.background);
    const gl = plated.length ? await shotMask('glyph') : tm;
    let gm = gm0;
    if (plated.length) {
      const m = gm0.m.slice();
      for (const o of plated) {
        const e = 0.4 * (o.fontPx || (o.box[3] - o.box[1]));
        const x0 = Math.max(0, Math.floor(o.box[0] - e)), y0 = Math.max(0, Math.floor(o.box[1] - e)), x1 = Math.min(tm.w, Math.ceil(o.box[2] + e)), y1 = Math.min(tm.h, Math.ceil(o.box[3] + e));
        for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) { const i = y * tm.w + x; if (tm.m[i]) m[i] = 0; }
      }
      gm = { w: gm0.w, h: gm0.h, m };
    }
    const td = P.dilate(gl, 2);
    const list = [];
    for (const o of T) {
      const box = [o.box[0] - 3, o.box[1] - 3, o.box[2] + 3, o.box[3] + 3];
      const n = P.overlapIn(td, gm, box);
      if (n >= 4) list.push([o, 'graphics', n, isMoving(o)]);
    }
    const glyphOf = (mk) => (gl === tm ? mk : { w: mk.w, h: mk.h, m: mk.m.map((v, i) => (v && gl.m[i] ? 1 : 0)) });
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) {
      const a = T[i], b = T[j];
      if (a.parent === b.id || b.parent === a.id) continue;
      if (R.gapBetween(R.inflate(R.B(a), 3), R.B(b)) > 0) continue;
      const ma = P.dilate(glyphOf(await shotMask('only', [a.id])), 2), mb2 = glyphOf(await shotMask('only', [b.id]));
      const n = P.overlapIn(ma, mb2, [Math.min(a.box[0], b.box[0]) - 3, Math.min(a.box[1], b.box[1]) - 3, Math.max(a.box[2], b.box[2]) + 3, Math.max(a.box[3], b.box[3]) + 3]);
      if (n >= 4) list.push([a, 'text:' + b.tid, n, isMoving(a) || isMoving(b)]);
    }
    return { tm, list };
  }
  // K4.0 (A13): a world page (factory, D-010) draws its 3D world on a canvas the objects() contract does not list; only a covering card/bg makes a frame text-only
  const isWorld = await page.evaluate(() => typeof window.CHECKS.segments === 'function');
  return { tl, claimsArr, claims, tokens, pageCfg, illustrative, condPat, conditional, scenes, sceneAt, browser, page, url, resources, seek, objects, layer, shotMask, hasCam, camAt, shotRGB, collide, isWorld };
}

async function closeEnv(env) {
  const { page, resources } = env;
  resources.entries = await page.evaluate(() => performance.getEntriesByType('resource').map((e) => ({ url: e.name, initiator: e.initiatorType })));
  resources.fonts = await page.evaluate(() => [...document.fonts].map((f) => ({ family: f.family, status: f.status, style: f.style, weight: f.weight })));
  await env.browser.close();
}

// One sampling job: the object and pixel rules on the given sample frames (consecutive samples of one scene, or every sample). warm: restore what a
// sequential run carries into the first frame from earlier samples: the previous sample's text boxes and visible claims, and the moving collisions of the
// last pixel sample that had text (V11 persistence).
async function sampleJob(env, frameList, warm) {
  const { claims, tokens, illustrative, condPat, conditional, scenes, sceneAt, page, seek, objects, layer, shotMask, hasCam, camAt, shotRGB, collide } = env;
  const t0 = Date.now();
  const per = Object.fromEntries(scenes.map((s) => [s.id, { samples: 0, l1: [], issues: {}, examples: {} }]));
  const add = (sid, rid, ex) => { const P_ = per[sid]; P_.issues[rid] = (P_.issues[rid] || 0) + 1; ((P_.examples[rid] ||= []).length < 3) && P_.examples[rid].push(ex); };
  const textTrack = [], yearsTrack = [], motionTrack = [], textOnlyTrack = [];
  let lastMotion = '', lastTextOnly = null;
  let lastTextSig = '';
  const claimScenes = {}, claimFirst = {}, claimRoles = {}, claimFinal = {};
  const orphan = [], charObs = {}, charSides = {}, casesTrack = [], posRows = [], timeBad = [];
  let s08Without = 0, s08Lag = 0; const s08Ex = []; const s09Ex = []; let s09Missing = 0;
  const badgeFirst = {}, illFirst = {};
  let s17Without = 0; const s17Ex = [];
  // S17 at one frame: a visible conditional claim span without a visible text matching its condition's label
  function s17(objs, t, s) {
    const vis = visibleClaims(objs).filter((x) => conditional[x.sp.id]);
    if (!vis.length) return;
    const texts = objs.filter((o) => o.kind === 'text' && o.opacity > 0.5 && R.onFrame(R.B(o))).map((o) => o.text || '');
    const miss = [...new Set(vis.map((x) => x.sp.id).filter((id) => { const re = condPat[conditional[id]]; return !re || !texts.some((tx) => re.test(tx)); }))];
    if (miss.length) { s17Without++; if (s17Ex.length < 10) s17Ex.push({ t: +t.toFixed(3), scene: s.id, claims: miss }); }
  }
  const px = { collisions: [], movingCollisions: 0, safe: [], safeTravelling: 0, contrast: [], small: [], worstContrast: null, samples: 0,
    ncc: [], nccStatic: [], nccMoving: [], nccSkipped: 0 };
  let prevBoxes = new Map(), prevMovingHits = new Set(), prevVisibleShapes = new Map();
  const chartEvents = [];
  let movingSamples = 0;
  let splitRun = []; const splitRuns = [];
  const prevVisible = new Set();

  function visibleClaims(objs) {
    const out = [];
    for (const t of objs) if (t.kind === 'text' && t.opacity > 0.5) for (const sp of t.claims || []) if (sp.opacity > 0.5 && R.onFrame({ l: sp.box[0], t: sp.box[1], r: sp.box[2], b: sp.box[3] })) out.push({ sp, t });
    return out;
  }
  function recordClaims(objs, t, s) {
    for (const { sp, t: tx } of visibleClaims(objs)) {
      (claimScenes[sp.id] ||= new Set()).add(s.id);
      if (claimFirst[sp.id] === undefined || t < claimFirst[sp.id]) claimFirst[sp.id] = t;
      (claimRoles[sp.id] ||= new Set()).add(tx.role);
      const c = claims[sp.id];
      const fk = sp.id + '|' + s.id;
      if (c && !sp.roll && sp.text === String(c.display) && (claimFinal[fk] === undefined || t < claimFinal[fk])) claimFinal[fk] = t;
    }
  }
  // S08 at one frame; also first-visible times for the lag
  function s08(objs, t, s) {
    const st = R.illustrativeState(objs, { illustrative });
    if (st.badge && badgeFirst[s.id] === undefined) badgeFirst[s.id] = t;
    for (const id of st.shown) if (illFirst[s.id + '|' + id] === undefined) illFirst[s.id + '|' + id] = t;
    if (st.shown.length && !st.badge) { s08Without++; if (s08Ex.length < 10) s08Ex.push({ t: +t.toFixed(3), scene: s.id, claims: st.shown }); }
  }

  const pf0 = frameList.length ? Math.ceil(frameList[0] / PSTEP) * PSTEP : 0;
  const video = videoReader(path.join(ROOT, 'out/video.mp4'), PSTEP, 'rgb24', pf0);
  const videoY = videoReader(path.join(ROOT, 'out/video.mp4'), PSTEP, 'gray', pf0); // the coded luma plane (full resolution; no chroma subsampling in it)
  if (warm && frameList.length && frameList[0] > 0) {
    const f0 = frameList[0];
    const boxesAt = (os) => new Map(os.filter((o) => o.kind === 'text').map((o) => [o.tid, o.box]));
    await seek((f0 - STEP) / FPS);
    const op = await objects();
    prevBoxes = boxesAt(op);
    visibleClaims(op).forEach((x) => prevVisible.add(x.sp.id + '|' + x.sp.text));
    for (let g = Math.floor((f0 - 1) / PSTEP) * PSTEP; g >= 0; g -= PSTEP) {
      await seek(g / FPS);
      let og = await objects();
      const T = og.filter((o) => o.kind === 'text' && o.opacity > 0.5 && R.onFrame(R.B(o)));
      if (!T.length) continue;
      let pb = new Map();
      if (g > 0) { await seek((g - STEP) / FPS); pb = boxesAt(await objects()); await seek(g / FPS); og = await objects(); }
      const mv = new Map();
      for (const o of og) if (o.kind === 'text') { const p = pb.get(o.tid); mv.set(o.id, p ? Math.max(...o.box.map((v, i) => Math.abs(v - p[i]))) : 0); }
      const T2 = og.filter((o) => o.kind === 'text' && o.opacity > 0.5 && R.onFrame(R.B(o)));
      const { list } = await collide(T2, (o) => (mv.get(o.id) || 0) >= TEXT_MOVING);
      prevMovingHits = new Set(list.map(([o, other]) => o.tid + '|' + other));
      break;
    }
  }
  for (const f of frameList) {
    const t = f / FPS, s = sceneAt(t), PS = per[s.id];
    if (ONLY && !ONLY.has(s.id)) continue;
    if (process.env.K_PROGRESS && (f / STEP) % 50 === 0) console.error(`t=${t.toFixed(1)} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    // "in a move" (layout rules judge the settled ends of a move; V13 bounds how long a move lasts): measured camera speed, or the declared move
    const inTransition = camAt ? camAt(t) >= FAST : t - s.start < s.move;
    if (inTransition) movingSamples++;
    await seek(t);
    let objs = await objects();
    // frame-accurate refinement: when something new became visible since the last sample, look at the skipped frames too
    const vis = new Set(visibleClaims(objs).map((x) => x.sp.id + '|' + x.sp.text));
    const newly = [...vis].some((k) => !prevVisible.has(k));
    if (newly && f > 0) {
      for (let g = f - STEP + 1; g < f; g++) {
        const tg = g / FPS, sg = sceneAt(tg);
        await seek(tg);
        const og = await objects();
        recordClaims(og, tg, sg); s08(og, tg, sg); s17(og, tg, sg);
      }
      await seek(t);
      objs = await objects();
    }
    prevVisible.clear(); vis.forEach((k) => prevVisible.add(k));
    // on-screen motion of each text since the previous object sample (0.1 s): replaces the camera-move exemption of the text pixel rules
    const moved = new Map();
    for (const o of objs) if (o.kind === 'text') { const p = prevBoxes.get(o.tid); moved.set(o.id, p ? Math.max(...o.box.map((v, i) => Math.abs(v - p[i]))) : 0); }
    prevBoxes = new Map(objs.filter((o) => o.kind === 'text').map((o) => [o.tid, o.box]));
    const ctx = { tokens, allowed: s.allowed, inTransition, illustrative, claims, scene: s };
    PS.samples++;
    const issues = [...R.sceneLeak(objs, ctx), ...R.bgOverData(objs), ...(inTransition ? [] : R.unlabelledCurve(objs)), ...(inTransition ? [] : R.axisAnchors(objs, ctx)),
      ...R.greyEmphasis(objs, ctx), ...R.numberColour(objs, ctx), ...R.barProportion(objs, ctx), ...R.offToken(objs, ctx)];
    for (const i of issues) add(s.id, i.rule, { t: +t.toFixed(2), ...i });
    PS.l1.push(R.level1Count(objs));
    if (!inTransition) for (const r of R.level1Position(objs, ctx)) posRows.push({ t: +t.toFixed(2), scene: s.id, ...r });
    recordClaims(objs, t, s);
    s08(objs, t, s);
    s17(objs, t, s);
    const mb = R.moneyBasis(objs, ctx);
    if (mb.length) { s09Missing++; if (s09Ex.length < 10) s09Ex.push({ t: +t.toFixed(2), scene: s.id, ...mb[0] }); }
    for (const o of R.orphanNumbers(objs)) if (!orphan.some((x) => x.text === o.text)) orphan.push({ t: +t.toFixed(2), scene: s.id, ...o });
    const ch = R.characters(objs);
    for (const [k, v] of Object.entries(ch)) { const c = charObs[k] ||= { xs: [], colours: {}, shapes: {} }; v.colours.forEach((x) => { c.colours[x] = (c.colours[x] || 0) + 1; }); v.shapes.forEach((x) => { c.shapes[x] = (c.shapes[x] || 0) + 1; }); }
    // K2: every pair of characters seen together (names come from the page's `char`; the episode contract says which are characters and on which side)
    const cks = Object.keys(ch).sort();
    for (let i = 0; i < cks.length; i++) for (let j = i + 1; j < cks.length; j++) {
      const d = Math.min(...ch[cks[i]].xs) - Math.min(...ch[cks[j]].xs);
      if (Math.abs(d) >= 20) { const sp = (charSides[cks[i] + '|' + cks[j]] ||= { samples: 0, signs: {} }); sp.samples++; sp.signs[Math.sign(d)] = (sp.signs[Math.sign(d)] || 0) + 1; }
    }
    const cases = [...new Set(objs.filter((o) => o.case != null && o.opacity > 0.5 && R.onFrame(R.B(o))).map((o) => String(o.case)))];
    if (cases.length) casesTrack.push({ t: +t.toFixed(2), scene: s.id, cases });
    const tb = R.timeOrder(objs); if (tb.length && timeBad.length < 10) timeBad.push({ t: +t.toFixed(2), ...tb[0] });
    const years = [...new Set(objs.filter((o) => o.year != null && o.opacity > 0.5 && R.onFrame(R.B(o))).map((o) => +o.year))];
    if (years.length) yearsTrack.push({ t: +t.toFixed(2), scene: s.id, years });
    const items = objs.filter((o) => o.kind === 'text' && o.opacity > 0.5 && R.onFrame(R.B(o))).map((o) => ({ tid: o.tid, role: o.role, text: o.text }));
    const sig = JSON.stringify(items);
    if (sig !== lastTextSig) { textTrack.push({ t: +t.toFixed(2), scene: s.id, items }); lastTextSig = sig; }
    // K3.8 (A7, calibration only): a change of any visible object's box or opacity (1 px, 0.01) since the previous sample
    const mh = require('crypto').createHash('sha1').update(JSON.stringify(objs.filter((o) => !(o.kind === 'shape' && o.role === 'bg') && o.opacity > 0.05 && R.onFrame(R.B(o), 1))
      .map((o) => [o.kind === 'text' ? o.tid : o.key, o.box.map(Math.round), +o.opacity.toFixed(2)]))).digest('hex').slice(0, 12);
    if (mh !== lastMotion) { motionTrack.push({ t: +t.toFixed(2), h: mh }); lastMotion = mh; }
    // K4.0 (A13, V15): text-only sample = visible text, no visible non-text object other than bg/card, and (world page) a bg/card covering >= 60% of the frame
    const content = objs.filter((o) => o.kind !== 'text' && o.opacity > 0.05 && o.role !== 'bg' && o.role !== 'card' && R.onFrame(R.B(o), 1)).length;
    const cover = objs.some((o) => o.kind !== 'text' && (o.role === 'bg' || o.role === 'card') && o.opacity > 0.5 &&
      Math.max(0, Math.min(1920, o.box[2]) - Math.max(0, o.box[0])) * Math.max(0, Math.min(1080, o.box[3]) - Math.max(0, o.box[1])) >= 0.6 * 1920 * 1080);
    const tOnly = items.length > 0 && content === 0 && (!env.isWorld || cover);
    if (tOnly !== lastTextOnly) { textOnlyTrack.push({ t: +t.toFixed(2), scene: s.id, textOnly: tOnly }); lastTextOnly = tOnly; }

    // ---- pixel rules (every frame, no camera-move exemption; K1) ---------------------------------------------------
    // Texts moving on screen get their own criteria: V12 (the video frame shows the same sharp text as the clean render) holds for
    // every text in every sample; V08/C14 judge stationary texts (moving ones are judged by V12 and again once they settle);
    // V11 counts a moving text's collision when it persists over two pixel samples (0.2 s); V03 lets a text leave the safe area
    // only while it travels (box moving >= 4 px per 0.1 s).
    if (f % PSTEP === 0) {
      const vf = await video.get(f), vy = await videoY.get(f);
      const T = objs.filter((o) => o.kind === 'text' && o.opacity > 0.5 && R.onFrame(R.B(o)));
      if (T.length) {
        px.samples++;
        const isMoving = (o) => (moved.get(o.id) || 0) >= TEXT_MOVING;
        const { tm, list } = await collide(T, isMoving);
        const hits = new Set();
        const hit = (o, other, n, moving = isMoving(o)) => {
          const k = o.tid + '|' + other;
          hits.add(k);
          if (!moving) px.collisions.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, role: o.role, with: other, pixels: n });
          else if (prevMovingHits.has(k)) px.collisions.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, role: o.role, with: other, pixels: n, moving: true });
          else px.movingCollisions++;
        };
        for (const [o, other, n, mv] of list) hit(o, other, n, mv);
        prevMovingHits = hits;
        // V03 safe area: text ink outside the 90% rectangle, unless the text is travelling (in or out of frame)
        for (const o of T) {
          const ib = P.inkBox(tm, [o.box[0] - 2, o.box[1] - 2, o.box[2] + 2, o.box[3] + 2]);
          if (ib && (ib[0] < SAFE[0] || ib[1] < SAFE[1] || ib[2] > SAFE[2] || ib[3] > SAFE[3])) {
            if ((moved.get(o.id) || 0) >= TEXT_TRAVEL) px.safeTravelling++;
            else px.safe.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, ink: ib, inMove: inTransition });
          }
        }
        if (vf && vy) {
          // V12 text integrity: normalised cross-correlation of luma, the video's coded Y plane vs the clean page render's Y' (BT.709 weights on
          // the gamma-encoded RGB), inside each text box (+4 px)
          const clean = await shotRGB();
          const lumaAt = (buf, ch, i) => ch === 1 ? buf[i] : 0.2126 * buf[i * ch] + 0.7152 * buf[i * ch + 1] + 0.0722 * buf[i * ch + 2];
          for (const o of T) {
            if (o.opacity < 0.95) continue;
            const bx = [Math.floor(o.box[0] - 4), Math.floor(o.box[1] - 4), Math.ceil(o.box[2] + 4), Math.ceil(o.box[3] + 4)];
            if (bx[0] < 0 || bx[1] < 0 || bx[2] > 1920 || bx[3] > 1080) continue;
            const A = [], Bv = [];
            for (let y = bx[1]; y < bx[3]; y++) for (let x = bx[0]; x < bx[2]; x++) { const i = y * 1920 + x; A.push(lumaAt(clean.data, 4, i)); Bv.push(lumaAt(vy, 1, i)); }
            const mean = (v) => v.reduce((a, b) => a + b, 0) / v.length;
            const ma = mean(A), mb = mean(Bv);
            let sab = 0, saa = 0, sbb = 0;
            for (let k = 0; k < A.length; k++) { const a = A[k] - ma, b = Bv[k] - mb; sab += a * b; saa += a * a; sbb += b * b; }
            if (Math.sqrt(saa / A.length) < 8) { px.nccSkipped++; continue; } // no ink contrast in the clean render (text faded into its background)
            const ncc = sab / Math.sqrt(saa * sbb + 1e-9);
            const mv = isMoving(o) || inTransition;
            (mv ? px.nccMoving : px.nccStatic).push(ncc);
            if (!px.nccWorst || ncc < px.nccWorst.ncc) px.nccWorst = { t: +t.toFixed(2), scene: s.id, tid: o.tid, ncc: +ncc.toFixed(4), movingText: isMoving(o), cameraMove: inTransition };
            if (ncc < NCC_MIN) px.ncc.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, text: (o.text || '').slice(0, 40), ncc: +ncc.toFixed(3), movingText: isMoving(o), cameraMove: inTransition });
          }
          // V08 contrast and C14 legibility at 25%, measured on the delivered video frame, for texts standing still on screen
          const needGlyph = T.some((o) => o.role === 'badge' || o.background);
          const gl = needGlyph ? await shotMask('glyph') : tm;
          const core = P.erode(gl, 1), ring1 = P.dilate(tm, 1), ring4 = P.dilate(tm, 4);
          const ring = { w: tm.w, h: tm.h, m: ring4.m.map((v, i) => v && !ring1.m[i] ? 1 : 0) };
          for (const o of T) {
            if (o.opacity < 0.95 || isMoving(o)) continue;
            const box = [o.box[0] - 5, o.box[1] - 5, o.box[2] + 5, o.box[3] + 5];
            if (box[0] < 0 || box[1] < 0 || box[2] > 1920 || box[3] > 1080) continue;
            const hasCore = P.countIn(core, o.box) >= 12;
            const fg = P.medianColour(vf, 1920, hasCore ? core : gl, o.box);
            const inner = o.role === 'badge' ? { w: tm.w, h: tm.h, m: tm.m.map((v, i) => v && !gl.m[i] ? 1 : 0) } : ring;
            const bg = P.medianColour(vf, 1920, inner, box);
            if (!fg || !bg) continue;
            const cr = (Math.max(P.relLum(...fg), P.relLum(...bg)) + 0.05) / (Math.min(P.relLum(...fg), P.relLum(...bg)) + 0.05);
            if (px.worstContrast === null || cr < px.worstContrast.cr) px.worstContrast = { t: +t.toFixed(2), tid: o.tid, cr: +cr.toFixed(2), fg, bg };
            if (cr < 4.5) px.contrast.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, cr: +cr.toFixed(2), fg, bg, inMove: inTransition });
            // C14: font ≥ 28 px and contrast ≥ 3:1 inside the box on the 25% downscale
            const q = [Math.floor(o.box[0] / 4), Math.floor(o.box[1] / 4), Math.ceil(o.box[2] / 4), Math.ceil(o.box[3] / 4)];
            const L = [];
            for (let y = q[1]; y < q[3]; y++) for (let x = q[0]; x < q[2]; x++) {
              let r = 0, g = 0, b = 0;
              for (let dy = 0; dy < 4; dy++) for (let dx = 0; dx < 4; dx++) { const i = ((y * 4 + dy) * 1920 + x * 4 + dx) * 3; r += vf[i]; g += vf[i + 1]; b += vf[i + 2]; }
              L.push(P.relLum(r / 16, g / 16, b / 16));
            }
            L.sort((a, b) => a - b);
            const c25 = L.length ? (L[Math.floor(L.length * 0.95)] + 0.05) / (L[Math.floor(L.length * 0.05)] + 0.05) : 0;
            if ((o.fontPx || 0) < 28 || c25 < 3) px.small.push({ t: +t.toFixed(2), scene: s.id, tid: o.tid, fontPx: o.fontPx, contrastAt25: +c25.toFixed(2), inMove: inTransition });
          }
        }
      }
    }

    // ---- frozen-camera comparison: T1 chart events and C12 split view ----------------------------------------------
    let split = null, a0 = null, a1 = null;
    if (t + DT < s.start + s.dur) {
      const snap = (os) => os.filter((o) => !(o.kind === 'shape' && o.role === 'bg') && o.opacity > 0.05 && R.onFrame(R.B(o), 1)).map((o) => ({ sig: o.sig + '|' + o.opacity.toFixed(3), key: o.key, box: o.box }));
      a0 = snap(objs);
      await page.evaluate((t) => window.CHECKS.freeze(t), t);
      await seek(t + DT);
      const o1 = await objects();
      a1 = snap(o1);
      await page.evaluate(() => window.CHECKS.freeze(null));
      // T1 chart events (camera frozen, so only the data moves): a data shape (bar, series, mark, or a character's shape) that appears
      // (opacity crosses 0.5) or whose box changes by >= 1 px within [t, t + 0.1 s]. The first 0.1 s of a scene (what is there at the cut) is not an event.
      if (t - s.start >= DT - 1e-6) {
        const isData = (o) => o.kind === 'shape' && (['bar', 'series', 'mark'].includes(o.role) || o.char);
        const before = new Map(objs.filter(isData).map((o) => [o.key, o]));
        for (const o of o1.filter(isData)) {
          const p = before.get(o.key);
          const vis1 = o.opacity > 0.5 && R.onFrame(R.B(o), 1), vis0 = p && p.opacity > 0.5 && R.onFrame(R.B(p), 1);
          let kind = null;
          if (vis1 && !vis0) kind = 'appear';
          else if (vis1 && vis0 && Math.max(...o.box.map((v, i) => Math.abs(v - p.box[i]))) >= 1) kind = o.role === 'bar' ? 'bar' : o.role === 'series' ? 'line' : 'move';
          if (kind) chartEvents.push({ t: +t.toFixed(3), scene: s.id, id: o.id, role: o.role, kind, x: +((o.box[0] + o.box[2]) / 2).toFixed(1) });
        }
      }
    }
    // C12 split view: same camera, 0.1 s later (judged on settled frames; moves are bounded by V13)
    if (!inTransition && a0) {
      const count = (arr) => { const m = new Map(); for (const x of arr) m.set(x.sig, (m.get(x.sig) || 0) + 1); return m; };
      const ca = count(a0), cb = count(a1);
      const gone = a0.filter((x) => (cb.get(x.sig) || 0) < ca.get(x.sig)), came = a1.filter((x) => (ca.get(x.sig) || 0) < cb.get(x.sig));
      const changed = [], pool = [...gone];
      for (const n of came) { const i = pool.findIndex((o) => o.key === n.key); if (i < 0) { changed.push(n); continue; } const o = pool.splice(i, 1)[0]; changed.push({ box: diffBox(o.box, n.box) }); }
      changed.push(...pool);
      if (changed.length) {
        const bb = changed.reduce((u, x) => [Math.min(u[0], x.box[0]), Math.min(u[1], x.box[1]), Math.max(u[2], x.box[2]), Math.max(u[3], x.box[3])], [1e9, 1e9, -1e9, -1e9]);
        split = { w: +((Math.min(bb[2], 1920) - Math.max(bb[0], 0)) / 1920).toFixed(3), h: +((Math.min(bb[3], 1080) - Math.max(bb[1], 0)) / 1080).toFixed(3) };
      }
    }
    const isSplit = split && (split.w > SPLIT_MAX || split.h > SPLIT_MAX);
    if (isSplit && (!splitRun.length || splitRun[0].scene === s.id)) splitRun.push({ t, scene: s.id, ...split });
    else { if (splitRun.length) splitRuns.push(splitRun); splitRun = isSplit ? [{ t, scene: s.id, ...split }] : []; }
  }
  if (splitRun.length) splitRuns.push(splitRun);
  video.close();
  videoY.close();
  return { per, textTrack, motionTrack, textOnlyTrack, yearsTrack, casesTrack, posRows, chartEvents, splitRuns, claimScenes: Object.fromEntries(Object.entries(claimScenes).map(([k, v]) => [k, [...v]])),
    claimRoles: Object.fromEntries(Object.entries(claimRoles).map(([k, v]) => [k, [...v]])), claimFirst, claimFinal, badgeFirst, illFirst, orphan, charObs, charSides,
    timeBad, s08Without, s08Ex, s09Missing, s09Ex, s17Without, s17Ex, movingSamples, px };
}

// Merge scene jobs (in time order) into the state one sequential job would have built.
function mergeStates(states) {
  const M = { per: {}, textTrack: [], motionTrack: [], textOnlyTrack: [], yearsTrack: [], casesTrack: [], posRows: [], chartEvents: [], splitRuns: [], claimScenes: {}, claimRoles: {}, claimFirst: {},
    claimFinal: {}, badgeFirst: {}, illFirst: {}, orphan: [], charObs: {}, charSides: {}, timeBad: [], s08Without: 0, s08Ex: [], s09Missing: 0, s09Ex: [], s17Without: 0, s17Ex: [], movingSamples: 0,
    px: { collisions: [], movingCollisions: 0, safe: [], safeTravelling: 0, contrast: [], small: [], worstContrast: null, samples: 0, ncc: [], nccStatic: [], nccMoving: [], nccSkipped: 0 } };
  const minInto = (dst, src) => { for (const [k, v] of Object.entries(src)) if (dst[k] === undefined || v < dst[k]) dst[k] = v; };
  const unionInto = (dst, src) => { for (const [k, v] of Object.entries(src)) { const u = dst[k] ||= []; for (const x of v) if (!u.includes(x)) u.push(x); } };
  for (const S of states) {
    for (const [k, v] of Object.entries(S.per)) {
      const d = M.per[k] ||= { samples: 0, l1: [], issues: {}, examples: {} };
      d.samples += v.samples; d.l1.push(...v.l1);
      for (const [r, n] of Object.entries(v.issues)) d.issues[r] = (d.issues[r] || 0) + n;
      for (const [r, xs] of Object.entries(v.examples)) { const e = d.examples[r] ||= []; for (const x of xs) if (e.length < 3) e.push(x); }
    }
    for (const e of S.textTrack) { const last = M.textTrack[M.textTrack.length - 1]; if (!last || JSON.stringify(last.items) !== JSON.stringify(e.items)) M.textTrack.push(e); }
    for (const e of S.motionTrack) { const last = M.motionTrack[M.motionTrack.length - 1]; if (!last || last.h !== e.h) M.motionTrack.push(e); }
    for (const e of S.textOnlyTrack || []) { const last = M.textOnlyTrack[M.textOnlyTrack.length - 1]; if (!last || last.textOnly !== e.textOnly) M.textOnlyTrack.push(e); }
    for (const k of ['yearsTrack', 'casesTrack', 'posRows', 'chartEvents', 'splitRuns']) M[k].push(...S[k]);
    unionInto(M.claimScenes, S.claimScenes); unionInto(M.claimRoles, S.claimRoles);
    minInto(M.claimFirst, S.claimFirst); minInto(M.claimFinal, S.claimFinal); minInto(M.badgeFirst, S.badgeFirst); minInto(M.illFirst, S.illFirst);
    for (const o of S.orphan) if (!M.orphan.some((x) => x.text === o.text)) M.orphan.push(o);
    for (const [k, v] of Object.entries(S.charObs)) {
      const c = M.charObs[k] ||= { xs: [], colours: {}, shapes: {} };
      for (const [x, n] of Object.entries(v.colours)) c.colours[x] = (c.colours[x] || 0) + n;
      for (const [x, n] of Object.entries(v.shapes)) c.shapes[x] = (c.shapes[x] || 0) + n;
    }
    for (const [k, v] of Object.entries(S.charSides)) { const d = M.charSides[k] ||= { samples: 0, signs: {} }; d.samples += v.samples; for (const [x, n] of Object.entries(v.signs)) d.signs[x] = (d.signs[x] || 0) + n; }
    for (const k of ['timeBad', 's08Ex', 's09Ex', 's17Ex']) for (const x of S[k]) if (M[k].length < 10) M[k].push(x);
    for (const k of ['s08Without', 's09Missing', 's17Without', 'movingSamples']) M[k] += S[k];
    const a = M.px, b = S.px;
    for (const k of ['collisions', 'safe', 'contrast', 'small', 'ncc', 'nccStatic', 'nccMoving']) a[k].push(...b[k]);
    for (const k of ['movingCollisions', 'safeTravelling', 'samples', 'nccSkipped']) a[k] += b[k];
    if (b.worstContrast && (a.worstContrast === null || b.worstContrast.cr < a.worstContrast.cr)) a.worstContrast = b.worstContrast;
    if (b.nccWorst && (!a.nccWorst || b.nccWorst.ncc < a.nccWorst.ncc)) a.nccWorst = b.nccWorst;
  }
  return M;
}

function aggregate(env, S, seconds) {
  const { scenes, hasCam, resources, url } = env;
  const { per, splitRuns, illFirst, badgeFirst, s08Without, s08Ex, s09Missing, s09Ex, s17Without, s17Ex, posRows, px, charObs, charSides, timeBad, chartEvents, movingSamples, textTrack, motionTrack,
    yearsTrack, casesTrack, claimScenes, claimFirst, claimRoles, claimFinal } = S;
  // ---- aggregate --------------------------------------------------------------------------------
  const rules = {};
  const sum = (rid) => { const sc = Object.entries(per).filter(([, P_]) => P_.issues[rid]); return { framesFlagged: sc.reduce((a, [, P_]) => a + P_.issues[rid], 0), scenes: sc.map(([id, P_]) => `${id} (${P_.issues[rid]})`), examples: sc.flatMap(([, P_]) => P_.examples[rid]).slice(0, 5) }; };
  for (const rid of ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C15']) rules[rid] = sum(rid);
  const l1 = scenes.filter((s) => per[s.id].samples).map((s) => { const xs = per[s.id].l1; const one = xs.filter((n) => n === 1).length / Math.max(1, xs.length); return { id: s.id, chart: !!s.chart, dur: s.dur, one, max: Math.max(0, ...xs) }; });
  rules.C10 = { failing: l1.filter((r) => r.chart && r.dur >= 2 && !(r.one >= 0.5 && r.max <= 1)).map((r) => `${r.id} (one l1 in ${Math.round(r.one * 100)}%, max ${r.max})`) };
  rules.C12 = { violations: splitRuns.map((r) => ({ scene: r[0].scene, start: +r[0].t.toFixed(2), durationS: +(r.length * STEP / FPS).toFixed(2), maxW: Math.max(...r.map((x) => x.w)), maxH: Math.max(...r.map((x) => x.h)) })).filter((v) => v.durationS >= SPLIT_MIN_RUN) };
  let maxLag = 0; const lagEx = [];
  for (const [k, ti] of Object.entries(illFirst)) { const sid = k.split('|')[0]; const tb_ = badgeFirst[sid]; const lag = tb_ === undefined ? 999 : Math.round((tb_ - ti) * FPS); if (lag > maxLag) maxLag = lag; if (lag > 0 && lagEx.length < 10) lagEx.push({ key: k, claimFirst: ti, badgeFirst: tb_ ?? null, lagFrames: lag }); }
  rules.S08 = { framesWithout: s08Without, maxLagFrames: maxLag, examples: [...s08Ex, ...lagEx] };
  rules.S09 = { framesMissing: s09Missing, examples: s09Ex };
  rules.S17 = { framesWithout: s17Without, examples: s17Ex };
  rules.V02 = { samples: posRows.length, ok: posRows.filter((r) => r.ok).length, examples: posRows.filter((r) => !r.ok).slice(0, 8) };
  // one example per distinct (scene, text, other) — first time seen — so the report names every offender
  const distinct = (xs, key, n = 40) => { const seen = new Map(); for (const x of xs) { const k = key(x); if (!seen.has(k)) seen.set(k, { ...x, samples: 0 }); seen.get(k).samples++; } return [...seen.values()].slice(0, n); };
  rules.V03 = { violations: px.safe.length, travellingSamples: px.safeTravelling, examples: distinct(px.safe, (x) => x.scene + '|' + x.tid) };
  rules.V08 = { violations: px.contrast.length, worst: px.worstContrast, examples: distinct(px.contrast, (x) => x.scene + '|' + x.tid) };
  rules.V11 = { violations: px.collisions.length, movingNotPersistent: px.movingCollisions, byRole: px.collisions.reduce((m, c) => { m[c.role] = (m[c.role] || 0) + 1; return m; }, {}), examples: distinct(px.collisions, (x) => x.scene + '|' + x.tid + '|' + x.with) };
  rules.C14 = { violations: px.small.length, examples: distinct(px.small, (x) => x.scene + '|' + x.tid) };
  const q = (xs, p) => { if (!xs.length) return null; const v = [...xs].sort((a, b) => a - b); return +v[Math.min(v.length - 1, Math.floor(p * v.length))].toFixed(3); };
  rules.V12 = { threshold: NCC_MIN, violations: px.ncc.length, textSamples: px.nccStatic.length + px.nccMoving.length, skippedFlat: px.nccSkipped,
    staticMedian: q(px.nccStatic, 0.5), staticP05: q(px.nccStatic, 0.05), movingMedian: q(px.nccMoving, 0.5), movingP05: q(px.nccMoving, 0.05), movingSamples: px.nccMoving.length, lowest: px.nccWorst || null,
    worst: [...px.ncc].sort((a, b) => a.ncc - b.ncc).slice(0, 10), examples: distinct(px.ncc, (x) => x.scene + '|' + x.tid) };
  const mode = (o) => Object.entries(o || {}).sort((a, b) => b[1] - a[1])[0];
  const characters = {};
  for (const k of Object.keys(charObs)) { const mc = mode(charObs[k].colours), ms = mode(charObs[k].shapes); const n = Object.values(charObs[k].colours).reduce((a, b) => a + b, 0); const ns = Object.values(charObs[k].shapes).reduce((a, b) => a + b, 0);
    characters[k] = { mainColour: mc && mc[0], colourShare: mc ? mc[1] / n : 0, mainShape: ms && ms[0], shapeShare: ms ? ms[1] / ns : 0 }; }
  rules.V04 = { characters, pairs: charSides, timeOrderViolations: timeBad };
  const orphan = S.orphan.slice(0, 200);
  const out = {
    root: ROOT, step: STEP, pixelStep: PSTEP, samples: Object.values(per).reduce((a, p) => a + p.samples, 0), pixelSamples: px.samples, seconds,
    rules, characters, chartEvents, movingSamples, cameraFromFile: hasCam, resources, pageUrl: url,
    textTrack, motionTrack, textOnlyTrack: S.textOnlyTrack, yearsTrack, casesTrack, orphanNumbers: orphan,
    claimScenes: Object.fromEntries(Object.entries(claimScenes).map(([k, v]) => [k, [...v]])), claimFirst, claimRoles: Object.fromEntries(Object.entries(claimRoles).map(([k, v]) => [k, [...v]])), claimFinal,
    scenes: Object.fromEntries(Object.entries(per).map(([k, v]) => [k, { samples: v.samples, issues: v.issues }])),
  };

  return out;
}

// Sample frames of each scene (contiguous in time); sequential when one job.
function sceneFrames(env, frames) {
  const groups = [];
  for (let f = 0; f < frames; f += STEP) {
    const s = env.sceneAt(f / FPS);
    if (ONLY && !ONLY.has(s.id)) continue;
    const g = groups[groups.length - 1];
    if (g && g.id === s.id) g.frames.push(f);
    else { if (groups.some((x) => x.id === s.id)) throw new Error(`scene ${s.id} is not contiguous in time: parallel sampling needs contiguous scenes`); groups.push({ id: s.id, frames: [f] }); }
  }
  return groups;
}

const sha = (x) => require('crypto').createHash('sha256').update(x).digest('hex');
// per-scene cache key: sampler code, steps, episode inputs the sampler reads, the scene, and the video packets (MD5) from the key frame at or before the
// scene's first sample to the key frame after its last one (closed GOPs: every sampled frame decodes from these packets alone). Page files are checked on
// read: the job records every local file the page served (sha256), and a changed file is a miss.
function videoPackets() {
  const r = require('child_process').spawnSync('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_data_hash', 'MD5', '-show_entries', 'packet=pts_time,flags,data_hash',
    '-of', 'csv=p=0', path.join(ROOT, 'out/video.mp4')], { maxBuffer: 1 << 28 });
  return String(r.stdout).trim().split('\n').map((l) => { const [t, h, fl] = l.split(','); return { t: +t, key: (fl || '').includes('K'), h }; });
}
function sceneKey(base, pk, frames) {
  const a = frames[0] / FPS, b = frames[frames.length - 1] / FPS;
  let i0 = 0;
  for (let i = 0; i < pk.length; i++) if (pk[i].key && pk[i].t <= a + 1e-6) i0 = i;
  let i1 = pk.length;
  for (let i = i0 + 1; i < pk.length; i++) if (pk[i].key && pk[i].t > b + 1e-6) { i1 = i; break; }
  return sha(base + '|' + frames.join(',') + '|' + pk.slice(i0, i1).map((p) => p.h).join(''));
}
function localFiles(env) {
  const out = {};
  const u0 = new URL(env.url);
  for (const r of env.resources.requests) {
    try {
      const u = new URL(r.url);
      if (u.origin !== u0.origin && u.protocol !== 'file:') continue;
      const rel = decodeURIComponent(u.pathname).replace(/^\//, '');
      const candidates = u.protocol === 'file:' ? [decodeURIComponent(u.pathname)] : [path.join(ROOT, rel), path.join(ROOT, '..', '..', rel)];
      const p_ = candidates.find((c) => fs.existsSync(c) && fs.statSync(c).isFile());
      out[r.url] = p_ ? sha(fs.readFileSync(p_)) : null;
    } catch (e) { /* not a URL */ }
  }
  return out;
}
const filesStillSame = (files) => Object.entries(files || {}).every(([u, h]) => { try { const x = localFiles({ url: u, resources: { requests: [{ url: u }] } }); return x[u] === h; } catch (e) { return false; } });

async function run() {
  const t0 = Date.now();
  const tl = J('out/timeline.json');
  const frames = Math.round(tl.total * FPS);
  if (JOBS === 1) {
    const env = await openEnv();
    const fl = [];
    for (let f = 0; f < frames; f += STEP) if (!ONLY || ONLY.has(env.sceneAt(f / FPS).id)) fl.push(f);
    const S = await sampleJob(env, fl, false);
    await closeEnv(env);
    return write(aggregate(env, S, +((Date.now() - t0) / 1000).toFixed(1)));
  }
  const envs = [];
  for (let i = 0; i < JOBS; i++) envs.push(await openEnv());
  const groups = sceneFrames(envs[0], frames);
  const cdir = path.join(ROOT, 'out', 'checks', 'cache', 'page-scenes');
  fs.mkdirSync(cdir, { recursive: true });
  const code = ['sampler.js', 'objrules.js', 'pixels.js'].map((f) => fs.readFileSync(path.join(__dirname, f), 'utf8')).join('');
  const inputs = ['out/timeline.json', 'out/claims.json', 'design/tokens.json', 'out/page.json', 'out/camera.json'].map((f) => fs.existsSync(path.join(ROOT, f)) ? fs.readFileSync(path.join(ROOT, f), 'utf8') : '-').join('|');
  const base = sha(code + '|' + STEP + '|' + PSTEP + '|' + inputs);
  const pk = NO_CACHE ? [] : videoPackets();
  const states = new Array(groups.length);
  // longest scenes first (better balance); merged in time order
  const order = groups.map((g, i) => i).sort((x, y) => groups[y].frames.length - groups[x].frames.length || x - y);
  let next = 0, hits = 0;
  await Promise.all(envs.map(async (env) => {
    while (next < order.length) {
      const k = order[next++], g = groups[k];
      const key = NO_CACHE ? null : sceneKey(base, pk, g.frames), cf = key && path.join(cdir, key + '.json');
      if (cf && fs.existsSync(cf)) {
        const c = JSON.parse(fs.readFileSync(cf, 'utf8'));
        if (filesStillSame(c.files)) { states[k] = c.state; hits++; continue; }
      }
      const n0 = env.resources.requests.length;
      states[k] = await sampleJob(env, g.frames, true);
      if (process.env.K_PROGRESS) console.error(`scene ${g.id} done ${((Date.now() - t0) / 1000).toFixed(0)}s`);
      if (cf) fs.writeFileSync(cf, JSON.stringify({ state: states[k], files: localFiles({ url: env.url, resources: { requests: env.resources.requests } }) }));
    }
  }));
  for (const env of envs) await closeEnv(env);
  // resources: the union of what every browser loaded (F12 compares the set of loaded files and font families)
  const res = { requests: [], entries: [], fonts: [] };
  for (const k of Object.keys(res)) { const seen = new Set(); for (const env of envs) for (const x of env.resources[k]) { const j = JSON.stringify(x); if (!seen.has(j)) { seen.add(j); res[k].push(x); } } }
  const env = { ...envs[0], resources: res };
  const out = aggregate(env, mergeStates(states), +((Date.now() - t0) / 1000).toFixed(1));
  out.jobs = JOBS; out.sceneCacheHits = hits; out.sceneJobs = groups.length;
  return write(out);
}

function write(out) {
  fs.mkdirSync(path.join(ROOT, 'out', 'checks'), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'out', 'checks', ONLY ? 'page-partial.json' : 'page.json'), JSON.stringify(out));
  console.log(JSON.stringify({ seconds: out.seconds, samples: out.samples, pixelSamples: out.pixelSamples, summary: Object.fromEntries(Object.entries(out.rules).map(([k, v]) => [k, v.framesFlagged ?? v.violations ?? v.framesWithout ?? v.failing?.length ?? ''])) }));
}


function diffBox(a, b) {
  const same = (i) => Math.abs(a[i] - b[i]) < 0.5;
  const x = same(0) && !same(2) ? [Math.min(a[2], b[2]), Math.max(a[2], b[2])] : same(2) && !same(0) ? [Math.min(a[0], b[0]), Math.max(a[0], b[0])] : [Math.min(a[0], b[0]), Math.max(a[2], b[2])];
  const y = same(1) && !same(3) ? [Math.min(a[3], b[3]), Math.max(a[3], b[3])] : same(3) && !same(1) ? [Math.min(a[1], b[1]), Math.max(a[1], b[1])] : [Math.min(a[1], b[1]), Math.max(a[3], b[3])];
  const onlyX = same(1) && same(3), onlyY = same(0) && same(2);
  return [onlyY ? Math.min(a[0], b[0]) : x[0], onlyX ? Math.min(a[1], b[1]) : y[0], onlyY ? Math.max(a[2], b[2]) : x[1], onlyX ? Math.max(a[3], b[3]) : y[1]];
}

if (require.main === module) run().then(() => process.exit(0)).catch((e) => { console.error(e); process.exit(1); });
module.exports = { diffBox };

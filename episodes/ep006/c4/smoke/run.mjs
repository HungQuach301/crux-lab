// Tập 6 · C4 · kiểm khai scene.js KHÔNG render (không WebGL, không Playwright): chạy frame(t) mỗi 0,1 s với three thật + renderer giả + canvas 2D giả.
// Báo: lỗi JS, vi phạm quy tắc 1 (log.violations của core.js), chữ < 48 px, hộp chữ giao nhau (đo gần đúng 0,55 em/ký tự), nhãn hiện < max(1 s, từ/3),
// chữ số trên hình không thuộc display của c4/gen/claims.json.  Dùng: node --import ./episodes/ep006/c4/smoke/register.mjs episodes/ep006/c4/smoke/run.mjs <đoạn> [bước s]
// Cần three: (cd toolkit/factory/world/vendor && npm ci).
import fs from 'node:fs';
const ROOT = '/home/user/crux-lab';
function ctx2d(cv) {
  let T = { a: 1, b: 0, c: 0, d: 1, e: 0, f: 0 }; const st = [];
  const px = () => { const m = /(\d+(?:\.\d+)?)px/.exec(c.font || ''); return m ? +m[1] : 10; };
  const c = new Proxy({
    font: '10px Inter', canvas: cv, globalAlpha: 1, fillStyle: '#000', strokeStyle: '#000', lineWidth: 1,
    setTransform(a, b, cc, d, e, f) { if (typeof a === 'object') T = { ...a }; else T = { a, b, c: cc, d, e, f }; },
    getTransform() { return { ...T }; }, save() { st.push({ ...T }); }, restore() { if (st.length) T = st.pop(); },
    measureText(s) { return { width: String(s).length * px() * 0.55 }; },
    createLinearGradient() { return { addColorStop() {} }; }, createRadialGradient() { return { addColorStop() {} }; },
    getImageData(x, y, w, h) { return { data: new Uint8ClampedArray(w * h * 4), width: w, height: h }; }, putImageData() {}, createImageData(w, h) { return { data: new Uint8ClampedArray(w * h * 4), width: w, height: h }; },
  }, { get(o, k) { if (k in o) return o[k]; return () => {}; }, set(o, k, v) { o[k] = v; return true; } });
  return c;
}
globalThis.document = {
  createElement(tag) { const cv = { width: 300, height: 150, style: {}, getContext() { return this._c || (this._c = ctx2d(this)); }, addEventListener() {} }; return cv; },
  body: { appendChild() {} }, fonts: { load: async () => [], ready: Promise.resolve() },
};
globalThis.window = globalThis;
globalThis.fetch = async (u) => ({ json: async () => JSON.parse(fs.readFileSync(ROOT + u, 'utf8')) });
const seg = process.argv[2], step = +(process.argv[3] || 0.1);
const S = JSON.parse(fs.readFileSync(`${ROOT}/episodes/ep006/world/c4/${seg}/spine.json`, 'utf8'));
const mod = await import(`file://${ROOT}/episodes/ep006/world/c4/${seg}/scene.js`);
const { frame } = await mod.boot(108);
const viol = [], small = [], over = [], err = []; const vis = new Map();
const CLA = JSON.parse(fs.readFileSync(`${ROOT}/episodes/ep006/c4/gen/claims.json`, 'utf8')).claims.map((c) => String(c.display)).filter((d) => /\d/.test(d)).sort((a, b) => b.length - a.length);
let n = 0;
for (let t = 0; t <= S.total + 1e-6; t += step) {
  let log;
  try { log = frame(+t.toFixed(3)); } catch (e) { err.push([t.toFixed(2), String(e.stack).split('\n').slice(0, 3).join(' | ')]); if (err.length > 3) break; continue; }
  n++; globalThis.NT = (globalThis.NT || 0) + (log.texts || []).length;
  for (const v of log.violations || []) viol.push([+t.toFixed(2), v.text, v.chartW]);
  const tx = (log.texts || []).filter((x) => x.opacity > 0.3);
  const seen = new Set(tx.filter((x) => x.opacity > 0.5 && x.kind !== 'chrome').map((x) => x.text));
  for (const k of seen) { const v = vis.get(k) || { run: 0, best: 0, last: -9 }; v.run = (t - v.last < step * 1.5) ? v.run + step : step; v.last = t; v.best = Math.max(v.best, v.run); vis.set(k, v); }
  for (const x of tx) if (x.kind !== 'chrome' && x.px < 48) small.push([+t.toFixed(2), x.text, x.px]);
  for (let i = 0; i < tx.length; i++) for (let j = i + 1; j < tx.length; j++) {
    const A = tx[i].box, B = tx[j].box, w = Math.min(A[2], B[2]) - Math.max(A[0], B[0]), h = Math.min(A[3], B[3]) - Math.max(A[1], B[1]);
    if (w > 4 && h > 4) over.push([+t.toFixed(2), tx[i].text, tx[j].text]);
  }
}
const uniq = (a, k) => { const m = new Map(); for (const x of a) { const key = k(x); if (!m.has(key)) m.set(key, x); } return [...m.values()]; };
const short = [...vis].filter(([k, v]) => v.best + 1e-6 < Math.max(1, k.split(/\s+/).length / 3)).map(([k, v]) => [k, +v.best.toFixed(2)]);
const unclaimed = [...vis.keys()].filter((k) => { let r = k; for (const d of CLA) r = r.split(d).join(' '); return /\d/.test(r); });
console.log(JSON.stringify({ seg, frames: n, short, unclaimed, texts: globalThis.NT, errors: err, rule1: uniq(viol, (x) => x[1]).slice(0, 12), rule1_n: viol.length,
  small: uniq(small, (x) => x[1]).slice(0, 8), overlaps_n: over.length, overlaps: uniq(over, (x) => x[1] + '|' + x[2]).slice(0, 25) }, null, 1));

// Nhà máy · TRANG KIỂM CỦA TẬP (hợp đồng window.CHECKS, checks/CONTRACT.md §Page) — chạy trong trang một-file do episode_page.py sinh.
// window.__CRUX = {mods:[{src}], order:[i…] (phụ thuộc trước), core: i, segs:[{id, mod, t0, t1}] (giây của tập), json:{'/path': text}, claims:[{id, display}], fps}
// - Mọi module (three, core.js, lib3d.js, scene.js của mỗi đoạn, thư viện của tập) nạp từ blob: URL (trang mở bằng file://, không cần máy chủ);
//   fetch() của loadJSON trả JSON đã nhúng. Cùng scene.js + frame(t) đã render video → seek(t) = khung của video (trước dither 2D).
// - seek(t): chọn đoạn chứa t (t0 ≤ t < t1), dựng frame(t − t0) ở ?res (mặc định 1080 → 1920×1080), hiện canvas của đoạn.
// - objects(): đối tượng chữ / hình theo thứ tự vẽ (core.Overlay ghi khi CK.on). layer(name, ids): dựng lại cùng khung chỉ với lớp đó.
// - freeze(t): giữ trạng thái máy quay của khung t (vị trí, hướng, fov) cho các lần seek sau trong cùng đoạn; freeze(null) thả.
const B = window.__CRUX;
const realFetch = window.fetch.bind(window);
window.fetch = async (u, ...a) => {
  const p = decodeURIComponent(new URL(String(u), 'http://crux.local/').pathname);
  if (Object.prototype.hasOwnProperty.call(B.json, p)) return new Response(B.json[p], { headers: { 'Content-Type': 'application/json' } });
  return realFetch(u, ...a);
};
const urls = [];
for (const i of B.order) urls[i] = URL.createObjectURL(new Blob([B.mods[i].src.replace(/__CRUXMOD_(\d+)__/g, (_, k) => urls[+k])], { type: 'text/javascript' }));
const { CK } = await import(urls[B.core]);
const q = new URLSearchParams(location.search), res = +(q.get('res') || 1080);
CK.on = true; CK.claims = B.claims;
if (B.view) CK.view = B.view;   // test / xem trước khung dọc (core.CK.view)
await document.fonts.ready;
const segs = [];
for (const s of B.segs) {
  const m = await import(urls[s.mod]);
  const S = await m.boot(res);
  S.canvas.style.display = 'none';
  segs.push({ ...s, S });
}
const EPS = 1e-6;
const pick = (t) => segs.find((g) => t >= g.t0 - EPS && t < g.t1 - EPS) || (t >= segs[segs.length - 1].t1 - EPS ? segs[segs.length - 1] : null);
const local = (g, t) => Math.min(Math.max(0, t - g.t0), g.t1 - g.t0 - 0.5 / (B.fps || 30));
let st = { t: null, g: null, lt: 0, log: null }, frozen = null, shown = null;
function show(g) { if (shown === g) return; if (shown) shown.S.canvas.style.display = 'none'; if (g) g.S.canvas.style.display = 'block'; shown = g; }
function draw(g, lt, mode = 'all', ids = null) {
  const keep = CK.freezeCam;
  if (frozen && frozen !== g) CK.freezeCam = null;   // máy quay giữ ở đoạn khác: không áp
  CK.mode = mode; CK.ids = ids ? new Set(ids) : null;
  try { return g.S.frame(lt); } finally { CK.mode = 'all'; CK.ids = null; CK.freezeCam = keep; }
}
window.CHECKS = {
  seek(t) {
    const g = pick(t); show(g);
    if (!g) { st = { t, g: null, lt: 0, log: { objects: [] } }; return false; }
    const lt = local(g, t); st = { t, g, lt, log: draw(g, lt) }; return true;
  },
  freeze(t) {
    if (t === null || t === undefined) { CK.freezeCam = null; frozen = null; return true; }
    const g = pick(t); if (!g) return false;
    CK.freezeCam = null; frozen = null; draw(g, local(g, t)); CK.freezeCam = CK.lastCam; frozen = g;   // canvas giữ khung t cho tới seek kế tiếp
    return true;
  },
  objects() { return ((st.log && st.log.objects) || []).map(({ n, kindHint, ...o }) => o); },
  layer(name, ids) { if (!st.g) return false; draw(st.g, st.lt, name || 'all', name === 'only' ? ids || [] : null); return true; },
  segments: () => segs.map(({ id, t0, t1 }) => ({ id, t0, t1 })),
  log: () => st.log,   // nhật ký khung của core.Overlay (chẩn đoán)
};
window.READY = true;

// Mốc V · LÕI "một thế giới, hai chế độ máy quay" (D-010).
//  - Máy quay: tư thế đặt tên (scene khai báo toạ độ), ĐỘNG TÁC HỮU HẠN giữa hai nhịp lấy từ spine.moves
//    {verb: push|pull|pan|mode, from, to, t0, t1, reason, sound}. Ngoài cửa sổ động tác máy quay ĐỨNG YÊN (quy tắc 2).
//  - Trọng số chế độ đồ thị chartW ∈ [0,1] nội suy theo tư thế (pose.chart = 0 thế giới, 1 đồ thị) — quy tắc 1 kiểm qua nhật ký.
//  - Lớp phủ 2D: chữ sắc ở thiết kế 1920×1080, vẽ ở độ phân giải bất kỳ; mọi chữ được ghi vào nhật ký (hộp, cỡ px, độ mờ, loại).
//    Loại 'number' / 'compare' chỉ hợp lệ khi chartW ≥ 0,95 — vi phạm ghi vào log.violations (quy tắc 1).
//  - Lớp bắt buộc (quy tắc 5): ILLUSTRATIVE, "US only · history, not a forecast", nguồn, đối trọng — chữ 48 px trên nền mờ, vị trí cố định.
import * as THREE from 'three';
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => (b <= a ? (t >= a ? 1 : 0) : clamp((t - a) / (b - a)));
export const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
export const easeOut = (t, a, b) => 1 - Math.pow(1 - lin(t, a, b), 3);
export const mix = (a, b, x) => a + (b - a) * x;
export function rgba(hex, a) { const n = parseInt(hex.slice(1, 7), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }
export const C = { bg: '#0E1116', surface: '#171B22', grid: '#2A303B', ink: '#F2F4F7', muted: '#9AA4B2', accent: '#4C8DFF', warn: '#F2B441', costlier: '#C72323', cushion: '#269783', chrome: '#C9D1DC' };

export async function loadJSON(u) { return (await fetch(u)).json(); }
export async function fonts() { for (const w of [400, 600, 700]) await document.fonts.load(`${w} 48px Inter`); await document.fonts.ready; }

// ------------------------------------------------------------------ máy quay
export function Camera(poses, moves, aspect = 16 / 9) {
  const cam = new THREE.PerspectiveCamera(35, aspect, 0.1, 400);
  const P = (name) => { const p = poses[name]; if (!p) throw new Error('pose ' + name); return p; };
  const lerpPose = (a, b, x) => ({ pos: a.pos.map((v, i) => mix(v, b.pos[i], x)), tgt: a.tgt.map((v, i) => mix(v, b.tgt[i], x)),
    fov: Math.exp(mix(Math.log(a.fov), Math.log(b.fov), x)), chart: mix(a.chart || 0, b.chart || 0, x) });
  // F-1 (opt-in, move.style === 'fly'; mặc định 'dissolve' = lerpPose ở trên, KHÔNG đổi): máy quay ĐI THẬT từ tư thế này sang tư thế kia.
  //  - vị trí + điểm nhìn theo đường cong bậc hai qua tư thế `via` (nếu có) ở x = 0,5 — máy đi ngang qua vật thế giới, không trượt thẳng;
  //  - dolly-zoom: chiều cao khung ở điểm nhìn h = 2·d·tan(fov/2) nội suy log giữa hai tư thế, fov = 2·atan(h / 2d) theo khoảng cách thật
  //    → lại gần thì góc rộng (thị sai khi đi qua vật), lùi xa thì tiêu cự dài ≈ trực giao ở tư thế đồ thị (fov của tư thế đích ở x = 1);
  //  - chartW chỉ dâng ở nửa cuối khi vào đồ thị (rời đồ thị: rơi ở nửa đầu) → cổng số (chartW ≥ 0,95, quy tắc 1) chỉ mở khi đã chính diện.
  const H = (p) => 2 * Math.hypot(...p.pos.map((v, i) => v - p.tgt[i])) * Math.tan(p.fov * Math.PI / 360);
  const bez = (a, v, b, x) => a.map((p, i) => { const c = v ? 2 * v[i] - (p + b[i]) / 2 : (p + b[i]) / 2; return (1 - x) * (1 - x) * p + 2 * (1 - x) * x * c + x * x * b[i]; });
  function flyPose(a, b, v, x) {
    const pos = bez(a.pos, v && v.pos, b.pos, x), tgt = bez(a.tgt, v && v.tgt, b.tgt, x), d = Math.hypot(...pos.map((p, i) => p - tgt[i]));
    const h = Math.exp(mix(Math.log(H(a)), Math.log(H(b)), x)), ca = a.chart || 0, cb = b.chart || 0;
    return { pos, tgt, fov: 2 * Math.atan(h / (2 * d)) * 180 / Math.PI, chart: mix(ca, cb, cb >= ca ? ease(x, 0.5, 1) : ease(x, 0, 0.5)), fly: true };
  }
  const ms = [...moves].sort((a, b) => a.t0 - b.t0);
  function poseAt(t) {
    let cur = P(ms.length ? ms[0].from : Object.keys(poses)[0]);
    for (const m of ms) {
      if (t < m.t0) break;
      cur = t >= m.t1 ? P(m.to) : m.style === 'fly' ? flyPose(P(m.from), P(m.to), m.via ? P(m.via) : null, ease(t, m.t0, m.t1)) : lerpPose(P(m.from), P(m.to), ease(t, m.t0, m.t1));
      if (t < m.t1) break;
    }
    return cur;
  }
  return {
    cam, poseAt, flyPose,
    apply(t) {
      const p = poseAt(t); cam.fov = p.fov; cam.position.set(...p.pos); cam.lookAt(...p.tgt); cam.updateProjectionMatrix(); cam.updateMatrixWorld();
      return p;
    },
    moving(t) { return ms.some((m) => t > m.t0 && t < m.t1); },
  };
}

// ------------------------------------------------------------------ CHECKS + khung dọc + dither (nhà máy; mặc định TẮT trừ dither → khung render như cũ)
// CK.on        trang kiểm (episode_page.py): mỗi chữ / nét / hình đánh dấu được ghi thành đối tượng hợp đồng window.CHECKS
//              (checks/CONTRACT.md §Page) vào log.objects, theo thứ tự vẽ; không đổi điểm ảnh.
// CK.mode      lớp đang vẽ — layer() của hợp đồng: 'all' | 'text' (chữ + nền pill) | 'glyph' (chỉ nét chữ) | 'graphics' (mọi hình trừ nền: 3D
//              không nền/sàn, nét/tô của lớp phủ trừ dải nền chrome và lớp phủ cả khung) | 'only' (chỉ CK.ids, nét chữ) | 'notext'.
// CK.claims    [{id, display}] (out/claims.json): khoảng claim trong chữ = chuỗi display xuất hiện nguyên vẹn (claimSpans).
// CK.freezeCam trạng thái máy quay giữ cố định (freeze(t) của hợp đồng); CK.lastCam = máy quay của lần render gần nhất.
// CK.view      null = khung ngang 1920×1080; {orient:'v', s, cy, hook, cws:[{id,text}], t0} = Short dọc 1080×1920 DỰNG LẠI từ cùng cảnh:
//              máy quay giữ nguyên, khung là cửa sổ dọc của mặt phẳng thiết kế (rộng 1080/s, tâm x 960) → 3D render đúng cửa sổ đó
//              (setViewOffset), lớp phủ vẽ qua cùng phép biến đổi; chữ ≥ 56 px (nâng), nằm trong vùng an toàn dọc (đẩy vào, xuống dòng);
//              lớp bắt buộc dọc của nhà máy: móc, ILLUSTRATIVE + "US only · history, not a forecast" trên MỌI khung có số, đối trọng xoay 3 s.
// CK.dither    0 tắt · 1 dither trong shader (material.dithering của three: nhiễu trước khi lượng tử 8 bit) · 2 (mặc định) = 1 + hạt nhiễu
//              ±4 mã CỐ ĐỊNH theo ô 2×2 ở điểm tối của khung ghép (darkDither; chỉ khi render, không ở trang kiểm) — chống banding gradient tối (checks F08).
export const CK = { on: false, mode: 'all', ids: null, claims: null, freezeCam: null, lastCam: null, view: null, dither: 2, shapes3d: [] };
export const VSAFE = { x0: 72, y0: 200, x1: 1008, y1: 1600 }, VFLOOR = 56, VZONE = { y0: 430, y1: 1410 };   // = qc.py SAFE['v'], FLOOR['v']
const TAG_RE = /^ILLUSTRATIVE$|history, not a forecast/;
const lumHex = (hex) => { const n = parseInt(String(hex).slice(1, 7), 16), f = (c) => { c /= 255; return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4; };
  return 0.2126 * f(n >> 16) + 0.7152 * f((n >> 8) & 255) + 0.0722 * f(n & 255); };
export const contrastHex = (a, b) => { const x = lumHex(a), y = lumHex(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
const r1 = (v) => +(+v).toFixed(1);
const hexOf = (c) => (typeof c === 'string' && /^#[0-9a-f]{6}$/i.test(c) ? c.toLowerCase() : null);

// khoảng claim trong một chuỗi: display (có chữ số) xuất hiện nguyên vẹn, không dính chữ/số hai bên; dài trước, không chồng nhau → [{id, i, d}]
export function claimSpans(s, claims) {
  const out = [];
  const list = [...(claims || [])].filter((c) => /\d/.test(String(c.display ?? ''))).sort((a, b) => String(b.display).length - String(a.display).length);
  for (const c of list) {
    const d = String(c.display);
    for (let i = s.indexOf(d); i >= 0; i = s.indexOf(d, i + 1)) {
      const pre = s[i - 1], post = s[i + d.length], post2 = s[i + d.length + 1];
      if (pre && /[\w.,]/.test(pre)) continue;
      if (post && (/\w/.test(post) || (/[.,]/.test(post) && post2 && /\d/.test(post2)))) continue;
      if (out.some((m) => i < m.i + m.d.length && m.i < i + d.length)) continue;
      out.push({ id: c.id, i, d });
    }
  }
  return out.sort((a, b) => a.i - b.i);
}

// ------------------------------------------------------------------ lớp phủ 2D
export function Overlay(canvas, res) {
  const V = CK.view && CK.view.orient === 'v' ? CK.view : null;
  const S = V ? res / 1920 : res / 1080;
  canvas.width = Math.round((V ? 1080 : 1920) * S); canvas.height = Math.round((V ? 1920 : 1080) * S);
  // khung dọc: cửa sổ của mặt phẳng thiết kế 1920×1080 — rộng 1080/vs, gốc (vx0, vy0); thiết kế (x, y) → dọc ((x − vx0)·vs, (y − vy0)·vs)
  const vs = V ? (V.s || 1) : 1, vx0 = V ? 960 - 540 / vs : 0, vy0 = V ? 540 - (V.cy ?? (VZONE.y0 + VZONE.y1) / 2) / vs : 0;
  const ctx = canvas.getContext('2d');
  let log = null, chartW = 0, camera = null, seq = 0, inText = false, bgDraw = false, vc = null;
  const base = () => ctx.setTransform(S * vs, 0, 0, S * vs, -vx0 * S * vs, -vy0 * S * vs);
  const proj = new THREE.Vector3();
  // F-2: mọi nét stroke (moveTo/lineTo) trên lớp phủ → log.lines {n: thứ tự vẽ, a, w, seg: [[x0,y0,x1,y1]…]} ở toạ độ thiết kế 1920×1080
  // (cả nét scene.js vẽ thẳng bằng O.ctx); sfx_labels.py kiểm đường cắt chữ. Đường cong/arc và đường 3D không ghi. Không đổi điểm ảnh.
  let path = [], pen = null, pts = [];
  const dz = (x, y) => { const m = ctx.getTransform(), k = S * vs; return [(m.a * x + m.c * y + m.e) / k + vx0, (m.b * x + m.d * y + m.f) / k + vy0]; };
  const raw = { beginPath: ctx.beginPath.bind(ctx), moveTo: ctx.moveTo.bind(ctx), lineTo: ctx.lineTo.bind(ctx), stroke: ctx.stroke.bind(ctx) };
  // CHECKS: lớp nào được vẽ (mode 'all' = mọi thứ, như khi render)
  const draws = (isText) => { const m = CK.mode; if (m === 'all') return true; if (m === 'text' || m === 'glyph' || m === 'only') return isText; if (m === 'graphics') return !isText && !bgDraw; return !isText; };
  const bbox = (P) => [Math.min(...P.map((p) => p[0])), Math.min(...P.map((p) => p[1])), Math.max(...P.map((p) => p[0])), Math.max(...P.map((p) => p[1]))];
  const shapeObj = (o, n = seq++) => { const id = 's' + n; log.objects.push({ id, n, kind: 'shape', key: o.key || id, sig: `${o.role}|${o.tag}|${(o.box || []).map(Math.round)}|${o.fill || ''}${o.stroke || ''}`, panel: null, chart: null, ...o }); };
  ctx.beginPath = () => { path = []; pen = null; pts = []; raw.beginPath(); };
  ctx.moveTo = (x, y) => { pen = dz(x, y); pts.push(pen); raw.moveTo(x, y); };
  ctx.lineTo = (x, y) => { const p = dz(x, y); if (pen) path.push([...pen, ...p].map((v) => +v.toFixed(1))); pen = p; pts.push(p); raw.lineTo(x, y); };
  ctx.stroke = (...a) => {
    if (log && !a.length && path.length && ctx.globalAlpha > 0.01 && !inText) {
      const n = seq++; log.lines.push({ n, a: +ctx.globalAlpha.toFixed(3), w: +ctx.lineWidth.toFixed(1), seg: path });
      if (CK.on) { const P = path.flatMap((g) => [[g[0], g[1]], [g[2], g[3]]]);
        shapeObj({ tag: 'line', role: 'line', stroke: hexOf(ctx.strokeStyle), fill: null, opacity: +ctx.globalAlpha.toFixed(3), box: bbox(P).map(r1), vertices: path.length + 1 }, n); }
    }
    if (draws(inText)) raw.stroke(...a);
  };
  for (const k of ['fill', 'fillRect', 'strokeRect', 'fillText', 'strokeText', 'drawImage']) {
    const f = ctx[k].bind(ctx);
    ctx[k] = (...a) => {
      const full = k === 'fillRect' && a[2] * a[3] >= 0.9 * 1920 * 1080;   // lớp phủ cả khung (tối dần, ident) = nền
      const b0 = bgDraw; if (full) bgDraw = true;
      if (CK.on && log && !inText && !bgDraw && ctx.globalAlpha > 0.01 && (k === 'fill' || k === 'fillRect')) {
        const P = k === 'fillRect' ? [dz(a[0], a[1]), dz(a[0] + a[2], a[1] + a[3])] : pts;
        if (P.length) shapeObj({ tag: k === 'fill' ? 'path' : 'rect', role: 'mark', fill: hexOf(ctx.fillStyle), stroke: null, opacity: +ctx.globalAlpha.toFixed(3), box: bbox(P).map(r1) });
      }
      if (draws(inText)) {
        if (full && V) { ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); f(0, 0, canvas.width, canvas.height); ctx.restore(); }   // dọc: phủ cả khung dọc
        else f(...a);
      }
      bgDraw = b0;
    };
  }
  const projBox = (P) => bbox(P.map(([x, y, z]) => { proj.set(x, y, z ?? 0).project(camera); return [(proj.x + 1) * 960, (1 - proj.y) * 540]; }));
  const vmap = (b) => [(b[0] - vx0) * vs, (b[1] - vy0) * vs, (b[2] - vx0) * vs, (b[3] - vy0) * vs];
  // dọc: chữ ≥ 56 px, xuống dòng khi rộng hơn vùng an toàn, đẩy vào vùng (nội dung: VZONE; chrome trực tiếp: VSAFE) → {px, lines, x, y, box}
  function vfit(s, x, y, px, o, wfont) {
    let p = px; const raised = p * vs < VFLOOR - 1e-6; if (raised) p = VFLOOR / vs;
    ctx.font = `${wfont} ${p}px Inter`;
    const pad = o.plate ? p * 0.32 : 0, room = (VSAFE.x1 - VSAFE.x0) / vs - 2 * pad, mw = (q) => ctx.measureText(q).width;
    let lines = [s];
    if (mw(s) > room && s.includes(' ')) { lines = []; let cur = ''; for (const w of s.split(' ')) { const tr = cur ? cur + ' ' + w : w; if (cur && mw(tr) > room) { lines.push(cur); cur = w; } else cur = tr; } if (cur) lines.push(cur); }
    const lh = p * 1.18, ws = lines.map(mw), W = Math.max(...ws);
    const xl = (w) => (o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x);
    let box = [Math.min(...ws.map(xl)), y - (lines.length - 1) * lh - p * 0.78, Math.max(...ws.map((w) => xl(w) + w)), y + p * 0.24];
    const vb = vmap(box), Z = o.kind === 'chrome' ? VSAFE : { x0: VSAFE.x0, y0: VZONE.y0, x1: VSAFE.x1, y1: VZONE.y1 }, pv = pad * vs;
    let dx = 0, dy = 0;
    if (vb[0] - pv < Z.x0) dx = Z.x0 - (vb[0] - pv); else if (vb[2] + pv > Z.x1) dx = Z.x1 - (vb[2] + pv);
    if (vb[1] - pv < Z.y0) dy = Z.y0 - (vb[1] - pv); else if (vb[3] + pv > Z.y1) dy = Z.y1 - (vb[3] + pv);
    x += dx / vs; y += dy / vs; box = [box[0] + dx / vs, box[1] + dy / vs, box[2] + dx / vs, box[3] + dy / vs];
    if (raised) log.v.raised.push({ s, from: +(px * vs).toFixed(1), to: VFLOOR });
    return { p, lines, lh, x, y, box, W };
  }
  const O = {
    ctx, S,
    begin(t, cw, cam) {
      chartW = cw; camera = cam; seq = 0; vc = null;
      log = { t, chartW: +cw.toFixed(3), texts: [], lines: [], violations: [] };
      if (cam) { const d = new THREE.Vector3(); cam.getWorldDirection(d); log.cam = { p: cam.position.toArray().map((v) => +v.toFixed(5)), d: d.toArray().map((v) => +v.toFixed(6)), fov: +cam.fov.toFixed(5), aspect: +cam.aspect.toFixed(6) }; }
      if (CK.on) { log.objects = []; for (const o of CK.shapes3d) { const id = 's' + seq; log.objects.push({ id, n: seq++, ...o }); } }
      if (V) log.v = { texts: [], raised: [], dropped: [], fitted: [], shifted: [], collisions: [], recoloured: [], tags: [], claims: [], hist: false, illus: false };
      ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, canvas.width, canvas.height); base(); return log;
    },
    // toạ độ màn hình (thiết kế 1920×1080) của một điểm thế giới
    toScreen(x, y, z = 0) { proj.set(x, y, z).project(camera); return [(proj.x + 1) * 960, (1 - proj.y) * 540]; },
    // hình dữ liệu khai cho trang kiểm (không vẽ gì): {role:'bar'|'series'|'mark'|…, box:[l,t,r,b] | world:[[x,y,z]…], case?, year?, series?,
    // value?, full?, chart?, panel?, char?, shape?, fill?, stroke?, opacity?, key?} — vd. mỗi đường của bó phát lại mang `case: 'YYYY-MM'` (S06)
    shape(o) { if (!CK.on || !log) return; const box = o.box || (o.world ? projBox(o.world) : null); if (!box) return; const { world, ...rest } = o;
      shapeObj({ tag: 'mark', role: 'mark', fill: null, stroke: null, opacity: 1, ...rest, box: box.map(r1) }); },
    // chữ: kind = 'name' | 'number' | 'compare' | 'chrome' | 'title'; tuỳ chọn cho trang kiểm: role, level, emph, series, anchor, chart, year, case, char, roll,
    // claims: [claimId] (chỉ khớp display của các claim này — khi nhiều claim cùng chuỗi hiển thị)
    text(s, x, y, px, o = {}) {
      const a = o.alpha ?? 1; if (a <= 0.01 || !s) return null;
      const kind = o.kind || 'name';
      if ((kind === 'number' || kind === 'compare') && chartW < 0.95 && a > 0.05) log.violations.push({ rule: 1, text: s, chartW: +chartW.toFixed(3) });
      const wfont = o.w || 700, id = 't' + seq, m = CK.mode, onlyHit = m !== 'only' || (CK.ids && CK.ids.has(id));
      ctx.save(); ctx.globalAlpha = a; ctx.font = `${wfont} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums';
      ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
      let w = ctx.measureText(s).width, x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
      let box = [x0, y - px * 0.78, x0 + w, y + px * 0.24], P = px, lines = null, lh = 0;
      if (V) { const f = vfit(s, x, y, px, o, wfont); ({ box, lines, lh } = f); P = f.p; x = f.x; y = f.y; w = f.W; ctx.font = `${wfont} ${P}px Inter`;
        // chữ NHỎ (< 48 px thiết kế: nhãn trục, vạch chia) được nâng lên sàn mà đè hộp chữ đã vẽ (> 4 px, vd. nhãn năm sát nhau) → bỏ
        // (log.v.dropped), không vẽ chồng; chữ ≥ 48 px (nhãn nội dung) luôn được vẽ
        const hit = P > px + 1e-6 && px < 48 && log.texts.some((q) => q.opacity > 0.05 && Math.min(q.box[2], box[2]) - Math.max(q.box[0], box[0]) > 4 / vs && Math.min(q.box[3], box[3]) - Math.max(q.box[1], box[1]) > 4 / vs);
        if (hit) { ctx.restore(); log.v.dropped.push({ s, px }); return null; } }
      inText = true;
      if (o.plate && m !== 'glyph' && m !== 'only') { const pad = P * 0.32; ctx.fillStyle = rgba(o.plate, o.plateA ?? 0.72); roundRect(ctx, box[0] - pad, box[1] - pad * 0.7, box[2] - box[0] + 2 * pad, box[3] - box[1] + pad * 1.4, P * 0.3); ctx.fill(); }
      ctx.fillStyle = o.color || C.ink;
      if (onlyHit) { if (lines) lines.forEach((ln, j) => ctx.fillText(ln, x, y - (lines.length - 1 - j) * lh)); else ctx.fillText(s, x, y); }
      inText = false;
      if (CK.on) {   // objet hợp đồng window.CHECKS (trước restore: phông đang đặt → đo khoảng claim)
        const col = hexOf(o.color || C.ink), occ = log.objects.filter((q) => q.kind === 'text' && q.text === s).length;
        const claims = claimSpans(s, o.claims ? (CK.claims || []).filter((c) => o.claims.includes(c.id)) : CK.claims).map((c) => { const xa = x0 + ctx.measureText(s.slice(0, c.i)).width;
          return { id: c.id, text: c.d, box: [xa, box[1], xa + ctx.measureText(c.d).width, box[3]].map(r1), opacity: +a.toFixed(3), color: col, series: o.series ?? null, roll: !!o.roll }; });
        const role = o.role || (/^ILLUSTRATIVE$/.test(s) ? 'badge' : kind === 'title' ? 'title' : 'label');
        log.objects.push({ id, n: seq, kind: 'text', tid: `${s}#${occ}`, role, text: s, box: box.map(r1), opacity: +a.toFixed(3), level: o.level ?? null, emph: !!o.emph,
          series: o.series ?? null, anchor: o.anchor ?? null, chart: o.chart ?? null, year: o.year ?? null, case: o.case ?? null, char: o.char ?? null,
          runs: [{ color: col, size: px }], color: col, fontPx: px, background: o.plate ? hexOf(o.plate) : null, parent: null, claims, key: `${s}#${occ}`,
          sig: `${kind}|${s}|${box.map(Math.round)}`, kindHint: kind });
      }
      ctx.restore();
      log.texts.push({ text: s, kind, px, opacity: +a.toFixed(3), box: box.map((v) => +v.toFixed(1)), n: seq++, ...(o.plate ? { plate: 1 } : {}) });
      if (V) log.v.texts.push({ s, kind, px: +(P * vs).toFixed(1), box: vmap(box).map(r1), opacity: +a.toFixed(3), contrast: +contrastHex(o.color || C.ink, o.plate || C.bg).toFixed(2) });
      return box;
    },
    bracket(x, y0, y1, color, a = 1, tick = 18, lw = 6) {
      if (a <= 0.01) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
      ctx.moveTo(x, y0); ctx.lineTo(x + tick, y0); ctx.lineTo(x + tick, y1); ctx.lineTo(x, y1); ctx.stroke(); ctx.restore();
    },
    // lớp bắt buộc: cố định, 48 px, nền mờ (quy tắc 5); flags: {illus, hist, src, cw}. Khung dọc: chỉ ghi cờ — lớp bắt buộc dọc vẽ ở finish()
    chrome(f, a = 1) {
      if (V) { vc ||= {}; for (const k of ['illus', 'hist', 'src', 'cw']) if (f[k] && a * (f[k + 'A'] ?? 1) > 0.01) vc[k] = f[k]; return; }
      const PX = 54, plate = '#0B0E13';
      const band = (y0, y1, up) => { const g = ctx.createLinearGradient(0, y0, 0, y1); g.addColorStop(up ? 1 : 0, rgba(plate, 0)); g.addColorStop(up ? 0.6 : 0.35, rgba(plate, 0.95 * a)); g.addColorStop(up ? 0 : 1, rgba(plate, 0.93 * a)); ctx.fillStyle = g; bgDraw = true; ctx.fillRect(0, y0, 1920, y1 - y0); bgDraw = false; };   // v3f: nửa trong của dải là nền ĐẶC sau chữ
      if (f.src || f.illus) band(0, 150, true);
      if (f.hist || f.cw) band(f.cw && f.hist ? 850 : 925, 1080, false);
      if (f.illus) O.text('ILLUSTRATIVE', 1824, 108, PX, { kind: 'chrome', color: '#1B1F26', plate: C.warn, plateA: 0.95, align: 'right', alpha: a * (f.illusA ?? 1) });
      if (f.src) O.text(f.src, 96, 108, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.srcA ?? 1) });
      if (f.cw) O.text(f.cw, 96, f.hist ? 952 : 1022, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.cwA ?? 1) });
      if (f.hist) O.text('US only · history, not a forecast', 96, 1022, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.histA ?? 1) });
    },
    // khung dọc (Short): lớp bắt buộc của nhà máy, toạ độ dọc 1080×1920 — móc (trên), ILLUSTRATIVE (phải, dưới móc), đối trọng xoay mỗi 3 s +
    // "US only · history, not a forecast" (dưới) trên MỌI khung có số (chữ có chữ số) hoặc khi cảnh bật cờ tương ứng (playbook §5, như engine.js)
    finish() {
      if (!V || !log) return;
      const T = log.t - (V.t0 || 0), L = log.v;
      const numeric = log.texts.some((x) => x.kind !== 'chrome' && x.opacity > 0.05 && /\d/.test(x.text));
      const illus = numeric || !!(vc && vc.illus), hist = numeric || !!(vc && vc.hist);
      const cws = (V.cws || []).filter((c) => !TAG_RE.test(c.text)), cw = (numeric || hist) && cws.length ? cws[Math.floor(Math.max(0, T) / 3) % cws.length] : null;
      ctx.save(); ctx.setTransform(S, 0, 0, S, 0, 0);
      const vt = (s, x, y, px, o = {}) => {   // chữ dọc: xuống dòng trong vùng an toàn, dòng cuối ở y
        ctx.font = `${o.w || 700} ${px}px Inter`; ctx.textAlign = o.align || 'center'; ctx.textBaseline = 'alphabetic'; ctx.fontVariantNumeric = 'tabular-nums';
        const room = VSAFE.x1 - VSAFE.x0 - (o.plate ? px * 0.64 : 0), mw = (q) => ctx.measureText(q).width;
        let lines = [s]; if (mw(s) > room) { lines = []; let cur = ''; for (const w of s.split(' ')) { const tr = cur ? cur + ' ' + w : w; if (cur && mw(tr) > room) { lines.push(cur); cur = w; } else cur = tr; } if (cur) lines.push(cur); }
        const lh = Math.round(px * 1.2), ws = lines.map(mw), xl = (w) => (ctx.textAlign === 'center' ? x - w / 2 : ctx.textAlign === 'right' ? x - w : x);
        const box = [Math.min(...ws.map(xl)), y - (lines.length - 1) * lh - px * 0.78, Math.max(...ws.map((w) => xl(w) + w)), y + px * 0.24];
        if (o.plate) { const pad = px * 0.32; ctx.fillStyle = o.plate; roundRect(ctx, box[0] - pad, box[1] - pad * 0.7, box[2] - box[0] + 2 * pad, box[3] - box[1] + pad * 1.4, px * 0.3); ctx.fill(); }
        ctx.fillStyle = o.color || C.ink; lines.forEach((ln, j) => ctx.fillText(ln, x, y - (lines.length - 1 - j) * lh));
        L.texts.push({ s, kind: 'chrome', px, box: box.map(r1), opacity: 1, contrast: +contrastHex(o.color || C.ink, o.plate || C.bg).toFixed(2) });
        return { lines: lines.length, lh, box };
      };
      const measureLines = (s, px, w = 700) => { ctx.font = `${w} ${px}px Inter`; let n = 1, cur = ''; for (const q of s.split(' ')) { const tr = cur ? cur + ' ' + q : q; if (cur && ctx.measureText(tr).width > VSAFE.x1 - VSAFE.x0) { n++; cur = q; } else cur = tr; } return n; };
      // dải nền dưới chữ bắt buộc (cùng màu tấm nền của chrome ngang)
      const band = (y0, y1, up) => { const g = ctx.createLinearGradient(0, y0, 0, y1); g.addColorStop(up ? 1 : 0, 'rgba(11,14,19,0)'); g.addColorStop(up ? 0.55 : 0.3, 'rgba(11,14,19,0.95)'); g.addColorStop(up ? 0 : 1, 'rgba(11,14,19,0.95)'); ctx.fillStyle = g; ctx.fillRect(0, y0, 1080, y1 - y0); };
      const HIST = 'US only · history, not a forecast', hl = hist ? measureLines(HIST, VFLOOR, 600) : 0, cl = cw ? measureLines(cw.text, VFLOOR) : 0;
      if (V.hook || illus) band(0, VZONE.y0 + 10, true);
      if (hist || cw) band(VSAFE.y1 - 68 * (hl + cl) - 70, 1920, false);
      if (V.hook) vt(V.hook, 540, VSAFE.y0 + 70, 64, { align: 'center' });
      if (illus) { vt('ILLUSTRATIVE', VSAFE.x1 - 18, VSAFE.y0 + 170, VFLOOR, { align: 'right', color: '#1B1F26', plate: C.warn }); L.tags.push('ILLUSTRATIVE'); }
      const yb = VSAFE.y1 - Math.ceil(VFLOOR * 0.24) - 2;   // dòng cuối: cả phần dưới chân chữ trong vùng an toàn
      if (hist) { vt(HIST, 540, yb, VFLOOR, { align: 'center', w: 600, color: C.chrome }); L.tags.push('HISTORY');
        for (const c of V.cws || []) if (TAG_RE.test(c.text)) L.tags.push('CW:' + c.id); }   // đối trọng trùng dòng history: đang hiện
      if (cw) { vt(cw.text, 540, yb - 68 * hl, VFLOOR, { align: 'center', color: C.ink }); L.tags.push('CW:' + cw.id); }
      ctx.restore();
      L.illus = illus; L.hist = hist; L.claims = numeric ? ['number'] : [];
    },
  };
  return O;
}
export function roundRect(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }

// ------------------------------------------------------------------ máy quay: chụp / đặt lại trạng thái (freeze của trang kiểm)
const grabCam = (c) => ({ pos: c.position.toArray(), quat: c.quaternion.toArray(), fov: c.fov, aspect: c.aspect, near: c.near, far: c.far, zoom: c.zoom });
function applyCam(c, s) { c.position.fromArray(s.pos); c.quaternion.fromArray(s.quat); Object.assign(c, { fov: s.fov, aspect: s.aspect, near: s.near, far: s.far, zoom: s.zoom }); c.updateProjectionMatrix(); c.updateMatrixWorld(true); }
// vật 3D khai cho trang kiểm: object.userData.checks = {role, case?, year?, series?, …} → hình hộp bao chiếu lên màn hình (thiết kế 1920×1080)
const _b = new THREE.Box3(), _v = new THREE.Vector3();
function shapes3d(scene, cam) {
  const out = [];
  scene.traverse((o) => {
    const k = o.userData && o.userData.checks; if (!k || !o.visible) return;
    _b.setFromObject(o); if (_b.isEmpty()) return;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity, op = 0;
    for (let i = 0; i < 8; i++) { _v.set(i & 1 ? _b.max.x : _b.min.x, i & 2 ? _b.max.y : _b.min.y, i & 4 ? _b.max.z : _b.min.z).project(cam);
      const x = (_v.x + 1) * 960, y = (1 - _v.y) * 540; x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x); y1 = Math.max(y1, y); }
    o.traverse((m) => { if (m.isMesh && m.visible) for (const q of [].concat(m.material)) op = Math.max(op, q.opacity ?? 1); });
    const box = [x0, y0, x1, y1].map(r1), key = k.key || o.name || o.uuid;
    out.push({ kind: 'shape', tag: 'mesh', role: 'mark', fill: null, stroke: null, ...k, box, opacity: +op.toFixed(3), key, sig: `${k.role || 'mark'}|${key}|${box.map(Math.round)}` });
  });
  return out;
}

// ------------------------------------------------------------------ khởi tạo trang chung: renderer WebGL + lớp phủ + canvas ra
export function Stage(res) {
  const V = CK.view && CK.view.orient === 'v' ? CK.view : null;
  const W = V ? Math.round(1080 * res / 1920) : Math.round(1920 * res / 1080), H = res;
  const vs = V ? (V.s || 1) : 1, cy = V ? (V.cy ?? (VZONE.y0 + VZONE.y1) / 2) : 0;
  const gl = document.createElement('canvas');
  // alpha: true — nền là scene.background (đục) nên khung render như cũ; lớp 'graphics' của trang kiểm cần nền trong suốt
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power', alpha: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const ov = document.createElement('canvas'), out = document.createElement('canvas'); out.width = W; out.height = H; document.body.appendChild(out);
  const O = Overlay(ov, res), octx = out.getContext('2d', CK.dither >= 2 ? { willReadFrequently: true } : undefined);
  const render0 = renderer.render.bind(renderer), cc = new THREE.Color();
  renderer.render = (scene, cam) => {
    const m = CK.mode;
    if (CK.dither >= 1) scene.traverse((o) => { if (o.material) for (const q of [].concat(o.material)) if (!q.dithering) { q.dithering = true; q.needsUpdate = true; } });
    if (CK.freezeCam) applyCam(cam, CK.freezeCam); else CK.lastCam = grabCam(cam);
    if (CK.on && m === 'all') CK.shapes3d = shapes3d(scene, cam);
    if (V) cam.setViewOffset(1920, 1080, 960 - 540 / vs, 540 - cy / vs, 1080 / vs, 1920 / vs);   // cửa sổ dọc của cùng khung thiết kế
    if (m === 'text' || m === 'glyph' || m === 'only') { renderer.getClearColor(cc); const ca = renderer.getClearAlpha(); renderer.setClearColor(0x000000, 0); renderer.clear(); renderer.setClearColor(cc, ca); }
    else if (m === 'graphics') {   // không nền: scene.background, sàn (userData.role 'bg')
      const bg = scene.background, hid = []; scene.background = null;
      scene.traverse((o) => { if (o.userData && o.userData.role === 'bg' && o.visible) { o.visible = false; hid.push(o); } });
      renderer.getClearColor(cc); const ca = renderer.getClearAlpha(); renderer.setClearColor(0x000000, 0);
      render0(scene, cam); renderer.setClearColor(cc, ca); scene.background = bg; for (const o of hid) o.visible = true;
    } else render0(scene, cam);
    if (V) cam.clearViewOffset();
  };
  return {
    renderer, O, out,
    compose() {
      O.finish();
      const m = CK.mode;
      if (m === 'all') { octx.drawImage(gl, 0, 0); octx.drawImage(ov, 0, 0); if (CK.dither >= 2 && !CK.on) darkDither(octx, W, H); return; }
      octx.clearRect(0, 0, W, H);
      if (m === 'graphics' || m === 'notext') octx.drawImage(gl, 0, 0);
      octx.drawImage(ov, 0, 0);
    },
  };
}

// dither CỐ ĐỊNH theo màn hình (như dither có thứ tự trước khi mã hoá): nhiễu tam giác (TPDF) ±4 mã (σ ≈ 1,6 mã) theo ô 2×2 px ở 1080
// (ô = res/540 px), cùng một mẫu ở mọi khung, chỉ cộng vào điểm ảnh tối (luma < 72). Bẻ các dải phẳng của gradient tối (sàn, sương, dải nền
// chrome) và SỐNG QUA hai lần mã hoá x264 (crf 16 → CBR 17M của master): khung P dự đoán đúng mẫu đứng yên nên không xoá nó. Đo (checks F08,
// banding_score, cửa sổ 70–84 s của Tập 5 ở 1080p, chuỗi mã hoá thật): không dither 62,9 %; nhiễu đổi theo khung ±4 mã 14,2 % (khung P mất
// nhiễu); mẫu cố định: xem BACKLOG F-6. Điểm sáng (chữ, vật) không đổi.
const DITHER = { amp: 4, lumaMax: 72, seed: 0x5EED1E };
let ditherField = null;
function darkDither(c, W, H) {
  const blk = Math.max(1, Math.round(H / 540)), nx = Math.ceil(W / blk), ny = Math.ceil(H / blk), A = DITHER.amp;
  if (!ditherField || ditherField.W !== W || ditherField.H !== H) {   // một mẫu cho cả phim (cùng hạt giống → mọi worker, mọi lần render như nhau)
    const f = new Int8Array(nx * ny); let s = DITHER.seed >>> 0;
    for (let i = 0; i < f.length; i++) { s ^= s << 13; s >>>= 0; s ^= s >>> 17; s ^= s << 5; s >>>= 0; f[i] = Math.round(((s & 1023) + ((s >>> 10) & 1023) - 1023) / 1023 * A); }
    ditherField = { W, H, f };
  }
  const im = c.getImageData(0, 0, W, H), d = im.data, F = ditherField.f;
  for (let y = 0; y < H; y++) {
    const row = ((y / blk) | 0) * nx;
    for (let x = 0; x < W; x++) {
      const k = F[row + ((x / blk) | 0)]; if (!k) continue;
      const i = (y * W + x) * 4;
      if (((d[i] * 54 + d[i + 1] * 183 + d[i + 2] * 19) >> 8) >= DITHER.lumaMax) continue;
      d[i] = Math.min(255, Math.max(0, d[i] + k)); d[i + 1] = Math.min(255, Math.max(0, d[i + 1] + k)); d[i + 2] = Math.min(255, Math.max(0, d[i + 2] + k));
    }
  }
  c.putImageData(im, 0, 0);
}

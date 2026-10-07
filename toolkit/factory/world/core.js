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

// ------------------------------------------------------------------ lớp phủ 2D
export function Overlay(canvas, res) {
  const S = res / 1080; canvas.width = Math.round(1920 * S); canvas.height = Math.round(1080 * S);
  const ctx = canvas.getContext('2d');
  let log = null, chartW = 0, camera = null, seq = 0;
  const proj = new THREE.Vector3();
  // F-2: mọi nét stroke (moveTo/lineTo) trên lớp phủ → log.lines {n: thứ tự vẽ, a, w, seg: [[x0,y0,x1,y1]…]} ở toạ độ thiết kế 1920×1080
  // (cả nét scene.js vẽ thẳng bằng O.ctx); sfx_labels.py kiểm đường cắt chữ. Đường cong/arc và đường 3D không ghi. Không đổi điểm ảnh.
  let path = [], pen = null;
  const dz = (x, y) => { const m = ctx.getTransform(); return [(m.a * x + m.c * y + m.e) / S, (m.b * x + m.d * y + m.f) / S]; };
  const raw = { beginPath: ctx.beginPath.bind(ctx), moveTo: ctx.moveTo.bind(ctx), lineTo: ctx.lineTo.bind(ctx), stroke: ctx.stroke.bind(ctx) };
  ctx.beginPath = () => { path = []; pen = null; raw.beginPath(); };
  ctx.moveTo = (x, y) => { pen = dz(x, y); raw.moveTo(x, y); };
  ctx.lineTo = (x, y) => { const p = dz(x, y); if (pen) path.push([...pen, ...p].map((v) => +v.toFixed(1))); pen = p; raw.lineTo(x, y); };
  ctx.stroke = (...a) => { if (log && !a.length && path.length && ctx.globalAlpha > 0.01) log.lines.push({ n: seq++, a: +ctx.globalAlpha.toFixed(3), w: +ctx.lineWidth.toFixed(1), seg: path }); raw.stroke(...a); };
  const O = {
    ctx, S,
    begin(t, cw, cam) { chartW = cw; camera = cam; seq = 0; log = { t, chartW: +cw.toFixed(3), texts: [], lines: [], violations: [] }; ctx.setTransform(S, 0, 0, S, 0, 0); ctx.clearRect(0, 0, 1920, 1080); return log; },
    // toạ độ màn hình (thiết kế 1920×1080) của một điểm thế giới
    toScreen(x, y, z = 0) { proj.set(x, y, z).project(camera); return [(proj.x + 1) * 960, (1 - proj.y) * 540]; },
    // chữ: kind = 'name' | 'number' | 'compare' | 'chrome' | 'title'
    text(s, x, y, px, o = {}) {
      const a = o.alpha ?? 1; if (a <= 0.01 || !s) return null;
      const kind = o.kind || 'name';
      if ((kind === 'number' || kind === 'compare') && chartW < 0.95 && a > 0.05) log.violations.push({ rule: 1, text: s, chartW: +chartW.toFixed(3) });
      ctx.save(); ctx.globalAlpha = a; ctx.font = `${o.w || 700} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums';
      ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
      const w = ctx.measureText(s).width, x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
      const box = [x0, y - px * 0.78, x0 + w, y + px * 0.24];
      if (o.plate) { const pad = px * 0.32; ctx.fillStyle = rgba(o.plate, o.plateA ?? 0.72); roundRect(ctx, box[0] - pad, box[1] - pad * 0.7, w + 2 * pad, box[3] - box[1] + pad * 1.4, px * 0.3); ctx.fill(); }
      ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y); ctx.restore();
      log.texts.push({ text: s, kind, px, opacity: +a.toFixed(3), box: box.map((v) => +v.toFixed(1)), n: seq++, ...(o.plate ? { plate: 1 } : {}) });
      return box;
    },
    bracket(x, y0, y1, color, a = 1, tick = 18, lw = 6) {
      if (a <= 0.01) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
      ctx.moveTo(x, y0); ctx.lineTo(x + tick, y0); ctx.lineTo(x + tick, y1); ctx.lineTo(x, y1); ctx.stroke(); ctx.restore();
    },
    // lớp bắt buộc: cố định, 48 px, nền mờ (quy tắc 5); flags: {illus, hist, src, cw}
    chrome(f, a = 1) {
      const PX = 54, plate = '#0B0E13';
      const band = (y0, y1, up) => { const g = ctx.createLinearGradient(0, y0, 0, y1); g.addColorStop(up ? 1 : 0, rgba(plate, 0)); g.addColorStop(up ? 0.6 : 0.35, rgba(plate, 0.95 * a)); g.addColorStop(up ? 0 : 1, rgba(plate, 0.93 * a)); ctx.fillStyle = g; ctx.fillRect(0, y0, 1920, y1 - y0); };   // v3f: nửa trong của dải là nền ĐẶC sau chữ
      if (f.src || f.illus) band(0, 150, true);
      if (f.hist || f.cw) band(f.cw && f.hist ? 850 : 925, 1080, false);
      if (f.illus) O.text('ILLUSTRATIVE', 1824, 108, PX, { kind: 'chrome', color: '#1B1F26', plate: C.warn, plateA: 0.95, align: 'right', alpha: a * (f.illusA ?? 1) });
      if (f.src) O.text(f.src, 96, 108, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.srcA ?? 1) });
      if (f.cw) O.text(f.cw, 96, f.hist ? 952 : 1022, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.cwA ?? 1) });
      if (f.hist) O.text('US only · history, not a forecast', 96, 1022, PX, { kind: 'chrome', w: 600, color: C.chrome, alpha: a * (f.histA ?? 1) });
    },
  };
  return O;
}
export function roundRect(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }

// ------------------------------------------------------------------ khởi tạo trang chung: renderer WebGL + lớp phủ + canvas ra
export function Stage(res) {
  const W = Math.round(1920 * res / 1080), H = res;
  const gl = document.createElement('canvas');
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const ov = document.createElement('canvas'), out = document.createElement('canvas'); out.width = W; out.height = H; document.body.appendChild(out);
  const O = Overlay(ov, res), octx = out.getContext('2d');
  return { renderer, O, out, compose() { octx.drawImage(gl, 0, 0); octx.drawImage(ov, 0, 0); } };
}

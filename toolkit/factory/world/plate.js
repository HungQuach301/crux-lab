// F-15 (f) · FOOTAGE NGOÀI TRONG THẾ GIỚI: ảnh/khung video tư liệu làm `plate` + bản đồ theo ngôn ngữ hình kênh.
// Opt-in: chỉ scene.js nào import mô-đun này mới dùng; plate không chạm core.js/lib3d.js (F-15 chỉ thêm `CK.spp` vào core, mặc định như cũ) → đoạn cũ
// trùng byte; render_shots.js tự thêm plate.js vào khoá cache khi scene.js nhắc tới nó. Vẽ trên lớp phủ 2D (O.ctx, toạ độ thiết kế 1920×1080) SAU renderer.render và TRƯỚC chữ → hoà vào/ra
// từ cảnh 3D bằng độ hiện (alpha) của plate; chữ vẽ sau luôn ở trên.
//   cine-lab #49: Ken Burns có điểm chính `focus` (đặt ở vị trí màn hình `anchor`, trên dải chú thích), không căn giữa ảnh;
//   cine-lab #50: nguồn ảnh bên PHẢI, nguồn số bên TRÁI, cùng dải; dải chữ chọn phía KHÔNG đè hộp chủ thể (`subject`);
//   cine-lab #93: cắt 3D ↔ ảnh lưu trữ bị đọc là "đổi chất liệu" → plate luôn có tông kênh (đơn sắc hai màu) và hoà ≥ 1 s.
// Mọi phép vẽ tất định (tông tính trên CPU một lần; không nhiễu, không thời gian thực) → cùng khung mọi worker/mọi lượt.
import { CK, rgba, roundRect } from './core.js';

export const TONE = { dark: '#0E1116', light: '#E8E1D0', gamma: 1.0 };   // nền kênh → giấy ấm (bill/card của Tập 7)
const hex = (h) => { const n = parseInt(h.slice(1, 7), 16); return [n >> 16, (n >> 8) & 255, n & 255]; };
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const smooth = (u) => { u = clamp(u, 0, 1); return u * u * (3 - 2 * u); };

export async function loadImage(url) { const img = new Image(); img.src = url; await img.decode(); return img; }

// ảnh → canvas đơn sắc hai màu của kênh (độ sáng Rec.709 → trộn dark…light); maxW giới hạn bộ nhớ
export function toneImage(img, { dark = TONE.dark, light = TONE.light, gamma = TONE.gamma, maxW = 2400 } = {}) {
  const k = Math.min(1, maxW / img.width), w = Math.round(img.width * k), h = Math.round(img.height * k);
  const c = document.createElement('canvas'); c.width = w; c.height = h; const g = c.getContext('2d', { willReadFrequently: true });
  g.drawImage(img, 0, 0, w, h);
  const im = g.getImageData(0, 0, w, h), d = im.data, D = hex(dark), L = hex(light);
  for (let i = 0; i < d.length; i += 4) {
    const y = Math.pow((0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2]) / 255, gamma);
    d[i] = Math.round(D[0] + (L[0] - D[0]) * y); d[i + 1] = Math.round(D[1] + (L[1] - D[1]) * y); d[i + 2] = Math.round(D[2] + (L[2] - D[2]) * y);
  }
  g.putImageData(im, 0, 0); return c;
}

// cửa sổ Ken Burns 16:9 trong ảnh iw×ih: zoom z (1 = phủ kín lớn nhất), điểm chính f = [fx, fy] (0–1 của ảnh) đặt ở anchor = [ax, ay] (0–1 của khung)
export function kbWindow(iw, ih, z, f, anchor = [0.5, 0.42]) {
  const cw = Math.min(iw, ih * 16 / 9), sw = cw / z, sh = sw * 9 / 16;
  const sx = clamp(f[0] * iw - anchor[0] * sw, 0, iw - sw), sy = clamp(f[1] * ih - anchor[1] * sh, 0, ih - sh);
  return [sx, sy, sw, sh];
}

// độ hiện theo [t0, t1] với hoà vào/ra (giây)
export function envelope(t, t0, t1, fin = 1.2, fout = 1.2) { return Math.min(smooth((t - t0) / Math.max(1e-6, fin)), smooth((t1 - t) / Math.max(1e-6, fout))); }

// P = {src: canvas đã tông (hoặc khung video hiện tại), subject: [x0,y0,x1,y1] (0–1 của ảnh), focus?: [fx,fy], zoom: [z0,z1], anchor?, t0, t1, fade?: [in,out]}
// Trả {a, subject: hộp chủ thể trên khung thiết kế, win}
export function drawPlate(O, P, t) {
  const a = envelope(t, P.t0, P.t1, ...(P.fade || [1.2, 1.2])); if (a <= 0.004) return { a: 0, subject: null };
  const src = P.frames ? P.frames[clamp(Math.floor((t - P.t0) * (P.fps || 30)), 0, P.frames.length - 1)] : P.src;
  const iw = src.width, ih = src.height, f = P.focus || [(P.subject[0] + P.subject[2]) / 2, (P.subject[1] + P.subject[3]) / 2];
  const u = smooth((t - P.t0) / Math.max(1e-6, P.t1 - P.t0)), z = P.zoom[0] + (P.zoom[1] - P.zoom[0]) * u;
  const [sx, sy, sw, sh] = kbWindow(iw, ih, z, f, P.anchor);
  const g = O.ctx, m = CK.mode;
  if (m === 'all' || m === 'notext' || m === 'graphics' || m === 'graphics2d') {
    g.save(); g.globalAlpha = a; g.imageSmoothingQuality = 'high'; g.drawImage(src, sx, sy, sw, sh, 0, 0, 1920, 1080); g.restore();
  }
  const X = (x) => (x * iw - sx) / sw * 1920, Y = (y) => (y * ih - sy) / sh * 1080;
  const subject = [X(P.subject[0]), Y(P.subject[1]), X(P.subject[2]), Y(P.subject[3])].map((v) => +v.toFixed(1));
  O.shape({ role: 'mark', tag: 'plate', key: P.key || 'plate', box: [0, 0, 1920, 1080], opacity: +a.toFixed(3) });
  return { a, subject, win: [sx, sy, sw, sh].map((v) => +v.toFixed(2)) };
}

// dải chữ (chú thích + nguồn): dưới (y 900–1026) trừ khi đè hộp chủ thể thì lên trên (y 54–180); cả hai đè → phía đè ít hơn + vi phạm
export const BANDS = { bottom: [900, 1026], top: [54, 180] };
export function captionBand(subject) {
  if (!subject) return { side: 'bottom', overlap: 0 };
  const ov = (b) => Math.max(0, Math.min(subject[3], b[1]) - Math.max(subject[1], b[0]));
  const ob = ov(BANDS.bottom), ot = ov(BANDS.top);
  if (!ob) return { side: 'bottom', overlap: 0 };
  if (!ot) return { side: 'top', overlap: 0 };
  return ob <= ot ? { side: 'bottom', overlap: ob } : { side: 'top', overlap: ot };
}

// chú thích (trái) + nguồn ảnh (phải) trên dải không đè chủ thể; ghi log.plate cho kiểm (hộp chữ ∩ hộp chủ thể)
export function drawCredits(O, log, subject, { caption, source, numbers }, a = 1) {
  const band = captionBand(subject), y = band.side === 'bottom' ? 1006 : 108, boxes = [];
  if (a <= 0.01) return band;
  const g = O.ctx; g.save(); g.globalAlpha = 0.86 * a; const grd = g.createLinearGradient(0, band.side === 'bottom' ? 880 : 0, 0, band.side === 'bottom' ? 1080 : 200);
  grd.addColorStop(band.side === 'bottom' ? 0 : 1, rgba('#0B0E13', 0)); grd.addColorStop(band.side === 'bottom' ? 0.45 : 0.55, rgba('#0B0E13', 0.9)); grd.addColorStop(band.side === 'bottom' ? 1 : 0, rgba('#0B0E13', 0.95));
  g.fillStyle = grd; g.fillRect(0, band.side === 'bottom' ? 880 : 0, 1920, 200); g.restore();
  // nguồn ảnh bên phải, cùng dòng chú thích; hai dòng sẽ giao nhau (đo trước bằng measureText) → nguồn lên một dòng trong dải (cine-lab #50)
  const g2 = O.ctx, wOf = (t, px, w) => { g2.save(); g2.font = `${w} ${px}px Inter`; const v = g2.measureText(t).width; g2.restore(); return v; };
  const capR = caption ? 96 + wOf(caption, 48, 600) : 0, srcL = source ? 1824 - wOf(source, 40, 600) : 1920;
  const ys = capR + 32 > srcL ? (band.side === 'bottom' ? y - 58 : y + 58) : y;
  if (caption) boxes.push(['caption', O.text(caption, 96, y, 48, { kind: 'name', w: 600, color: '#F2F4F7', alpha: a })]);
  if (numbers) boxes.push(['numbers', O.text(numbers, 96, y - 62, 40, { kind: 'chrome', w: 600, color: '#C9D1DC', alpha: a })]);
  if (source) boxes.push(['source', O.text(source, 1824, ys, 40, { kind: 'chrome', w: 600, color: '#C9D1DC', align: 'right', alpha: a })]);
  const hit = (b) => b && subject && b[0] < subject[2] && b[2] > subject[0] && b[1] < subject[3] && b[3] > subject[1];
  log.plate = { side: band.side, subject, boxes: boxes.map(([k, b]) => ({ k, box: b && b.map((v) => +v.toFixed(1)), hitsSubject: !!hit(b) })) };
  return band;
}

// bản đồ (toolkit/footage/map.py): vùng tô theo dữ liệu, hiện dần từ mốc từ của vùng; nhãn neo vào từ (`at` = giây của mốc từ, ±0 s)
// opts: {a, reveal: {id: t}, labels: [{id?, text, at, x?, y?, px?}], ramp: 0.35}
export function drawMap(O, M, t, { a = 1, reveal = {}, labels = [], ramp = 0.35 } = {}) {
  if (a <= 0.004) return [];
  const g = O.ctx, m = CK.mode, shown = [];
  if (m === 'all' || m === 'notext' || m === 'graphics' || m === 'graphics2d') {
    g.save(); g.globalAlpha = a; g.fillStyle = '#0E1116'; g.fillRect(0, 0, 1920, 1080);
    for (const f of M.features) {
      const r = f.id in reveal ? smooth((t - reveal[f.id]) / ramp) : 1;
      g.fillStyle = f.cls === 'focus' && r < 1 ? mixHex('#2A303B', f.fill, r) : f.fill;
      g.strokeStyle = '#0E1116'; g.lineWidth = 3; g.lineJoin = 'round';
      for (const R of f.rings) { g.beginPath(); R.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y))); g.closePath(); g.fill(); g.stroke(); }
    }
    g.restore();
  }
  for (const f of M.features) {
    const xs = f.rings.flat().map((p) => p[0]), ys = f.rings.flat().map((p) => p[1]);
    O.shape({ role: 'mark', tag: 'region', key: `map-${f.id}`, box: [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)], fill: f.fill, opacity: +a.toFixed(3) });
  }
  for (const L of labels) {
    if (t < L.at) continue;   // nhãn hiện ĐÚNG mốc từ (không trước)
    const f = L.id ? M.features.find((x) => x.id === L.id) : null;
    if (L.id && !f) continue;   // nhãn trỏ vùng không có trong bản đồ → bỏ (không sập trang)
    const [x, y] = [L.x ?? f.label[0], L.y ?? f.label[1]];
    const la = a * smooth((t - L.at) / 0.25);
    const b = O.text(L.text, x, y + (L.px || 48) * 0.3, L.px || 48, { kind: 'name', w: 700, color: '#F2F4F7', plate: '#0B0E13', plateA: 0.78, align: 'center', alpha: la });
    shown.push({ text: L.text, at: L.at, box: b });
  }
  return shown;
}

function mixHex(a, b, u) { const A = hex(a), B = hex(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * u).toString(16).padStart(2, '0')).join(''); }
export { roundRect };

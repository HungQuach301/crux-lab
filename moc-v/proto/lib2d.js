// Mốc V · thư viện 2D chung cho các hướng thử: token kênh, chữ (sàn 40 px @1080), huy hiệu nhỏ (ILLUSTRATIVE, lịch sử, nguồn,
// đối trọng), lịch dữ liệu dùng chung với âm (spine.json: DRAW, RIDE, cues). Không vẽ thẻ chữ toàn màn hình.
export const C = { bg: '#0E1116', surface: '#171B22', grid: '#2A303B', ink: '#F2F4F7', muted: '#9AA4B2', accent: '#4C8DFF',
  warn: '#F2B441', costlier: '#C72323', cushion: '#269783' };
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => (b <= a ? (t >= a ? 1 : 0) : clamp((t - a) / (b - a)));
export const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
export const easeOut = (t, a, b) => 1 - Math.pow(1 - lin(t, a, b), 3);
export const easeBack = (t, a, b) => { const x = lin(t, a, b), s = 1.6; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export function rgba(hex, a) { const n = parseInt(hex.slice(1, 7), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }

export async function loadAll(base = '/moc-v/proto/') {
  const [spine, data] = await Promise.all([fetch(base + 'spine.json').then((r) => r.json()), fetch(base + 'data.json').then((r) => r.json())]);
  for (const w of [400, 600, 700]) await document.fonts.load(`${w} 48px Inter`);
  await document.fonts.ready;
  const cue = {}; for (const b of spine.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };
  const gain = data.gain.map((p) => p.y), value = gain.map((g) => g + 200000);
  const at = (arr, q) => { const i = Math.floor(clamp(q, 0, arr.length - 1)), f = q - i; return i + 1 < arr.length ? mix(arr[i], arr[i + 1], f) : arr[i]; };
  const qYear = (q) => 2000 + q / 4 + 0.125; // giữa quý
  return { spine, data, cue, interp, gain, value, at, qYear, CL: (id) => data.claims[id].display, T: spine.total };
}

export function makeCtx(canvas) {
  canvas.width = 1920; canvas.height = 1080;
  const ctx = canvas.getContext('2d');
  const FLOOR = 40;
  const text = (s, x, y, px, o = {}) => {
    const a = o.alpha ?? 1; if (a <= 0.01 || !s) return 0;
    px = Math.max(px, FLOOR);
    ctx.save(); ctx.globalAlpha *= a; ctx.font = `${o.w || 600} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums';
    ctx.textAlign = o.align || 'left'; ctx.textBaseline = o.base || 'alphabetic';
    const w = ctx.measureText(s).width;
    if (o.plate) { const pad = 14, x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
      ctx.fillStyle = rgba(o.plate, o.plateA ?? 0.9); roundRect(ctx, x0 - pad, y - px * 0.95, w + 2 * pad, px * 1.3, 10); ctx.fill(); }
    ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y); ctx.restore(); return w;
  };
  return { ctx, text, FLOOR };
}

export function roundRect(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }

// Lớp bắt buộc thành huy hiệu / chân trang nhỏ (đọc được ở 25 %: ≥ 40 px @1080). flags: {illus, hist, src, cw, measure}
export function chrome(K, flags, a = 1) {
  const { ctx, text } = K;
  if (flags.illus) { // ILLUSTRATIVE: góc trên phải, viên warn
    ctx.save(); ctx.globalAlpha = a; ctx.font = '700 40px Inter'; const w = ctx.measureText('ILLUSTRATIVE').width;
    ctx.fillStyle = rgba(C.warn, 0.16); roundRect(ctx, 1824 - w - 28, 56, w + 28, 58, 29); ctx.fill();
    ctx.strokeStyle = C.warn; ctx.lineWidth = 2; ctx.stroke(); ctx.restore();
    text('ILLUSTRATIVE', 1824 - 14, 99, 40, { w: 700, color: C.warn, align: 'right', alpha: a });
  }
  if (flags.hist) text('US only · history, not a forecast', 96, 1040, 40, { w: 600, color: '#B9C2CE', alpha: a });
  if (flags.src) text('Source: FHFA via FRED', 96, 99, 40, { w: 600, color: '#B9C2CE', alpha: a * (flags.srcA ?? 1) });
  if (flags.cw) text(flags.cw, 1824, 1040, 40, { w: 600, color: '#B9C2CE', align: 'right', alpha: a * (flags.cwA ?? 1) });
}

export function money(v) { return '$' + Math.round(v).toLocaleString('en-US'); }

// Người minh hoạ (không mặt, ink), đứng: x,y = chân giữa; s = tỉ lệ (1 → cao 220 px)
export function person(ctx, x, y, s, color = C.ink, o = {}) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.fillStyle = color;
  ctx.beginPath(); ctx.arc(0, -190, 30, 0, Math.PI * 2); ctx.fill();               // đầu
  roundRect(ctx, -38, -152, 76, 104, 30); ctx.fill();                             // thân
  ctx.fillRect(-30, -60, 24, 60); ctx.fillRect(6, -60, 24, 60);                   // chân
  if (o.hair) { ctx.beginPath(); ctx.arc(0, -196, 33, Math.PI * 0.95, Math.PI * 2.05); ctx.fill(); }
  ctx.restore();
}

// Nhà (vật thể thật, phẳng): đáy giữa x,y; rộng w; màu tường/mái; tuỳ chọn cửa sổ sáng
export function house(ctx, x, y, w, o = {}) {
  const h = w * 0.62, roof = w * 0.42, wall = o.wall || '#D9D4C7', roofC = o.roof || '#8A4B3A';
  ctx.save(); ctx.globalAlpha *= o.alpha ?? 1;
  ctx.fillStyle = wall; ctx.fillRect(x - w / 2, y - h, w, h);
  ctx.fillStyle = roofC; ctx.beginPath(); ctx.moveTo(x - w * 0.6, y - h + 2); ctx.lineTo(x, y - h - roof); ctx.lineTo(x + w * 0.6, y - h + 2); ctx.closePath(); ctx.fill();
  ctx.fillStyle = o.door || '#3B4A5A'; ctx.fillRect(x - w * 0.09, y - h * 0.55, w * 0.18, h * 0.55);
  ctx.fillStyle = o.win || '#F6D58E'; ctx.fillRect(x - w * 0.38, y - h * 0.72, w * 0.18, h * 0.24); ctx.fillRect(x + w * 0.2, y - h * 0.72, w * 0.18, h * 0.24);
  ctx.fillStyle = roofC; ctx.fillRect(x + w * 0.22, y - h - roof * 0.75, w * 0.1, roof * 0.45);
  ctx.restore();
  return { top: y - h - roof, h: h + roof };
}

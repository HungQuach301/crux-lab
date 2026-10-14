// R&D hình lai vòng 2 · mẫu cắm "MINH HOẠ 2D GIÀU" (style B): nét viền mực, chuyển màu, vân giấy, bán sắc (halftone), nền vẽ chi tiết.
// Vẽ hoàn toàn bằng mã trên canvas 2D (thiết kế 1920×1080), tất định (hash, không Math.random). Nhân vật = rig.js + lớp mực/đổ bóng/bán sắc.
import { drawCharacter, drawProp, PALETTE as P, hash } from '/rnd-hybrid/cutout/rig.js';
import { paperGrain } from '/rnd-hybrid/v2/paper3d.js';

export const INK = '#15171C';
export const lg = (ctx, x0, y0, x1, y1, stops) => { const g = ctx.createLinearGradient(x0, y0, x1, y1); stops.forEach(([o, c]) => g.addColorStop(o, c)); return g; };

// bán sắc: chấm theo lưới xoay 30°, bán kính theo hàm mật độ dens(x,y) ∈ [0,1]; vẽ trong vùng clip hiện hành
export function halftone(ctx, x0, y0, w, h, dens, { step = 9, color = INK, alpha = 0.5, angle = 0.52 } = {}) {
  ctx.save(); ctx.fillStyle = color; ctx.globalAlpha = alpha; const ca = Math.cos(angle), sa = Math.sin(angle), R = Math.hypot(w, h);
  ctx.beginPath();
  for (let u = -R; u < R; u += step) for (let v = -R; v < R; v += step) {
    const x = x0 + w / 2 + u * ca - v * sa, y = y0 + h / 2 + u * sa + v * ca; if (x < x0 - step || x > x0 + w + step || y < y0 - step || y > y0 + h + step) continue;
    const r = step * 0.55 * Math.sqrt(Math.max(0, Math.min(1, dens(x, y)))); if (r < 0.4) continue; ctx.moveTo(x + r, y); ctx.arc(x, y, r, 0, Math.PI * 2);
  }
  ctx.fill(); ctx.restore();
}

// khối có nét mực + chuyển màu dọc
export function block(ctx, x, y, w, h, top, bot, { ink = INK, lw = 3 } = {}) {
  ctx.fillStyle = lg(ctx, 0, y, 0, y + h, [[0, top], [1, bot]]); ctx.fillRect(x, y, w, h);
  ctx.lineWidth = lw; ctx.strokeStyle = ink; ctx.strokeRect(x, y, w, h);
}

// hình (rig) → canvas tạm → nét mực ngoài (nở theo vòng) + tô chuyển sáng-tối + bán sắc phía tối + vân giấy
export function inked(ctx, draw, { x, y, w = 760, h = 1120, pad = 30, outline = 6, light = [-1, -1], shade = 0.42, dots = 0.55, grain = 0.28, flat = null } = {}) {
  const c = new OffscreenCanvas(w, h), g = c.getContext('2d'); g.translate(w / 2, h - pad); draw(g); g.setTransform(1, 0, 0, 1, 0, 0);
  const sil = new OffscreenCanvas(w, h), s = sil.getContext('2d'); s.drawImage(c, 0, 0); s.globalCompositeOperation = 'source-in'; s.fillStyle = INK; s.fillRect(0, 0, w, h);
  // ánh sáng: dải tối chéo ngược hướng đèn
  g.save(); g.globalCompositeOperation = 'source-atop';
  g.fillStyle = lg(g, w * (0.5 + 0.5 * light[0]), h * (0.5 + 0.5 * light[1]), w * (0.5 - 0.5 * light[0]), h * (0.5 - 0.5 * light[1]),
    [[0, 'rgba(255,240,215,0.22)'], [0.45, 'rgba(0,0,0,0)'], [1, `rgba(10,14,24,${shade})`]]); g.fillRect(0, 0, w, h);
  if (dots > 0) halftone(g, 0, 0, w, h, (px, py) => ((px / w - 0.5) * -light[0] + (py / h - 0.5) * -light[1]) * 1.6 - 0.15, { step: 8, alpha: dots });
  g.globalAlpha = grain; g.globalCompositeOperation = 'multiply'; paperGrain(g, w, h, 1); g.restore();
  g.save(); g.globalCompositeOperation = 'destination-in'; g.drawImage(sil, 0, 0); g.restore();   // cắt lại theo hình (vân giấy tràn)
  const ox = x - w / 2, oy = y - (h - pad);
  if (flat) { const f = new OffscreenCanvas(w, h), fg = f.getContext('2d'); fg.drawImage(sil, 0, 0); fg.globalCompositeOperation = 'source-in'; fg.fillStyle = flat; fg.fillRect(0, 0, w, h); ctx.drawImage(f, ox, oy); return; }   // bóng đổ: chỉ hình bóng
  for (let i = 0; i < 16; i++) { const a = (i / 16) * Math.PI * 2; ctx.drawImage(sil, ox + Math.cos(a) * outline, oy + Math.sin(a) * outline); }
  ctx.drawImage(c, ox, oy);
}
export const inkChar = (ctx, ch, o) => inked(ctx, (g) => drawCharacter(g, { x: 0, y: 0, s: ch.s, id: ch.id, pose: ch.pose, expr: ch.expr, flip: ch.flip, noShadow: true }), o);
export const inkProp = (ctx, id, po, o) => inked(ctx, (g) => drawProp(g, id, { x: 0, y: 0, s: po.s ?? 1, label: po.label, doors: po.doors, noShadow: true }), o);

// mưa: nét mảnh chéo, tất định
export function rain(ctx, W, H, { n = 420, len = 34, a = 0.22, slant = 0.22, seed = 9 } = {}) {
  ctx.save(); ctx.strokeStyle = `rgba(200,214,236,${a})`; ctx.lineWidth = 1.6; ctx.beginPath();
  for (let i = 0; i < n; i++) { const x = hash(seed + i * 3) * (W + 200) - 100, y = hash(seed + i * 7 + 1) * H, l = len * (0.6 + 0.8 * hash(i + 11));
    ctx.moveTo(x, y); ctx.lineTo(x - l * slant, y + l); }
  ctx.stroke(); ctx.restore();
}

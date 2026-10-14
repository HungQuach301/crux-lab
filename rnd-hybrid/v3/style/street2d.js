// R&D vòng 3 · khung phong cách: MẶT TIỀN PHỐ 1930 vẽ bằng mã (dùng chung P1 'paper' và P3 'engrave').
//   facade(g, W, H, {kind:'shop'|'office', sign, awning, seed, style})  — gạch, cửa sổ khung kéo, phào, mái hiên sọc, biển chữ serif vẽ tay, thang thoát hiểm
//   bankFacade(g, W, H, {style})                                        — bậc thềm, 6 cột có rãnh, dầm chữ BANK, trán tường, cửa đồng đóng + tờ CLOSED
//   sky(g, W, H, {style}), pavement(g, W, H, {style})
// Không đồ vật hiện đại (không biển điện, không xe hiện đại, không điều hoà). Tất định (hash).
import { hash } from '/rnd-hybrid/cutout/rig.js';
import { INK } from '/rnd-hybrid/v3/style/figure1930.js';

const SEP = (c, st, k = 0.55) => { if (st.style !== 'engrave') return c; const n = parseInt(c.slice(1), 16), a = [n >> 16, (n >> 8) & 255, n & 255], L = (a[0] * 0.3 + a[1] * 0.59 + a[2] * 0.11) / 255;
  const s = [236, 222, 192].map((v) => v * (0.35 + 0.75 * L)); return 'rgb(' + a.map((v, i) => Math.round(v + (s[i] - v) * k)).join(',') + ')'; };
function hatchRect(g, x, y, w, h, d, st, ang = 0.0, gap = 6) {
  if (st.style !== 'engrave' || d <= 0.02) return; g.save(); g.beginPath(); g.rect(x, y, w, h); g.clip(); g.strokeStyle = INK; g.globalAlpha = 0.3 + d * 0.6; g.lineWidth = 1.1 + d;
  const R = Math.hypot(w, h), cx = x + w / 2, cy = y + h / 2, ca = Math.cos(ang), sa = Math.sin(ang), sp = gap / Math.max(0.25, d); g.beginPath();
  for (let s = -R; s <= R; s += sp) { g.moveTo(cx - ca * R - sa * s, cy - sa * R + ca * s); g.lineTo(cx + ca * R - sa * s, cy + sa * R + ca * s); } g.stroke(); g.restore(); }
const box = (g, x, y, w, h, fill, st, d = 0.3, lw = 3, ang = 0) => { g.fillStyle = SEP(fill, st); g.fillRect(x, y, w, h); hatchRect(g, x, y, w, h, d, st, ang); g.strokeStyle = INK; g.lineWidth = lw; g.strokeRect(x, y, w, h); };

export function facade(g, W, H, { kind = 'shop', sign = 'LUNCH', awning = '#8E3B33', brick = '#8A5A44', seed = 1, style = 'paper', fire = false } = {}) {
  const st = { style }, r = (k) => hash(seed * 131 + k);
  box(g, 0, 0, W, H, kind === 'office' ? '#9C9282' : brick, st, 0.35, 4);
  // gạch: hàng ngang + mạch so le
  g.save(); g.strokeStyle = INK; g.globalAlpha = style === 'engrave' ? 0.45 : 0.18; g.lineWidth = 1.2; const bh = Math.max(10, H / 90);
  for (let y = bh; y < H * 0.82; y += bh) { g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); if (kind !== 'office') for (let x = ((y / bh) % 2) * 14; x < W; x += 28) { g.beginPath(); g.moveTo(x, y - bh); g.lineTo(x, y); g.stroke(); } }
  g.restore();
  // phào mái
  box(g, -6, 0, W + 12, H * 0.035, '#6E6254', st, 0.6, 3); for (let x = 6; x < W; x += 22) box(g, x, H * 0.035, 10, H * 0.015, '#6E6254', st, 0.6, 1.5);
  // tầng trên: cửa sổ khung kéo (2 ô dọc), bậu, mi cửa
  const cols = Math.max(2, Math.round(W / 150)), rows = Math.max(2, Math.floor((H * 0.62) / 170)), cw = W / cols;
  for (let rI = 0; rI < rows; rI++) for (let c = 0; c < cols; c++) {
    const x = c * cw + cw * 0.24, y = H * 0.08 + rI * 170, w = cw * 0.52, h = 112, lit = r(rI * 7 + c) < 0.25;
    box(g, x - 8, y - 14, w + 16, 12, '#B8AC96', st, 0.2, 2);
    box(g, x, y, w, h, lit ? '#E9C88A' : '#2D3038', st, lit ? 0.1 : 0.85, 3, 1.57);
    g.strokeStyle = INK; g.lineWidth = 3; g.beginPath(); g.moveTo(x, y + h / 2); g.lineTo(x + w, y + h / 2); g.moveTo(x + w / 2, y); g.lineTo(x + w / 2, y + h); g.stroke();
    if (!lit && r(rI * 13 + c) < 0.5) box(g, x + 3, y + 3, w - 6, h * 0.32, '#C9BFA9', st, 0.15, 1.5);   // mành kéo
    box(g, x - 10, y + h, w + 20, 10, '#B8AC96', st, 0.2, 2);
  }
  if (fire) { g.save(); g.strokeStyle = INK; g.lineWidth = 3; for (let rI = 0; rI < rows; rI++) { const y = H * 0.08 + rI * 170 + 124, x0 = cw * 0.1, x1 = cw * 1.9;
    g.strokeRect(x0, y, x1 - x0, 6); for (let x = x0; x <= x1; x += 14) { g.beginPath(); g.moveTo(x, y); g.lineTo(x, y - 34); g.stroke(); } g.beginPath(); g.moveTo(x0, y - 34); g.lineTo(x1, y - 34); g.stroke();
    if (rI < rows - 1) { g.beginPath(); g.moveTo(x1 - 20, y); g.lineTo(x0 + 40, y + 170); g.stroke(); } } g.restore(); }
  // tầng trệt: cửa hàng — kính lớn, cửa, mái hiên sọc, biển chữ
  const gy = H * 0.72;
  box(g, 0, gy - 18, W, 18, '#5A4E44', st, 0.6, 3);
  if (sign) { box(g, W * 0.1, gy - 92, W * 0.8, 70, '#E9DFC6', st, 0.05, 3); g.fillStyle = INK; g.font = `700 ${Math.min(58, W * 0.09)}px Georgia, 'Times New Roman', serif`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(sign, W / 2, gy - 56); }
  box(g, W * 0.06, gy + 40, W * 0.56, H - gy - 60, '#2D3038', st, 0.8, 4, 1.57);
  g.save(); g.strokeStyle = INK; g.lineWidth = 3; g.beginPath(); g.moveTo(W * 0.06 + W * 0.28, gy + 40); g.lineTo(W * 0.06 + W * 0.28, H - 20); g.stroke(); g.restore();
  box(g, W * 0.7, gy + 30, W * 0.22, H - gy - 30, '#5A4330', st, 0.7, 4);
  if (awning) { const ay = gy + 4; g.save(); g.beginPath(); g.moveTo(-4, ay); g.lineTo(W + 4, ay); g.lineTo(W - 10, ay + 52); g.lineTo(10, ay + 52); g.closePath(); g.clip();
    for (let x = -10, k = 0; x < W + 20; x += 34, k++) { g.fillStyle = SEP(k % 2 ? awning : '#E9DFC6', st); g.fillRect(x, ay, 34, 52); } hatchRect(g, 0, ay, W, 52, 0.3, st, 0.6); g.restore();
    g.strokeStyle = INK; g.lineWidth = 3; g.beginPath(); g.moveTo(-4, ay); g.lineTo(W + 4, ay); g.lineTo(W - 10, ay + 52); g.lineTo(10, ay + 52); g.closePath(); g.stroke(); }
}

export function bankFacade(g, W, H, { style = 'paper', closed = true, columns = true } = {}) {
  const st = { style }, stone = '#CFC6B2', stoneD = '#A79E8B';
  box(g, W * 0.04, H * 0.24, W * 0.92, H * 0.62, stone, st, 0.2, 4);
  // bậc thềm
  for (let i = 0; i < 4; i++) box(g, W * (0.0 + i * 0.015), H * (0.86 + i * 0.035), W * (1 - i * 0.03), H * 0.035, i % 2 ? stone : stoneD, st, 0.25 + i * 0.05, 3);
  // trán tường + dầm
  g.fillStyle = SEP('#DCD3C0', st); g.beginPath(); g.moveTo(0, H * 0.21); g.lineTo(W / 2, H * 0.02); g.lineTo(W, H * 0.21); g.closePath(); g.fill(); g.save(); g.clip(); hatchRect(g, 0, 0, W, H * 0.22, 0.25, st, 0.3); g.restore();
  g.strokeStyle = INK; g.lineWidth = 4; g.stroke();
  box(g, -W * 0.01, H * 0.2, W * 1.02, H * 0.09, '#D6CDB9', st, 0.2, 4);
  g.fillStyle = INK; g.font = `700 ${H * 0.06}px Georgia, 'Times New Roman', serif`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText('B A N K', W / 2, H * 0.247);
  // cửa (giữa)
  const dx = W * 0.4, dw = W * 0.2, dy = H * 0.5;
  box(g, dx - 10, dy - 10, dw + 20, H * 0.36 + 10, '#2D2A26', st, 0.9, 4);
  for (const k of [0, 1]) { const x = dx + k * dw / 2 + 4; box(g, x, dy, dw / 2 - 8, H * 0.36, closed ? '#6B5236' : '#1E1C1A', st, closed ? 0.55 : 0.95, 3, 1.57);
    if (closed) for (const y of [0.3, 0.7]) box(g, x + 12, dy + H * 0.36 * y - 30, dw / 2 - 32, 60, '#7E6444', st, 0.4, 2); }
  if (closed) { // tờ CLOSED dán chéo
    g.save(); g.translate(W / 2, dy + H * 0.13); g.rotate(-0.06); box(g, -W * 0.09, -H * 0.045, W * 0.18, H * 0.09, '#F2EAD6', st, 0.03, 3);
    g.fillStyle = '#8E2B2B'; g.font = `800 ${H * 0.058}px Georgia, serif`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText('CLOSED', 0, 2); g.restore(); }
  // 6 cột có rãnh
  for (let i = 0; i < 6; i++) { if (i === 2 || i === 3 || !columns) continue; const cx = W * (0.1 + i * 0.16), cw = W * 0.07, y0 = H * 0.3, y1 = H * 0.86;
    box(g, cx - cw * 0.7, y0 - 8, cw * 1.4, 18, '#D6CDB9', st, 0.2, 3); box(g, cx - cw * 0.65, y1 - 14, cw * 1.3, 16, '#D6CDB9', st, 0.2, 3);
    g.fillStyle = SEP('#E2DACA', st); g.fillRect(cx - cw / 2, y0 + 10, cw, y1 - y0 - 24);
    g.save(); g.beginPath(); g.rect(cx - cw / 2, y0 + 10, cw, y1 - y0 - 24); g.clip(); hatchRect(g, cx + cw * 0.15, y0, cw * 0.4, y1 - y0, 0.55, st, 1.57, 4);
    if (style !== 'engrave') { g.fillStyle = 'rgba(0,0,0,0.16)'; g.fillRect(cx + cw * 0.18, y0, cw * 0.32, y1 - y0); } g.restore();
    g.strokeStyle = INK; g.lineWidth = 1.6; for (let f = 1; f < 5; f++) { g.beginPath(); g.moveTo(cx - cw / 2 + f * cw / 5, y0 + 12); g.lineTo(cx - cw / 2 + f * cw / 5, y1 - 16); g.stroke(); }
    g.lineWidth = 3.5; g.strokeRect(cx - cw / 2, y0 + 10, cw, y1 - y0 - 24); }
  // cửa sổ cao hai bên cửa chính
  for (const x of [W * 0.27, W * 0.66]) box(g, x, H * 0.42, W * 0.07, H * 0.3, '#2D3038', st, 0.85, 3, 1.57);
}

export function sky(g, W, H, { style = 'paper', top = '#2E3442', bottom = '#7A7468' } = {}) {
  const gr = g.createLinearGradient(0, 0, 0, H); gr.addColorStop(0, style === 'engrave' ? '#B9AE96' : top); gr.addColorStop(1, style === 'engrave' ? '#E4D8BE' : bottom); g.fillStyle = gr; g.fillRect(0, 0, W, H);
  if (style === 'engrave') { g.save(); g.strokeStyle = INK; for (let y = 6; y < H; y += 7) { g.globalAlpha = 0.5 * (1 - y / H); g.lineWidth = 1.2; g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); } g.restore(); }
  // đường chân trời: nhà cao xa (khối đơn, không chi tiết hiện đại)
  for (let i = 0; i < 14; i++) { const w = W / 14 * (0.7 + hash(i + 3) * 0.5), h = H * (0.25 + hash(i * 7 + 1) * 0.35), x = i * W / 14;
    g.fillStyle = style === 'engrave' ? 'rgba(90,80,64,0.55)' : 'rgba(40,46,58,0.75)'; g.fillRect(x, H - h, w, h); if (style === 'engrave') { g.save(); g.beginPath(); g.rect(x, H - h, w, h); g.clip(); g.strokeStyle = INK; g.globalAlpha = 0.35; for (let s = -h; s < w; s += 6) { g.beginPath(); g.moveTo(x + s, H - h); g.lineTo(x + s + h, H); g.stroke(); } g.restore(); } }
}
export function pavement(g, W, H, { style = 'paper' } = {}) {
  g.fillStyle = style === 'engrave' ? '#CFC2A6' : '#6A645C'; g.fillRect(0, 0, W, H);
  g.save(); g.strokeStyle = INK; g.globalAlpha = style === 'engrave' ? 0.55 : 0.3; g.lineWidth = 1.5;
  for (let y = 0; y < H; y += 26) for (let x = (y / 26 % 2) * 20; x < W; x += 40) { g.strokeRect(x, y, 40, 26); }
  if (style === 'engrave') for (let y = 0; y < H; y += 5) { g.globalAlpha = 0.25; g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
  g.restore();
}

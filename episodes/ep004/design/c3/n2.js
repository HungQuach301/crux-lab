// Bố cục: dải trên-phải (dòng đối trọng của engine) và dưới-phải (nhãn lịch sử) để trống.
// Tập 4 · ký hiệu mới N2 "threshold ladder" (beats.md B13 + B14 · KEY-6, cảnh S13, S14). Nạp qua custom_symbols của episode.yaml.
// Nghĩa: "một giá mua năm 2000 mà trên nó lãi vượt trần, mỗi nơi một giá". Một thước giá DỌC (cùng thang ở B13 và B14):
//   B13 (mode 'phoenix'): mốc Phoenix ≈ $179,200; chấm cặp đôi $200,000 ngay trên (ILLUSTRATIVE); thước tách: dưới mốc trung tính
//        "under the cap", trên mốc warn "over the cap".
//   B14 (mode 'ladder'): 12 bậc thành phố tại giá ngưỡng (ink), bậc quốc gia đứt (ink-muted), thanh tăng trưởng mảnh chỉ TRÁI (accent =
//        chỉ số thị trường; dài ∝ ×tăng, dài nhất ở dưới), vạch ngang $300,000 (giá ILLUSTRATIVE), tiêu đề cuối.
// Vị trí bậc/thanh từ DATA.rungs (out/model.json, làm tròn như numbers.md); mọi chữ số trên hình là claim ({claimId}). Thước là vị trí giá
// (như swarm), không phải độ dài; thanh tăng trưởng là độ dài từ thước (0 = không thanh).
import { ease, easeOut, lin, mix, clamp } from '/toolkit/factory/lib/engine.js';

const at = (p, k, def = 0) => (typeof p[k] === 'number' ? p[k] : def);
const fade = (t, a0) => ease(t, a0, a0 + 0.4);
const RX = 900, RW = 22, LO = 100000, HI = 400000, YB = 900, YT = 290;   // thước: x, bề rộng, khoảng giá, y đáy/đỉnh
const Y = (v) => mix(YB, YT, (v - LO) / (HI - LO));
const LX = RX + RW / 2 + 120;                                               // cột tên thành phố

// nhãn tên không chồng nhau: nới đều từ vị trí mong muốn (khoảng ≥ gap), giữ trong [lo, hi]
function spread(ys, gap, lo, hi) {
  const y = ys.slice();
  for (let it = 0; it < 200; it++) {
    let moved = false;
    for (let i = 1; i < y.length; i++) { const d = y[i - 1] - y[i]; if (d < gap) { const s = (gap - d) / 2 + 0.01; y[i - 1] += s; y[i] -= s; moved = true; } }
    for (let i = 0; i < y.length; i++) y[i] = clamp(y[i], lo, hi);
    if (!moved) break;
  }
  return y;
}

function ruler(E, t, a0, split) {
  const top = Y(HI), bot = Y(LO), al = fade(t, a0);
  E.text('{buy_year} purchase price', RX - RW / 2 - 24, top + 10, 'note', { align: 'right', color: E.C.muted, alpha: al, group: 'n2-ruler' });
  if (split == null) { E.rect(RX - RW / 2, top, RW, bot - top, E.C.grid, al); return; }
  const k = split.k, ym = Y(split.v);
  E.rect(RX - RW / 2, top, RW, bot - top, E.C.grid, al);
  E.rect(RX - RW / 2, ym, RW, (bot - ym) * k, E.C.muted, 0.75 * k);                 // trung tính: dưới ngưỡng
  E.rect(RX - RW / 2, ym - (ym - top) * k, RW, (ym - top) * k, E.C.above || E.C.warn, k); // warn: trên ngưỡng
}

export const n2 = { draw(E, t, p) {
  const R = E.data.rungs, a0 = at(p, 'at');
  if (p.mode === 'phoenix') {
    const ph = R.find((r) => r.slug === 'phoenix'), sa = at(p, 'splitAt', 1e9), k = easeOut(t, sa, sa + 1.0);
    ruler(E, t, a0, { v: ph.threshold, k });
    E.CL('threshold_joint_phoenix');
    const y = Y(ph.threshold), ma = fade(t, a0);
    E.line([[RX - 70, y], [RX + 70, y]], E.C.ink, 8, ma);
    E.text('Phoenix · {threshold_joint_phoenix}', RX + 100, y + 18, 'label', { alpha: ma, group: 'n2-ph' });
    const da = at(p, 'dotAt', a0 + 0.5), cy = Y(+E.claims.illustrative_price_200k_usd.value), dk = easeOut(t, da, da + 0.6);
    if (t >= da) { E.dot(RX, cy, 18 * dk, E.C.gain || E.C.ink, 1, E.C.bg); E.illustrative(); }
    E.text('Rosa & Frank · {illustrative_price_200k_usd}', RX - 60, cy - 30, 'label', { align: 'right', alpha: fade(t, da), group: 'n2-rf' });
    E.text('over the cap', RX - 60, Y(330000), 'label', { align: 'right', color: E.C.above || E.C.warn, alpha: fade(t, at(p, 'overAt', sa + 0.6)), group: 'n2-over' });
    E.text('under the cap', RX - 60, Y(125000), 'label', { align: 'right', alpha: fade(t, at(p, 'underAt', sa + 0.3)), group: 'n2-under' });
    E.historical();
    return;
  }
  // ---- ladder (B14)
  ruler(E, t, a0, null);
  const r0 = at(p, 'rungsAt0', a0), r1 = at(p, 'rungsAt1', r0 + 4), n = R.length;
  const ly = spread(R.map((r) => Y(r.threshold) + 16), 47, Y(HI) + 40, YB + 35);
  const ba = at(p, 'barsAt', 1e9), gmax = Math.max(...R.map((r) => r.growth)), BL = 560;
  R.forEach((r, i) => {
    const ra = mix(r0, r1, i / (n - 1)), al = fade(t, ra); if (al <= 0) return;   // bậc rơi vào từ dưới lên
    E.CL(`threshold_joint_${r.slug}`);
    const drop = (1 - easeOut(t, ra, ra + 0.5)) * 40, y = Y(r.threshold) - drop;
    E.line([[RX - 40, y], [RX + 60, y]], r.national ? E.C.muted : E.C.ink, r.national ? 5 : 6, al, r.national ? [12, 9] : undefined);
    E.line([[RX + 64, y], [LX - 12, ly[i] - 16]], E.C.grid, 2, al);
    const lab = r.slug === 'miami' || r.slug === 'chicago' ? `${r.name} {threshold_joint_${r.slug}}` : r.name;
    const la = r.slug === 'miami' ? at(p, 'minAt', 1e9) : r.slug === 'chicago' ? at(p, 'maxAt', 1e9) : 1e9;
    E.text(t >= la ? lab : r.name, LX, ly[i], 42, { color: r.national ? E.C.muted : E.C.ink, alpha: al, group: 'n2-l' + i });
    // thanh tăng trưởng mảnh, chỉ trái, dài ∝ tăng (quốc gia: đứt như bậc của nó)
    const gk = easeOut(t, ba + 0.08 * (n - 1 - i), ba + 0.08 * (n - 1 - i) + 1.2);
    if (gk > 0) { E.CL(`growth_${r.slug}`); E.line([[RX - 44, y], [RX - 44 - BL * r.growth / gmax * gk, y]], E.C.index || E.C.accent, 7, 0.9, r.national ? [12, 9] : undefined); }
  });
  [['miami', 'gMinAt'], ['chicago', 'gMaxAt']].forEach(([s, k], j) => {
    const r = R.find((x) => x.slug === s), ga = at(p, k, 1e9);
    E.text(`{growth_${s}}`, RX - 64 - BL * r.growth / gmax, Y(r.threshold) + 16, 'label', { align: 'right', alpha: fade(t, ga), group: 'n2-g' + j });
  });
  if (t >= ba) E.text('price growth since {buy_year}', RX - 44 - BL, YB + 50, 'note', { color: E.C.muted, alpha: fade(t, ba), group: 'n2-gl' });
  // vạch $300,000 (giá ILLUSTRATIVE): cắt ngang thước và thanh, không qua cột tên
  const ra = at(p, 'refAt', 1e9), rk = easeOut(t, ra, ra + 0.8), yr = Y(+E.claims.illustrative_price_300k_usd.value);
  if (t >= ra) { E.line([[RX + 70, yr], [RX + 70 - (RX + 70 - (RX - 44 - BL)) * rk, yr]], E.C.ink, 4, 1); E.CL('illustrative_price_300k_usd'); }
  E.text('{illustrative_price_300k_usd} purchase', RX - 44 - BL, yr - 30, 'label', { alpha: fade(t, ra + 0.3), group: 'n2-ref' });
  // tiêu đề cuối (S14.5)
  const ta = at(p, 'titleAt', 1e9);
  E.text('{buy_year} price where the gain', E.SAFE.x0 + 24, 190, 'note', { alpha: fade(t, ta), group: 'n2-t1' });
  E.text('reaches the {excl_joint_limit_usd} cap', E.SAFE.x0 + 24, 246, 'note', { alpha: fade(t, ta), group: 'n2-t2' });
  E.historical();
} };

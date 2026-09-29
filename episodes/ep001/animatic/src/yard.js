// The yard (signed SF5 world), shared by S14-S17 and S20: houses on a lawn (volume = loan), and in front of each
// borrower a "pair": a ream = loan costs, a hatched slab on it = still owed on the new loan vs the old one (grows with
// the month), and a column of monthly-savings bundles. One dollar scale K per scene.
import { THREE, C, DATA, CL, mix, easeOut, clamp, box, mat, pm, canvasTex, ptxt, paperEdgeTex, owedTex, house } from './engine.js';
import { outdoors, shadowAll } from './common.js';

export const WHO = {
  walt: { d: () => DATA.small, cost: () => CL('cost_small'), hx: -5.2, hz: -3.2, px: -5.4, wall: '#CDBF9F', roof: '#4A4036' },
  nora: { d: () => DATA.median, cost: () => CL('cost_median'), hx: 0.3, hz: -3.9, px: 0.1, wall: '#C9BBA4', roof: '#3B3F48' },
  anjali: { d: () => DATA.large, cost: () => CL('cost_large'), hx: 6.2, hz: -4.8, px: 5.6, wall: '#B9C3CC', roof: '#3A404C' },
};
export function makeYard({ scene, renderer }, { who = ['walt', 'nora', 'anjali'], K = 2.1 / 14000, months = 36, FW = 1.0, FD = 0.8, Z = 1.2, gapKey = 'gap', data = {} } = {}) {
  outdoors(scene, renderer, { trees: 14 });
  const base = { w: 2.1, d: 1.8, h: 1.25, roof: 0.9 };
  const edge = paperEdgeTex();
  const out = {};
  for (const k of who) {
    const W0 = WHO[k], d = data[k] || W0.d(), s = Math.cbrt(d.loan / DATA.small.loan);
    const h = shadowAll(house({ w: base.w * s, d: base.d * s, h: base.h * s, roof: base.roof * s, wall: W0.wall, roofCol: W0.roof, lit: 0.3 }));
    h.position.set(W0.hx, 0, W0.hz); scene.add(h);
    const rh = d.cost * K;
    const front = canvasTex(512, Math.max(96, Math.round(512 * rh / FW)), (g, w, hh) => {
      g.fillStyle = C.paper; g.fillRect(0, 0, w, hh); for (let y = 0; y < hh; y += 6) { g.fillStyle = C.paperLine; g.fillRect(0, y, w, 2); }
      g.fillStyle = '#2E3440'; g.fillRect(0, hh * 0.12, w, hh * 0.76); ptxt(g, W0.cost(), w / 2, hh * 0.5 + 40, { size: 118, weight: 700, color: '#FFFFFF', align: 'center' });
    });
    const ream = box(FW, rh, FD, [pm(edge), pm(edge), pm(edge), pm(edge), pm(front), pm(edge)]); ream.userData.h = rh; scene.add(ream);
    const ot = owedTex(); ot.repeat.set(1.5, 1);
    const owed = box(FW + 0.02, 1, FD + 0.02, new THREE.MeshStandardMaterial({ map: ot, roughness: 0.85 })); scene.add(owed);
    const noteTex = canvasTex(256, 128, (g, w, hh) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, hh); g.strokeStyle = '#6FA383'; g.lineWidth = 6; g.strokeRect(8, 8, w - 16, hh - 16); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 36, 0, 72, hh); });
    const cs = mat(C.cashSide, { roughness: 0.95 }), bandS = mat(C.cashBand, { roughness: 0.9 });
    const th = d.sav * K, geo = new THREE.BoxGeometry(FW * 0.92, th * 0.9, FD * 0.8), cm = [cs, cs, pm(noteTex), cs, bandS, cs];
    const col = []; for (let i = 0; i < months; i++) { const b = new THREE.Mesh(geo, cm); b.castShadow = b.receiveShadow = true; b.userData = { jx: Math.sin(i * 12.99 + d.sav) * 0.02, jr: Math.sin(i * 78.2 + d.sav) * 0.03 }; b.visible = false; scene.add(b); col.push(b); }
    const laser = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(laser);
    out[k] = { house: h, ream, owed, col, laser, d, th, rh, x: W0.px, xs: W0.px + 1.35, Z, FW, FD,
      gapAt(m) { const arr = d[gapKey] || d.gap; const a = Math.floor(m), b = Math.min(arr.length - 1, a + 1); return mix(arr[a] || 0, arr[b] || 0, m - a); },
    };
  }
  // st: { houseGrow, reamIn (0..1 drop), month, colOn, owedOn, laser, colDx }
  function update(k, st) {
    const o = out[k]; if (!o) return;
    o.house.scale.set(1, Math.max(0.001, st.houseGrow ?? 1), 1); o.house.visible = (st.houseGrow ?? 1) > 0.001;
    if (st.lit !== undefined) o.house.userData.winMat.emissiveIntensity = st.lit;
    const r = st.reamIn ?? 1; o.ream.visible = r > 0; o.ream.position.set(o.x, o.rh / 2 + (1 - r) * 3, o.Z);
    const m = st.month ?? 0;
    const g = Math.max(0.001, o.gapAt(m) * K); o.owed.visible = (st.owedOn ?? 0) > 0 && m > 0.05; o.owed.scale.y = g; o.owed.position.set(o.x, o.rh + g / 2, o.Z);
    const nOn = st.colOn ?? 1;
    o.col.forEach((b, i) => { const land = easeOut(m, i, i + 0.9); b.visible = nOn > 0 && m > i; b.position.set(o.xs + b.userData.jx, o.th * (i + 0.5) + (1 - land) * 0.5, o.Z + b.userData.jx); b.rotation.y = b.userData.jr + (1 - land) * 0.3; });
    const top = o.rh + ((st.owedOn ?? 0) > 0 ? o.gapAt(m) * K : 0);
    o.laser.position.set((o.x + o.xs) / 2, top + 0.012, o.Z + o.FD / 2 + 0.03); o.laser.material.opacity = st.laser ?? 0;
    const full = o.d.sav * m * K >= top - 1e-4; o.laser.material.color.set(full && m > 0 ? C.positive : (st.laserRed ? C.negative : '#FFFFFF'));
  }
  return { out, update, K };
}

// The history table shared by K3-K7 + thumbnail: ridge (TB3MS 1954-2026), two trays under its halves, the 10-year
// frame with its own rail (9% = 1.5 points above the ridge at the frame's start) and Leah's bead riding the ridge top.
// Because Leah's rate = 7.5% + (T-bill now - T-bill at start) (floored, model.py), "rate above 9%" <=> "ridge above the
// frame's rail": the ridge itself is the track.
import { THREE, C, DATA, mix, ease, clamp } from './engine.js';
import { lights, table, ridge, ridgeWire, rail, bead, bracket, frame, ghostFrame, trays, xOf, DX, KY, RIDGE, Z, NM, STARTS } from './world.js';

export const NS = STARTS.length; // 753
export function history(scene, o = {}) {
  lights(scene, { key: [-3, 12, 9], target: [0, 0.5, -0.5], power: o.power ?? 170, shadowSize: 2048 });
  table(scene, 26, 16, 0.5);
  const R = ridge(scene);
  const TR = trays(scene);
  const F = frame(scene);
  const ghosts = (o.ghosts ?? 0) ? [0, 1, 2].map(() => ghostFrame(scene)) : [];
  const WIRE = ridgeWire(scene);
  const FR = rail(scene, 120); // rail inside the frame, one amber segment per month of the window
  const B = bead(scene, 0.085);
  const BR = bracket(scene, { arm: 0.1, th: 0.028 });
  const railY = (k) => KY * (RIDGE[k] + 1.5); // ridge index of start k == k (1954-01 is index 0)
  // place the frame (and its rail, wire, bead) at start k (may be fractional for sliding); bm = months travelled by the bead
  function placeFrame(k, { alpha = 1, lift = 0, bm = 0, wire = 1, wireUpto = 1, litUpto = -1, railA = 1, bracketA = 0 } = {}) {
    const ki = Math.round(k);
    F.position.x = xOf(k); F.position.y = lift; F.userData.alpha(alpha);
    const ry = railY(ki);
    FR.userData.place(xOf(k), xOf(k + 119), ry, Z.rail + 0.02, (j) => (j <= litUpto && RIDGE[ki + j] > RIDGE[ki] + 1.5 ? 1 : 0), alpha * railA);
    WIRE.visible = wire > 0.01 && alpha > 0.01; if (WIRE.visible) WIRE.userData.set(ki, 120, 0, Z.ridge1 + 0.03, wireUpto);
    const m = Math.min(119, bm), j = Math.floor(m), f = m - j;
    const by = KY * mix(RIDGE[ki + j], RIDGE[Math.min(NM - 1, ki + j + 1)], f) + 0.085;
    B.visible = alpha > 0.3; B.position.set(xOf(k + m), by, Z.ridge1 + 0.05);
    BR.userData.set(xOf(k) - 0.06, KY * RIDGE[ki] + 0.085, ry, Z.ridge1 + 0.05, bracketA);
  }
  return { R, TR, F, ghosts, WIRE, FR, B, BR, placeFrame, railY };
}
export function costlierAt(gap, k) { return DATA.costlier[String(gap)][k]; }

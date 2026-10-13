// Tập 8 · vật thể MỚI thử trước G1 (luật tạm 13/10 (c)) — dựng trên lib3d (W1 House, W4 Person, W9 Apartment, Studio).
// N1 Street: 307 nhà giống hệt dọc một con đường (trái → phải = tháng mua 1991 → 2016); đèn cửa sổ sáng = người mua hơn sau 10 năm,
//    tối + cửa warn = người thuê hơn. .set({lit: [0..1 mỗi nhà], doorWarn: [0..1]}).
// N2 RentTag: thẻ treo cửa căn hộ, mặt số giả định tiền thuê (ink-muted = mức giả định); .set({value}) xoay kim + đổi chữ (canvas).
// N3 NinaLamp: đèn ấm riêng của nhân vật dẫn đường (PointLight + quả cầu nhỏ), đi theo người; .set({on, t}) nhịp thở sáng.
import * as THREE from 'three';
import { PALETTE, House } from '/toolkit/factory/world/lib3d.js';

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });
export const LAMP = '#FFB86B';

export function Street({ n = 307, gap = 0.62, w = 0.5 } = {}) {
  const g = new THREE.Group(), houses = [];
  const road = new THREE.Mesh(new THREE.BoxGeometry(n * gap + 2, 0.02, 0.9), mat('#232934'));
  road.position.set((n - 1) * gap / 2, 0.01, 0.75); road.receiveShadow = true; g.add(road);
  for (let i = 0; i < n; i++) {
    const h = House({ w, lit: false });
    h.position.set(i * gap, 0, 0);
    const wins = [], doors = [];
    h.traverse((o) => { if (o.isMesh && o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) wins.push(o); });
    h.children.forEach((o) => { if (o.isMesh && o.material.color && o.material.color.getHexString() === '3b4a5a') doors.push(o); });
    for (const m of wins) m.material = m.material.clone();
    for (const m of doors) m.material = m.material.clone();
    houses.push({ h, wins, doors }); g.add(h);
  }
  const warn = new THREE.Color(PALETTE.warn), door0 = new THREE.Color('#3B4A5A');
  g.userData = { gap, n,
    set({ lit = [], doorWarn = [] } = {}) {
      houses.forEach((o, i) => {
        const a = lit[i] || 0, d = doorWarn[i] || 0;
        for (const m of o.wins) m.material.emissiveIntensity = 1.1 * a;
        for (const m of o.doors) { m.material.color.copy(door0).lerp(warn, d); m.material.emissive = warn.clone(); m.material.emissiveIntensity = 0.35 * d; }
      });
    } };
  return g;
}

function tagTexture(text) {
  const c = document.createElement('canvas'); c.width = 512; c.height = 256;
  const x = c.getContext('2d');
  x.fillStyle = '#171B22'; x.fillRect(0, 0, 512, 256);
  x.strokeStyle = PALETTE.muted; x.lineWidth = 10; x.strokeRect(8, 8, 496, 240);
  x.fillStyle = PALETTE.ink; x.font = 'bold 64px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText('RENT', 256, 72); x.fillStyle = PALETTE.muted; x.font = 'bold 96px Inter, sans-serif'; x.fillText(text, 256, 170);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}

export function RentTag({ w = 0.9 } = {}) {
  const g = new THREE.Group();
  const card = new THREE.Mesh(new THREE.BoxGeometry(w, w / 2, 0.03), [mat('#171B22'), mat('#171B22'), mat('#171B22'), mat('#171B22'),
    new THREE.MeshStandardMaterial({ map: tagTexture('5%'), roughness: 0.6 }), mat('#171B22')]);
  g.add(card);
  const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.008, 0.008, 0.35), mat(PALETTE.muted)); cord.position.set(0, w / 4 + 0.17, 0); g.add(cord);
  let last = null;
  g.userData = { set({ value = 5, swing = 0 } = {}) {
    const txt = value.toFixed(0) + '%';
    if (txt !== last) { card.material[4].map.dispose(); card.material[4].map = tagTexture(txt); card.material[4].needsUpdate = true; last = txt; }
    g.rotation.z = swing;
  } };
  return g;
}

export function NinaLamp() {
  const g = new THREE.Group();
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 8), new THREE.MeshStandardMaterial({ color: LAMP, emissive: new THREE.Color(LAMP), emissiveIntensity: 2 }));
  const light = new THREE.PointLight(LAMP, 3, 3.2, 1.6);
  g.add(bulb); g.add(light);
  g.userData = { set({ on = 1, t = 0 } = {}) {
    const k = on * (0.85 + 0.15 * Math.sin(t * 2.1));
    light.intensity = 3 * k; bulb.material.emissiveIntensity = 2 * k; bulb.visible = on > 0.02;
  } };
  return g;
}

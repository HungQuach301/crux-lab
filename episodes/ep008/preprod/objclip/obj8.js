// Tập 8 · vật thể MỚI thử trước G1 (luật tạm 13/10 (c)) — dựng trên lib3d (W1 House, W4 Person, W9 Apartment, Studio).
// N1 Street: 307 nhà giống hệt dọc một con đường (trái → phải = tháng mua 1991 → 2016); đèn cửa sổ sáng = người mua hơn sau 10 năm,
//    tối + cửa warn = người thuê hơn. .set({lit: [0..1 mỗi nhà], doorWarn: [0..1]}).
// N2 RentTag: thẻ treo cửa căn hộ, mặt số giả định tiền thuê (ink-muted = mức giả định); .set({value}) xoay kim + đổi chữ (canvas).
// N3 NinaLamp: đèn ấm riêng của nhân vật dẫn đường (PointLight + quả cầu nhỏ), đi theo người; .set({on, t}) nhịp thở sáng.
import * as THREE from 'three';
import { PALETTE, House } from '/toolkit/factory/world/lib3d.js';

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });
export const LAMP = '#FFB86B';

export function Street({ starts, gap = 0.95, rowGap = 0.95, w = 0.55 } = {}) {
  // lưới các tháng mua: cột = năm (trái → phải 1991 → 2016), hàng = tháng (Jan ở trước máy); mỗi nhà một tháng bắt đầu
  const g = new THREE.Group(), houses = [];
  const y0 = Number(starts[0].slice(0, 4)), ny = Number(starts[starts.length - 1].slice(0, 4)) - y0 + 1;
  for (let c = 0; c < ny; c++) {   // mỗi năm một con phố ngắn (dải đường dưới cột)
    const road = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.02, 12 * rowGap), mat('#232934'));
    road.position.set(c * gap + 0.42, 0.01, -5.5 * rowGap); road.receiveShadow = true; g.add(road);
  }
  starts.forEach((s, i) => {
    const c = Number(s.slice(0, 4)) - y0, r = Number(s.slice(5, 7)) - 1;
    const h = House({ w, lit: false }); h.rotation.y = Math.PI / 2; h.position.set(c * gap, 0, -r * rowGap);
    const wins = [], doors = [], walls = [], roofs = [];
    h.traverse((o) => { if (!o.isMesh) return; const hx = o.material.color.getHexString();
      if (o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) wins.push(o);
      else if (hx === '3b4a5a') doors.push(o); else if (hx === 'd9d4c7') walls.push(o); else roofs.push(o); });
    for (const m of [...wins, ...doors, ...walls, ...roofs]) m.material = m.material.clone();
    houses.push({ wins, doors, walls, roofs }); g.add(h);
  });
  const warn = new THREE.Color(PALETTE.warn), door0 = new THREE.Color('#3B4A5A'), glow = new THREE.Color('#F6D58E');
  const neutral = new THREE.Color('#7E838C'), dim = new THREE.Color('#3A3E46'), roof0 = new THREE.Color('#5B5F66'), roofLit = new THREE.Color('#C98A4E');
  g.userData = { gap, rowGap, ny, y0,
    set({ lit = [], doorWarn = [] } = {}) {
      houses.forEach((o, i) => {
        const a = lit[i] || 0, d = doorWarn[i] || 0;
        for (const m of o.wins) m.material.emissiveIntensity = 1.5 * a;
        for (const m of o.walls) { m.material.color.copy(neutral).lerp(glow, a).lerp(dim, d); m.material.emissive = glow; m.material.emissiveIntensity = 0.55 * a; }
        for (const m of o.roofs) { m.material.color.copy(roof0).lerp(roofLit, a).lerp(dim, d); m.material.emissive = roofLit; m.material.emissiveIntensity = 0.35 * a; }
        for (const m of o.doors) { m.material.color.copy(door0).lerp(warn, d); m.material.emissive = warn; m.material.emissiveIntensity = 0.5 * d; }
      });
    } };
  return g;
}

function tagTexture(text, head = 'RENT') {
  const c = document.createElement('canvas'); c.width = 512; c.height = 256;
  const x = c.getContext('2d');
  x.fillStyle = '#171B22'; x.fillRect(0, 0, 512, 256);
  x.strokeStyle = PALETTE.muted; x.lineWidth = 10; x.strokeRect(8, 8, 496, 240);
  x.fillStyle = PALETTE.ink; x.font = 'bold 64px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText(head, 256, 72); x.fillStyle = PALETTE.muted; x.font = 'bold 96px Inter, sans-serif'; x.fillText(text, 256, 170);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}

export function RentTag({ w = 0.9, head = 'RENT', blank = false } = {}) {
  const g = new THREE.Group();
  const card = new THREE.Mesh(new THREE.BoxGeometry(w, w / 2, 0.03), [mat('#171B22'), mat('#171B22'), mat('#171B22'), mat('#171B22'),
    new THREE.MeshStandardMaterial({ map: tagTexture(blank ? '' : '5%', head), roughness: 0.6 }), mat('#171B22')]);
  g.add(card);
  const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.008, 0.008, 0.35), mat(PALETTE.muted)); cord.position.set(0, w / 4 + 0.17, 0); g.add(cord);
  let last = null;
  g.userData = { set({ value = 5, swing = 0 } = {}) {
    const txt = value.toFixed(0) + '%';
    if (!blank && txt !== last) { card.material[4].map.dispose(); card.material[4].map = tagTexture(txt); card.material[4].needsUpdate = true; last = txt; }
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

// R&D vòng 3 · khung phong cách P2: SA BÀN TƯỢNG NHỎ. Mọi thứ dựng bằng mã từ khối bo tròn cùng một chất (thạch cao/đất sơn mờ):
// người (áo khoác, mũ phớt, váy dài, mũ chuông là khối thật), mặt tối giản (mắt, lông mày, miệng theo cảm xúc), nhà 1930 (gạch sơn, cửa sổ khung kéo,
// phào, mái hiên), ngân hàng tân cổ điển. Hậu kỳ: độ sâu trường ảnh nông (tilt-shift) theo depth. Ánh sáng hồi khủng hoảng: trời lạnh + đèn phố ấm.
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { hash } from '/rnd-hybrid/cutout/rig.js';

const M = new Map();
const mat = (c, r = 0.82) => { const k = c + r; if (!M.has(k)) M.set(k, new THREE.MeshStandardMaterial({ color: c, roughness: r, metalness: 0 })); return M.get(k); };
const add = (g, geo, m, x = 0, y = 0, z = 0, rx = 0, ry = 0, rz = 0) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.rotation.set(rx, ry, rz); o.castShadow = o.receiveShadow = true; g.add(o); return o; };
const rbox = (w, h, d, r = 0.02) => new RoundedBoxGeometry(w, h, d, 3, Math.min(r, w / 2.1, h / 2.1, d / 2.1));
const lathe = (pts, seg = 28) => new THREE.LatheGeometry(pts.map(([r, y]) => new THREE.Vector2(r, y)), seg);
const SK = { light: '#E6C2A0', medium: '#C79270', tan: '#A87450', dark: '#74482F', deep: '#4F3123' };
const COAT = { charcoal: '#464B53', brown: '#6E5644', navy: '#38445C', grey: '#767A82', tweed: '#7D6C55', camel: '#9C7E58', plum: '#6C5674', green: '#506A5A' };

// ---- tượng người (cao ≈ 1,75; gốc giữa hai chân, nhìn +z)
export function figurine({ sex = 'm', skin = 'light', coat = 'charcoal', hat, hatColor, hair = '#2A211B', expr = 'neutral', pose = 'down', tie = '#7A3B33' } = {}) {
  const g = new THREE.Group(), fem = sex === 'f', S = mat(SK[skin]), C = mat(COAT[coat] || coat), dark = mat('#211A15', 0.6), shirt = mat('#E8E0CC');
  hat = hat || (fem ? 'cloche' : 'fedora'); const HC = mat(hatColor || new THREE.Color(COAT[coat] || coat).multiplyScalar(0.7).getStyle());
  // chân + giày
  for (const s of [-1, 1]) { if (!fem) add(g, new THREE.CapsuleGeometry(0.068, 0.5, 4, 12), mat(new THREE.Color(COAT[coat] || coat).multiplyScalar(0.62).getStyle()), s * 0.085, 0.36, 0);
    else add(g, new THREE.CapsuleGeometry(0.035, 0.14, 4, 10), S, s * 0.07, 0.14, 0);
    add(g, rbox(0.12, 0.08, 0.25, 0.035), dark, s * (fem ? 0.07 : 0.085), 0.04, 0.04); }
  if (fem) { add(g, lathe([[0.001, 0.1], [0.27, 0.1], [0.25, 0.4], [0.2, 0.78], [0.15, 0.98], [0.001, 0.98]]), mat(new THREE.Color(COAT[coat] || coat).multiplyScalar(0.85).getStyle()), 0, 0, 0).scale.set(1, 1, 0.78);   // váy dài
    add(g, lathe([[0.001, 0.9], [0.2, 0.9], [0.185, 1.08], [0.19, 1.3], [0.16, 1.38], [0.001, 1.4]]), C).scale.set(1, 1, 0.74); }                                                      // áo khoác lửng
  else { add(g, lathe([[0.001, 0.55], [0.235, 0.55], [0.205, 0.8], [0.18, 1.02], [0.205, 1.28], [0.2, 1.38], [0.13, 1.44], [0.001, 1.45]]), C).scale.set(1, 1, 0.72);            // áo khoác dài tới gối
    for (const s of [-1, 1]) add(g, rbox(0.03, 0.34, 0.03, 0.012), C, s * 0.05, 1.2, 0.145, 0, 0, s * 0.22);                                                                          // ve áo
    for (const y of [0.98, 0.86, 0.74]) for (const s of [-1, 1]) add(g, new THREE.SphereGeometry(0.012, 8, 6), dark, s * 0.045, y, 0.135); }
  add(g, new THREE.CylinderGeometry(0.06, 0.07, 0.06, 14), shirt, 0, 1.45, 0);                                                                                                         // cổ áo sơ mi
  if (!fem) { add(g, rbox(0.06, 0.06, 0.02, 0.01), shirt, 0, 1.4, 0.12); add(g, rbox(0.03, 0.2, 0.018, 0.008), mat(tie), 0, 1.33, 0.133, -0.12); }
  // tay (ống tay + bàn tay)
  const arms = { down: [[0.1, 0.03], [-0.1, -0.03]], clasp: [[0.55, 0.35], [0.55, -0.35]], pocket: [[0.12, 0.2], [-0.12, -0.2]] }[pose] || [[0.1, 0.03], [-0.1, -0.03]];
  for (const [i, s] of [[0, -1], [1, 1]]) { const [rx, rz] = arms[i], piv = new THREE.Group(); piv.position.set(s * (fem ? 0.2 : 0.235), 1.38, 0); piv.rotation.set(-rx, 0, s * 0.08 + rz); g.add(piv);
    add(piv, new THREE.CapsuleGeometry(0.055, 0.46, 4, 12), C, 0, -0.27, 0); add(piv, new THREE.SphereGeometry(0.048, 14, 10), S, 0, -0.56, 0); }
  // đầu: cổ, đầu trứng, tai, tóc, mặt
  add(g, new THREE.CylinderGeometry(0.045, 0.05, 0.1, 12), S, 0, 1.5, 0);
  const head = new THREE.Group(); head.position.set(0, 1.64, 0); g.add(head);
  add(head, new THREE.SphereGeometry(0.115, 28, 20), S).scale.set(0.92, 1.1, 0.98);
  for (const s of [-1, 1]) add(head, new THREE.SphereGeometry(0.026, 10, 8), S, s * 0.106, 0, -0.005).scale.set(0.6, 1, 1);
  add(head, new THREE.SphereGeometry(0.119, 24, 16, 0, Math.PI * 2, 0, Math.PI * (fem ? 0.62 : 0.45)), mat(hair, 0.9), 0, 0.012, -0.012).scale.set(0.93, 1.08, 0.99);
  if (fem) add(head, new THREE.SphereGeometry(0.05, 12, 10), mat(hair, 0.9), 0, -0.02, -0.105);
  const E = { neutral: [0, 0, 0], worried: [0.45, 0, -0.4], anxious: [0.55, 0.3, -0.1], sad: [0.35, 0, -0.9], relieved: [-0.15, 0, 0.8] }[expr] || [0, 0, 0], ink = mat('#17150F', 0.5);
  for (const s of [-1, 1]) { add(head, new THREE.SphereGeometry(0.017 + E[1] * 0.005, 10, 8), ink, s * 0.042, 0.012, 0.103).scale.set(1, 1.3, 0.6);                               // mắt
    add(head, rbox(0.052, 0.016, 0.012, 0.006), ink, s * 0.044, 0.054 + E[0] * 0.006, 0.104, 0, 0, s * -E[0] * 0.55); }                                                                 // lông mày (đầu trong nhướng = lo âu)
  add(head, new THREE.SphereGeometry(0.014, 10, 8), S, 0, -0.012, 0.118);                                                                                                            // mũi
  const mc = new THREE.QuadraticBezierCurve3(new THREE.Vector3(-0.028, -0.052, 0.104), new THREE.Vector3(0, -0.052 + E[2] * 0.024, 0.112), new THREE.Vector3(0.028, -0.052, 0.104));
  add(head, new THREE.TubeGeometry(mc, 12, 0.0065, 6), ink);                                                                                                                         // miệng
  if (hat === 'fedora') { const h = add(head, lathe([[0.001, 0.0], [0.205, 0.0], [0.21, 0.012], [0.12, 0.018], [0.118, 0.12], [0.09, 0.15], [0.03, 0.135], [0.001, 0.14]], 32), HC, 0, 0.065, -0.005);
    h.rotation.x = -0.06; add(head, new THREE.CylinderGeometry(0.121, 0.121, 0.03, 28, 1, true), mat('#17150F', 0.6), 0, 0.1, -0.008).rotation.x = -0.06; }
  else if (hat === 'cloche') add(head, lathe([[0.001, 0.16], [0.08, 0.155], [0.12, 0.12], [0.135, 0.06], [0.15, 0.0], [0.155, -0.012], [0.12, -0.006], [0.001, 0.0]], 32), HC, 0, 0.03, -0.01);
  return g;
}

// ---- nhà phố 1930 cùng chất (gạch sơn, cửa sổ lõm có khung kéo, phào, mái hiên sọc, biển chữ sơn)
function signTex(text) { const c = document.createElement('canvas'); c.width = 512; c.height = 128; const g = c.getContext('2d'); g.fillStyle = '#E6DCC4'; g.fillRect(0, 0, 512, 128);
  g.fillStyle = '#2A1E16'; g.font = '700 84px Georgia, serif'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, 256, 68); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
function stripeTex(a, b) { const c = document.createElement('canvas'); c.width = 256; c.height = 16; const g = c.getContext('2d'); for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? a : b; g.fillRect(i * 32, 0, 32, 16); } const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
function building({ w = 8, h = 13, d = 5, brick = '#8A5A44', sign = null, awning = null, seed = 1, fire = false } = {}) {
  const g = new THREE.Group(), r = (k) => hash(seed * 77 + k), trim = mat('#B8AC96'), glass = mat('#2A2E36', 0.35), lit = mat('#F0CC86', 0.6);
  add(g, rbox(w, h, d, 0.12), mat(brick, 0.9), 0, h / 2, -d / 2);
  add(g, rbox(w + 0.5, 0.45, d + 0.5, 0.1), mat('#6E6254'), 0, h - 0.2, -d / 2 + 0.05); add(g, rbox(w + 0.3, 0.18, 0.4, 0.06), trim, 0, h - 0.6, 0.12);
  const cols = Math.max(2, Math.round(w / 2.2)), rows = Math.floor((h - 4.5) / 2.2);
  for (let a = 0; a < rows; a++) for (let c = 0; c < cols; c++) { const x = -w / 2 + (c + 0.5) * w / cols, y = 5 + a * 2.2, L = r(a * 9 + c) < 0.28;
    add(g, rbox(0.9, 1.3, 0.12, 0.03), L ? lit : glass, x, y, -0.02); add(g, rbox(1.1, 0.12, 0.25, 0.04), trim, x, y - 0.72, 0.08); add(g, rbox(1.06, 0.14, 0.12, 0.04), trim, x, y + 0.72, 0.03);
    add(g, rbox(0.9, 0.05, 0.06, 0.02), trim, x, y, 0.06); add(g, rbox(0.05, 1.3, 0.06, 0.02), trim, x, y, 0.06);
    if (fire) { add(g, rbox(w * 0.9, 0.06, 0.8, 0.02), mat('#2A2F38', 0.5), 0, y - 0.95, 0.42); for (let k = 0; k < 10; k++) add(g, new THREE.CylinderGeometry(0.015, 0.015, 0.7, 6), mat('#2A2F38', 0.5), -w * 0.43 + k * w * 0.095, y - 0.6, 0.8); } }
  add(g, rbox(w, 0.35, 0.4, 0.08), mat('#5A4E44'), 0, 3.9, 0.12);
  add(g, rbox(w * 0.55, 2.4, 0.15, 0.05), glass, -w * 0.18, 1.6, 0.0); add(g, rbox(1.2, 2.7, 0.15, 0.05), mat('#5A4330'), w * 0.3, 1.35, 0.0);
  if (sign) { const s = new THREE.Mesh(new THREE.BoxGeometry(w * 0.7, 0.75, 0.12), [trim, trim, trim, trim, new THREE.MeshStandardMaterial({ map: signTex(sign), roughness: 0.8 }), trim]); s.position.set(0, 3.35, 0.1); s.castShadow = true; g.add(s); }
  if (awning) { const aw = new THREE.Mesh(new THREE.BoxGeometry(w * 0.9, 0.06, 1.3), new THREE.MeshStandardMaterial({ map: stripeTex(awning, '#E6DCC4'), roughness: 0.85 })); aw.position.set(0, 2.95, 0.65); aw.rotation.x = 0.35; aw.castShadow = true; g.add(aw); }
  return g;
}
function bank() {
  const g = new THREE.Group(), stone = mat('#CFC6B2'), stoneD = mat('#ADA491'), trim = mat('#DDD5C3');
  for (let i = 0; i < 4; i++) add(g, rbox(17.4 - i * 0.5, 0.25, 2.8 - i * 0.5, 0.06), i % 2 ? stone : stoneD, 0, 0.125 + i * 0.25, -i * 0.5);
  add(g, rbox(16, 10, 6, 0.15), stone, 0, 1.0 + 5, -4.4);
  for (let i = 0; i < 6; i++) { if (i === 2 || i === 3) continue; const x = -6.8 + i * 2.72; add(g, new THREE.CylinderGeometry(0.42, 0.46, 8.4, 24), trim, x, 1.0 + 4.4, -1.6);
    add(g, rbox(1.2, 0.3, 1.2, 0.06), stone, x, 1.15, -1.6); add(g, rbox(1.2, 0.3, 1.2, 0.06), stone, x, 9.7, -1.6); }
  add(g, rbox(17, 1.2, 2.6, 0.1), trim, 0, 10.4, -1.9);
  const sh = new THREE.Shape(); sh.moveTo(-8.6, 0); sh.lineTo(8.6, 0); sh.lineTo(0, 2.6); sh.closePath(); const ped = add(g, new THREE.ExtrudeGeometry(sh, { depth: 2.4, bevelEnabled: true, bevelSize: 0.08, bevelThickness: 0.08, bevelSegments: 2 }), trim, 0, 11.0, -3.1);
  const s = new THREE.Mesh(new THREE.BoxGeometry(6, 0.8, 0.1), [trim, trim, trim, trim, new THREE.MeshStandardMaterial({ map: signTex('B A N K'), roughness: 0.8 }), trim]); s.position.set(0, 10.4, -0.55); g.add(s);
  add(g, rbox(3.4, 4.6, 0.3, 0.05), mat('#2A2622'), 0, 1.0 + 2.3, -1.35); for (const x of [-0.8, 0.8]) add(g, rbox(1.5, 4.3, 0.18, 0.04), mat('#6B5236', 0.7), x, 1.0 + 2.15, -1.15);
  const cs = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.75, 0.04), [trim, trim, trim, trim, new THREE.MeshStandardMaterial({ map: (() => { const c = document.createElement('canvas'); c.width = 512; c.height = 200; const x = c.getContext('2d'); x.fillStyle = '#F2EAD6'; x.fillRect(0, 0, 512, 200); x.fillStyle = '#8E2B2B'; x.font = '800 120px Georgia, serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText('CLOSED', 256, 108); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; })(), roughness: 0.8 }), trim]);
  cs.position.set(0, 1.0 + 2.9, -1.0); cs.rotation.z = -0.05; g.add(cs);
  for (const x of [-4.4, 4.4]) add(g, rbox(1.1, 3.6, 0.2, 0.04), mat('#2A2E36', 0.35), x, 1.0 + 4.0, -1.35);
  return g;
}
function lamp() { const g = new THREE.Group(), iron = mat('#23272E', 0.5); add(g, new THREE.CylinderGeometry(0.07, 0.11, 4.2, 12), iron, 0, 2.1, 0); add(g, rbox(0.3, 0.12, 0.3, 0.04), iron, 0, 4.25, 0);
  const gl = add(g, new THREE.CylinderGeometry(0.2, 0.14, 0.5, 10), new THREE.MeshStandardMaterial({ color: '#F6D58E', emissive: new THREE.Color('#F2B441'), emissiveIntensity: 1.3 }), 0, 4.55, 0); gl.castShadow = false;
  add(g, new THREE.ConeGeometry(0.28, 0.22, 10), iron, 0, 4.92, 0); const L = new THREE.PointLight('#FFC97A', 26, 13, 1.3); L.position.y = 4.4; g.add(L); return g; }

// ---- hậu kỳ: độ sâu trường ảnh nông (tilt-shift) theo depth tuyến tính
function DOF(renderer, W, H) {
  const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType, samples: 4 }); rt.depthTexture = new THREE.DepthTexture(W, H); rt.depthTexture.type = THREE.UnsignedIntType;
  const q = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), new THREE.ShaderMaterial({ uniforms: { tC: { value: rt.texture }, tD: { value: rt.depthTexture }, near: { value: 0.1 }, far: { value: 300 }, focus: { value: 3 }, range: { value: 1.2 }, maxR: { value: 9 * H / 1080 }, res: { value: new THREE.Vector2(W, H) } },
    vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0., 1.); }',
    fragmentShader: `uniform sampler2D tC, tD; uniform float near, far, focus, range, maxR; uniform vec2 res; varying vec2 vUv;
      float lin(float z){ float n = z * 2. - 1.; return 2. * near * far / (far + near - n * (far - near)); }
      float coc(vec2 uv){ float d = lin(texture2D(tD, uv).x); return clamp(abs(d - focus) / (range * focus) , 0., 1.) * maxR; }
      void main(){ float c0 = coc(vUv); vec3 acc = vec3(0.); float wsum = 0.;
        for (int i = 0; i < 24; i++) { float a = float(i) * 2.39996; float r = sqrt(float(i) / 24.) * c0; vec2 o = vec2(cos(a), sin(a)) * r / res;
          float ci = coc(vUv + o); float w = smoothstep(0., 1., ci / max(c0, 0.001) + 0.2); acc += texture2D(tC, vUv + o).rgb * w; wsum += w; }
        vec3 col = acc / max(wsum, 0.001); vec2 v = vUv - .5; col *= 1. - 0.28 * smoothstep(.35, .85, length(v * vec2(1.2, 1.))); gl_FragColor = vec4(col, 1.);
        #include <colorspace_fragment>
      }` }));
  const qs = new THREE.Scene(); qs.add(q); const qc = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  return { u: q.material.uniforms, render(scene, cam) { q.material.uniforms.near.value = cam.near; q.material.uniforms.far.value = cam.far; renderer.setRenderTarget(rt); renderer.render(scene, cam); renderer.setRenderTarget(null); renderer.render(qs, qc); } };
}

export async function boot(res) {
  for (const f of ['700 48px Georgia', '800 48px Georgia', '600 48px Inter']) await document.fonts.load(f);
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: false, preserveDrawingBuffer: true }); renderer.setPixelRatio(1); renderer.setSize(W, H);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#3A4558'); scene.fog = new THREE.Fog('#3A4558', 30, 90);
  scene.add(new THREE.HemisphereLight('#B8C6DE', '#3A3026', 0.8));
  const key = new THREE.DirectionalLight('#CFDCF0', 2.0); key.position.set(-10, 16, 10); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
  Object.assign(key.shadow.camera, { left: -16, right: 16, top: 16, bottom: -10, near: 0.5, far: 70 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02; key.shadow.radius = 4; key.target.position.set(0, 0, -8); scene.add(key, key.target);
  const fill = new THREE.PointLight('#FFE2BA', 6, 10, 1.3); scene.add(fill);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(90, 50), mat('#6A645C', 0.95)); ground.rotation.x = -Math.PI / 2; ground.position.z = -8; ground.receiveShadow = true; scene.add(ground);
  const curb = add(scene, rbox(60, 0.18, 14, 0.05), mat('#7C766C', 0.95), 0, 0.09, -12);
  const SIGNS = [['LUNCH', '#8E3B33', '#8A5A44'], ['HATS', '#3E5A4A', '#7A5040'], [null, null, '#9C9282'], ['DRUGS', '#7A5A2E', '#86553F']];
  for (let i = 0; i < 4; i++) { const left = i < 2, [sign, aw, brick] = SIGNS[i]; const b = building({ w: 8.6, h: 13 + (i % 2) * 3, brick, sign, awning: aw, seed: i + 2, fire: i === 1 || i === 3 });
    b.position.set(left ? -21.5 + (i % 2) * 9.2 : 12.3 + (i % 2) * 9.2, 0.18, -19.5 - (i % 2) * 1.5); scene.add(b); }
  const B = bank(); B.position.set(-0.4, 0.18, -15.2); scene.add(B);
  for (const x of [-6.5, 7.5]) { const l = lamp(); l.position.set(x, 0.18, -5.6); scene.add(l); }
  // đám đông: tượng nhỏ quay lưng về ngân hàng (đa số), đa dạng da/áo/mũ
  const coats = Object.keys(COAT), skins = Object.keys(SK), hairs = ['#2A211B', '#4A3222', '#1A1612', '#6B4A2E', '#7A7470'];
  for (let i = 0; i < 46; i++) { const r = (k) => hash(i * 53 + k * 7 + 11), fem = r(1) < 0.38, row = Math.floor(i / 11.5), x = -7.5 + (i % 12) * 1.32 + (r(2) - 0.5) * 0.5, z = -13.2 + row * 1.9 + (r(3) - 0.5) * 0.6;
    const f = figurine({ sex: fem ? 'f' : 'm', skin: skins[Math.floor(r(4) * 5)], coat: fem ? ['plum', 'green', 'navy', 'brown'][Math.floor(r(5) * 4)] : coats[Math.floor(r(5) * 6)], hair: hairs[Math.floor(r(6) * 5)], expr: ['worried', 'sad', 'anxious'][Math.floor(r(7) * 3)], pose: r(8) < 0.3 ? 'pocket' : 'down' });
    f.position.set(x, 0.18, z); f.rotation.y = Math.PI + (r(9) - 0.5) * 0.9 + (r(10) < 0.15 ? Math.PI * 0.8 : 0); f.scale.setScalar(0.94 + r(11) * 0.12); scene.add(f); }
  const man = figurine({ sex: 'm', skin: 'light', coat: 'charcoal', expr: 'worried', pose: 'clasp' }); man.position.set(1.0, 0.18, -2.6); man.rotation.y = -0.35; scene.add(man);
  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 300), dof = DOF(renderer, W, H);
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  function frame(t) {
    const K1 = t < 1;
    if (K1) { cam.position.set(-0.2, 1.72, -0.4); cam.fov = 32; cam.lookAt(2.0, 1.62, -10); man.visible = true; dof.u.focus.value = 2.35; dof.u.range.value = 0.9; dof.u.maxR.value = 10 * H / 1080; }
    else { cam.position.set(1.2, 3.6, 8.5); cam.fov = 40; cam.lookAt(0.0, 4.6, -14); man.visible = false; dof.u.focus.value = 19.5; dof.u.range.value = 0.35; dof.u.maxR.value = 8 * H / 1080; }
    cam.updateProjectionMatrix(); fill.position.set(cam.position.x + 0.4, cam.position.y + 0.8, cam.position.z + 0.4);
    dof.render(scene, cam); ctx.drawImage(renderer.domElement, 0, 0);
    const s = W / 1920; ctx.save(); ctx.scale(s, s); const pill = (txt, x, y, px2, fg, bg, right) => { ctx.font = `600 ${px2}px Inter`; const pw = ctx.measureText(txt).width + px2 * 0.9, ph = px2 * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px2 * 0.45, y + ph / 2 + px2 * 0.04); };
    pill('December 1930', 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.75)'); pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.9)', true); ctx.restore();
    return { violations: [] };
  }
  return { canvas: out, frame };
}

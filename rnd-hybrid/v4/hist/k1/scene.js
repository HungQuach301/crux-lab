// R&D v4 · K1 chương lịch sử KHÔNG vẽ người (2b): ngân hàng đóng cửa 12/1930 bằng TƯ LIỆU.
// Ảnh LoC cph.3c17261 (RIGHTS §F6 X-RND-1; LoC ghi năm 1931) TOÀN KHUNG, như một bản in: chỉnh tông (đường cong + hai tông giấy ấm / bóng lạnh
// cùng grade 'dusk' của lớp ánh sáng), hạt tất định, viền giấy mảnh + bóng đổ trên nền tối. Chữ in (serif) = mốc có nguồn (v2/CLAIMS.md s06/N3).
// Không người minh hoạ, không dán gì lên ảnh. Chrome theo nhà máy (nguồn ảnh, nhãn ARCHIVE PHOTO, "US only · history, not a forecast").
import * as THREE from 'three';
import { Stage, Camera, fonts, C } from '/toolkit/factory/world/core.js';

const PHOTO = '/rnd-hybrid/work/external/bank1931_crop.jpg';   // 1920×1080 cắt từ TIFF gốc (SHA-256 trong RIGHTS)
export async function boot(res) {
  await fonts();
  const st = Stage(res), O = st.O, renderer = st.renderer, scene = new THREE.Scene(); scene.background = new THREE.Color('#0D0C0C');
  const CAM = Camera({ p: { pos: [0, 0, 10], tgt: [0, 0, 0], fov: 30, chart: 0 } }, []);
  const H = 2 * 10 * Math.tan(15 * Math.PI / 180), W = H * 16 / 9;    // khung nhìn ở z = 0
  const tex = await new THREE.TextureLoader().loadAsync(PHOTO); tex.colorSpace = THREE.SRGBColorSpace;
  const k = 0.84, pw = W * k, ph = pw * 1080 / 1920;                   // bản in chiếm 84 % bề ngang
  const photo = new THREE.Mesh(new THREE.PlaneGeometry(pw, ph), new THREE.ShaderMaterial({
    uniforms: { map: { value: tex }, warm: { value: new THREE.Color('#F1E6D0') }, cool: { value: new THREE.Color('#1A1E24') } },
    vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
    fragmentShader: `uniform sampler2D map; uniform vec3 warm, cool; varying vec2 vUv;
      float h(vec2 p){ p = fract(p * vec2(443.897, 441.423)); p += dot(p, p.yx + 19.19); return fract((p.x + p.y) * p.x); }
      void main(){
        vec3 c = texture2D(map, vUv).rgb; float l = dot(c, vec3(0.2126, 0.7152, 0.0722));
        l = smoothstep(0.03, 0.97, l); l = mix(l, l * l * (3.0 - 2.0 * l), 0.35);          // đường cong: đen sâu hơn, sáng cuộn mềm
        vec3 o = mix(cool, warm, l);                                                          // hai tông in: bóng lạnh, giấy ấm
        vec2 q = vUv - 0.5; o *= 1.0 - 0.28 * smoothstep(0.25, 0.75, length(q * vec2(1.4, 1.0)));
        vec2 px = floor(vUv * vec2(1920.0, 1080.0)); o += 0.035 * (h(px) + h(px + 7.0) - 1.0) * (0.3 + l * (1.0 - l) * 3.0);
        gl_FragColor = vec4(o, 1.0); }`, toneMapped: false }));
  const edge = new THREE.Mesh(new THREE.PlaneGeometry(pw + 0.09, ph + 0.09), new THREE.MeshBasicMaterial({ color: '#E3D8C2', toneMapped: false })); edge.position.z = -0.01;
  const sh = new THREE.Mesh(new THREE.PlaneGeometry(pw + 0.5, ph + 0.5), new THREE.MeshBasicMaterial({ color: '#000000', transparent: true, opacity: 0.55, toneMapped: false })); sh.position.set(0.08, -0.1, -0.02);
  const g = new THREE.Group(); g.add(sh, edge, photo); g.position.y = 0.12; scene.add(g);
  function frame(t) {
    const pose = CAM.apply(t), cam = CAM.cam;
    g.scale.setScalar(1 + 0.012 * t);                                  // đẩy chậm (Ken Burns 1,2 %/s) — trong ảnh tĩnh chỉ là cỡ
    renderer.render(scene, cam);
    const log = O.begin(t, pose.chart, cam), c = O.ctx;
    // chữ in: dải giấy tối dưới bản in, serif; mốc = claim s06 (N3: "on December 11 … Bank of United States, ceased operations")
    c.save(); c.fillStyle = 'rgba(13,12,12,0.86)'; c.fillRect(150, 742, 1010, 196);
    c.fillStyle = '#E9DFC9'; c.font = '600 40px "DejaVu Serif", Georgia, serif'; c.fillText('NEW YORK · DECEMBER 11, 1930', 186, 802);
    c.font = '700 64px "DejaVu Serif", Georgia, serif'; c.fillText('Bank of United States', 186, 876);
    c.font = '400 40px "DejaVu Serif", Georgia, serif'; c.fillText('ceases operations', 186, 922); c.restore();
    O.chrome({ src: 'Photo: Library of Congress (NYWT&S), 1931', hist: true });
    O.text('ARCHIVE PHOTO', 1800, 108, 54, { kind: 'chrome', color: '#1B1F26', plate: C.chrome, plateA: 0.95, align: 'right' });
    st.compose(); log.camMoving = false; return log;
  }
  return { canvas: st.out, frame };
}

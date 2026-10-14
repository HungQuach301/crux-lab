// R&D vòng 3 · H4: HẬU KỲ TOÀN KHUNG thống nhất (áp cho người, vật, nhà như nhau):
//   lượt 1 màu (vật liệu toon 4 bậc) → RT màu + depthTexture; lượt 2 pháp tuyến (overrideMaterial MeshNormalMaterial) → RT pháp tuyến;
//   ghép: nét mực Sobel theo depth tuyến tính + pháp tuyến · bán sắc chấm xoay 45° ở vùng tối · vân giấy (hash tất định) · viền tối nhẹ.
import * as THREE from 'three';

export function Post(renderer, W, H, { ink = '#15171C', paper = '#F2EAD6', dot = 7, lineW = 2.0 } = {}) {
  const mk = (depth) => { const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType });
    if (depth) { rt.depthTexture = new THREE.DepthTexture(W, H); rt.depthTexture.type = THREE.UnsignedIntType; } return rt; };
  const rtC = mk(true), rtN = mk(true), nmat = new THREE.MeshNormalMaterial();
  const quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), new THREE.ShaderMaterial({
    uniforms: { tC: { value: rtC.texture }, tN: { value: rtN.texture }, tD: { value: rtC.depthTexture }, near: { value: 0.1 }, far: { value: 400 },
      res: { value: new THREE.Vector2(W, H) }, ink: { value: new THREE.Color(ink) }, paper: { value: new THREE.Color(paper) }, cell: { value: dot * H / 1080 },
      lw: { value: lineW * H / 1080 }, dots: { value: 0.55 }, grain: { value: 0.07 }, vig: { value: 0.35 } },
    vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0., 1.); }',
    fragmentShader: `
      uniform sampler2D tC, tN, tD; uniform float near, far, cell, lw, dots, grain, vig; uniform vec2 res; uniform vec3 ink, paper; varying vec2 vUv;
      float lin(float z){ float n = z * 2. - 1.; return 2. * near * far / (far + near - n * (far - near)); }
      float D(vec2 o){ return lin(texture2D(tD, vUv + o / res).x); }
      vec3 N(vec2 o){ return texture2D(tN, vUv + o / res).xyz * 2. - 1.; }
      float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
      void main(){
        vec3 c = texture2D(tC, vUv).rgb; float d0 = D(vec2(0.));
        // nét: sai khác depth tương đối (bóng ngoài) + sai khác pháp tuyến (nếp gấp, mép khối)
        float e = 0.; vec3 n0 = N(vec2(0.));
        for (int i = 0; i < 4; i++) { vec2 o = (i == 0 ? vec2(1., 0.) : i == 1 ? vec2(-1., 0.) : i == 2 ? vec2(0., 1.) : vec2(0., -1.)) * lw;
          float dd = abs(D(o) - d0) / max(d0, 0.5); e = max(e, smoothstep(0.006, 0.02, dd));
          e = max(e, smoothstep(0.2, 0.45, 1. - dot(n0, N(o)))); }
        e *= 1. - smoothstep(60., 140., d0);                       // xa: nét nhạt (sương)
        // bán sắc: lưới xoay 45°, bán kính theo độ tối
        float L = dot(c, vec3(.299, .587, .114)); vec2 p = gl_FragCoord.xy; mat2 R = mat2(.7071, -.7071, .7071, .7071); vec2 q = R * p / cell;
        vec2 f = fract(q) - .5; float r = sqrt(max(0., .55 - L) / .55) * .62; float ht = (1. - smoothstep(r - .08, r + .08, length(f))) * step(0.001, r);
        c = mix(c, c * .45, ht * dots);
        // vân giấy: hạt + sợi ngang tất định
        float g = (h(floor(p)) - .5) * grain + (h(vec2(floor(p.y / 3.), 7.)) - .5) * grain * .6;
        c = c * (1. + g); c = mix(c, c * paper, .18);
        c = mix(c, ink, e * .92);
        vec2 v = vUv - .5; c *= 1. - vig * smoothstep(.35, .85, length(v * vec2(1.2, 1.)));
        gl_FragColor = vec4(c, 1.);
        #include <colorspace_fragment>
      }` }));
  quad.frustumCulled = false; const qs = new THREE.Scene(); qs.add(quad); const qc = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  return {
    uniforms: quad.material.uniforms,
    render(scene, cam) {
      quad.material.uniforms.near.value = cam.near; quad.material.uniforms.far.value = cam.far;
      renderer.setRenderTarget(rtC); renderer.render(scene, cam);
      const bg = scene.background, fog = scene.fog; scene.overrideMaterial = nmat; scene.background = new THREE.Color(0.5, 0.5, 1); scene.fog = null;
      renderer.setRenderTarget(rtN); renderer.render(scene, cam);
      scene.overrideMaterial = null; scene.background = bg; scene.fog = fog;
      renderer.setRenderTarget(null); renderer.render(qs, qc);
    },
  };
}

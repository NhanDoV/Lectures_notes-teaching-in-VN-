const canvas = document.getElementById("heartCanvas");
const ctx = canvas.getContext("2d");
const chartType = document.getElementById("chartType");
const slidersDiv = document.getElementById("sliders");

const W = canvas.width;
const H = canvas.height;

ctx.lineCap = "round";
ctx.lineJoin = "round";

/* ===================== STATE ===================== */

let currentParams = {};
let targetParams = {};
let animating = false;

/* ===================== UTILS ===================== */

const lerp = (a, b, t) => a + (b - a) * t;

function smoothParams() {
  let done = true;
  for (let k in targetParams) {
    if (!(k in currentParams)) currentParams[k] = targetParams[k];
    currentParams[k] = lerp(currentParams[k], targetParams[k], 0.15);
    if (Math.abs(currentParams[k] - targetParams[k]) > 1e-3) done = false;
  }
  return done;
}

/* ===================== HEART POINTS ===================== */

function heartPoints(type, p) {
  const pts = [];
  const n = Math.floor(p.n_pat || 400);
  const eps = p.epsilon || 1e-6;
  const deg = p.n_deg || 3;

  switch (type) {

    case "1":
      for (let i = 0; i < n; i++) {
        const t = -1 + 2 * i / (n - 1);
        pts.push({
          x: Math.sin(t) * Math.cos(t) * Math.log(Math.abs(t) + eps),
          y: Math.sqrt(Math.abs(t)) * Math.cos(t)
        });
      }
      break;

    case "2":
      sampleImplicit(
        (x, y) => (x*x + y*y - 1)**3 - x*x*y*y*y,
        -1.3, 1.3, -1.2, 1.3, n / 4, pts
      );
      break;

    case "3":
      sampleImplicit(
        (x, y) => x*x + 2*(0.6*Math.cbrt(x*x) - y)**2 - 1,
        -1.2, 1.2, -0.9, 1.2, n / 4, pts
      );
      break;

    case "4":
      for (let i = 0; i < n; i++) {
        const t = 60 * i / (n - 1);
        const r = 0.01 * (-t*t + 40*t + 1200);
        pts.push({ x: -r*Math.sin(Math.PI*t/180), y: r*Math.cos(Math.PI*t/180) });
        pts.push({ x:  r*Math.sin(Math.PI*t/180), y: r*Math.cos(Math.PI*t/180) });
      }
      break;

    case "5":
      for (let i = 0; i < n; i++) {
        const t1 = -Math.PI + Math.PI/2 * i / (n - 1);
        const t2 =  Math.PI/2 + Math.PI/2 * i / (n - 1);
        const r1 = Math.sin(t1)**7 * Math.exp(2*Math.abs(t1));
        const r2 = Math.sin(t2)**7 * Math.exp(2*Math.abs(t2));
        pts.push({ x: r1*Math.cos(t1), y: r1*Math.sin(t1) });
        pts.push({ x: r2*Math.cos(t2), y: r2*Math.sin(t2) });
      }
      break;

    case "6":
      const s = (deg + 5) / 3;
      sampleImplicit(
        (x, y) => x*x + (y - Math.sqrt(Math.abs(x)))**2 - deg,
        -s, s, -s*0.3, s*1.2, n / 4, pts
      );
      break;
  }

  return pts;
}

/* ===================== IMPLICIT SAMPLER ===================== */

function sampleImplicit(F, xmin, xmax, ymin, ymax, n, pts) {
  const dx = (xmax - xmin) / n;
  const dy = (ymax - ymin) / n;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const x = xmin + i * dx;
      const y = ymin + j * dy;
      if (F(x, y) * F(x + dx, y) < 0) pts.push({ x, y });
      if (F(x, y) * F(x, y + dy) < 0) pts.push({ x, y });
    }
  }
}

/* ===================== AUTO FIT ===================== */

function computeTransform(pts) {
  let minX = Infinity, maxX = -Infinity;
  let minY = Infinity, maxY = -Infinity;

  pts.forEach(p => {
    minX = Math.min(minX, p.x);
    maxX = Math.max(maxX, p.x);
    minY = Math.min(minY, p.y);
    maxY = Math.max(maxY, p.y);
  });

  const scale = 0.69 * Math.min(W / (maxX - minX), H / (maxY - minY));

  return {
    scale,
    tx: W / 2 - scale * (minX + maxX) / 2,
    ty: H / 2 + scale * (minY + maxY) / 2
  };
}

/* ===================== DRAW ===================== */

function drawPoints(pts) {
  const T = computeTransform(pts);
  ctx.setTransform(1,0,0,1,0,0);
  ctx.clearRect(0,0,W,H);

  ctx.translate(T.tx, T.ty);
  ctx.scale(T.scale, -T.scale);

  ctx.beginPath();
  pts.forEach((p,i)=> i ? ctx.lineTo(p.x,p.y) : ctx.moveTo(p.x,p.y));

  ctx.strokeStyle = "#ff4d6d";
  ctx.lineWidth = 1 / T.scale;
  ctx.stroke();
}

/* ===================== ANIMATION ===================== */

function animate() {
  if (!animating) return;
  const done = smoothParams();
  drawPoints(heartPoints(chartType.value, currentParams));
  if (!done) requestAnimationFrame(animate);
  else animating = false;
}

/* ===================== SLIDERS ===================== */

const sliderConfigs = {
  1: [
    { name: "n_pat", min: 50, max: 800, step: 10, value: 320 },
    { name: "epsilon", min: 1e-3, max: 0.1, step: 5e-4, value: 2e-3 }
  ],
  2: [{ name: "n_pat", min: 200, max: 800, step: 50, value: 400 }],
  3: [{ name: "n_pat", min: 200, max: 800, step: 50, value: 400 }],
  4: [{ name: "n_pat", min: 10, max: 200, step: 10, value: 140 }],
  5: [{ name: "n_pat", min: 100, max: 800, step: 50, value: 400 }],
  6: [
    { name: "n_deg", min: 1, max: 8, step: 1, value: 3 },
    { name: "n_pat", min: 200, max: 800, step: 50, value: 400 }
  ]
};

function updateSliders(type) {
  slidersDiv.innerHTML = "";
  currentParams = {};
  targetParams = {};

  (sliderConfigs[type] || []).forEach(cfg => {
    const wrap = document.createElement("div");
    wrap.className = "slider-container";

    const label = document.createElement("label");
    label.innerHTML = `
      <span class="param-name">${cfg.name}</span>
      <span class="param-value">${cfg.value}</span>
    `;

    const input = document.createElement("input");
    Object.assign(input, cfg);
    input.type = "range";

    input.oninput = () => {
      targetParams[cfg.name] = parseFloat(input.value);
      label.innerHTML = `
        <span class="param-name">${cfg.name}</span>
        <span class="param-value">${input.value}</span>
      `;
      if (!animating) {
        animating = true;
        requestAnimationFrame(animate);
      }
    };

    wrap.append(label, input);
    slidersDiv.appendChild(wrap);

    currentParams[cfg.name] = cfg.value;
    targetParams[cfg.name] = cfg.value;
  });

  drawPoints(heartPoints(type, currentParams));
}

/* ===================== INIT ===================== */

chartType.onchange = () => updateSliders(chartType.value);
updateSliders(chartType.value);
const wheel = document.getElementById("wheel");
const result = document.getElementById("result");
const btn = document.getElementById("center-button");

const segments = [
  "Lucky",
  "Fortune",
  "Wealth",
  "Success",
  "Prosperity",
  "Luck & Love",
  "Victory",
  "Joy",
  "Energy"
];

const colors = [
  "#b45309", // gold
  "#991b1b", // casino red
  "#065f46", // dark green
];

const degPerSlice = 360 / segments.length;

let currentRotation = 0;
let isSpinning = false;

// ----- create slices ------
segments.forEach((text, i) => {
  const slice = document.createElement("div");
  slice.className = "slice";

  slice.style.borderTopColor = colors[i % colors.length];
  slice.style.transform = `translate(-50%, -50%) rotate(${i * degPerSlice}deg)`;

  const label = document.createElement("div");
  label.className = "slice-text";
  label.textContent = text;

  slice.appendChild(label);
  wheel.appendChild(slice);
});

// ----- spin ------
btn.onclick = () => {
  if (isSpinning) return; // chặn spam click
  isSpinning = true;

  const extraSpin = 360 * 10 + Math.floor(Math.random() * 360);
  currentRotation += extraSpin;

  wheel.style.transform = `rotate(${currentRotation}deg)`;

  const normalizedDeg = currentRotation % 360;
  let index = Math.floor(normalizedDeg / degPerSlice);
  index = (segments.length - index - 1 + segments.length) % segments.length;

  setTimeout(() => {
    result.textContent = segments[index];
    isSpinning = false;
  }, 4200);
};
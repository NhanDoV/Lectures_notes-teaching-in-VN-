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

const colors = ["#60BA97", "#f1573fff"];
const degPerSlice = 360 / segments.length;

// ----- create slices ------
segments.forEach((text, i) => {
    const slice = document.createElement("div");
    slice.className = "slice";

    slice.style.borderTopColor = colors[i % 2];
    slice.style.transform = `translate(-50%, -50%) rotate(${i * degPerSlice}deg)`;

    const label = document.createElement("div");
    label.className = "slice-text";
    label.textContent = text;

    slice.appendChild(label);
    wheel.appendChild(slice);
});

// ----- spin ------
btn.onclick = () => {
    const spin = 3600 + Math.floor(Math.random() * 360);
    wheel.style.transform = `rotate(${spin}deg)`;

    let index = Math.floor(((spin % 360) / degPerSlice));
    index = (segments.length - index - 1 + segments.length) % segments.length;

    setTimeout(() => {
        result.textContent = segments[index];
    }, 4200);
};
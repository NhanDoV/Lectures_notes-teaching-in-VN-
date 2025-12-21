const thu = 5902500;
const chi = 10000000;
const mucTieu = 100000000;

const names = [
  "Anloz-Must",
  "Bill-Git",
  "Barack-Banana",
  "David-Solomon",
  "Athena Foonish"
];

// ===== RANDOM TOP DONATE =====
const maxTopTotal = thu * 0.8; // 80% tổng thu

// random tổng tiền cho top (50% → 80%)
const topTotal = Math.floor(
  maxTopTotal * (0.5 + Math.random() * 0.5)
);

// random trọng số
let weights = names.map(() => Math.random());
const weightSum = weights.reduce((a, b) => a + b, 0);

// phân bổ tiền theo trọng số
const topDonate = names.map((name, i) => ({
  name,
  amount: Math.floor((weights[i] / weightSum) * topTotal)
}));

// ===== FORMAT =====
function formatMoney(num) {
  return num.toLocaleString("vi-VN") + " đ";
}

// ===== SET STATS =====
document.getElementById("total").innerText = formatMoney(thu);
document.getElementById("thu").innerText = formatMoney(thu);
document.getElementById("conlai").innerText = formatMoney(thu - chi);

// ===== PROGRESS =====
const percent = Math.min((thu / mucTieu) * 100, 100);
document.getElementById("progressBar").style.width = percent + "%";

// ===== RENDER TOP DONATE =====
const topList = document.getElementById("topList");
topList.innerHTML = "";

topDonate
  .sort((a, b) => b.amount - a.amount)
  .forEach((user, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <span class="rank">#${index + 1}</span>
      <span>${user.name}</span>
      <span>${formatMoney(user.amount)}</span>
    `;
    topList.appendChild(li);
  });

// ===== DEBUG (optional) =====
console.log("Top 5 total:", topDonate.reduce((s, u) => s + u.amount, 0));
console.log("80% thu:", maxTopTotal);
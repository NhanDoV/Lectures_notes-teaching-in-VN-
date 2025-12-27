const ball = document.getElementById("ball");
const btn = document.getElementById("triggerBtn");
const resultBox = document.getElementById("result");
const tube = document.querySelector(".tube");

const tubeHeight = tube.clientHeight;
const ballSize = ball.clientHeight;
const maxY = tubeHeight - ballSize;

function findNearestKey(value, keys) {
  return keys.reduce((prev, curr) => {
    return Math.abs(curr - value) < Math.abs(prev - value)
      ? curr
      : prev;
  });
}

function formatTextForBox(text, maxChars = 60, wordsPerLine = 3) {
  // Nếu text ngắn, giữ nguyên
  if (text.length <= maxChars) return text;

  // Tách thành mảng từ
  const words = text.split(" ");
  const lines = [];
  
  for (let i = 0; i < words.length; i += wordsPerLine) {
    // Lấy cụm 3 từ (hoặc ít hơn nếu cuối text)
    const line = words.slice(i, i + wordsPerLine).join(" ");
    lines.push(line);
  }

  // Join lại với \n
  return lines.join("\n");
}

// dict map
const dictmap = {
  1: "ĐỊT CON ĐĨ MẸ THẰNG TÔ LÂM TÀU",
  2: "LỒN BÀ GIÀ THĂNG TÔ LÂM TÀU CHÓ",
  3: "中國 婊子 貓 (CHINESE FUCKING BITCH)",
  4: "LŨ MẶT LỒN TRUNG CẨU",
  5: "習近平 - TẬP CẠP BUỒI",
  6: "習近平 - Xi Jinping THE BITCH",
  7: "毛泽东 - CON HEO KHOÁI TÁP LỒN ĐĨ TÀU",
  8: "毛泽东 - MẠO VẶT LÔNG",
  9: "ĐỊT MẸ NGƯỜI HÁN, LŨ CHÓ TÀU CÚT",
  10: "LÀNG ĐỔN TÔ LÂM LỒN MẶT CẶC ÓC LOZ",
  11: "ĐỊT MẸ VIN VƯỢN THẰNG LOZ MAFIA",
  12: "BAISE VINFAST putain VIN VƯỢN",
  13: "ĐỊT MẸ ĐỜ CỜ SỜ TQ",
  14: "FICKEN VINFAST",
  15: "FOLLAR VINFAST",
  16: "Fille chinoise baise GROSSE CHATTE",
  17: "Une bonne baise, BELLES FILLES CHINOIS",
  18: "Хороший трах, КРАСИВЫЕ КИТАЙСКИЕ ДЕВУШКИ",
  19: "Nice fuck, BEAUTIFUL CHINESE GIRLS",
  20: "ナイスファック、美しい雌犬の中国人の女の子たち",
  21: "好他妈的，美丽的婊子中国女孩",
  22: "你的阴户太大而且太糟糕了；中国女孩",
  23: "ta chatte est trop grosse et mauvaise ; fille chinoise",
  24: "你個陰太大而且太差喇；中國女仔",
  25: "ཁྱེད་ཀྱི་ཆུ་བོ་དེ་ཧ་ཅང་ཆེ་ཞིང་ངན་པ་རེད། རྒྱ་རིགས་བུ་མོ།",
  30: "CHÚC LŨ CHÓ TÀU VẠN KIẾP SÚC SANH",
  31: "CON ĐĨ MẸ THẰNG TÔ LÂM ĂN CỨC BÒ",
  32: "THỤT NÁT LỒN BÀ GIÀ THẰNG TÔ LÂM",
  33: "TÔ LÂM LIẾM CỨT TẬP CẠP BUỒI",
  35: "NGUYỀN RỦA HÁN TỘC VÀ ĐÁM HÁN NÔ",
  40: "DƯ LUẬN VIÊN CHÓ ĐẺ",
  42: "TÔ LÂM MẶT LỒN ÓC CẶC",
  45: "LŨ BÒ ĐỎ ÓC CẶC",
  49: "GIA TỘC ĐĨ LỒN TÔ LÂM HÁN NÔ VẠN KIẾP LÀM SÚC SINH",
  50: "共產主義黨的婊子 (COMMUNIST BITCH)",
  55: "ĐẶNG TIỂU ĐƯỜNG - TẬP CẠP BUỒI - CẶP ĐÔI CHÓ LIẾM",
  60: "讓日本做得更多，至少在北京屠殺 1000 起南京大屠殺",
  65: "ĐÁM KHÁCH DU LỊCH TÀU LỒN",
  70: "LŨ CHÓ TRUNG QUỐC MẶT LỒN",
  75: "ĐỊT MẸ LŨ TÀU LỒN",
  76: "ĐỊT VÔ BANH NÃO THẰNG TÔ LÂM",
  77: "THẰNG HÁN NÔ TÔ LÂM ĐĨ LỒN",
  80: "HỠI ĐÁM CHÓ TÀU, CHÚNG BÂY SẮP CHẾT MẸ RỒI",
  81: "THÔNG CHẾT BÀ MẸ THẰNG TÔ LÂM",
  90: "CHINESE FUCKING",
  99: "ĐỊT MẸ ĐỜ CỜ SỜ TÀU +",
  100: "vạn sự khởi đều ngu =)))"
};

const availableKeys = Object.keys(dictmap).map(Number);

// helper delay
const sleep = (ms) => new Promise(res => setTimeout(res, ms));

// TAB SYSTEM
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const targetTab = btn.dataset.tab;
    
    // Remove active from all
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    
    // Add active to clicked
    btn.classList.add('active');
    document.getElementById(targetTab).classList.add('active');
  });
});

// GAME LAUNCH FUNCTION
async function launch() {
  btn.disabled = true;
  resultBox.textContent = "";
  
  // random số vòng chạy (2–5)
  const randomLoop = Math.floor(Math.random() * 4) + 2;
  // random giá trị cuối (1–100)
  const randomValue = Math.floor(Math.random() * 100) + 1;
  
  // animation speed
  ball.style.transition = "top 0.35s ease-in-out";
  
  // chạy full cây lên xuống
  for (let i = 0; i < randomLoop; i++) {
    ball.style.top = `${maxY}px`;
    await sleep(350);
    ball.style.top = `0px`;
    await sleep(350);
  }
  
  // dừng ở vị trí cuối
  const finalY = (randomValue / 100) * maxY;
  ball.style.top = `${finalY}px`;
  await sleep(400);
  
  // mapping value
  const nearestKey = findNearestKey(randomValue, availableKeys);
  let output = dictmap[nearestKey];

  output = formatTextForBox(output);  
  resultBox.textContent = output;
  
  console.log({
    loop: randomLoop,
    value: randomValue
  });
  
  btn.disabled = false;
}

btn.addEventListener("click", launch);

// ================= TAB 2 – LUCKY SPIN =================
const wheel = document.getElementById("wheel");
const spinResult = document.getElementById("spin-result");
const spinBtn = document.getElementById("center-button");

if (wheel && spinBtn) {
  const segments = [
    "Óc lồn TôLâm",
    "Chó tàu chó đẻ",
    "Địt mẹ tung hoa",
    "Chinese suck",
    "Fuck chinese",
    "Chinese bitch",
    "Trung quốc đầu cặc",
    "TôLâmLồn",
    "Tàu chó"
  ];

  const colors = ["#b45309", "#991b1b", "#065f46"];
  const degPerSlice = 360 / segments.length;

  let currentRotation = 0;
  let isSpinning = false;

  // create slices
if (wheel.children.length === 0) {
  segments.forEach((text, i) => {
    const slice = document.createElement("div");
    slice.className = "slice";
    slice.style.borderTopColor = colors[i % colors.length];
    slice.style.transform = `translate(-50%, -50%) rotate(${i * degPerSlice - 0.3}deg)`;

    const label = document.createElement("div");
    label.className = "slice-text";
    label.textContent = text;

    slice.appendChild(label);
    wheel.appendChild(slice);
  });
}

  // spin
  spinBtn.onclick = () => {
    if (isSpinning) return;
    isSpinning = true;
    spinResult.textContent = "";

    const extraSpin = 360 * 10 + Math.floor(Math.random() * 360);
    currentRotation += extraSpin;

    wheel.style.transform = `rotate(${currentRotation}deg)`;

    const normalizedDeg = (currentRotation + 90) % 360;
    let index = Math.floor(normalizedDeg / degPerSlice);
    index = (segments.length - index - 1) % segments.length;

    setTimeout(() => {
      spinResult.textContent = segments[index];
      isSpinning = false;
    }, 4200);
  };
}
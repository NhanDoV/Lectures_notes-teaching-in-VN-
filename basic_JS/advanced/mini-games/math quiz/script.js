const quizData = {
    0: { // Đạo hàm & Tích phân
        name: "📉 Đạo hàm & Tích phân",
        questions: [
            {
                question: "Đạo hàm của hàm số f(x) = x³ - 3x² + 1 là gì?",
                image: "images/img1.png",
                options: [ "A. 3x² - 6x", "B. x² - 6x", "C. 3x² - 3x", "D. x³ - 6x"],
                correct: 0
            },
            {
                question: "Tích phân ∫₀¹ 2x dx bằng bao nhiêu?",
                image: null,
                options: ["A. 1", "B. 2", "C. 1/2", "D. 0"],
                correct: 0
            },
            {
                question: "Đạo hàm của hàm số f(x) = 5x² là:",
                image: null,
                options: ["A. 5x", "B. 10x", "C. x²", "D. 25x"],
                correct: 1
            },
            {
                question: "Đạo hàm của hàm số f(x) = sin x là:",
                image: null,
                options: ["A. cos x", "B. −cos x", "C. sin x", "D. −sin x"],
                correct: 0
            },
            {
                question: "Nguyên hàm của hàm số f(x) = 3x² là:",
                image: null,
                options: ["A. x³ + C", "B. 6x + C", "C. x² + C", "D. 3x³ + C"],
                correct: 0
            },
            {
                question: "Tích phân ∫ 1 dx bằng:",
                image: null,
                options: ["A. 0", "B. 1", "C. x + C", "D. x² + C"],
                correct: 2
            },
            {
                question: "Đạo hàm của hàm số f(x) = e^x là:",
                image: null,
                options: ["A. xe^x", "B. e^x", "C. e", "D. x^e"],
                correct: 1
            },
            {
                question: "Tích phân ∫₀² x dx bằng:",
                image: null,
                options: ["A. 2", "B. 4", "C. 1", "D. 0"],
                correct: 0
            },
            {
                question: "Đạo hàm của hàm số f(x) = ln x là:",
                image: null,
                options: ["A. ln x", "B. 1/x", "C. x", "D. e^x"],
                correct: 1
            },
            {
                question: "Nguyên hàm của hàm số f(x) = 2x là:",
                image: null,
                options: [ "A. x² + C", "B. 2x² + C", "C. x + C", "D. 2x + C"],
                correct: 0
            }
        ]
    },

    1: { // Mệnh đề - Tập hợp - Logic
        name: "🧠 Mệnh đề - Tập hợp - Logic",
        questions: [
            {
                question: "Phủ định của mệnh đề “∀x ∈ ℝ, x² ≥ 0” là gì?",
                image: null,
                options: ["A. ∀x ∈ ℝ, x² < 0", "B. ∃x ∈ ℝ, x² < 0", "C. ∃x ∈ ℝ, x² ≥ 0", "D. ∀x ∈ ℝ, x² = 0"],
                correct: 1
            },
            {
                question: "Mệnh đề nào sau đây là mệnh đề đúng?",
                image: null,
                options: ["A. ∀x ∈ ℝ, x² < 0", "B. ∃x ∈ ℝ, x² = −1", "C. ∀x ∈ ℝ, x² ≥ 0", "D. ∃x ∈ ℝ, x² < 0"],
                correct: 2
            },
            {
                question: "Phủ định của mệnh đề “x > 3” là:",
                image: null,
                options: ["A. x ≥ 3", "B. x < 3", "C. x ≤ 3", "D. x = 3"],
                correct: 2
            },
            {
                question: "Cho A = {1,2,3}, B = {2,3,4}. Khi đó A ∩ B là:",
                image: null,
                options: ["A. {1,4}", "B. {2,3}", "C. {1,2,3,4}", "D. ∅"],
                correct: 1
            },
            {
                question: "Cho A = {1,2}, B = {2,3}. Khi đó A ∪ B là:",
                image: null,
                options: ["A. {2}", "B. {1,2,3}", "C. {1,3}", "D. ∅"],
                correct: 1
            },
            {
                question: "Mệnh đề “Nếu a > b thì a² > b²” là:",
                image: null,
                options: ["A. Luôn đúng", "B. Luôn sai", "C. Đúng với mọi a,b ∈ ℝ", "D. Sai với một số a,b"],
                correct: 3
            },
            {
                question: "Phát biểu nào là mệnh đề?",
                image: null,
                options: ["A. Bạn ăn cơm chưa?", "B. Học toán khó quá!", "C. 2 + 3 = 5", "D. Hãy học bài"],
                correct: 2
            },
            {
                question: "Cho mệnh đề P: “x > 2”. Tập nghiệm của P là:",
                image: null,
                options: ["A. (−∞, 2)", "B. (2, +∞)", "C. [2, +∞)", "D. (−∞, +∞)"],
                correct: 1
            },
            {
                question: "Cho A ⊂ B. Mệnh đề nào sau đây đúng?",
                image: null,
                options: ["A. A = B", "B. A ⊃ B", "C. A ⊆ B", "D. B ⊆ A"],
                correct: 2
            },
            {
                question: "Phủ định của mệnh đề “∃x ∈ ℝ, x² = 4” là:",
                image: null,
                options: ["A. ∀x ∈ ℝ, x² ≠ 4", "B. ∀x ∈ ℝ, x² = 4", "C. ∃x ∈ ℝ, x² ≠ 4", "D. x² ≠ 4"],
                correct: 0
            }
        ]
    },

    2: { // Hình học phẳng
        name: "📐 Hình học phẳng",
        questions: [
            {
                question: "Trong tam giác đều cạnh a, diện tích bằng bao nhiêu?",
                image: null,
                options: ["A. a²√3 / 2", "B. a²√3 / 4", "C. a² / 2", "D. a²"],
                correct: 1
            },
            {
                question: "Tổng ba góc trong một tam giác bằng:",
                image: null,
                options: ["A. 90°", "B. 180°", "C. 270°", "D. 360°"],
                correct: 1
            },
            {
                question: "Trong tam giác vuông, cạnh huyền là:",
                image: null,
                options: ["A. Cạnh lớn nhất", "B. Cạnh nhỏ nhất", 
                          "C. Cạnh đối góc nhọn", "D. Cạnh bất kỳ"],
                correct: 0
            },
            {
                question: "Đường trung tuyến của tam giác là đoạn thẳng:",
                image: null,
                options: ["A. Nối hai đỉnh", "B. Nối trung điểm hai cạnh", 
                          "C. Từ đỉnh đến trung điểm cạnh đối diện", "D. Từ đỉnh vuông góc cạnh đối diện"],
                correct: 2
            },
            {
                question: "Một hình chữ nhật có chiều dài 5 và chiều rộng 3. Diện tích bằng:",
                image: null,
                options: ["A. 8", "B. 15", "C. 16", "D. 30"],
                correct: 1
            },
            {
                question: "Bán kính đường tròn ngoại tiếp tam giác đều cạnh a là:",
                image: null,
                options: ["A. a√3 / 6", "B. a√3 / 3", "C. a / 2", "D. a√2 / 2"],
                correct: 1
            },
            {
                question: "Hình thoi có hai đường chéo:",
                image: null,
                options: ["A. Song song", "B. Bằng nhau", "C. Vuông góc với nhau", 
                           "D. Cắt nhau tại trung điểm nhưng không vuông góc"],
                correct: 2
            },
            {
                question: "Chu vi hình tròn bán kính R là:",
                image: null,
                options: ["A. πR²", "B. 2πR", "C. πR", "D. 4πR"],
                correct: 1
            },
            {
                question: "Diện tích hình tròn bán kính R là:",
                image: null,
                options: ["A. 2πR", "B. πR", "C. πR²", "D. R²"],
                correct: 2
            },
            {
                question: "Trong tam giác cân, hai cạnh bên:",
                image: null,
                options: ["A. Vuông góc nhau", "B. Bằng nhau", "C. Song song", "D. Không bằng nhau"],
                correct: 1
            }
        ]
    },

    3: { // Hình học không gian
        name: "📦 Hình học không gian",
        questions: [
            {
                question: "Thể tích khối lập phương cạnh a là:",
                image: null,
                options: ["A. a²", "B. 4a³", "C. a³", "D. 6a²"],
                correct: 2
            },
            {
                question: "Diện tích toàn phần của khối lập phương cạnh a là:",
                image: null,
                options: ["A. a²", "B. 4a²", "C. 6a²", "D. a³"],
                correct: 2
            },
            {
                question: "Thể tích khối hộp chữ nhật có các kích thước a, b, c là:",
                image: null,
                options: ["A. abc", "B. 2abc", "C. ab + bc + ca", "D. a + b + c"],
                correct: 0
            },
            {
                question: "Một hình chóp có đáy là hình vuông cạnh a, chiều cao h. Thể tích bằng:",
                image: null,
                options: ["A. a²h", "B. a²h/2", "C. a²h/3", "D. 2a²h/3"],
                correct: 2
            },
            {
                question: "Khối cầu bán kính R có thể tích là:",
                image: null,
                options: ["A. 4πR²", "B. (4/3)πR³", "C. πR²", "D. (1/3)πR³"],
                correct: 1
            },
            {
                question: "Diện tích mặt cầu bán kính R là:",
                image: null,
                options: ["A. πR²", "B. 2πR²", "C. 4πR²", "D. (4/3)πR³"],
                correct: 2
            },
            {
                question: "Khối trụ có bán kính đáy R và chiều cao h có thể tích là:",
                image: null,
                options: ["A. πR²h", "B. 2πRh", "C. πRh", "D. 2πR²h"],
                correct: 0
            },
            {
                question: "Diện tích xung quanh của khối trụ bán kính R, chiều cao h là:",
                image: null,
                options: ["A. πR²h", "B. 2πRh", "C. πRh²", "D. 4πRh"],
                correct: 1
            },
            {
                question: "Khối nón có bán kính đáy R, chiều cao h có thể tích là:",
                image: null,
                options: ["A. πR²h", "B. (1/2)πR²h", "C. (1/3)πR²h", "D. (2/3)πR²h"],
                correct: 2
            },
            {
                question: "Đường sinh của hình nón là:",
                image: null,
                options: ["A. Bán kính đáy", "B. Chiều cao", "C. Cạnh bên", "D. Đường kính đáy"],
                correct: 2
            }
        ]
    },

    4: { // Bất phương trình & Bất đẳng thức
        name: "⚖️ Bất phương trình & Bất đẳng thức",
        questions: [
            {
                question: "Nghiệm của bất phương trình x − 3 > 0 là:",
                image: null,
                options: ["A. x > 3", "B. x < 3", "C. x ≥ 3", "D. x ≤ 3"],
                correct: 0
            },
            {
                question: "Tập nghiệm của bất phương trình 2x ≤ 4 là:",
                image: null,
                options: ["A. x ≤ 2", "B. x < 2", "C. x ≥ 2", "D. x > 2"],
                correct: 0
            },
            {
                question: "Giải bất phương trình x + 5 ≥ 1 ta được:",
                image: null,
                options: ["A. x ≥ 6", "B. x ≥ −4", "C. x > −4", "D. x ≤ −4"],
                correct: 1
            },
            {
                question: "Tập nghiệm của bất phương trình −x > 2 là:",
                image: null,
                options: ["A. x > −2", "B. x < −2", "C. x ≥ −2", "D. x ≤ −2"],
                correct: 1
            },
            {
                question: "Bất phương trình nào sau đây luôn đúng với mọi x ∈ ℝ?",
                image: null,
                options: ["A. x² ≥ 0", "B. x² < 0", "C. x > 0", "D. x < 0"],
                correct: 0
            },
            {
                question: "Giải bất phương trình 3x − 6 < 0 ta được:",
                image: null,
                options: ["A. x < 2", "B. x > 2", "C. x ≤ 2", "D. x ≥ 2"],
                correct: 0
            },
            {
                question: "Tập nghiệm của bất phương trình |x| ≤ 3 là:",
                image: null,
                options: ["A. x ≥ 3", "B. x ≤ −3", "C. −3 ≤ x ≤ 3", "D. x ≤ 3"],
                correct: 2
            },
            {
                question: "Bất phương trình |x| > 2 tương đương với:",
                image: null,
                options: ["A. −2 < x < 2", "B. x ≥ 2", "C. x ≤ −2 hoặc x ≥ 2", "D. x ≤ 2"],
                correct: 2
            },
            {
                question: "Cho a > b > 0. Bất đẳng thức nào sau đây đúng?",
                image: null,
                options: ["A. a² < b²", "B. a² = b²", "C. a² > b²", "D. a < b"],
                correct: 2
            },
            {
                question: "Giải bất phương trình x/2 ≥ 1 ta được:",
                image: null,
                options: ["A. x ≥ 1", "B. x ≥ 2", "C. x > 2", "D. x ≤ 2"],
                correct: 1
            }
        ]
    },

    5: { // Hàm số - PT - HPT
        name: "📊 Hàm số – Phương trình – Hệ",
        questions: [
            {
                question: "Hàm số y = x² là hàm:",
                image: null,
                options: ["A. Hàm lẻ", "B. Hàm chẵn", "C. Không chẵn không lẻ", "D. Hàm tuần hoàn"],
                correct: 1
            },
            {
                question: "Tập xác định của hàm số y = 1/x là:",
                image: null,
                options: ["A. ℝ", "B. ℝ+", "C. ℝ \\ {0}", "D. ℝ−"],
                correct: 2
            },
            {
                question: "Nghiệm của phương trình x + 3 = 0 là:",
                image: null,
                options: ["A. 3", "B. −3", "C. 0", "D. 1"],
                correct: 1
            },
            {
                question: "Phương trình x² = 4 có nghiệm là:",
                image: null,
                options: ["A. x = 2", "B. x = −2", "C. x = 0", "D. x = ±2"],
                correct: 3
            },
            {
                question: "Hàm số y = 2x + 1 là hàm:",
                image: null,
                options: ["A. Bậc nhất", "B. Bậc hai", "C. Bậc ba", "D. Hằng"],
                correct: 0
            },
            {
                question: "Đồ thị hàm số y = x² là:",
                image: null,
                options: ["A. Đường thẳng", "B. Parabol", "C. Hình tròn", "D. Hyperbol"],
                correct: 1
            },
            {
                question: "Hệ phương trình có nghiệm duy nhất khi:",
                image: null,
                options: ["A. Hai đường thẳng song song", "B. Hai đường thẳng cắt nhau", "C. Hai đường trùng nhau", "D. Không có nghiệm"],
                correct: 1
            },
            {
                question: "Nghiệm của phương trình 2x − 4 = 0 là:",
                image: null,
                options: ["A. −2", "B. 0", "C. 2", "D. 4"],
                correct: 2
            },
            {
                question: "Hàm số y = ax + b (a ≠ 0) đồng biến khi:",
                image: null,
                options: ["A. a = 0", "B. a > 0", "C. a < 0", "D. b > 0"],
                correct: 1
            },
            {
                question: "Phương trình nào sau đây là phương trình bậc hai?",
                image: null,
                options: ["A. x + 1 = 0", "B. x² − 3x + 2 = 0", "C. 2x − 1 = 0", "D. x³ = 1"],
                correct: 1
            }
        ]
    },

    6: { // Lượng giác
        name: "📐 Lượng giác & Quỹ tích",
        questions: [
            {
                question: "Giá trị của sin²x + cos²x bằng:",
                image: null,
                options: ["A. 0", "B. 1", "C. 2", "D. Phụ thuộc x"],
                correct: 1
            },
            {
                question: "Giá trị của sin 0° bằng:",
                image: null,
                options: ["A. 0", "B. 1", "C. −1", "D. 1/2"],
                correct: 0
            },
            {
                question: "Giá trị của cos 0° bằng:",
                image: null,
                options: ["A. 0", "B. 1", "C. −1", "D. 1/2"],
                correct: 1
            },
            {
                question: "Giá trị của tan 45° bằng:",
                image: null,
                options: ["A. 0", "B. 1", "C. √2", "D. 1/2"],
                correct: 1
            },
            {
                question: "Công thức đúng là:",
                image: null,
                options: ["A. 1 + tan²x = cos²x", "B. sin²x − cos²x = 1", "C. 1 + tan²x = 1 / cos²x", "D. sin²x + cos²x = 0"],
                correct: 2
            },
            {
                question: "Giá trị của cos 60° bằng:",
                image: null,
                options: ["A. 1", "B. √3/2", "C. 1/2", "D. 0"],
                correct: 2
            },
            {
                question: "Giá trị của sin 30° bằng:",
                image: null,
                options: ["A. 1", "B. √3/2", "C. 1/2", "D. 0"],
                correct: 2
            },
            {
                question: "Giá trị của tan 0° là:",
                image: null,
                options: ["A. 1", "B. 0", "C. −1", "D. Không xác định"],
                correct: 1
            },
            {
                question: "Giá trị của cos 180° bằng:",
                image: null,
                options: ["A. 1", "B. 0", "C. −1", "D. 1/2"],
                correct: 2
            },
            {
                question: "Phương trình sin x = 0 có nghiệm là:",
                image: null,
                options: ["A. x = kπ", "B. x = π/2 + kπ", "C. x = π + kπ", "D. x = 2πk + π/2"],
                correct: 0
            }
        ]
    },

    7: { // Số học & Dãy số
        name: "🔢 Số học – Dãy số – CSC & CSN",
        questions: [
            {
                question: "Dãy số 2, 4, 6, 8, ... là:",
                image: null,
                options: [
                    "A. Cấp số nhân",
                    "B. Dãy ngẫu nhiên",
                    "C. Cấp số cộng",
                    "D. Không phải dãy số"
                ],
                correct: 2
            }
        ]
    },

    8: { // Xác suất
        name: "🎲 Xác suất & Thống kê",
        questions: [
            {
                question: "Gieo một con xúc xắc đều. Xác suất ra mặt số 6 là:",
                image: null,
                options: [
                    "A. 1/2",
                    "B. 1/3",
                    "C. 1/6",
                    "D. 1/12"
                ],
                correct: 2
            }
        ]
    },

    9: { // Tổ hợp
        name: "🧮 Tổ hợp – Chỉnh hợp – Hoán vị",
        questions: [
            {
                question: "Số hoán vị của 3 phần tử là:",
                image: null,
                options: [
                    "A. 3",
                    "B. 6",
                    "C. 9",
                    "D. 12"
                ],
                correct: 1
            }
        ]
    },

    10: { // Số phức
        name: "💠 Số phức",
        questions: [
            {
                question: "Cho z = 3 + 4i. Môđun |z| bằng:",
                image: null,
                options: [
                    "A. 5",
                    "B. 7",
                    "C. 1",
                    "D. √7"
                ],
                correct: 0
            }
        ]
    },

    11: { // Vector
        name: "🧭 Vector & Tọa độ",
        questions: [
            {
                question: "Độ dài vector (3, 4) bằng:",
                image: null,
                options: [
                    "A. 5",
                    "B. 7",
                    "C. √7",
                    "D. 25"
                ],
                correct: 0
            }
        ]
    }
};

let currentSet = -1;
let currentQuestion = 0;
let score = 0;
let answered = false;

const screens = {
    menu: document.getElementById('menu-screen'),
    game: document.getElementById('game-screen'),
    end: document.getElementById('end-screen')
};

document.querySelectorAll('.set-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        currentSet = parseInt(btn.dataset.set);
        startQuiz();
    });
});

function startQuiz() {
    currentQuestion = 0;
    score = 0;
    screens.menu.classList.remove('active');
    screens.game.classList.add('active');
    showQuestion();
}

function showQuestion() {
    const quiz = quizData[currentSet];
    const q = quiz.questions[currentQuestion];
    
    document.getElementById('set-name').textContent = quiz.name;
    const total = quiz.questions.length;
    document.getElementById('question-progress').textContent =
        `Câu ${currentQuestion + 1}/${total}`;

    document.getElementById('score').textContent = score;
    
    const imgDiv = document.getElementById('question-image');
    if (q.image) {
        imgDiv.innerHTML = `<img src="${q.image}" alt="Hình câu hỏi">`;
    } else {
        imgDiv.innerHTML = '❓';
    }
    
    document.getElementById('question-text').textContent = q.question;
    
    const optionsDiv = document.getElementById('options');
    optionsDiv.innerHTML = '';
    q.options.forEach((option, index) => {
        const btn = document.createElement('div');
        btn.className = 'option';
        btn.textContent = option;
        btn.dataset.index = index;
        btn.addEventListener('click', () => selectOption(index, q.correct));
        optionsDiv.appendChild(btn);
    });
    
    document.getElementById('next-btn').style.display = 'none';
    answered = false;
}

function selectOption(selected, correct) {
    if (answered) return;
    
    answered = true;
    const options = document.querySelectorAll('.option');
    
    options.forEach((opt, index) => {
        if (index === correct) {
            opt.classList.add('correct');
        } else if (index === selected && selected !== correct) {
            opt.classList.add('incorrect');
        }
        
        opt.style.pointerEvents = 'none';
    });
    
    if (selected === correct) {
        score++;
        document.getElementById('score').textContent = score;
    }
    
    setTimeout(() => {
        document.getElementById('next-btn').style.display = 'block';
    }, 1000);
}

document.getElementById('next-btn').addEventListener('click', nextQuestion);

function nextQuestion() {
    currentQuestion++;
    const total = quizData[currentSet].questions.length;

    if (currentQuestion < total) {
        showQuestion();
    } else {
        endQuiz();
    }
}

function endQuiz() {
    screens.game.classList.remove('active');
    screens.end.classList.add('active');
    
    const total = quizData[currentSet].questions.length;
    const percentage = Math.round((score / total) * 100);

    document.getElementById('final-score').textContent =
        `${score}/${total} (${percentage}%)`;
    
    let message = '';
    if (percentage === 100) {
        message = '👑 Xuất sắc! Bạn là thiên tài!';
    } else if (percentage >= 70) {
        message = '👍 Rất tốt! Giỏi lắm!';
    } else if (percentage >= 40) {
        message = '👌 Khá ổn! Cố lên nhé!';
    } else {
        message = '😅 Chơi lại để cải thiện nào!';
    }
    
    document.getElementById('final-title').textContent = percentage === 100 ? '🏆 CHÚC MỪNG!' : '🎉 Hoàn Thành!';
    document.getElementById('final-message').textContent = message;
}

document.getElementById('restart-btn').addEventListener('click', () => {
    screens.end.classList.remove('active');
    screens.menu.classList.add('active');
    currentSet = -1;
});
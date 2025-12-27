const board = document.getElementById("board");
const statusText = document.getElementById("status");
const p1Score = document.getElementById("p1-score");
const p2Score = document.getElementById("p2-score");
const p2NameEl = document.getElementById("p2-name");
const resetBtn = document.getElementById("reset");
const modePicker = document.getElementById("modePicker");

const SIZE = 15;
const COLORS = ["#a8d8ea","#aa96da","#fcbad3","#ffffd2","#b8f2e6","#ffd6a5"];

let grid = [];
let currentPlayer = 1;
let playerColor = {1:null, 2:null};

// ---------- INIT ----------
function createBoard() {
    board.innerHTML = "";
    grid = [];

    for (let i=0;i<SIZE*SIZE;i++){
        const cell = document.createElement("div");
        cell.className="cell";
        const color=randomColor();
        cell.style.background=color;
        cell.dataset.color=color;
        cell.dataset.owner="0";

        // click only if Human Player 2
        cell.addEventListener("click", () => {
            if (currentPlayer === 2 && modePicker.value === "human") playerMove(color);
            if (currentPlayer === 1) playerMove(color);
        });

        grid.push(cell);
        board.appendChild(cell);
    }

    claimCell(0,1);
    claimCell(SIZE*SIZE-1,2);

    playerColor[1]=grid[0].dataset.color;
    playerColor[2]=grid[SIZE*SIZE-1].dataset.color;

    currentPlayer=1;
    updateScores();
    updateStatus();
}

resetBtn.onclick=createBoard;

// ---------- UTILS ----------
function randomColor(){ return COLORS[Math.floor(Math.random()*COLORS.length)]; }

function getPlayerName(player){
    if(player === 1) return "You";
    if(player === 2) return modePicker.value === "human" ? "Player 2" : "Computer";
}

function updateStatus(){
    statusText.textContent=`${getPlayerName(currentPlayer)}'s turn`;
    p2NameEl.textContent = getPlayerName(2);
}

// ---------- FLOOD FILL ----------
function floodFill(player){
    const owned = grid.map((c,i)=>c.dataset.owner===String(player)?i:-1).filter(i=>i!==-1);
    const targetColor = playerColor[player];
    const visited = new Set(owned);
    const queue=[...owned];

    while(queue.length){
        const idx=queue.shift();
        grid[idx].style.background=targetColor;
        grid[idx].dataset.color=targetColor;

        neighbors(idx).forEach(n=>{
            if(!visited.has(n) && grid[n].dataset.owner==="0" && grid[n].dataset.color===targetColor){
                claimCell(n,player);
                visited.add(n);
                queue.push(n);
            }
        });
    }
}

function simulateFlood(player,color){
    const owned = grid.map((c,i)=>c.dataset.owner===String(player)?i:-1).filter(i=>i!==-1);
    const visited = new Set(owned);
    const queue=[...owned];
    let gain=0;

    while(queue.length){
        const idx=queue.shift();
        neighbors(idx).forEach(n=>{
            if(!visited.has(n) && grid[n].dataset.owner==="0" && grid[n].dataset.color===color){
                visited.add(n);
                queue.push(n);
                gain++;
            }
        });
    }
    return gain;
}

function neighbors(i){
    const n=[]; const x=i%SIZE; const y=Math.floor(i/SIZE);
    if(x>0) n.push(i-1);
    if(x<SIZE-1) n.push(i+1);
    if(y>0) n.push(i-SIZE);
    if(y<SIZE-1) n.push(i+SIZE);
    return n;
}

function claimCell(i,player){
    grid[i].dataset.owner=player;
    grid[i].classList.add(player===1?"p1":"p2");
}

// ---------- GAME ----------
function playerMove(color){
    if(color===playerColor[currentPlayer]) return;
    playerColor[currentPlayer]=color;
    floodFill(currentPlayer);
    updateScores();

    // next turn
    currentPlayer= currentPlayer===1 ? 2 : 1;
    updateStatus();

    if(currentPlayer===2 && modePicker.value==="computer"){
        setTimeout(aiMove,400);
    }
}

function aiMove(){
    let bestColor=null; let bestGain=-1;
    COLORS.forEach(color=>{
        if(color===playerColor[2]) return;
        const gain=simulateFlood(2,color);
        if(gain>bestGain){ bestGain=gain; bestColor=color; }
    });

    playerColor[2]=bestColor;
    floodFill(2);

    currentPlayer=1;
    updateScores();
    updateStatus();
}

function updateScores(){
    const total=SIZE*SIZE;
    const p1=grid.filter(c=>c.dataset.owner==="1").length;
    const p2=grid.filter(c=>c.dataset.owner==="2").length;
    p1Score.textContent=Math.round((p1/total)*100);
    p2Score.textContent=Math.round((p2/total)*100);
}

// ---------- START ----------
createBoard();
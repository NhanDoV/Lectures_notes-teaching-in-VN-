const board = document.getElementById('board');
const status = document.getElementById('status');
const resetBtn = document.getElementById('reset');
const gameModeSelect = document.getElementById('gameMode');

let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;
let gameMode = 'human';
let isComputerThinking = false;

const winningConditions = [
    [0,1,2], [3,4,5], [6,7,8], // rows
    [0,3,6], [1,4,7], [2,5,8], // columns
    [0,4,8], [2,4,6] // diagonals
];

gameModeSelect.addEventListener('change', (e) => {
    gameMode = e.target.value;
    resetGame();
});

function createBoard() {
    board.innerHTML = '';
    gameBoard.forEach((_, index) => {
        const cell = document.createElement('button');
        cell.classList.add('cell');
        cell.dataset.index = index;
        cell.addEventListener('click', handleCellClick);
        board.appendChild(cell);
    });
}

function handleCellClick(e) {
    const index = parseInt(e.target.dataset.index);
    if (
        gameBoard[index] !== '' ||
        !gameActive ||
        isComputerThinking ||
        (gameMode === 'computer' && currentPlayer === 'O')
    ) return;

    makeMove(index, currentPlayer);

    if (!gameActive) return;

    // Computer play
    if (gameMode === 'computer' && currentPlayer === 'O') {
        setTimeout(computerMove, 500);
    }
}

function makeMove(index, player) {
    gameBoard[index] = player;
    const cell = board.children[index];
    cell.textContent = player;
    cell.classList.add(player.toLowerCase());
    cell.disabled = true;

    if (checkWin(player)) {
        status.textContent = `${player} wins!`;
        gameActive = false;
        return;
    }

    if (gameBoard.every(cell => cell !== '')) {
        status.textContent = 'Draw!';
        gameActive = false;
        return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    status.textContent = `${currentPlayer === 'X' ? "Player" : "Computer"} ${currentPlayer}'s turn`;
}

function computerMove() {
    if (!gameActive || currentPlayer !== 'O') return;
    
    isComputerThinking = true;
    status.textContent = "Computer thinking...";
    
    const bestMove = getBestMove();
    makeMove(bestMove, 'O');
    
    isComputerThinking = false;
}

// Minimax Algorithm for unbeatable AI
function getBestMove() {
    let bestScore = -Infinity;
    let move;
    
    for (let i = 0; i < 9; i++) {
        if (gameBoard[i] === '') {
            gameBoard[i] = 'O';
            let score = minimax(gameBoard, 0, false);
            gameBoard[i] = '';
            
            if (score > bestScore) {
                bestScore = score;
                move = i;
            }
        }
    }
    return move;
}

function minimax(board, depth, isMaximizing) {
    const result = checkResult();
    
    if (result !== null) {
        return result === 'O' ? 10 - depth : result === 'X' ? depth - 10 : 0;
    }
    
    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'O';
                let score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'X';
                let score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

function checkWin(player) {
    return winningConditions.some(condition => {
        return condition.every(index => gameBoard[index] === player);
    });
}

function checkResult() {
    for (let player of ['X', 'O']) {
        if (checkWin(player)) return player;
    }
    if (gameBoard.every(cell => cell !== '')) return 'draw';
    return null;
}

function resetGame() {
    currentPlayer = 'X';
    gameBoard = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    isComputerThinking = false;
    status.textContent = "Player X's turn";
    createBoard();
}

resetBtn.addEventListener('click', resetGame);
createBoard();
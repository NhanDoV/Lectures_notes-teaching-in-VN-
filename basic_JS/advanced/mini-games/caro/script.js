class CaroGame {
    constructor() {
        this.dimension = 15;
        this.squares = [];
        this.currentPlayer = 'X';

        this.playerColor = 'black';
        this.opponentColor = 'white';

        this.singlePlayerMode = false;
        this.gameActive = false;
        this.winner = null;

        this.winningLine = [];
        this.warningLine = [];

        this.init();
    }

    init() {
        this.bindEvents();
    }

    bindEvents() {
        document.getElementById('board-size').addEventListener('change', e => {
            this.dimension = parseInt(e.target.value);
        });

        document.getElementById('play-mode').addEventListener('change', e => {
            this.singlePlayerMode = e.target.value === 'computer';
        });

        document.getElementById('symbol-color').addEventListener('change', e => {
            this.playerColor = e.target.value;
            this.opponentColor = this.playerColor === 'black' ? 'white' : 'black';
        });

        document.getElementById('symbol-type').addEventListener('change', e => {
            this.currentPlayer = e.target.value;
        });

        document.getElementById('start-game').addEventListener('click', () => this.startGame());
        document.getElementById('restart-btn').addEventListener('click', () => this.restartGame());
        document.getElementById('new-game-btn').addEventListener('click', () => this.newGame());
        document.getElementById('back-btn').addEventListener('click', () => this.backToOptions());
    }

    startGame() {
        this.newGame();
        document.getElementById('options-panel').classList.add('hide');
        document.getElementById('game-container').classList.remove('hide');
    }

    newGame() {
        this.dimension = parseInt(document.getElementById('board-size').value);
        this.singlePlayerMode = document.getElementById('play-mode').value === 'computer';

        this.playerColor = document.getElementById('symbol-color').value;
        this.opponentColor = this.playerColor === 'black' ? 'white' : 'black';

        this.currentPlayer = document.getElementById('symbol-type').value;

        this.squares = Array.from({ length: this.dimension }, () =>
            Array(this.dimension).fill(null)
        );

        this.gameActive = true;
        this.winner = null;
        this.winningLine = [];
        this.warningLine = [];

        this.renderBoard();
        this.updateStatus();

        if (this.singlePlayerMode && this.currentPlayer !== 'X') {
            setTimeout(() => this.makeComputerMove(), 300);
        }
    }

    restartGame() {
        this.newGame();
    }

    backToOptions() {
        document.getElementById('game-container').classList.add('hide');
        document.getElementById('options-panel').classList.remove('hide');
        this.gameActive = false;
        this.squares = [];
        this.winner = null;
        this.winningLine = [];
        this.warningLine = [];
        document.getElementById('board').innerHTML = '';
        document.getElementById('status').textContent = '';
    }

    renderBoard() {
        const board = document.getElementById('board');
        board.innerHTML = '';
        board.style.gridTemplateColumns = `repeat(${this.dimension}, 1fr)`;

        const playerSymbol = document.getElementById('symbol-type').value;

        for (let r = 0; r < this.dimension; r++) {
            for (let c = 0; c < this.dimension; c++) {
                const sq = document.createElement('button');
                sq.className = 'square';

                const val = this.squares[r][c];
                if (val) {
                    const isPlayer = val === playerSymbol;
                    const color = isPlayer ? this.playerColor : this.opponentColor;
                    sq.textContent = val;
                    sq.classList.add(`${val.toLowerCase()}-${color}`);
                }

                if (this.winningLine.some(p => p[0] === r && p[1] === c)) {
                    sq.classList.add('winning');
                }

                if (this.warningLine.some(p => p[0] === r && p[1] === c)) {
                    sq.classList.add('warning');
                }

                sq.onclick = () => this.handleClick(r, c);
                board.appendChild(sq);
            }
        }
    }

    handleClick(row, col) {
        if (!this.gameActive || this.squares[row][col]) return;

        this.makeMove(row, col, this.currentPlayer);
        if (!this.gameActive) return;

        this.switchPlayer();
        this.updateStatus();

        if (this.singlePlayerMode && this.gameActive) {
            setTimeout(() => {
                this.makeComputerMove();
                if (this.gameActive) {
                    this.switchPlayer();
                    this.updateStatus();
                }
            }, 300);
        }
    }

    makeMove(row, col, player) {
        this.squares[row][col] = player;

        const result = this.checkWin(row, col, player);

        if (result.win) {
            this.gameActive = false;
            this.winner = player;
            this.winningLine = result.line;
        } else if (result.bounded) {
            this.warningLine = result.line;
        } else {
            this.warningLine = [];
        }

        this.renderBoard();
        this.updateStatus();
    }

    switchPlayer() {
        this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
    }

    updateStatus() {
        const status = document.getElementById('status');
        const playerSymbol = document.getElementById('symbol-type').value;

        if (this.winner) {
            status.textContent =
                this.winner === playerSymbol ? '🎉 You win!' :
                (this.singlePlayerMode ? '🤖 Computer wins!' : 'Opponent wins!');
        } else if (this.warningLine.length) {
            status.textContent = '⚠️ 5 in a row blocked at both ends!';
        } else {
            if (this.singlePlayerMode) {
                status.textContent = this.currentPlayer === playerSymbol
                    ? 'Your turn'
                    : 'Computer\'s turn';
            } else {
                status.textContent = this.currentPlayer === playerSymbol
                    ? 'Your turn'
                    : 'Opponent\'s turn';
            }
        }
    }

    // ===== WIN CHECK =====
    checkWin(row, col, player) {
        const dirs = [
            [0, 1],
            [1, 0],
            [1, 1],
            [1, -1]
        ];

        for (const [dx, dy] of dirs) {
            let line = [[row, col]];
            let blocks = 0;

            let r = row + dx, c = col + dy;
            while (this.squares[r]?.[c] === player) {
                line.push([r, c]);
                r += dx; c += dy;
            }
            if (this.squares[r]?.[c]) blocks++;

            r = row - dx; c = col - dy;
            while (this.squares[r]?.[c] === player) {
                line.unshift([r, c]);
                r -= dx; c -= dy;
            }
            if (this.squares[r]?.[c]) blocks++;

            if (line.length >= 5) {
                if (blocks < 2) return { win: true, bounded: false, line };
                return { win: false, bounded: true, line };
            }
        }
        return { win: false, bounded: false, line: [] };
    }

    // ===== AI =====
    makeComputerMove() {
        if (!this.gameActive) return;
        const [r, c] = this.findBestMove();
        this.makeMove(r, c, this.currentPlayer);
    }

    findBestMove() {
        let bestScore = -Infinity;
        let bestMove = null;

        const opp = this.currentPlayer === 'X' ? 'O' : 'X';

        for (let r = 0; r < this.dimension; r++) {
            for (let c = 0; c < this.dimension; c++) {
                if (!this.squares[r][c] && this.hasNeighbor(r, c)) {
                    const attack = this.evaluateMove(r, c, this.currentPlayer);
                    const defense = this.evaluateMove(r, c, opp) * 0.9;
                    const score = Math.max(attack, defense);

                    if (score > bestScore) {
                        bestScore = score;
                        bestMove = [r, c];
                    }
                }
            }
        }

        if (bestMove) return bestMove;

        const mid = Math.floor(this.dimension / 2);
        return [mid, mid];
    }

    evaluateMove(row, col, player) {
        const dirs = [
            [0, 1], [1, 0], [1, 1], [1, -1]
        ];
        let score = 0;

        for (const [dx, dy] of dirs) {
            let count = 1;
            let openEnds = 0;

            let r = row + dx, c = col + dy;
            while (this.squares[r]?.[c] === player) {
                count++; r += dx; c += dy;
            }
            if (this.squares[r]?.[c] === null) openEnds++;

            r = row - dx; c = col - dy;
            while (this.squares[r]?.[c] === player) {
                count++; r -= dx; c -= dy;
            }
            if (this.squares[r]?.[c] === null) openEnds++;

            score += this.scorePattern(count, openEnds);
        }
        return score;
    }

    scorePattern(count, openEnds) {
        if (count >= 5) return 100000;
        if (count === 4 && openEnds === 2) return 10000;
        if (count === 4 && openEnds === 1) return 5000;
        if (count === 3 && openEnds === 2) return 1000;
        if (count === 3 && openEnds === 1) return 200;
        if (count === 2 && openEnds === 2) return 100;
        return 10;
    }

    hasNeighbor(r, c) {
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                if (this.squares[r + dr]?.[c + dc]) return true;
            }
        }
        return false;
    }
}

const game = new CaroGame();
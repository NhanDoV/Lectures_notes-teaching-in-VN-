class Game2048 {
    constructor() {
        this.board = Array(4).fill().map(() => Array(4).fill(0));
        this.score = 0;
        this.bestScore = localStorage.getItem('best2048') || 0;
        this.gameWon = false;
        this.gameOver = false;
        this.init();
    }

    init() {
        this.setupElements();
        this.newGame();
        this.bindEvents();
    }

    setupElements() {
        this.grid = document.getElementById('game-grid');
        this.scoreEl = document.getElementById('score');
        this.bestEl = document.getElementById('best');
        this.messageEl = document.getElementById('game-message').querySelector('p');
        this.newGameBtn = document.getElementById('new-game');
        this.keepPlayingBtn = document.getElementById('keep-playing');
        this.retryBtn = document.getElementById('retry');
    }

    bindEvents() {
        document.addEventListener('keydown', (e) => this.handleInput(e));
        this.newGameBtn.addEventListener('click', () => this.newGame());
        this.keepPlayingBtn.addEventListener('click', () => this.hideMessage());
        this.retryBtn.addEventListener('click', () => this.newGame());
    }

    newGame() {
        this.board = Array(4).fill().map(() => Array(4).fill(0));
        this.score = 0;
        this.gameWon = false;
        this.gameOver = false;
        this.updateScore();
        this.clearGrid();
        this.addRandomTile();
        this.addRandomTile();
        this.updateGrid();
        this.hideMessage();
    }

    handleInput(e) {
        if (this.gameOver || e.key.includes('Arrow') === false) return;
        
        let moved = false;
        switch(e.key) {
            case 'ArrowUp': moved = this.moveUp(); break;
            case 'ArrowDown': moved = this.moveDown(); break;
            case 'ArrowLeft': moved = this.moveLeft(); break;
            case 'ArrowRight': moved = this.moveRight(); break;
        }
        
        if (moved) {
            this.updateScore();
            setTimeout(() => {
                this.addRandomTile();
                this.updateGrid();
                this.checkGameState();
            }, 150);
        }
    }

    // ✅ LEFT - Đã hoạt động đúng
    moveLeft() {
        let moved = false;
        for (let i = 0; i < 4; i++) {
            let original = [...this.board[i]];

            let row = this.board[i].filter(val => val);
            let merged = this.merge(row);
            let newRow = merged.concat(Array(4 - merged.length).fill(0));

            if (original.toString() !== newRow.toString()) {
                moved = true;
            }

            this.board[i] = newRow;
        }
        return moved;
    }

    // ✅ RIGHT - Đã hoạt động đúng  
    moveRight() {
        let moved = false;
        for (let i = 0; i < 4; i++) {
            let original = [...this.board[i]];

            let row = this.board[i].filter(val => val).reverse();
            let merged = this.merge(row).reverse();
            let newRow = Array(4 - merged.length).fill(0).concat(merged);

            if (original.toString() !== newRow.toString()) {
                moved = true;
            }

            this.board[i] = newRow;
        }
        return moved;
    }


    // ✅ UP - SỬA BUG: Logic di chuyển theo cột từ trên xuống
    moveUp() {
        let moved = false;
        for (let j = 0; j < 4; j++) {
            let original = [
                this.board[0][j],
                this.board[1][j],
                this.board[2][j],
                this.board[3][j]
            ];

            let col = original.filter(val => val);
            let merged = this.merge(col);

            for (let i = 0; i < 4; i++) {
                this.board[i][j] = i < merged.length ? merged[i] : 0;
            }

            let newCol = [
                this.board[0][j],
                this.board[1][j],
                this.board[2][j],
                this.board[3][j]
            ];

            if (original.toString() !== newCol.toString()) {
                moved = true;
            }
        }
        return moved;
    }

    // ✅ DOWN - SỬA BUG: Logic di chuyển theo cột từ dưới lên
    moveDown() {
        let moved = false;
        for (let j = 0; j < 4; j++) {
            let original = [
                this.board[0][j],
                this.board[1][j],
                this.board[2][j],
                this.board[3][j]
            ];

            let col = original.filter(val => val).reverse();
            let merged = this.merge(col).reverse();

            for (let i = 0; i < 4; i++) {
                this.board[i][j] =
                    i >= 4 - merged.length ? merged[i - (4 - merged.length)] : 0;
            }

            let newCol = [
                this.board[0][j],
                this.board[1][j],
                this.board[2][j],
                this.board[3][j]
            ];

            if (original.toString() !== newCol.toString()) {
                moved = true;
            }
        }
        return moved;
    }

    merge(arr) {
        let newArr = [];
        for (let i = 0; i < arr.length; i++) {
            if (i + 1 < arr.length && arr[i] === arr[i + 1] && arr[i] !== 0) {
                let val = arr[i] * 2;
                newArr.push(val);
                this.score += val;
                if (val === 8192) this.gameWon = true;
                i++; // Skip next element
            } else if (arr[i] !== 0) {
                newArr.push(arr[i]);
            }
        }
        return newArr;
    }

    addRandomTile() {
        let emptyCells = [];
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if (this.board[i][j] === 0) {
                    emptyCells.push({x: i, y: j});
                }
            }
        }
        if (emptyCells.length > 0) {
            let pos = emptyCells[Math.floor(Math.random() * emptyCells.length)];
            this.board[pos.x][pos.y] = Math.random() < 0.9 ? 2 : 4;
        }
    }

    updateGrid() {
        this.grid.innerHTML = '';
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                let tile = document.createElement('div');
                tile.className = `tile ${this.board[i][j] ? 'tile-' + this.board[i][j] : ''}`;
                if (this.board[i][j]) {
                    tile.textContent = this.board[i][j];
                    tile.classList.add('animate');
                    setTimeout(() => tile.classList.remove('animate'), 500);
                }
                this.grid.appendChild(tile);
            }
        }
    }

    clearGrid() {
        this.grid.innerHTML = '';
    }

    updateScore() {
        this.scoreEl.textContent = this.score;
        if (this.score > this.bestScore) {
            this.bestScore = this.score;
            localStorage.setItem('best2048', this.bestScore);
        }
        this.bestEl.textContent = this.bestScore;
    }

    checkGameState() {
        if (this.has8192()) {
            this.showMessage('🎉 Bạn đã thắng! Đạt được 8192!', true);
            return;
        }
        
        if (!this.canMove()) {
            this.showMessage('❌ Game Over! Không còn nước đi nào.', false);
        }
    }

    has8192() {
        return this.board.flat().includes(8192);
    }

    canMove() {
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if (this.board[i][j] === 0) return true;
                if (j < 3 && this.board[i][j] === this.board[i][j + 1]) return true;
                if (i < 3 && this.board[i][j] === this.board[i + 1][j]) return true;
            }
        }
        return false;
    }

    showMessage(text, won) {
        this.messageEl.textContent = text;
        this.gameOver = true;
        document.getElementById('game-message').style.display = 'block';
        if (won) {
            this.keepPlayingBtn.style.display = 'inline-block';
            this.retryBtn.style.display = 'inline-block';
        } else {
            this.keepPlayingBtn.style.display = 'none';
            this.retryBtn.style.display = 'inline-block';
        }
    }

    hideMessage() {
        document.getElementById('game-message').style.display = 'none';
        this.gameOver = false;
    }
}

// Start game
window.addEventListener('load', () => {
    new Game2048();
});
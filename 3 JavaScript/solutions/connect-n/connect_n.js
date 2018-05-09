/* connect_four.js
JS rendition of the connect_four.py lab
*/

class Piece {
    constructor(color) {
        this.color = color;
    }
    
    toString() {
        if (this.color === 'black') return '██';
        if (this.color === 'white') return '░░';
    }
    
    isEqual(piece) {
        if (piece instanceof Piece) {
            return this.color == piece.color;
        }
    }
    
}


class GameBoard {    
    constructor(n=5, size=8) {
		this.DEPTH = size;
		this.WIDTH = size;
        this.N = n;
        this.board = Array.from(new Array(this.DEPTH), (y,i) => Array.from(new Array(this.WIDTH), (x,j) => pad(j+i*this.DEPTH+1)));
    }
    
    toString() {
        let ret = "";
        for (let i=0; i<this.DEPTH; ++i) {
            ret += this.board[i].join('|');
            ret += '\n';
        }
        return ret;
    }
    
    placePiece(pieceColor, y, x) {
        if (this.board[y][x] instanceof Piece) {
            return false;
        } else {
            this.board[y][x] = new Piece(pieceColor);
            return [y, x];            
        }
    }
    
    hasWon() {
        for (let i=this.DEPTH-1; i>=0; --i) {
            for (let j=0; j<this.WIDTH; ++j) {
                // check horizontal wins
                if (j<this.WIDTH-this.N+1) {
                    let chunk = this.board[i].slice(j,j+this.N);
                    if (chunk.every(function(item) {
                        return item instanceof Piece && item.isEqual(chunk[0]);
                    })) {
                        return chunk[0];
                    }                    
                }
                
                // check vertical wins
                if (i<this.DEPTH-this.N+1) {
                    let chunk = [];
                    for (let k=i; k<this.N; ++k) {
                        chunk.push(this.board[k][j])
                    }
                    if (chunk.every(function(item) {
                        return item instanceof Piece && item.isEqual(chunk[0]);
                    })) {
                        return chunk[0];
                    }    
                }
                
                // check diagonal wins
                if (i<this.DEPTH-this.N+1 && j<this.WIDTH-this.N+1) {
                    let chunk = [];
                    let leftDiag = true;
                    let rightDiag = true;
                    for (let k=0; k<this.N; ++k) {
                        chunk.push(this.board[i+k].slice(j, j+this.N));
                    }
                    for (let k=0; k<this.N; ++k) {
                        if (!leftDiag && !rightDiag) {
                            continue;
                        } else if ((chunk[k][k] instanceof Piece && !chunk[k][k].isEqual(chunk[0][0])) || !(chunk[k][k] instanceof Piece)) {
                            leftDiag = false;
                        } 
                        if ((chunk[this.N-k-1][k] instanceof Piece && !chunk[this.N-k-1][k].isEqual(chunk[this.N-1][0])) || !(chunk[this.N-k-1][k] instanceof Piece)) {
                            rightDiag = false;
                        }
                    }
                    
                    if (leftDiag) {
                        return chunk[0][0];
                    } 
                    if (rightDiag) {
                        return chunk[this.N-1][0];
                    }
                }
            }
        }
        return false;
    }
    
    isFull() {
        for (let i=0; i<this.DEPTH; ++i) {
            if (this.board[i].some(function(item) {
                return typeof item === 'string';                
            })) {
                return false;
            }
        }
        return true;
    }
    
    isGameOver() {
        return this.isFull() || this.hasWon();
    }
}


function pad(num, size=2) {
    var s = "000" + num;
    return s.substr(s.length-size);
}


function getCurrentPlayer(gameRound) {
    return (gameRound % 2 ? 'white' : 'black');
}


function initGameBoard(board, game) {
    for (let i=0; i<game.board.length; ++i) {
        let cells = [];
        for (let j=0; j<game.board[i].length; ++j) {
            cells.push($('<td>', {'class':"board-cell square", id:`cell-${i}-${j}`}).text(game.board[i][j]));
        }
        board.append($('<tr>').append(cells));
    }    
}


$(function () {
    var boardDiv = $('#board');
    var game = new GameBoard();
    console.log(String(game));
    var gameRound = 1;
    var currentPlayer = getCurrentPlayer(gameRound);
    
    initGameBoard(boardDiv, game);
    
    $('.board-cell').on('click', function(event) {
        if (!game.isGameOver()) {
            let position = $(event.delegateTarget).attr('id').split('-').slice(1);
            let move = game.placePiece(currentPlayer, position[0], position[1]);
            if (move) {
                gameRound++;
                let selected = $(`#cell-${move[0]}-${move[1]}`);
                selected.css({'background': currentPlayer, 'border-radius': '50px'});
                console.log(String(game));

                if (game.isGameOver()) {
                    $('#game-over').show();
                    $('#game').css({'z-index':100, 'background':'black', 'opacity':0.8})
                    $('#new-game').show();
                    if (game.hasWon()) {
                        console.log(`Game over! ${currentPlayer} wins!`);
                    } else {
                        console.log("Game over! No one wins!");
                    }
                } else {
                    currentPlayer = getCurrentPlayer(gameRound);
                }
            } else {
                console.log("Invalid position. Please choose a square that isn't full.");    
            }      
        }
    });
    
    $('#new-game').on('click', function(event) {
        game = new GameBoard();
        boardDiv.empty();
        initGameBoard(boardDiv, game);
        gameRound = 1;
        currentPlayer = getCurrentPlayer(gameRound);
        $('#game').css('background', 'tan');
        $('.board-cell').css('background', 'none');
    });
});
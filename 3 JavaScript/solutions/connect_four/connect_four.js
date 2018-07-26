/* connect_four.js
JS rendition of the connect_four.py lab
*/

class Piece {
    constructor(color) {
        this.color = color;
    }
    
    toString() {
        return this.color.charAt(0).toUpperCase();
    }
    
    isEqual(piece) {
        if (piece instanceof Piece) {
            return this.color == piece.color;
        }
    }
    
}


class GameBoard {    
    constructor() {
		this.DEPTH = 6;
		this.WIDTH = 7;
        this.board = Array.from(new Array(this.DEPTH), (y,i) => Array.from(new Array(this.WIDTH), (x,i) => 'O'));
    }
    
    toString() {
        let ret = "";
        for (let i=0; i<this.DEPTH; ++i) {
            ret += this.board[i].join('|');
            ret += '\n';
        }
        return ret;
    }
    
    getHeight(position) {
        for (let i=this.DEPTH-1; i>=0; --i) {
            if (this.board[i][position] == 'O') {
                return i;
            }
        }
        return false;
    }
    
    placePiece(pieceColor, position) {
        let height = this.getHeight(position);
        if (typeof height === 'boolean') {
            console.log("Column full. Select another.");
            return false;
        }
        this.board[height][position] = new Piece(pieceColor);
        return [height, position];
    }
    
    hasWon() {
        for (let i=this.DEPTH-1; i>=0; --i) {
            for (let j=0; j<this.WIDTH; ++j) {
                // check horizontal wins
                if (j<this.WIDTH-3) {
                    let chunk = this.board[i].slice(j,j+4);
                    if (chunk.every(function(item) {
                        return item != 'O' && item.isEqual(chunk[0]);
                    })) {
                        return chunk[0];
                    }                    
                }
                
                // check vertical wins
                if (i<this.DEPTH-3) {
                    let chunk = [];
                    chunk.push(this.board[i][j]);
                    chunk.push(this.board[i+1][j]);
                    chunk.push(this.board[i+2][j]);
                    chunk.push(this.board[i+3][j]);
                    if (chunk.every(function(item) {
                        return item != 'O' && item.isEqual(chunk[0]);
                    })) {
                        return chunk[0];
                    }    
                }
                
                // check diagonal wins
                if (i<this.DEPTH-3 && j<this.WIDTH-3) {
                    let chunk = [];
                    chunk.push(this.board[i].slice(j,j+4));
                    chunk.push(this.board[i+1].slice(j,j+4));
                    chunk.push(this.board[i+2].slice(j,j+4));
                    chunk.push(this.board[i+3].slice(j,j+4));
                    if (chunk[0][0] != 'O' && chunk[0][0].isEqual(chunk[1][1]) && chunk[1][1].isEqual(chunk[2][2]) && chunk[2][2].isEqual(chunk[3][3])) {
                        return chunk[0][0]                        
                    } else if (chunk[3][0] != 'O' && chunk[3][0].isEqual(chunk[1][2]) && chunk[1][2].isEqual(chunk[2][1]) && chunk[2][1].isEqual(chunk[0][3])) {
                        return chunk[3][0]                   
                    }
                }
            }
        }
        return false;
    }
    
    isFull() {
        for (let i=0; i<this.DEPTH; ++i) {
            if (this.board[i].some(function(item) {
                return item === 'O';                
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


function getCurrentPlayer(gameRound) {
    return (gameRound % 2 ? 'red' : 'yellow');
}


function initGameBoard(board, game) {
    for (let i=0; i<game.board.length; ++i) {
        let cells = [];
        for (let j=0; j<game.board[i].length; ++j) {
            cells.push($('<td>', {'class':"board-cell", id:`cell-${i}-${j}`}));
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
            let position = $(event.delegateTarget).attr('id').split('-')[2];
            let move = game.placePiece(currentPlayer, position);
            if (move) {
                gameRound++;
                let selected = $(`#cell-${move[0]}-${move[1]}`);
                selected.css({'background': currentPlayer, 'border-radius': '50px'});
                console.log(String(game));

                if (game.isGameOver()) {
                    $('#game-over').show();
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
                console.log("Invalid column. Please choose a column that isn't full.");    
            }      
        }
    });
    
    $('#new-game').on('click', function(event) {
        $('#game-over').hide();
        game = new GameBoard();
        initGameBoard(boardDiv, game);
        gameRound = 1;
        currentPlayer = getCurrentPlayer(gameRound);
        $('.board-cell').css('background', 'none');
    });
});
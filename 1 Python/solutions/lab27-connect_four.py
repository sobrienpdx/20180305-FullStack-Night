import random

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color[0].upper()

    def __eq__(self, other):
        if type(other) is Piece:
            if self.color == other.color:
                return True


class GameBoard:
    DEPTH = 6
    WIDTH = 7

    def __init__(self):
        self.board = [['O' for col in range(self.WIDTH)] for row in range(self.DEPTH)]

    def _get_height(self, position):
        for i in range(self.DEPTH-1, -1, -1):
            if self.board[i][position] == 'O':
                return i
        return False # column is full

    def check_win(self):
        # check horizontal wins
        for i in range(self.DEPTH-1, -1, -1):
            for j in range(self.WIDTH-3):
                chunk = self.board[i][j:j+4]
                if all(item == self.board[i][j] and item != 'O' for item in chunk):
                    return self.board[i][j]

        # check vertical wins
        for j in range(self.WIDTH):  
            for i in range(self.DEPTH-3):  
                chunk = []
                chunk.append(self.board[i][j])
                chunk.append(self.board[i+1][j])
                chunk.append(self.board[i+2][j])
                chunk.append(self.board[i+3][j])
                if all(item == self.board[i][j] and item != 'O' for item in chunk):
                    return self.board[i][j]

        # check diagonal wins
        for i in range(self.DEPTH-3):
            for j in range(self.WIDTH-3):
                chunk = []
                chunk.append(self.board[i][j:j+4])
                chunk.append(self.board[i+1][j:j+4])
                chunk.append(self.board[i+2][j:j+4])
                chunk.append(self.board[i+3][j:j+4])
                # for row in chunk:
                #     for cell in row:
                #         print(cell, end='|')
                #     print()
                # print(chunk[0][0] , chunk[1][1] , chunk[2][2] , chunk[3][3])
                # print(chunk[3][0] , chunk[1][2] , chunk[2][1] , chunk[0][3])
                # print()
                if chunk[0][0] == chunk[1][1] == chunk[2][2] == chunk[3][3] and chunk[0][0] != 'O':
                    return chunk[0][0]
                elif chunk[3][0] == chunk[1][2] == chunk[2][1] == chunk[0][3] and chunk[3][0] != 'O':
                    return chunk[3][0]


    def place_piece(self, piece_color, position):
        height = self._get_height(position)
        if not height:
            print('Column full. Select another.')
            return False
        self.board[height][position] = Piece(piece_color)

    def print_board(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print(cell, end='|')
            print()


if __name__ == '__main__':
    board = GameBoard()

    with open('connect-four-moves.txt', 'r') as f:
        moves = f.read().split()

    for i, move in enumerate(moves):
        current_turn = 'yellow' if i % 2 == 0 else 'red'
        board.place_piece(current_turn, int(move) - 1)

    board.print_board()
    print(board.check_win())
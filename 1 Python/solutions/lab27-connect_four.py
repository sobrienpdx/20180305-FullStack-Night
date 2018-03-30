import random

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color[0].upper()

class Game:
    DEPTH = 6
    WIDTH = 8

    def __init__(self):
        self.board = [['O' for col in range(self.WIDTH)] for row in range(self.DEPTH)]

    def place_piece(self, piece_color, board_index):
        height = self.get_height(board_index)
        if not height:
            print('Column full. Select another.')
            return False
        self.board[height][board_index] = Piece(piece_color)

    def get_height(self, board_index):
        for i in range(self.DEPTH-1, -1, -1):
            if self.board[i][board_index] == 'O':
                return i
        return False # column is full

    def print_board(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print(cell, end='|')
            print()
board = Game()

board.place_piece('red', 0)
board.place_piece('yellow', 0)

with open('connect-four-moves.txt', 'r') as f:
    moves = f.read().split()

for i, move in enumerate(moves):
    current_turn = 'yellow' if i % 2 == 0 else 'red'
    board.place_piece(current_turn, int(move) - 1)

board.print_board()
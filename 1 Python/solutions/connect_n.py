# connect_n.py 
# A combination of Tic Tac Toe and Connect Four: a two player game where to first player to get N in a row wins!
# Constraints:  2 <= N <= 8, 3x3 <= board_size <= 8x8

import argparse, random

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __eq__(self, other):
        if type(other) is Player:
            return self.token == other.token

    def __repr__(self):
        return self.token

class Board:

    def __init__(self, n, size):
        self.DEPTH = size
        self.WIDTH = size
        self.n = n
        self.board = [[' ' for i in range(self.WIDTH)] for j in range(self.DEPTH)]

    def __repr__(self):
        ret = ''
        for row in self.board:
            ret += '|'.join(row)
            ret += '\n'
        return ret
        
        # ret = ''
        # i = 1
        # for row in self.board:
        #     for cell in row:
        #         if cell == ' ':
        #             cell = i
        #         ret += str(cell)
        #         if i%3:
        #             ret += '|'
        #         i += 1
        #     ret += '\n'
        # return ret        

    def place_token(self, x, y, token):
        if self.board[y][x] != ' ':
            return 'Invalid move. Space taken.'
        else:
            self.board[y][x] = token

    def calc_winner(self):
        # check horizontal wins
        for i in range(self.DEPTH):
            for j in range(self.WIDTH-self.n-1):
                chunk = self.board[i][j:j+n]
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j].name

        # check vertical wins
        for j in range(self.WIDTH):  
            for i in range(self.DEPTH-self.n-1):  
                chunk = [(self.board[i+k][j] for k in range(self.n))]
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j]

        # check diagonal wins
        for i in range(self.DEPTH-self.n-1):
            for j in range(self.WIDTH-self.n-1):
                chunk = [chunk.append(self.board[i+k][j:j+self.n]) for k in range(self.n)]
                # for row in chunk:
                #     for cell in row:
                #         print(cell, end='|')
                #     print()
                left_diag = True
                right_diag = True
                for k in range(self.n):
                    if not left_diag and not right_diag :
                        return False
                    if chunk[k][k] != chunk[0][0] or chunk[k][k] == ' ':
                        left_diag = False
                    if chunk[self.n-k-1][k] != chunk[self.n-1][0] or chunk[self.n-k-1][k] == ' ':
                        right_diag = False
                if left_diag:
                    return chunk[0][0]
                if right_diag:
                    return chunk[self.n-1][0]

    def is_full(self):
        for row in self.board:
            if any(item==' ' for item in row):
                return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect N Game')
    parser.add_argument('-n', help='Number to connect to win.')
    parser.add_argument('-size', help='Size of game board (sizexsize)')
    args = parser.parse_args()

    grid_coord = {1:(0,0), 2:(1,0), 3:(2,0),
                  4:(0,1), 5:(1,1), 6:(2,1),
                  7:(0,2), 8:(1,2), 9:(2,2)}
    move = 6
    x, y = grid_coord[move]
    while True:
        board = Board(3,3)
        player_one = Player(input("Player one: "), 'X')
        player_two = Player(input("Player two: "), 'O')
        game_round = 1

        while not board.is_game_over():
            current_player = player_one if game_round % 2 else player_two 

            while True:
                move = input(f"{current_player.name}: Enter your move: ").strip()
                try:
                    move = int(move)
                    if 1 <= move <= 9:
                        x, y = grid_coord[move]
                        move = board.place_token(x, y, current_player.token)
                        if type(move) is str:
                            raise IndexError('Invalid move.')
                        print(board)
                        game_round += 1
                        break
                    else:
                        raise IndexError('Invalid move.')
                except (ValueError, IndexError):
                    # try:
                    #   x, y = move.split(',')
                    # except ValueError, IndexError:
                        print("Invalid move. Please choose a sqaure [1-9] that isn't full.")

        if not board.is_full():
            print(f"Game over! Winner: {board.calc_winner()}")
        else:
            print(f"Game over! Tie!")

        while True:
            play_ag = input("Do you want to play again: ").strip().lower()
            if play_ag in ['yes', 'y', 'no', 'n']:
                break

        if play_ag in ['no', 'n']:
            break      
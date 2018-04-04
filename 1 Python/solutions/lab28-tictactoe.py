# lab28 - tictactoe.py

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
    DEPTH = 3
    WIDTH = 3

    def __init__(self):
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
        for i in range(self.DEPTH-1, -1, -1):
            for j in range(self.WIDTH-2):
                chunk = self.board[i][j:j+3]
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j].name

        # check vertical wins
        for j in range(self.WIDTH):  
            for i in range(self.DEPTH-2):  
                chunk = []
                chunk.append(self.board[i][j])
                chunk.append(self.board[i+1][j])
                chunk.append(self.board[i+2][j])
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j]

        # check diagonal wins
        for i in range(self.DEPTH-2):
            for j in range(self.WIDTH-2):
                chunk = []
                chunk.append(self.board[i][j:j+3])
                chunk.append(self.board[i+1][j:j+3])
                chunk.append(self.board[i+2][j:j+3])
                # for row in chunk:
                #     for cell in row:
                #         print(cell, end='|')
                #     print()

                if chunk[0][0] == chunk[1][1] == chunk[2][2] and chunk[0][0] != ' ':
                    return chunk[0][0]
                elif chunk[2][0] == chunk[1][1] == chunk[0][2] and chunk[2][0] != ' ':
                    return chunk[2][0]

    def is_full(self):
        for row in self.board:
            if any(item==' ' for item in row):
                return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


if __name__ == '__main__':
    grid_coord = {1:(0,0), 2:(1,0), 3:(2,0),
                  4:(0,1), 5:(1,1), 6:(2,1),
                  7:(0,2), 8:(1,2), 9:(2,2)}
    while True:
        board = Board()
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

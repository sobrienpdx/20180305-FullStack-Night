class Piece(object):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def __repr__(self):
		if self.color == 'red':
			return 'R'
		else:
			return 'B'

	def change_position(self, direction, magnitude):
		if self.color == 'red':
			if direction == 'left':
				return (self.position[0]-(magnitude*1), self.position[1]-(magnitude*1))
			else:
				return (self.position[0]+(magnitude*1), self.position[1]-(magnitude*1))
		else:
			if direction == 'left':
				return (self.position[0]+(magnitude*1), self.position[1]+(magnitude*1))
			else:
				return (self.position[0]-(magnitude*1), self.position[1]+(magnitude*1))

	def move_forward(self, direction):
		self.position = self.change_position(direction, 1)

	def jump(self, direction):
		self.position = self.change_position(direction, 2)



class CheckersBoard(object):

	def __init__(self):
		self.board = [['B', 'O', 'B', 'O', 'B', 'O', 'B', 'O'],
					  ['O', 'B', 'O', 'B', 'O', 'B', 'O', 'B'],
					  ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
					  ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
					  ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
					  ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
					  ['X', 'R', 'X', 'R', 'X', 'R', 'X', 'R'],
					  ['R', 'X', 'R', 'X', 'R', 'X', 'R', 'X']]
		self.black_team = []
		self.red_team = []
		self.black_points = 0
		self.red_points = 0

		for j in range(len(self.board)):
			for i in range(len(self.board[j])):
				square = self.board[j][i]
				if square == 'B':
					self.board[j][i] = Piece('black', (i, j))
					self.black_team.append(self.board[j][i])
				elif square == 'R':
					self.board[j][i] = Piece('red', (i, j))
					self.red_team.append(self.board[j][i])


	def __repr__(self):
		ret = ''
		for j in range(len(self.board)):
			if j > 0:
				ret += '\n'
			for i in range(len(self.board[j])):
				if j%2 == 0:
					even = 'X'
					odd = 'O'
				else:
					even = 'O'
					odd = 'X'
				if type(self.board[j][i]) is Piece:
					ret += str(self.board[j][i])
				else:
					if i%2 == 0:
						ret += even
					else:
						ret += odd
		return ret


	def move_piece(self, position, direction):
		y, x = position
		square = self.board[x][y] 
		if type(square) is Piece:
			self.board[x][y].move_forward(direction)
			piece = self.board[x][y]
			y2, x2 = piece.position
			self.board[x2][y2] = piece
			self.board[x][y] = None

if __name__ == '__main__':
	board = CheckersBoard()
	print(board)
	print()
	board.move_piece((1,1), 'left')
	print(board)

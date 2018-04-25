"""
knights_moves.py

From Google foo.bar challenge:

Write a function answer(src, dest) that takes a two integers with values between 1 and 64 representing a position on a chessboard and returns the length of the minimal route a knight piece can take to get from the source position to the destination position.

"""
import heapq
from collections import defaultdict


class Position:
    def __init__(self, coord):
        self.x, self.y = coord

    def __add__(self, coord):
        return (self.x + coord.x, self.y+coord.y)


class PriorityQueue:
    """ Simple priority queue implementation using binary heaps
    """
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def empty(self):
        return len(self.elements) == 0


class Graph:
    """ Simple graph implementation
    """
    CHESSBOARD = {}
    for i in range(8):
        for j in range(8):
            CHESSBOARD[i+8*j] = (i, j)        

    COORDINATES = {v:k for k,v in CHESSBOARD.items()}            

    def __init__(self):
        self.edges = {}

    def get_neighbors(self, node):
        """ Returns list of positions reachable with knight moves
        """
        knight_moves = [(-1,-2), (1,2),
                        (1,-2), (-1,2),
                        (-2,-1), (2,1),
                        (2,-1), (-2,1)] 
        neighbors = []
        for move in knight_moves:
            x, y = Position(node) + Position(move)
            if 0 <= x < 8 and 0 <= y < 8:
                neighbors.append((x,y))
        self.edges[node] = neighbors
        
    @staticmethod
    def h(start, goal):
        """ Returns manhattan distance heuristic
        """
        (x1, y1) = start
        (x2, y2) = goal
        return abs(x1-x2) + abs(y1-y2)

    def reconstruct_path(self, came_from, start, end):
        path = []
        current_node = end
        while current_node != start:
            path.append(self.COORDINATES[current_node])
            current_node = came_from[current_node]
        path.reverse()
        return path

    def validate_destination(self, start, goal):
        try:
            start = self.CHESSBOARD[start]
            goal = self.CHESSBOARD[goal]
            return (start, goal)
        except KeyError:
            return 'Invalid destination.'

    def bfs(self, start, goal):
        valid = self.validate_destination(start, goal)
        if type(valid) is str:
            return valid 
        start, goal = valid
        visited = set()                         # set of visited nodes
        fringe = []                             # fringe with queue list implementation
        came_from = {}                          # path history
        fringe.append(start)
        came_from[start] = None

        while len(fringe):
            current_node = fringe.pop(0)
            # exit condition: solution found
            if current_node == goal:
                return self.reconstruct_path(came_from, start, current_node)

            # update fringe and visited set
            visited.add(current_node)
            self.get_neighbors(current_node)
            for neighbor in self.edges[current_node]:
                # add neighbor to fringe it's unexplored
                if neighbor not in visited:
                    fringe.append(neighbor)
                    came_from[neighbor] = current_node


    def a_star(self, start, goal):
        """ A* search algorithm implementation
        """
        valid = self.validate_destination(start, goal)
        if type(valid) is str:
            return valid 
        start, goal = valid
        visited = set()                         # set of visited nodes
        fringe = PriorityQueue()                # priority queue of fringe nodes
        came_from = {}                          # path history
        f = defaultdict(lambda: float('inf'))   # f(n) = g(n) + h(n) (priority rating)
        g = defaultdict(lambda: float('inf'))   # g(n) = cost of path from start node
                                                # h(n) = heuristic distance to goal
        came_from[start] = None
        f[start] = self.h(start, goal)
        g[start] = 0
        fringe.put(start, f[start])

        while not fringe.empty():
            # select node with lowest f value
            current_node = fringe.get()

            # exit condition
            if current_node == goal:
                return self.reconstruct_path(came_from, start, current_node)

            # update fringe and visited set
            visited.add(current_node)

            # explore neighbors of current node
            self.get_neighbors(current_node)            
            for neighbor in self.edges[current_node]:
                g_score = g[current_node] + 1
                # add neighbor to fringe it's unexplored or now has a lower cost
                if neighbor not in visited or g_score < g[neighbor]:
                    g[neighbor] = g_score
                    f[neighbor] = self.h(neighbor, goal) + g[neighbor]
                    fringe.put(neighbor, f[neighbor])
                    came_from[neighbor] = current_node


def answer(src, dest):
    ret = Graph().bfs(src, dest)
    return len(ret) if type(ret) is list else ret
    

if __name__ == '__main__':
    game = Graph()
    board = list(game.CHESSBOARD.keys())


    start, goal = (0, 1)
    start, goal = (19, 36)
    # start, goal = (0, 0)
    start, goal = (0, 64)
    start, goal = (0, 7)    
    start, goal = (63, 56)  
    # tests = [((0, 1), , (0, 0), (0, 64), (19, 36), (0, 7), (63, 56)] 


    for i in range(8):
        for j in range(8):
            square = str(board[i+8*j])
            if str(square) == str(start): 
                square = '██'
            elif str(square) == str(goal):
                square = '██'
            print(square.zfill(2), end='|')
        print()

    solution = game.a_star(start, goal)
    print(solution, len(solution) if not type(solution) is str else '')
    print(answer(start, goal))    
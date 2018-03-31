from collections import defaultdict
from multiprocessing import Queue

# # Chessboard position
# Position = namedtuple('Position', ['number', 'coord'])

# # Chessboard
# Chessboard = [[Position(i+8*j, (i, j)) for i in range(8)] for j in range(8)]

class Graph:
    """ Simple graph implementation
    """
    CHESSBOARD = {}
    for i in range(8):
        for j in range(8):
            CHESSBOARD[i+8*j] = (i, j)        

    def __init__(self):
        self.edges = {}

    def get_neighbors(self, node):
        """ Returns list of positions reachable with knight moves
        """
        knight_moves = [-17, -15, -10, -6, 6, 10, 15, 17] 
        neighbors = []
        for move in night_moves:
            neighbor = node + move
            if 0 <= neighbor < 64:
                neighbors.append(neighbor)
        self.edges[node] = neighbors
        
    @staticmethod
    def h(start, goal):
        """ Returns manhattan distance heuristic
        """
        (x1, y1) = self.CHESSBOARD[start]
        (x2, y2) = self.CHESSBOARD[goal]
        return abs(x1-x2) + abs(y1-y2)

    @staticmethod
    def reconstruct_path(came_from, start, end):
        path = []
        current_node = end
        while current_node != start:
            path.append(current_node)
            current_node = came_from[current_node]
        path.reverse()
        return path


    def a_star(self, start, goal):
        """ A* search algorithm implementation
        """
        visited = set()                         # set of visited nodes
        fringe = PriorityQueue()                # priority queue of fringe nodes
        came_from = {}                          # history of nodes
        f = defaultdict(float('inf'))           # f(n) = g(n) + h(n) (total cost to goal)
        g = defaultdict(float('inf'))           # g(n) = cost of path from start node
                                                # h(n) = heuristic distance to goal
        came_from[start] = None
        f[start] = h(start, goal)
        g[start] = 0
        fringe.put(start, f[start])
        current_node = start

        while not fringe.empty():
            # select node with lowest f value
            current_node = fringe.get()

            # exit condition
            if current_node == goal:
                return reconstruct_path(came_from, current_node)

            # update fringe and visited sets
            visited.add(current_node)

            # explore neighbors of current node
            for neighbor in self.get_neighbors(current_node):
                if neighbor in visited:
                    continue  # ignore visited nodes
                
                if neighbor not in fringe:
                    fringe.add(neighbor)
                    g_score = g[current_node] + 1
                    f_score = h(neighbor, goal) + g_score




if __name__ == '__main__':
    game = Graph()
    board = game.CHESSBOARD.keys():
    for i in range(8):
        for j in range(8):
            print(str(board[i+8*j]).zfill(2), sep='|')
        print()
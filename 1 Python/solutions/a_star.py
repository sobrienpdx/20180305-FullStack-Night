from collections import defaultdict, namedtuple

# # Chessboard position
# Position = namedtuple('Position', ['number', 'coord'])

# # Chessboard
# Chessboard = [[Position(i+8*j, (i, j)) for i in range(8)] for j in range(8)]

Chessboard = {}
for i in range(8):
    for j in range(8):
        Chessboard[i+8*j] = (i, j)
        
def Tree():
    """ Tree implementation using defaultdict
    """
    return defaultdict(Tree)


def h(start, goal):
    """ Returns manhattan distance heuristic
    """
    (x1, y1) = Chessboard[start]
    (x2, y2) = Chessboard[goal]
    return abs(x1-x2) + abs(y1-y2)


def get_neighbors(node):
    """ Returns list of positions reachable with knight moves
    """
    knight_moves = [-17, -15, -10, -6, 6, 10, 15, 17] 
    neighbors = []
    for move in night_moves:
        neighbor = node + move
        if 0 <= neighbor < 64:
            neighbors.append(neighbor)
    return neighbors


def a_star(start, goal):
    """ A* search algorithm implementation
    """
    visited = set()                         # set of visited nodes
    fringe = set(start)                     # set of fringe nodes
    came_from = {}                          # history of nodes
    f = defaultdict(float('inf'))           # f(n) = g(n) + h(n) (total cost to goal)
    g = defaultdict(float('inf'))           # cost of path from start node
    f[start] = h(start, goal)
    g[start] = 0
    current_node = start

    while len(fringe):
        # calculate f values for all nodes in the fringe
        options = [(node, g[current_node] + h(node, goal)) for node in fringe]
        options.sort(key=operator.itemgetter(1))
        # select node with lowest f value
        current_node = options[0][0]

        # exit condition
        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        # update fringe and visited sets
        fringe.remove(current_node)
        visited.add(current_node)

        # explore neighbors of current node
        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor in visited:
                continue  # ignore visited nodes
            
            if neighbor not in fringe:
                fringe.add(neighbor)
                g[neighbor] = came_from[]



if __name__ == '__main__':
    for row in Chessboard:
        for col in row:
            print(f'{col}', sep=' ')
        print()
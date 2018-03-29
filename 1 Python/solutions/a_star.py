from collections import defaultdict, namedtuple

# Chessboard position
Position = namedtuple('Position', ['number', 'coord'])

# Chessboard
Chessboard = [[Position(i+8*j, (i, j)) for i in range(8)] for j in range(8)]

def Tree():
    """ Tree implementation using defaultdict
    """
    return defaultdict(Tree)


def h(start, goal):
    """ Returns manhattan distance heuristic
    """
    return abs(goal[0]-start[0]) + abs(goal[1]-start[1])


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
        current_node = options[0][0]       # select node with lowest f value
        if current_node == goal:
            return reconstruct_path(came_from, current_node)
        fringe.remove(current_node)
        visited.add(current_node)

        # neighbors = 


if __name__ == '__main__':
    for row in Chessboard:
        for col in row:
            print(f'{col}', sep=' ')
        print()
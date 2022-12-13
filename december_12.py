import math


class Node:
    def __init__(self, position, height, name):
        self.x = position[0]
        self.y = position[1]
        self.height = height
        self.path_length = float('inf')
        self.closed = False
        self.prev_node = None
        self.end_node = False
        self.name = name

class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.initial_node = None
        self.nodes = self.build_grid()
    def get_neighbours(self, current_node):
        return {v for k, v in self.nodes.items() if vector_distance((current_node.x, current_node.y), k) == 1}

    def build_grid(self):
        x = 0
        y = 0
        nodes = {}
        for row in self.rows:
            for height in row:
                node = Node(position=(x, y), height = 200 - ord(height), name=height)
                if height == 'a':
                    node.end_node = True
                if height == ('E'):
                    node.height = 200 - ord('z')
                    self.initial_node = node
                nodes[x, y] = node
                x += 1
            y += 1
            x = 0
        return nodes
def bfs(grid):
    initial_node = grid.initial_node
    queue = [grid.initial_node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        if not current_node.closed:
            current_node.closed = True
            if current_node.end_node:
                print(current_node.height, current_node.path_length)
                return current_node, current_node.path_length
            neighbours = grid.get_neighbours(current_node)
            for neighbour in neighbours:
                if not neighbour.closed:
                    if (neighbour.height - current_node.height) <= 1:
                        neighbour.path_length = current_node.path_length + 1
                        neighbour.prev_node = current_node
                        queue.append(neighbour)
    return initial_node, float('inf')


def read_grid(grid):
    with open(grid, 'r') as f:
        rows = f.read().split('\n')
    return rows

def vector_distance(v1, v2):
    return math.sqrt(sum([math.pow(v1[i]-v2[i], 2) for i in range(len(v1))]))
def get_result(file):
    rows = read_grid(file)

    grid = Grid(rows)
    last_node, path_lenght = bfs(grid)
    total_lenght = 0
    while last_node.prev_node is not None:
        print(last_node.prev_node.x, last_node.prev_node.y, last_node.prev_node.name, last_node.prev_node.height)
        last_node = last_node.prev_node
        total_lenght += 1
    print(total_lenght)



if __name__ == '__main__':
    get_result('./data/input_12.txt')


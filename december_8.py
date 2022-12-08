import numpy as np

def read_grid(file):
    with open(file, 'r') as f:
        rows = f.read().split('\n')
    rows = [list(map(int, row)) for row in rows]
    grid = np.zeros((len(rows), len(rows[0])))
    for i, row in enumerate(rows):
        grid[i,:] = row
    return grid

def check_if_visible(x, y, grid):
    tree = grid[x,y]
    if (tree > max(grid[:x, y])) or (tree > max(grid[x+1:, y])) or (tree > max(grid[x, :y])) or (tree > max(grid[x, y+1:])):
        return 1
    else:
         return 0

def get_num_of_smaller_trees(x, y, grid):
    tree = grid[x,y]
    top = np.flip(grid[:x, y])
    bottom = grid[x+1:, y]
    left = np.flip(grid[x, :y])
    right = grid[x, y+1:]

    tree_numbers = [get_num_of_lower_trees(tree, direction) for direction in [left, right, top, bottom]]
    return np.prod(tree_numbers)

def get_num_of_lower_trees(tree, tree_list):
    indices = np.where(tree_list >= tree)
    if len(indices[0]) > 0:
        return len(tree_list[:min(indices)[0]]) + 1
    else:
        return len(tree_list)


def get_result(file):
    grid = read_grid(file)
    visible_trees = 0
    max_visibility = 0
    for x in range(1, grid.shape[0]-1):
        for y in range(1, grid.shape[1]-1):
            visible_trees += check_if_visible(x, y, grid)
            tree_visibility = get_num_of_smaller_trees(x, y, grid)
            if tree_visibility > max_visibility:
                max_visibility = tree_visibility

    border = 2*grid.shape[0] + 2*grid.shape[1] - 4
    visible_trees += border
    print(visible_trees)
    print(max_visibility)

if __name__ == '__main__':
    get_result('./data/input_8.txt')


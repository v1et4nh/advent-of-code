def within_grid(grid, row, col):
    return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))


def is_valid(current_val, next_val):
    return next_val - current_val == 1


def get_total(grid, src):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    open_list = [src]
    reached = []
    while len(open_list) > 0:
        i, j = open_list.pop(0)
        current_val = grid[i][j]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            if within_grid(grid, new_i, new_j) and is_valid(current_val, grid[new_i][new_j]):
                if grid[new_i][new_j] == 9:
                    reached.append((new_i, new_j))
                else:
                    open_list.append((new_i, new_j))
    return len(reached)


if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    grid = [list(map(int, list(l.strip()))) for l in lines]
    start = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                start.append((row, col))
    total = 0
    for s in start:
        total += get_total(grid, s)
    print(total)
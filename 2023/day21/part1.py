from copy import deepcopy
import numpy as np
from tqdm import tqdm


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [list(l.strip()) for l in file]
    output = 0
    n      = 2
    steps  = (len(lines)-1)//2 + len(lines) * n

    for _ in range(n):
        lines = np.hstack((lines, lines, lines))
        lines = np.vstack((lines, lines, lines))

    start = ((len(lines)-1)//2, (len(lines)-1)//2)
    pos_arr = [start]

    for s in tqdm(range(steps)):
        new_start = []
        for pos in pos_arr:
            i, j = pos
            # north
            if lines[i-1][j] in ['.', 'S'] and (i-1, j) and (i-1, j) not in new_start:
                new_start.append((i-1, j))
            # south
            if lines[i+1][j] in ['.', 'S'] and (i+1, j) and (i+1, j) not in new_start:
                new_start.append((i+1, j))
            # west
            if lines[i][j+1] in ['.', 'S'] and (i, j+1) and (i, j+1) not in new_start:
                new_start.append((i, j+1))
            # east
            if lines[i][j-1] in ['.', 'S'] and (i, j-1) and (i, j-1) not in new_start:
                new_start.append((i, j-1))
        pos_arr = deepcopy(new_start)

    print(len(pos_arr))
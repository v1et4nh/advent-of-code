import numpy as np

goal = 26501365
def f(n):
    a0 = 3955   # 3906
    a1 = 35214  # 34896
    a2 = 96784

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

print(f(goal//131))

if __name__ == '__main__':
    with open('puzzle_input_example.txt', 'r') as file:
        lines = [list(l.strip()) for l in file]
    steps = 5 + 11*2

    for _ in range(3):
        lines = np.hstack((lines, lines, lines))
        lines = np.vstack((lines, lines, lines))

    start = ((len(lines)-1)//2, (len(lines)-1)//2)
    pos_arr_even = []  # Using a set for faster operations
    pos_arr_odd  = [start]
    total_set = {0: [], 1: []}
    last_set = {0: [start], 1: []}
    for s in range(steps):
        new_start = []
        c = 1  # even
        if s % 2 == 0:  # odd
            c = 0
        pos_arr = last_set[c]
        for pos in pos_arr:
            i, j = pos
            # Check and update positions
            directions = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
            for new_pos in directions:
                x, y = new_pos
                if lines[x][y] in ['.', 'S'] and new_pos not in total_set[c ^ 1] and new_pos not in new_start:
                    new_start.append(new_pos)
        last_set[c ^ 1] = new_start
        total_set[c].extend(pos_arr)
    total_set[c ^ 1].extend(new_start)
    print(len(total_set[c ^ 1]))

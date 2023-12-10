import numpy as np


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [line.replace('\n', '') for line in lines]

    # Get starting position
    start_row = [i for i, l in enumerate(lines) if 'S' in l][0]
    start_col = [i for i, l in enumerate(lines[start_row]) if 'S' in l][0]
    start = (start_row, start_col)
    dir_1 = [start]
    pos_arr = ['S']

    current_pos = start
    # First
    while dir_1.count(start) == 1:
        north = tuple(np.subtract(current_pos, (1, 0)))
        east  = tuple(np.add(current_pos, (0, 1)))
        south = tuple(np.add(current_pos, (1, 0)))
        west  = tuple(np.subtract(current_pos, (0, 1)))
        if north[0] < len(lines) and north[1] < len(lines[0]):
            if lines[north[0]][north[1]] in ['S', '|', '7', 'F'] \
                    and pos_arr[-1] in ['S', '|', 'L', 'J'] \
                    and (north not in dir_1 or (north == start and len(dir_1) > 2)):
                dir_1.append((north[0], north[1]))
                current_pos = north
                pos_arr.append(lines[north[0]][north[1]])
                continue
        if east[0] < len(lines) and east[1] < len(lines[0]):
            if lines[east[0]][east[1]] in ['S', '-', 'J', '7'] \
                    and pos_arr[-1] in ['S', '-', 'L', 'F'] \
                    and (east not in dir_1 or (east == start and len(dir_1) > 2)):
                dir_1.append((east[0], east[1]))
                current_pos = east
                pos_arr.append(lines[east[0]][east[1]])
                continue
        if south[0] < len(lines) and south[1] < len(lines[0]):
            if lines[south[0]][south[1]] in ['S', '|', 'L', 'J'] \
                    and pos_arr[-1] in ['S', '|', '7', 'F'] \
                    and (south not in dir_1 or (south == start and len(dir_1) > 2)):
                dir_1.append((south[0], south[1]))
                current_pos = south
                pos_arr.append(lines[south[0]][south[1]])
                continue
        if west[0] < len(lines) and west[1] < len(lines[0]):
            if lines[west[0]][west[1]] in ['S', '-', 'L', 'F'] \
                    and pos_arr[-1] in ['S', '-', 'J', '7'] \
                    and (west not in dir_1 or (west == start and len(dir_1) > 2)):
                dir_1.append((west[0], west[1]))
                current_pos = west
                pos_arr.append(lines[west[0]][west[1]])

    lines = [list(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) not in dir_1:
                lines[i][j] = '.'
    total_sum = 0
    lines = [''.join(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                count = lines[i][:j].count('|') + lines[i][:j].count('L') + lines[i][:j].count('J')
                if (count % 2 == 1) and (count != 0):
                    total_sum += 1
                # lines[i][j] = '.'
    print(total_sum)

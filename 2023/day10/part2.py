from numpy import add, subtract


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    # Get starting position
    start_row = [i for i, l in enumerate(lines) if 'S' in l][0]
    start_col = lines[start_row].find('S')
    start     = (start_row, start_col)
    dir_arr   = [start]
    pos_arr   = ['S']

    current_pos = start
    while dir_arr.count(start) == 1:
        north = tuple(subtract(current_pos, (1, 0)))
        east  = tuple(add(current_pos, (0, 1)))
        south = tuple(add(current_pos, (1, 0)))
        west  = tuple(subtract(current_pos, (0, 1)))
        if north[0] < len(lines) and north[1] < len(lines[0]):
            if lines[north[0]][north[1]] in ['S', '|', '7', 'F'] \
                    and pos_arr[-1] in ['S', '|', 'L', 'J'] \
                    and (north not in dir_arr or (north == start and len(dir_arr) > 2)):
                dir_arr.append((north[0], north[1]))
                current_pos = north
                pos_arr.append(lines[north[0]][north[1]])
                continue
        if east[0] < len(lines) and east[1] < len(lines[0]):
            if lines[east[0]][east[1]] in ['S', '-', 'J', '7'] \
                    and pos_arr[-1] in ['S', '-', 'L', 'F'] \
                    and (east not in dir_arr or (east == start and len(dir_arr) > 2)):
                dir_arr.append((east[0], east[1]))
                current_pos = east
                pos_arr.append(lines[east[0]][east[1]])
                continue
        if south[0] < len(lines) and south[1] < len(lines[0]):
            if lines[south[0]][south[1]] in ['S', '|', 'L', 'J'] \
                    and pos_arr[-1] in ['S', '|', '7', 'F'] \
                    and (south not in dir_arr or (south == start and len(dir_arr) > 2)):
                dir_arr.append((south[0], south[1]))
                current_pos = south
                pos_arr.append(lines[south[0]][south[1]])
                continue
        if west[0] < len(lines) and west[1] < len(lines[0]):
            if lines[west[0]][west[1]] in ['S', '-', 'L', 'F'] \
                    and pos_arr[-1] in ['S', '-', 'J', '7'] \
                    and (west not in dir_arr or (west == start and len(dir_arr) > 2)):
                dir_arr.append((west[0], west[1]))
                current_pos = west
                pos_arr.append(lines[west[0]][west[1]])

    # Replace all unvisited tiles with '.'
    lines = [list(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) not in dir_arr:
                lines[i][j] = '.'
    total_sum = 0

    # Check if tiles are inside or outside
    lines = [''.join(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                count = sum(lines[i][:j].count(x) for x in ['|', 'L', 'J'])
                if count % 2 == 1:
                    total_sum += 1
    print(total_sum)

from numpy import add, subtract


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        data = [l.strip() for l in file]

    # Init
    start_row = [i for i, l in enumerate(data) if 'S' in l][0]
    start_col = data[start_row].find('S')
    start     = (start_row, start_col)
    dir_arr   = [start]
    pos_arr   = ['S']

    current_pos = start
    while dir_arr.count(start) == 1:
        north = tuple(subtract(current_pos, (1, 0)))
        east  = tuple(add(current_pos, (0, 1)))
        south = tuple(add(current_pos, (1, 0)))
        west  = tuple(subtract(current_pos, (0, 1)))
        directions = [north, east, south, west]

        if north[0] < len(data) and north[1] < len(data[0]):
            if data[north[0]][north[1]] in ['S', '|', '7', 'F'] \
                    and pos_arr[-1] in ['S', '|', 'L', 'J'] \
                    and (north not in dir_arr or (north == start and len(dir_arr) > 2)):
                dir_arr.append((north[0], north[1]))
                current_pos = north
                pos_arr.append(data[north[0]][north[1]])
                continue
        if east[0] < len(data) and east[1] < len(data[0]):
            if data[east[0]][east[1]] in ['S', '-', 'J', '7'] \
                    and pos_arr[-1] in ['S', '-', 'L', 'F'] \
                    and (east not in dir_arr or (east == start and len(dir_arr) > 2)):
                dir_arr.append((east[0], east[1]))
                current_pos = east
                pos_arr.append(data[east[0]][east[1]])
                continue
        if south[0] < len(data) and south[1] < len(data[0]):
            if data[south[0]][south[1]] in ['S', '|', 'L', 'J'] \
                    and pos_arr[-1] in ['S', '|', '7', 'F'] \
                    and (south not in dir_arr or (south == start and len(dir_arr) > 2)):
                dir_arr.append((south[0], south[1]))
                current_pos = south
                pos_arr.append(data[south[0]][south[1]])
                continue
        if west[0] < len(data) and west[1] < len(data[0]):
            if data[west[0]][west[1]] in ['S', '-', 'L', 'F'] \
                    and pos_arr[-1] in ['S', '-', 'J', '7'] \
                    and (west not in dir_arr or (west == start and len(dir_arr) > 2)):
                dir_arr.append((west[0], west[1]))
                current_pos = west
                pos_arr.append(data[west[0]][west[1]])

    print((len(dir_arr)-1)//2)

def get_neighbors(block_list, open_list, pos):
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    appended = True
    while appended:
        appended = False
        neighbors = [(pos[0]+d[0], pos[1]+d[1]) for d in direction if (pos[0]+d[0], pos[1]+d[1]) in current_plots]
        for n in neighbors:
            if n in open_list:
                dict_separate[count].append(n)
                open_list.remove(n)
                appended = True
                block_list, open_list = get_neighbors(block_list, open_list, n)
    return block_list, open_list


def get_area_perimeter(block):
    perimeter = []
    for coords in block:
        for orientation, d in enumerate(direction):
            fence = (coords[0] + d[0], coords[1] + d[1])
            if fence not in block:
                perimeter.append((coords[0] + d[0], coords[1] + d[1], orientation))
    perimeter_len = len(list(set(perimeter)))
    area = len(block)
    return area, perimeter_len


def get_area_sides(block):
    sides = 0
    perimeter = []
    for coords in block:
        for orientation, d in enumerate(direction):
            fence = (coords[0] + d[0], coords[1] + d[1])
            if fence not in block:
                perimeter.append((coords[0] + d[0], coords[1] + d[1], orientation))
    perimeter = list(set(perimeter))
    dict_perimeter = {0: [], 1: [], 2: [], 3: []}  # top, down, right, left
    for p in perimeter:
        dict_perimeter[p[2]].append(p[:2])
    # sorted(data, key=lambda tup: tup[1])
    # Sort
    dict_perimeter[0] = sorted(dict_perimeter[0], key=lambda tup: (tup[0], tup[1]))
    dict_perimeter[1] = sorted(dict_perimeter[1], key=lambda tup: (tup[0], tup[1]))
    dict_perimeter[2] = sorted(dict_perimeter[2], key=lambda tup: (tup[1], tup[0]))
    dict_perimeter[3] = sorted(dict_perimeter[3], key=lambda tup: (tup[1], tup[0]))

    row = -9999
    col = -9999
    for idx in range(len(dict_perimeter[0])):
        current_el = dict_perimeter[0][idx]
        if current_el[0] != row:
            row, col = current_el
            sides += 1
        if abs(col-current_el[1]) > 1:
            sides += 1
        col = current_el[1]

    row = -9999
    col = -9999
    for idx in range(len(dict_perimeter[1])):
        current_el = dict_perimeter[1][idx]
        if current_el[0] != row:
            row, col = current_el
            sides += 1
        if abs(col-current_el[1]) > 1:
            sides += 1
        col = current_el[1]

    row = -9999
    col = -9999
    for idx in range(len(dict_perimeter[2])):
        current_el = dict_perimeter[2][idx]
        if current_el[1] != col:
            row, col = current_el
            sides += 1
        if abs(row-current_el[0]) > 1:
            sides += 1
        row = current_el[0]

    row = -9999
    col = -9999
    for idx in range(len(dict_perimeter[3])):
        current_el = dict_perimeter[3][idx]
        if current_el[1] != col:
            row, col = current_el
            sides += 1
        if abs(row-current_el[0]) > 1:
            sides += 1
        row = current_el[0]

    return len(block), sides


if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    garden_map = [list(l.strip()) for l in puzzle_input.readlines()]
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # top, down, right, left
    total = 0
    dict_map = {}
    for row in range(len(garden_map)):
        for col in range(len(garden_map[0])):
            current_type = garden_map[row][col]
            if current_type not in dict_map:
                dict_map[current_type] = []
            dict_map[current_type].append((row, col))

    for current_type in dict_map:
        if current_type == 'F':
            print('DEBUG')
        current_plots = dict_map[current_type]
        dict_separate = {0: [current_plots[0]]}
        count = 0
        open_list = current_plots[1:]
        for cp in current_plots:
            if all([cp not in dict_separate[c] for c in dict_separate]):
                count += 1
                dict_separate[count] = [cp]
                open_list.remove(cp)
            dict_separate[count], open_list = get_neighbors(dict_separate[count], open_list, cp)

        for block in dict_separate:
            current_block = dict_separate[block]
            area, perimeter_len = get_area_sides(current_block)
            total += area * perimeter_len
            print(f"{current_type}: {area} x {perimeter_len} = {area*perimeter_len}")
    print(total)

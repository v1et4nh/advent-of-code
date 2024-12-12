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


if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    garden_map = [list(l.strip()) for l in puzzle_input.readlines()]
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    total = 0
    dict_map = {}
    for row in range(len(garden_map)):
        for col in range(len(garden_map[0])):
            current_type = garden_map[row][col]
            if current_type not in dict_map:
                dict_map[current_type] = []
            dict_map[current_type].append((row, col))

    for current_type in dict_map:
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
            area, perimeter_len = get_area_perimeter(current_block)
            total += area * perimeter_len
    print(total)

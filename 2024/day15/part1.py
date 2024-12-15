def print_maps(maps):
    for row in maps:
        print(''.join(row))


if __name__ == '__main__':
    # puzzle_input = open('example.txt', 'r')
    puzzle_input = open('input.txt', 'r')
    lines = [l.strip() for l in puzzle_input.readlines()]
    maps = []
    for idx, row in enumerate(lines):
        if row == '':
            idx = idx + 1
            break
        if '@' in row:
            start = [idx, row.find('@')]
        maps.append(list(row))
    movements = ''.join([lines[i] for i in range(idx, len(lines))])

    dict_direction = {'>': [0, 1], 'v': [1, 0], '<': [0, -1], '^': [-1, 0]}
    pos = start
    print("Start: ")
    print_maps(maps)
    for m in movements:
        direction = dict_direction[m]
        new_pos = [pos[0]+direction[0], pos[1]+direction[1]]

        if maps[new_pos[0]][new_pos[1]] == '#':
            continue
        elif maps[new_pos[0]][new_pos[1]] == '.':
            maps[new_pos[0]][new_pos[1]] = '@'
            maps[pos[0]][pos[1]] = '.'
            pos = new_pos.copy()
        elif maps[new_pos[0]][new_pos[1]] == 'O':
            box_pos = new_pos.copy()
            new_box_pos = box_pos.copy()
            while maps[new_box_pos[0]][new_box_pos[1]] not in ['#', '.']:
                new_box_pos = [box_pos[0]+direction[0], box_pos[1]+direction[1]]
                box_pos = new_box_pos.copy()
            if maps[new_box_pos[0]][new_box_pos[1]] == '#':
                continue
            elif maps[new_box_pos[0]][new_box_pos[1]] == '.':
                maps[new_box_pos[0]][new_box_pos[1]] = 'O'
                maps[new_pos[0]][new_pos[1]] = '@'
                maps[pos[0]][pos[1]] = '.'
                pos = new_pos.copy()
        print(f"Movement {m}: ")
        print_maps(maps)

    total = 0
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'O':
                total += 100 * row + col
    print(total)
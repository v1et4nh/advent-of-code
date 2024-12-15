def print_maps(maps):
    for row in maps:
        print(''.join(row))


def get_new_maps(maps):
    new_maps = []
    for row in range(len(maps)):
        new_row = ''
        for col in range(len(maps[0])):
            if maps[row][col] == '#':
                new_row += '##'
            if maps[row][col] == 'O':
                new_row += '[]'
            if maps[row][col] == '.':
                new_row += '..'
            if maps[row][col] == '@':
                new_row += '@.'
        new_maps.append(list(new_row))
    return new_maps


if __name__ == '__main__':
    puzzle_input = open('example.txt', 'r')
    # puzzle_input = open('input.txt', 'r')
    lines = [l.strip() for l in puzzle_input.readlines()]
    maps = []
    for idx, row in enumerate(lines):
        if row == '':
            idx = idx + 1
            break
        maps.append(list(row))
    movements = ''.join([lines[i] for i in range(idx, len(lines))])

    new_maps = get_new_maps(maps)
    maps = new_maps
    for idx, row in enumerate(new_maps):
        if '@' in row:
            start = [idx, row.index('@')]
    print_maps(maps)

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
        else:
            if m in ['<', '>']:
                box_pos = new_pos.copy()
                new_box_pos = box_pos.copy()
                while maps[new_box_pos[0]][new_box_pos[1]] not in ['#', '.']:
                    new_box_pos = [box_pos[0]+direction[0], box_pos[1]+direction[1]]
                    box_pos = new_box_pos.copy()
                if maps[new_box_pos[0]][new_box_pos[1]] == '#':
                    continue
                maps[new_pos[0]][new_pos[1]] = '@'
                maps[pos[0]][pos[1]] = '.'
                box_pos = new_pos.copy()
                new_box_pos = box_pos.copy()
                while maps[new_box_pos[0]][new_box_pos[1]] not in ['#', '.']:
                    new_box_pos = [box_pos[0] + direction[0], box_pos[1] + direction[1]]
                    if maps[new_box_pos[0]][new_box_pos[1]] == ']':
                        maps[new_box_pos[0]][new_box_pos[1]] = '['
                    elif maps[new_box_pos[0]][new_box_pos[1]] == '[':
                        maps[new_box_pos[0]][new_box_pos[1]] = ']'
                    box_pos = new_box_pos.copy()
                if m == '<':
                    maps[new_box_pos[0]][new_box_pos[1]] = '['
                if m == '>':
                    maps[new_box_pos[0]][new_box_pos[1]] = ']'
                pos = new_pos.copy()
            elif m in ['^', 'v']:
                box_list = [new_pos]
                if maps[new_pos[0]][new_pos[1]] == ']':
                    box_list.append([new_pos[0], new_pos[1]-1])
                elif maps[new_pos[0]][new_pos[1]] == '[':
                    box_list.append([new_pos[0], new_pos[1]+1])
                new_box_list = box_list.copy()
                ended = False
                moveable = True
                while not ended:
                    for box in new_box_list:
                        tmp_list = []
                        if maps[box[0]][box[1]] == '#':
                            ended = True
                            moveable = False
                            break
                        elif maps[box[0]][box[1]] == '.':
                            continue
                        else:
                            new_box_list.append([box[0]+direction[0], box[1]+direction[1]])
                            box_list.append([box[0]+direction[0], box[1]+direction[1]])
                    new_box_list = tmp_list.copy()
                    if len(new_box_list) == 0:
                        ended = True
                        moveable = True
                if not moveable:
                    continue
                tmp_maps = maps.copy()
                current_pos = box_list.pop(0)
                tmp_maps[current_pos[0]][current_pos[1]] = '@'
                current_pos = box_list.pop(0)
                tmp_maps[current_pos[0]][current_pos[1]] = '.'
                while len(box_list) > 0:
                    current_pos = box_list.pop(-1)

                    tmp_maps[new_pos[0]][new_pos[1]] = '@'
                maps[pos[0]][pos[1]] = '.'



        print(f"Movement {m}: ")
        print_maps(maps)

    total = 0
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'O':
                total += 100 * row + col
    print(total)
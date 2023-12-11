from numpy import subtract

if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    # double row
    new_lines = []
    for l in lines:
        new_lines.append(l)
        if list(set(l)) == ['.']:
            new_lines.append(l)
    lines = new_lines.copy()
    # double col
    idx_arr = []
    new_lines = ['' for j in range(len(lines))]
    for i in range(len(lines[0])):
        if list(set(''.join([row[i] for row in lines]))) == ['.']:
            idx_arr.append(i)
            for j in range(len(lines)):
                new_lines[j] += lines[j][i]*2
        else:
            for j in range(len(lines)):
                new_lines[j] += lines[j][i]

    # get index of #
    count = 1
    map_dict = {}
    for i in range(len(new_lines)):
        for j in range(len(new_lines[i])):
            if new_lines[i][j] == '#':
                map_dict[count] = (i, j)
                count += 1

    total_sum = 0
    for i in map_dict:
        for j in range(i+1, len(map_dict)+1):
            # print(f"{map_dict[i]}-{map_dict[j]}")
            total_sum += sum(abs(subtract(map_dict[i], map_dict[j])))
    print(total_sum)

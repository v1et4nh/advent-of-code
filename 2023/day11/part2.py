from numpy import subtract

if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    orig_lines = lines.copy()

    # double row
    new_lines = []
    for l in lines:
        new_lines.append(l)
        if list(set(l)) == ['.']:
            for i in range(2-1):
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
    total_diff = []
    for i in map_dict:
        for j in range(i+1, len(map_dict)+1):
            # print(f"{map_dict[i]}-{map_dict[j]}")
            total_sum += sum(abs(subtract(map_dict[i], map_dict[j])))
            total_diff.append(tuple(abs(subtract(map_dict[i], map_dict[j]))))

    # get index of #
    count = 1
    map_dict_orig = {}
    for i in range(len(orig_lines)):
        for j in range(len(orig_lines[i])):
            if orig_lines[i][j] == '#':
                map_dict_orig[count] = (i, j)
                count += 1

    total_sum_orig = 0
    total_diff_orig = []
    for i in map_dict_orig:
        for j in range(i+1, len(map_dict_orig)+1):
            total_sum_orig += sum(abs(subtract(map_dict_orig[i], map_dict_orig[j])))
            total_diff_orig.append(tuple(abs(subtract(map_dict_orig[i], map_dict_orig[j]))))

    row_diff = 0
    col_diff = 0

    map_diff = {}
    for i in range(len(total_diff)):
        row_diff += abs(subtract(total_diff[i], total_diff_orig[i]))[0]
        col_diff += abs(subtract(total_diff[i], total_diff_orig[i]))[1]

    age = 1000000
    solution = total_sum_orig + int(row_diff) * (age-1) + int(col_diff) * (age-1)
    print(solution)

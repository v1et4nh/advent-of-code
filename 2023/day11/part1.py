from numpy import subtract

if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        data = [l.strip() for l in file]

    # double row
    new_data = []
    for l in data:
        new_data.append(l)
        if list(set(l)) == ['.']:
            new_data.append(l)
    data = new_data.copy()
    # double col
    idx_arr = []
    new_lines = ['' for j in range(len(data))]
    for i in range(len(data[0])):
        if list(set(''.join([row[i] for row in data]))) == ['.']:
            idx_arr.append(i)
            for j in range(len(data)):
                new_lines[j] += data[j][i]*2
        else:
            for j in range(len(data)):
                new_lines[j] += data[j][i]

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

from copy import deepcopy


def get_sum(lines, row):
    return sum([int(l[row]) for l in lines])


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [line.replace('\n', '') for line in lines]
    row_len = len(lines[0])
    col_len = len(lines)
    total_sum = [0 for i in range(row_len)]

    oxygen = deepcopy(lines)
    co2    = deepcopy(lines)
    for i in range(row_len):
        oxygen_sum = get_sum(oxygen, i)
        if oxygen_sum >= len(oxygen) / 2:
            oxygen = [line for line in oxygen if line[i] == '1']
        else:
            oxygen = [line for line in oxygen if line[i] == '0']
        if len(oxygen) == 1:
            oxygen = oxygen[0]
            break
    for i in range(row_len):
        co2_sum = get_sum(co2, i)
        if co2_sum >= len(co2) / 2:
            co2 = [line for line in co2 if line[i] == '0']
        else:
            co2 = [line for line in co2 if line[i] == '1']
        if len(co2) == 1:
            co2 = co2[0]
            break

    print(int(oxygen, 2) * int(co2, 2))
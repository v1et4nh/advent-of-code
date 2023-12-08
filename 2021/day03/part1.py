if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [line.replace('\n', '') for line in lines]
    row_len = len(lines[0])
    col_len = len(lines)
    total_sum = [0 for i in range(row_len)]
    for line in lines:
        for i, val in enumerate(line):
            total_sum[i] += int(val)
    # dec_arr = [int(line, 2) for line in lines]
    gamma = ''
    epsilon = ''
    for i in total_sum:
        if i >= col_len//2:
            gamma   += '1'
            epsilon += '0'
        else:
            gamma   += '0'
            epsilon += '1'

    total_sum = int(gamma, 2) * int(epsilon, 2)
    print(total_sum)
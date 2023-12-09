import numpy as np


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [line.replace('\n', '') for line in lines]
    total_sum = 0
    for line in lines:
        diff_arr = [list([int(l) for l in line.split(' ')])]
        tmp_diff = list(np.diff(diff_arr[-1]))
        while not all(x == 0 for x in tmp_diff):
            diff_arr.append(tmp_diff)
            tmp_diff = list(np.diff(diff_arr[-1]))
        diff_arr.append(list(np.diff(diff_arr[-1])))
        for i in reversed(range(1, len(diff_arr))):
            val1 = diff_arr[i-1][-1]
            val2 = diff_arr[i][-1]
            diff_arr[i-1].append(val1+val2)
        total_sum += diff_arr[0][-1]

    print(total_sum)
import numpy as np


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    data = [d.replace('\n', '') for d in data]
    total_sum = 0
    for d in data:
        diff_arr = [list([int(l) for l in d.split(' ')])]
        tmp_diff = list(np.diff(diff_arr[-1]))
        while not all(x == 0 for x in tmp_diff):
            diff_arr.append(tmp_diff)
            tmp_diff = list(np.diff(diff_arr[-1]))
        diff_arr.append(list(np.diff(diff_arr[-1])))
        for i in reversed(range(1, len(diff_arr))):
            val1 = diff_arr[i-1][0]
            val2 = diff_arr[i][0]
            diff_arr[i-1].insert(0, val1-val2)
        total_sum += diff_arr[0][0]

    print(total_sum)
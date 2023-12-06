import numpy as np


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(line.replace('\n', '')) for line in lines]
    lines_diff = np.diff(lines)
    count = 0
    for i in lines_diff:
        if i > 0:
            count += 1
    print(count)
import numpy as np


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(line.replace('\n', '')) for line in lines]
    new_lines = [sum(lines[i:i+3]) for i in range(len(lines)-2)]
    lines_diff = np.diff(new_lines)
    count = 0
    for i in lines_diff:
        if i > 0:
            count += 1
    print(count)
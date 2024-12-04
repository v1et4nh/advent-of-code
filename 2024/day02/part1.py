import numpy as np

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    total = 0
    for l in lines:
        num_list = [int(num) for num in l.strip().split(' ')]
        d_list = np.diff(num_list)
        if (d_list > -4).all() & (d_list < 0).all() or (d_list < 4).all() & (d_list > 0).all():
            total += 1
    print(total)
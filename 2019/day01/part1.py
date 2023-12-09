if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        total_sum += int(int(line) / 3) - 2
    print(total_sum)
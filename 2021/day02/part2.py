if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    horizontal = 0
    depth      = 0
    aim        = 0
    for line in lines:
        line = line.replace('\n', '').split(' ')
        move_type = line[0]
        value     = int(line[1])
        if move_type == 'forward':
            depth += aim * value
            horizontal += value
        if move_type == 'down':
            aim += value
        if move_type == 'up':
            aim -= value
    print(horizontal*depth)
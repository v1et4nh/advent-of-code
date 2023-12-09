if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    line = puzzle_input.readlines()[0]
    instructions = line.split(', ')
    direction    = ['up', 'right', 'down', 'left']
    current_d    = 0
    horizontal   = 0
    vertical     = 0
    for step in instructions:
        turn = step[0]
        steps = int(step[1:])
        if turn == 'L':
            current_d -= 1
            if current_d == -1:
                current_d = 3
        if turn == 'R':
            current_d += 1
            if current_d == 4:
                current_d = 0
        if current_d == 0:
            vertical += steps
        elif current_d == 1:
            horizontal += steps
        elif current_d == 2:
            vertical -= steps
        elif current_d == 3:
            horizontal -= steps
    print(abs(horizontal)+abs(vertical))
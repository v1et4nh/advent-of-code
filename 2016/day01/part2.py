if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    line = puzzle_input.readlines()[0]
    instructions = line.split(', ')
    direction    = ['up', 'right', 'down', 'left']
    current_d    = 0
    current_p = (0, 0)
    visit_arr = [current_p]
    is_found  = False
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
        for i in range(steps):
            if current_d == 0:
                current_p = (current_p[0]+1, current_p[1])
            elif current_d == 1:
                current_p = (current_p[0], current_p[1]+1)
            elif current_d == 2:
                current_p = (current_p[0]-1, current_p[1])
            elif current_d == 3:
                current_p = (current_p[0], current_p[1]-1)
            if current_p in visit_arr:
                print(abs(current_p[0])+abs(current_p[1]))
                is_found = True
                break
            else:
                visit_arr.append(current_p)
        if is_found:
            break

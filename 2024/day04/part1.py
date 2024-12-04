if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [list(line.strip()) for line in lines]
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = lines[i][j]
            for d in direction:
                pos = (i, j)
                if current == 'X':
                    pos = (pos[0] + d[0], pos[1] + d[1])
                    if pos[0] < 0 or pos[0] > len(lines[0])-1 or pos[1] < 0 or pos[1] > len(lines)-1:
                        continue
                    tmp = lines[pos[0]][pos[1]]
                    if tmp == 'M':
                        pos = (pos[0] + d[0], pos[1] + d[1])
                        if pos[0] < 0 or pos[0] > len(lines[0]) - 1 or pos[1] < 0 or pos[1] > len(lines) - 1:
                            continue
                        tmp = lines[pos[0]][pos[1]]
                        if tmp == 'A':
                            pos = (pos[0] + d[0], pos[1] + d[1])
                            if pos[0] < 0 or pos[0] > len(lines[0]) - 1 or pos[1] < 0 or pos[1] > len(lines) - 1:
                                continue
                            tmp = lines[pos[0]][pos[1]]
                            if tmp == 'S':
                                total += 1
    print(total)

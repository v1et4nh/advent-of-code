from copy import deepcopy


if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [list(line.strip()) for line in lines]
    direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0
    A_pos = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = lines[i][j]
            for d in direction:
                pos = (i, j)
                if current == 'M':
                    pos = (pos[0] + d[0], pos[1] + d[1])
                    if pos[0] < 0 or pos[0] > len(lines[0])-1 or pos[1] < 0 or pos[1] > len(lines)-1:
                        continue
                    tmp = lines[pos[0]][pos[1]]
                    if tmp == 'A':
                        tmp_a_pos = deepcopy(pos)
                        pos = (pos[0] + d[0], pos[1] + d[1])
                        if pos[0] < 0 or pos[0] > len(lines[0]) - 1 or pos[1] < 0 or pos[1] > len(lines) - 1:
                            continue
                        tmp = lines[pos[0]][pos[1]]
                        if tmp == 'S':
                            A_pos.append(tmp_a_pos)
    total = len(set([a for a in A_pos if A_pos.count(a) == 2]))
    print(total)

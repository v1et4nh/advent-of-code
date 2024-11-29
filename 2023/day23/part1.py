from numpy import add


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    start   = (0, lines[0].find('.'))
    end     = (len(lines)-1, lines[len(lines)-1].find('.'))
    visited = [[start]]

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    current_pos = start
    i = 0
    while True:
        while current_pos != end:
            path = []
            for d in direction:
                next_pos = tuple(add(current_pos, d))
                if next_pos[0] < 0 or next_pos[1] < 0:
                    continue
                if next_pos in visited[i] or next_pos == '#':
                    continue
                if lines[next_pos[0]][next_pos[1]] == '.':
                    visited[i].append(next_pos)
                    current_pos = next_pos
                    break

                if lines[next_pos[0]][next_pos[1]] == '^':
                    if d == (1, 0):
                        continue
                    path.append([next_pos, tuple(add(next_pos, (-1, 0)))])
                if lines[next_pos[0]][next_pos[1]] == 'v':
                    if d == (-1, 0):
                        continue
                    path.append([next_pos, tuple(add(next_pos, (1, 0)))])
                if lines[next_pos[0]][next_pos[1]] == '<':
                    if d == (0, 1):
                        continue
                    path.append([next_pos, tuple(add(next_pos, (0, -1)))])
                if lines[next_pos[0]][next_pos[1]] == '>':
                    if d == (0, -1):
                        continue
                    path.append([next_pos, tuple(add(next_pos, (0, 1)))])

            if len(path) == 0:
                continue
            if len(path) == 1:
                visited[i].extend(path[0])
                current_pos = visited[i][-1]
            if len(path) >= 2:
                for p in path[1:]:
                    tmp_visited = visited[i] + p
                    visited.append(tmp_visited)
                visited[i].extend(path[0])
                current_pos = visited[i][-1]
        i += 1
        if i == len(visited):
            break
        current_pos = visited[i][-1]

    print(max([len(v) for v in visited])-1)
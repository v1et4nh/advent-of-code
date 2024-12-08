def get_visited_list(lines):
    start = [(row, s.find('^')) for row, s in enumerate(lines) if '^' in s][0]
    visit_list = [start]
    pos = start
    last_pos = pos
    ongoing = True
    while ongoing:
        for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            pos = (pos[0] + d[0], pos[1] + d[1])
            while True:
                if not ((0 <= pos[0] < len(lines)) and (0 <= pos[1] < len(lines[0]))):
                    ongoing = False
                    break
                if lines[pos[0]][pos[1]] in ['.', '^']:
                    visit_list.append(pos)
                    last_pos = pos
                    pos = (pos[0] + d[0], pos[1] + d[1])  # going forward
                else:  # change direction
                    pos = last_pos
                    break
    return list(set(visit_list))

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [el.strip() for el in lines]
    print(len(get_visited_list(lines)))

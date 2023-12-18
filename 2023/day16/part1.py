from numpy import add

if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]
    print('')
    beams         = [[(0, -1), (0, 1)]]
    beams_history = []
    visited       = [(0, 0)]
    still_moving = True
    while beams:
        current_pos, direction = beams[0]
        beams.pop(0)
        current_pos = tuple(add(current_pos, direction))
        if current_pos[0] < 0 or current_pos[0] == len(lines) or current_pos[1] < 0 or current_pos[1] == len(lines[0]):
            continue
        tile = lines[current_pos[0]][current_pos[1]]
        if current_pos not in visited:
            visited.append(current_pos)
        if tile == '.':
            if [current_pos, direction] not in beams_history:
                beams.append([current_pos, direction])
                beams_history.append([current_pos, direction])
        elif tile == '|':
            if direction in [(0, 1), (0, -1)]:
                if [current_pos, (-1, 0)] not in beams_history:
                    beams.append([current_pos, (-1, 0)])
                    beams_history.append([current_pos, (-1, 0)])
                if [current_pos, (1, 0)] not in beams_history:
                    beams.append([current_pos, (1, 0)])
                    beams_history.append([current_pos, (1, 0)])
            if direction in [(1, 0), (-1, 0)]:
                if [current_pos, direction] not in beams_history:
                    beams.append([current_pos, direction])
                    beams_history.append([current_pos, direction])
        elif tile == '-':
            if direction in [(0, 1), (0, -1)]:
                if [current_pos, direction] not in beams_history:
                    beams.append([current_pos, direction])
                    beams_history.append([current_pos, direction])
            if direction in [(1, 0), (-1, 0)]:
                if [current_pos, (0, 1)] not in beams_history:
                    beams.append([current_pos, (0, 1)])
                    beams_history.append([current_pos, (0, 1)])
                if [current_pos, (0, -1)] not in beams_history:
                    beams.append([current_pos, (0, -1)])
                    beams_history.append([current_pos, (0, -1)])
        elif tile == '/':
            if direction == (0, 1):
                if [current_pos, (-1, 0)] not in beams_history:
                    beams.append([current_pos, (-1, 0)])
                    beams_history.append([current_pos, (-1, 0)])
            if direction == (0, -1):
                if [current_pos, (1, 0)] not in beams_history:
                    beams.append([current_pos, (1, 0)])
                    beams_history.append([current_pos, (1, 0)])
            if direction == (1, 0):
                if [current_pos, (0, -1)] not in beams_history:
                    beams.append([current_pos, (0, -1)])
                    beams_history.append([current_pos, (0, -1)])
            if direction == (-1, 0):
                if [current_pos, (0, 1)] not in beams_history:
                    beams.append([current_pos, (0, 1)])
                    beams_history.append([current_pos, (0, 1)])
        elif tile == '\\':
            if direction == (0, 1):
                if [current_pos, (1, 0)] not in beams_history:
                    beams.append([current_pos, (1, 0)])
                    beams_history.append([current_pos, (1, 0)])
            if direction == (0, -1):
                if [current_pos, (-1, 0)] not in beams_history:
                    beams.append([current_pos, (-1, 0)])
                    beams_history.append([current_pos, (-1, 0)])
            if direction == (1, 0):
                if [current_pos, (0, 1)] not in beams_history:
                    beams.append([current_pos, (0, 1)])
                    beams_history.append([current_pos, (0, 1)])
            if direction == (-1, 0):
                if [current_pos, (0, -1)] not in beams_history:
                    beams.append([current_pos, (0, -1)])
                    beams_history.append([current_pos, (0, -1)])

    print(len(visited))
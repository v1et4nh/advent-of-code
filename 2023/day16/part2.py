from numpy import add
from tqdm import tqdm


def get_visited(beams, lines):
    beams_history = []
    visited = []
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

    return len(visited)


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]
    print('')
    visited_max = 0
    for i in tqdm(range(len(lines))):
        visited_max = max(visited_max, get_visited([[(i, -1), (0, 1)]], lines))
        visited_max = max(visited_max, get_visited([[(i, len(lines[0])), (0, -1)]], lines))
    for i in tqdm(range(len(lines[0]))):
        visited_max = max(visited_max, get_visited([[(-1, i), (1, 0)]], lines))
        visited_max = max(visited_max, get_visited([[(len(lines[0]), i), (-1, 0)]], lines))
    print(visited_max)
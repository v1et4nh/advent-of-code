from numpy import add
from tqdm import tqdm


def shoelace(xy):
    xy.append(xy[0])
    area = 0.0
    for i in range(len(xy)-1):
        area += float(xy[i][0]) * float(xy[i+1][1]) - float(xy[i][1]) * float(xy[i+1][0])

    return abs((area*0.5))


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    current       = (0, 0)
    coordinates   = []
    direction_map = ['R', 'D', 'L', 'U']
    for l in tqdm(lines):
        _, _, color = l.split(' ')
        color = color.replace('(', '').replace(')', '').replace('#', '')
        steps = int(color[:5], 16)
        direction = direction_map[int(color[-1])]
        if direction == 'R':
            for _ in range(int(steps)):
                current = add(current, (0, 1))
                coordinates.append(current)
        elif direction == 'L':
            for _ in range(int(steps)):
                current = add(current, (0, -1))
                coordinates.append(current)
        elif direction == 'D':
            for _ in range(int(steps)):
                current = add(current, (1, 0))
                coordinates.append(current)
        elif direction == 'U':
            for _ in range(int(steps)):
                current = add(current, (-1, 0))
                coordinates.append(current)

    area = shoelace(coordinates)
    area = int(area + int(len(coordinates)/2)) + 1  # Pick's Theorem

    print(area)
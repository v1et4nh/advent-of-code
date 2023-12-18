from numpy import add


def shoelace(xy_coords):
    xy_coords.append(xy_coords[0])
    xy = xy_coords
    area = 0
    for i in range(len(xy)-1):
        area += xy[i][0] * xy[i+1][1] - xy[i][1]*xy[i+1][0]

    return abs(int(area*0.5))


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    current = (0, 0)
    coordinates = []
    for l in lines:
        direction, steps, color = l.split(' ')
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
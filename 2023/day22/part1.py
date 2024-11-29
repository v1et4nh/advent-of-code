from numpy import add


def is_within(b1, b2):
    return any(b2[0] <= x <= b2[1] or b2[0] <= x <= b2[1] for x in range(b1[0], b1[1]+1))


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    occupied_grid  = []
    grid_mapping   = {}
    brick_mapping  = {}
    lines.sort(key=lambda x: (int(x.split('~')[0].split(',')[-1]), int(x.split('~')[0].split(',')[-0])))
    max_z = max([int(x.split('~')[0].split(',')[-1]) for x in lines])
    bricks_arr = [[] for _ in range(max_z)]
    for b, l in enumerate(lines):
        l1, l2     = l.split('~')
        x1, y1, z1 = l1.split(',')
        x2, y2, z2 = l2.split(',')
        x_range = (int(x1), int(x2))
        y_range = (int(y1), int(y2))
        z_range = (int(z1), int(z2))

        coords = []
        # x-y-Coords for 1 level
        for i in range(x_range[0], x_range[1]+1):
            for j in range(y_range[0], y_range[1]+1):
                coords.append((i, j))

        # Check if any same coord is 1 level below current level
        # Yes: add coords to current level
        # No: reduce z by 1 level
        still_falling = True
        while still_falling:
            if any(c in bricks_arr[z_range[0]-1] for c in coords) or z_range[0]-1 == 0:
                for z in range(z_range[0], z_range[1]+1):
                    for c in coords:
                        bricks_arr[z].append(c)
                        occupied_grid.append((c[0], c[1], z))
                        grid_mapping[(c[0], c[1], z)] = b
                        if b not in brick_mapping:
                            brick_mapping[b] = []
                        brick_mapping[b].append((c[0], c[1], z))
                still_falling = False
            else:
                z_range = tuple(add(z_range, (-1, -1)))

    # get bricks
    brick_brick = {}
    brick_support = []
    for k in brick_mapping:
        for c in brick_mapping[k]:
            # get every attached brick and safe it to brick
            c_down = (c[0], c[1], c[2]-1)
            if c_down[2] == 0:
                brick_brick[k] = []
            if c_down in grid_mapping:
                if k not in brick_brick:
                    brick_brick[k] = []
                if k != grid_mapping[c_down] and grid_mapping[c_down] not in brick_brick[k]:
                    brick_brick[k].append(grid_mapping[c_down])
                    brick_support.append(grid_mapping[c_down])

    brick_support = list(set(brick_support))
    bricks = []
    single_support = []
    for k in brick_brick:
        if len(brick_brick[k]) == 1:
            single_support.append(brick_brick[k][0])

    for k in brick_brick:
        if len(brick_brick[k]) >= 2:
            bricks.extend(b for b in brick_brick[k] if b not in single_support)
        if k not in brick_support:
            bricks.append(k)

    bricks = set(bricks)
    print(len(bricks))
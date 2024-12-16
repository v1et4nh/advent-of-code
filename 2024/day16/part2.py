if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = [l.strip() for l in puzzle_input.readlines()]
    maps = [list(l) for l in lines]
    start, end = None, None
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'S':
                start = (row, col)
            elif maps[row][col] == 'E':
                end = (row, col)
    directions = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }
    rotation_cost = {
        ("N", "E"): 1000, ("N", "W"): 1000, ("N", "S"): 2000,
        ("E", "N"): 1000, ("E", "S"): 1000, ("E", "W"): 2000,
        ("S", "E"): 1000, ("S", "W"): 1000, ("S", "N"): 2000,
        ("W", "N"): 1000, ("W", "S"): 1000, ("W", "E"): 2000,
        ("N", "N"): 0, ("E", "E"): 0, ("S", "S"): 0, ("W", "W"): 0
    }

    queue = [(0, start[0], start[1], 'E', [start])]   # [(cost, x, y, direction)]
    visited = {}
    all_path = {}
    count = 0
    while queue:
        print(len(queue))
        queue.sort(key=lambda x: x[0])  # sort by cost-value
        cost, x, y, direction, path = queue.pop(0)

        if (x, y) == end:
            count += 1
            all_path[count] = {'path': path, 'cost': cost}
            continue

        if (x, y, direction) in visited:
            if visited[(x, y, direction)] < cost:
                continue
        visited[(x, y, direction)] = cost

        for new_direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "#" and (nx, ny) not in path:
                move_cost = 1
                turn_cost = rotation_cost[(direction, new_direction)]
                total_cost = cost + move_cost + turn_cost
                queue.append((total_cost, nx, ny, new_direction, path + [(nx, ny)]))

    # sort dict
    sorted_paths = dict(sorted(all_path.items(), key=lambda item: item[1]['cost']))
    lowest_cost = list(sorted_paths.values())[0]['cost']
    unique_tiles = []
    for value in sorted_paths.values():
        if value['cost'] > lowest_cost:
            break
        unique_tiles.extend(value['path'])

    print(len(list(set(unique_tiles))))
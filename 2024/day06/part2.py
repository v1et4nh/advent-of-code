import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib.animation import FuncAnimation

import matplotlib
matplotlib.use('TkAgg')

from part1 import get_visited_list

enable_plot = False

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [el.strip() for el in lines]
    visited_list = get_visited_list(lines)  # from part 1

    # Fill map with obstacles
    map_size = (len(lines), len(lines[0]))
    map_data = [[1 if char == '#' else 0 for char in line] for line in lines]

    start = [(row, s.find('^')) for row, s in enumerate(lines) if '^' in s][0]

    total = 0
    for obstacle in tqdm(visited_list):
        map_data[obstacle[0]][obstacle[1]] = 1
        movements = []
        corner_list = []
        pos = start
        last_pos = start
        path = [start]
        ongoing = True
        while ongoing:
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                pos = (pos[0] + d[0], pos[1] + d[1])
                if not ongoing:
                    break
                while True:
                    if not ((0 <= pos[0] < len(lines)) and (0 <= pos[1] < len(lines[0]))):
                        ongoing = False
                        break
                    if map_data[pos[0]][pos[1]] == 0:
                        path.append(pos)
                        movements.append(d)
                        last_pos = pos
                        pos = (pos[0] + d[0], pos[1] + d[1])
                    else:
                        pos = last_pos
                        corner_list.append(pos)
                        if corner_list.count(pos) > 2:
                            total += 1
                            ongoing = False
                        break

        ### Plot ###
        if enable_plot:
            fig, ax = plt.subplots()
            ax.set_xlim(0, map_size[1])
            ax.set_ylim(0, map_size[0])
            ax.set_xticks(range(map_size[1] + 1))
            ax.set_yticks(range(map_size[0] + 1))
            ax.grid(True)

            # Draw Obstacles
            for x in range(map_size[0]):
                for y in range(map_size[1]):
                    if map_data[x][y] == 1:
                        ax.add_patch(plt.Rectangle((y, map_size[0] - x - 1), 1, 1, color='black'))
            ax.plot(obstacle[1] + 0.5, map_size[0] - obstacle[0] - 0.5, marker='*', color='yellow', markersize=10)

            # Current Position
            point, = ax.plot([], [], 'ro', markersize=10)

            # Visited path
            line, = ax.plot([], [], 'r-', linewidth=2)

            def update(frame):
                current_position = path[frame]
                # Draw current position
                point.set_data([current_position[1] + 0.5], [map_size[0] - current_position[0] - 0.5])

                # Draw visited path
                x_data = [p[1] + 0.5 for p in path[:frame + 1]]
                y_data = [map_size[0] - p[0] - 0.5 for p in path[:frame + 1]]
                line.set_data(x_data, y_data)
                return point, line

            ani = FuncAnimation(fig, update, frames=len(path), interval=0.01, blit=True)

            plt.show()
            plt.close()

        # Reset obstacle
        map_data[obstacle[0]][obstacle[1]] = 0
    print(f"Total: {total}")
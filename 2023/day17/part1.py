from numpy import add


if __name__ == '__main__':
    with open('puzzle_input_example.txt', 'r') as file:
        lines = [list(map(int, list(l.strip()))) for l in file]

    explored = []
    queue    = [[(0, 0)]]
    goal     = [(len(lines)-1, len(lines[0])-1)]


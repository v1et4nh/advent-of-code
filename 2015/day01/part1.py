if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()[0]
    print(lines.count('(')-lines.count(')'))
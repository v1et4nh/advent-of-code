if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(line) for line in lines]
    print(sum(lines))
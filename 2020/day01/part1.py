if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(l.replace('\n', '')) for l in lines]
    for l in lines:
        if 2020-l in lines:
            print((2020-l)*l)
            break
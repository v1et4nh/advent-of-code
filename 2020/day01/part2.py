if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(l.replace('\n', '')) for l in lines]
    for l in lines:
        remaining = 2020 - l
        for k in lines:
            if remaining-k in lines:
                print(l*k*(remaining-k))
                break
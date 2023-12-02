if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    highest_total = 0
    tmp_total     = 0
    for line in lines:
        if line != '\n':
            tmp_total += int(line)
        else:
            if tmp_total > highest_total:
                highest_total = tmp_total
            tmp_total = 0
    print(highest_total)
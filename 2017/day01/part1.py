if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    line = puzzle_input.readlines()[0].replace('\n', '')
    total_sum = 0
    for i in range(len(line)):
        if i+1 == len(line):
            if line[i] == line[0]:
                total_sum += int(line[0])
        else:
            if line[i] == line[i+1]:
                total_sum += int(line[i])
    print(total_sum)
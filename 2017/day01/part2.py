if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    line = puzzle_input.readlines()[0].replace('\n', '')
    total_sum = 0
    first, second = line[:(len(line)//2)], line[(len(line)//2):]
    for i in range(len(first)):
        if first[i] == second[i]:
            total_sum += int(first[i]) * 2
    print(total_sum)
if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    tmp_total = 0
    total_array = []
    for line in lines:
        if line != '\n':
            tmp_total += int(line)
        else:
            total_array.append(tmp_total)
            tmp_total = 0
    total_array.sort(reverse=True)
    total_sum = sum(total_array[:3])
    print(total_sum)
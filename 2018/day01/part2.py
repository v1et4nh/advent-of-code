if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [int(line) for line in lines]
    sum_arr = []
    is_found = False
    current_sum = 0
    while not is_found:
        for i in range(len(lines)):
            current_sum += lines[i]
            if current_sum not in sum_arr:
                sum_arr.append(current_sum)
            else:
                is_found = True
                break
    print(current_sum)
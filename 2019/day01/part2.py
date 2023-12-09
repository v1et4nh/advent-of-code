if __name__ == '__main__':
    puzzle_input = open('puzzle_input_example.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        val = int(int(line) / 3) - 2
        total_sum += val
        while val > 0:
            val = int(int(val) / 3) - 2
            if val > 0:
                total_sum += val
    print(total_sum)
if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()[0]
    total_sum = 0
    for i, c in enumerate(lines):
        if c == '(':
            total_sum += 1
        elif c == ')':
            total_sum -= 1
        if total_sum == -1:
            print(i+1)
            break
if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [list(line.strip()) for line in lines]
    total = 0
    s = {'M', 'S'}
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            current = lines[i][j]
            if current == 'A':
                if {lines[i-1][j-1], lines[i+1][j+1]} == s and {lines[i-1][j+1], lines[i+1][j-1]} == s:
                    total += 1
    print(total)

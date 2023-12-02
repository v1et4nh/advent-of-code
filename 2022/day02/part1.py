def get_score(text_line):
    first, second = text_line.replace('\n', '').split(' ')
    if first == 'A':  # Rock
        if second == 'X':  # Rock
            return 1 + 3
        if second == 'Y':  # Paper
            return 2 + 6
        if second == 'Z':  # Scissor
            return 3 + 0
    if first == 'B':  # Paper
        if second == 'X':  # Rock
            return 1 + 0
        if second == 'Y':  # Paper
            return 2 + 3
        if second == 'Z':  # Scissor
            return 3 + 6
    if first == 'C':  # Scissor
        if second == 'X':  # Rock
            return 1 + 6
        if second == 'Y':  # Paper
            return 2 + 0
        if second == 'Z':  # Scissor
            return 3 + 3


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_score = 0
    for line in lines:
        score = get_score(line)
        total_score += score
    print(total_score)
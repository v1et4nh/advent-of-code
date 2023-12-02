def get_score(text_line):
    first, second = text_line.replace('\n', '').split(' ')
    if first == 'A':  # Rock
        if second == 'X':  # Lose: Scissor (3)
            return 0 + 3
        if second == 'Y':  # Draw: Rock (1)
            return 3 + 1
        if second == 'Z':  # Win: Paper (2)
            return 6 + 2
    if first == 'B':  # Paper
        if second == 'X':  # Lose: Rock (1)
            return 0 + 1
        if second == 'Y':  # Draw: Paper (2)
            return 3 + 2
        if second == 'Z':  # Win: Scissor (3)
            return 6 + 3
    if first == 'C':  # Scissor
        if second == 'X':  # Lose: Paper (2)
            return 0 + 2
        if second == 'Y':  # Draw: Scissor (3)
            return 3 + 3
        if second == 'Z':  # Win: Rock (1)
            return 6 + 1


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_score = 0
    for line in lines:
        score = get_score(line)
        total_score += score
    print(total_score)
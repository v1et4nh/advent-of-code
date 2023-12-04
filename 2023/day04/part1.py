if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        card_row, numbers_row = line.replace('\n', '').split(':')
        winning_row, my_row   = numbers_row.split('|')
        winning_row = winning_row.split(' ')
        my_row = my_row.split(' ')
        match = list(set(winning_row) & set(my_row))
        match.remove('')
        if len(match) > 0:
            total_sum += 2**(len(match)-1)

    print(total_sum)


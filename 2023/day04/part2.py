if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    winning_dict = {}
    for i in range(len(lines)):
        winning_dict[i+1] = 1

    for line in lines:
        card_row, numbers_row = line.replace('\n', '').split(':')
        card_row = int(card_row.replace('Card ', ''))
        winning_row, my_row   = numbers_row.split('|')
        winning_row = winning_row.split(' ')
        my_row = my_row.split(' ')
        match = list(set(winning_row) & set(my_row))
        match.remove('')
        if len(match) > 0:
            num_cards = winning_dict[card_row]
            for i in range(card_row, card_row + len(match)):
                winning_dict[i + 1] += 1 * num_cards

    total_sum = 0
    for i in winning_dict:
        total_sum += winning_dict[i]
    print(total_sum)


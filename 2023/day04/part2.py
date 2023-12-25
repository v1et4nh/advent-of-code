if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    winning_dict = {}
    for i in range(len(data)):
        winning_dict[i+1] = 1

    for d in data:
        card_row, numbers_row = d.replace('\n', '').split(':')
        card_row = int(card_row.replace('Card ', ''))
        winning_row, my_row   = numbers_row.split('|')
        winning_row = winning_row.split(' ')
        my_row = my_row.split(' ')
        match  = list(set(winning_row) & set(my_row))
        match.remove('')
        if len(match) > 0:
            num_cards = winning_dict[card_row]
            for i in range(card_row, card_row + len(match)):
                winning_dict[i + 1] += 1 * num_cards

    total_sum = 0
    for i in winning_dict:
        total_sum += winning_dict[i]
    print(total_sum)


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    data = [d.replace('\n', '') for d in data]
    max_rank = len(data)
    cards = []
    bids  = []
    type_arr = []
    for d in data:
        card, bid = d.split(' ')
        cards.append(card.replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('J', 'W'))
        bids.append(int(bid))
        if len(set(card)) == 1:  # Five of a kind
            type_arr.append(7)
        elif len(set(card)) == 2:
            if any([True for c in card if card.count(c) == 4]):
                type_arr.append(6)  # Four of a kind
            else:
                type_arr.append(5)  # Full House
        elif len(set(card)) == 3:
            if any([True for c in card if card.count(c) == 3]):
                type_arr.append(4)  # three of a kind
            else:
                type_arr.append(3)  # two pair
        elif len(set(card)) == 4:
            type_arr.append(2)      # one pair
        elif len(set(card)) == 5:
            type_arr.append(1)      # high card

    sorted_cards = [card for card, _, _ in sorted(zip(cards, bids, type_arr), key=lambda pair: (pair[2], pair[0]))]
    sorted_bids  = [bid for _, bid, _ in sorted(zip(cards, bids, type_arr), key=lambda pair: (pair[2], pair[0]))]
    sorted_hands = [hand for _, _, hand in sorted(zip(cards, bids, type_arr), key=lambda pair: (pair[2], pair[0]))]

    total_sum = 0
    for i, bid in enumerate(sorted_bids):
        total_sum += (i+1) * bid
    print(total_sum)

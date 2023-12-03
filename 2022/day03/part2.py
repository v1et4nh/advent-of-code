def get_priority(rucksack):
    prio = 0
    for i in range(0, len(rucksack), 3):
        tmp_set = rucksack[i:i+3]
        common_letter = list(set(tmp_set[0]) & set(tmp_set[1]) & set(tmp_set[2]))[0]
        if ord(common_letter) < 91:
            prio += ord(common_letter) - ord('A') + 27
        else:
            prio += ord(common_letter) - ord('a') + 1

    return prio


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    rucksack_arr = [line.replace('\n', '') for line in lines]
    total_sum = get_priority(rucksack_arr)
    print(total_sum)

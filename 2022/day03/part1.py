def get_priority(rucksack):
    # if len(rucksack) % 2 == 0:
    first  = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    common_letter = list(set(first) & set(second))[0]
    if ord(common_letter) < 91:
        prio = ord(common_letter) - ord('A') + 27
    else:
        prio = ord(common_letter) - ord('a') + 1

    return prio


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        priority = get_priority(line)
        total_sum += priority
    print(total_sum)

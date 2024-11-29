from functools import cache
from functools import lru_cache
from tqdm import tqdm


def get_valid_combi(springs, groups):
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0

    if springs[0] == '.':
        return get_valid_combi(springs.lstrip('.'), groups)
    elif springs[0 == '#':


@cache
def generate_combinations(groups, num_places, built_combi="", first_group=True):
    combinations_arr = []

    if not groups:  # all groups are placed
        if num_places >= 0:  # fill up the rest with '.'
            combinations_arr.append(built_combi + "." * num_places)
        return combinations_arr

    current_group_length = groups[0]

    start_gap = 0 if first_group else 1

    for gap in range(start_gap, num_places - current_group_length + 1):
        new_built_combi = built_combi + "." * gap + "#" * current_group_length
        new_num_places  = num_places - gap - current_group_length
        combinations_arr.extend(generate_combinations(groups[1:], new_num_places, new_built_combi, False))

    return combinations_arr


if __name__ == '__main__':
    with open('puzzle_input_example.txt', 'r') as file:
        lines = [l.strip() for l in file]

    total_sum = 0
    for l in tqdm(lines):
        tmp_combi = 0
        springs, groups = l.strip().split(' ')
        springs = (springs + '?') * 5
        springs = springs[:-1].split('.')
        springs = [el for el in springs if el != '']
        groups = (groups + ',') * 5
        groups = groups.split(',')
        groups = [int(el) for el in groups if el != '']
        if len(springs) > 1:
            springs = ['|'.join(springs)]
        springs = springs[0]

        combinations = generate_combinations_memo(groups, len(springs))
        for combi in combinations:
            tmp_1 = combi.replace('#', '1').replace('.', '0')
            tmp_2 = springs.replace('#', '1').replace('.', '0').replace('?', '0').replace('|', '2')
            if any((int(tmp_1[i]) - int(tmp_2[i])) == -1 for i in range(len(tmp_1))):
                continue
            else:
                tmp_combi += 1
        total_sum += tmp_combi

    print(total_sum)
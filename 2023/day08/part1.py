if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [line.replace('\n', '') for line in lines]
    instructions = lines[0].split()[0] * 10000000
    lines = lines[2:]
    map_dict = {}
    for line in lines:
        entry, steps = line.split(' = ')
        map_dict[entry] = steps.replace('(', '').replace(')', '').split(', ')
    current_entry = 'AAA'
    total_steps = 0
    for instruction in instructions:
        total_steps += 1
        if instruction == 'L':
            current_entry = map_dict[current_entry][0]
        else:
            current_entry = map_dict[current_entry][1]
        if current_entry == 'ZZZ':
            print('reached')
            break
    print(total_steps)

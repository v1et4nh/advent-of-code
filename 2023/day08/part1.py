if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    data = [d.replace('\n', '') for d in data]
    instructions = data[0].split()[0] * 10000000
    data = data[2:]
    map_dict = {}
    for d in data:
        entry, steps = d.split(' = ')
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

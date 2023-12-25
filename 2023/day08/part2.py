import math

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

    current_entry = [entry for entry in map_dict if entry[-1] == 'A']
    total_steps   = [0 for i in range(len(current_entry))]
    for i, entry in enumerate(current_entry):
        for instruction in instructions:
            total_steps[i] += 1
            if instruction == 'L':
                entry = map_dict[entry][0]
            else:
                entry = map_dict[entry][1]
            if entry[-1] == 'Z':
                print('reached')
                break
    print(math.lcm(*total_steps))  # Least Common Multiple

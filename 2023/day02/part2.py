import re


def get_power_of_game(line):
    game, sets = line.split(':')
    sets = sets.split(';')
    red_counter_max   = 0
    green_counter_max = 0
    blue_counter_max  = 0
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            if 'red' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > red_counter_max:
                    red_counter_max = counter
            if 'green' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > green_counter_max:
                    green_counter_max = counter
            if 'blue' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > blue_counter_max:
                    blue_counter_max = counter
    power = red_counter_max * green_counter_max * blue_counter_max
    return power


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    total_sum = 0
    for d in data:
        total_sum += get_power_of_game(d)
    print(total_sum)
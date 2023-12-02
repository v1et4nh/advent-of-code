import re


def get_possible_id(line):
    game, sets = line.split(':')
    sets = sets.split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            if 'red' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > 12:
                    return 0
            if 'green' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > 13:
                    return 0
            if 'blue' in cube:
                counter = list(map(int, re.findall(r'\d+', cube)))[0]
                if counter > 14:
                    return 0
    game_id = list(map(int, re.findall(r'\d+', game)))[0]
    return game_id


if __name__ == '__main__':
    puzzle_input = open('puzzle_input_example.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        total_sum += get_possible_id(line)
    print(total_sum)
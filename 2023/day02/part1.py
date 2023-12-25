import re


def get_possible_id(text_line):
    game, sets = text_line.split(':')
    sets = sets.split(';')
    for subset in sets:
        cubes = subset.split(',')
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
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    total_sum = 0
    for d in data:
        total_sum += get_possible_id(d)
    print(total_sum)
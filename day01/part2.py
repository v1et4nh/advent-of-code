import re


def get_first_and_last_digit(str_line):
    str_line = str_line.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three')\
        .replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six')\
        .replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')

    list_num = list(map(int, re.findall(r'\d', str_line)))
    str_num = str(list_num[0]) + str(list_num[-1])
    return int(str_num)


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        total_sum += get_first_and_last_digit(line)
    print(total_sum)
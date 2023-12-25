import re


def get_first_and_last_digit(str_line):
    list_num = list(map(int, re.findall(r'\d', str_line)))
    str_num  = str(list_num[0]) + str(list_num[-1])
    return int(str_num)


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    total_sum = 0
    for d in data:
        total_sum += get_first_and_last_digit(d)
    print(total_sum)
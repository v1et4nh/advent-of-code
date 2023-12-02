import re
import math
list_valid_inputs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_first_and_last_digit(str_line):
    # Init
    valid_digits  = [-1, -1]
    lowest_index  = math.inf
    highest_index = -math.inf
    first_number  = -1
    last_number   = -1

    # Get Index for text numbers, if there are any
    for count, str_digit in enumerate(list_valid_inputs):
        if str_line.find(str_digit) == -1:
            continue
        if str_line.find(str_digit) < lowest_index:
            lowest_index = str_line.find(str_digit)
            first_number = str(count + 1)
        if str_line.rfind(str_digit) > highest_index:
            highest_index = str_line.rfind(str_digit)
            last_number   = str(count + 1)

    # If index, check for integers before and after the text numbers
    if not math.isinf(lowest_index):
        first_part = str_line[:lowest_index]
        if not list(map(int, re.findall(r'\d', first_part))):
            valid_digits[0] = first_number
    if not math.isinf(highest_index):
        last_part = str_line[highest_index:]
        if not list(map(int, re.findall(r'\d', last_part))):
            valid_digits[1] = last_number

    list_num = list(map(int, re.findall(r'\d', str_line)))
    if valid_digits[0] == -1:
        valid_digits[0] = str(list_num[0])
    if valid_digits[1] == -1:
        valid_digits[1] = str(list_num[-1])

    total_string = valid_digits[0] + valid_digits[-1]
    return int(total_string)


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        searched_digit = get_first_and_last_digit(line)
        total_sum += searched_digit
        print(line + str(searched_digit))
        print('total_sum:' + str(total_sum))
        print('______')
    print(total_sum)
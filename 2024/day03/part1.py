import re

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    text  = ''.join(lines)

    mul_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)

    total = 0
    for m in mul_list:
        total += int(m[0]) * int(m[1])
    print(total)
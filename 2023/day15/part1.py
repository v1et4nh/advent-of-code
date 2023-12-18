def convert_hash(inp_str):
    current_value = 0
    for c in inp_str:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file][0]
    values = lines.split(',')
    total_sum = 0
    for val in values:
        total_sum += convert_hash(val)
    print(total_sum)
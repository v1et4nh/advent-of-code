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
    box = [[] for i in range(256)]
    for val in values:
        if '-' in val:  # remove
            label = val.replace('-', '')
            box_num = convert_hash(label)
            for b in box[box_num]:
                if label in b[0]:
                    box[box_num].remove(b)
                    break
        elif '=' in val:
            label = val.replace('=', ' ')
            box_num = convert_hash(label.split(' ')[0])
            is_replaced = False
            for i, b in enumerate(box[box_num]):
                if label.split(' ')[0] in b[0]:
                    box[box_num][i] = [label]
                    is_replaced = True
            if not is_replaced:
                box[box_num].append([label])

    for i, b in enumerate(box):
        for j, l in enumerate(b):
            focal_len = l[0].split(' ')[-1]
            total_sum += (i+1) * (j+1) * int(focal_len)
    print(total_sum)
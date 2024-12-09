if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    line = lines[0].strip()
    array = []
    id = -1
    for i, el in enumerate(line):
        if i % 2 == 0:
            id += 1
            for _ in range(int(el)):
                array.append(id)
        else:
            for _ in range(int(el)):
                array.append('.')

    # sort
    sorted_array = array.copy()
    for i, e in reversed(list(enumerate(array))):
        if '.' not in sorted_array:
            break
        if e != '.':
            first_free_idx = sorted_array.index('.')
            sorted_array[first_free_idx] = sorted_array.pop(i)
        else:
            sorted_array.pop(i)
            continue
    total = sum([i*el for i, el in enumerate(sorted_array)])
    print(total)
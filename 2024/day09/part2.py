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
    block_size = 1
    block = None
    idx_start = None

    for i, e in reversed(list(enumerate(array))):
        # Get Block Size
        if e != '.':
            if block_size == 1:
                idx_end = i+1
                block = e
            next_el = array[i-1]
            if next_el != block:
                idx_start = i
            else:
                block_size += 1

        # Get first index of available free space
        free_idx = None
        idx = 0
        while idx < len(sorted_array):
            c = 0
            sa = sorted_array[idx]
            if sa == '.':
                while sorted_array[idx + c] == '.':
                    c += 1
            if c >= block_size:
                free_idx = idx
                break
            idx = idx + 1 + c

        # idx_start and free_idx defined -> move
        if idx_start:
            if free_idx and free_idx < idx_start:
                for size in range(block_size):
                    sorted_array[free_idx + size] = sorted_array[idx_end-1-size]
                    sorted_array[(idx_end-1-size)] = '_'
            # Reset
            id -= 1
            block = None
            block_size = 1
            idx_start = None

    total = sum([i*int(el) for i, el in enumerate(sorted_array) if el not in ['.', '_']])
    print(total)
import re

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    text  = ''.join(lines)

    do_match = [0]
    [do_match.append(match.start()) for match in re.finditer('do', text)]
    dont_match = [match.start() for match in re.finditer("don't", text)]
    for dn in dont_match:
        if dn in do_match:
            idx = do_match.index(dn)
            do_match.pop(idx)

    list_start_end = []
    idx      = 0
    dont     = -1
    last_idx = 0
    for do in do_match:
        for idx, dont in enumerate(dont_match):
            if do > dont:
                continue
            if do < dont:
                break
        if do < last_idx:
            continue
        if do > dont:
            dont = len(text) + 1
        list_start_end.append((do, dont+1))
        dont_match = dont_match[idx+1:]
        last_idx = dont

    total = 0
    for d_start, d_end in list_start_end:
        new_l = text[d_start:d_end]
        mul_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", new_l)
        for m in mul_list:
            total += int(m[0]) * int(m[1])
    print(total)
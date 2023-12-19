if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    wf_map = {}
    is_map = True
    rating = []
    for l in lines:
        if l == '':
            is_map = False
            continue
        if is_map:
            k, r = l.split('{')
            r = r.replace('}', '')
            wf_map[k] = r
        else:
            tmp_arr = l.replace('{', '').replace('}', '').split(',')
            tmp_arr = [int(el.split('=')[1]) for el in tmp_arr]
            rating.append(tmp_arr)

    total_sum = 0
    for r in rating:
        is_accepted = False
        is_rejected = False
        current_k = 'in'
        x, m, a, s = r
        while not (is_accepted or is_rejected):
            current = wf_map[current_k].split(',')
            for c in current:
                if ':' in c:
                    cond, res = c.split(':')
                    if eval(cond):
                        if res == 'A':
                            is_accepted = True
                        elif res == 'R':
                            is_rejected = True
                        else:
                            current_k = res
                        break
                else:
                    if c == 'A':
                        is_accepted = True
                    elif c == 'R':
                        is_rejected = True
                    else:
                        current_k = c
                    break
        if is_accepted:
            total_sum += sum(r)

    print(total_sum)
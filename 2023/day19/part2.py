from tqdm import tqdm
import math

if __name__ == '__main__':
    with open('puzzle_input_example.txt', 'r') as file:
        lines = [l.strip() for l in file]

    wf_map = {}
    for l in lines:
        if l == '':
            break
        k, r = l.split('{')
        r = r.replace('}', '')
        wf_map[k] = r

    total_sum = 0
    is_accepted = False
    is_rejected = False
    current_k = 'in'
    range_map = {'x': [1, 4001], 'm': [1, 4001], 'a': [1, 4001], 's': [1, 4001]}
    while not (is_accepted or is_rejected):
        current = wf_map[current_k].split(',')
        for c in current:
            if ':' in c:
                cond, res = c.split(':')
                r_var = cond[0]
                r_val = int(cond[2:])
                sign  = cond[1]
                if sign == '<':
                    range_map[r_var][1] = r_val
                elif sign == '>':
                    range_map[r_var][0] = r_val + 1
                rating = []
                for k in range_map:
                    rating.append(int(range_map[k][1])-int(range_map[k][0]))
                x, m, a, s = rating
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
        total_sum += math.prod(rating)
        # print(total_sum)

    print(total_sum)
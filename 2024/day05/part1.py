from functools import cmp_to_key

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    rules = [el.strip().split('|') for el in lines if '|' in el]
    pages = [el.strip().split(',') for el in lines if ',' in el]


    def cmp_func(r0, r1):
        if [r0, r1] in rules:
            return -1
        if [r1, r0] in rules:
            return 0
        else:
            return 1


    total = 0
    for p in pages:
        sort_p = sorted(p, key=cmp_to_key(cmp_func))
        if sort_p == p:
            total += int(p[int(len(p) / 2)])

    print(total)

if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [el.strip() for el in lines]
    total = 0
    for count, l in enumerate(lines):
        print(f"{count}/{len(lines)}")
        sol, el_list = int(l.split(': ')[0]), l.split(': ')[1]
        el_list = el_list.split(' ')
        el_list = [int(el) for el in el_list]
        tmp_sols = [el_list[0]*el_list[1], el_list[0]+el_list[1], int(str(el_list[0])+str(el_list[1]))]
        new_list = []
        for el in el_list[2:]:
            for tmp_sol in tmp_sols:
                new_list.append(tmp_sol*el)
                new_list.append(tmp_sol+el)
                new_list.append(int(str(tmp_sol)+str(el)))
            tmp_sols = new_list
            new_list = []
        if sol in tmp_sols:
            total += sol
    print(total)
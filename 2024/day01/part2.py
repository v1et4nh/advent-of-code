if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    list_1, list_2 = [], []
    for l in lines:
        tmp = l.split(' ')
        list_1.append(int(int(tmp[0])))
        list_2.append(int(int(tmp[-1].replace('\n', ''))))
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    score = 0
    for l1 in list_1:
        c = list_2.count(l1)
        score += l1 * c
    print(score)

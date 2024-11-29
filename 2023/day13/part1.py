if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    groups = []
    tmp_groups = []
    for l in lines:
        if l != '':
            tmp_groups.append(l)
        else:
            groups.append(tmp_groups)
            tmp_groups = []
    groups.append(tmp_groups)

    total_sum = 0
    for group in groups:
        # horizontal
        is_founded = False
        for i in range(len(group)):
            if is_founded:
                break
            j = 0
            if i+1 == len(group):
                break
            while group[i-j] == group[i+1+j]:
                if i+2+j == len(group):
                    total_sum += 100 * (i+1)
                    is_founded = True
                    break
                j += 1
                if i+1+j == len(group) or i-j == -1:
                    total_sum += 100 * (i+1)
                    is_founded = True
                    break

        # vertical
        if not is_founded:
            for i in range(len(group[0])):
                if is_founded:
                    break
                j = 0
                if i+1 == len(group[0]):
                    break
                while [x[i-j] for x in group] == [x[i+1+j] for x in group]:
                    if i+2+j == len(group[0]):
                        total_sum += i+1
                        is_founded = True
                        break
                    j += 1
                    if i+1+j == len(group[0]) or i-j == -1:
                        total_sum += i+1
                        is_founded = True
                        break
    print(total_sum)
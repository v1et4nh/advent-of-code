if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as file:
        lines = [l.strip() for l in file]

    difference = 1
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
        is_found = False
        for i in range(len(group)):
            if is_found:
                break
            j = 0
            if i+1 == len(group):
                break

            if group[i] == group[i+1] or sum([group[i][l] != group[i+1][l] for l in range(len(group[i]))]) == 1:
                count = 0
                for j in range(len(group)-i-1):
                    if i-j < 0:
                        break
                    if group[i-j] != group[i+1+j]:
                        count += 1
                if count == difference:
                    total_sum += 100 * (i+1)
                    is_found = True

        # vertical
        if not is_found:
            for i in range(len(group[0])):
                if is_found:
                    break
                j = 0
                if i+1 == len(group[0]):
                    break

                if [x[i] for x in group] == [x[i+1] for x in group] \
                        or sum([[x[i] for x in group][l] != [x[i+1] for x in group][l] for l in range(len(group))]) == 1:
                    count = 0
                    for j in range(len(group[0])-i-1):
                        if i-j < 0:
                            break
                        if [x[i-j] for x in group] != [x[i+1+j] for x in group]:
                            count += 1
                    if count == difference:
                        total_sum += i + 1
                        is_found = True
    print(total_sum)
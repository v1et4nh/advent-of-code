if __name__ == '__main__':
    puzzle_input = open('input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [el.strip() for el in lines]
    total_list = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = lines[i][j]
            if current != '.':
                matching = [(idx, s.find(current)) for idx, s in enumerate(lines) if current in s]
                matching.pop(matching.index((i, j)))
                total_list.append((i, j))
                for match in matching:
                    diff = (match[0]-i, match[1]-j)
                    x = 1
                    while True:
                        anti_node = (i-x*diff[0], j-x*diff[1])
                        if 0 <= anti_node[0] < len(lines) and (0 <= anti_node[1] < len(lines[0])):
                            total_list.append(anti_node)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        anti_node = (match[0]+x*diff[0], match[1]+x*diff[1])
                        if 0 <= anti_node[0] < len(lines) and (0 <= anti_node[1] < len(lines[0])):
                            total_list.append(anti_node)
                            x += 1
                        else:
                            break
    total = len(list(set(total_list)))
    print(total)
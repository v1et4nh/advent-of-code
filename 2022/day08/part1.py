if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [l.replace('\n', '') for l in lines]
    map_tree = []
    total_count = 0
    for i, l in enumerate(lines):
        map_tree.append([int(c) for c in l])
    for i in range(len(map_tree)):
        for j in range(len(map_tree[0])):
            if i == 0 or j == 0 or i == len(map_tree)-1 or j == len(map_tree[0])-1:
                total_count += 1
            else:
                tree = map_tree[i][j]
                if all(left < tree for left in map_tree[i][:j]):
                    total_count += 1
                    continue
                if all(right < tree for right in map_tree[i][j+1:]):
                    total_count += 1
                    continue
                if all(top[j] < tree for top in map_tree[:i]):
                    total_count += 1
                    continue
                if all(down[j] < tree for down in map_tree[i+1:]):
                    total_count += 1

    print(total_count)
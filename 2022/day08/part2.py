if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    lines = [l.replace('\n', '') for l in lines]
    map_tree    = []
    total_count = []
    for i, l in enumerate(lines):
        map_tree.append([int(c) for c in l])
    for i in range(len(map_tree)):
        for j in range(len(map_tree[0])):
            if i == 0 or j == 0 or i == len(map_tree)-1 or j == len(map_tree[0])-1:
                continue
            else:
                tree = map_tree[i][j]
                for cl, left in enumerate(reversed(map_tree[i][:j])):
                    if left >= tree:
                        break
                cl += 1
                for cr, right in enumerate(map_tree[i][j+1:]):
                    if right >= tree:
                        break
                cr += 1
                for ct, top in enumerate(reversed(map_tree[:i])):
                    if top[j] >= tree:
                        break
                ct += 1
                for cd, down in enumerate(map_tree[i+1:]):
                    if down[j] >= tree:
                        break
                cd += 1
                total_count.append(cl*cr*ct*cd)

    print(max(total_count))
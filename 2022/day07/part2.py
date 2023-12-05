MAX_SIZE = 100000


class Tree:
    def __init__(self, name, parent=None):
        self.name     = name
        self.children = []
        self.size     = 0
        self.parent   = parent


def recursive_search(node, tmp_size):
    for child in node.children:
        tmp_size += child.size
        if not child.children:
            continue
        else:
            tmp_size = recursive_search(child, tmp_size)
    return tmp_size


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    current_dir = '/'
    dir_dict    = {'/': Tree('/')}
    for line in lines:
        if 'dir ' in line or '$ ls\n' in line or '$ cd /' in line:
            continue
        elif '$ cd' in line:
            dir_name = line.split(' ')[-1].replace('\n', '')
            if '..' in line:
                current_dir = dir_dict[current_dir].parent
            elif dir_name not in dir_dict:
                dir_dict[dir_name] = Tree(dir_name, parent=current_dir)
                dir_dict[current_dir].children.append(dir_dict[dir_name])
                current_dir = dir_name
            else:
                for i in range(999):
                    tmp_dir_name = f"{dir_name}_{i}"
                    if tmp_dir_name not in dir_dict:
                        dir_dict[tmp_dir_name] = Tree(tmp_dir_name, parent=current_dir)
                        dir_dict[current_dir].children.append(dir_dict[tmp_dir_name])
                        current_dir = tmp_dir_name
                        break
                    else:
                        continue
        else:
            size_val = int(line.split(' ')[0])
            dir_dict[current_dir].size += size_val

    for folder in dir_dict:
        tmp_size = dir_dict[folder].size
        tmp_size = recursive_search(dir_dict[folder], tmp_size)
        dir_dict[folder].size = tmp_size

    total_used   = dir_dict['/'].size
    unused_size  = 70000000 - total_used
    min_size_req = 30000000 - unused_size
    valid_size_list = [dir_dict[folder].size for folder in dir_dict if dir_dict[folder].size >= min_size_req]
    print(min(valid_size_list))

def is_overlapped(pairs):
    first, second = pairs.split(',')
    first  = list(range(int(first.split('-')[0]), int(first.split('-')[1])+1))
    second = list(range(int(second.split('-')[0]), int(second.split('-')[1])+1))
    if any(item in second for item in first) or any(item in first for item in second):
        return 1
    else:
        return 0


if __name__ == '__main__':
    puzzle_input = open('puzzle_input.txt', 'r')
    lines = puzzle_input.readlines()
    total_sum = 0
    for line in lines:
        total_sum += is_overlapped(line)
    print(total_sum)
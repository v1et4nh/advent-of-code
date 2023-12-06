puzzle_input_example = [[71530], [940200]]
puzzle_input         = [[48876981], [255128811171623]]

if __name__ == '__main__':
    time_arr, dist_arr = puzzle_input
    possible_arr = []
    for max_t, max_d in zip(time_arr, dist_arr):
        counter = 0
        for i in range(max_t+1):
            speed = i
            dist  = (max_t-i)*speed
            if dist > max_d:
                counter += 1
        possible_arr.append(counter)

    total_sum = 1
    for i in possible_arr:
        total_sum *= i
    print(total_sum)
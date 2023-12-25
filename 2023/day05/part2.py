import re
import math


def get_destination(source, map_lines):
    destination = source
    for line in map_lines:
        line = line.split(' ')
        if source in range(int(line[1]), int(line[1]) + int(line[2])):
            tmp_diff = source - int(line[1])
            destination = int(line[0]) + tmp_diff
    return destination


def get_loca(seed):
    soil = get_destination(seed, seed_to_soil_map)
    fert = get_destination(soil, soil_to_fert_map)
    watr = get_destination(fert, fert_to_watr_map)
    ligh = get_destination(watr, watr_to_ligh_map)
    temp = get_destination(ligh, ligh_to_temp_map)
    humi = get_destination(temp, temp_to_humi_map)
    loca = get_destination(humi, humi_to_loca_map)
    return loca


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data   = data.readlines()
    data   = [d.replace('\n', '') for d in data]
    seeds   = list(map(int, re.findall(r'\d+', data[0])))          # Get list of seeds
    idx_arr = [i+1 for i, d in enumerate(data) if d == '']   # Get start_idx of each map

    # Create maps
    seed_to_soil_map = data[idx_arr[0]+1:idx_arr[1]-1]
    soil_to_fert_map = data[idx_arr[1]+1:idx_arr[2]-1]
    fert_to_watr_map = data[idx_arr[2]+1:idx_arr[3]-1]
    watr_to_ligh_map = data[idx_arr[3]+1:idx_arr[4]-1]
    ligh_to_temp_map = data[idx_arr[4]+1:idx_arr[5]-1]
    temp_to_humi_map = data[idx_arr[5]+1:idx_arr[6]-1]
    humi_to_loca_map = data[idx_arr[6]+1:]

    # find first rough minima within given ranges
    tmp_loca     = math.inf
    search_range = (-1, 1)
    new_seeds    = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for range_val in new_seeds:
        for seed in range_val:
            loca = get_loca(seed)
            if loca < tmp_loca:
                tmp_loca     = loca
                search_range = range_val

    # Use smaller batch_size for each iteration
    batch_size = 1000000000
    while batch_size >= 1:
        print(f'Run {batch_size}: {tmp_loca} | {search_range}')
        tmp_search_range = search_range
        for seed in range(search_range[0], search_range[1], batch_size):
            loca = get_loca(seed)
            if loca <= tmp_loca:
                tmp_loca = loca
                tmp_search_range = (seed-batch_size*2, seed+batch_size*2)
        search_range = tmp_search_range
        batch_size   = batch_size//10

    print(f"Solution: {tmp_loca}")
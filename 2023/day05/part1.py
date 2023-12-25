import re


def get_map(map_lines):
    total_map = {}
    for line in map_lines:
        destination, source, step = line.split(' ')
        for i in range(int(line[2])):
            total_map[int(line[1])+i] = int(line[0])+i
    return total_map


def get_destination(source, map_lines):
    destination = source
    for line in map_lines:
        line = line.split(' ')
        if source in range(int(line[1]), int(line[1]) + int(line[2])):
            tmp_diff = source - int(line[1])
            destination = int(line[0]) + tmp_diff
    return destination


if __name__ == '__main__':
    data = open('puzzle_input.txt', 'r')
    data = data.readlines()
    data = [d.replace('\n', '') for d in data]
    seeds   = list(map(int, re.findall(r'\d+', data[0])))          # Get list of seeds
    idx_arr = [i+1 for i, line in enumerate(data) if line == '']   # Get start_idx of each map

    # Create maps
    seed_to_soil_map = data[idx_arr[0]+1:idx_arr[1]-1]
    soil_to_fert_map = data[idx_arr[1]+1:idx_arr[2]-1]
    fert_to_watr_map = data[idx_arr[2]+1:idx_arr[3]-1]
    watr_to_ligh_map = data[idx_arr[3]+1:idx_arr[4]-1]
    ligh_to_temp_map = data[idx_arr[4]+1:idx_arr[5]-1]
    temp_to_humi_map = data[idx_arr[5]+1:idx_arr[6]-1]
    humi_to_loca_map = data[idx_arr[6]+1:]

    # Find all loca values
    total_loca = []
    for seed in seeds:
        soil = get_destination(seed, seed_to_soil_map)
        fert = get_destination(soil, soil_to_fert_map)
        watr = get_destination(fert, fert_to_watr_map)
        ligh = get_destination(watr, watr_to_ligh_map)
        temp = get_destination(ligh, ligh_to_temp_map)
        humi = get_destination(temp, temp_to_humi_map)
        loca = get_destination(humi, humi_to_loca_map)
        total_loca.append(loca)

    print(min(total_loca))

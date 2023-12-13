# Read data from the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

maps = {
    'seedtosoil': dict(),
    'soiltofertilizer': dict(),
    'fertilizertowater': dict(),
    'watertolight': dict(),
    'lighttotemperature': dict(),
    'temperaturetohumidity': dict(),
    'humiditytolocation': dict(),
}
diretions = ['seedtosoil','soiltofertilizer','fertilizertowater','watertolight','lighttotemperature','temperaturetohumidity','humiditytolocation']


def get_map(name) :
    return maps[name] 

seeds = []

def generate_seed_array(seed_string) :
    numbers_text = seed_string.split(":")[1].strip()
    number_pairs = [list(map(int, numbers_text.split()[i:i+2])) for i in range(0, len(numbers_text.split()), 2)]
    print(number_pairs)
    seeds = []

    for x in number_pairs :
        print(x[1], len(seeds))
        for r in range(1, x[1] + 1) :
            seeds.append(x[0]+r)

    print(len(seeds))
    return seeds

def add_data_to_map(data_line) :
    map_to_update = get_map(current_map)
    data = [int(d) for d in data_line.split() ]
    map_to_update[str(data[1])] = [data[0], data[1], data[2]]

def find_closest_key(input_number, input_dict):
    keys = sorted(map(int, input_dict.keys()))
    for key in reversed(keys):
        if input_number >= key:
            return key
    return -1


def get_location(item) :
    return_data = []
    for level in diretions :
       
        current_dict = maps[level]
        ## Find the key
        key = find_closest_key(item, current_dict)
        if key == -1:
            return_data.append(item)
            continue
        entery_data = current_dict[str(key)]
        if item >= entery_data[1] + entery_data[2] :
            return_data.append(item)
            continue
        diff = item - key
        value = entery_data[0] + diff
        return_data.append(value)       
 
        item = value
    return return_data[-1]
    ## Get soil 



current_map = ''

for line in lines :
    line = line.strip()
    if not line : continue
    if line.startswith('seeds') :
        seeds = generate_seed_array(line)
        continue
    if line.endswith('map:') :
        current_map = line.split()[0].replace('-','')
        continue
    add_data_to_map(line)

locations = []
for x in seeds :
    d = maps['seedtosoil'].get(str(x), x)
    e = get_location(x)
    locations.append(e)

print('part 1', min(locations))




# Print or use the extracted data



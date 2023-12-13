import re

with open('input.txt', 'r') as file:
    data = file.read().split("\n\n")

# Part 1
# Initialize lists to store data
part_1 = []
seeds1 = [int(seed) for seed in data[0][7:].split(" ")]
maps = []

# Process each line in data
for index, value in enumerate(data):
    # we have already added the seeds into seeds1
    if index == 0:
        continue

    # Extract mappings from each line
    mapping_data = re.sub("^.*:\n", "", value, 1).split("\n")
    
    # Convert strings to lists of integers
    mappings = [[int(r) for r in row.split(" ")] for row in mapping_data]
    
    # Append mappings to the maps list
    maps.append(mappings)

# Loop over the seeds
for seed in seeds1:
    # Then we loop over the mappings
    for step in range(len(maps) ):
        for destination, source_start, range_length in maps[step]:
            # Check if the seed is inside current mapping 
            if source_start <= seed < source_start + range_length:
                seed = destination + (seed - source_start)
                break

    # Adding the new seed value to the first task
    part_1.append(seed)

# Find the minimum value in part_1
part_1_min = min(part_1)

# Part 2 
couter = 0
seeds2 = []
part_2 = []

# Create ranges from seeds1
while couter < len(seeds1):
    seeds2.append(range(seeds1[couter], seeds1[couter] + seeds1[couter + 1]))
    couter += 2

# Location is the last element in maps 
locations = maps[-1]

#Sort by first element in tuple
locations.sort(key=lambda x: x[0])
location = 0

def fuck_it(location: int) -> bool:
    for step in range(6, -1, -1):
        for dimensions in maps[step]:
            if location >= dimensions[0] and location < dimensions[0]+dimensions[2]: 
                location = dimensions[1] + (location - dimensions[0])
                break
    for seed in seeds2:
        if location in seed: 
            return True
    return False
while True:
    if not fuck_it(location): location+=1
    else: part_2 = location; break

print(part_1_min, part_2)
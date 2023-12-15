import re
import math

with open('input.txt') as file :
    lines = file.readlines()

directions = []
map_dict = {}
current_nodes = []

def parse_line(line) :
    parts = line.split('=')
    key = parts[0].strip()
    values = re.sub(r'[() ]', '', parts[1].strip() ).split(',')
    return key,values


for counter, line in enumerate(lines):
    line = line.strip()
    if not line : continue
    if counter == 0 :
        directions = [int(char) for char in line.replace('L','0').replace('R','1').strip()]
    else :
        key, values = parse_line(line)
        if str(key).endswith('A') : current_nodes.append(key)
        map_dict[key] = values


def get_new_nodes(directions, current_node) :
    for i in directions :
        current_node = map_dict[current_node][i] 
    return current_node

steps = 0
steps_needed = []

print(current_nodes)

while len(current_nodes) > 0:
    new_nodes = []
    steps += len(directions)
    for cn in current_nodes :
        new_node = get_new_nodes(directions, cn)

        if new_node[-1] == 'Z':
            steps_needed.append(steps)
        else:
            new_nodes.append(new_node)
    current_nodes = new_nodes

    
print('number of steps', math.lcm(*steps_needed ) )

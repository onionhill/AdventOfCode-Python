import re
with open('input.txt') as file :
    lines = file.readlines()

directions = []

def parse_line(line) :
    parts = line.split('=')
    key = parts[0].strip()
    values = re.sub(r'[() ]', '', parts[1].strip() ).split(',')
    return key,values

map_dict = {}

for counter, line in enumerate(lines):
    line = line.strip()
    if not line : continue
    if counter == 0 :
        directions = [int(char) for char in line.replace('L','0').replace('R','1').strip()]
    else :
        key, values = parse_line(line)
        map_dict[key] = values

current = 'AAA'
goal = 'ZZZ'

steps = 0
while True:
    d = directions[steps % len(directions)]
    current = map_dict[current][d]
    print('current', current)
    steps+=1
    if current == goal : break
    if steps > 1_000_000 : break ## failsafe
print('number of steps', steps)

# https://adventofcode.com/2023/day/10
with open('input.txt') as file :
    lines = file.readlines()

grid = []
for y, line in enumerate(lines):
    grid.append(line)

    start_location = line.find('S')
    if start_location >= 0:
        start_x, start_y = start_location, y

x, y, steps = start_x, start_y, 0

if y > 1 and grid[y - 1][x] in {'|', 'F', '7'}:
    direction = 'U'
elif x < len(grid[0]) - 1 and grid[y][x + 1] in {'-', 'J', '7'}:
    direction = 'R'
elif y < len(grid) - 1 and grid[y + 1][x] in {'|', 'J', 'L'}:
    direction = 'D'
elif x > 0 and grid[y][x - 1] in {'-', 'F', 'L'}:
    direction = 'L'

while True:
    if direction  == 'U' :
        y-= 1
    elif direction == 'R' :
        x+= 1
    elif direction == 'D' :
        y+= 1
    elif direction == 'L' :
        x-= 1


    match grid[y][x]:
        case 'L':
            if direction == 'D' :
                direction = 'R'
            else:
                direction = 'U'
        case 'J':
            if direction == 'D' :
                direction = 'L'
            else:
                direction = 'U'
        case '7':
            if direction == 'R' :
                direction = 'D'
            else :
                direction = 'L'
        case 'F':
            if direction == 'L':
                direction = 'D'
            else:
                direction = 'R'
    steps += 1
    if start_x == x and start_y == y:
        print(steps // 2 + (1 if steps % 2 == 1 else 0))
        quit()
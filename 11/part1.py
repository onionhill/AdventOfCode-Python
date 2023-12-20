# https://adventofcode.com/2023/day/10
with open('sample.txt') as file :
    lines = file.readlines()

def expand_universe(grid) :
    new_grid = []
    ## Adding empty lines
    for row in grid:
        new_grid.append(row.strip())
        if '#' not in row:
            new_grid.append('.' * (len(row) -1) )
    ## Adding all columns
    empty_cols = [i for i, row in enumerate(zip(*new_grid)) if all(char == '.' for char in row)]

    while(empty_cols ) :
        col = empty_cols.pop()
        for x, row in enumerate(new_grid) :
            print('row', len(row))
            new_grid[x] = row[:col] + '.' + row[col:]

    counter = 1
    for i in range(len(new_grid)):
        while '#' in new_grid[i]:
            new_grid[i] = new_grid[i].replace('#', str(counter), 1)
            counter += 1
    return new_grid

universe =  expand_universe(lines) 
for x in universe :
    print(x)

print(universe)
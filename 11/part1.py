# https://adventofcode.com/2023/day/10
with open('sample.txt') as file :
    lines = file.readlines()


def find_distance(c1, c2) : 
    print( abs(c2[0] - c1[0]), abs(c2[1] - c1[1]) )
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

def expand_universe(grid, expander) :
    new_grid = []
    ## Adding empty lines
    for row in grid:
        new_grid.append(row.strip())
        if '#' not in row:
            new_grid.extend(['.' * (len(row) - 1) for _ in range(expander-1)])
    ## Adding all columns
    empty_cols = [i for i, row in enumerate(zip(*new_grid)) if all(char == '.' for char in row)]
    while(empty_cols ) :
        col = empty_cols.pop()
        for x, row in enumerate(new_grid) :
            new_grid[x] = row[:col] + '.' * (expander-1) + row[col:]
    return new_grid

def map_hash(matrix) :
    number_dict = dict()
    counter = 1
    
    for y,row in enumerate(matrix) :
        for x, char in enumerate(row) :
            if char == '#' :
                number_dict[counter] = (x,y)
                counter += 1

    return number_dict

universe =  expand_universe(lines,10) 
stars = map_hash(universe)
sum_distance = 0

for key, value in stars.items() :
    for key2 in range(key +1, max(stars) + 1) :
        sum_distance += find_distance(value, stars[key2])
        
print('part 1' ,sum_distance)


 


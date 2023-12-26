# https://adventofcode.com/2023/day/10
with open('input.txt') as file :
    lines = file.readlines()


def find_distance(c1, c2, empty_rows, empty_cols, expander) : 
    ## check in there should be an empty row between this

    empty_row_between = sum(1 for number in range(min(c1[1],c2[1]), max(c1[1],c2[1]) + 1) if number in empty_rows)
    empty_cols_between = sum(1 for number in range(min(c1[0],c2[0]), max(c1[0],c2[0]) +1) if number in empty_cols)
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1]) + (empty_row_between * (expander-1) ) + (empty_cols_between *(expander-1))

def find_empty(grid) :
    empty_rows = []
    ## Adding empty lines
    for x, row in enumerate(grid):
        if '#' not in row:
            empty_rows.append(x)
    empty_cols = [i for i, row in enumerate(zip(*grid)) if all(char == '.' for char in row)]
 
    return empty_rows,empty_cols

def find_stars(matrix) :
    number_dict = dict()
    counter = 1
    
    for y,row in enumerate(matrix) :
        for x, char in enumerate(row) :
            if char == '#' :
                number_dict[counter] = (x,y)
                counter += 1

    return number_dict


empty_rows, empty_cols = find_empty(lines) 

stars = find_stars(lines)
sum_distance = 0


for key, value in stars.items() :
    for key2 in range(key +1, max(stars) + 1) :
        #if key == 3 and key2 == 6 :
        #print(key,key2, find_distance(value, stars[key2], empty_rows, empty_cols,10))
        #print(key, key2,find_distance(value, stars[key2], empty_rows, empty_cols,1))
        #print(key, key2, find_distance(value, stars[key2], empty_rows, empty_cols,10))
        sum_distance += find_distance(value, stars[key2], empty_rows, empty_cols,1_000_000)
        
print('part 2' ,sum_distance)


 


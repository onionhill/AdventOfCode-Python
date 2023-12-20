# https://adventofcode.com/2023/day/10

def read_data() :
    with open('input.txt') as file :
        lines = file.readlines()

    grid = []
    for y, line in enumerate(lines):
        grid.append(list(line.strip()))

        start_location = line.find('S')
        if start_location >= 0:
            start_x, start_y = start_location, y
    
    return grid, start_x, start_y


def generate_grid(grid, x,y) :
    check = [(y, x)] ## 
    seen = {(y, x)} ## List off all 

    s_can_be = {'|', '-', 'L', 'J', '7', 'F'} ## Used to substed out S with the correct value
    
    counter = 0
    while len(check) > 0:
        row,col = check.pop()
        node_value = grid[row][col]
        counter += 1
        ## If this node is a S|LJ we check if the node above send data down
        if (
            row > 0 and 
            node_value in "S|LJ" and 
            grid[row - 1][col] in "|7F" and 
            (row - 1, col) not in seen 
        ):
            seen.add((row -1, col) )
            check.append((row-1, col))
            ## we now that the node above send data down. Then we now that S only can be one of three values
            if node_value == 'S' :
                s_can_be = s_can_be.intersection({'|', 'L', 'J'})

        ## If this node is a S|7F we check the node below
        if (
            row < len(grid) - 1 and 
            node_value in "S|7F" and 
            grid[row + 1][col] in "|LJ" and 
            (row + 1, col) not in seen 
        ):
            seen.add((row + 1, col))
            check.append((row + 1, col))
            if node_value == 'S':
                s_can_be = s_can_be.intersection({'|', '7', 'F'})

        ## If this node is a "S-7J we check the node to the left
        if(
            col > 0 and 
            node_value in "S-7J" and 
            grid[row][col - 1] in "-LF" and 
            (row, col - 1) not in seen
        ):
            seen.add((row, col - 1))
            check.append((row, col - 1))
            if node_value == 'S':
                s_can_be = s_can_be.intersection({'-', '7', 'J'})

        ## If this node is a S-LF we check the node to the right
        if(
            col < len(grid[row]) - 1 and 
            node_value in "S-LF" and 
            grid[row][col + 1] in "-J7" and 
            (row, col + 1) not in seen
        ):
            seen.add((row, col + 1))
            check.append((row, col + 1))
            if node_value == 'S':
                s_can_be = s_can_be.intersection({'-', 'L', 'F'})

    s_value = s_can_be.pop()
    grid[y][x] = s_value
  
    return copy_grid(grid,seen)

## This removes all nodes we have not visited
def copy_grid(g,seen) :
    new_grid = []
    for y in range(len(g)) :
        new_row = []
        for x in range(len(g[y])) :
            if (y,x) not in seen :
                new_row.append('.')
            else:
                new_row.append(g[y][x])
        new_grid.append(new_row)
    return new_grid

#https://en.wikipedia.org/wiki/Point_in_polygon thanks reddit :D 

def part2(grid) :
    solution = 0
    for row in grid :
        for i, value in enumerate(row) :
            if value != '.' :
                continue
            intersections = 0
            corners = []
            for j in range(i+1, len(row)) :
                if row[j] == '|' :
                    intersections += 1
                if row[j] in 'FL' :
                    corners.append(row[j])
                if (
                    len(corners) != 0 and
                    row[j] == "J" and 
                    corners[-1] == "F" or 
                    (row[j] == "7" and corners[-1] == "L" )
                ):
                    corners.pop(-1)
                    intersections += 1
            ## If the number of intersections is a odd number we know its inside
        
            if intersections % 2 == 1:
               # print(row,i, value, intersections)

                solution += 1
    return solution
                

grid, start_x, start_y = read_data()
grid = generate_grid(grid, start_x, start_y)
print(part2(grid))

# Function to read the input file and create a 2D list
from functools import cache
import copy

def read_input_file(file_path):
    rock_map = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            rock_map.append(row)
    return rock_map

# Replace 'input.txt' with the actual path to your input file
file_path = 'input.txt'
rock_map = read_input_file(file_path)
def tilt_north(rock_map): 
    for row in range(1, len(rock_map)):
        for col in range(0, len(rock_map[0])):
            if (rock_map[row][col] == 'O'):
                goFurther = True
                times = row
                while goFurther:
                    if(rock_map[times-1][col] == '.' and times > 0):
                        times = times-1
                    else:
                        goFurther = False
                rock_map[row][col] = '.'
                rock_map[times][col] = 'O'
    return rock_map
def tilt_west(rock_map): 
    for row in range(0, len(rock_map)):
        for col in range(1, len(rock_map[0])):
            if (rock_map[row][col] == 'O'):
                goFurther = True
                times = col
                while goFurther:
                    if times > 0:
                        if(rock_map[row][times-1] == '.'):
                            times = times-1
                        else:
                            goFurther = False
                    else:
                        goFurther = False
                rock_map[row][col] = '.'
                rock_map[row][times] = 'O'
    return rock_map

def tilt_east(rock_map): 
    for row in range(0, len(rock_map)):
        for col in range(len(rock_map[0])-2, -1, -1):
            if (rock_map[row][col] == 'O'):
                goFurther = True
                times = col
                while goFurther:
                    if times+1 < len(rock_map[0]):
                        if rock_map[row][times+1] == '.':
                            times = times+1
                        else:
                            goFurther = False
                    else:
                        goFurther = False
                rock_map[row][col] = '.'
                rock_map[row][times] = 'O'
    return rock_map

def tilt_south(rock_map): 
    for row in range(len(rock_map)-2, -1, -1):
        for col in range(0, len(rock_map[0])):
            if (rock_map[row][col] == 'O'):
                goFurther = True
                times = row
                while goFurther:
                    if times < len(rock_map)-1:
                        if(rock_map[times+1][col] == '.'):
                            times = times+1
                        else:
                            goFurther = False
                    else:
                        goFurther = False
                rock_map[row][col] = '.'
                rock_map[times][col] = 'O'
    return rock_map

def calculatePoints(rock_map):
    points = 0
    for row in range(0, len(rock_map)):
        for col in range(0, len(rock_map[0])):
            if rock_map[row][col] == 'O':
                points += len(rock_map) - row
    return points


# Print the 2D list
result_rock_map = rock_map

loops = []

#Part 1
result_rock_map = tilt_north(result_rock_map)
points = calculatePoints(result_rock_map)
print(f"Part 1 answer is: {points}")


#Part 2
for i in range(0, 1000000000):
    result_rock_map = tilt_north(result_rock_map)
    result_rock_map = tilt_west(result_rock_map)
    result_rock_map = tilt_south(result_rock_map)
    result_rock_map = tilt_east(result_rock_map)
    result_string = ''.join([element for row in result_rock_map for element in row])

    found = False
    for idx, loop in enumerate(loops):
        if (loop == result_string):
            found = (i, idx)

    if found:
        break
    else:
        loops.append(result_string)

if found:
    lam = found[0]-found[1] # loop size
    startedRepetition = found[1]

rock_map = read_input_file(file_path)
for  i in range(0, (1000000000 - startedRepetition) % lam-1):
    result_rock_map = tilt_north(result_rock_map)
    result_rock_map = tilt_west(result_rock_map)
    result_rock_map = tilt_south(result_rock_map)
    result_rock_map = tilt_east(result_rock_map)

points = calculatePoints(result_rock_map)
print(f"Part 2 answer is: {points}")

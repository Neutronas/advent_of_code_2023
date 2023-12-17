from enum import Enum
import copy
import sys

sys.setrecursionlimit(10000)

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove newline characters and create a 2D array
    array_2d = [list(line.strip()) for line in lines]

    return array_2d

file_path = 'input.txt'

cave_map = read_input_file(file_path)

class Direction(Enum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'

light = 0

lightMap = copy.deepcopy(cave_map)

def up(start):
    return tuple([start[0]-1, start[1]])

def right(start):
    return tuple([start[0], start[1]+1])

def down(start):
    return tuple([start[0]+1, start[1]])

def left(start):
    return tuple([start[0], start[1]-1])

scan_info = []
def scanBeam(start, direction):
    # If already went this direction
    if (tuple([start, direction]) not in scan_info):
        scan_info.append(tuple([start, direction]))
    else:
        return False

    # if goes beyond scope
    if start[0] == -1 or start[0] == len(cave_map) or start[1] == -1 or start[1] == len(cave_map[0]):
        return False
    
    lightMap[start[0]][start[1]] = '#'
    currentSymbol = cave_map[start[0]][start[1]]

    if direction == Direction.UP:
        if currentSymbol == '.' or currentSymbol == '|':
            scanBeam(up(start), direction)
        elif currentSymbol == '/':
            scanBeam(right(start), Direction.RIGHT)
        elif currentSymbol == '\\':
            scanBeam(left(start), Direction.LEFT)
        elif currentSymbol == '-':
            scanBeam(left(start), Direction.LEFT)
            scanBeam(right(start), Direction.RIGHT)

    elif direction == Direction.RIGHT:
    
        if currentSymbol == '.' or currentSymbol == '-':
            scanBeam(right(start), direction)
        elif currentSymbol == '/':
            scanBeam(up(start), Direction.UP)
        elif currentSymbol == '\\':
            scanBeam(down(start), Direction.DOWN)
        elif currentSymbol == '|':
            scanBeam(up(start), Direction.UP)
            scanBeam(down(start), Direction.DOWN)
    elif direction == Direction.DOWN:
        if currentSymbol == '.' or currentSymbol == '|':
            scanBeam(down(start), direction)
        elif currentSymbol == '/':
            scanBeam(left(start), Direction.LEFT)
        elif currentSymbol == '\\':
            scanBeam(right(start), Direction.RIGHT)
        elif currentSymbol == '-':
            scanBeam(left(start), Direction.LEFT)
            scanBeam(right(start), Direction.RIGHT)
    elif direction == Direction.LEFT:
        if currentSymbol == '.' or currentSymbol == '-':
            scanBeam(left(start), direction)
        elif currentSymbol == '/':
            scanBeam(down(start), Direction.DOWN)
        elif currentSymbol == '\\':
            scanBeam(up(start), Direction.UP)
        elif currentSymbol == '|':
            scanBeam(up(start), Direction.UP)
            scanBeam(down(start), Direction.DOWN)
        



def count_symbols(array_2d, symbol='#'):
    count = 0
    for row in array_2d:
        count += row.count(symbol)
    return count

max_configuration = 0
for i in range(0, len(cave_map)):
    for j in range(0, len(cave_map[0])):
        if (i == 0):
            scan_info = []
            scanBeam(tuple([i, j]), Direction.DOWN)
            result = count_symbols(lightMap, symbol='#')
            lightMap = copy.deepcopy(cave_map)
            if(result > max_configuration):
                max_configuration = result
        if j == 0:
            scan_info = []
            scanBeam(tuple([i, j]), Direction.RIGHT)
            result = count_symbols(lightMap, symbol='#')
            lightMap = copy.deepcopy(cave_map)
            if(result > max_configuration):
                max_configuration = result
        if j == len(cave_map[0])-1:
            scan_info = []
            scanBeam(tuple([i, j]), Direction.LEFT)
            result = count_symbols(lightMap, symbol='#')
            lightMap = copy.deepcopy(cave_map)
            if(result > max_configuration):
                max_configuration = result
        if i == len(cave_map)-1:
            scan_info = []
            scanBeam(tuple([i, j]), Direction.UP)
            result = count_symbols(lightMap, symbol='#')
            lightMap = copy.deepcopy(cave_map)
            if(result > max_configuration):
                max_configuration = result

print(f"Answer for part2: {max_configuration}")
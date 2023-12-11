def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove newline characters and create a 2D array
    array_2d = [list(line.strip()) for line in lines]
    
    return array_2d

file_path = "input.txt"
galaxies = read_input_file(file_path)

expandedGalaxies = []

def expandGalaxies (galaxies):
    gal = []
    for row in galaxies:
        allDots = True
        count = 0
        for col in row:
            if (col != "."):
                allDots = False
        gal.insert(count, row)
        count +=1
        if allDots:
            gal.insert(count, row)
            count+=1
    return gal

def getExpandedRows(galaxies):
    gal = []
    for row in range(0, len(galaxies)):
        allDots = True
        for col in range(0, len(galaxies[0])):
            if (galaxies[row][col] != "."):
                allDots = False
        if(allDots):
          gal.append(row)
    return gal

def transpose_2d_array(array_2d):
    transposed_array = [list(row) for row in zip(*array_2d)]
    
    return transposed_array

def revert_transpose(transposed_array):
    original_array = [list(row) for row in zip(*transposed_array)]
    return original_array

expandedRows = getExpandedRows(galaxies)

expandedGalaxies = transpose_2d_array(galaxies)
expandedCols = getExpandedRows(expandedGalaxies)
expandedGalaxies = revert_transpose(expandedGalaxies)


for row in range (0, len(expandedGalaxies)):
    expandedGalaxies[row].reverse()

def findGalaxies (galaxies):
    galMap = []
    for row in range(0, len(galaxies)):
        for col in range(0, len(galaxies[0])):
            if galaxies[row][col] == '#':
                galMap.append([row, col])
    return galMap

galMap = findGalaxies(galaxies)

def findMinMoves(a, b, mult):
    countMoves = 0
    if (a[0] > b[0]):
        distanceY = a[0] - b[0]
        curRow = a[0]
    else:
        distanceY = b[0] - a[0]
        curRow = b[0]
    while(distanceY != 0):
        countMoves +=1
        distanceY -=1
        
        if (curRow in expandedRows):
            countMoves += mult-1
        curRow-= 1

    if (a[1] > b[1]):
        distanceX = a[1] - b[1]
        curCol = a[1]
    else:
        distanceX = b[1] - a[1]
        curCol = b[1]

    while(distanceX != 0):
        countMoves +=1
        distanceX -=1
        if (curCol in expandedCols):
            countMoves += mult-1
        curCol-= 1
    return countMoves

totalMoves = 0

for i in range(0, len(galMap)-1):
    for j in range(i, len(galMap)):
        totalMoves += findMinMoves(galMap[i], galMap[j], 1000000)

print(f"Answer for part2: {totalMoves}")

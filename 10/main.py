def read_pipe_map(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.read().splitlines()

            # Create a 2D list from the lines
            pipe_map = [list(line) for line in lines]

            return pipe_map
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

if __name__ == "__main__":
    file_path = "input.txt"  # Change this to the path of your input file
    pipeMap = read_pipe_map(file_path)

def find_character_index(matrix, char):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == char:
                return i, j
    return None


def checkTop(currentPosition):
    if(pipeMap[currentPosition[0]][currentPosition[1]] not in ['|', 'L', 'J', 'S']):
        return None
    y = currentPosition[0]-1
    x = currentPosition[1]
    if pipeMap[y][x] == '|' or pipeMap[y][x] == "7" or pipeMap[y][x] == 'F':
        return [y, x]
    return None

def checkLeft(currentPosition):
    if(pipeMap[currentPosition[0]][currentPosition[1]] not in ['-', 'J', '7']):
        return None
    y = currentPosition[0]
    x = currentPosition[1]-1
    if pipeMap[y][x] == '-' or pipeMap[y][x] == "L" or pipeMap[y][x] == 'F':
        return [y, x]
    return None

def checkRight(currentPosition):
    if(pipeMap[currentPosition[0]][currentPosition[1]] not in ['-', 'L', 'F']):
        return None
    y = currentPosition[0]
    x = currentPosition[1]+1
    if pipeMap[y][x] == '-' or pipeMap[y][x] == "J" or pipeMap[y][x] == '7':
        return [y, x]
    return None

def checkBot(currentPosition):
    if(pipeMap[currentPosition[0]][currentPosition[1]] not in ['|', '7', 'F']):
        return None
    y = currentPosition[0]+1
    x = currentPosition[1]
    if pipeMap[y][x] == '|' or pipeMap[y][x] == "L" or pipeMap[y][x] == 'J':
        return [y, x]
    return None


startingPosition = find_character_index(pipeMap, 'S')

currentPosition = startingPosition

fullMap = []
for i in range(0, 4):
    # fullMap.append([[startingPosition[0], startingPosition[1]]])
    match i:
        case 0:
            if(startingPosition[0] > 0):
                fullMap.append([[startingPosition[0]-1, startingPosition[1]]])
            else:
                break
        case 1:
            if(startingPosition[1] < len(pipeMap[0])-1):
                fullMap.append([[startingPosition[0], startingPosition[1]+1]])
            else:
                break
        case 2:
            if(startingPosition[0] < len(pipeMap)-1):
                fullMap.append([[startingPosition[0]+1, startingPosition[1]]])
            else:
                break
        case 3:
            if(startingPosition[1] > 0):
                fullMap.append([[startingPosition[0], startingPosition[1]-1]])
            else:
                break

    currentPosition = fullMap[i][0]
    SpinLoop = True

    while SpinLoop:
        #checkTop
        if currentPosition[0] > 0:
            top = checkTop(currentPosition)
            if top and top not in fullMap[i]:
                currentPosition = top
                fullMap[i].append(top)
                continue

        #checkBot
        if currentPosition[0] < len(pipeMap)-1:
            bot = checkBot(currentPosition)
            if bot and bot not in fullMap[i]:
                currentPosition = bot
                fullMap[i].append(bot)
                continue

            
        #checkLeft
        if currentPosition[1] > 0:
            left = checkLeft(currentPosition)
            if left and left not in fullMap[i]:
                currentPosition = left
                fullMap[i].append(left)
                continue

        #checkRight
        if currentPosition[1] < len(pipeMap[0])-1:
            right = checkRight(currentPosition)
            if right and right not in fullMap[i]:
                currentPosition = right
                fullMap[i].append(right)
                continue
        
        SpinLoop = False

def retrieveS(path):
    lastCoords = path[-1]
    previousCoords = path[-2]
    lastSymbol = pipeMap[lastCoords[0]][lastCoords[1]]
    nextIsLast = False
    if (lastSymbol == '.'):
        return False
    if (lastSymbol == '|'):
        if previousCoords[0] == lastCoords[0]+1 and lastCoords[0]-1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
        elif lastCoords[0]+1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
    if (lastSymbol == '-'):
        if previousCoords[1] == lastCoords[1]+1 and lastCoords[1]-1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True
        elif lastCoords[1]+1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True
    if (lastSymbol == 'L'):
        if previousCoords[0] == lastCoords[0]-1 and lastCoords[1]+1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True
        elif lastCoords[0]-1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
    if (lastSymbol == 'J'):
        if previousCoords[0] == lastCoords[0]-1 and lastCoords[1]-1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True
        elif lastCoords[0]-1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
    if (lastSymbol == '7'):
        if previousCoords[1] == lastCoords[1]-1 and lastCoords[0]+1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
        elif lastCoords[1]-1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True
    if (lastSymbol == 'F'):
        if previousCoords[1] == lastCoords[1]+1 and lastCoords[0]+1 == startingPosition[0] and lastCoords[1] == startingPosition[1]:
            nextIsLast = True
        elif lastCoords[1]+1 == startingPosition[1] and lastCoords[0] == startingPosition[0]:
            nextIsLast = True

    if(nextIsLast):
        path.append(startingPosition)
        return path
    
    return False

startingPosition = [startingPosition[0], startingPosition[1]]

finalPath = []

for path in fullMap:
    print(f"Path starts and ends with: {path}")
    if(len(path) >= 3):
        finalPath = retrieveS(path)
    if(finalPath):
        break

print(f"Part1: {int(len(finalPath)/2)}")

sum = 0
for i in range(0, len(pipeMap)):
    outside = True
    skip = False
    for j in range(0, len(pipeMap[0])):
        if [i, j] in finalPath:
            if pipeMap[i][j] in ["|", "F", "7"]:
                outside = not outside
        elif (not outside):
            sum+=1

                
print(f"Part 2: {sum}")
        


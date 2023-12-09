
def read_input_file(file_path):
    result_array = []

    with open(file_path, 'r') as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            result_array.append(values)

    return result_array

history = read_input_file("input.txt")

fullMapOfHistory = []

for idx, line in enumerate(history):
    newLine = []
    fullMapOfHistory.append([line])
    allZeroes = False
    currentLine = line
    while (not allZeroes):
        allZeroes = True
        for i in range(len(currentLine)-1, 0, -1):
            newLine.append(currentLine[i] - currentLine[i-1])
            if (currentLine[i] - currentLine[i-1] != 0):
                allZeroes = False
        # print(f"ČIA: {newLine}")
        newLine.reverse()
        # print(f"Current line dabar bus: {newLine}")
        fullMapOfHistory[idx].append(newLine)
        currentLine = newLine
        newLine = []

# sum of last numbers
sumOfLastNumbers = 0
for map in fullMapOfHistory:
    map.reverse()
    for idx, line in enumerate(map):
        if idx == 0:
            line.insert(0, 0)
        else:
            line.insert(0, line[0] - map[idx-1][0])
    print(line)
    sumOfLastNumbers += line[0]

print(f"Answer for Part2 = {sumOfLastNumbers}")

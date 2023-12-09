
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
            line.append(0)
        else:
            line.append(line[len(line)-1] + map[idx-1][len(line)-1])
    sumOfLastNumbers += line[len(line)-1]

print(f"Answer for Part1 = {sumOfLastNumbers}")

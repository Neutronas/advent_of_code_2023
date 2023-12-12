from itertools import combinations

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_line(line):
    symbols, numbers = line.split(' ', 1)
    symbols = list(symbols.strip())
    numbers = list(map(int, numbers.split(',')))
    return symbols, numbers

def process_input(lines):
    springs = []
    defects = []

    for line in lines:
        symbols, numbers = parse_line(line)
        springs.append(symbols)
        defects.append(numbers)

    return springs, defects

file_path = 'input.txt'
lines = read_input(file_path)
springs, defects = process_input(lines)

def checkMatches(row, defects):
    count = 0
    modDefects = defects.copy()
    for charIdx, char in enumerate(row):
        if(char == '#'):
            count += 1 
        elif(count > 0 and count != modDefects[0]):
            count = 0
            return False
        elif(count > 0):
            count = 0
            modDefects.pop(0)
    if(count > 0 and count != modDefects[0]):
        return False
    return True

totalSumOfArrangements = 0
for i, row in enumerate(springs):
    questionMarks = []
    broken = 0
    totalBroken = 0
    arrangements = 0
    for defect in defects[i]:
        totalBroken += defect
    for j, symbol in enumerate(row):
        if (symbol == '?'):
            questionMarks.append([j])
        elif symbol == '#':
            broken += 1
    brokenToAdd = totalBroken - broken
    for variation in combinations(questionMarks, brokenToAdd):
        newRow = row.copy()
        for index in variation:
            # print(index[0])
            newRow[index[0]] = '#'
        newRow = ['.' if element == '?' else element for element in newRow]

        if(checkMatches(newRow, defects[i])):
            arrangements += 1
    totalSumOfArrangements+=arrangements

print(f"Part1: {totalSumOfArrangements}")


import numpy as np

# Read input file
with open('input.txt', 'r') as file:
    # Read the first line and remove newline characters
    input_line = file.readline().strip()

# Split the line into strings using commas as separators
hashChars = input_line.split(',')

# Display the array of hashChars
print("Array of hashChars:", hashChars)

total_sum = 0
boxes = [[] for _ in range(256)]
for string in hashChars:
    current_value = 0
    if '-' in string:
        values = string.split('-')
        current_string = values[0]
        isRemoval = True
    else:
        values = string.split('=')
        current_string = values[0]
        lens = values[1]
        isRemoval = False
    for char in current_string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    if(isRemoval):
        for i in range(len(boxes[current_value])):
            if (i < len(boxes[current_value])):
                if (boxes[current_value][i][0] == current_string):
                    boxes[current_value].pop(i)
    else:
        replaced = False
        for i in range(len(boxes[current_value])):
            if (i < len(boxes[current_value])):
                if (boxes[current_value][i][0] == current_string):
                    boxes[current_value][i] = tuple([current_string, lens])
                    replaced = True
        if not replaced:
            boxes[current_value].append(tuple([current_string, lens]))

# for box in boxes:
#     print(box)
for i, box in enumerate(boxes):
    for j, tup in enumerate(box):
        temp = (i+1)*(j+1)*int(tup[1])
        print(f"{i+1}*{j+1}*{int(tup[1])}")
        print(temp)
        total_sum += (i+1)*(j+1)*int(tup[1])

print(f"Part 2 answer is: {total_sum}")


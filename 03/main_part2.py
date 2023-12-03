# Specify the file name
file_name = 'input.txt'

# Read data from the file
with open(file_name, 'r') as file:
    data = file.read()

# Split the data into rows
rows = data.split('\n')

# Remove empty rows
rows = [row for row in rows if row]

# Create a 2D array
two_d_array = [list(row) for row in rows]

numbers = []
current_number = ''
current_index = None
current_row = None

for row_index, row in enumerate(two_d_array):
    for col_index, char in enumerate(row):
        if char.isdigit():
            if current_number == '':
                current_index = col_index
                current_row = row_index
            current_number += char
        elif current_number:
            numbers.append((int(current_number), current_row, current_index, current_index+ len(str(current_number))))
            current_number = ''
            current_index = None
            current_row = None

# Check for any remaining number at the end of the array
if current_number:
    numbers.append((int(current_number), current_row, current_index, current_index + (len(current_number))))

print(numbers)

rows = len(two_d_array)
cols = len(two_d_array[0])

def left(row, col):
  if (col > 0):
    for number in numbers:
        if (number[1] == row):
          if (number[3] == col):
              return number[0]
  return None

def right(row, col):
  if (col < cols):
    for number in numbers:
        if (number[1] == row):
          if (number[2] == col+1):
              return number[0]
  return None

def range_overlap(range1, range2):
  x1, x2 = range1.start, range1.stop
  y1, y2 = range2.start, range2.stop
  return x1 <= y2 and y1 <= x2

def top(row, col):
  if (row == 0):
     return None
  topNumbers = []
  for number in numbers:
    if (number[1] == row-1):
      for i in range(number[2], number[3]):
         if (i == col-1 or i == col or i == col+1):
            topNumbers.append(number[0])
            break
  if len(topNumbers) > 0:
     return topNumbers
  return None

def bot(row, col):
  if (row == rows):
     return None
  botNumbers = []
  for number in numbers:
    if (number[1] == row+1):
      for i in range(number[2], number[3]):
         if (i == col-1 or i == col or i == col+1):
            botNumbers.append(number[0])
            break            
  if len(botNumbers) > 0:
     return botNumbers
  return None

sumOfMultiplications = 0

for row_index, row in enumerate(two_d_array):
    for col_index, char in enumerate(row):
      goodNumbers = []
      if(char == "*"):
        foundNumber = left(row_index, col_index)
        if(foundNumber != None):
          goodNumbers.append(foundNumber)
        foundNumber = right(row_index, col_index)
        if(foundNumber != None):
          goodNumbers.append(foundNumber)
        foundNumber = top(row_index, col_index)
        if(foundNumber != None):
          goodNumbers += foundNumber
        foundNumber = bot(row_index, col_index)
        if(foundNumber != None):
          goodNumbers += foundNumber
        if (len(goodNumbers) > 1):
          multiplicationResult = 1
          for number in goodNumbers:
             multiplicationResult = multiplicationResult * number
          sumOfMultiplications += multiplicationResult


print(sumOfMultiplications)
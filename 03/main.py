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
            numbers.append((int(current_number), current_row, current_index))
            current_number = ''
            current_index = None
            current_row = None

# Check for any remaining number at the end of the array
if current_number:
    numbers.append((int(current_number), current_row, current_index))

rows = len(two_d_array)
cols = len(two_d_array[0])



def left(number):
  if (number[2]-1 > 0):
    if (two_d_array[number[1]][number[2]-1] != '.'):
      return True
  return False

def right(number):
  numberLength = len(str(number[0]))
  if(number[2]+numberLength < cols):
    if (two_d_array[number[1]][number[2]+numberLength] != '.'):
      return True
  return False

def top(number):
  # Return false immediately if it is top row
  if (number[1] == 0):
     return False
  
  # Check if it's bordering left
  if (number[2]-1 > 0):
    startFrom = number[2]-1
  else:
    startFrom = number[2]
  
  #Check if it's bordering right
  numberLength = len(str(number[0]))
  if(number[2]+numberLength < cols):
     endWith = number[2]+numberLength+1
  else:
    endWith = number[2]+numberLength

  for i in range(startFrom, endWith):
     if (two_d_array[number[1]-1][i] != '.'):
      return True
  return False

def bottom(number):
  # Return false immediately if it is bot row
  if (number[1] == rows-1):
     return False
  
  # Check if it's bordering left
  if (number[2]-1 > 0):
    startFrom = number[2]-1
  else:
    startFrom = number[2]
  
  #Check if it's bordering right
  numberLength = len(str(number[0]))
  if(number[2]+numberLength < cols):
     endWith = number[2]+numberLength+1
  else:
    endWith = number[2]+numberLength
  for i in range(startFrom, endWith):
     if (two_d_array[number[1]+1][i] != '.'):
      return True
  return False

finalNumbersSum = 0
for number in numbers:
  adjacent = False
  numberLength = len(str(number[0]))
  if(left(number)):
      adjacent = True
  if(right(number)):
    adjacent = True
  if(top(number)):
     adjacent = True
  if(bottom(number)):
     adjacent = True
  if adjacent:
    finalNumbersSum += number[0]

print(finalNumbersSum)
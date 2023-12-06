from functools import reduce

# Open the file for reading
with open('input.txt', 'r') as file:
    # Read the lines from the file
    lines = file.readlines()

# Initialize dynamic arrays
holdingTime = []
distance = []

# Loop through the lines and extract values
for line in lines:
    # Split each line into words
    words = line.split()
    
    # Check if the line has values
    if len(words) > 1:
        # Extract numerical values and convert to integers
        values = [int(value) for value in words[1:]]
        
        # Check if the line is for Time or Distance
        if words[0] == 'Time:':
            holdingTime.extend(values)
        elif words[0] == 'Distance:':
            distance.extend(values)

# Print the input
print("holdingTime =", holdingTime)
print("distance =", distance)

def merge_integers(int_list):
    # Convert each integer to a string and join them
    merged_string = ''.join(map(str, int_list))
    
    # Convert the merged string back to an integer
    merged_integer = int(merged_string)
    
    return merged_integer

holdingTime = merge_integers(holdingTime)
distance = merge_integers(distance)

def calculateResult(time, recordToBeat):
  waysToBeatRecord = 0
  for i in range(0, time):
    speed = time - i
    distanceTraveled = speed * i
    if(distanceTraveled > recordToBeat):
        waysToBeatRecord += 1
  return waysToBeatRecord
    



result = calculateResult(holdingTime, distance)
print(result)

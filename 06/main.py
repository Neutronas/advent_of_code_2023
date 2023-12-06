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

def calculateResult(time, recordToBeat):
  waysToBeatRecord = 0
  for i in range(0, time):
    speed = time - i
    distanceTraveled = speed * i
    if(distanceTraveled > recordToBeat):
        waysToBeatRecord += 1
  return waysToBeatRecord
    
waysToBeatRecord = []
for i in range(0, len(holdingTime)):
    waysToBeatRecord.append(calculateResult(holdingTime[i], distance[i]))

result = reduce(lambda x, y: x * y, waysToBeatRecord)
print(result)


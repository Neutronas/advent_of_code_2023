import math

# Initialize variables
instructions = []
mapDictionary = {}

# Read input file
with open("input.txt", "r") as file:
    # Read first line for instructions
    first_line = file.readline().strip()
    instructions = [0 if char == 'L' else 1 for char in first_line]

    # Read remaining lines for map dictionary
    for line in file:
        parts = line.strip().split('=')

        # Ensure the line has expected elements
        if len(parts) == 2:
            key = parts[0].strip()
            values_str = parts[1].strip()

            # Handle values enclosed in brackets
            if values_str.startswith('(') and values_str.endswith(')'):
                values = [val.strip() for val in values_str[1:-1].split(',')]
                
                # Update map_dict
                mapDictionary[key] = values

# find starting positions
currentPositions = []
for position in mapDictionary:
    if(position[2] == 'A'):
        currentPositions.append(position)

currentInstructionStep = 0
  
    
allStepsTaken = []
for currentDestination in currentPositions:
    totalStepsTaken = 0
    while( currentDestination[2] != 'Z'):
        currentDestination = mapDictionary[currentDestination][instructions[currentInstructionStep]]
        totalStepsTaken +=1
        currentInstructionStep += 1
        if currentInstructionStep == len(instructions):
            currentInstructionStep = 0
    allStepsTaken.append(totalStepsTaken)
    print(f"Total steps taken: {totalStepsTaken}")
    
print (math.lcm(*allStepsTaken))
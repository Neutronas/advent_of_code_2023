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

currentDestination = 'AAA'
currentInstructionStep = 0
totalStepsTaken = 0
while( currentDestination != 'ZZZ'):
    currentDestination = mapDictionary[currentDestination][instructions[currentInstructionStep]]
    totalStepsTaken +=1
    currentInstructionStep += 1
    if currentInstructionStep == len(instructions):
        currentInstructionStep = 0
print(f"Total steps taken: {totalStepsTaken}")

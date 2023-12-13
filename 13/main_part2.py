def read_input_file(file_path):
    patterns = []
    current_pattern = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                current_pattern.append(line.strip())
            elif current_pattern:  # Check if current pattern is not empty
                patterns.append(current_pattern)
                current_pattern = []

    # Add the last pattern if there is one at the end of the file
    if current_pattern:
        patterns.append(current_pattern)

    return patterns

file_path = "input.txt"
patterns = read_input_file(file_path)

def transpose_2d_array(array):
    # Use the zip function to transpose the array
    transposed_array = list(map(list, zip(*array)))
    return transposed_array

def calculate_difference(str1, str2):
    # Ensure both strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    # Calculate the difference amount
    difference_count = sum(1 for a, b in zip(str1, str2) if a != b)

    return difference_count

def find_mirror(pattern):
    for idx, line in enumerate(pattern):
        if idx < len(pattern)-1:
            if(idx+1 > len(pattern)-1-idx):
                longer = pattern[:idx+1]
                longer.reverse()
                shorter = pattern[idx+1:]
            else:
                longer = pattern[idx+1:]
                shorter = pattern[:idx+1]
                shorter.reverse()
            foundMirror = True
            mistakes = 0
            for i in range(0, len(shorter)):
                if shorter[i] != longer[i]:
                    if calculate_difference(shorter[i], longer[i]) == 1 and mistakes == 0:
                        mistakes+=1
                    else:
                        foundMirror = False
                        break
            if foundMirror and mistakes == 1:
                return idx+1

    return 0

def inverse(symbol):
    if (symbol) == '.':
        return '#'
    return '.'

totalSum = 0
for i, pattern in enumerate(patterns):
    #search vertical first
    flipped = transpose_2d_array(patterns[i])
    flipped_strings = [''.join(sub_array) for sub_array in flipped]
    vertical = find_mirror(flipped_strings)
    totalSum += vertical
    if(vertical == 0):
        horizontal = find_mirror(patterns[i])
        totalSum += horizontal*100
        
print(f"Total sum is {totalSum}")

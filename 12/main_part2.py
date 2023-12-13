import functools

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_line(line):
    symbols, numbers = line.split(' ', 1)
    # symbols = list(symbols.strip())
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

for idx, row in enumerate(springs):
    row += '?'
    springs[idx] = row*5
    springs[idx] = springs[idx][:-1]

for idx, row in enumerate(defects):
    defects[idx] = row*5


@functools.cache
def calc(record, groups):

    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that we can't fit
            return 0

    # There are more groups, but no more record
    if not record:
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as hashtag
    def hashtag():

        # If the first is a hashtag, then the first n characters must be
        # able to be treated as a hashtag, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc(record[next_group+1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as a dot
    def dot():
        # We just skip over the dot looking for the next hashtag
        return calc(record[1:], groups)

    if next_character == '#':
        # Test hashtag logic
        out = hashtag()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + hashtag()

    else:
        raise RuntimeError

    # print(record, groups, out)
    return out


totalSumOfArrangements = 0

for i, row in enumerate(springs):
    totalSumOfArrangements += calc(row, tuple(defects[i]))

print(f"Part2: {totalSumOfArrangements}")


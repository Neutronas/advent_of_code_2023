def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    data = []
    list_data = None
    for line in lines:
        if 'map:' in line:
            if list_data is not None:
                data.append({'title': title, 'list': list_data})
            parts = line.split('-')
            title = parts[-1].strip()
            list_data = []
        elif 'seeds:' in line:
            seeds = list(map(int, line.split(':')[1].strip().split()))
        elif line.strip():  # check if line is not empty
            list_data.append(list(map(int, line.strip().split())))

    if list_data is not None:
        data.append({'title': title, 'list': list_data})

    return seeds, data



seeds, data = parse_file('input.txt')


seedsRanges = {}
for i in range(0, int(len(seeds)), 2):
    seedsRanges[seeds[i]] = seeds[i+1]
print(seedsRanges)

def eliminate_overlap(seed_ranges):
    sorted_ranges = sorted(seed_ranges.items())

    result = {}
    current_start, current_end = None, None

    for start, length in sorted_ranges:
        if current_end is None or start > current_end:
            # No overlap, add the range as is
            result[start] = length
            current_start, current_end = start, start + length - 1
        else:
            # Overlap, update the range
            overlap = current_end - start + 1
            if overlap < length:
                result[current_start] += length - overlap
                current_end = current_start + result[current_start] - 1

    return result

lowest = None

def removeUsedRanges(migrated, leftovers):
  for i in range(len(migrated)):
      range_beginning_migrated = migrated[i][0]
      range_length_migrated = migrated[i][1]
      range_end_migrated = range_beginning_migrated + range_length_migrated

      # Check if the range in leftovers overlaps with the current range in migrated
      for range_beginning_leftover, range_length_leftover in leftovers.copy().items():
          range_end_leftover = range_beginning_leftover + range_length_leftover

          # Check for overlap
          if (
              range_beginning_leftover < range_end_migrated
              and range_end_leftover > range_beginning_migrated
          ):
              # Calculate the remaining part in leftovers after migration
              remaining_leftover = max(0, range_end_leftover - range_end_migrated)

              # Update the leftovers with the remaining part
              leftovers[range_beginning_leftover] = remaining_leftover

              # If the range is completely consumed, remove it from leftovers
              if remaining_leftover == 0:
                  del leftovers[range_beginning_leftover]

  # Remove the ranges with length 0 from leftovers
  leftovers = {k: v for k, v in leftovers.items() if v != 0}
  return leftovers


def getNewRanges(seedRanges, maps):
  newRanges = {}
  changedMap = {}
  migrated = []
  leftovers = {}
  for seedRange in seedRanges:
    changedMap[seedRange] = False

  for map in maps:
    # If matches fully:
    for seedRange in seedRanges:
      # if seed fully overlaps mapping
      if map[1] >= seedRange and map[1]+map[2] <= seedRange+seedRanges[seedRange]:
            leftovers[seedRange] = map[1] - seedRange
            leftovers[seedRange+map[1]+map[2]] = seedRanges[seedRange] - (map[1]+map[2])
            newRanges[map[0]] = map[2]
            migrated.append([map[1], map[2], map[0], map[2]])
            changedMap[seedRange] = True
      else:
        if( map[1] <= seedRange < map[1] + map[2]) and (map[1] < seedRange+seedRanges[seedRange] <= map[1] + map[2]):
            diff = map[0] - map[1]
            newRanges[seedRange + diff] = seedRanges[seedRange]
            changedMap[seedRange] = True
        # If map starts in the middle of range:
        if (seedRange < map[1]) and (seedRange+seedRanges[seedRange] > map[1]):
            diff = map[0] - map[1]
            rangeDiff = map[1] - seedRange
            leftovers[seedRange] = rangeDiff
            newRanges[seedRange+diff+rangeDiff] = seedRanges[seedRange]-rangeDiff
            migrated.append([seedRange - (seedRange-map[1]), seedRanges[seedRange]-rangeDiff, seedRange+diff+rangeDiff, seedRanges[seedRange]-rangeDiff])
            changedMap[seedRange] = True
        # If map ends in the middle of range
        if (seedRange < map[1]+map[2]) and (seedRange+seedRanges[seedRange] > map[1] + map[2]):
            diff = map[0] - map[1]
            rangeDiff = map[1]+map[2] - seedRange
            newRanges[diff+seedRange] = rangeDiff
            leftovers[seedRange+rangeDiff] = seedRanges[seedRange]-rangeDiff
            migrated.append([seedRange, rangeDiff, diff+seedRange, rangeDiff])
            changedMap[seedRange] = True
  leftovers = removeUsedRanges(migrated, leftovers)
  newRanges.update(leftovers)
  for changed in changedMap:
    if(not changedMap[changed]):
        newRanges[changed] = seedRanges[changed]
  return newRanges

seedRanges = seedsRanges
for item in data:
  seedRanges = getNewRanges(seedRanges, item['list'])

lowest_location = min(seedRanges.keys())

print(f"Lowest location: {lowest_location}")
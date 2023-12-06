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
            # title = line.split('-')[0].strip()
            list_data = []
        elif 'seeds:' in line:
            seeds = list(map(int, line.split(':')[1].strip().split()))
        elif line.strip():  # check if line is not empty
            list_data.append(list(map(int, line.strip().split())))

    if list_data is not None:
        data.append({'title': title, 'list': list_data})

    return seeds, data

def transform_list(lists):
    dictionary = {}
    #converting numbers
    for map in lists:
        currentNumber = 0
        for i in range(map[1], map[1]+map[2]):
            dictionary[i] = map[0]+currentNumber
            currentNumber += 1
    return dictionary


seeds, data = parse_file('input2.txt')
print('Seeds:', seeds)

# for item in data:
#     # print('Title:', item['title'])
#     # print('Original List:', item['list'])
    # item['map'] = transform_list(item['list'])
#     for key in item['map']:
#         print(f"{key}      {item['map'][key]}")

lowest = None
for seed in seeds:
    currentSeed = seed

    for idx, item in enumerate(data):
        for map in item['list']:
            if ( map[1] < currentSeed < map[1] + map[2]):
                diff = currentSeed - map[1]
                currentSeed = map[0] + diff
                break
            elif (map[1] == currentSeed):
                currentSeed = map[0]
                break
        print(f"Seed {seed} _ {item['title']} {currentSeed}")
    if lowest == None:
        lowest = currentSeed
    elif currentSeed < lowest:
        lowest = currentSeed


print(lowest)
def read_lottery_file(file_path):
    winning_list = {}
    lottery_numbers = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            card_number = int(line[0].split()[1])
            
            # Reading winning numbers
            winning_numbers = list(map(int, line[1].split('|')[0].split()))
            winning_list[card_number] = winning_numbers
            
            # Reading ticket numbers
            ticket_numbers = list(map(int, line[1].split('|')[1].split()))
            lottery_numbers[card_number] = ticket_numbers

    return winning_list, lottery_numbers

# Example usage
file_path = 'input.txt'  # Replace with the actual file path
winning_list, lottery_numbers = read_lottery_file(file_path)

# Print the result
for card_number, winning_numbers in winning_list.items():
    print(f"Card {card_number} Winning Numbers: {winning_numbers}")

for card_number, ticket_numbers in lottery_numbers.items():
    print(f"Card {card_number} Ticket Numbers: {ticket_numbers}")

def count_matches(lottery_numbers):
    match_counts = {}

    for card_number, ticket_numbers in lottery_numbers.items():
        matches = sum(1 for number in ticket_numbers if number in winning_list[card_number])
        match_counts[card_number] = matches
        for i in range(0, matches):
            match_counts_number[card_number+i] = matches

    return match_counts

def count_points (matches):
    points = 0
    for i in range(0, matches):
        if (points == 0):
            points = 1
        else:
            points *= 2
    return points

match_counts_number = {}
match_counts = count_matches(lottery_numbers)

total_sum_of_points =  0
# Print the result
for card_number, matches in match_counts.items():
    total_sum_of_points += count_points(matches)
    print(f"Card {card_number} has {count_points(matches)} points.")

print(f"Total sum of points: {total_sum_of_points}")
print(match_counts_number)
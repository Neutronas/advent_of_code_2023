import re

with open('input.txt') as f:
  lines = f.readlines()
sum = 0

for text in lines:
    first_digit = re.search(r"\d", text)
    last_digit=re.search(r'(\d)[^\d]*$', text)
    result = int(text[first_digit.start()] + text[last_digit.start()])
    sum += result

print(sum)
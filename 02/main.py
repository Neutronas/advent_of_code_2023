import re

with open('input.txt') as f:
  lines = f.readlines()

sumOfIds = 0

for line in lines:
  reds, greens, blues = 0, 0, 0
  failingLine = False
  dividedArray = re.findall(r"[\w']+|[.,!?;]", line)

  for i in range(2, len(dividedArray)):
    # print(f"Element at index {i}: {dividedArray[i]}")
    if (dividedArray[i].isdigit()):
      match dividedArray[i+1]:
        case "blue":
          blues = int(dividedArray[i])
        case "red":
          reds = int(dividedArray[i])
        case "green":
          greens = int(dividedArray[i])
      if ((reds > 12) or (greens > 13) or (blues > 14)):
        failingLine = True

  if not failingLine:
    sumOfIds += int(dividedArray[1])

print(sumOfIds)
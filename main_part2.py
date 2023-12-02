import re

with open('input.txt') as f:
  lines = f.readlines()

sumOfIds = 0
finalPowerSum = 0

for line in lines:
  reds, greens, blues = 0, 0, 0
  minReds, minGreens, minBlues = None, None, None
  failingLine = False
  dividedArray = re.findall(r"[\w']+|[.,!?;]", line)

  for i in range(2, len(dividedArray)):
    # print(f"Element at index {i}: {dividedArray[i]}")
    if (dividedArray[i].isdigit()):
      match dividedArray[i+1]:
        case "blue":
          blues = int(dividedArray[i])
          if minBlues == None or minBlues < int(dividedArray[i]):
            minBlues = int(dividedArray[i])
        case "red":
          reds = int(dividedArray[i])
          if minReds == None or minReds < int(dividedArray[i]):
            minReds = int(dividedArray[i])
        case "green":
          greens = int(dividedArray[i])
          if minGreens == None or minGreens < int(dividedArray[i]):
            minGreens = int(dividedArray[i])
      if ((reds > 12) or (greens > 13) or (blues > 14)):
        failingLine = True
  powerSum = 1
  if (minBlues != None):
    powerSum *= minBlues
  if (minReds != None):
    powerSum *= minReds
  if (minGreens != None):
    powerSum *= minGreens
  print(f"Total: {powerSum}")

  if not failingLine:
    sumOfIds += int(dividedArray[1])
  finalPowerSum += powerSum

print(finalPowerSum)
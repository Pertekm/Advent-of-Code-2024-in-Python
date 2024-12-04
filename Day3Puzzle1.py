import re

with open("Day3Puzzle1_Input.txt", "r") as file:
    data = file.read()

sum = 0

multiplyStatements = re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)', data)
for multiplyStatement in multiplyStatements:
    #print(multiplyStatement)
    multiplyNumbers = multiplyStatement.split("(")[1].split(")")[0].split(",")
    #print(numbers)
    multiplyResult = int(multiplyNumbers[0]) * int(multiplyNumbers[1])
    sum += multiplyResult

print("sum:", sum)
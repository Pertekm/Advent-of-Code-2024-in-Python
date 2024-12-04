import re

with open("Day3Puzzle1_Input.txt", "r") as file:
    data = file.read()

sum = 0

matches = re.finditer(r'mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)', data)

mutptiplyIsEnabled = True

for match in matches:
    print(f"Found '{match.group()}' at index {match.start()}")
    
    if(match.group() == "do()"):
        print("do() found")
        mutptiplyIsEnabled = True

    if(match.group() == "don't()"):
        print("don't() found")
        mutptiplyIsEnabled = False
    
    if match.group().startswith("mul"):
        print("mul found")
        if(mutptiplyIsEnabled):
            multiplyNumbers = match.group().split("(")[1].split(")")[0].split(",")
            multiplyResult = int(multiplyNumbers[0]) * int(multiplyNumbers[1])
            sum += multiplyResult

print("sum:", sum)
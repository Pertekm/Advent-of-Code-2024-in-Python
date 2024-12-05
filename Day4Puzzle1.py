import re
import math

with open("Day4Puzzle1_Input.txt", "r") as file:
    data = file.read()

line_length = data.find('\n')
#print(f"line_length: {line_length}")

data = data.replace('\n', '')
count_xmas = 0

xLettersIter = re.finditer(r'X', data)
for xLetterMatch in xLettersIter:
    startIndex1Based = xLetterMatch.start() + 1
    if(startIndex1Based < line_length):
        lineNumber = 1
        position = startIndex1Based
    else:
        lineNumber = math.ceil(startIndex1Based / line_length)
        position = startIndex1Based - line_length * ( lineNumber - 1 )

    #print(f"match X at lineNumber: {lineNumber} at position: {position}")
    #print(f"start index raw: {xLetterMatch.start()} start index 1-based: {startIndex1Based}")

    # check if XMAS is horizontal (left to right)
    if position + 3 <= line_length:  # Ensure there are enough characters remaining in the line
        if data[xLetterMatch.start():xLetterMatch.start() + 4] == "XMAS":
           #print(f"lineNumber: {lineNumber} XMAS is horizontal (left to right) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is horizontal reversed (right to left): SAMX
    if position - 3 > 0:  # Ensure there are enough characters remaining in the line
        if data[xLetterMatch.start()-3:xLetterMatch.start()+1] == "SAMX":
            #print(f"lineNumber: {lineNumber} XMAS is horizontal reversed (right to left) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is vertical (top to bottom)
    if lineNumber + 3 <= len(data) // line_length:  # Ensure there are enough lines remaining
        if (data[xLetterMatch.start()] == 'X' and
            data[xLetterMatch.start() + line_length] == 'M' and
            data[xLetterMatch.start() + 2 * line_length] == 'A' and
            data[xLetterMatch.start() + 3 * line_length] == 'S'):
            #print(f"lineNumber: {lineNumber} XMAS is vertical (top to bottom) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is vertical reversed (bottom to top)
    if lineNumber - 3 > 0:  # Ensure there are enough lines remaining
        if (data[xLetterMatch.start() - 3 * line_length] == 'S' and
            data[xLetterMatch.start() - 2 * line_length] == 'A' and
            data[xLetterMatch.start() - 1 * line_length] == 'M' and
            data[xLetterMatch.start() - 0 * line_length] == 'X'):
            #print(f"lineNumber: {lineNumber} XMAS is vertical reversed (bottom to top) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is diagonal (top-left to bottom-right)
    if lineNumber + 3 <= len(data) // line_length and position + 3 <= line_length:
        if (data[xLetterMatch.start()] == 'X' and
            data[xLetterMatch.start() + 1 * line_length + 1] == 'M' and
            data[xLetterMatch.start() + 2 * line_length + 2] == 'A' and
            data[xLetterMatch.start() + 3 * line_length + 3] == 'S'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal (top-left to bottom-right) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is diagonal (top-right to bottom-left)
    if lineNumber + 3 <= len(data) // line_length and position - 3 > 0:
        if (data[xLetterMatch.start()] == 'X' and
            data[xLetterMatch.start() + 1 * line_length - 1] == 'M' and
            data[xLetterMatch.start() + 2 * line_length - 2] == 'A' and
            data[xLetterMatch.start() + 3 * line_length - 3] == 'S'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal (top-right to bottom-left) starting at position: {position}")
            count_xmas += 1

    # check if XMAS is diagonal reversed (bottom-right to top-left)
    if lineNumber - 3 > 0 and position - 3 > 0:
        if (data[xLetterMatch.start() - 3 * line_length - 3] == 'S' and
            data[xLetterMatch.start() - 2 * line_length - 2] == 'A' and
            data[xLetterMatch.start() - 1 * line_length - 1] == 'M' and
            data[xLetterMatch.start() - 0 * line_length - 0] == 'X'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal reversed (bottom-right to top-left) starting at position: {position}")
            count_xmas += 1
    
    # check if XMAS is diagonal reversed (bottom-left to top-right)
    if lineNumber - 3 > 0 and position + 3 <= line_length:
        if (data[xLetterMatch.start() - 3 * line_length + 3] == 'S' and
            data[xLetterMatch.start() - 2 * line_length + 2] == 'A' and
            data[xLetterMatch.start() - 1 * line_length + 1] == 'M' and
            data[xLetterMatch.start() - 0 * line_length + 0] == 'X'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal reversed (bottom-left to top-right) starting at position: {position}")
            count_xmas += 1

print("count_xmas:", count_xmas)

import re
import math

#with open("Day4Puzzle2_Input_Sample_simplified.txt", "r") as file:
with open("Day4Puzzle1_Input.txt", "r") as file:    
    data = file.read()

line_length = data.find('\n')
#print(f"line_length: {line_length}")

data = data.replace('\n', '')
count_x_mas = 0

aLettersIter = re.finditer(r'A', data)
for aLetterMatch in aLettersIter:
    startIndex1Based = aLetterMatch.start() + 1
    if(startIndex1Based < line_length):
        lineNumber = 1
        position = startIndex1Based
    else:
        lineNumber = math.ceil(startIndex1Based / line_length)
        position = startIndex1Based - line_length * ( lineNumber - 1 )

    found_mas_diagonal_top_left_to_bottom_right = False
    found_mas_diagonal_top_right_to_bottom_left = False
    found_mas_diagonal_reversed_bottom_right_to_top_left = False
    found_mas_diagonal_reversed_bottom_left_to_top_right = False

    # check if X-MAS is diagonal (top-left to bottom-right)
    if lineNumber + 1 <= len(data) // line_length and position + 1 <= line_length and lineNumber - 1 > 0 and position - 1 > 0:
        if (data[aLetterMatch.start()] == 'A' and
            data[aLetterMatch.start() + 1 * line_length + 1] == 'S' and
            data[aLetterMatch.start() - 1 * line_length + -1] == 'M'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal (top-left to bottom-right) starting at position: {position}")
            found_mas_diagonal_top_left_to_bottom_right = True

    # check if X-MAS is diagonal reversed (bottom-right to top-left)
    if lineNumber + 1 <= len(data) // line_length and position + 1 <= line_length and lineNumber - 1 > 0 and position - 1 > 0:
        if (data[aLetterMatch.start()] == 'A' and
            data[aLetterMatch.start() + 1 * line_length + 1] == 'M' and
            data[aLetterMatch.start() - 1 * line_length - 1] == 'S'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal reversed (bottom-right to top-left) starting at position: {position}")
            found_mas_diagonal_reversed_bottom_right_to_top_left = True

    # check if X-MAS is diagonal reversed (bottom-left to top-right)
    if lineNumber + 1 <= len(data) // line_length and position + 1 <= line_length and lineNumber - 1 > 0 and position - 1 > 0:
        if (data[aLetterMatch.start() + 1 * line_length + 1] == 'M' and
            data[aLetterMatch.start() - 1 * line_length - 1] == 'S' and
            data[aLetterMatch.start() - 0 * line_length - 0] == 'A'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal reversed (bottom-left to top-right) starting at position: {position}")
            found_mas_diagonal_reversed_bottom_left_to_top_right = True
    
    # check if X-MAS is diagonal (top-right to bottom-left)
    if lineNumber + 1 <= len(data) // line_length and position + 1 <= line_length and lineNumber - 1 > 0 and position - 1 > 0:
        if (data[aLetterMatch.start() + 1 * line_length + 1] == 'S' and
            data[aLetterMatch.start() - 1 * line_length - 1] == 'M' and
            data[aLetterMatch.start() - 0 * line_length - 0] == 'A'):
            #print(f"lineNumber: {lineNumber} XMAS is diagonal (top-right to bottom-left) starting at position: {position}")
            found_mas_diagonal_top_right_to_bottom_left = True
    
#     if ((found_mas_diagonal_top_left_to_bottom_right and found_mas_diagonal_top_right_to_bottom_left ) or
#       (found_mas_diagonal_reversed_bottom_right_to_top_left and found_mas_diagonal_reversed_bottom_left_to_top_right ) or
#       (found_mas_diagonal_top_left_to_bottom_right and found_mas_diagonal_reversed_bottom_left_to_top_right ) or
#       (found_mas_diagonal_top_right_to_bottom_left and found_mas_diagonal_reversed_bottom_right_to_top_left )):

    if ((found_mas_diagonal_top_left_to_bottom_right or found_mas_diagonal_reversed_bottom_right_to_top_left ) and
       (found_mas_diagonal_top_right_to_bottom_left or found_mas_diagonal_reversed_bottom_left_to_top_right )):
         count_x_mas += 1

print("count_x_mas:", count_x_mas, " 2767 is WRONG!!!, to high :(")

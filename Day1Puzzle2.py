with open("Day1Puzzle1_Input.txt", "r") as file:
    data = file.read()

numbersLeft = []
numbersRight = []

for lineIndex, line in enumerate(data.splitlines(), start=1):
    # print("line " + str(lineIndex) + ": " + line)
    numbers = line.split()
    # print("numbers:", numbers)
    numberLeft = numbers[0]
    numberRight = numbers[1]
    #print("numberLeft:", numberLeft, " numberRight:", numberRight)
    numbersLeft.append(int(numberLeft))
    numbersRight.append(int(numberRight))

totalSimilarityScore = 0

for numberLeftIndex, numberLeft in enumerate(numbersLeft):
    countNumber = numbersRight.count(numbersLeft[numberLeftIndex])
    totalSimilarityScore += numbersLeft[numberLeftIndex] * countNumber
   
print("totalSimilarityScore:", totalSimilarityScore)